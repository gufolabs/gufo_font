# ---------------------------------------------------------------------
# Gufo Font: Create package.json file.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate package.json file."""

# Python modules
import json
from pathlib import Path

# Gufo Font modules
from gufo.font.manifest import Manifest

DIST = Path("dist", "gufo-font")
PACKAGE_JSON = DIST / "package.json"


def main() -> None:
    """Generate packages.json file."""
    manifest = Manifest.read()
    PACKAGE_JSON.write_text(json.dumps(manifest.package_json, indent=2))


if __name__ == "__main__":
    main()
