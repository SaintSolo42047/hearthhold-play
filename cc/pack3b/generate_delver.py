#!/usr/bin/env python3
"""HearthHold Pack 3b — delver walk-cycle fix.
Based on Pack 3; redraws mid-stride (frame 2 all dirs) and side frame 3
leg separation. Frame 0 idle copied bit-identical from Pack 3.
Hard-pixel 32x32 RGBA. No DF/Kenney/third-party copies.
"""
from pathlib import Path
from PIL import Image
import shutil

SRC_PACK3 = Path("/workspace/hearthhold-pack3-delver")
OUT = Path("/workspace/hearthhold-pack3b-delver-fix")
DELVERS = OUT / "delvers"
SIZE = 32

# Limited palette — gray armor recolorable; skin & hair fixed (unchanged from Pack 3)
PAL = {
    "_": None,
    "O": (24, 24, 28, 255),       # outline
    "A": (100, 104, 114, 255),    # armor mid
    "a": (70, 74, 84, 255),       # armor dark
    "H": (148, 152, 162, 255),    # armor highlight
    "S": (210, 160, 120, 255),    # skin
    "s": (176, 124, 92, 255),     # skin shade
    "R": (96, 60, 40, 255),       # hair
    "r": (70, 42, 28, 255),       # hair shade
    "B": (56, 48, 44, 255),       # boots
    "b": (38, 32, 30, 255),       # boot shade
    "C": (130, 118, 72, 255),     # belt brass
    "c": (96, 86, 52, 255),       # belt shade
    "E": (32, 36, 48, 255),       # eye pupil
    "W": (230, 230, 236, 255),    # eye white
    "P": (88, 92, 102, 255),      # pack
    "p": (58, 62, 70, 255),       # pack dark
}

FOOT_Y = 27  # fixed boot-bottom baseline (lower third) — no hop


def blank():
    return [["_" for _ in range(SIZE)] for _ in range(SIZE)]


def put(g, x, y, ch):
    if 0 <= x < SIZE and 0 <= y < SIZE and ch != "_":
        g[y][x] = ch


def rect(g, x0, y0, x1, y1, ch):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            put(g, x, y, ch)


def outline_box(g, x0, y0, x1, y1):
    for x in range(x0, x1 + 1):
        put(g, x, y0, "O")
        put(g, x, y1, "O")
    for y in range(y0, y1 + 1):
        put(g, x0, y, "O")
        put(g, x1, y, "O")


# ---- heads (unchanged from Pack 3) ----------------------------------------

def head_down(g):
    rect(g, 11, 6, 20, 8, "R")
    rect(g, 11, 7, 20, 8, "R")
    for x in (12, 15, 18):
        put(g, x, 7, "r")
    rect(g, 11, 9, 20, 13, "S")
    for y in range(9, 14):
        put(g, 11, y, "s")
        put(g, 20, y, "s")
    put(g, 13, 10, "W"); put(g, 14, 10, "E")
    put(g, 17, 10, "W"); put(g, 18, 10, "E")
    put(g, 15, 11, "s"); put(g, 16, 11, "s")
    put(g, 15, 12, "s"); put(g, 16, 12, "s")
    outline_box(g, 10, 6, 21, 13)
    for x in range(12, 20):
        put(g, x, 8, "R")
    put(g, 13, 8, "r"); put(g, 18, 8, "r")


def head_up(g):
    rect(g, 11, 6, 20, 13, "R")
    for y in range(7, 13):
        put(g, 11, y, "r")
        put(g, 20, y, "r")
    for x in (13, 15, 17):
        put(g, x, 8, "r")
        put(g, x, 10, "r")
    outline_box(g, 10, 6, 21, 13)


def head_side(g, facing):
    rect(g, 11, 6, 20, 13, "S")
    rect(g, 11, 6, 20, 8, "R")
    if facing == "right":
        for y in range(7, 12):
            put(g, 11, y, "R")
            put(g, 12, y, "r")
        for y in range(9, 13):
            put(g, 19, y, "s")
        put(g, 17, 10, "W"); put(g, 18, 10, "E")
        put(g, 18, 11, "s")
    else:
        for y in range(7, 12):
            put(g, 20, y, "R")
            put(g, 19, y, "r")
        for y in range(9, 13):
            put(g, 12, y, "s")
        put(g, 14, 10, "E"); put(g, 13, 10, "W")
        put(g, 13, 11, "s")
    outline_box(g, 10, 6, 21, 13)


# ---- torso (unchanged from Pack 3) ----------------------------------------

