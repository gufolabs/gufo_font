# ---------------------------------------------------------------------
# Gufo Font: Create build/_codepoints.scss file.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate build/_codepoints.scss file."""

# Python modules
from pathlib import Path

# Gufo Font modules
from lib.manifest import Manifest

CODEPOINTS = Path("build", "_codepoints.scss")


def main() -> None:
    """Generate codepoints file."""
    manifest = Manifest.read()
    CODEPOINTS.write_text(manifest.get_codepoints_scss())


if __name__ == "__main__":
    main()
