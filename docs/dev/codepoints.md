# Gufo Font Codepoints Range

*Gufo Font* uses the Unicode Private Use Area (PUA) for glyph codepoints.
The allocated ranges for different sections are as follows:

| Name    | Section Prefix | From   | To     | Size | Description                                        |
| ------- | -------------- | ------ | ------ | ---- | -------------------------------------------------- |
| ASCII   |                |        | U+FF   | 256  | Standard ASCII symbols                             |
| BRANDS  | `brand`        | U+E000 | U+E07F | 128  | NOC authorided derived products and parther's logo |
| APPS    | `app`          | U+E080 | U+E27F | 512  | NOC Application's icons, including plugins         |
| UI      |                | U+E280 | U+E67F | 1024 | Application UI elements                            |
| IT      |                | U+F000 | U+F1FF | 512  | IT Stencils                                        |
| CISCO   | `cisco`        | U+F200 | U+F3FF | 512  | Cisco-style network stencils                       |
| JUNIPER | `juniper`      | U+F400 | U+F43F | 64   | Juniper-style network stencils                     |
| HUAWEI  | `huawei`       | U+F440 | U+F540 | 256  | Huawei-style network stencils                      |

!!! note

    All glyphs must remain within their assigned PUA range to avoid codepoint conflicts.

All used and reserved glyph codepoints are enumerated in the [manifest.yml][manifest] file,
located at the root of the Gufo Font project.

[manifest]: https://github.com/gufolabs/gufo_font/blob/master/manifest.yml