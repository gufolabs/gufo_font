# Gufo Font Codepoints Range

*Gufo Font* uses the Unicode Private Use Area (PUA) for glyph codepoints.
The allocated ranges for different sections are as follows:

| Name   | Section Prefix | From   | To     | Size | Description                                        |
| ------ | -------------- | ------ | ------ | ---- | -------------------------------------------------- |
| BRANDS | `brand`        | U+E000 | U+E07F | 128  | NOC authorided derived products and parther's logo |
| APPS   | `app`          | U+E080 | U+E27F | 512  | NOC Application's icons, including plugins         |
| UI     |                | U+E280 | U+E67F | 1024 | Application UI elements                            |
| CISCO  | `cisco`        | U+F000 | U+F1FF | 512  | Cisco-style UI stencils                            |

!!! note

    All glyphs must remain within their assigned PUA range to avoid codepoint conflicts.

All used and reserved glyph codepoints are enumerated in the [manifest.yml][manifest] file,
located at the root of the Gufo Font project.

[manifest]: https://github.com/gufolabs/gufo_font/blob/master/manifest.yml