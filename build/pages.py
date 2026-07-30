#!/usr/bin/env python3
"""Assemble the GitHub Pages site in ../docs from the built proposals.

Each proposal gets its own directory so it publishes at its own URL:
    docs/index.html          landing page (links to both)
    docs/website/index.html  the website proposal
    docs/logo/index.html     the logo proposal
    docs/.nojekyll           serve files verbatim (skip Jekyll)

Run realweb.py + reallogo.py first (build.py does both, then calls this).
Reuses the embedded Safiro font + D9 logo + palette from assets.json/d9real.css
so the landing page matches the decks and stays fully offline-capable.
"""
import json, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output")
DOCS = os.path.join(HERE, "..", "docs")

A = json.load(open(os.path.join(HERE, "assets.json")))
FONT = A["safiro"]
LOGO = A["d9logo"]

# One entry per output. slug -> URL directory under docs/.
OUTPUTS = [
    dict(slug="website", src="hibbing-website-proposal.html",
         eye="Website Design & Development",
         title="Website",
         blurb="A conversion-first site engineered to own organic search — "
               "the one channel Minnesota dispensaries can still scale."),
    dict(slug="logo", src="hibbing-logo-proposal.html",
         eye="Brand & Logo Design",
         title="Logo & Brand",
         blurb="An Iron Range identity a multi-state operator can't copy — "
               "rooted in the Hull-Rust pit, the strata, the iron."),
]

LANDING = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Hibbing Dispensary — Delta9 Digital Proposals</title>
<style>
@font-face{{font-family:'Safiro';src:url(data:font/woff2;base64,{font}) format('woff2');font-weight:400 800;font-display:swap}}
:root{{--ink:#2a2e2e;--paper:#eeedea;--panel:#fff;--mint:#58d2ac;--coral:#e79796;
--cyan:#a8f3ef;--purple:#561ba7;--gray:#6a6e68;
--display:"Safiro","Poppins",sans-serif;--body:"Open Sans",system-ui,sans-serif}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:var(--body);color:var(--paper);background:#1b1f1e;
min-height:100vh;display:flex;flex-direction:column;
-webkit-font-smoothing:antialiased;line-height:1.6}}
.wrap{{width:min(1040px,90vw);margin:0 auto;padding:56px 0 40px;
flex:1;display:flex;flex-direction:column}}
header{{display:flex;align-items:center;gap:16px;margin-bottom:auto}}
header .logo{{width:52px;height:auto}}
header .logo svg{{width:100%;height:auto;display:block}}
header .kicker{{font-family:var(--body);font-weight:700;font-size:11px;
letter-spacing:.16em;text-transform:uppercase;color:var(--mint)}}
h1{{font-family:var(--display);font-weight:700;text-transform:uppercase;
line-height:.94;letter-spacing:-.01em;font-size:clamp(40px,8vw,84px);
margin:40px 0 14px}}
.lead{{color:#c9cbc7;font-size:clamp(15px,2vw,19px);max-width:52ch;margin-bottom:44px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}}
a.card{{display:flex;flex-direction:column;text-decoration:none;color:inherit;
background:var(--panel);color:var(--ink);border-radius:18px;padding:30px 30px 26px;
position:relative;overflow:hidden;transition:transform .18s ease,box-shadow .18s ease;
box-shadow:0 1px 0 rgba(255,255,255,.04)}}
a.card:hover{{transform:translateY(-4px);box-shadow:0 18px 40px rgba(0,0,0,.35)}}
a.card::before{{content:"";position:absolute;inset:0 0 auto 0;height:6px}}
a.card.website::before{{background:var(--mint)}}
a.card.logo::before{{background:var(--coral)}}
a.card .eye{{font-weight:700;font-size:11px;letter-spacing:.14em;text-transform:uppercase;
color:var(--gray);margin:6px 0 12px;display:block}}
a.card h2{{font-family:var(--display);font-weight:700;text-transform:uppercase;
line-height:.96;letter-spacing:-.01em;font-size:clamp(26px,4vw,38px);margin-bottom:12px}}
a.card p{{color:#4a4e4c;font-size:15px;flex:1}}
a.card .go{{margin-top:20px;font-weight:700;font-size:13px;letter-spacing:.08em;
text-transform:uppercase;display:inline-flex;align-items:center;gap:8px}}
a.card.website .go{{color:#2b8f72}}
a.card.logo .go{{color:#c26b6a}}
a.card .go svg{{width:18px;height:18px}}
footer{{margin-top:44px;padding-top:22px;border-top:1px solid rgba(255,255,255,.1);
display:flex;flex-wrap:wrap;gap:6px 22px;color:#8f938f;font-size:12.5px}}
footer a{{color:var(--mint);text-decoration:none}}
</style>
</head><body>
<div class="wrap">
<header>
<span class="logo">{logo}</span>
<span class="kicker">Delta9 Digital &nbsp;·&nbsp; Client Proposals</span>
</header>
<h1>Hibbing<br>Dispensary</h1>
<p class="lead">Two proposals for launching the Iron Range's most recognizable
cannabis brand. Choose a deck below — each opens as a full-screen pitch.</p>
<div class="cards">
{cards}
</div>
<footer>
<span>Prepared by Delta9 Digital</span>
<span>Contact Joshua Giowaya · <a href="mailto:JG@delta9digital.com">JG@delta9digital.com</a></span>
<span>612-669-9349</span>
</footer>
</div>
</body></html>
"""

CARD = """<a class="card {slug}" href="{slug}/">
<span class="eye">{eye}</span>
<h2>{title}</h2>
<p>{blurb}</p>
<span class="go">Open proposal
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"
stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
</a>"""


def build():
    if os.path.isdir(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)

    # .nojekyll: large embedded assets + no need for Jekyll processing
    open(os.path.join(DOCS, ".nojekyll"), "w").close()

    cards = []
    for o in OUTPUTS:
        src = os.path.join(OUT, o["src"])
        if not os.path.exists(src):
            raise SystemExit(f"Missing build artifact: {src}\nRun build.py first.")
        d = os.path.join(DOCS, o["slug"])
        os.makedirs(d)
        shutil.copyfile(src, os.path.join(d, "index.html"))
        cards.append(CARD.format(**o))
        print(f"  docs/{o['slug']}/index.html")

    open(os.path.join(DOCS, "index.html"), "w").write(
        LANDING.format(font=FONT, logo=LOGO, cards="\n".join(cards)))
    print("  docs/index.html (landing)")
    print("Done. Pages site in ../docs/")


if __name__ == "__main__":
    build()
