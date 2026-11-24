#!/usr/bin/env python3
"""news-image-20261123 entry: copy the bundled newspaper image to output.

Stdlib only. Writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
The image itself is a fixed asset in this repo; this program just copies it.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
