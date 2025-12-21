# ---------------------------------------------------------------------
# Gufo Font: Create package.json file.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate package.json file."""

# Python modules
import json
from pathlib import Path

import yaml

# Gufo Font modules
from gufo.font.manifest import Manifest

DIST = Path("dist", "gufo-font")
FUNDING = Path(".github", "FUNDING.yml")
PACKAGE_JSON = DIST / "package.json"


def main() -> None:
    """Generate packages.json file."""
    manifest = Manifest.read()
    data = manifest.package_json
    if FUNDING.exists():
        data["funding"] = get_funding()
    PACKAGE_JSON.write_text(json.dumps(data, indent=2))


def get_funding() -> list[dict[str, str]]:
    """Generate funding data."""
    r = []
    with open(FUNDING) as fp:
        d = yaml.safe_load(fp)
    for k, v in d.items():
        match k:
            case "github":
                if isinstance(v, str):
                    v = [v]
                for item in v:
                    r.append(
                        {"type": "github", "url": f"https://github.com/sponsors/{item}"}
                    )
            case "buy_me_a_coffee":
                r.append(
                    {
                        "type": "buy-me-a-coffee",
                        "url": f"https://www.buymeacoffee.com/{v}",
                    }
                )
    return r


if __name__ == "__main__":
    main()
