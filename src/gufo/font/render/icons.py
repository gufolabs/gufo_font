# ---------------------------------------------------------------------
# Gufo Font: Render icons.md
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate icons.md."""

# Python modules
from pathlib import Path

# Third-party modules
from jinja2 import Environment, PackageLoader

from ..manifest import Manifest

# Gufo Font modules
from ..scss import ScssParser

TEMPLATE = "icons.md.j2"


def get_icons_md() -> str:
    """Generate html file."""

    def q_color(s: str) -> str:
        return " ".join(c.capitalize() for c in s.split("-"))

    env = Environment(loader=PackageLoader("gufo.font", "templates"), autoescape=True)
    tpl = env.get_template(TEMPLATE)
    manifest = Manifest.read()
    # Build colors and states
    color_choices = []
    states_parser = ScssParser(Path("scss", "_state.scss"))
    for k in states_parser.extract_dict("states"):
        color_choices.append((f"gf-{k}", q_color(k)))
    colors_parser = ScssParser(Path("scss", "_colors.scss"))
    for k in colors_parser.extract_dict("colors"):
        color_choices.append((f"gf-{k}", q_color(k)))
    # Render
    return tpl.render(manifest=manifest, color_choices=color_choices)
