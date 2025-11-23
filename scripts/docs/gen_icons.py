# ---------------------------------------------------------------------
# Gufo Font: Generate icons.html
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate icons.html file."""

# Third-party modules
import mkdocs_gen_files

# Gufo Font modules
from gufo.font.render.icons import get_icons_md

ICONS_DOC = "icons.md"


with mkdocs_gen_files.open(ICONS_DOC, "w") as fp:
    fp.write(get_icons_md())
