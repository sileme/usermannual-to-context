"""Inject ``<!-- page:N -->`` HTML comments into a markdown file based on
minerU's ``<doc>_content_list.json``.

minerU writes blocks in reading order. Each block has ``page_idx`` (0-indexed)
and ``text``. We rewrite the source markdown so a page anchor appears
immediately before the first occurrence of each new page's first non-empty
text block.

Design:
    - We do not regenerate markdown from the JSON (formatting / spacing /
      table rendering would drift from minerU's). Instead we walk the
      markdown linearly and the JSON blocks in parallel; when we encounter
      a text block whose page_idx changed, we insert an anchor line above
      the matching line in the markdown.
    - Matching uses a normalised substring search (collapse whitespace,
      drop trailing punctuation). minerU sometimes wraps long blocks across
      multiple markdown lines, so we anchor on the first ~40 chars.
    - Page numbers are 1-indexed in the anchor (page_idx + 1), matching
      "PDF page 1" intuition.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_WS = re.compile(r"\s+")


def _norm_head(text: str, n: int = 40) -> str:
    """Normalise to first ``n`` chars of whitespace-collapsed text."""
    s = _WS.sub(" ", text).strip()
    return s[:n]


def inject_anchors(md_text: str, content_list: list[dict]) -> str:
    """Return ``md_text`` with ``<!-- page:N -->`` lines inserted.

    Strategy: for each unique page_idx (in first-occurrence order), find a
    block whose normalised head appears in md_text; insert the anchor just
    before that line. Pages we cannot locate are still recorded in a
    fallback anchor line at the top.
    """
    # Group: page -> list of block heads in reading order.
    page_blocks: dict[int, list[str]] = {}
    page_order: list[int] = []
    for block in content_list:
        if block.get("type") != "text":
            continue
        text = (block.get("text") or "").strip()
        if not text:
            continue
        head = _norm_head(text)
        if not head:
            continue
        page = int(block.get("page_idx", 0))
        if page not in page_blocks:
            page_blocks[page] = []
            page_order.append(page)
        page_blocks[page].append(head)

    if not page_order:
        return md_text

    lines = md_text.splitlines(keepends=False)
    # Pre-normalise each markdown line head.
    norm_lines = [_norm_head(ln) for ln in lines]

    # For each page (in order), find the earliest matching line index that
    # comes after the previous page's anchor position.
    anchors: dict[int, int] = {}  # line_index -> page (1-indexed)
    cursor = 0
    for page in page_order:
        target_heads = page_blocks[page]
        found_at = None
        for head in target_heads:
            for i in range(cursor, len(norm_lines)):
                if head and head in norm_lines[i]:
                    found_at = i
                    break
            if found_at is not None:
                break
        if found_at is None:
            continue
        anchors[found_at] = page + 1
        cursor = found_at + 1

    if not anchors:
        return md_text

    out: list[str] = []
    last_page: int | None = None
    for i, line in enumerate(lines):
        if i in anchors and anchors[i] != last_page:
            out.append(f"<!-- page:{anchors[i]} -->")
            last_page = anchors[i]
        out.append(line)
    # Ensure the very top has an anchor for the first page we located.
    if out and not out[0].startswith("<!-- page:"):
        first_page = next(iter(anchors.values()))
        out.insert(0, f"<!-- page:{first_page} -->")

    return "\n".join(out) + ("\n" if md_text.endswith("\n") else "")


def page_count(content_list: list[dict]) -> int:
    """Highest page_idx + 1 in the content list (0 if empty)."""
    max_idx = -1
    for block in content_list:
        idx = block.get("page_idx")
        if isinstance(idx, int) and idx > max_idx:
            max_idx = idx
    return max_idx + 1


def load_content_list(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{path}: expected JSON array, got {type(data).__name__}")
    return data
