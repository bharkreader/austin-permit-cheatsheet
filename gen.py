import html,json
D="Oct 15, 2026"
S={
"atx_types":"https://www.austintexas.gov/development-services/types-permits",
"atx_exempt":"https://www.austintexas.gov/development-services/work-exempt-building-permits",
"atx_fees":"https://www.austintexas.gov/development-services/fees",
"atx_res_pdf":"https://austin.widen.net/s/fz9rhwg8qq/fees_residential",
"atx_wui":"https://www.austintexas.gov/fire/wildland-urban-interface-code",
"atx_express":"https://www.austintexas.gov/development-services/express-permits",
"rr_div":"https://www.roundrocktexas.gov/city-departments/planning-and-development-services/building-inspection/",
"rr_home":"https://www.roundrocktexas.gov/city-departments/planning-and-development-services/building-inspection/homeowner-projects/",
"rr_std":"https://www.roundrocktexas.gov/city-departments/planning-and-development-services/building-inspection/standalone-building-permits/",
"rr_misc":"https://www.roundrocktexas.gov/city-departments/planning-and-development-services/building-inspection/miscellaneous-building-permits/",
"pf_fees":"https://www.pflugervilletx.gov/asset/25ed7379-981a-41fc-8950-14df8f9d01dd",
"cp_need":"https://www.cedarparktexas.gov/DocumentCenter/View/1787/Do-I-Need-a-Permit-PDF",
"cp_fees":"https://ecode360.com/38630398",
}
# Answers from city permit offices by email (no link given): shown as text instead of a link
EMAIL={"pf_email":"City permit office email, Oct 16, 2026","cp_email":"City permit office email, Oct 16, 2026","atx_chat":"City of Austin permit live chat, Oct 19, 2026"}
def src(s): return html.escape(EMAIL[s]) if s in EMAIL else f'<a href="{S[s]}" target="_blank" rel="noopener">city source</a><br><small>checked {D}</small>'
C=None # check with city
P=["Water heater","HVAC replacement","Roof replacement","Fence","Deck / patio cover","Shed / accessory building","Solar PV","In-ground pool","Electrical panel upgrade","Irrigation system"]
# (permit, fee, note, source)  fee "n/a" when no permit
data={
"Austin":[
 ("Yes","About $74","Done under a stand-alone Plumbing Change Out permit; city permit staff said stand-alone water heater change-out permits are about $74. Contractor must be registered with the city.","atx_chat"),
 ("Yes","$74.05","Mechanical Change Out stand-alone permit: $74.05 first system, $20.69 each additional (FY26-27).","atx_res_pdf"),
 ("Depends","$112.76 + $72.96","Permit if replacing >128 sq ft of decking, or >50% of roof in Wildland-Urban Interface area; some shingle replacements are exempt. Express review $112.76 + inspection $72.96.","atx_express"),
 ("Depends","$146.15","City Residential Plan Review staff said no permit is needed for a fence 8 ft or less that isn't in a floodplain, and code doesn't allow fences over 8 ft. (The Work Exempt page still says 7 ft.) Small-project review $146.15 if a permit is needed.","atx_chat"),
 ("Yes",C,"Uncovered deck listed under Residential Building Permit.","atx_types"),
 ("Depends",C,"Exempt if one story, ≤200 sq ft, ≤15 ft tall, no plumbing, not a dwelling, not in flood hazard area.","atx_exempt"),
 ("Yes","$53.56 + $169.83 + $84.92","Electrical Auxiliary Power/Solar permit. Intake $53.56, Austin Energy electrical base $169.83, inspection $84.92 (1–50 kW).","atx_res_pdf"),
 ("Yes","$146.15+","Residential building permit; small-project plan review $146.15 plus trade/inspection fees.","atx_res_pdf"),
 ("Yes","$73.81 + about $220","Permit required: a Repair permit for a like-for-like breaker panel swap, or an Upgrade permit if upgrading. Permit fee $73.81. Upgrades on Austin Energy service also need an ESPA, with Austin Energy fees of about $220.","atx_chat"),
 ("Yes","About $74","Stand-alone Plumbing Irrigation permit (registered contractor); city permit staff said it's about $74.","atx_chat")],
"Round Rock":[
 ("Yes","$50","Permits required when replacing plumbing/gas/mechanical systems; standalone permit $50. Tank-to-tankless needs a gas piping chart.","rr_std"),
 ("Yes","$50","Standalone HVAC (mechanical) permit.","rr_std"),
 ("No","n/a","No permit for a residential re-roof; modifying the roof structure requires a residential permit.","rr_home"),
 ("No","n/a","No building permit, but must meet code; check height/material with Code Enforcement, 512-341-3329.","rr_home"),
 ("Yes","$125 / $200","Wood deck/uncovered patio $125; covered patio $200 (without electrical/plumbing).","rr_home"),
 ("Yes","$50","Required even under 200 sq ft. $300 with electrical/plumbing.","rr_misc"),
 ("Yes","$150","Needs one-line drawings stamped by an electrical engineer; torque letter at final.","rr_home"),
 ("Yes","$350","In-ground pool $350 (spa/above-ground $125). Must meet 2024 pool code; review about 30 business days.","rr_home"),
 ("Yes","$50","Standalone electrical; upgrades need a torque letter with master electrician license #.","rr_std"),
 ("Yes","$50","Required for new systems on city water; repairs exempt unless the backflow device is replaced.","rr_home")],
"Pflugerville":[
 ("Yes","$90","Total $90: $60 plumbing permit + $30 tech fee.","pf_email"),
 ("Yes","$130","Total $130: $60 mechanical permit + $30 tech fee + $40 plan review.","pf_email"),
 ("Yes","$80","Residential re-roof listed in fee schedule.","pf_fees"),
 ("No","n/a","No permit required; follow the city fence ordinance.","pf_email"),
 ("Yes","$60","Residential deck & patio covers.","pf_fees"),
 ("Depends","$50–$65","Listed for accessory buildings over 200 sq ft ($50 portable, $65 permanent); detached garage $65. Smaller: check with city.","pf_fees"),
 ("Yes","$130","Total $130: $60 electrical permit + $30 tech fee + $40 plan review.","pf_email"),
 ("Yes","$158 / $204","$158 without heater, $204 with heater. Above-ground/hot tub $60.","pf_fees"),
 ("Yes","$90","Total $90: $60 electrical permit + $30 tech fee.","pf_email"),
 ("Yes","$70","Irrigation permit.","pf_fees")],
"Cedar Park":[
 ("Yes","$50","Installing or replacing a water heater requires a permit; Water Heater Install/Changeout fee $50.","cp_fees"),
 ("Yes","$50","Installing or replacing heating/AC requires a permit; HVAC Changeout fee $50.","cp_fees"),
 ("Depends","n/a","Non-structural roof covering: no permit. Structural work: check with city.","cp_need"),
 ("No","n/a","No permit, but must follow fencing ordinance Sec. 14.07.007.","cp_need"),
 ("Yes","$25 + $0.10/sq ft","Deck and patio permit required: $25 plan review + $0.10 per sq ft permit fee.","cp_email"),
 ("Yes","$0.10/sq ft (min $35) + $25","Storage sheds need a permit; accessory structure fee $0.10/sq ft (min $35) + $25 plan review.","cp_fees"),
 ("Yes","$25","Solar panel installation requires a permit; solar permit fee $25.","cp_email"),
 ("Yes","$250+","In-ground: building $100 + electrical $100 + plan review $50 (+$100 plumbing if gas heated).","cp_fees"),
 ("Yes","$25 / $40","Residential electrical service upgrade fee: $25 up to 100 A, $40 over 100 A.","cp_fees"),
 ("Yes","$25","Irrigation systems require a permit; residential fee $25.","cp_fees")],
}
WUI={
"Austin":["Vent/flue openings: 1/8-in ember mesh or WUI-approved vents (dryer vents metal).","Intake/exhaust vents: 1/8-in ember mesh.","Class A roof assembly; metal valley flashing; noncombustible gutters with leaf guards. Replacing 50%+ of roof requires full replacement to WUI code.","Within 10 ft of a building: ignition-resistant/noncombustible (metal, masonry); fire-retardant coatings not allowed.","Ignition-resistant materials (Zone A: all; B: within 30 ft of building; C: within 10 ft). Deck board gaps ≤1/8 in. Over slopes >10%, enclose underside.","Exempt from WUI Ch. 5 only if ≤100 sq ft AND >50 ft from nearest structure; otherwise ignition-resistant materials.","Check with city","Check with city","n/a","Keep 5-ft noncombustible Ember Ignition Zone around structures."],
}
WUI_NOTE={"Round Rock":"No city WUI code found (city adopted 2024 IFC).","Cedar Park":"No WUI code found; city recommends 30 ft defensible space.","Pflugerville":"No city WUI code found.",}
ps=fs=pu=fu=0
for c,rows in data.items():
  for p,f,n,s in rows:
    if p: ps+=1
    else: pu+=1
    if f: fs+=1
    else: fu+=1
