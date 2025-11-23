# ---------------------------------------------------------------------
# Gufo Font: Render icons.md
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate icons.md."""

# Third-party modules
from jinja2 import Environment, PackageLoader

# Gufo Font modules
from ..manifest import Manifest

TEMPLATE = "icons.md.j2"


def get_icons_md() -> str:
    """Generate html file."""
    env = Environment(loader=PackageLoader("gufo.font", "templates"), autoescape=True)
    tpl = env.get_template(TEMPLATE)
    manifest = Manifest.read()
    return tpl.render(manifest=manifest)
