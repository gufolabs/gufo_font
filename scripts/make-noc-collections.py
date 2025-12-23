# ---------------------------------------------------------------------
# Gufo Font: Generate NOC collections bundle.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import json
import uuid
from dataclasses import dataclass
from operator import attrgetter
from typing import Any

# Gufo Font modules
from gufo.font.manifest import Icon, Manifest

GUFO_FONT_NS = uuid.UUID("263c5192-d18c-4716-ba02-dc34ae5ff0b6")


@dataclass
class Glyph(object):
    """Glyph collection item."""

    name: str
    code: int

    @classmethod
    def from_icon(cls, icon: Icon) -> "Glyph":
        """Generate glyph from manifest icon."""
        return Glyph(name=icon.name, code=icon.code)

    @property
    def uuid(self) -> str:
        """Generate stable uuid."""
        return str(uuid.uuid5(GUFO_FONT_NS, f"{self.code}"))

    def to_dict(self) -> dict[str, Any]:
        """Generate collection's item."""
        return {"name": self.name, "uuid": self.uuid, "code": self.code}


def main() -> None:
    manifest = Manifest.read()
    items: list[Glyph] = []
    for icons in manifest.icons.values():
        items.extend(Glyph.from_icon(icon) for icon in icons if icon.added_in)
    r = {
        "$type": "bundle",
        "$collection": "sa.actioncommands",
        "items": [item.to_dict() for item in sorted(items, key=attrgetter("code"))],
    }
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