print(json.dumps({"permit_sourced":ps,"permit_unknown":pu,"fee_sourced_or_na":fs,"fee_unknown":fu}))
def cell(v,cls=True):
  if v is None: return '<span class="tag check">Check with city</span>'
  k={"Yes":"yes","No":"no","Depends":"dep"}.get(v,"")
  return f'<span class="tag {k}">{html.escape(v)}</span>' if cls and k else html.escape(v)
import os,re
BASE="https://txpermitguide.com"
BUILD="2026-10-17"  # lastmod date for sitemap
CHECKER="https://check.txpermitguide.com"
BEACON="<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{\"token\": \"6d4910da73b54ea4af900760f5b52dc4\"}'></script>"
CSLUG={c:c.lower().replace(" ","-") for c in data}
PSLUG=["water-heater","hvac-replacement","roof-replacement","fence","deck-patio-cover","shed","solar-panels","in-ground-pool","electrical-panel-upgrade","irrigation-system"]
PFOR=["a water heater replacement","an HVAC replacement","a roof replacement","a fence","a deck or patio cover","a shed or accessory building","solar panels","an in-ground pool","an electrical panel upgrade","an irrigation system"]
CSS='''
:root{--ink:#1f2a44;--muted:#5d6b85;--bg:#f4f6fb;--brand:#3b5bdb}*{box-sizing:border-box}
body{margin:0;font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
header{background:linear-gradient(135deg,#1f3a8a,#3b5bdb);color:#fff;padding:1.6rem 1rem 3.4rem}header div,main,footer{max-width:1040px;margin:0 auto}
header h1{margin:0;font-size:1.6rem}header p{margin:.4rem 0 0;opacity:.9}header a{color:#fff}main{padding:0 1rem 1rem;margin-top:-2.4rem}footer{padding:0 1rem 2rem;color:var(--muted)}
section,.card{background:#fff;border-radius:16px;box-shadow:0 6px 24px rgba(31,42,68,.09);padding:1.1rem 1.3rem 1.3rem;margin-bottom:1rem}
.cta{display:flex;gap:1rem;align-items:center;flex-wrap:wrap;justify-content:space-between;background:#fff3dc}.cta p{margin:0;color:#7a4a00}
.btn{display:inline-block;font-weight:700;color:#fff;background:#c2410c;border-radius:12px;padding:.8rem 1.3rem;text-decoration:none}.btn:hover{background:#9a3412}
.btn2{display:inline-block;font-weight:700;color:var(--brand);background:#fff;border:1.5px solid var(--brand);border-radius:12px;padding:.7rem 1.2rem;text-decoration:none;margin:.25rem .5rem .25rem 0}.btn2:hover{background:#eef1fd}
.tests{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center}.tests p{margin:0 1rem 0 0;font-weight:600}
.disc{font-size:.9rem;color:var(--muted);background:#fff8ea;border-left:4px solid #f0a020;padding:.75rem 1rem;border-radius:8px}
h2{margin:.2rem 0 .6rem}table{width:100%;border-collapse:collapse;font-size:.92rem}th,td{text-align:left;padding:.55rem;border-bottom:1px solid #e8ebf2;vertical-align:top}
th{background:#eef1f8;color:#33415c}th:first-child{border-radius:10px 0 0 10px}th:last-child{border-radius:0 10px 10px 0}
.tag{display:inline-block;padding:.12rem .55rem;border-radius:99px;font-size:.8rem;font-weight:700;white-space:nowrap}
.yes{background:#e6f6ec;color:#185c36}.no{background:#eceffd;color:#2b3a8f}.dep{background:#fff3dc;color:#7a4a00}.check{background:#eef0f4;color:#5d6b85}
a{color:var(--brand)}small{color:var(--muted)}nav a{margin-right:1rem;font-weight:600}
dl.facts{display:grid;grid-template-columns:max-content 1fr;gap:.4rem 1rem;margin:0}dl.facts dt{font-weight:700;color:var(--muted)}dl.facts dd{margin:0}
ul.links{columns:2;padding-left:1.1rem}.crumbs{font-size:.9rem;opacity:.9;margin:0 0 .4rem}
@media(max-width:720px){thead{display:none}tr{display:block;border-bottom:2px solid #e8ebf2;padding:.5rem 0}td{display:block;border:0;padding:.2rem 0}td::before{content:attr(data-l)": ";font-weight:700;color:var(--muted)}ul.links{columns:1}dl.facts{grid-template-columns:1fr}}
'''
DISC='<p class="disc"><b>Disclaimer:</b> This is a free informational summary, not legal or professional advice. Rules and fees change (most cities update fees each October) and depend on your exact address, scope, HOA, historic district or floodplain status. Fees are base permit fees unless the notes list extra charges (like tech or plan-review fees). Always confirm with your city\'s building department before starting work. Areas outside city limits (ETJ / unincorporated Travis or Williamson County) follow different rules.</p>'
AUSTIN_WUI='<p><b>Wildfire zone:</b> Over half of Austin is in a WUI zone (A, B or C). Check your address on the <a href="'+S['atx_wui']+'" target="_blank" rel="noopener">2024 WUI Code map</a>. WUI projects need residential plan review, exact product specs on plans, and two WUI inspections. Applies to permit applications on/after July 10, 2025; existing homes are not required to retrofit.</p>'
TESTS='<div class="card tests"><p>Planning this project?</p><a class="btn2" href="/quotes/">Get quotes from local pros</a><a class="btn2" href="/hoa/">Need HOA approval too?</a></div>'
WUICTA=f'<div class="card cta"><p><b>🔥 Is your address in Austin\'s wildfire zone?</b><br>Check your address and see the WUI rules and fees for your project.</p><a class="btn" href="{CHECKER}">Is your address in Austin\'s wildfire zone?</a></div>'
FOOT=f'<footer><small>Sources last checked {D}. Found an error? <a href="https://github.com/bharkreader/austin-permit-cheatsheet/issues">Open an issue</a>. Not affiliated with any city.</small></footer>'
e=html.escape
def page(title,desc,path,body,head_extra="",robots=None):
  canon=BASE+path
  r=f'<meta name="robots" content="{robots}">' if robots else ''
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">{r}
<link rel="canonical" href="{canon}">
<style>{CSS}</style>{head_extra}</head><body>
{body}
{FOOT}{BEACON}</body></html>'''
def write(path,s):
  fn=path.strip("/")+"/index.html" if path!="/" else "index.html"
  d=os.path.dirname(fn)
  if d: os.makedirs(d,exist_ok=True)
  open(fn,"w").write(s)
def fee_txt(f): return "Check with city" if f is None else f
def short(p):
  return {"Yes":"Yes, a permit is required.","No":"No permit is required, with the conditions in the notes.","Depends":"It depends on the details in the notes.",None:"Check with city: we couldn't find a clear answer on the city pages we checked."}[p]
def ld(o): return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False).replace("</","<\\/")+'</script>'
def qpath(c,i): return f"/{CSLUG[c]}/{PSLUG[i]}/"
def qtitle(c,i): return f"Do I need a permit for {PFOR[i]} in {c}, TX?"

# main page
secs=""
for c,rows in data.items():
  trs="".join(f'<tr><td data-l="Project"><a href="{qpath(c,i)}">{e(P[i])}</a></td><td data-l="Permit?">{cell(p)}</td><td data-l="Fee">{cell(f,False)}</td><td data-l="Notes">{e(n)}</td><td data-l="Wildfire (WUI)">{e(WUI[c][i] if c in WUI else WUI_NOTE.get(c,""))}</td><td data-l="Source">{src(s)}</td></tr>' for i,(p,f,n,s) in enumerate(rows))
  secs+=f'<section id="{CSLUG[c]}"><h2>{c}</h2>{AUSTIN_WUI if c=="Austin" else ""}<table><thead><tr><th>Project</th><th>Permit?</th><th>Fee</th><th>Notes</th><th>Wildfire (WUI) rules</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></section>'
body=f'''<header><div><h1>Austin-Area Residential Permit Cheat Sheet</h1>
<p>Do you need a permit for common home projects in <b>Austin, Round Rock, Pflugerville and Cedar Park</b>? Every answer cites the city source it came from. Where we couldn't find a clear answer, it says <b>Check with city</b>.</p></div></header>
<main>{WUICTA}
{TESTS}
<div class="card"><nav>{"".join(f'<a href="#{CSLUG[c]}">{c}</a>' for c in data)}</nav>
{DISC}</div>
{secs}</main>'''
write("/",page("Austin-Area Permit Cheat Sheet: Austin, Round Rock, Pflugerville, Cedar Park","Do you need a permit for a water heater, fence, deck, roof, solar or pool in the Austin area? Answers with links to city sources.","/",body))

# question pages
urls=["/"]; llms=[]; faq_n=0; gaps=[]
for c,rows in data.items():
  for i,(p,f,n,s) in enumerate(rows):
    path=qpath(c,i); t=qtitle(c,i); urls.append(path)
    wui=WUI[c][i] if c in WUI else WUI_NOTE.get(c,"")
    ans=short(p)
    SD={"Yes":"Yes, a permit is required","No":"No permit required (see conditions)","Depends":"It depends on the details",None:"Check with city"}[p]
    desc=f"{P[i]} permit in {c}, TX: {SD}. Fee: {fee_txt(f)}. {"Source: "+(EMAIL[s] if EMAIL[s].startswith("City of") else EMAIL[s][0].lower()+EMAIL[s][1:])+"." if s in EMAIL else "With the city source link, checked "+D+"."}"
    if p is None or f is None: gaps.append(f"{c} / {P[i]}: " + ", ".join(x for x,v in (("permit",p),("fee",f)) if v is None))
    lds=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Permit cheat sheet","item":BASE+"/"},
      {"@type":"ListItem","position":2,"name":c,"item":BASE+"/#"+CSLUG[c]},
      {"@type":"ListItem","position":3,"name":P[i],"item":BASE+path}]}]
    if p is not None:
      faq_n+=1
      lds.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":t,
        "acceptedAnswer":{"@type":"Answer","text":f"{ans} {n} Permit fee: {fee_txt(f)}. Source: {EMAIL[s] if s in EMAIL else S[s]+" (checked "+D+")"}. Informational only; confirm with the City of {c} before starting work."}}]})
    others="".join(f'<li><a href="{qpath(c2,i)}">{e(P[i])} in {c2}</a></li>' for c2 in data if c2!=c)
    more="".join(f'<li><a href="{qpath(c,j)}">{e(P[j])}</a></li>' for j in range(len(P)) if j!=i)
    aus=(AUSTIN_WUI+f'<p><a class="btn" href="{CHECKER}">Check your Austin address for wildfire (WUI) rules</a></p>') if c=="Austin" else ""
    body=f'''<header><div><p class="crumbs"><a href="/">Permit cheat sheet</a> › <a href="/#{CSLUG[c]}">{c}</a> › {e(P[i])}</p><h1>{e(t)}</h1>
