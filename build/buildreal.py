import json
A=json.load(open('assets.json'))
A['p_cole']=A.get('p_wade')  # Cole reuses Wade's portrait
css=open('d9real.css').read()
fontface="@font-face{font-family:'Safiro';src:url(%s) format('woff2');font-weight:400 800;font-display:swap}\n" % A['safiro']
LOGO=A['d9logo']

def head(t):
    return f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><style>\n{fontface}{css}\n</style>\n'
def meta(pn,sec,proj):
    return (f'<div class="pgfoot"><div class="meta"><div class="pn">Page {pn}</div><div>{sec}</div>'
            f'<div class="proj">{proj}</div><div>Delta9 Digital</div></div>'
            f'<div class="mark">{LOGO}</div></div>')

PERSONAS=[
('tanner','Trailhead Tanner','38','Visitor','highest','One big buy on a trail or hunting weekend. Finds you via a map pin.'),
('ray','Iron Range Ray','58','Daily user','high','Familiar formats and a fair price. Buys the same thing every week.'),
('nikki','Night-Shift Nikki','34','Occasional','med','Low-friction ordering at odd hours, one-handed after a shift.'),
('marlene','Managing-Pain Marlene','62','Wellness','high','Consistency and predictable dosing for chronic pain, in large type.'),
('dale','Veteran Dale','49','Wellness','med','Discretion and respect, sleep and stress. Browses without an account.'),
('carol','Curious Carol','67','New buyer','grow','A first purchase without embarrassment, sleep and arthritis.'),
('sadie','Sober-Curious Sadie','43','Lifestyle','high','Swapping the nightly glass of wine for a 5mg drink, low-dose, no hangover.'),
('cole','Connoisseur Cole','34','Enthusiast','high','Knows his terpenes, wants premium flower, potency, and a rotating menu.'),
]
POT={'highest':('Highest','p-high'),'high':('High','p-high'),'med':('Medium','p-med'),'grow':('Growing','p-grow')}
PH_ASSETS={'ray','nikki','marlene','dale','carol','tanner','cole','sadie'}
PH_GRAD={}
def _initials(n):
    parts=[p for p in n.replace('-',' ').split() if p]
    return (parts[0][0]+parts[-1][0]).upper()

def pgallery():
    c=''
    for k,n,a,seg,pot,need in PERSONAS:
        star = k=='tanner'
        badge = '<span class="tp">Highest-Value Buyer</span>' if star else ''
        if k in PH_ASSETS:
            ph=f'<div class="ph"><img src="{A["p_"+k]}" alt="{n}"></div>'
        else:
            ph=f'<div class="ph ph-ph" style="background:{PH_GRAD[k]}"><span>{_initials(n)}</span></div>'
        plabel,pcls=POT[pot]
        c+=(f'<div class="pc{" newp" if star else ""}">{badge}{ph}'
            f'<div class="pb"><div class="phd"><div class="nm">{n}</div><div class="ag">Age {a}</div></div>'
            f'<div class="ppts">'
            f'<div class="ppt"><b>Buying potential</b><span class="pot {pcls}">{plabel}</span></div>'
            f'<div class="ppt"><b>Segment</b>{seg}</div>'
            f'<div class="ppt"><b>Wants</b>{need}</div>'
            f'</div></div></div>')
    return f'<div class="pgrid">{c}</div>'


SW=[("Taconite Black","#16130F"),("Ore Red","#8C3A20"),("Mesabi Rust","#B4541F"),
("Mesabi Navy","#1E3A5F"),("Boreal Green","#25382C"),("Signal Amber","#E0A32E"),
("Bone White","#F2EDE4"),("Birch Tan","#DCD3C4"),("Pit Gray","#4A443C")]
def swatches():
    o=''
    for n,h in SW:
        b=';border:1px solid #ccc' if h.upper()=='#F2EDE4' else ''
        o+=f'<div class="sw"><div class="chip" style="background:{h}{b}"></div><div class="lbl"><b>{n}</b><span>{h}</span></div></div>'
    return o

def cover_hero(proj,date,title_line):
    return (f'<section class="pg cover">'
      f'<div class="hero tall" style="background-image:url({A["hero"]})">'
      f'<div class="propo">PROPOSAL</div>'
      f'<div class="info"><div class="dt">{date}</div><div class="tl">{("<span class=\"tla\">"+title_line.split(" | ")[0]+"</span><span class=\"tlsep\"> | </span><span class=\"tlb\">"+title_line.split(" | ")[1]+"</span>") if " | " in title_line else title_line}</div>'
      f'<div class="nav"><a href="#scope">Scope</a><a href="#investment">Investment</a><a href="#timeline">Timeline</a></div></div>'
      f'<div class="hlogo">{LOGO}</div></div></section>')

def cover_toc(proj,toc):
    tr=''.join(f'<div class="r"><div class="n">{n}</div><div class="t">{t}</div></div>' for n,t in toc)
    return (f'<section class="pg"><span class="eye">Table Of Contents</span>'
      f'<div class="toc">{tr}</div>{meta("02","Table Of Contents",proj)}</section>')

def statement(proj):
    return ('<section class="pg dark statement">'
            '<h1>Let\'s Grow<br>Something<br>Special<br>Together</h1>'
            f'{meta("02","Introduction",proj)}</section>')

