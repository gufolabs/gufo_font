---
hide:
    - navigation
---
## Add CSS

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

## Glyph Size

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

### Exact sizes

You can also set an exact icon size using pixel-based classes:

| `gf-16px`                               | `gf-24px`                               | `gf-32px`                               | `gf-48px`                               | Default                         |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------- |
| <i class="gf gf-16px cisco-router"></i> | <i class="gf gf-24px cisco-router"></i> | <i class="gf gf-32px cisco-router"></i> | <i class="gf gf-48px cisco-router"></i> | <i class="gf cisco-router"></i> |

## Glyph Rotation

You can rotate glyph using "rotation classes". Rotation angles are measured clockwise:

| Default                         | `gf-r90`                               | `gf-r180`                               | `gf-270`                                |
| ------------------------------- | -------------------------------------- | --------------------------------------- | --------------------------------------- |
| <i class="gf cisco-router"></i> | <i class="gf gf-r90 cisco-router"></i> | <i class="gf gf-r180 cisco-router"></i> | <i class="gf gf-r270 cisco-router"></i> |