# Calibration Chart

This calibration chart is used for debugging and testing purposes.

## Bounding Box

`X` sign must be surrounded by red box (without gap):

<i class="gf xmark-s" style="border: 1px solid red"></i>

<i class="gf gf-2x xmark-s" style="border: 1px solid red"></i>

<i class="gf gf-2x xmark-s" style="border: 1px solid red; --gf-size: 200px"></i>

## Inline Text

Logo must be aligned with following text on baseline:

<span style="border: 1px solid red; display: inline-block"><i class="gf brand-gufolabs-s"></i> Gufo Labs</span>

## Vertical and Horizontal Gap

Four `X` signs must touch each other.

<i class="gf xmark-s"></i><i class="gf xmark-s"></i>

<i class="gf xmark-s"></i><i class="gf xmark-s"></i>

## Canvas

<style>
    #c1 {
        border: 1px solid white;
    }
</style>


<canvas id="c1" width="256" height="256"></canvas>
<script>
    const canvas = document.getElementById("c1");
    const ctx = canvas.getContext("2d");
    // Background
    ctx.fillStyle = "#1abc9c";
    ctx.fillRect(0, 0, 256, 256);
    // Cross lines
    ctx.strokeStyle = "red";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(128, 0);
    ctx.lineTo(128, 256);
    ctx.moveTo(0, 128);
    ctx.lineTo(256, 128);
    ctx.stroke();
    // Glyph
    //ctx.fillStyle = "black";
    ctx.font = "64px GufoFont";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // Replace with actual glyph codepoint if needed
    ctx.fillText("\uF22C", 128, 128); // cisco-router glyph
</script>