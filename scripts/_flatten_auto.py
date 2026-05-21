"""Flatten `auto/` subdirectories under corpus/markdown/<software>/<doc>/.

minerU (both local CLI and cloud API via markdown_merge) currently writes:
    <doc>/auto/<doc>.md
    <doc>/auto/<doc>_content_list.json
    <doc>/auto/images/...

This one-shot script moves everything from <doc>/auto/ up into <doc>/ and
removes the now-empty auto/ directory.  Image references in the markdown are
relative (`images/...`) so they remain valid after the move.

Usage:
    python scripts/_flatten_auto.py                            # all software
    python scripts/_flatten_auto.py --software sentaurus       # single software
    python scripts/_flatten_auto.py --dry-run                  # preview only
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def flatten_one(doc_dir: Path, *, dry_run: bool = False) -> bool:
    """Move contents of `doc_dir/auto/` up into `doc_dir/`, then remove auto/.

    Returns True if this directory had an auto/ that was (or would be) flattened.
    """
    auto_dir = doc_dir / "auto"
    if not auto_dir.is_dir():
        return False

    has_auto = True  # found an auto/ dir — counts even in dry-run

    for item in sorted(auto_dir.iterdir()):
        dest = doc_dir / item.name
        if dest.exists():
            print(f"[skip] {dest} already exists")
            continue
        print(f"[move] {item} -> {dest}")
        if not dry_run:
            shutil.move(str(item), str(dest))

    # Only remove auto/ if it's empty after moving
    remaining = list(auto_dir.iterdir())
    if not remaining:
        print(f"[rm] {auto_dir}")
        if not dry_run:
            auto_dir.rmdir()
    else:
        print(f"[warn] {auto_dir} not empty after move, leaving in place: "
              f"{[p.name for p in remaining]}")

    return has_auto


def flatten_software(markdown_dir: Path, *, dry_run: bool = False) -> int:
    """Flatten all doc dirs under a software's markdown directory.

    Returns count of flattened dirs.
    """
    count = 0
    for doc_dir in sorted(markdown_dir.iterdir()):
        if not doc_dir.is_dir():
            continue
        if doc_dir.name.startswith("."):  # skip .parts etc.
            continue
        if flatten_one(doc_dir, dry_run=dry_run):
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--software", default=None,
                        help="Only flatten this software (default: all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without moving files")
    args = parser.parse_args()

    markdown_root = REPO_ROOT / "corpus" / "markdown"
    if not markdown_root.is_dir():
        print(f"[error] {markdown_root} not found", file=sys.stderr)
        return 1

    total = 0
    software_list = [args.software] if args.software else \
        sorted(d.name for d in markdown_root.iterdir() if d.is_dir())

    for sw in software_list:
        sw_dir = markdown_root / sw
        if not sw_dir.is_dir():
            print(f"[warn] {sw_dir} not found, skipping")
            continue
        print(f"\n== {sw} ==")
        n = flatten_software(sw_dir, dry_run=args.dry_run)
        total += n
        if n == 0:
            print("  (no auto/ directories found)")

    print(f"\nDone. {total} director{'y' if total == 1 else 'ies'} flattened.")
    if args.dry_run:
        print("[dry-run] no files were actually moved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
