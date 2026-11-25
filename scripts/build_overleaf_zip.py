#!/usr/bin/env python3
"""
Package overleaf/ into a clean Overleaf-uploadable ZIP archive
with main.tex at the root of the archive.
Usage:
  python scripts/build_overleaf_zip.py
"""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVERLEAF_DIR = ROOT / "overleaf"
DIST_DIR = ROOT / "dist"
ZIP_PATH = DIST_DIR / "MultibaggerScout_IEEE_Conference_Overleaf.zip"

ALLOWED_SUFFIXES = {".tex", ".bib", ".cls", ".bst", ".png", ".pdf", ".eps", ".jpg"}


def build_zip() -> Path:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    included: list[str] = []
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OVERLEAF_DIR.rglob("*")):
            if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES:
                arcname = path.relative_to(OVERLEAF_DIR).as_posix()
                zf.write(path, arcname)
                included.append(arcname)

    print(f"Built Overleaf ZIP: {ZIP_PATH}")
    print(f"Total files packed: {len(included)}")
    for item in included:
        print(f"  - {item}")
    return ZIP_PATH


if __name__ == "__main__":
    build_zip()
