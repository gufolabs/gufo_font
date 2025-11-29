# Gufo Font Metrics

Gufo Font is a highly specialized icon font, and following the guidelines in this document
is essential for maintaining overall consistency and visual quality across all glyphs.
Throughout this guide, we refer to internal font units.

Each glyph in Gufo Font is defined within its own internal coordinate system,
with the origin located at the bottom-left corner. All measurements, shapes,
and alignment rules are expressed relative to this coordinate system.

## Glyph Size

Gufo Font is designed with **UPM** (Units per Em) = 4096.

This means that all glyph coordinates—both X and Y—must lie within the range 0..4096,
corresponding to the internal design grid of the font.

## Ascender and Descender

As an icon-focused typeface, Gufo Font aligns its baseline with the bottom edge of the glyph’s
design space. The font uses the following typographic metrics:

* Typo Ascender: 4096
* Typo Descender: 0
* 
This configuration ensures that all icons sit consistently on the baseline and utilize the full
internal vertical space available within the 0–4096 UPM grid.

## Design Grid

Gufo Font is organized around a 16×16 design grid, which provides a consistent structural framework
for all glyphs.

Given the font’s UPM of 4096, each grid cell corresponds to 256×256 internal units.
Designers should align key shapes, anchors, and visual features to this grid to ensure consistent
proportions, spacing, and stylistic cohesion across all icons.

## Proportions and Centering

Gufo Font glyphs are ideally designed with square proportions. When this is not possible and the
glyph’s width and height differ, the following rules apply:

* The larger dimension must span the full available 4096-unit space.
* The shorter dimension must be optically centered within the design area, leaving equal spacing on both sides (horizontally or vertically, depending on orientation).

This ensures consistent visual balance across all icons, regardless of their inherent aspect ratios.

## Element width

To maintain visual consistency across all Gufo Font glyphs, the following element widths are highly recommended:

* Outline: 64 units
* Border / Stroke: 256 units

These values align with the 16×16 design grid and provide a balanced,
uniform appearance when icons are rendered at various sizes.

## Element Proportions

Recognizable elements must have consistent proportions:

| Element                      | W:H |
| ---------------------------- | --- |
| Paper page (portrait)        | 3:4 |
| Paper page (landscape)       | 4:3 |
| Perspective (cylinder's top) | 5:2 |