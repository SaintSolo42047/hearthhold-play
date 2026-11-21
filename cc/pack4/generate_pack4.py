#!/usr/bin/env python3
"""HearthHold Pack 4 — creatures + ore nuggets.
Original hard-pixel Pillow art for Grok Build / HearthHold.
NO DF / Kenney / third-party copies.
Creatures: 32x32 RGBA hard alpha, facing DOWN, no walk cycle, no floor baked in.
Nuggets: 16x16 RGBA hard alpha, loose chunks, no tile background.
"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path("/workspace/hearthhold-pack4-creatures-nuggets")
CREATURES = OUT / "creatures"
NUGGETS = OUT / "nuggets"
SIZE = 32
NUG_SIZE = 16


def blank(sz=SIZE):
    return [["_" for _ in range(sz)] for _ in range(sz)]


def put(g, x, y, ch, sz=None):
    h = len(g)
    w = len(g[0])
    if 0 <= x < w and 0 <= y < h and ch != "_":
        g[y][x] = ch


def rect(g, x0, y0, x1, y1, ch):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            put(g, x, y, ch)


def outline_box(g, x0, y0, x1, y1, ch="O"):
    for x in range(x0, x1 + 1):
        put(g, x, y0, ch)
        put(g, x, y1, ch)
    for y in range(y0, y1 + 1):
        put(g, x0, y, ch)
        put(g, x1, y, ch)


def render(g, pal, path):
    h = len(g)
    w = len(g[0])
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = im.load()
    for y in range(h):
        for x in range(w):
            ch = g[y][x]
            if ch != "_" and ch in pal and pal[ch] is not None:
                c = pal[ch]
                # hard alpha only
                px[x, y] = (c[0], c[1], c[2], 255)
    im.save(path)
    return im


def harden(im):
    """Force hard alpha 0/255 (no AA fringing)."""
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 128:
                px[x, y] = (0, 0, 0, 0)
            else:
                px[x, y] = (r, g, b, 255)
    return im


# =============================================================================
# GOBLIN — greener, smaller than orc, ~delver height, feet y=27
# Slightly narrower/shorter than delver; pointed ears; green skin.
# =============================================================================
GOBLIN_PAL = {
    "O": (20, 28, 18, 255),
    "G": (72, 148, 58, 255),     # skin mid
    "g": (48, 108, 40, 255),     # skin dark
    "H": (110, 180, 90, 255),    # skin highlight
    "A": (90, 70, 48, 255),      # ragged tunic
    "a": (64, 48, 32, 255),
    "B": (50, 42, 36, 255),      # feet
    "b": (34, 28, 24, 255),
    "E": (220, 40, 40, 255),     # eye glow
    "W": (240, 230, 180, 255),   # tooth
    "R": (40, 80, 36, 255),      # ear/hair tuft
    "C": (120, 100, 50, 255),    # belt
}


def draw_goblin():
    g = blank()
    # pointed ears
    put(g, 9, 9, "R"); put(g, 9, 10, "G"); put(g, 10, 10, "G")
    put(g, 22, 9, "R"); put(g, 22, 10, "G"); put(g, 21, 10, "G")
    # head (narrower than delver: x11-20 -> x11-20 but shorter)
    rect(g, 11, 8, 20, 14, "G")
    for y in range(8, 15):
        put(g, 11, y, "g")
        put(g, 20, y, "g")
    rect(g, 12, 8, 19, 9, "H")
    # eyes looking down
    put(g, 13, 11, "E"); put(g, 14, 11, "E")
    put(g, 17, 11, "E"); put(g, 18, 11, "E")
    # snoutish nose / mouth
    put(g, 15, 12, "g"); put(g, 16, 12, "g")
    put(g, 15, 13, "W"); put(g, 16, 13, "g")
    outline_box(g, 10, 8, 21, 14)
    put(g, 9, 9, "O"); put(g, 22, 9, "O")
    # neck
    rect(g, 14, 15, 17, 15, "g")
    # torso (slightly smaller)
    rect(g, 12, 16, 19, 21, "A")
    for y in range(16, 22):
        put(g, 12, y, "a")
        put(g, 19, y, "a")
    rect(g, 13, 20, 18, 20, "C")
    outline_box(g, 12, 16, 19, 21)
    # arms
    rect(g, 9, 16, 11, 20, "G")
    rect(g, 20, 16, 22, 20, "G")
    for y in range(16, 21):
        put(g, 9, y, "g")
        put(g, 22, y, "g")
    put(g, 9, 16, "O"); put(g, 10, 16, "O"); put(g, 11, 16, "O")
    put(g, 20, 16, "O"); put(g, 21, 16, "O"); put(g, 22, 16, "O")
    put(g, 9, 20, "O"); put(g, 22, 20, "O")
    # hands
    put(g, 9, 21, "g"); put(g, 10, 21, "G")
    put(g, 21, 21, "G"); put(g, 22, 21, "g")
    # legs (feet bottom at y=27)
    rect(g, 13, 22, 15, 25, "g")
    rect(g, 16, 22, 18, 25, "g")
    for y in range(22, 26):
        put(g, 13, y, "O"); put(g, 15, y, "O")
        put(g, 16, y, "O"); put(g, 18, y, "O")
    # boots / feet y=26-27
    rect(g, 12, 26, 15, 27, "B")
    rect(g, 16, 26, 19, 27, "B")
    put(g, 12, 26, "b"); put(g, 19, 26, "b")
    for x in range(12, 16):
        put(g, x, 27, "b")
    for x in range(16, 20):
        put(g, x, 27, "b")
    outline_box(g, 12, 26, 15, 27)
    outline_box(g, 16, 26, 19, 27)
    return g


# =============================================================================
# ORC — larger/brutish than goblin, ~delver height, feet y=27
# Broader shoulders, tusks, olive-grey green skin, thicker build.
# =============================================================================
ORC_PAL = {
    "O": (22, 24, 18, 255),
    "G": (88, 118, 62, 255),     # olive skin
    "g": (58, 82, 40, 255),
    "H": (120, 150, 90, 255),
    "A": (70, 74, 82, 255),      # dark armor scraps
    "a": (48, 50, 56, 255),
    "L": (110, 114, 124, 255),   # armor highlight
    "B": (42, 36, 32, 255),
    "b": (28, 24, 22, 255),
    "E": (200, 50, 40, 255),
    "W": (235, 225, 200, 255),   # tusks
    "C": (140, 110, 50, 255),
}


def draw_orc():
    g = blank()
    # broader head
    rect(g, 10, 6, 21, 14, "G")
    for y in range(6, 15):
        put(g, 10, y, "g")
        put(g, 21, y, "g")
    rect(g, 11, 6, 20, 8, "H")
    # brow ridge
    rect(g, 11, 9, 20, 10, "g")
    # eyes
    put(g, 12, 11, "E"); put(g, 13, 11, "E")
    put(g, 18, 11, "E"); put(g, 19, 11, "E")
    # nose
    put(g, 15, 12, "g"); put(g, 16, 12, "g")
    # tusks
    put(g, 13, 13, "W"); put(g, 14, 14, "W")
    put(g, 18, 13, "W"); put(g, 17, 14, "W")
    put(g, 15, 13, "g"); put(g, 16, 13, "g")
    outline_box(g, 9, 6, 22, 14)
    # thick neck
    rect(g, 13, 15, 18, 15, "g")
    # broad torso
    rect(g, 10, 16, 21, 21, "A")
    for y in range(16, 22):
        put(g, 10, y, "a")
        put(g, 21, y, "a")
        put(g, 11, y, "L")
    rect(g, 12, 17, 19, 18, "L")
    rect(g, 11, 20, 20, 20, "C")
    outline_box(g, 10, 16, 21, 21)
    # thick arms
    rect(g, 7, 16, 9, 21, "G")
    rect(g, 22, 16, 24, 21, "G")
    for y in range(16, 22):
        put(g, 7, y, "g")
        put(g, 24, y, "g")
    outline_box(g, 7, 16, 9, 21)
    outline_box(g, 22, 16, 24, 21)
    put(g, 7, 22, "g"); put(g, 8, 22, "G")
    put(g, 23, 22, "G"); put(g, 24, 22, "g")
    # thick legs
    rect(g, 12, 22, 14, 25, "g")
    rect(g, 17, 22, 19, 25, "g")
    for y in range(22, 26):
        put(g, 12, y, "O"); put(g, 14, y, "O")
        put(g, 17, y, "O"); put(g, 19, y, "O")
    # boots feet y=26-27
    rect(g, 11, 26, 15, 27, "B")
    rect(g, 16, 26, 20, 27, "B")
    for x in range(11, 16):
        put(g, x, 27, "b")
    for x in range(16, 21):
        put(g, x, 27, "b")
    outline_box(g, 11, 26, 15, 27)
    outline_box(g, 16, 26, 20, 27)
    return g


# =============================================================================
# TROLL — bulky, fills most of canvas, feet y=27
# Huge hunched body, long arms, mottled grey-green.
# =============================================================================
TROLL_PAL = {
    "O": (18, 22, 16, 255),
    "G": (96, 130, 78, 255),
    "g": (64, 92, 52, 255),
    "H": (130, 160, 110, 255),
    "M": (80, 100, 70, 255),     # mottling
    "A": (70, 58, 48, 255),      # loincloth
    "a": (48, 38, 32, 255),
    "B": (40, 34, 28, 255),
    "b": (26, 22, 18, 255),
    "E": (240, 200, 40, 255),    # yellow eyes
    "W": (220, 210, 190, 255),
}


def draw_troll():
    g = blank()
    # huge head near top
    rect(g, 9, 2, 22, 11, "G")
    for y in range(2, 12):
        put(g, 9, y, "g")
        put(g, 22, y, "g")
    rect(g, 10, 2, 21, 4, "H")
    # wart / mottling
    put(g, 12, 4, "M"); put(g, 18, 5, "M"); put(g, 14, 3, "M")
    # brow
    rect(g, 10, 6, 21, 7, "g")
    # eyes
    put(g, 12, 8, "E"); put(g, 13, 8, "E")
    put(g, 18, 8, "E"); put(g, 19, 8, "E")
    # big nose / mouth
    rect(g, 14, 8, 17, 9, "g")
    put(g, 13, 10, "W"); put(g, 18, 10, "W")
    put(g, 14, 10, "g"); put(g, 15, 10, "g"); put(g, 16, 10, "g"); put(g, 17, 10, "g")
    outline_box(g, 8, 2, 23, 11)
    # hunched shoulders / massive torso fills width
    rect(g, 6, 12, 25, 20, "G")
    for y in range(12, 21):
        put(g, 6, y, "g")
        put(g, 25, y, "g")
        put(g, 7, y, "H")
    put(g, 10, 14, "M"); put(g, 16, 16, "M"); put(g, 20, 13, "M")
    put(g, 12, 18, "M"); put(g, 22, 17, "M")
    # loincloth
    rect(g, 12, 19, 19, 21, "A")
    for x in range(12, 20):
        put(g, x, 21, "a")
    outline_box(g, 6, 12, 25, 20)
    outline_box(g, 12, 19, 19, 21)
    # long arms hanging down sides
    rect(g, 3, 13, 5, 24, "G")
    rect(g, 26, 13, 28, 24, "G")
    for y in range(13, 25):
        put(g, 3, y, "g")
        put(g, 28, y, "g")
    put(g, 4, 15, "M"); put(g, 27, 16, "M")
    outline_box(g, 3, 13, 5, 24)
    outline_box(g, 26, 13, 28, 24)
    # big hands
    rect(g, 2, 25, 6, 26, "g")
    rect(g, 25, 25, 29, 26, "g")
    outline_box(g, 2, 25, 6, 26)
    outline_box(g, 25, 25, 29, 26)
    # thick stump legs
    rect(g, 10, 22, 14, 25, "g")
    rect(g, 17, 22, 21, 25, "g")
    for y in range(22, 26):
        put(g, 10, y, "O"); put(g, 14, y, "O")
        put(g, 17, y, "O"); put(g, 21, y, "O")
    # huge feet y=26-27
    rect(g, 8, 26, 15, 27, "B")
    rect(g, 16, 26, 23, 27, "B")
    for x in range(8, 16):
        put(g, x, 27, "b")
    for x in range(16, 24):
        put(g, x, 27, "b")
    outline_box(g, 8, 26, 15, 27)
    outline_box(g, 16, 26, 23, 27)
    return g


# =============================================================================
# KOBOLD — smaller than goblin, snout visible, ~delver-ish smaller, feet y=27
# Dog/lizard snout, reddish-brown, short stature.
# =============================================================================
KOBOLD_PAL = {
    "O": (28, 18, 14, 255),
    "K": (168, 100, 62, 255),    # hide mid
    "k": (120, 68, 40, 255),
    "H": (200, 140, 90, 255),
    "A": (80, 90, 70, 255),      # ragged cloth
    "a": (54, 62, 48, 255),
    "B": (48, 36, 28, 255),
    "b": (32, 24, 18, 255),
    "E": (240, 220, 60, 255),
    "S": (90, 50, 36, 255),      # snout shade
    "N": (190, 120, 80, 255),    # snout
    "W": (230, 220, 200, 255),
}


def draw_kobold():
    g = blank()
    # small head higher start ~y10
    rect(g, 12, 10, 19, 15, "K")
    for y in range(10, 16):
        put(g, 12, y, "k")
        put(g, 19, y, "k")
    rect(g, 13, 10, 18, 11, "H")
    # ears / horns stubs
    put(g, 11, 10, "k"); put(g, 11, 9, "O")
    put(g, 20, 10, "k"); put(g, 20, 9, "O")
    # eyes
    put(g, 13, 12, "E"); put(g, 14, 12, "E")
    put(g, 17, 12, "E"); put(g, 18, 12, "E")
    # visible snout protruding DOWN (facing down — snout toward bottom of face)
    rect(g, 14, 13, 17, 16, "N")
    put(g, 14, 13, "S"); put(g, 17, 13, "S")
    put(g, 15, 15, "S"); put(g, 16, 15, "S")
    put(g, 15, 16, "O"); put(g, 16, 16, "O")  # nostrils tip
    # tiny teeth
    put(g, 14, 15, "W"); put(g, 17, 15, "W")
    outline_box(g, 11, 10, 20, 15)
    outline_box(g, 13, 13, 18, 16)
    # tiny neck
    rect(g, 14, 17, 17, 17, "k")
    # small torso
    rect(g, 13, 18, 18, 22, "A")
    for y in range(18, 23):
        put(g, 13, y, "a")
        put(g, 18, y, "a")
    outline_box(g, 13, 18, 18, 22)
    # thin arms
    rect(g, 10, 18, 12, 21, "K")
    rect(g, 19, 18, 21, 21, "K")
    for y in range(18, 22):
        put(g, 10, y, "k")
        put(g, 21, y, "k")
    outline_box(g, 10, 18, 12, 21)
    outline_box(g, 19, 18, 21, 21)
    put(g, 10, 22, "k"); put(g, 21, 22, "k")
    # short legs — stretched so feet land at y=27
    rect(g, 13, 23, 15, 25, "k")
    rect(g, 16, 23, 18, 25, "k")
    for y in range(23, 26):
        put(g, 13, y, "O"); put(g, 15, y, "O")
        put(g, 16, y, "O"); put(g, 18, y, "O")
    # feet y=26-27
    rect(g, 12, 26, 15, 27, "B")
    rect(g, 16, 26, 19, 27, "B")
    for x in range(12, 16):
        put(g, x, 27, "b")
    for x in range(16, 20):
        put(g, x, 27, "b")
    outline_box(g, 12, 26, 15, 27)
    outline_box(g, 16, 26, 19, 27)
    return g


# =============================================================================
# BAT — wings visible, slightly higher than y=27 (flying)
# Body centered mid-canvas; wings spread; feet/tip around y=22-24.
# =============================================================================
BAT_PAL = {
    "O": (16, 12, 20, 255),
    "B": (70, 52, 88, 255),      # body purple-brown
    "b": (44, 32, 56, 255),
    "H": (100, 78, 120, 255),
    "W": (90, 70, 110, 255),     # wing membrane
    "w": (56, 42, 72, 255),
    "E": (240, 60, 60, 255),
    "F": (180, 140, 100, 255),   # fang/ear
    "L": (40, 30, 50, 255),      # wing bone
}


def draw_bat():
    g = blank()
    # body oval mid-upper
    rect(g, 13, 10, 18, 18, "B")
    for y in range(10, 19):
        put(g, 13, y, "b")
        put(g, 18, y, "b")
    rect(g, 14, 10, 17, 12, "H")
    # head
    rect(g, 14, 7, 17, 10, "B")
    put(g, 14, 7, "b"); put(g, 17, 7, "b")
    # ears
    put(g, 13, 6, "F"); put(g, 13, 5, "O")
    put(g, 18, 6, "F"); put(g, 18, 5, "O")
    # eyes
    put(g, 14, 8, "E"); put(g, 17, 8, "E")
    # tiny fangs
    put(g, 15, 9, "F"); put(g, 16, 9, "F")
    outline_box(g, 13, 7, 18, 10)
    outline_box(g, 13, 10, 18, 18)
    # left wing (spread)
    # membrane rows
    for dx, dy in [
        (12, 11), (11, 11), (10, 12), (9, 12), (8, 13), (7, 13),
        (6, 14), (5, 14), (4, 15), (3, 15), (2, 16),
        (12, 12), (11, 12), (10, 13), (9, 13), (8, 14), (7, 14),
        (6, 15), (5, 15), (4, 16), (3, 16),
        (12, 13), (11, 13), (10, 14), (9, 14), (8, 15), (7, 15),
        (6, 16), (5, 16),
        (11, 14), (10, 15), (9, 15), (8, 16),
    ]:
        put(g, dx, dy, "W")
    for dx, dy in [(12, 11), (10, 12), (8, 13), (6, 14), (4, 15), (2, 16)]:
        put(g, dx, dy, "L")
    # right wing mirror
    for dx, dy in [
        (19, 11), (20, 11), (21, 12), (22, 12), (23, 13), (24, 13),
        (25, 14), (26, 14), (27, 15), (28, 15), (29, 16),
        (19, 12), (20, 12), (21, 13), (22, 13), (23, 14), (24, 14),
        (25, 15), (26, 15), (27, 16), (28, 16),
        (19, 13), (20, 13), (21, 14), (22, 14), (23, 15), (24, 15),
        (25, 16), (26, 16),
        (20, 14), (21, 15), (22, 15), (23, 16),
    ]:
        put(g, dx, dy, "W")
    for dx, dy in [(19, 11), (21, 12), (23, 13), (25, 14), (27, 15), (29, 16)]:
        put(g, dx, dy, "L")
    # wing tips outline accents
    for x, y in [(2, 16), (3, 15), (29, 16), (28, 15)]:
        put(g, x, y, "O")
    # dangling feet (flying — above y=27; tip around y=22)
    put(g, 14, 19, "b"); put(g, 15, 19, "B"); put(g, 16, 19, "B"); put(g, 17, 19, "b")
    put(g, 14, 20, "O"); put(g, 15, 20, "b"); put(g, 16, 20, "b"); put(g, 17, 20, "O")
    put(g, 15, 21, "O"); put(g, 16, 21, "O")
    put(g, 15, 22, "F"); put(g, 16, 22, "F")
    return g


# =============================================================================
# RAT — all fours, occupies lower ~20 pixels of canvas
# Side-ish top-down facing down/toward viewer; body in y12-31.
# =============================================================================
RAT_PAL = {
    "O": (24, 18, 16, 255),
    "R": (140, 100, 72, 255),
    "r": (100, 68, 48, 255),
    "H": (170, 130, 96, 255),
    "E": (220, 40, 40, 255),
    "N": (60, 44, 36, 255),      # nose/ears dark
    "T": (160, 120, 100, 255),   # tail
    "t": (110, 80, 60, 255),
    "W": (230, 220, 210, 255),   # tooth
    "P": (180, 150, 130, 255),   # paw
}


def draw_rat():
    g = blank()
    # body in lower ~20 px: roughly y=12..31
    # elongated body facing down (head toward bottom)
    rect(g, 10, 12, 21, 22, "R")
    for y in range(12, 23):
        put(g, 10, y, "r")
        put(g, 21, y, "r")
    rect(g, 11, 12, 20, 14, "H")
    # spine stripe
    for y in range(13, 21):
        put(g, 15, y, "r"); put(g, 16, y, "r")
    outline_box(g, 9, 12, 22, 22)
    # head toward bottom
    rect(g, 12, 22, 19, 27, "R")
    for y in range(22, 28):
        put(g, 12, y, "r")
        put(g, 19, y, "r")
    rect(g, 13, 22, 18, 23, "H")
    # ears on sides of head
    put(g, 11, 22, "N"); put(g, 10, 21, "N"); put(g, 11, 21, "R")
    put(g, 20, 22, "N"); put(g, 21, 21, "N"); put(g, 20, 21, "R")
    # eyes
    put(g, 13, 24, "E"); put(g, 18, 24, "E")
    # snout
    rect(g, 14, 25, 17, 28, "H")
    put(g, 14, 27, "r"); put(g, 17, 27, "r")
    put(g, 15, 28, "N"); put(g, 16, 28, "N")
    put(g, 15, 26, "W")  # tooth hint
    outline_box(g, 12, 22, 19, 27)
    outline_box(g, 14, 25, 17, 28)
    # four paws (all fours) at sides of body — lower canvas
    # rear paws (higher y smaller = rear toward top of facing-down)
    rect(g, 7, 14, 9, 16, "P")
    rect(g, 22, 14, 24, 16, "P")
    outline_box(g, 7, 14, 9, 16)
    outline_box(g, 22, 14, 24, 16)
    # front paws near head
    rect(g, 8, 24, 10, 26, "P")
    rect(g, 21, 24, 23, 26, "P")
    outline_box(g, 8, 24, 10, 26)
    outline_box(g, 21, 24, 23, 26)
    # tail curling up from rear (top of body)
    for i, (x, y) in enumerate([
        (15, 11), (16, 10), (17, 9), (18, 8), (19, 7),
        (20, 6), (21, 5), (22, 5), (23, 6), (24, 7), (24, 8),
    ]):
        put(g, x, y, "T" if i % 2 == 0 else "t")
    put(g, 24, 8, "O")
    return g


# =============================================================================
# NUGGETS — 16x16 loose chunks, visually distinct, no tile bg
# =============================================================================
def draw_nugget_stone():
    """Grey irregular rock chunk."""
    pal = {
        "O": (30, 30, 32, 255),
        "S": (130, 130, 136, 255),
        "s": (90, 90, 96, 255),
        "H": (170, 170, 176, 255),
        "D": (60, 60, 64, 255),
    }
    g = blank(NUG_SIZE)
    # irregular chunk shape
    shape = [
        # y, x0..x1 fills
        (3, 5, 10),
        (4, 4, 12),
        (5, 3, 13),
        (6, 3, 13),
        (7, 2, 12),
        (8, 3, 13),
        (9, 4, 13),
        (10, 4, 12),
        (11, 5, 11),
        (12, 6, 10),
    ]
    for y, x0, x1 in shape:
        rect(g, x0, y, x1, y, "S")
    # shading / facets
    for y in range(5, 11):
        put(g, 3 if y >= 5 else 4, y, "s")
    put(g, 4, 7, "s"); put(g, 5, 8, "s"); put(g, 6, 10, "s")
    put(g, 9, 5, "H"); put(g, 10, 4, "H"); put(g, 11, 6, "H")
    put(g, 8, 9, "D"); put(g, 10, 11, "D")
    # outline key edge pixels
    for x, y in [(5, 3), (10, 3), (4, 4), (12, 4), (3, 5), (13, 5),
                 (3, 6), (13, 6), (2, 7), (12, 7), (3, 8), (13, 8),
                 (4, 9), (13, 9), (4, 10), (12, 10), (5, 11), (11, 11),
                 (6, 12), (10, 12)]:
        put(g, x, y, "O")
    return g, pal


def draw_nugget_iron():
    """Dark metallic blue-grey angular chunk with specular."""
    pal = {
        "O": (18, 20, 24, 255),
        "I": (110, 120, 140, 255),
        "i": (70, 78, 96, 255),
        "H": (190, 200, 220, 255),
        "D": (40, 46, 58, 255),
        "R": (150, 90, 60, 255),  # rust fleck
    }
    g = blank(NUG_SIZE)
    # more angular / crystalline chunk
    shape = [
        (2, 6, 9),
        (3, 5, 11),
        (4, 4, 12),
        (5, 3, 12),
        (6, 3, 13),
        (7, 4, 13),
        (8, 3, 12),
        (9, 4, 12),
        (10, 5, 11),
        (11, 6, 10),
        (12, 7, 9),
    ]
    for y, x0, x1 in shape:
        rect(g, x0, y, x1, y, "I")
    for y in range(4, 11):
        put(g, 4, y, "i")
        put(g, 5, y, "i")
    put(g, 8, 5, "H"); put(g, 9, 4, "H"); put(g, 10, 6, "H")
    put(g, 7, 3, "H")
    put(g, 9, 9, "D"); put(g, 6, 10, "D"); put(g, 11, 8, "i")
    put(g, 5, 8, "R"); put(g, 10, 11, "R")
    for x, y in [(6, 2), (9, 2), (5, 3), (11, 3), (4, 4), (12, 4),
                 (3, 5), (12, 5), (3, 6), (13, 6), (4, 7), (13, 7),
                 (3, 8), (12, 8), (4, 9), (12, 9), (5, 10), (11, 10),
                 (6, 11), (10, 11), (7, 12), (9, 12)]:
        put(g, x, y, "O")
    return g, pal


def draw_nugget_gold():
    """Warm yellow-gold lumpy nugget with bright highlights."""
    pal = {
        "O": (60, 40, 10, 255),
        "G": (220, 170, 40, 255),
        "g": (170, 120, 20, 255),
        "H": (255, 230, 120, 255),
        "D": (120, 80, 16, 255),
        "S": (240, 200, 80, 255),
    }
    g = blank(NUG_SIZE)
    # lumpy organic gold shape
    shape = [
        (3, 6, 10),
        (4, 4, 12),
        (5, 3, 13),
        (6, 3, 13),
        (7, 2, 13),
        (8, 3, 14),
        (9, 3, 13),
        (10, 4, 12),
        (11, 5, 11),
        (12, 7, 10),
    ]
    for y, x0, x1 in shape:
        rect(g, x0, y, x1, y, "G")
    for y in range(5, 11):
        put(g, 3, y, "g")
        put(g, 4, y, "g")
    put(g, 8, 4, "H"); put(g, 9, 5, "H"); put(g, 10, 4, "S")
    put(g, 7, 6, "S"); put(g, 11, 7, "H")
    put(g, 6, 9, "D"); put(g, 9, 11, "D"); put(g, 12, 8, "g")
    put(g, 5, 7, "g")
    for x, y in [(6, 3), (10, 3), (4, 4), (12, 4), (3, 5), (13, 5),
                 (3, 6), (13, 6), (2, 7), (13, 7), (3, 8), (14, 8),
                 (3, 9), (13, 9), (4, 10), (12, 10), (5, 11), (11, 11),
                 (7, 12), (10, 12)]:
        put(g, x, y, "O")
    return g, pal


def draw_nugget_gem():
    """Faceted jewel — cyan/magenta crystal distinct from ores."""
    pal = {
        "O": (20, 10, 40, 255),
        "C": (80, 200, 220, 255),   # cyan face
        "c": (40, 130, 160, 255),
        "M": (180, 70, 200, 255),   # magenta face
        "m": (120, 40, 140, 255),
        "H": (220, 240, 255, 255),  # bright facet
        "D": (30, 50, 80, 255),
    }
    g = blank(NUG_SIZE)
    # diamond-ish crystal pointing up
    # top point
    put(g, 7, 2, "H"); put(g, 8, 2, "H")
    rect(g, 6, 3, 9, 3, "C")
    rect(g, 5, 4, 10, 4, "C")
    rect(g, 4, 5, 11, 5, "C")
    # mid band — split cyan / magenta facets
    for y in range(6, 10):
        rect(g, 3, y, 7, y, "C")
        rect(g, 8, y, 12, y, "M")
    for y in range(6, 10):
        put(g, 3, y, "c")
        put(g, 7, y, "c")
        put(g, 8, y, "m")
        put(g, 12, y, "m")
    # bright center facet
    put(g, 6, 6, "H"); put(g, 5, 7, "H")
    put(g, 9, 6, "H"); put(g, 10, 7, "H")
    # lower taper
    rect(g, 4, 10, 11, 10, "c")
    for x in range(8, 12):
        put(g, x, 10, "m")
    rect(g, 5, 11, 10, 11, "D")
    rect(g, 6, 12, 9, 12, "D")
    put(g, 7, 13, "D"); put(g, 8, 13, "D")
    # outline
    for x, y in [(7, 2), (8, 2), (6, 3), (9, 3), (5, 4), (10, 4),
                 (4, 5), (11, 5), (3, 6), (12, 6), (3, 7), (12, 7),
                 (3, 8), (12, 8), (3, 9), (12, 9), (4, 10), (11, 10),
                 (5, 11), (10, 11), (6, 12), (9, 12), (7, 13), (8, 13)]:
        put(g, x, y, "O")
    return g, pal


# =============================================================================
# PREVIEWS + DOCS
# =============================================================================
def make_creature_preview(images, labels, path, scale=4, pad=4):
    n = len(images)
    cell = SIZE * scale
    cols = n
    rows = 1
    w = cols * cell + (cols + 1) * pad
    h = rows * cell + (rows + 1) * pad + 14
    sheet = Image.new("RGBA", (w, h), (36, 36, 42, 255))
    # checkerboard behind for alpha visibility
    for cy in range(0, h, 8):
        for cx in range(0, w, 8):
            if ((cx // 8) + (cy // 8)) % 2 == 0:
                for yy in range(cy, min(cy + 8, h)):
                    for xx in range(cx, min(cx + 8, w)):
                        sheet.putpixel((xx, yy), (48, 48, 56, 255))
    for i, im in enumerate(images):
        big = im.resize((cell, cell), Image.NEAREST)
        x = pad + i * (cell + pad)
        y = pad
        sheet.paste(big, (x, y), big)
    sheet.save(path)
    return sheet


def make_nugget_preview(images, path, scale=6, pad=4):
    n = len(images)
    cell = NUG_SIZE * scale
    w = n * cell + (n + 1) * pad
    h = cell + 2 * pad
    sheet = Image.new("RGBA", (w, h), (36, 36, 42, 255))
    for cy in range(0, h, 8):
        for cx in range(0, w, 8):
            if ((cx // 8) + (cy // 8)) % 2 == 0:
                for yy in range(cy, min(cy + 8, h)):
                    for xx in range(cx, min(cx + 8, w)):
                        sheet.putpixel((xx, yy), (48, 48, 56, 255))
    for i, im in enumerate(images):
        big = im.resize((cell, cell), Image.NEAREST)
        x = pad + i * (cell + pad)
        y = pad
        sheet.paste(big, (x, y), big)
    sheet.save(path)
    return sheet


def write_readme():
    text = """# HearthHold Pack 4 — Creatures & Nuggets

