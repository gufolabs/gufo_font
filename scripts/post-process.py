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
import re
import shutil
from hashlib import sha3_512
from pathlib import Path

FONT_NAME = "GufoFont-Regular"
DIST = Path("dist", "gufo-font")
WOFF2 = DIST / f"{FONT_NAME}.woff2"
CSS = DIST / "gufo-font.css"
HASH_LEN = 8
FILE_MASK = rf"{FONT_NAME}\.{'X' * HASH_LEN}\.woff2"
rx_url = re.compile(rf"url\(\"({FILE_MASK})\"\)", re.DOTALL | re.MULTILINE)


def hash_font() -> None:
    """Add hash into font's file name and update css."""
    if not WOFF2.exists():
        return
    # Find CSS in URL
    css = CSS.read_text()
    match = rx_url.search(css)
    if not match:
        msg = "Cannot replace CSS with hash"
        raise ValueError(msg)
    # Calculate hash
    hash_value = sha3_512(WOFF2.read_bytes()).hexdigest()[:HASH_LEN]
    hashed_name = f"{FONT_NAME}.{hash_value}.woff2"
    # Update CSS
    css = css[: match.start(1)] + hashed_name + css[match.end(1) :]
    CSS.write_text(css)
    # Rename file
    shutil.move(WOFF2, DIST / hashed_name)


def main() -> None:
    """Perform post-processing."""
    hash_font()


if __name__ == "__main__":
    main()
