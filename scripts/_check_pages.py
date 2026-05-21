"""Quick check: page counts of all PDFs for a given software."""
import sys
from pathlib import Path
import pymupdf

software = sys.argv[1] if len(sys.argv) > 1 else "sentaurus"
raw = Path("corpus/raw") / software
for pdf in sorted(raw.glob("*.pdf")):
    doc = pymupdf.open(str(pdf))
    n = len(doc)
    doc.close()
    parts = (n + 199) // 200
    print(f"{pdf.stem}: {n} pages -> {parts} part(s)")
