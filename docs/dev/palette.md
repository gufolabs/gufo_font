# Palette

Gufo Font is a COLR/CPAL color font, and to provide a consistent and predictable user experience, the following conventions are used:

* Outline (`-o`) and Solid (`-s`) glyphs are rendered as plain monochrome shapes.
* Palette 1 defines the standard color roles:

    * Index 0 — Fill color. This color may change dynamically to represent the state of the UI element. By default, it is black.
    * Index 1 — White outline. Used for both the outer borders and internal line details. This color does not change when the glyph style or fill color changes.
