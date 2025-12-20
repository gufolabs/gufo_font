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

## Alphabet

### Numbers

> <span class="gf">0123456789</span>

### Latin

> <span class="gf">THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG</span>

### Russian

> <span class="gf">СЪЕШЬ ЖЕ ЕЩЕ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК, ДА ВЫПЕЙ ЧАЮ</span>

