exec(open('buildreal.py').read())
PROJ="Brand Proposal for Hibbing Dispensary | Logo Design"
P=[]
P.append(head("Logo Design & Brand, Hibbing Dispensary"))
P.append(cover_hero(PROJ,"2026 – 07 – 24","BRAND PROPOSAL FOR HIBBING DISPENSARY | LOGO DESIGN"))
P.append(cover_toc(PROJ,[("03","Introduction"),("05","Market &amp; Audience"),
   ("06","Scope"),("13","Investment"),("17","Timeline"),("20","Next Steps")]))
P.append(statement(PROJ))
P.append(getknow(PROJ,'<p>Delta9 Digital is a Minnesota-based agency built for the cannabis industry, marketing, technology, and compliance under one roof, crafting identities that are distinctive, ownable, and compliant.</p><p>A multi-state operator can copy a menu or a discount. What it can\'t copy is a mark rooted in the ground under Hibbing, the Hull–Rust pit, the strata, the iron.</p>'))
P.append(work_logo(PROJ))

# Market Snapshot (brand-framed, light)
P.append(f'''<section class="pg"><span class="eye">Market Snapshot</span><h2>Why Brand<br>Is the Moat</h2>
<p class="lead">Minnesota bans nearly every paid channel, no billboards, no paid social, two signs on your own building. When you can\'t out-spend, you out-mean-something.</p>
<div class="grid g3" style="margin:20px 0">
<div class="card"><span class="k">The field</span><h3>Bland by default</h3><p>Competitors within 40 miles run green-and-black wellness minimalism. None reads as local.</p></div>
<div class="card"><span class="k">The town</span><h3>Story-rich</h3><p>The world\'s largest open-pit mine, birthplace of Greyhound, a landmark high school.</p></div>
<div class="card"><span class="k">The opening</span><h3>Be unmistakable</h3><p>A distinctly Iron Range mark is the one asset a chain can\'t replicate from a distance.</p></div></div>
<div class="flag"><strong>Compliance frames every choice.</strong> Minnesota restricts imagery that appeals to under-21s, animals, characters, candy shapes are out. That eliminates the mascot route and points toward material, landscape, and typography.</div>
{meta("06","Market Snapshot",PROJ)}</section>''')
P.append(demographics(PROJ,"06","Median age 45.7","Local, Not Startup","An older, rooted, working population responds to an identity that feels local and earned, the mine, the strata, the iron, not a wellness-startup aesthetic aimed at a 25-year-old in a metro."))

# Personas (light) with gallery
P.append(f'''<section class="pg"><span class="eye">Audience, Personas &amp; What They Change</span><h2>Your Customers</h2>
<p class="lead">Native to a 58-year-old miner and legible to a 38-year-old weekender on a phone. That range is the brief.</p>
{pgallery()}
<p><strong>Tanner changes the logo brief.</strong> The weekend visitor finds you as a Google Maps pin and a sign glimpsed from the highway, an argument for the logo-mark direction: a bold, high-contrast mark that survives being tiny on a map and large on a building.</p>
{meta("07","Audience",PROJ)}</section>''')

# BRAND MARK & LOGO DIRECTION (dark)
ring='<svg width="140" height="110" viewBox="0 0 140 110" fill="none"><g fill="none" stroke-width="2.4"><ellipse cx="70" cy="50" rx="64" ry="43" stroke="#8C3A20"/><ellipse cx="70" cy="54" rx="50" ry="33" stroke="#B4541F"/><ellipse cx="70" cy="58" rx="36" ry="23" stroke="#4A443C"/><ellipse cx="70" cy="61" rx="22" ry="13" stroke="#e79796"/><ellipse cx="70" cy="63" rx="10" ry="6" stroke="#a8f3ef"/></g></svg>'


# SCOPE divider
P.append(divider(PROJ,"yellow","Scope","2 Weeks","10","Scope",sid="scope"))
# DELIVERABLES
P.append(f'''<section class="pg"><h2 style="color:var(--purple)">Deliverables</h2>
<div class="dlist">
<div class="r"><div class="n">01.</div><div class="t">Direction</div></div>
<div class="r"><div class="n">02.</div><div class="t">Logo Design</div></div>
<div class="r"><div class="n">03.</div><div class="t">Variants &amp; Files</div></div></div>
<p class="lead" style="margin-top:18px">A focused sprint, one direction, a single logo mark, taken to finished files that reuse the shared design system.</p>
{meta("11","Deliverables",PROJ)}</section>''')
# STAGE 1 only (single sprint)
P.append(divider(PROJ,"coral","The Sprint","Direction &amp; Logo Execution","12","Stage 1"))
P.append(stagecards("coral",[
("01","Direction","Quick discovery, compliance check, locked creative direction, the logo mark, reusing the shared system\'s color and type."),
("02","Logo Design","Terraced-pit primary mark + Big Shoulders logotype, drawn and refined against your feedback."),
("03","Variants","Icon/favicon, horizontal lockup, monochrome, taconite &amp; bone."),
("04","Files","Full package, SVG, PNG, PDF, ready for web and print.")],PROJ,"13"))

