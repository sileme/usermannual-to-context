"""One-shot: split all sentaurus PDFs >200 pages into parts <=200 pages.
Skips PDFs that already have the correct number of part files.
"""
import sys
from pathlib import Path
import pymupdf

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.pdf_split import split_pdf

raw_dir = REPO_ROOT / "corpus" / "raw" / "sentaurus"
out_dir = REPO_ROOT / "corpus" / "markdown" / "sentaurus"
max_pages = 200

pdfs = sorted(raw_dir.glob("*.pdf"))
split_count = 0
skipped = 0

for pdf in pdfs:
    doc = pymupdf.open(str(pdf))
    n_pages = len(doc)
    doc.close()
    needed = (n_pages + max_pages - 1) // max_pages if n_pages > max_pages else 1
    parts_dir = out_dir / ".parts" / pdf.stem

    existing = sorted(parts_dir.glob(f"{pdf.stem}_part*.pdf")) if parts_dir.exists() else []
    if needed > 1 and len(existing) == needed:
        print(f"[skip]  {pdf.name}: {n_pages} pages, {len(existing)} parts already exist")
        skipped += 1
        continue

    parts = split_pdf(pdf, parts_dir, max_pages=max_pages)
    if len(parts) == 1:
        print(f"[skip]  {pdf.name}: {n_pages} pages (no split needed)")
    split_count += len(parts)

print(f"\nSplit: {split_count} part file(s), skipped: {skipped} already-complete doc(s)")
