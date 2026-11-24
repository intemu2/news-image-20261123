# news-image-20261123 — "Pin Drop: 23 Nov 2026" (putaran 2)

One image summing up Monday 23 November 2026 world news: a schematic world
map with 15 numbered pins, 3 illustrated leads (Nvidia's Huang returns,
153 drones over Ukraine, Java factory toll put at 24), a number strip, 12
small cards and a two-column "Also on Monday" list of 15 — 30 stories,
6 continents.

Putaran 2 (revisi Warden R1): cerita 15 → 31; offset chip pin diperkecil dan
diaudit (pin 9 Zurich tidak lagi melayang ke Timur Tengah); lead Nvidia
diperkuat atribusinya (tag "MARKETS · REUTERS" + S&P +5%, Nasdaq +6% di sub).

Micro-fix supervisor (24 Nov, atas verdict Warden R2): A13 Medicare dihapus
(artikel AP yang sama sudah terbit 20 Nov) dan A2 diperbaiki ("Taipei fall"
salah — Taiex naik +2,23%) → 30 cerita.

The image was drawn from scratch with PIL (see `../work/render.py`); every
story was verified against a primary source for 23 Nov 2026 UTC
(see `../DATE-LOG.md`: 30/30 verified, 0 wrong-date, 0 unverified).

`main.py` (stdlib only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