def torso_front(g):
    rect(g, 11, 14, 20, 19, "A")
    for y in range(14, 20):
        put(g, 11, y, "a")
        put(g, 20, y, "a")
        put(g, 12, y, "H")
    rect(g, 14, 15, 17, 16, "H")
    put(g, 15, 17, "H"); put(g, 16, 17, "H")
    rect(g, 12, 18, 19, 18, "C")
    rect(g, 12, 19, 19, 19, "c")
    put(g, 15, 18, "H"); put(g, 16, 18, "H")
    put(g, 14, 14, "S"); put(g, 15, 14, "S"); put(g, 16, 14, "S"); put(g, 17, 14, "s")
    outline_box(g, 11, 14, 20, 19)


def torso_back(g):
    rect(g, 11, 14, 20, 19, "A")
    for y in range(14, 20):
        put(g, 11, y, "a")
        put(g, 20, y, "a")
    rect(g, 13, 15, 18, 18, "P")
    for y in range(15, 19):
        put(g, 13, y, "p")
        put(g, 18, y, "p")
    put(g, 15, 16, "a"); put(g, 16, 16, "a")
    rect(g, 12, 19, 19, 19, "c")
    put(g, 14, 19, "C"); put(g, 15, 19, "C"); put(g, 16, 19, "C"); put(g, 17, 19, "C")
    outline_box(g, 11, 14, 20, 19)
    outline_box(g, 13, 15, 18, 18)


def torso_side(g, facing):
    rect(g, 12, 14, 19, 19, "A")
    for y in range(14, 20):
        put(g, 12, y, "a")
        put(g, 19, y, "a")
        put(g, 13, y, "H")
    rect(g, 13, 18, 18, 18, "C")
    rect(g, 13, 19, 18, 19, "c")
    put(g, 15, 18, "H")
    if facing == "right":
        for y in range(15, 19):
            put(g, 12, y, "P")
            put(g, 13, y, "p")
        put(g, 12, 15, "O"); put(g, 12, 18, "O")
    else:
        for y in range(15, 19):
            put(g, 19, y, "P")
            put(g, 18, y, "p")
        put(g, 19, 15, "O"); put(g, 19, 18, "O")
    put(g, 14, 14, "S"); put(g, 15, 14, "S"); put(g, 16, 14, "s")
    outline_box(g, 12, 14, 19, 19)


# ---- limbs -----------------------------------------------------------------

def boot(g, x0, x1, bottom_y):
    """Draw boot with sole at bottom_y (FOOT_Y or FOOT_Y-1 if lifted)."""
    top = bottom_y - 2
    rect(g, x0, top, x1, bottom_y, "B")
    for x in range(x0, x1 + 1):
        put(g, x, bottom_y, "b")
    put(g, x0, top, "O"); put(g, x1, top, "O")
    put(g, x0, bottom_y, "O"); put(g, x1, bottom_y, "O")
    for x in range(x0, x1 + 1):
        put(g, x, bottom_y, "b")
    put(g, x0, bottom_y, "O")
    put(g, x1, bottom_y, "O")


def leg_col(g, x0, x1, y0, y1, shade="a"):
    rect(g, x0, y0, x1, y1, shade)
    for y in range(y0, y1 + 1):
        put(g, x0, y, "O")
        put(g, x1, y, "O")


def legs_frontish(g, frame):
    """Front/back legs. Foot baseline FOOT_Y.
    0 stand (idle); 1 L-contact; 2 opposite mid-stride (R forward); 3 R-contact recover.
    Frame 2 deliberately large vs idle (not a near-identical pass).
    """
    # (L_dx, L_lift, R_dx, R_lift)  lift 1 => sole at FOOT_Y-1
    table = {
        0: (0, 0, 0, 0),
        1: (-2, 0, 2, 1),   # L planted out, R lifted out — wide contact
        2: (-2, 1, 2, 0),   # OPPOSITE mid-stride: same wide stance, opposite foot planted
        3: (1, 1, -1, 0),   # recover inward toward idle — two distinct columns
    }
    ldx, llift, rdx, rlift = table[frame]
    ly0 = 20
    lx0, lx1 = 12 + ldx, 14 + ldx
    rx0, rx1 = 17 + rdx, 19 + rdx
    lb = FOOT_Y - llift
    rb = FOOT_Y - rlift
    leg_col(g, lx0, lx1, ly0, lb - 3, "a")
    leg_col(g, rx0, rx1, ly0, rb - 3, "a")
    boot(g, lx0, lx1, lb)
    boot(g, rx0, rx1, rb)


