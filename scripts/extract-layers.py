# ---------------------------------------------------------------------
# Gufo Font: Extract layers from SVG file
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import io
import xml.etree.ElementTree as ET
from enum import Enum, IntEnum
from pathlib import Path
from typing import Iterable

SVG_NS = "http://www.w3.org/2000/svg"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
SODIPODI_NS = "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"

CLEAN_NS = (INKSCAPE_NS, SODIPODI_NS)

UPM = 4096
VALID_VIEWBOX = f"0 0 {UPM} {UPM}"


class LayerName(Enum):
    """
    Layer names.

    Attributes:
        OUTLINE: White outline.
        STATUS: Black status.
        SOLID: Solid layer.
    """

    OUTLINE = ".A"
    STATUS = ".B"
    SOLID = ".S"
    COLOR = ".C"


class LayerLayout(IntEnum):
    """
    Document layers layout.

    Attributes:
        SOLID: Single `.S` layer.
        COLOR: `.A` and `.B` layers.
    """

    SOLID = 0
    COLOR = 1


# Register namespaces so ET doesn't generate ns0 prefixes
ET.register_namespace("", "http://www.w3.org/2000/svg")


def get_layer_layout(tree: ET.ElementTree) -> LayerLayout:
    """
    Detect document layer layout.

    Args:
        tree: Document to analyze.

    Returns:
        LayerLayout.SOLID: Document defines `.S` layer.
        LayerLayout.COLOR: Document defines `.A` and `.B` layers.

    Raises:
        ValueError: if layout cannot be detected.
    """

    def has_layer(layer: LayerName) -> bool:
        label = layer.value
        xpath = (
            f".//{{{SVG_NS}}}g"
            f"[@{{{INKSCAPE_NS}}}groupmode='layer']"
            f"[@{{{INKSCAPE_NS}}}label='{label}']"
        )
        return root.find(xpath) is not None

    root = tree.getroot()

    if has_layer(LayerName.SOLID):
        return LayerLayout.SOLID
    if has_layer(LayerName.OUTLINE) and has_layer(LayerName.STATUS):
        return LayerLayout.COLOR
    msg = "SVG does not contain required .S or (.A and .B) inkcape layers"
    raise ValueError(msg)


def iter_color_layers(tree: ET.ElementTree) -> Iterable[str]:
    """
    Iterate all .C<index> layers in document.

    Args:
        tree: Document to analyze.

    Returns:
        Yield color layers.
    """
    xpath = f".//{{{SVG_NS}}}g[@{{{INKSCAPE_NS}}}groupmode='layer']"
    root = tree.getroot()
    for g in root.findall(xpath):
        label = g.get(f"{{{INKSCAPE_NS}}}label")
        if not label:
            continue
        if label.startswith(LayerName.COLOR.value):
            yield label


def clean_element(element: ET.Element) -> None:
    """
    Clean up namespaces from CLEAN_NS.

    Args:
        element: Element to clean, including all children.
    """
    # Clean namespaces
    q = [attr for attr in element.attrib if attr.startswith(CLEAN_NS)]
    for attr in q:
        del element.attrib[attr]
    # Clean style
    style = element.attrib.get("style")
    if style:
        parts = dict(item.split(":", 1) for item in style.split(";") if ":" in item)
        parts["fill"] = "#000000"
        parts["stroke"] = "#000000"
        element.set("style", ";".join(f"{k}:{v}" for k, v in parts.items()))
    # Clean up recursively
    for child in element:
        clean_element(child)


def extract_layer(
    tree: ET.ElementTree, layer: LayerName, color: int | None = None
) -> list[ET.Element]:
    """
    Extract children of layer.

    Args:
        tree: Document's tree.
        layer: Layer to extract.
        color: Solor pallete index.

    Returns:
        List of children.
    """
    if layer == LayerName.COLOR and color:
        label = f"{layer.value}{color}"
    else:
        label = layer.value
    root = tree.getroot()
    for g in root.findall(f".//{{{SVG_NS}}}g"):
        gm = g.attrib.get(f"{{{INKSCAPE_NS}}}groupmode")
        glabel = g.attrib.get(f"{{{INKSCAPE_NS}}}label")
        if gm == "layer" and glabel == label:
            return list(g)
    msg = f"Layer {label} is not found"
    raise ValueError(msg)


