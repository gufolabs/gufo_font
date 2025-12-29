# ---------------------------------------------------------------------
# Gufo Font: Create manifest.json
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Create manifest.json."""

# Python modules
import json
from pathlib import Path

# Gufo Font modules
from gufo.font.manifest import Manifest

DIST = Path("dist", "gufo-font")
MANIFEST_JSON = DIST / "manifest.json"


def write_manifest_json(manifest: Manifest) -> None:
    """Write manifest.json file."""
    r = {"version": manifest.version, "icons": {}}
    for section, icons in manifest.icons.items():
        s_data = []
        r["icons"][section] = s_data
        for icon in icons:
            if not icon.is_enabled:
                continue
            item = {"name": icon.name, "code": icon.code, "added_in": icon.added_in}
            if icon.description:
                item["description"] = icon.description
            if icon.labels:
                item["labels"] = icon.labels
            s_data.append(item)
    MANIFEST_JSON.write_text(json.dumps(r))


def main() -> None:
    """Main function."""
    manifest = Manifest.read()
    write_manifest_json(manifest)


if __name__ == "__main__":
    main()
