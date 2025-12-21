# ---------------------------------------------------------------------
# Gufo Font: Show Font Summary
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import operator
from pathlib import Path

# Third party modules
from fontTools.pens.recordingPen import RecordingPen
from fontTools.ttLib import TTFont

# Gufo Font modules
from gufo.font.manifest import Manifest

FONT_PATH = Path("webfonts", "GufoFont-Regular.woff2")
CFF = "CFF "


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
    cff = font[CFF].cff
    top_dict = cff.topDictIndex[0]
    char_strings = top_dict.CharStrings

    points_count: dict[str, int] = {}

    for glyph_name in char_strings.keys():
        code = cmap.get(glyph_name)
        if code is None:
            continue

        manifest_name = code_to_name.get(code)
        if not manifest_name:
            continue

        pen = RecordingPen()

        # Draw glyph to pen (executes charstring)
        char_strings[glyph_name].draw(pen)

        # Count points from recorded operations
        num_points = 0
        for op, args in pen.value:
            if op == "moveTo" or op == "lineTo":
                num_points += 1
            elif op == "curveTo":
                # cubic Bezier: 3 control points
                num_points += 3
            # closePath adds no points

        points_count[manifest_name] = num_points

    return points_count


def summary() -> None:
    for name, count in sorted(
        glyph_points().items(), key=operator.itemgetter(1), reverse=True
    ):
        print(f"{name}: {count}")


if __name__ == "__main__":
    summary()