Original 32×32 creature sprites and 16×16 ore nuggets for **Grok Build / HearthHold**.

Hard-pixel Pillow art. Not derived from Dwarf Fortress, Kenney, or other third-party packs.

## Contents

### `creatures/` — 32×32 RGBA, hard alpha (0/255)

Facing **DOWN**. No walk cycle. No floor baked in.

| File | Notes |
|------|-------|
| `goblin.png` | Greener skin; smaller/narrower than orc; ~delver height; feet y=27 |
| `orc.png` | Larger/brutish; olive hide + tusks; ~delver height; feet y=27 |
| `troll.png` | Bulky; fills most of canvas; long arms; feet y=27 |
| `kobold.png` | Smaller than goblin; snout visible; feet y=27 |
| `bat.png` | Wings spread; flying (body/feet above y=27) |
| `rat.png` | All fours; occupies lower ~20 pixels of canvas |

### `nuggets/` — 16×16 RGBA, hard alpha

Loose chunks. No tile/floor background. Visually distinct from each other.

| File | Look |
|------|------|
| `nugget_stone.png` | Grey irregular rock |
| `nugget_iron.png` | Dark blue-grey metal + rust fleck |
| `nugget_gold.png` | Warm yellow-gold lumpy nugget |
| `nugget_gem.png` | Faceted cyan/magenta crystal |