# INVESTMENT ($500)
inv=[("Discovery","Questionnaire, competitor scan, compliance review","Included"),
("Direction","Mood, positioning, voice in brief","Included"),
("Logo Design, Logo Mark","Primary mark + Big Shoulders logotype","Included"),
("Core Variants","Icon/favicon, lockup, monochrome","Included"),
("File Package","SVG, PNG, PDF","Included")]
ir=''.join(f'<div class="li c1"><div><div class="tt">{t}</div><div class="ds">{d}</div></div><div class="amt">{a}</div></div>' for t,d,a in inv)
P.append(f'''<section class="pg dark" id="investment"><div class="expertise"><h2>Our Expertise + Your Investment</h2></div>
<div class="inv"><div class="grp c1">Logo Design · Focused Scope</div>{ir}
<div class="total"><div class="tt">Total</div><div class="amt">$500</div></div></div>
<div class="flag"><strong>Add later:</strong> second finished direction (V2) $500 · usage guide $200 · exterior-sign master $200 · extended icon set $250.</div>
<p class="note" style="margin-top:14px">Price includes two rounds of revisions.</p>
{meta("16","Investment",PROJ)}</section>''')

# DELIVERY (2 weeks)
P.append(f'''<section class="pg dark" id="timeline"><h2 style="color:#fff;text-align:center">Delivery Schedule</h2>
<div class="dsched duo" style="max-width:680px;margin:20px auto 0">
<div class="dcol"><div class="wk">Week 1</div><h3>Direction &amp; Draft</h3><div class="pill w">Kick-off</div><div class="pill coral">Logo Mark Drafted</div><div class="dsc">Discovery, compliance check, first concept.</div></div>
<div class="dcol"><div class="wk">Week 2</div><h3>Refine &amp; Deliver</h3><div class="pill cyan">Revisions</div><div class="pill cyan">Files &amp; Sign-off</div><div class="dsc">Variants, final package, handoff.</div></div>
</div>{meta("17","Timeline",PROJ)}</section>''')

# PAYMENT (50/50)
P.append(f'''<section class="pg dark"><h2 style="color:#fff;text-align:center">Payment Schedule</h2>
<div class="pay duo" style="max-width:680px;margin:20px auto 0">
<div class="paycol"><div class="pn">Payment 1</div><h3>Kick-off</h3><div class="pct">50%</div><div class="dsc">$250 to begin, direction locked, logo mark drafted.</div></div>
<div class="paycol"><div class="pn">Payment 2</div><h3>Delivery</h3><div class="pct">50%</div><div class="dsc">$250 at sign-off, final files handed over.</div></div>
</div>{meta("18","Payment Schedule",PROJ)}</section>''')

# WHAT'S NEXT
P.append(f'''<section class="pg dark"><div class="split">
<div class="lft"><h2>What's<br>Next?</h2><div class="nsteps">
<div class="s"><div class="h">01 – Finalize Scope</div><p>Approve $500 single-direction, or add a V2 option.</p></div>
<div class="s"><div class="h">02 – Sign Contract</div><p>Terms to sign and return; confirm legal entity name.</p></div>
<div class="s"><div class="h">03 – Pay Deposit</div><p>50% before work begins.</p></div>
<div class="s"><div class="h">04 – Kick-off</div><p>Run the logo before the website build.</p></div></div></div>
<div class="rgt"><div class="rsg"><div class="w ready">Ready</div><div class="w set">Set</div><div class="w go">Go</div></div></div>
</div>{meta("19","Next Steps",PROJ)}</section>''')

# QUESTIONS
P.append(f'''<section class="pg dark"><h2 style="color:var(--mint)">Any Questions<br>Or Thoughts?<br>Or Just Say Hi?</h2>
<div class="contact"><div>Contact Joshua Giowaya</div><div>Email JG@delta9digital.com</div><div>Cell 612-669-9349</div></div>
{meta("20","Questions",PROJ)}</section>''')
P.append(f'''<section class="pg mint"><div class="thanks"><div class="small">Thank you for your time and consideration</div>
<h2>What To See More?<br>Follow Us:<br>@Delta9Digital</h2></div>{meta("21","Thank You",PROJ)}</section>''')

body=''.join(P[1:]); open('../output/hibbing-logo-proposal.html','w').write(P[0]+wrap_sections(body))
print("real logo:", len(''.join(P))//1024,"KB,",len(P)-1,"pages")
