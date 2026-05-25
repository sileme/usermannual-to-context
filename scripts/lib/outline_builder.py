"""Build ``outline.md`` for T1+ documents.

Outline is **navigation only** — never a source of factual claims.

minerU often emits all headings as H1, so the markdown ``#`` level alone is
unreliable. We infer a logical level from the heading text:

    - "Part X", "Chapter N", "Appendix X", "N <Title>"  → 1
    - "N.M <Title>"                                     → 2
    - "N.M.K <Title>"                                   → 3
    - "N.M.K.L <Title>"                                 → 4
    - everything else                                   → 99 (uncategorised)

Filtering happens against the inferred level. When > 70% of headings are
uncategorised (i.e. the doc has no numeric hierarchy at all), we fall back
to treating every heading as level 1.

Token budget cap (tier-specific) protects against pathological cases where
the inferred filter still emits hundreds of entries:

    Render → if exceeds budget, re-render without blurbs → if still over,
    drop level-99 entries → if still over, truncate.

Targets:
    T1  ≤ 3K tokens, max_depth 3
    T2  ≤ 5K tokens, max_depth 2
    T3  ≤ 8K tokens, max_depth 1
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
_FALLBACK_NO_HIERARCHY_RATIO = 0.30  # if < 30% of headings are categorised, treat all as level 1

_LVL4 = re.compile(r"^\d+\.\d+\.\d+\.\d+\s+\S")
_LVL3 = re.compile(r"^\d+\.\d+\.\d+\s+\S")
_LVL2 = re.compile(r"^\d+\.\d+\s+\S")
_LVL1 = re.compile(
    r"^(Part\s+[IVX\d]+|Chapter\s+\d+|Appendix\s+[A-Z0-9]+|\d+\s+[A-Z])",
    re.IGNORECASE,
)


def _infer_level(title: str) -> int:
    t = title.strip()
    if _LVL4.match(t):
        return 4
    if _LVL3.match(t):
        return 3
    if _LVL2.match(t):
        return 2
    if _LVL1.match(t):
        return 1
    return 99


def _slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len] or "section"


def _is_toc_like(text: str) -> bool:
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
class _Entry:
    node: HeadingNode
    inferred_level: int
    end_line: int
    blurb: str
    page_start: int | None
    page_end: int | None


def _build_entries(md_text: str) -> List[_Entry]:
    lines = md_text.splitlines()
    root = parse_headings(md_text)

    flat: List[HeadingNode] = []

    def _gather(n: HeadingNode) -> None:
        for child in n.children:
            flat.append(child)
            _gather(child)

    _gather(root)

    if not flat:
        return []

    entries: List[_Entry] = []
    for i, node in enumerate(flat):
        end = len(lines) + 1
        for j in range(i + 1, len(flat)):
            if flat[j].level <= node.level:
                end = flat[j].line
                break
        body = lines[node.line : end - 1]
        pre = lines[max(0, node.line - 6) : node.line - 1]
        ps, pe = _page_range(body, pre)
        entries.append(
            _Entry(
                node=node,
                inferred_level=_infer_level(node.title),
                end_line=end,
                blurb=_extract_blurb(body),
                page_start=ps,
                page_end=pe,
            )
        )
    return entries


def _render(
    doc_name: str,
    full_md_rel: str,
    entries: List[_Entry],
    *,
    include_blurbs: bool,
    drop_uncategorised: bool,
    treat_all_as_level1: bool,
    max_depth: int,
) -> str:
    out: List[str] = []
    out.append(f"# {doc_name} — outline\n")
    out.append(
        f"Navigation only. Confirm any claim against [`{full_md_rel}`]({full_md_rel}) "
        "by reading the passage near the cited `<!-- page:N -->` anchor.\n"
    )

    for e in entries:
        eff_level = 1 if treat_all_as_level1 else e.inferred_level
        if eff_level > max_depth:
            continue
        if drop_uncategorised and eff_level == 99:
            continue
        indent = "  " * (eff_level - 1) if eff_level != 99 else ""
        page_str = ""
        if e.page_start is not None:
            if e.page_end and e.page_end != e.page_start:
                page_str = f" _(p.{e.page_start}–{e.page_end})_"
            else:
                page_str = f" _(p.{e.page_start})_"
        slug = _slugify(e.node.title)
        out.append(f"{indent}- **{e.node.title}**{page_str} <a id=\"{slug}\"></a>")
        if include_blurbs and e.blurb:
            out.append(f"{indent}  - {e.blurb}")
    out.append("")
    return "\n".join(out)


def build_outline(
    doc_name: str,
    md_text: str,
    full_md_rel: str,
    max_depth: int = 3,
    token_budget: int = 3_000,
) -> str:
    """Generate ``outline.md`` content. Applies graceful degradation if the
    rendered outline exceeds ``token_budget``."""
    entries = _build_entries(md_text)
    if not entries:
        return (
            f"# {doc_name} — outline\n\n"
            f"_No headings detected. Grep [`{full_md_rel}`]({full_md_rel}) directly._\n"
        )

    # Decide whether the doc has a useful numeric hierarchy.
    categorised = sum(1 for e in entries if e.inferred_level != 99)
    has_hierarchy = (categorised / len(entries)) >= _FALLBACK_NO_HIERARCHY_RATIO

    # Strategy ladder: try richest first, fall back if over budget.
    strategies = [
        # (include_blurbs, drop_uncategorised, treat_all_as_level1)
        (True, has_hierarchy, not has_hierarchy),
        (False, has_hierarchy, not has_hierarchy),
        (False, True, False),  # last resort: only categorised entries, titles only
    ]

    for include_blurbs, drop_uncat, force_l1 in strategies:
        text = _render(
            doc_name,
            full_md_rel,
            entries,
            include_blurbs=include_blurbs,
            drop_uncategorised=drop_uncat,
            treat_all_as_level1=force_l1,
            max_depth=max_depth,
        )
        if estimate_tokens(text) <= token_budget:
            return text

    # Final hard truncation: emit categorised + page list, no blurbs.
    return _render(
        doc_name,
        full_md_rel,
        entries,
        include_blurbs=False,
        drop_uncategorised=True,
        treat_all_as_level1=False,
        max_depth=1,
    )


def estimate_outline_tokens(outline_text: str) -> int:
    return estimate_tokens(outline_text)
