"""Read / write ``context_layer/manifest.json``.

Schema (top-level):
    {
      "version": 1,
      "generated_at": "<ISO-8601 UTC>",
      "software": {
        "<software>": {
          "total_estimated_tokens": <int>,
          "docs": {
            "<doc>": {
              "source_pdf":         "corpus/raw/<software>/<doc>.pdf",
              "md_path":            "corpus/markdown/<software>/<doc>/<doc>.md",
              "content_list_path":  "corpus/markdown/<software>/<doc>/<doc>_content_list.json",
              "estimated_tokens":   <int>,
              "page_count":         <int>,
              "tier":               "T0|T1|T2|T3",
              "outputs": {
                "full_md":    "context_layer/<software>/<doc>/full.md",
                "outline_md": "context_layer/<software>/<doc>/outline.md"  // if T1+
                "chapters":   ["context_layer/<software>/<doc>/chapters/00_intro.md", ...]  // if T2+
              }
            }
          }
        }
      }
    }
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MANIFEST_VERSION = 1


def load(manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        return {"version": MANIFEST_VERSION, "generated_at": None, "software": {}}
    with manifest_path.open(encoding="utf-8") as f:
        return json.load(f)


def upsert_software(manifest: dict[str, Any], software: str, entry: dict[str, Any]) -> None:
    """Replace the entry for ``software``. ``entry`` is the dict that goes
    under ``manifest["software"][software]``.
    """
    manifest.setdefault("software", {})[software] = entry


def save(manifest: dict[str, Any], manifest_path: Path) -> None:
    manifest["version"] = MANIFEST_VERSION
    manifest["generated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
