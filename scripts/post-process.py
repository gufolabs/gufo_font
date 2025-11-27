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
DIST = Path("dist")
WOFF2 = DIST / f"{FONT_NAME}.woff2"
CSS = DIST / "gufo-font.css"
CSS_MINI = DIST / "gufo-font.min.css"
HASH_LEN = 8
FILE_MASK = rf"{FONT_NAME}\.{'X' * HASH_LEN}\.woff2"
rx_url = re.compile(rf"url\(\"({FILE_MASK})\"\)", re.DOTALL | re.MULTILINE)
rx_font_name = re.compile(rf"{FONT_NAME}\.[0-9a-f]{{{HASH_LEN}}}\.woff2$")


def find_font_file() -> Path | None:
    """Return original or already hashed font file."""
    if WOFF2.exists():
        return WOFF2
    for candidate in DIST.glob(f"{FONT_NAME}.*.woff2"):
        if rx_font_name.fullmatch(candidate.name):
            return candidate
    return None


def hash_font(path: Path) -> None:
    """Add hash into font's file name and update css."""
    font_path = find_font_file()
    if font_path is None:
        return
    # Find CSS in URL
    css = path.read_text()
    match = rx_url.search(css)
    if not match:
        msg = "Cannot replace CSS with hash"
        raise ValueError(msg)
    # Calculate hash
    hash_value = sha3_512(font_path.read_bytes()).hexdigest()[:HASH_LEN]
    hashed_name = f"{FONT_NAME}.{hash_value}.woff2"
    # Update CSS
    css = css[: match.start(1)] + hashed_name + css[match.end(1):]
    path.write_text(css)
    # Rename file (only if needed)
    target = DIST / hashed_name
    if font_path.name != hashed_name:
        shutil.move(font_path, target)


def main() -> None:
    """Perform post-processing."""
    hash_font(CSS)
    hash_font(CSS_MINI)


if __name__ == "__main__":
    main()
