"""Tier classification.

Per-document tier (T0..T3) is determined ONLY by the document's own size:

    T0  < 12_000           → full.md
    T1  12_000 ..  80_000  → full.md + outline.md
    T2  80_000 .. 350_000  → full.md + outline.md + chapters/
    T3  > 350_000          → same outputs as T2, but with stricter chapter
                             budgets (target 8–12K, hard max 25K)

Whether a *software* needs a top-level ``<software>/index.md`` router is a
separate decision (see ``software_needs_router``) driven by aggregate size or
the presence of any T3 document. Small docs inside a router-required
software are still T0/T1/T2 by their own size — they do not get force-promoted
into T3 chapter splitting.
"""
from __future__ import annotations

from typing import Literal

Tier = Literal["T0", "T1", "T2", "T3"]

T0_MAX = 12_000
T1_MAX = 80_000
T2_MAX = 350_000
SOFTWARE_TOTAL_FOR_ROUTER = 500_000


def classify(doc_tokens: int) -> Tier:
    """Return tier for a single document, based on its own token count."""
    if doc_tokens > T2_MAX:
        return "T3"
    if doc_tokens > T1_MAX:
        return "T2"
    if doc_tokens > T0_MAX:
        return "T1"
    return "T0"


def software_needs_router(
    total_tokens: int,
    doc_tiers: list[Tier],
) -> bool:
    """A software requires a ``<software>/index.md`` router when:
       - total estimated tokens across all docs > 500_000, OR
       - any single doc is T3.
    """
    if total_tokens > SOFTWARE_TOTAL_FOR_ROUTER:
        return True
    return any(t == "T3" for t in doc_tiers)


def outputs_for_tier(tier: Tier) -> list[str]:
    """List of output artefact basenames a tier requires under ``<doc>/``."""
    if tier == "T0":
        return ["full.md"]
    if tier == "T1":
        return ["full.md", "outline.md"]
    # T2 / T3 both require chapter splits.
    return ["full.md", "outline.md", "chapters/"]
