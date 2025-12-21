# Calibration Chart

This calibration chart is used for debugging and testing purposes.

## Bounding Box

`X` sign must be surrounded by red box (without gap):

<i class="gf gf-1x xmark-s" style="border: 1px solid red"></i>

<i class="gf gf-2x xmark-s" style="border: 1px solid red"></i>

<i class="gf gf-2x xmark-s" style="border: 1px solid red; --gf-size: 200px"></i>

## Inline Text

Logo must be aligned with following text on baseline:

<span style="border: 1px solid red; display: inline-block"><i class="gf brand-gufolabs-s"></i> Gufo Labs</span>

Larger text:

<span style="border: 1px solid red; display: inline-block; font-size: 128px"><i class="gf brand-gufolabs-s"></i> Gufo Labs</span>

##  Horizontal Gap

Four `X` signs must touch each other.

<i class="gf xmark-s"></i><i class="gf xmark-s"></i><i class="gf xmark-s"></i><i class="gf xmark-s"></i>

## Canvas

<script>
    async function draw(selector, icon) {
        const canvas = document.getElementById(selector);
        const ctx = canvas.getContext("2d");
        const H = 256;
        const W = H;
        const ICON = 64;
        await document.fonts.load("64px Gufo");
        await document.fonts.ready;
        // Background
        ctx.fillStyle = "#1abc9c";
        ctx.fillRect(0, 0, W, H);
        // Central area
        ctx.fillStyle = "#16a085";
        ctx.fillRect(W/2-ICON/2, H/2-ICON/2, ICON, ICON);
        // Cross lines
        ctx.strokeStyle = "red";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(W / 2, 0);
        ctx.lineTo(W / 2, H);
        ctx.moveTo(0, H / 2);
        ctx.lineTo(W, H / 2);
        ctx.stroke();
        // Glyph
        ctx.fillStyle = "black";
        ctx.font = "64px GufoFont";
        // Replace with actual glyph codepoint if needed
        ctx.fillText(icon, W / 2 - ICON / 2, H / 2 + ICON / 2); // cisco-router glyph
    };
</script>

### Square Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full width and height of the gray square.

<canvas id="c1" width="256" height="256"></canvas>
<script>
    draw("c1", "\uF400");
</script>

### Horizontal Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full width of the gray square and to be
vertically centered.

<canvas id="c2" width="256" height="256"></canvas>
<script>
    draw("c2", "\uF22C");
</script>

### Vertical Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full height of the gray square and to be
horizontally centered.

<canvas id="c3" width="256" height="256"></canvas>
<script>
    draw("c3", "2");
</script>

## SVG

### Square Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full width and height of the gray square.

<svg width="256" height="256" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="256" height="256" fill="#1abc9c" />
    <!-- Central area -->
    <rect x="96" y="96" width="64" height="64" fill="#16a085" />
    <!-- Cross lines -->
    <line x1="128" y1="0" x2="128" y2="256" stroke="red" stroke-width="1"/>
    <line x1="0" y1="128" x2="256" y2="128" stroke="red" stroke-width="1"/>
    <!-- Glyph (cisco-router) -->
    <text x="96" y="160" font-family="GufoFont" font-size="64" fill="black">&#xF400;</text>
</svg>

### Horizontal Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full width of the gray square and to be
vertically centered.

<svg width="256" height="256" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="256" height="256" fill="#1abc9c" />
    <!-- Central area -->
    <rect x="96" y="96" width="64" height="64" fill="#16a085" />
    <!-- Cross lines -->
    <line x1="128" y1="0" x2="128" y2="256" stroke="red" stroke-width="1"/>
    <line x1="0" y1="128" x2="256" y2="128" stroke="red" stroke-width="1"/>
    <!-- Glyph (cisco-router) -->
    <text x="96" y="160" font-family="GufoFont" font-size="64" fill="black">&#xF22C;</text>
</svg>

### Vertical Icon

You must see turquose square with centered darker square, red cross and the router
perfectly aligned on center. It must fill full height of the gray square and to be
horizontally centered.

<svg width="256" height="256" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="256" height="256" fill="#1abc9c" />
    <!-- Central area -->
    <rect x="96" y="96" width="64" height="64" fill="#16a085" />
    <!-- Cross lines -->
    <line x1="128" y1="0" x2="128" y2="256" stroke="red" stroke-width="1"/>
    <line x1="0" y1="128" x2="256" y2="128" stroke="red" stroke-width="1"/>
    <!-- Glyph (cisco-router) -->
    <text x="96" y="160" font-family="GufoFont" font-size="64" fill="black">2</text>
</svg>


## Alphabet

### Numbers

> <span class="gf">0123456789</span>

### Latin

> <span class="gf">THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG</span>

### Russian

> <span class="gf">СЪЕШЬ ЖЕ ЕЩЕ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК, ДА ВЫПЕЙ ЧАЮ</span>

