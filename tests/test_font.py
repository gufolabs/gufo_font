# ---------------------------------------------------------------------
# Gufo Font: Font tests
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
from pathlib import Path

# Third-party modules
import pytest
from fontTools.ttLib.ttFont import TTFont

# Gufo Font modules
from gufo.font.manifest import Manifest

PATH = Path("webfonts", "GufoFont-Regular.woff2")
GLYF = "glyf"
COLR = "COLR"
NAME = "name"
FONT_FAMILY = "Gufo Font"
FONT_SUBFAMILY = "Regular"


@pytest.fixture(scope="module")
def font() -> TTFont:
    return TTFont(PATH)


@pytest.fixture(scope="module")
def manifest() -> Manifest:
    return Manifest.read()


def test_flavor(font: TTFont) -> None:
    assert font.flavor == "woff2"


def _font_name_record(font: TTFont, record_id: int) -> str | None:
    """Get given record from name table."""
    for record in font[NAME].names:
        if record.nameID == record_id:
            return record.toUnicode()
    return None


def test_font_family(font: TTFont) -> None:
    family = _font_name_record(font, 1)
    assert family, "Font family is not set"
    assert family == FONT_FAMILY


def test_font_subfamily(font: TTFont) -> None:
    family = _font_name_record(font, 2)
    assert family, "Font subfamily is not set"
    assert family == FONT_SUBFAMILY


def test_font_version(font: TTFont, manifest: Manifest) -> None:
    def to_semver(s: str) -> str:
        return ".".join(str(int(x)) for x in s.split("."))

    version_string = _font_name_record(font, 5)
    assert version_string, "Version is not set"
    if ";" in version_string:
        version_string = version_string.split(";", 1)[0].strip()
    if " " in version_string:
        version_string = version_string.split()[-1]
    assert to_semver(version_string) == to_semver(manifest.version)


def test_glyf_table(font: TTFont, manifest: Manifest) -> None:
    assert GLYF in font
    # Collect codepoints from font
    table = font[GLYF]
    cmap = {v: k for k, v in font.getBestCmap().items()}
    font_codepoints: set[str] = set()
    for c in table.glyphs:
        cp = cmap.get(c)
        if cp:
            font_codepoints.add(f"{cp:X}")
    # Collect codepoints from manifest
    manifest_codepoints: set[str] = set()
    for icons in manifest.icons.values():
        for icon in icons:
            if icon.added_in:
                manifest_codepoints.add(f"{icon.code:X}")
    if not_defined := font_codepoints - manifest_codepoints:
        lst = ", ".join(sorted(not_defined))
        ln = len(not_defined)
        pytest.fail(
            f"{ln} codepoints present in font but not defined in manifest: {lst}"
        )
    if missed := manifest_codepoints - font_codepoints:
        lst = ", ".join(missed)
        pytest.fail(f"{len(missed)} codepoints are missed in font: {lst}")


def test_colr_table(font: TTFont, manifest: Manifest) -> None:
    assert COLR in font
    table = font[COLR]
    too_few_layers: set[str] = set()
    missed_glyph: set[str] = set()
    for icons in manifest.icons.values():
        for icon in icons:
            if (
                icon.added_in
                and not icon.name.endswith("-s")
                and not icon.name.endswith("-o")
                and icon.code > 255
            ):
                try:
                    r = table[f"uni{icon.code:X}"]
                    if len(r) < 2:
                        too_few_layers(f"{icon.code:X}")
                except KeyError:
                    missed_glyph(f"{icon.code:X}")
    if too_few_layers:
        lst = ", ".join(sorted(too_few_layers))
        pytest.fail(
            f"{len(too_few_layers)} color symbols must have at least 2 layers: {lst}"
        )
    if missed_glyph:
        lst = ", ".join(sorted(missed_glyph))
        pytest.fail(f"{len(missed_glyph)} missed color glyphs: {lst}")
