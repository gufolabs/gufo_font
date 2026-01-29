# ---------------------------------------------------------------------
# Gufo Font: Create package.json file.
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------
"""Generate package.json file."""

# Python modules
import datetime
import json
import operator
from pathlib import Path
from typing import Iterable

import yaml

# Gufo Font modules
from gufo.font.manifest import Manifest

DIST = Path("dist", "gufo-font")
FUNDING = Path(".github", "FUNDING.yml")
PACKAGE_JSON = DIST / "package.json"
INDEX_JS = DIST / "index.js"
INDEX_D_TS = DIST / "index.d.ts"
GLYPHS_JS = DIST / "glyphs.js"
GLYPHS_TS = DIST / "glyphs.ts"

JS_HEADER = """
// ------------------------------------------------------------------------
// Gufo Font: {name}
// ------------------------------------------------------------------------
// Copyright (C) {years}, Gufo Labs
// ------------------------------------------------------------------------
"""
PROJECT_START = 2025
CURRENT_YEAR = datetime.date.today().year


def main() -> None:
    """Generate packages.json file."""
    manifest = Manifest.read()
    make_package_json(manifest)
    make_index_js()
    make_index_d_ts()
    make_glyphs_js(manifest)
    make_glyphs_ts(manifest)


def make_package_json(manifest: Manifest) -> None:
    """Generate package.json file."""
    data = manifest.package_json
    data["main"] = "./index.js"
    data["types"] = "./index.d.ts"
    data["exports"] = {
        ".": {"types": "./index.d.ts", "default": "./index.js"},
        "./gufo-font.css": "./gufo-font.css",
        "./gufo-font.min.css": "./gufo-font.min.css",
        "./manifest.json": "./manifest.json",
    }
    if FUNDING.exists():
        data["funding"] = get_funding()
    PACKAGE_JSON.write_text(json.dumps(data, indent=2))


def get_js_header(name: str) -> str:
    """Generate JS file header."""
    if CURRENT_YEAR == PROJECT_START:
        years = str(PROJECT_START)
    else:
        years = f"{PROJECT_START}-{CURRENT_YEAR % 100}"
    return JS_HEADER.lstrip().format(name=name, years=years)


def make_index_js() -> None:
    """Generate index.js file."""
    r = [
        get_js_header("TypeScript definitions for index"),
        'export { CODEPOINTS, CSS_CLASSES } from "./glyphs.js";',
        "",
    ]
    INDEX_JS.write_text("\n".join(r))


def make_index_d_ts() -> None:
    """Generate index.d.ts file."""
    r = [
        get_js_header("Project index"),
        "export declare const CODEPOINTS: Record<string, number>;",
        "export declare const CSS_CLASSES: Record<string, string>;",
        "",
    ]
    INDEX_D_TS.write_text("\n".join(r))


def q_name(s: str) -> str:
    """Quote JS variable name."""
    return s.replace("-", "_")


def iter_codepoints_defs(manifest: Manifest) -> Iterable[str]:
    """Generate CODEPOINTS definitions."""
    for section, icons in manifest.icons.items():
        yield f"  // {section}"
        for icon in sorted(icons, key=operator.attrgetter("code")):
            yield f"  {q_name(icon.name)}: 0x{icon.code:X},"


def iter_css_classes_defs(manifest: Manifest) -> Iterable[str]:
    """Generate CSS_CLASSES definitions."""
    for section, icons in manifest.icons.items():
        yield f"  // {section}"
        for icon in sorted(icons, key=operator.attrgetter("name")):
            yield f'  {q_name(icon.name)}: "{icon.name}",'


def make_glyphs_js(manifest: Manifest) -> None:
    """Generate glyphs.js file."""
    r = [
        get_js_header("Glyphs definitions"),
        "export const CODEPOINTS = {",
        *iter_codepoints_defs(manifest),
        "};",
        "",
        "export const CSS_CLASSES = {",
        *iter_css_classes_defs(manifest),
        "};",
        "",
    ]
    GLYPHS_JS.write_text("\n".join(r))


def make_glyphs_ts(manifest: Manifest) -> None:
    """Generate glyphs.ts file."""
    r = [
        get_js_header("Glyphs definitions"),
        "export const CODEPOINTS: Record<string, number> = {",
        *iter_codepoints_defs(manifest),
        "};",
        "",
        "export const CSS_CLASSES: Record<string, string> = {",
        *iter_css_classes_defs(manifest),
        "};",
        "",
    ]
    GLYPHS_TS.write_text("\n".join(r))


def get_funding() -> list[dict[str, str]]:
    """Generate funding data."""
    r = []
    with open(FUNDING) as fp:
        d = yaml.safe_load(fp)
    for k, v in d.items():
        match k:
            case "github":
                if isinstance(v, str):
                    v = [v]
                for item in v:
                    r.append(
                        {"type": "github", "url": f"https://github.com/sponsors/{item}"}
                    )
            case "buy_me_a_coffee":
                r.append(
                    {
                        "type": "buy-me-a-coffee",
                        "url": f"https://www.buymeacoffee.com/{v}",
                    }
                )
    return r


if __name__ == "__main__":
    main()