def getknow(proj,body):
    return (f'<section class="pg dark" id="intro"><div class="split">'
      f'<div class="lft"><h2>Get to<br>Know Us</h2>{body}</div>'
      f'<div class="rgt">'
      f'<div class="statrow"><img src="{A["hello"]}"><div><div class="lbl">Worked For</div><div class="big">15<sub> Years</sub></div><div class="cap">In Digital Marketing</div></div></div>'
      f'<div class="statrow"><img src="{A["work1"]}"><div><div class="lbl">Worked With</div><div class="big">20<sub>+</sub></div><div class="cap">Local Minnesota Companies</div></div></div>'
      f'<div class="statrow"><img src="{A["work2"]}"><div><div class="lbl">Worked On</div><div class="big">50<sub>+</sub></div><div class="cap">Branding &amp; Website Launches</div></div></div>'
      f'</div></div>{meta("03","Introduction",proj)}</section>')

def work_web(proj):
    def cell(k,n,s):
        return (f'<div class="cell site"><div class="shot"><img src="{A[k]}" alt="{n}"></div>'
                f'<div class="cap">{n}<span>{s}</span></div></div>')
    tiles=(cell("site_youbetcha","You Betcha! Cannabis Co.","E-commerce Design &amp; Development")
           +cell("site_lake","Lake Group Insurance","Website Design &amp; Development"))
    return (f'<section class="pg dark"><div class="workhd">'
            f'<div class="workttl">We Put In That Work</div></div>'
            f'<div class="work sites pair">{tiles}</div>{meta("05","Work",proj)}</section>')

def work_logo(proj):
    logos=[("logo_sensoria","Sensoria","Wordmark for an infused sparkling beverage line."),
           ("logo_uforia","UFOria","Character logo and packaging for a THC gummy brand."),
           ("logo_lomi","Lomi","Clean horizontal wordmark and brand identity."),
           ("logo_ggt","GGT","Heritage emblem built from fine, detailed linework.")]
    cells=''.join(
      f'<div class="cell"><div class="lg"><img src="{A[k]}" alt="{n}"></div>'
      f'<div class="lb"><div class="nm">{n}</div><div class="ds">{d}</div></div></div>'
      for k,n,d in logos)
    return (f'<section class="pg dark"><div class="workhd"><div class="workttl">We Put In That Work</div></div>'
            f'<div class="work logos">{cells}</div>{meta("05","Work",proj)}</section>')

def demographics(proj, pn, kicker, heading, body):
    return (f'''<section class="pg"><span class="eye">Hibbing Demographics</span><h2>Who Lives in Hibbing</h2>
<div class="dstats">
<div class="dstat"><div class="v">16,057</div><div class="k">Population</div><div class="s">City proper (16,214 at the 2020 census); roughly 40,000 across the trade area with feeder towns.</div></div>
<div class="dstat"><div class="v">45.7</div><div class="k">Median Age</div><div class="s">About 20% older than the U.S. (38.9) and Minnesota (38.8). Your buyer skews older.</div></div>
<div class="dstat"><div class="v">$55,789</div><div class="k">Median HH Income</div><div class="s">Working-class; below the MN median. Price and value messaging matter.</div></div>
<div class="dstat"><div class="v">~12,500</div><div class="k">Adults 21+</div><div class="s">The legal-age market inside city limits, before visitors and feeder towns.</div></div>
</div>
<div class="grid g2" style="align-items:stretch;gap:26px;margin-top:8px">
<div style="display:flex;flex-direction:column"><h3 style="font-size:clamp(18px,2.4vw,22px);margin-bottom:14px">Age Distribution</h3>
<div class="bars" style="max-width:none;margin:auto 0">
<div class="bar"><div class="bl">Under 25</div><div class="bt"><i style="width:26.6%"></i></div><div class="bv">26.6%</div></div>
<div class="bar"><div class="bl">25–44</div><div class="bt"><i style="width:22.8%"></i></div><div class="bv">22.8%</div></div>
<div class="bar hot"><div class="bl">45–64</div><div class="bt"><i style="width:27.3%"></i></div><div class="bv">27.3%</div></div>
<div class="bar hot"><div class="bl">65+</div><div class="bt"><i style="width:23.3%"></i></div><div class="bv">23.3%</div></div>
</div></div>
<div class="move m2" style="height:100%"><div class="top"></div><div class="bd"><div class="kick">{kicker}</div><h3>{heading}</h3><p>{body}</p></div></div>
</div>
<p class="note" style="text-align:right">Source: U.S. Census Bureau, ACS 2024 5-year &amp; 2020 Decennial. Top sectors: health care, retail, and mining (median mining earnings top $105k).</p>
{meta(pn,"Demographics",proj)}</section>''')

def divider(proj,color,word,sub,pn,sec,sid=''):
    _id=f' id="{sid}"' if sid else ''
    return (f'<section class="pg"{_id}><div class="divider {color}">'
            f'<div class="w">{word}</div><div class="s">{sub}</div></div>'
            f'{meta(pn,sec,proj)}</section>')

def stagecards(color,cards,proj,pn):
    c=''.join(f'<div class="scard {color}"><div class="n">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n,t,d in cards)
    return f'<section class="pg dark"><div class="scards">{c}</div>{meta(pn,"Deliverables",proj)}</section>'

import re
def wrap_sections(body):
    def repl(m):
        full=m.group(0)
        ot=re.match(r'<section[^>]*>',full).group(0)
        inner=full[len(ot):-len('</section>')]
        i=inner.find('<div class="pgfoot">')
        content=inner if i<0 else inner[:i]
        tail='' if i<0 else inner[i:]
        cs=content.strip()
        if cs.startswith('<div class="divider') or cs.startswith('<div class="split'):
            b=content
        else:
            b=f'<div class="wrap">{content}</div>'
        return f'{ot}{b}{tail}</section>'
    return re.sub(r'<section\b.*?</section>', repl, body, flags=re.S)