def get_svg(original_root: ET.Element, children: list[ET.Element]) -> ET.ElementTree:
    """
    Construct SVG with children.

    Args:
        original_root: Original document's root.
        children: List of layer's children.

    Returns:
        SVG document.
    """
    new_svg = ET.Element(original_root.tag, original_root.attrib)
    for c in children:
        new_svg.append(c)
    clean_element(new_svg)
    return ET.ElementTree(new_svg)


def write_layer(tree: ET.ElementTree, children: list[ET.Element], path: Path) -> None:
    """Build and write SVG for layer."""
    out_tree = get_svg(tree.getroot(), children)
    f = io.BytesIO()
    out_tree.write(f, encoding="utf-8", xml_declaration=True)
    data = f.getvalue()
    if path.exists():
        old_data = path.read_bytes()
        if old_data == data:
            return
    print(f"Writing {path}: {len(data)} bytes")
    path.write_bytes(data)


def check_svg(path: Path, tree: ET.ElementTree) -> None:
    """
    Check if SVG is well-formated.

    Raises:
        ValueError: On violations.
    """

    def fix_viewbox(viewbox: str) -> bool:
        """Try to fix viewbox."""

        def near_4k(v: str) -> bool:
            try:
                return abs(float(v) - 4096.0) < 0.01
            except ValueError:
                return False

        items = viewbox.split()
        if len(items) != 4:
            return False
        if items[0] != "0" or items[1] != "0":
            return False
        if near_4k(items[2]) and near_4k(items[3]):
            root.set("viewBox", VALID_VIEWBOX)
            return True
        return False

    root = tree.getroot()
    # Check viewBox
    viewbox = root.attrib.get("viewBox")
    if viewbox is None:
        msg = f"{path}: SVG missing required viewBox attribute"
        raise ValueError(msg)
    # Normalize whitespace
    viewbox = " ".join(viewbox.split())
    if viewbox != VALID_VIEWBOX and not fix_viewbox(viewbox):
        msg = f"{path}: Invald viewbox: {viewbox}"
        raise ValueError(msg)


def extract_layers(path: Path) -> None:
    """Extract layers."""
    # Prepare file names
    out_dir = (path.parent / ".." / "layers").resolve()
    base = path.stem
    # Parse source
    tree = ET.parse(path)
    check_svg(path, tree)
    # Process layers
    match get_layer_layout(tree):
        case LayerLayout.SOLID:
            write_layer(
                tree,
                extract_layer(tree, LayerName.SOLID),
                (out_dir / base).with_suffix(".svg"),
            )
        case LayerLayout.COLOR:
            write_layer(
                tree,
                extract_layer(tree, LayerName.OUTLINE),
                (out_dir / f"{base}-a").with_suffix(".svg"),
            )
            write_layer(
                tree,
                extract_layer(tree, LayerName.STATUS),
                (out_dir / f"{base}-b").with_suffix(".svg"),
            )
            for cl in iter_color_layers(tree):
                index = int(cl[2:])
                write_layer(
                    tree,
                    extract_layer(tree, LayerName.COLOR, index),
                    (out_dir / f"{base}-c{index}").with_suffix(".svg"),
                )
        case _:
            msg = f"{path}: Unknown layout"
            raise ValueError(msg)


def main(paths: list[str]) -> None:
    """Extract layers from all files."""
    tasks: set[Path] = set()
    for p in paths:
        path = Path(p)
        if path.is_dir():
            tasks.update(pp for pp in path.rglob("*.svg"))
        else:
            tasks.add(path)
    for p in sorted(tasks):
        try:
            extract_layers(Path(p))
        except ValueError as e:
            print(f"{p}: {e}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
