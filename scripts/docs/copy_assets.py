# ---------------------------------------------------------------------
# Gufo Font: Copy font and css into docs
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Copy font file and css into doc's distro."""

# Python modules
from pathlib import Path

# Third-party modules
import mkdocs_gen_files

build = Path("dist", "gufo-font")
assets = Path("assets")


def copy_file(src: str) -> None:
    """Copy file from repo to distro."""
    src_path = build / src
    if not src_path.exists():
        msg = f"Missed file: {src_path}"
        raise FileNotFoundError(msg)
    data = src_path.read_bytes()
    dst_path = assets / src
    with mkdocs_gen_files.open(str(dst_path), "wb") as fp:
        fp.write(data)


def main() -> None:
    """Copy assets."""
    copy_file("gufo-font.css")
    copy_file("gufo-font.css.map")
    for font in build.glob("*.woff2"):
        copy_file(font.name)


main()
