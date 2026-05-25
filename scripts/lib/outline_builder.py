"""Build ``outline.md`` for T1+ documents.

Outline is **navigation only** — never the source of factual claims.
Content (per heading, depth ≤ 3 by default):

    - heading title with anchor link
    - PDF page range (from nearest page anchors)
    - first-paragraph extract (≤ 240 chars), trimmed
    - sub-heading list (one level deeper, titles only)
    - top keywords harvested from the section body (proper-noun-ish tokens
      and code-fenced identifiers, deduplicated)

The whole outline targets 1K–3K tokens for typical T1 docs. For very large
T2/T3 docs we keep depth at 2 to control size; depth bumps to 3 for smaller
ones.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from heading_parser import HeadingNode, parse_headings
from token_estimator import estimate_tokens

_PAGE_ANCHOR = re.compile(r"<!--\s*page:(\d+)\s*-->")
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_INLINE_CODE = re.compile(r"`([^`\n]{2,40})`")
_IDENT = re.compile(r"\b([A-Z][A-Za-z0-9_]{2,}|[a-z_][a-zA-Z0-9_]{3,})\b")
_HEADING_LINE = re.compile(r"^#{1,6}\s")

# Common English stopwords + markdown / TCAD chrome we don't want as keywords.
_STOP = frozenset(
    """
    the and for with from this that have will been into when then than them they
    your there here also which while where what about over under such only most
    each any all not but yet shall does done made make like used uses using user
    note see also example examples figure figures table tables chapter chapters
    section sections page pages following above below following return returns
    type types value values default defaults true false none null option options
    parameter parameters command commands input output inputs outputs file files
    name names list lists set sets get gets number numbers function functions
    must should would could might may can if in is it of on or to be we us at by
    """.split()
)


@dataclass
class _SectionBody:
    start_line: int  # 1-indexed inclusive
    end_line: int  # 1-indexed exclusive
    first_paragraph: str
    page_start: int | None
    page_end: int | None
    keywords: list[str]


def _slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len] or "section"


def _harvest_section(lines: list[str], start: int, end: int) -> _SectionBody:
    """Inspect lines[start-1:end-1] (1-indexed semantics). Lines is the full
    document; ``start`` is the heading line number and ``end`` is the next
    sibling-or-ancestor heading's line, or len(lines)+1.
    """
    # Body = lines after the heading itself.
    body_lines = lines[start:end - 1] if end > start else []
    body_text = "\n".join(body_lines)

    # Page range from anchors inside this section (or just before).
    pages: list[int] = []
    # Look back up to 5 lines for the nearest anchor that announces this section.
    for i in range(max(0, start - 6), start - 1):
        m = _PAGE_ANCHOR.search(lines[i])
        if m:
            pages.append(int(m.group(1)))
    for ln in body_lines:
        for m in _PAGE_ANCHOR.finditer(ln):
            pages.append(int(m.group(1)))
    page_start = min(pages) if pages else None
    page_end = max(pages) if pages else None

    # First paragraph: skip blank lines, take until next blank.
    first_paragraph = ""
    for chunk in _PARAGRAPH_BREAK.split(body_text):
        c = chunk.strip()
        # Skip lines that are entirely page anchors / headings / sub-titles.
        c = "\n".join(
            ln for ln in c.splitlines()
            if ln.strip()
            and not _PAGE_ANCHOR.match(ln.strip())
            and not _HEADING_LINE.match(ln)
        ).strip()
        if c:
            first_paragraph = re.sub(r"\s+", " ", c)
            if len(first_paragraph) > 240:
                first_paragraph = first_paragraph[:237] + "..."
            break

    # Keywords: inline code first (highest signal), then identifier-ish tokens.
    seen: dict[str, int] = {}
    for m in _INLINE_CODE.finditer(body_text):
        k = m.group(1).strip()
        if k and k.lower() not in _STOP:
            seen[k] = seen.get(k, 0) + 3  # weighted higher
    for m in _IDENT.finditer(body_text):
        k = m.group(1)
        if k.lower() in _STOP:
            continue
        # Skip pure lowercase short words.
        if k.islower() and len(k) < 6:
            continue
        seen[k] = seen.get(k, 0) + 1
    keywords = [k for k, _ in sorted(seen.items(), key=lambda kv: -kv[1])[:8]]

    return _SectionBody(
        start_line=start,
        end_line=end,
        first_paragraph=first_paragraph,
        page_start=page_start,
        page_end=page_end,
        keywords=keywords,
    )


def _iter_with_end(nodes: list[HeadingNode], doc_end_line: int) -> Iterable[tuple[HeadingNode, int]]:
    """Yield (node, end_line) where end_line is the start_line of the next
    heading at the same-or-lesser level (i.e. where this section ends).
    """
    for i, node in enumerate(nodes):
        end = doc_end_line + 1
        for j in range(i + 1, len(nodes)):
            if nodes[j].level <= node.level:
                end = nodes[j].line
                break
        yield node, end


def _flatten_to_depth(root: HeadingNode, max_depth: int) -> list[HeadingNode]:
    out: list[HeadingNode] = []

    def _walk(n: HeadingNode) -> None:
        for child in n.children:
            if child.level <= max_depth:
                out.append(child)
                _walk(child)

    _walk(root)
    return out


def build_outline(doc_name: str, md_text: str, full_md_rel: str, max_depth: int = 3) -> str:
    """Generate ``outline.md`` content. ``full_md_rel`` is the relative
    path from the outline.md to the full.md (typically ``./full.md``).
    """
    lines = md_text.splitlines()
    root = parse_headings(md_text)
    nodes_at_depth = _flatten_to_depth(root, max_depth)

    if not nodes_at_depth:
        return (
            f"# {doc_name} — outline\n\n"
            "_No headings detected in the source markdown. "
            f"Grep [`{full_md_rel}`]({full_md_rel}) directly._\n"
        )

    out: list[str] = []
    out.append(f"# {doc_name} — outline\n")
    out.append(
        f"Navigation only. Confirm any claim against [`{full_md_rel}`]({full_md_rel}) "
        "by reading the passage near the cited `<!-- page:N -->` anchor.\n"
    )

    # Pre-compute end lines for sections at every depth using a flat list of all headings.
    all_nodes = sorted(
        _flatten_to_depth(root, max_depth=6),
        key=lambda n: n.line,
    )
    node_end: dict[int, int] = {}
    for i, node in enumerate(all_nodes):
        end = len(lines) + 1
        for j in range(i + 1, len(all_nodes)):
            if all_nodes[j].level <= node.level:
                end = all_nodes[j].line
                break
        node_end[node.line] = end

    # Collect immediate child titles (one level deeper) for each node we render.
    def _child_titles(n: HeadingNode) -> list[str]:
        return [c.title for c in n.children if c.level <= max_depth]

    for node in nodes_at_depth:
        body = _harvest_section(lines, node.line, node_end[node.line])
        indent = "  " * max(0, node.level - 1)
        slug = _slugify(node.title)
        page_str = ""
        if body.page_start is not None:
            if body.page_end and body.page_end != body.page_start:
                page_str = f" _(p.{body.page_start}–{body.page_end})_"
            else:
                page_str = f" _(p.{body.page_start})_"
        out.append(f"{indent}- **{node.title}**{page_str} <a id=\"{slug}\"></a>")
        if body.first_paragraph:
            out.append(f"{indent}  - {body.first_paragraph}")
        if node.level < max_depth:
            kids = _child_titles(node)
            if kids:
                preview = ", ".join(kids[:8])
                if len(kids) > 8:
                    preview += f", … ({len(kids)} total)"
                out.append(f"{indent}  - _Sub:_ {preview}")
        if body.keywords:
            out.append(f"{indent}  - _Keywords:_ {', '.join(body.keywords)}")

    out.append("")  # trailing newline
    return "\n".join(out)


def estimate_outline_tokens(outline_text: str) -> int:
    return estimate_tokens(outline_text)
