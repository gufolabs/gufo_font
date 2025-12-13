---
hide:
    - navigation
---
## Installation

### npm

Add `@gufo-labs/font` package to your project:

``` bash
npm install @gufo-labs/font
```

### CSS
```html
<link rel="stylesheet" href="https://gf.cdn.gufolabs.com/latest/gufo-font.css"/>
```
#todo: Archive

## Using Stencils

To add a network node use `<i>` tag with the required classes:

``` html
<i class="gf cisco-router"></i>
```

Where:

* `gf` - Enables Gufo Font.
* `cisco-router` - The icon name (see the [icons list](icons.md) for details).

Rendered result:

<i class="gf cisco-router"></i>

## Colour States

Apply a state class to indicate the network node’s status.

### gf-unknown

Marks the node as being in an unknown state.

Example:

``` html
<i class="gf gf-unknown cisco-router"></i>
```

Rendered result:

<i class="gf gf-unknown cisco-router"></i>

### gf-ok

Indicates the node is up and operational.

Example:

``` html
<i class="gf gf-ok cisco-router"></i>
```

Rendered result:

<i class="gf gf-ok cisco-router"></i>

### gf-warn

Indicates the node has active alarms or warnings.

Example:

``` html
<i class="gf gf-warn cisco-router"></i>
```

Rendered result:

<i class="gf gf-warn cisco-router"></i>

### gf-fail

Marks the node as in a critical failure state.

Example:

``` html
<i class="gf gf-fail cisco-router"></i>
```

Rendered result:

<i class="gf gf-fail cisco-router"></i>

## Colors

Gufo Font goes with predefined sets of colors styles:

| Style              | Color                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gf-black`         | <i class="gf gf-32px gf-black rectangle"></i> <i class="gf gf-32px gf-black rectangle-s"></i>  <i class="gf gf-32px gf-black rectangle-o"></i>                          |
| `gf-write`         | <i class="gf gf-32px gf-write rectangle"></i>  <i class="gf gf-32px gf-write rectangle-s"></i>  <i class="gf gf-32px gf-write rectangle-o"></i>                         |
| `gf-turquoise`     | <i class="gf gf-32px gf-turquoise rectangle"></i>  <i class="gf gf-32px gf-turquoise rectangle-s"></i>  <i class="gf gf-32px gf-turquoise rectangle-o"></i>             |
| `gf-emerald`       | <i class="gf gf-32px gf-emerald rectangle"></i>  <i class="gf gf-32px gf-emerald rectangle-s"></i>  <i class="gf gf-32px gf-emerald rectangle-o"></i>                   |
| `gf-green-sea`     | <i class="gf gf-32px gf-green-sea rectangle"></i>  <i class="gf gf-32px gf-green-sea rectangle-s"></i>  <i class="gf gf-32px gf-green-sea rectangle-o"></i>             |
| `gf-nephritis`     | <i class="gf gf-32px gf-nephritis rectangle"></i>  <i class="gf gf-32px gf-nephritis rectangle-s"></i>  <i class="gf gf-32px gf-nephritis rectangle-o"></i>             |
| `gf-sunflower`     | <i class="gf gf-32px gf-sunflower rectangle"></i>  <i class="gf gf-32px gf-sunflower rectangle-s"></i>  <i class="gf gf-32px gf-sunflower rectangle-o"></i>             |
| `gf-orange`        | <i class="gf gf-32px gf-orange rectangle"></i>  <i class="gf gf-32px gf-orange rectangle-s"></i>  <i class="gf gf-32px gf-orange rectangle-o"></i>                      |
| `gf-carrot`        | <i class="gf gf-32px gf-carrot rectangle"></i>  <i class="gf gf-32px gf-carrot rectangle-s"></i>  <i class="gf gf-32px gf-carrot rectangle-o"></i>                      |
| `gf-pumpkin`       | <i class="gf gf-32px gf-pumpkin rectangle"></i>  <i class="gf gf-32px gf-pumpkin rectangle-s"></i>  <i class="gf gf-32px gf-pumpkin rectangle-o"></i>                   |
| `gf-peter-river`   | <i class="gf gf-32px gf-peter-river rectangle"></i>  <i class="gf gf-32px gf-peter-river rectangle-s"></i>  <i class="gf gf-32px gf-peter-river rectangle-o"></i>       |
| `gf-belize-hole`   | <i class="gf gf-32px gf-belize-hole rectangle"></i>  <i class="gf gf-32px gf-belize-hole rectangle-s"></i>  <i class="gf gf-32px gf-belize-hole rectangle-o"></i>       |
| `gf-amethyst`      | <i class="gf gf-32px gf-amethyst rectangle"></i>  <i class="gf gf-32px gf-amethyst rectangle-s"></i>  <i class="gf gf-32px gf-amethyst rectangle-o"></i>                |
| `gf-wisteria`      | <i class="gf gf-32px gf-wisteria rectangle"></i>  <i class="gf gf-32px gf-wisteria rectangle-s"></i>  <i class="gf gf-32px gf-wisteria rectangle-o"></i>                |
| `gf-alizarin`      | <i class="gf gf-32px gf-alizarin rectangle"></i>  <i class="gf gf-32px gf-alizarin rectangle-s"></i>  <i class="gf gf-32px gf-alizarin rectangle-o"></i>                |
| `gf-pomegranade`   | <i class="gf gf-32px gf-pomegranade rectangle"></i>  <i class="gf gf-32px gf-pomegranade rectangle-s"></i>  <i class="gf gf-32px gf-pomegranade rectangle-o"></i>       |
| `gf-clouds`        | <i class="gf gf-32px gf-clouds rectangle"></i>  <i class="gf gf-32px gf-clouds rectangle-s"></i>  <i class="gf gf-32px gf-clouds rectangle-o"></i>                      |
| `gf-silver`        | <i class="gf gf-32px gf-silver rectangle"></i>  <i class="gf gf-32px gf-silver rectangle-s"></i>  <i class="gf gf-32px gf-silver rectangle-o"></i>                      |
| `gf-wet-asphalt`   | <i class="gf gf-32px gf-wet-asphalt rectangle"></i>  <i class="gf gf-32px gf-wet-asphalt rectangle-s"></i>  <i class="gf gf-32px gf-wet-asphalt rectangle-o"></i>       |
| `gf-midnight-blue` | <i class="gf gf-32px gf-midnight-blue rectangle"></i>  <i class="gf gf-32px gf-midnight-blue rectangle-s"></i>  <i class="gf gf-32px gf-midnight-blue rectangle-o"></i> |
| `gf-concrete`      | <i class="gf gf-32px gf-concrete rectangle"></i>  <i class="gf gf-32px gf-concrete rectangle-s"></i>  <i class="gf gf-32px gf-concrete rectangle-o"></i>                |
| `gf-asbestos`      | <i class="gf gf-32px gf-asbestos rectangle"></i>  <i class="gf gf-32px gf-asbestos rectangle-s"></i>  <i class="gf gf-32px gf-asbestos rectangle-o"></i>                |

## Size

Default network node size is 64x64px. You can adjust it using "scale classes".

### Default

Default size (64x64px). Rendered result:

<i class="gf cisco-router"></i>

### gf-2x

Doubles icon size.

Example:

``` html
<i class="gf gf-2x cisco-router"></i>
```

Rendered result:

<i class="gf gf-2x cisco-router"></i>

### gf-3x

Triples icon size.

Example:

``` html
<i class="gf gf-3x cisco-router"></i>
```

Rendered result:

<i class="gf gf-3x cisco-router"></i>

### Exact Sizes

You can also set an exact icon size using pixel-based classes:

| `gf-16px`                               | `gf-24px`                               | `gf-32px`                               | `gf-48px`                               | Default                         |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------- |
| <i class="gf gf-16px cisco-router"></i> | <i class="gf gf-24px cisco-router"></i> | <i class="gf gf-32px cisco-router"></i> | <i class="gf gf-48px cisco-router"></i> | <i class="gf cisco-router"></i> |

### Arbitrary Sizes

You can set an arbitrary size using `--gf-size` variable:

``` html
<i class="gf gf-3x cisco-router" style="--gf-size:100px"></i>
```

Renders as:

<i class="gf gf-3x cisco-router" style="--gf-size:100px"></i>

## Rotation

You can rotate glyph using "rotation classes". Rotation angles are measured clockwise:

| Default                         | `gf-r90`                               | `gf-r180`                               | `gf-270`                                |
| ------------------------------- | -------------------------------------- | --------------------------------------- | --------------------------------------- |
| <i class="gf cisco-router"></i> | <i class="gf gf-r90 cisco-router"></i> | <i class="gf gf-r180 cisco-router"></i> | <i class="gf gf-r270 cisco-router"></i> |

To rotate an arbitrary angle use `gf-rotate` class along with `--gf-rotate` variable:

``` html
<i class="gf gf-rotate cisco-router" style="--gf-rotate:33deg"></i>
```

Rendered as:

<i class="gf gf-rotate cisco-router" style="--gf-rotate:33deg"></i>

## Flipping

In addition to rotation, you can flip (mirror) a glyph across the vertical axis (gf-flip-v), the horizontal axis (gf-flip-h), or both axes (gf-flip).

| Default                | `gf-flip-v`                      | `gf-flip-h`                      | `gf-flip`                      |
| ---------------------- | -------------------------------- | -------------------------------- | ------------------------------ |
| <i class="gf cloud-o"> | <i class="gf gf-flip-v cloud-o"> | <i class="gf gf-flip-h cloud-o"> | <i class="gf gf-flip cloud-o"> |

## Subscript and Superscript

Subscript and superscript glyphs are smaller variants used to annotate or modify other icons.
They are positioned relative to a base symbol using predefined CSS classes.

### Subscript

Subscript glyphs are rendered below the baseline:

```
O<i class="gf gf-sub check-s"></a>
```

Rendered result:

O<i class="gf gf-sub check-s"></i>

### Superscript

Superscript glyphs are rendered above the baseline:

```
O<i class="gf gf-sup check-s"></a>
```

Rendered result:

O<i class="gf gf-sup check-s"></i>


## Stacking

Glyphs can be stacked together using `gf-stack` class:

``` html
<span class="gf-stack">
    <i class="gf rectangle-o"></i>
    <i class="gf gf-ok star-small-s"></i>
</span>
```

Rendered result:

<span class="gf-stack">
    <i class="gf rectangle-o"></i>
    <i class="gf gf-ok star-small-s"></i>
</span>