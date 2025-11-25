# Glyph Naming Scheme

Gufo Font uses a systematic naming scheme for glyphs, based on the glyph’s section, name, size, and style. The general format is:

```
[<section>-]<name>[-<size>][-<style>]
```

Brackets indicate optional parts.

## <section>

The optional section prefix categorizes glyphs:

| Section        | Prefix  | Description                              |
| -------------- | ------- | ---------------------------------------- |
| Brands         | `brand` | NOC branding icons                       |
| App Icons      | `app`   | NOC application icons                    |
| UI Icons       |         | User interface elements, default section |
| Cisco Stencils | `cisco` | Cisco-style stencils                     |

## <name>

A unique identifier for the glyph within its section.
Examples: `home`, `search`, `user`.

## Size

Specifies the relative size of the glyph:

* Not specified – Full-size glyph occupying the entire 4096-unit design grid.
* `small` – Smaller version, centered within the 8×8 central grid cells.

## Style

Specifies the visual style of the glyph:

* Not specified – Default bi-color outline style. Allows the colors to change depending on the element’s state.
* `solid` – Fully filled glyph.
* `border` – Hollow glyph with only the border/stroke visible, transparent inside.