### Previews

- `preview_creatures.png` — creatures at 4× nearest-neighbor
- `preview_nuggets.png` — nuggets at 6× nearest-neighbor

## Specs

- Creatures: 32×32 RGBA, hard alpha only (no AA fringing)
- Nuggets: 16×16 RGBA, hard alpha only
- Top-down / facing-down readable silhouettes
- Limited palettes, hard pixels
- Feet baseline y=27 for grounded humanoids (goblin, orc, troll, kobold)

## Generator

`generate_pack4.py` — reproducible Pillow generator.
"""
    (OUT / "README.md").write_text(text)


def write_credits():
    text = """Original pixel art for HearthHold
Created procedurally with Python + Pillow for HearthHold Pack 4 (Grok Build).
Creatures and ore nuggets; not derived from Dwarf Fortress, Kenney,
or other third-party sprite packs.
"""
    (OUT / "CREDITS.txt").write_text(text)


def verify(path, expect_w, expect_h, label):
    im = Image.open(path)
    assert im.size == (expect_w, expect_h), f"{label} size {im.size}"
    assert im.mode == "RGBA", f"{label} mode {im.mode}"
    px = im.load()
    soft = 0
    opaque = 0
    for y in range(expect_h):
        for x in range(expect_w):
            a = px[x, y][3]
            if a not in (0, 255):
                soft += 1
            if a == 255:
                opaque += 1
    assert soft == 0, f"{label} has {soft} soft-alpha pixels"
    assert opaque > 0, f"{label} fully transparent"
    # foot check for grounded
    return opaque


def main():
    CREATURES.mkdir(parents=True, exist_ok=True)
    NUGGETS.mkdir(parents=True, exist_ok=True)

    creature_specs = [
        ("goblin.png", draw_goblin, GOBLIN_PAL, True),
        ("orc.png", draw_orc, ORC_PAL, True),
        ("troll.png", draw_troll, TROLL_PAL, True),
        ("kobold.png", draw_kobold, KOBOLD_PAL, True),
        ("bat.png", draw_bat, BAT_PAL, False),
        ("rat.png", draw_rat, RAT_PAL, False),
    ]

    creature_ims = []
    for name, drawer, pal, grounded in creature_specs:
        g = drawer()
        path = CREATURES / name
        im = render(g, pal, path)
        harden(im)
        im.save(path)
        opaque = verify(path, 32, 32, name)
        # feet y check for grounded
        px = im.load()
        max_y = max(y for y in range(32) for x in range(32) if px[x, y][3] == 255)
        if grounded:
            assert max_y == 27, f"{name} feet y={max_y}, expected 27"
        print(f"  creatures/{name}: opaque={opaque} max_y={max_y}")
        creature_ims.append(im)

    nugget_drawers = [
        ("nugget_stone.png", draw_nugget_stone),
        ("nugget_iron.png", draw_nugget_iron),
        ("nugget_gold.png", draw_nugget_gold),
        ("nugget_gem.png", draw_nugget_gem),
    ]
    nugget_ims = []
    for name, drawer in nugget_drawers:
        g, pal = drawer()
        path = NUGGETS / name
        im = render(g, pal, path)
        harden(im)
        im.save(path)
        opaque = verify(path, 16, 16, name)
        print(f"  nuggets/{name}: opaque={opaque}")
        nugget_ims.append(im)

    make_creature_preview(creature_ims, [s[0] for s in creature_specs],
                          OUT / "preview_creatures.png")
    make_nugget_preview(nugget_ims, OUT / "preview_nuggets.png")
    write_readme()
    write_credits()
    print("Done.")


if __name__ == "__main__":
    main()
