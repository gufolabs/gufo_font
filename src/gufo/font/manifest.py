# ---------------------------------------------------------------------
# Gufo Font: Manifest class
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Manifest class and utilities."""

# Python modules
import operator
from dataclasses import dataclass
from typing import Any, Iterable

import yaml

MANIFEST = "manifest.yml"
PJ_NAME = "@gufo-labs/font"
PJ_DESCRIPTION = "Telecom and IT-oriented icon font"
PJ_LICENSE = "SEE LICENCE IN README.md"


@dataclass
class Icon(object):
    """
    Icon.

    Attributes:
        name: CSS class name, kebab-case.
        code: Codepoint.
        description: Icon description.
        labels: List of tags.
        added_in: Version added. Use "upcoming" for upcoming release.
            Icons with empty added_in considered reserved codepoints
            and not added into resulting bundle.
    """

    name: str
    code: int
    description: str | None = None
    labels: list[str] | None = None
    added_in: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Icon":
        """
        Create Icon instance from dict.

        Args:
            data: Input data.

        Returns:
            Icon instance.
        """
        return Icon(
            name=data["name"],
            code=data["code"],
            description=data.get("description"),
            labels=data.get("labels") or [],
            added_in=data.get("added-in"),
        )

    @property
    def is_enabled(self) -> bool:
        """Check if icon is enabled."""
        return bool(self.added_in)


@dataclass
class Manifest(object):
    """
    Font manifest.

    Attributes:
        version: Gufo Font version.
        icons: Icon tables. Key is table name, values are the lists of Icons.
    """

    version: str
    icons: dict[str, list[Icon]]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Manifest":
        """
        Create Manifest instance from dict.

        Args:
            data: Input data.

        Returns:
            Manifest instance.
        """
        return Manifest(
            version=data["version"],
            icons={
                table: [Icon.from_dict(x) for x in icons]
                for table, icons in data["icons"].items()
            },
        )

    def get_codepoints_scss(self) -> str:
        """Generate _codepoints.css content."""
        codepoints = []
        for _table, icons in self.icons.items():
            for icon in sorted(icons, key=operator.attrgetter("code")):
                if icon.is_enabled:
                    codepoints.append(f'    {icon.name}: "\\\\{icon.code:x}"')
        r = ["$glyph-codepoints: (", ",\n".join(codepoints), ");"]
        return "\n".join(r)

    @classmethod
    def read(cls) -> "Manifest":
        """
        Read manifest.

        Returns:
            Manifest instance.
        """
        with open(MANIFEST) as fp:
            data = yaml.load(fp.read(), Loader=yaml.SafeLoader)
            return Manifest.from_dict(data)

    def iter_enabled_icons(self, group: str) -> Iterable[Icon]:
        """
        Iterate all enabled icons in group.

        Args:
            group: Icons group name.

        Returns:
            Yields active icons
        """
        for icon in sorted(self.icons.get(group, []), key=operator.attrgetter("code")):
            if icon.is_enabled:
                yield icon

    @property
    def package_json(self) -> dict[str, Any]:
        """Generate packages.json data."""
        return {
            "name": PJ_NAME,
            "version": self.version,
            "description": PJ_DESCRIPTION,
            "license": PJ_LICENSE,
            "type": "module",
            "files": ["**/*"],
            "publishConfig": {"access": "public"},
        }
