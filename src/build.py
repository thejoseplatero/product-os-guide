import os, re, html
D = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(D, "frags")
P1 = ["research-hypothesis","customer-interviews","jtbd-framing","personas-archetypes","continuous-discovery","journey-mapping"]
P2 = ["value-proposition","pmf-canvas","business-canvases","four-risks"]
P3 = ["kano-model","prioritization","innovation-games","scoping-mvp","story-mapping"]
P4 = ["strategy-kernel","metrics-trees","okrs","prd","story-writing","states-and-edges"]
P5 = ["experiment-design","usability-testing","heuristic-eval"]
P6 = ["positioning","pricing","gtm-launch","roadmapping","go-roadmap"]
REF = ["moats","premortem","working-backwards","briefs-and-cases","ux-writing","information-architecture","visual-hierarchy","accessibility-audit","design-metrics","design-system-ops","design-canvases","crit-facilitation","stakeholder-comms","calibration","memory-protocol"]
def title(s):
    m = re.search(r"<h2>(.*?)</h2>", s)
    return m.group(1) if m else "?"
def load(n):
    p = os.path.join(F, n + ".html")
    if not os.path.exists(p): return None
    s = open(p).read()
    s = s.replace("—", ", ").replace("–", "-")
    for a,b in [("<h3>Read this to the class</h3>","<h3>The full idea</h3>"),("<dt>They write</dt>","<dt>You write</dt>"),("<dt>Exercise</dt>","<dt>Try it</dt>")]:
        s = s.replace(a,b)
    return s
groups = [("1 · Discover", P1), ("2 · Shape the value", P2), ("3 · Decide and scope", P3), ("4 · Specify", P4), ("5 · Validate", P5), ("6 · Go to market", P6), ("Reference shelf", REF)]
nav, body, missing = [], [], []
sysf = load("_system")
nav.append('<a href="#top" class="nav-home">Start here</a>')
nav.append('<a href="#system">The shape of Product OS</a>')
for label, names in groups:
    nav.append(f'<p class="nav-group">{label}</p>')
    for n in names:
        s = load(n)
        if not s: missing.append(n); continue
        nav.append(f'<a href="#{n}">{html.escape(title(s))}</a>')
        body.append(s)
css = open(os.path.join(D, "site.css")).read()
home = open(os.path.join(D, "home.html")).read()
out = f"""<title>Product OS Guide</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:title" content="Product OS Guide">
<meta property="og:description" content="One real problem, worked end to end. 44 product skills from discovery through go to market.">
<meta property="og:image" content="https://thejoseplatero.github.io/product-os-guide/og.png">
<meta property="og:url" content="https://thejoseplatero.github.io/product-os-guide/">
<meta name="twitter:card" content="summary_large_image">
<style>{css}</style>
<input type="checkbox" id="navtoggle" hidden>
<label for="navtoggle" class="navbtn" aria-label="Open contents">Contents</label>
<nav class="side">{''.join(nav)}</nav>
<div class="brandbar"><div class="brandbar-in">
<a class="wordmark" href="https://github.com/thejoseplatero/product-os">PRODUCT<span class="dot">&middot;</span>OS</a>
<span class="kicker">Guide</span>
</div></div>
<main class="page" id="top">
{home}
{sysf or ''}
{''.join(body)}
<hr><p class="foot">Jose Platero &middot; Product OS Guide &middot; one case, six phases, 44 skills</p>
</main>
"""
OUT = os.path.join(os.path.dirname(D), "index.html")
he = out.index("</style>") + len("</style>")
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
       '<meta name="description" content="Learn product management by working one real case end to end: the Uber Eats weekday lunch gap. 44 skills from discovery to go to market.">\n'
       + out[:he] + "\n</head>\n<body>" + out[he:] + "\n</body>\n</html>\n")
open(OUT, "w").write(doc)
print("built; missing:", missing, "; size KB:", len(out)//1024)
