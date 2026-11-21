# HearthHold Pack 3b — Delver Walk Cycle (fix)

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
