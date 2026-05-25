"""Build ``outline.md`` for T1+ documents.

Outline is **navigation only** — never a source of factual claims.

Per-heading rendering (depth controlled by tier):

    - title with page-range hint
    - one short blurb (first non-TOC paragraph, hard-capped at ~140 chars)
    - children rendered as nested bullets at the next depth

We deliberately drop keyword harvesting — proper-noun extraction was capturing
author names and table-of-contents fragments, adding noise.

Depth budget by tier (caller passes ``max_depth``):
    T1  3   (chapters → sections → subsections)
    T2  2   (chapters → sections)
    T3  1   (chapters only)

Targets:
    T1 outline ≤ 3K tokens
    T2 outline ≤ 5K tokens
    T3 outline ≤ 8K tokens
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List

from heading_parser import HeadingNode, parse_headings
from token_estimator import estimate_tokens

_PAGE_ANCHOR = re.compile(r"<!--\s*page:(\d+)\s*-->")
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_HEADING_LINE = re.compile(r"^#{1,6}\s")
_BLURB_MAX = 140
_TOC_DIGIT_RATIO = 0.18


def _slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len] or "section"


def _is_toc_like(text: str) -> bool:
    """Heuristic: lots of digits and dots vs. letters → it's a TOC fragment."""
    if not text:
        return True
    digits = sum(1 for c in text if c.isdigit())
    return (digits / len(text)) >= _TOC_DIGIT_RATIO


def _extract_blurb(body_lines: List[str]) -> str:
    body_text = "\n".join(body_lines)
    for chunk in _PARAGRAPH_BREAK.split(body_text):
        c = "\n".join(
            ln for ln in chunk.splitlines()
            if ln.strip()
            and not _PAGE_ANCHOR.match(ln.strip())
            and not _HEADING_LINE.match(ln)
        ).strip()
        if not c:
            continue
        c = re.sub(r"\s+", " ", c)
        if _is_toc_like(c):
            continue
        if len(c) > _BLURB_MAX:
            c = c[: _BLURB_MAX - 1].rstrip() + "…"
        return c
    return ""


def _page_range(body_lines: List[str], pre_lines: List[str]) -> tuple[int | None, int | None]:
    pages: list[int] = []
    for ln in pre_lines:
        m = _PAGE_ANCHOR.search(ln)
        if m:
            pages.append(int(m.group(1)))
    for ln in body_lines:
        for m in _PAGE_ANCHOR.finditer(ln):
            pages.append(int(m.group(1)))
    if not pages:
        return None, None
    return min(pages), max(pages)


@dataclass
class _Section:
    node: HeadingNode
    end_line: int  # exclusive (next sibling/ancestor heading line, or len+1)


def _walk_sections(root: HeadingNode, doc_end_line: int) -> List[_Section]:
    flat: List[HeadingNode] = []

    def _gather(n: HeadingNode) -> None:
        for child in n.children:
            flat.append(child)
            _gather(child)

    _gather(root)
    out: List[_Section] = []
    for i, node in enumerate(flat):
        end = doc_end_line + 1
        for j in range(i + 1, len(flat)):
            if flat[j].level <= node.level:
                end = flat[j].line
                break
        out.append(_Section(node=node, end_line=end))
    return out


def _render_node(
    node: HeadingNode,
    sections_by_line: dict[int, _Section],
    lines: List[str],
    max_depth: int,
    indent_level: int,
    out: List[str],
) -> None:
    section = sections_by_line[node.line]
    body_lines = lines[node.line : section.end_line - 1]
    pre_window = lines[max(0, node.line - 6) : node.line - 1]
    page_start, page_end = _page_range(body_lines, pre_window)
    blurb = _extract_blurb(body_lines)

    indent = "  " * indent_level
    page_str = ""
    if page_start is not None:
        if page_end and page_end != page_start:
            page_str = f" _(p.{page_start}–{page_end})_"
        else:
            page_str = f" _(p.{page_start})_"
    slug = _slugify(node.title)
    out.append(f"{indent}- **{node.title}**{page_str} <a id=\"{slug}\"></a>")
    if blurb:
        out.append(f"{indent}  - {blurb}")

    if node.level >= max_depth:
        return
    for child in node.children:
        if child.level > max_depth:
            continue
        _render_node(child, sections_by_line, lines, max_depth, indent_level + 1, out)


def build_outline(doc_name: str, md_text: str, full_md_rel: str, max_depth: int = 3) -> str:
    """Generate ``outline.md`` content. ``full_md_rel`` is the relative path
    from outline.md to full.md (typically ``./full.md``).
    """
    lines = md_text.splitlines()
    root = parse_headings(md_text)

    if not root.children:
        return (
            f"# {doc_name} — outline\n\n"
            f"_No headings detected. Grep [`{full_md_rel}`]({full_md_rel}) directly._\n"
        )

    sections = _walk_sections(root, len(lines))
    sections_by_line = {s.node.line: s for s in sections}

    out: List[str] = []
    out.append(f"# {doc_name} — outline\n")
    out.append(
        f"Navigation only. Confirm any claim against [`{full_md_rel}`]({full_md_rel}) "
        "by reading the passage near the cited `<!-- page:N -->` anchor.\n"
    )

    for top in root.children:
        if top.level > max_depth:
            continue
        _render_node(top, sections_by_line, lines, max_depth, 0, out)

    out.append("")
    return "\n".join(out)


def estimate_outline_tokens(outline_text: str) -> int:
    return estimate_tokens(outline_text)
