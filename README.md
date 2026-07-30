# Hibbing Dispensary — Delta9 Digital proposals

Two self-contained HTML pitch decks, generated from Python. The `.html` files in
`output/` are **build artifacts** — never edit them by hand. Edit the source in
`build/` and regenerate.

## Layout

```
build/
  buildreal.py   Shared helpers: page builders (cover, statement, getknow, work,
                 divider, stagecards, demographics, personas, swatches, meta),
                 the PERSONAS list, and wrap_sections() (post-processor that wraps
                 each section's content in .wrap unless it's a full-bleed divider/split).
  realweb.py     Builds the WEBSITE proposal  -> output/hibbing-website-proposal.html
  reallogo.py    Builds the LOGO proposal     -> output/hibbing-logo-proposal.html
  d9real.css     The stylesheet (matched to Delta9's real deck).
  assets.json    All base64 assets: Safiro woff2 font, D9 logo SVG, stat photos,
                 persona portraits (p_ray … p_cole), client-site screenshots
                 (site_youbetcha, site_lake), and the four brand logos
                 (logo_sensoria, logo_uforia, logo_lomi, logo_ggt). ~1.8 MB. Don't hand-edit.
  build.py       Convenience runner (rebuilds both).
output/
  hibbing-website-proposal.html
  hibbing-logo-proposal.html
```

## Rebuild

From the `build/` directory:

```bash
python3 build.py
# or individually:
python3 realweb.py && python3 reallogo.py
```

No dependencies needed for a plain rebuild — just Python 3. Each script reads
`assets.json` + `d9real.css` and writes one HTML file to `../output/`.

## Only needed if you re-process images or fonts
The original crop/embed steps used Pillow, fontTools, and brotli. You only need
these if you're adding new photos or re-embedding the font:

```bash
pip install pillow fonttools brotli
```

## How it fits together
- `buildreal.py` defines `head()`, `meta()` (footer), and one function per section type.
  Each `realweb.py` / `reallogo.py` assembles a list `P` of `<section>` strings, then
  `wrap_sections()` wraps normal sections in `.wrap` (full-bleed dividers/splits are
  left alone), and the result is written out.
- Every slide is `min-height:100vh`, full-width, with content centered in `.wrap`
  and a flow footer (`.pgfoot`) pinned to the bottom.
- The palette, Safiro headings, and layout mirror Delta9's house template.

## Notes on assets
- Persona portraits for Ray, Nikki, Marlene, Dale, Carol, Tanner are AI-generated;
  Sadie and Cole use real/reused photos. Swap in real staff/customer photos before
  anything public-facing.
- `logo_lomi` recolored to #e68081, `logo_ggt` to #133F2D (edited in `assets.json`).
- Content is current as of this export; the demographics figures cite U.S. Census
  ACS 2024 5-yr + 2020 Decennial.

## Publish
Both HTML files are fully offline-capable (fonts/images embedded). To host: rename
either file to `index.html` in its own repo and enable GitHub Pages, or drag onto
Netlify Drop. (See PUBLISH-GUIDE.md if included.)
