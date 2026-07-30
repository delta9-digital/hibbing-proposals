exec(open('buildreal.py').read())
PROJ="Website Design &amp; Development | Hibbing Dispensary"
P=[]
P.append(head("Website Design & Development, Hibbing Dispensary"))
P.append(cover_hero(PROJ,"2026 – 07 – 24","WEBSITE DESIGN &amp; DEVELOPMENT | Hibbing Dispensary"))
P.append(cover_toc(PROJ,[("03","Introduction"),("05","Market &amp; Audience"),("06","Platform &amp; Sitemap"),
   ("06","Scope"),("13","Investment"),("17","Timeline"),("20","Next Steps")]))
P.append(statement(PROJ))
P.append(getknow(PROJ,'<p>Delta9 Digital is a Minnesota-based digital agency built for the cannabis industry, marketing, technology, and compliance under one roof.</p><p>We know this market: Metrc, OCM advertising rules, and the reality that organic search and owned content are close to the only channels a dispensary can scale. This site is engineered to win the channel your competitors have abandoned.</p>'))
P.append(work_web(PROJ))

# NEW: Market Snapshot (light)
P.append(f'''<section class="pg"><span class="eye">Market Snapshot</span><h2>The Range, Right Now</h2>
<div class="grid g3" style="margin:6px 0 24px">
<div class="card"><span class="k">Supply</span><h3>Constrained</h3><p>Retail opened Sept 2025. Flower past $4,500/lb, lab backlog slows shelves. Availability swings 12–18 months.</p></div>
<div class="card"><span class="k">Trade area</span><h3>~40,000 adults</h3><p>Hibbing (~16,400) is the hub for Chisholm, Buhl, Keewatin, Mountain Iron and beyond.</p></div>
<div class="card"><span class="k">Visitors</span><h3>$65M / year</h3><p>Iron Range tourism on trail, hunting and mine-view traffic that searches on a phone.</p></div></div>
<table><tr><th>Competitor</th><th>Location</th><th>Distance</th><th>Digital posture</th></tr>
<tr><td>RISE Hibbing</td><td>Hibbing</td><td class="mono">In town</td><td>Corporate template; menu inconsistently surfaced</td></tr>
<tr><td>Northern Frost</td><td>Hibbing</td><td class="mono">In town</td><td>Brochure site, thin content, no blog</td></tr>
<tr><td>Ishkode / ANANG</td><td>Tower / Cloquet</td><td class="mono">39–75 mi</td><td>Tribal retailers, strong regional draw</td></tr></table>
{meta("06","Market Snapshot",PROJ)}</section>''')
P.append(demographics(PROJ,"06","Median age 45.7","Built for Older Buyers","Half of Hibbing (50.6%) is 45 or older, the whole case for larger type, simpler navigation, and one-tap mobile ordering, for a long-commute working population that rewards a site they can order from before they drive in."))

# NEW: Personas (light) with gallery
P.append(f'''<section class="pg"><span class="eye">Audience, Personas</span><h2>Your Customers</h2>
<p class="lead">Real people who walk into a Hibbing dispensary, the site is built around them.</p>
{pgallery()}
{meta("07","Audience",PROJ)}</section>''')
P.append(f'''<section class="pg"><span class="eye">How We Build Around Them</span><h2>We Design Around Your Customers</h2>
<div class="moves">
<div class="move m1"><div class="top"></div><div class="bd"><div class="kick">Highest-value buyer</div><h3>Capture the Weekend Visitor</h3><p>Trailhead Tanner buys big, decides on a phone, and never returns unless it's effortless. A dedicated "Visiting the Range" page and local SEO route trail, hunting and mine-view traffic straight to your menu.</p></div></div>
<div class="move m2"><div class="top"></div><div class="bd"><div class="kick">Five of seven are 38+</div><h3>Legible by Default</h3><p>Larger type, 48px tap targets and AA contrast throughout, so Ray, Marlene and Carol never squint or mis-tap on a phone in the truck.</p></div></div>
<div class="move m3"><div class="top"></div><div class="bd"><div class="kick">New and returning</div><h3>Two Front Doors</h3><p><em>Shop the Menu</em> for buyers who know what they want; <em>New Here? Start Here</em> for first-timers. Nobody lands on the wrong page.</p></div></div>
<div class="move m4"><div class="top"></div><div class="bd"><div class="kick">Occasion, not ailment</div><h3>Compliant Navigation</h3><p>Evening · Daytime · Low-Dose · Social · First-Time Friendly, the wayfinding Marlene and Carol need, with none of the health-claim risk Minnesota prohibits.</p></div></div>
</div>
{meta("08","Audience",PROJ)}</section>''')

