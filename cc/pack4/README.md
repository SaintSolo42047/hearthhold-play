# HearthHold Pack 4 — Creatures & Nuggets

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