def legs_side(g, frame, facing):
    """Side legs with guaranteed near/far column separation on stride frames.
    Pack 3 bug: frame 3 ±1 dx collapsed near+far into one pillar (~176 opaque).
    Pack 3b: amplitude keeps two distinct columns; opaque stays ~200.
    """
    fwd = 1 if facing == "right" else -1
    # near_dx, near_lift, far_dx, far_lift  (+ = toward facing)
    # Amplitude chosen so near/far never share the same 3px column on frames 1–3.
    table = {
        0: (0, 0, 0, 0),
        1: (2 * fwd, 0, -2 * fwd, 1),   # near planted forward, far lifted back
        2: (-3 * fwd, 1, 3 * fwd, 0),   # OPPOSITE mid-stride: near back lifted, far forward plant
        3: (-4 * fwd, 1, 2 * fwd, 0),   # recover; keep gap between columns (not one pillar)
    }
    ndx, nl, fdx, fl = table[frame]
    ly0 = 20
    # Base columns overlap slightly at rest (profile idle). Stride amps pull them apart.
    if facing == "right":
        far = (13, 15)
        near = (15, 17)
    else:
        far = (16, 18)
        near = (14, 16)

    def one(xpair, dx, lift, shade):
        x0, x1 = xpair[0] + dx, xpair[1] + dx
        # clamp softly inside canvas
        x0 = max(0, min(SIZE - 1, x0))
        x1 = max(0, min(SIZE - 1, x1))
        if x1 < x0:
            x0, x1 = x1, x0
        bottom = FOOT_Y - lift
        leg_col(g, x0, x1, ly0, bottom - 3, shade)
        boot(g, x0, x1, bottom)

    one(far, fdx, fl, "a")
    one(near, ndx, nl, "A")


def arms_down(g, frame):
    # Stronger swing on frame 2 so mid-stride reads clearly vs idle
    swing = {0: 0, 1: 1, 2: -1, 3: -1}[frame]
    for i in range(5):
        ly = 15 + i + (swing if i >= 2 else 0)
        ry = 15 + i + (-swing if i >= 2 else 0)
        put(g, 9, ly, "A"); put(g, 8, ly, "O")
        put(g, 22, ry, "A"); put(g, 23, ry, "O")
    put(g, 9, 19 + swing, "S")
    put(g, 22, 19 - swing, "S")


def arms_up(g, frame):
    swing = {0: 0, 1: 1, 2: -1, 3: -1}[frame]
    for i in range(5):
        ly = 15 + i + (-swing if i >= 2 else 0)
        ry = 15 + i + (swing if i >= 2 else 0)
        put(g, 9, ly, "A"); put(g, 8, ly, "O")
        put(g, 22, ry, "A"); put(g, 23, ry, "O")
    put(g, 9, 19 - swing, "S")
    put(g, 22, 19 + swing, "S")


def arms_side(g, frame, facing):
    # Frame 2 uses opposite arm pose vs frame 1 (matches opposite leg stride)
    if facing == "right":
        if frame == 0:
            fx, bx = 20, 11
        elif frame == 1:
            fx, bx = 21, 10
        elif frame == 2:
            fx, bx = 18, 13   # opposite reach — clear vs idle/frame1
        else:
            fx, bx = 19, 12
        for i in range(4):
            put(g, fx, 15 + i, "A"); put(g, fx + 1, 15 + i, "O")
            put(g, bx, 15 + i, "a"); put(g, bx - 1, 15 + i, "O")
        put(g, fx, 18, "S"); put(g, bx, 18, "s")
    else:
        if frame == 0:
            fx, bx = 11, 20
        elif frame == 1:
            fx, bx = 10, 21
        elif frame == 2:
            fx, bx = 13, 18
        else:
            fx, bx = 12, 19
        for i in range(4):
            put(g, fx, 15 + i, "A"); put(g, fx - 1, 15 + i, "O")
            put(g, bx, 15 + i, "a"); put(g, bx + 1, 15 + i, "O")
        put(g, fx, 18, "S"); put(g, bx, 18, "s")


# ---- compose ---------------------------------------------------------------

def compose(direction, frame):
    g = blank()
    if direction == "down":
        legs_frontish(g, frame)
        torso_front(g)
        arms_down(g, frame)
        head_down(g)
    elif direction == "up":
        legs_frontish(g, frame)
        torso_back(g)
        arms_up(g, frame)
        head_up(g)
    elif direction == "right":
        legs_side(g, frame, "right")
        torso_side(g, "right")
        arms_side(g, frame, "right")
        head_side(g, "right")
    elif direction == "left":
        legs_side(g, frame, "left")
        torso_side(g, "left")
        arms_side(g, frame, "left")
        head_side(g, "left")
    return g


