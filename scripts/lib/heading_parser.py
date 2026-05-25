"""Parse markdown heading structure into a tree.

Headings inside fenced code blocks (``` ... ``` or ~~~ ... ~~~) are ignored.
Skipped levels are tolerated: H1 → H3 attaches H3 as child of nearest
ancestor (the H1).

Returns a virtual root with level=0. Each ``HeadingNode`` carries:
    - ``level``    1..6
    - ``title``    raw heading text (no leading ``#`` characters)
    - ``line``     1-indexed line number in the source markdown
    - ``page``     PDF page anchored just before this heading (from
                   ``<!-- page:N -->``), or None if no anchor seen yet
    - ``children`` list of child HeadingNode
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_FENCE = re.compile(r"^(```|~~~)")
_PAGE_ANCHOR = re.compile(r"^<!--\s*page:(\d+)\s*-->\s*$")


@dataclass
class HeadingNode:
    level: int
    title: str
    line: int  # 1-indexed
    page: Optional[int] = None
    children: List["HeadingNode"] = field(default_factory=list)


def parse_headings(md_text: str) -> HeadingNode:
    """Parse ``md_text`` into a heading tree. Returns a virtual root."""
    root = HeadingNode(level=0, title="", line=0)
    # Stack of (level, node). Root sits at index 0.
    stack: list[HeadingNode] = [root]

    in_fence = False
    current_page: Optional[int] = None

    for lineno, line in enumerate(md_text.splitlines(), start=1):
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        anchor_match = _PAGE_ANCHOR.match(line)
        if anchor_match:
            current_page = int(anchor_match.group(1))
            continue

        m = _HEADING.match(line)
        if not m:
            continue

        level = len(m.group(1))
        title = m.group(2).strip()
        node = HeadingNode(level=level, title=title, line=lineno, page=current_page)

        # Pop until parent's level < this node's level.
        while stack and stack[-1].level >= level:
            stack.pop()
        if not stack:
            stack.append(root)
        stack[-1].children.append(node)
        stack.append(node)

    return root


def flatten(root: HeadingNode) -> list[HeadingNode]:
    """Return all non-root nodes in document order."""
    out: list[HeadingNode] = []

    def _walk(n: HeadingNode) -> None:
        for child in n.children:
            out.append(child)
            _walk(child)

    _walk(root)
    return out
