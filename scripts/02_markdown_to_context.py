"""Build ``context_layer/`` from ``corpus/markdown/``.

Per-doc inputs:
    corpus/markdown/<software>/<doc>/<doc>.md
    corpus/markdown/<software>/<doc>/<doc>_content_list.json

Per-doc outputs (depend on tier classification from `lib/tier_classifier.py`):
    context_layer/<software>/<doc>/full.md       (T0+)
    context_layer/<software>/<doc>/outline.md    (T1+)
    context_layer/<software>/<doc>/chapters/*.md (T2+, NOT YET IMPLEMENTED in this revision)

Shared output:
    context_layer/manifest.json — tier / token / outputs index for every doc.

T2/T3 status: this revision (M1 partial) emits full.md + outline.md only, the
same as T1, and marks the doc with ``tier_implemented = "T1-as-T2-fallback"``
in the manifest. Proper chapter splitting lands in the next M1 step.

This script is decoupled from minerU: it only reads the two files above.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR / "lib"))

from token_estimator import estimate_tokens  # noqa: E402
from tier_classifier import classify, software_needs_router  # noqa: E402
from page_anchor import inject_anchors, load_content_list, page_count  # noqa: E402
from outline_builder import build_outline  # noqa: E402
import manifest as manifest_mod  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--software",
        required=True,
        help="Software name. Must match a subdirectory of corpus/markdown/.",
    )
    parser.add_argument(
        "--doc",
        default=None,
        help="Process a single doc (subdirectory name). Default: all docs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without writing anything.",
    )
    parser.add_argument(
        "--estimate-only",
        action="store_true",
        help="Just compute tokens / tiers and update manifest; do not write full.md or outline.md.",
    )
    return parser.parse_args()


def find_doc_artifacts(doc_dir: Path) -> tuple[Path | None, Path | None]:
    """Locate the .md and _content_list.json under a doc dir.

    minerU may nest outputs under ``<backend>/`` (auto/, pipeline/, vlm/),
    or write them directly under ``<doc>/``. Find the first non-underscore
    .md whose sibling _content_list.json also exists.
    """
    for md in sorted(doc_dir.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        content_list = md.with_name(md.stem + "_content_list.json")
        if content_list.exists():
            return md, content_list
    return None, None


def process_doc(
    doc_dir: Path,
    software: str,
    dry_run: bool,
    estimate_only: bool,
) -> dict | None:
    """Process one doc. Returns the manifest entry, or None if skipped."""
    doc_name = doc_dir.name
    md_path, content_list_path = find_doc_artifacts(doc_dir)
    if md_path is None or content_list_path is None:
        print(f"[skip] {doc_name}: missing .md or _content_list.json under {doc_dir}", file=sys.stderr)
        return None

    md_text = md_path.read_text(encoding="utf-8")
    content_list = load_content_list(content_list_path)

    # Inject page anchors before estimating tokens — the anchors add tokens too,
    # but the count we care about is what the agent will actually load.
    anchored_md = inject_anchors(md_text, content_list)
    est_tokens = estimate_tokens(anchored_md)
    pages = page_count(content_list)

    # Tier (per-document, based on the doc's own token count).
    tier = classify(est_tokens)

    print(
        f"[scan] {software}/{doc_name}: "
        f"tokens={est_tokens:,} pages={pages} tier={tier}"
    )

    entry: dict = {
        "source_pdf": f"corpus/raw/{software}/{doc_name}.pdf",
        "md_path": str(md_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "content_list_path": str(content_list_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "estimated_tokens": est_tokens,
        "page_count": pages,
        "tier": tier,
        "outputs": {},
    }

    if estimate_only:
        return entry

    out_dir = REPO_ROOT / "context_layer" / software / doc_name
    full_md = out_dir / "full.md"
    outline_md = out_dir / "outline.md"

    if dry_run:
        print(f"[dry-run] write {full_md}")
        if tier != "T0":
            print(f"[dry-run] write {outline_md}")
        return entry

    out_dir.mkdir(parents=True, exist_ok=True)
    full_md.write_text(anchored_md, encoding="utf-8")
    entry["outputs"]["full_md"] = str(full_md.relative_to(REPO_ROOT)).replace("\\", "/")

    if tier != "T0":
        depth_by_tier = {"T1": 3, "T2": 2, "T3": 1}
        outline_text = build_outline(
            doc_name=doc_name,
            md_text=anchored_md,
            full_md_rel="./full.md",
            max_depth=depth_by_tier.get(tier, 2),
        )
        outline_md.write_text(outline_text, encoding="utf-8")
        entry["outputs"]["outline_md"] = str(outline_md.relative_to(REPO_ROOT)).replace("\\", "/")
        entry["outline_estimated_tokens"] = estimate_tokens(outline_text)

    if tier in ("T2", "T3"):
        entry["chapters_pending"] = True  # M1 next step: chapter_splitter

    return entry


def main() -> int:
    args = parse_args()

    md_dir = REPO_ROOT / "corpus" / "markdown" / args.software
    if not md_dir.exists():
        print(
            f"[error] {md_dir} does not exist. Run scripts/01_pdf_to_markdown.py first.",
            file=sys.stderr,
        )
        return 2

    if args.doc:
        doc_dirs = [md_dir / args.doc]
        if not doc_dirs[0].exists():
            print(f"[error] {doc_dirs[0]} not found.", file=sys.stderr)
            return 2
    else:
        doc_dirs = sorted(
            p for p in md_dir.iterdir()
            if p.is_dir() and not p.name.startswith(".")
        )

    if not doc_dirs:
        print(f"[error] no doc subdirectories under {md_dir}", file=sys.stderr)
        return 2

    # First pass: process each doc and accumulate per-software total tokens.
    entries: dict[str, dict] = {}
    for d in doc_dirs:
        entry = process_doc(d, args.software, args.dry_run, args.estimate_only)
        if entry is not None:
            entries[d.name] = entry

    if not entries:
        print(f"[error] no docs processed for {args.software}", file=sys.stderr)
        return 1

    # Per-software aggregates.
    total_tokens = sum(e["estimated_tokens"] for e in entries.values())
    needs_router = software_needs_router(
        total_tokens,
        [e["tier"] for e in entries.values()],
    )

    # Update manifest.
    manifest_path = REPO_ROOT / "context_layer" / "manifest.json"
    manifest = manifest_mod.load(manifest_path)
    manifest_mod.upsert_software(
        manifest,
        args.software,
        {
            "total_estimated_tokens": total_tokens,
            "needs_router": needs_router,
            "router_pending": needs_router,  # M2: write <software>/index.md
            "docs": entries,
        },
    )
    if not args.dry_run:
        manifest_mod.save(manifest, manifest_path)

    # Tier summary.
    by_tier: dict[str, int] = {}
    for e in entries.values():
        by_tier[e["tier"]] = by_tier.get(e["tier"], 0) + 1
    summary = ", ".join(f"{t}={n}" for t, n in sorted(by_tier.items()))
    router_str = "needs_router=yes" if needs_router else "needs_router=no"
    print(
        f"[done] {args.software}: {len(entries)} doc(s), "
        f"total_tokens={total_tokens:,}, {summary}, {router_str}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