<p>Short answer for {c}, Texas, with its source.</p></div></header>
<main><section><h2>Answer</h2><p>{cell(p)} {e(ans)}</p>
<dl class="facts"><dt>Permit required?</dt><dd>{cell(p)}</dd><dt>Permit fee</dt><dd>{e(fee_txt(f))}</dd><dt>Notes</dt><dd>{e(n)}</dd>
<dt>Source</dt><dd>{e(EMAIL[s]) if s in EMAIL else f'<a href="{S[s]}" target="_blank" rel="noopener">{e(S[s])}</a><br><small>checked {D}</small>'}</dd></dl></section>
<section><h2>Wildfire (WUI) rules</h2><p>{e(wui) if wui else "Check with city"}</p>{aus}</section>
{TESTS}
<div class="card">{DISC}<p><a href="/#{CSLUG[c]}">← See all {c} projects in the main permit table</a></p></div>
<section><h2>{e(P[i])} in other cities</h2><ul class="links">{others}</ul><h2>Other projects in {c}</h2><ul class="links">{more}</ul></section></main>'''
    write(path,page(t+" | Texas Permit Guide",desc,path,body,"".join(ld(x) for x in lds)))
    llms.append(f"- [{t}]({BASE}{path}): {('Check with city' if p is None else p)}; fee {fee_txt(f)}")

# click-test pages (no forms, no email collection)
for path,t,msg in [("/quotes/","Get quotes from local pros (coming soon)","We're looking at adding a way to get quotes from local contractors for permit-required projects. It isn't available yet."),
                   ("/hoa/","Need HOA approval too? (coming soon)","Many Austin-area neighborhoods also need HOA architectural approval before you build. We're looking at adding help with that. It isn't available yet.")]:
  body=f'''<header><div><p class="crumbs"><a href="/">Permit cheat sheet</a></p><h1>{e(t)}</h1></div></header>
<main><section><p>{e(msg)}</p><p>Thanks for checking. Your visit helps us decide what to build next.</p><p><a href="/">← Back to the permit cheat sheet</a></p></section></main>'''
  write(path,page(t+" | Texas Permit Guide",msg,path,body,robots="noindex"))

# sitemap + robots
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{BUILD}</lastmod></url>\n" for u in urls)+"</urlset>\n"
open("sitemap.xml","w").write(sm)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

# llms.txt: regenerate the "Question pages" block, keep the rest as written
L=open("llms.txt").read()
L=re.sub(r"## Question pages\n.*?(?=## City sources)","",L,flags=re.S)
block="## Question pages\n\nOne page per city and project, generated from the same data as the main table.\n\n"+"\n".join(llms)+"\n\n"
L=L.replace("## City sources",block+"## City sources",1)
open("llms.txt","w").write(L)
print(json.dumps({"question_pages":len(llms),"faq_pages":faq_n,"sitemap_urls":len(urls),"gaps":len(gaps)}))
for g in gaps: print("GAP",g)
