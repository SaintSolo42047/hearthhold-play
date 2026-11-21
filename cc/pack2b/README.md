# HearthHold Pack 2b — Edge-Match Revision

Original 32×32 hard-pixel art generated with Python and Pillow. Terrain is opaque RGB; furniture uses RGBA with transparent backgrounds. No external game-art copies are used.

## Revision fixes
- `terrain/floor_stone_a..e.png`: five varied stone floors with shared normalized grey perimeter pixels (around RGB 118), no repeated T-notch motif, and subtle interior texture variation.
- `terrain/rock_face_a..d.png`: dark irregular mountain rock with distributed speckle/noise and a shared noisy seam so the set continues across tile edges without masonry frames.
- `furniture/table_wood.png`: clearly a rectangular wooden table with four visible corner legs; it has no mattress or pillow silhouette.
- `preview_sheet.png`: the stone set is shown in a mixed 3×3 grid, plus rock and table samples.

## Validation
`edge_match_report.txt` records the machine check. Every stone left edge matches every stone right edge exactly (maximum channel delta 0), and every stone top edge matches every stone bottom edge exactly (maximum channel delta 0). The same exact edge check passes for the rock set. All terrain/furniture files are validated as 32×32; terrain is opaque RGB and furniture is RGBA. Table alpha is transparent outside its object silhouette.

## Contents
- `terrain/`: 20 opaque 32×32 terrain tiles.
- `furniture/`: 7 transparent-background 32×32 objects.
- `preview_sheet.png`: nearest-neighbor revision preview with the requested 3×3 stone proof grid.
- `edge_match_report.txt`: generated validation results.