def grid_to_image(g):
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            col = PAL.get(g[y][x])
            if col is not None:
                px[x, y] = col
    return img


def harden(img):
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            r, g, b, a = px[x, y]
            px[x, y] = (0, 0, 0, 0) if a == 0 else (r, g, b, 255)
    return img


def make_preview(frames):
    dirs = ["down", "left", "right", "up"]
    pad, cell = 2, 32
    w = h = 4 * cell + 5 * pad
    sheet = Image.new("RGBA", (w, h), (40, 44, 52, 255))
    for ri, d in enumerate(dirs):
        for fi in range(4):
            x = pad + fi * (cell + pad)
            y = pad + ri * (cell + pad)
            for cy in range(cell):
                for cx in range(cell):
                    c = (60, 64, 72, 255) if ((cx // 4) + (cy // 4)) % 2 == 0 else (48, 52, 60, 255)
                    sheet.putpixel((x + cx, y + cy), c)
            sheet.alpha_composite(frames[(d, fi)], (x, y))
    return sheet


def main():
    DELVERS.mkdir(parents=True, exist_ok=True)
    src_delvers = SRC_PACK3 / "delvers"
    frames = {}

    for d in ("down", "left", "right", "up"):
        for f in range(4):
            path = DELVERS / f"delver_{d}_{f}.png"
            if f == 0:
                # Frame 0 idle: copy bit-identical from Pack 3
                shutil.copy2(src_delvers / path.name, path)
                img = Image.open(path).convert("RGBA")
            else:
                img = harden(grid_to_image(compose(d, f)))
                img.save(path, "PNG")
            frames[(d, f)] = img
            print("wrote", path.name)

    preview = make_preview(frames)
    preview.save(OUT / "preview_sheet.png")
    print("wrote preview_sheet.png")

    (OUT / "README.md").write_text(
        """# HearthHold Pack 3b — Delver Walk Cycle (fix)

Original 32×32 hard-pixel delver sprites for **Grok Build / HearthHold**.

Revision of Pack 3 addressing walk-cycle feedback.

## 3b fixes

- **Frame 2 (all directions):** real mid-stride / opposite-leg PASS pose with substantial pixel difference from idle frame 0 (no longer an 8–9 px near-duplicate).
- **Side views frame 3 (left & right):** separated front/back leg columns — not stacked into one pillar. Opaque pixel count stays near ~200.
- **Frame 0:** standing/idle copied bit-identical from Pack 3 for all directions.
- Head, armor colors/shape, skin/hair unchanged; feet baseline y≈27; 32×32 hard alpha; no hop.

## Contents

- `delvers/` — 16 RGBA PNGs (4 directions × 4 frames)
- `preview_sheet.png` — 4×4 sheet (rows: down, left, right, up; cols: frames 0–3)
- `CREDITS.txt`
- `generate_delver.py` — Pillow generator (reproducible)

## Filenames

| Direction | Frames |
|-----------|--------|
| down | `delver_down_0.png` … `delver_down_3.png` |
| left | `delver_left_0.png` … `delver_left_3.png` |
| right | `delver_right_0.png` … `delver_right_3.png` |
| up | `delver_up_0.png` … `delver_up_3.png` |

Frame 0 = standing idle; frames 1–3 = walk cycle (1 contact, 2 opposite mid-stride, 3 recover).

## Specs

- Size: 32×32 RGBA, hard alpha (no AA fringing)
- Top-down readable silhouette
- Centered horizontally; feet in the lower third (boot baseline y=27)
- Neutral **gray** armor (recolorable); skin and hair colors stay fixed across frames
- Limited palette, hard pixels, consistent registration (no hop)

## Usage

Recolor armor grays in your pipeline; leave skin/hair unchanged for identity.
""",
        encoding="utf-8",
    )
    (OUT / "CREDITS.txt").write_text(
        "Original pixel art for HearthHold\n"
        "Created procedurally with Python + Pillow for HearthHold Pack 3b (Grok Build).\n"
        "Revision of Pack 3 walk-cycle frames; not derived from Dwarf Fortress, Kenney,\n"
        "or other third-party sprite packs.\n",
        encoding="utf-8",
    )
    print("wrote README.md CREDITS.txt")


if __name__ == "__main__":
    main()