# NEW: Platform + Sitemap (dark)
cards=[("T1","Home","Two-CTA hero → status bar → occasion &amp; category tiles → featured → deals → posts → visit."),
("T2","Shop / Menu","Dutchie embed on /shop. Occasion row deep-links filtered states."),
("T7","Education Hub","Pillar + children: first-time, reading a label, formats, what\'s legal, dosing."),
("T8","About / Our Story","Iron Range framing, real staff, beats multi-state operators."),
("T9","Visit / Contact","Hours, map, directions from feeder towns, payment, price-context."),
("T11","Visiting the Range","Trail proximity + consumption law. Tanner\'s landing page.")]
cg=''.join(f'<div class="card"><span class="k">{k}</span><h3>{h}</h3><p>{p}</p></div>' for k,h,p in cards)
P.append(f'''<section class="pg dark"><span class="eye">Platform &amp; Sitemap</span><h2 style="color:#fff">WordPress + Dutchie</h2>
<table><tr><th>Layer</th><th>Choice</th><th>Why</th></tr>
<tr><td>CMS</td><td><strong>WordPress</strong></td><td>Portable, blog-native, locally maintainable</td></tr>
<tr><td>Menu / checkout</td><td><strong>Dutchie embed</strong> on /shop</td><td>Compliant checkout Dutchie handles; SEO toggle on. No API, dodges the 2026 Plus sunset.</td></tr>
<tr><td>Age gate + analytics</td><td>Custom overlay · GA4/GTM</td><td>Lighter; click-to-menu tracked as proxy conversion</td></tr></table>
<h3 style="color:#fff;margin-top:18px;font-size:20px">Eleven Templates</h3>
<div class="grid g3" style="margin-top:10px">{cg}</div>
{meta("08","Platform &amp; Sitemap",PROJ)}</section>''')


# SCOPE divider
P.append(divider(PROJ,"yellow","Scope","4 – 6 Weeks","10","Scope",sid="scope"))
# DELIVERABLES (light numbered)
P.append(f'''<section class="pg"><h2 style="color:var(--purple)">Deliverables</h2>
<div class="dlabel">Website Design</div>
<div class="dlist">
<div class="r"><div class="n">01.</div><div class="t">Style Guide</div></div>
<div class="r"><div class="n">02.</div><div class="t">Info Architecture</div></div>
<div class="r"><div class="n">03.</div><div class="t">Visual Design</div></div></div>
<div class="dlabel" style="margin-top:20px">Website Development</div>
<div class="dlist">
<div class="r"><div class="n">04.</div><div class="t">Foundation &amp; Structure</div></div>
<div class="r"><div class="n">05.</div><div class="t">Templates &amp; Patterns</div></div>
<div class="r"><div class="n">06.</div><div class="t">Integration</div></div>
<div class="r"><div class="n">07.</div><div class="t">Optimization &amp; SEO</div></div></div>
{meta("11","Deliverables",PROJ)}</section>''')
# STAGE 1
P.append(divider(PROJ,"coral","Stage 1","Style Guide, Patterns, Templates","12","Stage 1"))
P.append(stagecards("coral",[
("01","Style Guide","Color, typography, iconography, component specs, photography direction."),
("02","Information Architecture","Navigation, hierarchy, categories, occasion taxonomy, content plan."),
("03","Template Mock-ups","High-fidelity page designs, desktop &amp; mobile.<br><br><b>Templates:</b> Home · Shop / Menu · Product · Education Hub · About · Visit / Contact · Blog · Visiting the Range"),
("04","Visual Design","Approved system translated into polished, responsive page designs.")],PROJ,"13"))
# STAGE 2
P.append(divider(PROJ,"cyan","Stage 2","Pages, Integrations, Content","14","Stage 2"))
P.append(stagecards("cyan",[
("05","Foundation","Global styles, header/footer, nav, status bar, age gate, OCM footer."),
("06","Templates &amp; Patterns","8 page templates, reusable modules, deals &amp; occasion components."),
("07","Integration","Dutchie embed on /shop, GA4/GTM, newsletter, forms."),
("08","Optimization &amp; SEO","Core Web Vitals, schema, sitemap, Google Business Profile, seed content.")],PROJ,"15"))

# INVESTMENT
inv1=[("Style Guide","Color, type, iconography, component specs","$350",False),
("Information Architecture","Navigation, taxonomy, content plan","$250",False),
("Template Mock-ups","Home, Shop, Product, About, Education, Blog, Contact, Visiting the Range (SEO)","$400",False)]
inv2=[("Build, 8 Templates","Foundation, structure, patterns, page templates","$1,300",False),
("Dutchie + Compliance","Embed on isolated route, age gate, OCM blocks","$300",False),
("SEO &amp; Google Business Profile","GBP is the top-priority SEO asset; schema, sitemap, CWV","$200",False),
("Blog Setup + Seed Post","Template, categories, first post","$200",False),
("QA, Mobile &amp; Launch","Responsive desktop &amp; mobile, cross-browser, WCAG, training","Included",False)]
def invrows(items,cls):
    o=''
    for t,d,a,s in items:
        o+=f'<div class="li {cls}{" strike" if s else ""}"><div><div class="tt">{t}</div><div class="ds">{d}</div></div><div class="amt">{a}</div></div>'
    return o
