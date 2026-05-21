"""Split a PDF into chunks of at most `max_pages` pages.

minerU's cloud API limits a single uploaded file to 200 pages. Several of
our manuals (Dakota at 347, Sentaurus sdevice_ug at 1530) exceed that, so
01_pdf_to_markdown.py transparently pre-splits them. The split parts get
re-merged into a single markdown after the API returns — callers downstream
(02_markdown_to_context.py) only ever see the merged output.

Uses PyMuPDF (MuPDF C engine) — no per-page deep-copy, fast even on 1500+ page PDFs.
"""
from __future__ import annotations

from pathlib import Path


def split_pdf(src: Path, dst_dir: Path, max_pages: int) -> list[tuple[Path, int]]:
    """Split `src` into `dst_dir/<stem>_partNN.pdf` chunks of <= max_pages pages.

    Returns `[(part_path, page_count), ...]`. If `src` already fits in
    `max_pages` (or `max_pages <= 0`), returns `[(src, page_count)]` without
    writing anything.

    Existing part files are overwritten.
    """
    import sys
    import pymupdf

    doc = pymupdf.open(str(src))
    n_pages = len(doc)
    if max_pages <= 0 or n_pages <= max_pages:
        doc.close()
        return [(src, n_pages)]

    dst_dir.mkdir(parents=True, exist_ok=True)
    num_parts = (n_pages + max_pages - 1) // max_pages
    width = max(2, len(str(num_parts)))
    parts: list[tuple[Path, int]] = []
    bar_width = 20
    label = src.stem
    for i in range(num_parts):
        start = i * max_pages
        end = min((i + 1) * max_pages, n_pages) - 1
        filled = i * bar_width // num_parts
        bar = "█" * filled + "░" * (bar_width - filled)
        sys.stdout.write(f"\r[{label}] {bar} part {i + 1}/{num_parts} "
                         f"(pages {start}-{end + 1})")
        sys.stdout.flush()
        sub = pymupdf.open()
        sub.insert_pdf(doc, from_page=start, to_page=end)
        out = dst_dir / f"{src.stem}_part{i + 1:0{width}d}.pdf"
        if out.exists():
            out.unlink()
        sub.save(str(out))
        sub.close()
        parts.append((out, end - start + 1))
    filled = bar_width
    bar = "█" * filled
    sys.stdout.write(f"\r[{label}] {bar} ✓ {num_parts} parts ({n_pages} pages)\n")
    sys.stdout.flush()
    doc.close()
    return parts
