# ---------------------------------------------------------------------
# Gufo Font: Font tests
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
from pathlib import Path

import pytest

# Third-party modules
from fontTools.ttLib.ttFont import TTFont

# Gufo Font modules
from gufo.font.manifest import Manifest

PATH = Path("webfonts", "GufoFont-Regular.woff2")
GLYF = "glyf"
COLR = "COLR"


@pytest.fixture(scope="module")
def font() -> TTFont:
    return TTFont(PATH)


@pytest.fixture(scope="module")
def manifest() -> Manifest:
    return Manifest.read()


def test_flavor(font: TTFont) -> None:
    assert font.flavor == "woff2"


def test_glyf_table(font: TTFont, manifest: Manifest) -> None:
    assert GLYF in font
    table = font[GLYF]
    font_codepoints = {int(c[3:], 16) for c in table.glyphs if c.startswith("uni")}
    required_codepoints: set(int) = set()
    for icons in manifest.icons.values():
        for icon in icons:
            if icon.added_in:
                required_codepoints.add(icon.code)
    assert font_codepoints == required_codepoints


def test_colr_table(font: TTFont, manifest: Manifest) -> None:
    assert COLR in font
    table = font[COLR]
    errors: list[str] = []
    for icons in manifest.icons.values():
        for icon in icons:
            if (
                icon.added_in
                and not icon.name.endswith("-s")
                and not icon.name.endswith("-o")
            ):
                try:
                    r = table[f"uni{icon.code:X}"]
                    if len(r) < 2:
                        errors.append(
                            f"Color symbol 0x{icon.code:X} must have at least 2 layers"
                        )
                except KeyError:
                    errors.append(f"Missed color glyph 0x{icon.code:X}")
    assert not errors
