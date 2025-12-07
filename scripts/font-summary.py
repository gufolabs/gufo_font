# ---------------------------------------------------------------------
# Gufo Font: Show Font Summary
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import operator
from pathlib import Path

# Third party modules
from fontTools.ttLib import TTFont

# Gufo Font modules
from gufo.font.manifest import Manifest

FONT_PATH = Path("webfonts", "GufoFont-Regular.woff2")


def glyph_points() -> dict[str, int]:
    font = TTFont(str(FONT_PATH))
    # Get glyph name to code map
    cmap = {v: k for k, v in font.getBestCmap().items()}
    manifest = Manifest.read()
    code_to_name = {}
    for icons in manifest.icons.values():
        for icon in icons:
            code_to_name[icon.code] = icon.name
    # Get points
    glyf_table = font["glyf"]
    points_count = {}
    for glyph_name in glyf_table.keys():
        code = cmap.get(glyph_name)
        if not code:
            continue
        manifest_name = code_to_name.get(code)
        if not manifest_name:
            continue
        glyph = glyf_table[glyph_name]
        if glyph.isComposite():
            # Composite glyph: sum points of components
            num_points = sum(
                glyf_table[comp.glyphName].numberOfContours
                for comp in glyph.components
                if hasattr(glyf_table[comp.glyphName], "numberOfContours")
            )
            # Note: numberOfContours may be negative for empty glyphs
        elif glyph.numberOfContours > 0:
            num_points = sum(
                len(contour) for contour in glyph.getCoordinates(font["glyf"])[0]
            )
        else:
            num_points = 0
        points_count[manifest_name] = num_points
    return points_count


def summary() -> None:
    for name, count in sorted(
        glyph_points().items(), key=operator.itemgetter(1), reverse=True
    ):
        print(f"{name}: {count}")


if __name__ == "__main__":
    summary()
