# ---------------------------------------------------------------------
# Gufo Font: Extract layers from SVG file
# ---------------------------------------------------------------------
# Copyright (C) 2025, Gufo Labs
# ---------------------------------------------------------------------

# Python modules
import sys
import xml.etree.ElementTree as ET
from enum import Enum, IntEnum
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
SODIPODI_NS = "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"

CLEAN_NS = (INKSCAPE_NS, SODIPODI_NS)


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


class LayerLayout(IntEnum):
    """
    Document layers layout.

    Attributes:
        SOLID: Single `.S` layer.
        BICOLOR: `.A` and `.B` layers.
    """

    SOLID = 0
    BICOLOR = 1


# Register namespaces so ET doesn't generate ns0 prefixes
ET.register_namespace("", "http://www.w3.org/2000/svg")


def get_layer_layout(tree: ET.ElementTree) -> LayerLayout:
    """
    Detect document layer layout.

    Args:
        tree: Document to analyze.

    Returns:
        LayerLayout.SOLID: Document defines `.S` layer.
        LayerLayout.BICOLOR: Document defines `.A` and `.B` layers.

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
        return LayerLayout.BICOLOR
    msg = "SVG does not contain required .S or (.A and .B) inkcape layers"
    raise ValueError(msg)


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


def extract_layer(tree: ET.ElementTree, layer: LayerName) -> list[ET.Element]:
    """
    Extract children of layer.

    Args:
        tree: Document's tree.
        layer: Layer to extract.

    Returns:
        List of children.
    """
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
    out_tree.write(str(path), encoding="utf-8", xml_declaration=True)
    print(f"Written {path}")


def main(path: Path) -> None:
    """Extract layers."""
    # Prepare file names
    out_dir = (path.parent / ".." / "layers").resolve()
    base = path.stem
    # Parse source
    tree = ET.parse(path)
    # Process layers
    match get_layer_layout(tree):
        case LayerLayout.SOLID:
            write_layer(
                tree,
                extract_layer(tree, LayerName.SOLID),
                (out_dir / base).with_suffix(".svg"),
            )
        case LayerLayout.BICOLOR:
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
        case _:
            msg = "Unknown layout"
            raise ValueError(msg)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