P.append(f'''<section class="pg dark" id="investment"><div class="expertise"><h2>Our Expertise + Your Investment</h2></div>
<div class="inv"><div class="grp c1"><span>Stage 1 · Design</span><span class="sub">$1,000</span></div>{invrows(inv1,"c1")}
<div class="grp c2" style="margin-top:18px"><span>Stage 2 · Development</span><span class="sub">$2,000</span></div>{invrows(inv2,"c2")}
<div class="total"><div class="tt">Total</div><div class="amt">$3,000</div></div></div>
<p class="note" style="margin-top:16px">Price includes two rounds of revisions.</p>
{meta("16","Investment",PROJ)}</section>''')

# DELIVERY SCHEDULE (dark, pills, two rows)
P.append(f'''<section class="pg dark" id="timeline"><h2 style="color:#fff;text-align:center">Delivery Schedule</h2>
<div class="dsched">
<div class="dcol"><div class="wk">Week 1</div><h3>Set-up</h3><div class="pill w">Kick-off</div><div class="pill coral">Style Guide</div><div class="dsc">Discovery, brand assets, Dutchie provisioning begins.</div></div>
<div class="dcol"><div class="wk">Week 2</div><h3>Design</h3><div class="pill coral">Info Architecture</div><div class="pill coral">Template Mock-ups</div><div class="dsc">Mock-ups approved, remaining templates from the system.</div></div>
<div class="dcol"><div class="wk">Week 3–4</div><h3>Build</h3><div class="pill cyan">Foundation</div><div class="pill cyan">Templates &amp; Dutchie</div><div class="dsc">Structure, age gate, embed, patterns.</div></div>
</div>
<div class="dsched" style="margin-top:8px">
<div class="dcol"><div class="wk">Week 5</div><h3>Content</h3><div class="pill cyan">Seed Posts</div><div class="pill cyan">Schema · GBP</div><div class="dsc">Content load, SEO config, Google Business Profile.</div></div>
<div class="dcol"><div class="wk">Week 6</div><h3>Launch</h3><div class="pill w">QA · a11y</div><div class="pill w">Launch + Training</div><div class="dsc">Compliance review, sign-off, 2-hour handoff.</div></div>
<div class="dcol"><div class="wk"> </div><h3 style="color:var(--gray-d)"> </h3><div class="dsc" style="margin-top:0">Critical path: start Dutchie provisioning in week 1.</div></div>
</div>{meta("17","Timeline",PROJ)}</section>''')

# PAYMENT
P.append(f'''<section class="pg dark"><h2 style="color:#fff;text-align:center">Payment Schedule</h2>
<div class="pay">
<div class="paycol"><div class="pn">Payment 1</div><h3>Kick-off</h3><div class="pct">30%</div><div class="dsc">Aligns objectives and scope, secures the schedule, begins discovery and style guide.</div></div>
<div class="paycol"><div class="pn">Payment 2</div><h3>Milestone</h3><div class="pct">20%</div><div class="dsc">Due at design sign-off, comps approved, build begins.</div></div>
<div class="paycol"><div class="pn">Payment 3</div><h3>Sign-off</h3><div class="pct">50%</div><div class="dsc">Due at launch, all deliverables reviewed, handed over, training complete.</div></div>
</div>{meta("18","Payment Schedule",PROJ)}</section>''')

# WHAT'S NEXT
P.append(f'''<section class="pg dark"><div class="split">
<div class="lft"><h2>What's<br>Next?</h2><div class="nsteps">
<div class="s"><div class="h">01 – Finalize Scope</div><p>Approve the proposal and pick add-ons between $3,050 and $3,500.</p></div>
<div class="s"><div class="h">02 – Sign Contract</div><p>Terms to sign and return; confirm OCM license and legal entity.</p></div>
<div class="s"><div class="h">03 – Pay Deposit</div><p>30% before work begins. Secure the domain, open Dutchie.</p></div>
<div class="s"><div class="h">04 – Kick-off</div><p>Work begins. Weekly updates in your project board.</p></div></div></div>
<div class="rgt"><div class="rsg"><div class="w ready">Ready</div><div class="w set">Set</div><div class="w go">Go</div></div></div>
</div>{meta("19","Next Steps",PROJ)}</section>''')

# QUESTIONS
P.append(f'''<section class="pg dark"><h2 style="color:var(--mint)">Any Questions<br>Or Thoughts?<br>Or Just Say Hi?</h2>
<div class="contact"><div>Contact Joshua Giowaya</div><div>Email JG@delta9digital.com</div><div>Cell 612-669-9349</div></div>
{meta("20","Questions",PROJ)}</section>''')

# THANK YOU
P.append(f'''<section class="pg mint"><div class="thanks"><div class="small">Thank you for your time and consideration</div>
<h2>What To See More?<br>Follow Us:<br>@Delta9Digital</h2></div>{meta("21","Thank You",PROJ)}</section>''')

body=''.join(P[1:]); open('../output/hibbing-website-proposal.html','w').write(P[0]+wrap_sections(body))
print("real website:", len(''.join(P))//1024,"KB,",len(P)-1,"pages")
