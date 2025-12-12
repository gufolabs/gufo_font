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
CFF = "CFF "
COLR = "COLR"
NAME = "name"
HEAD = "head"
HHEA = "hhea"
OS2 = "OS/2"
FONT_FAMILY = "Gufo Font"
FONT_SUBFAMILY = "Regular"
UPM = 4096


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


def test_curve_type(font: TTFont) -> None:
    assert GLYF not in font
    assert CFF in font


@pytest.mark.parametrize(
    ("metric", "expected"),
    [("unitsPerEm", UPM)],  # , ("xMin", 0), ("yMin", 0), ("xMax", UPM), ("yMax", UPM)],
)
def test_head_metrics(font: TTFont, metric: str, expected: int) -> None:
    v = getattr(font[HEAD], metric)
    assert v == expected, f"{metric} must be {expected} (currently {v})"


@pytest.mark.parametrize(
    ("metric", "expected"), [("ascent", UPM), ("descent", 0), ("lineGap", 0)]
)
def test_hhea_metrics(font: TTFont, metric: str, expected: int) -> None:
    v = getattr(font[HHEA], metric)
    assert v == expected, f"{metric} must be {expected} (currently {v})"


@pytest.mark.parametrize(
    ("metric", "expected"),
    [
        ("sTypoAscender", UPM),
        ("sTypoDescender", 0),
        ("sTypoLineGap", 0),
        ("usWinAscent", UPM),
        ("usWinDescent", 0),
        ("sCapHeight", UPM),
        ("sxHeight", UPM),
    ],
)
def test_os2_metrics(font: TTFont, metric: str, expected: int) -> None:
    v = getattr(font[OS2], metric)
    assert v == expected, f"{metric} must be {expected} (currently {v})"


def test_cff_table(font: TTFont, manifest: Manifest) -> None:
    assert CFF in font
    # Collect codepoints from font
    table = font[CFF]
    cff_top = table.cff.topDictIndex[0]
    glyph_names = set(cff_top.CharStrings.keys())
    cmap = {v: k for k, v in font.getBestCmap().items()}
    font_codepoints: set[str] = set()
    for gname in glyph_names:
        cp = cmap.get(gname)
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
    cmap = dict(font.getBestCmap().items())
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
                name = cmap.get(icon.code)
                if name:
                    r = table[name]
                    if len(r) < 2:
                        too_few_layers(f"{icon.code:X}")
                else:
                    missed_glyph.add(f"{icon.code:X}")
    if too_few_layers:
        lst = ", ".join(sorted(too_few_layers))
        pytest.fail(
            f"{len(too_few_layers)} color symbols must have at least 2 layers: {lst}"
        )
    if missed_glyph:
        lst = ", ".join(sorted(missed_glyph))
        pytest.fail(f"{len(missed_glyph)} missed color glyphs: {lst}")
