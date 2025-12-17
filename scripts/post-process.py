# ---------------------------------------------------------------------
# Gufo Font: Post-processing.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""
Perform post-processing.

1. Hash .woff2 filename and change font's URL in resulting CSS.
"""

# Python modules
import argparse
import re
import shutil
from hashlib import sha3_512
from pathlib import Path

FONT_NAME = "GufoFont-Regular"
DIST = Path("dist", "gufo-font")
WOFF2 = DIST / f"{FONT_NAME}.woff2"
CSS = DIST / "gufo-font.css"
CSS_MIN = DIST / "gufo-font.min.css"
DEFAULT_HASH_LEN = 8


def hash_font(hash_placeholder: str) -> None:
    """Add hash into font's file name and update css."""
    if not WOFF2.exists():
        return  # Already post-processed
    # Generate mask
    FILE_MASK = rf"{FONT_NAME}\.{hash_placeholder}\.woff2"
    rx_url = re.compile(rf"url\(\"({FILE_MASK})\"\)", re.DOTALL | re.MULTILINE)
    # Calculate hash
    hash_value = sha3_512(WOFF2.read_bytes()).hexdigest()[: len(hash_placeholder)]
    hashed_name = f"{FONT_NAME}.{hash_value}.woff2"
    # Rename file
    shutil.move(WOFF2, DIST / hashed_name)
    # Patch css
    for path in (CSS, CSS_MIN):
        if not path.exists():
            continue
        # Find CSS in URL
        css = path.read_text()
        match = rx_url.search(css)
        if not match:
            msg = "Cannot replace CSS with hash"
            raise ValueError(msg)
        # Update CSS
        css = css[: match.start(1)] + hashed_name + css[match.end(1) :]
        path.write_text(css)


def main() -> None:
    """Perform post-processing."""
    parser = argparse.ArgumentParser(
        description="Example script with hash placeholder."
    )
    parser.add_argument(
        "--hash-placeholder", default="X" * DEFAULT_HASH_LEN, help="Hash placeholder"
    )
    args = parser.parse_args()
    hash_font(args.hash_placeholder)


if __name__ == "__main__":
    main()
