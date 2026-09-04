#!/usr/bin/env python3
"""Generate BuiltByBit-style resource pages + explore cards for every ByJTT template.
Data-driven from registry + manifests: every fact/stat shown is real. Usage: python3 gen-listing.py"""
import json, html, os

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = __import__("datetime").datetime.utcnow().strftime("%Y-%m-%d")

ICONS = {
    "download": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v8m0 0l-3-3m3 3l3-3M3 13h10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "tag": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 7V3a1 1 0 011-1h4l7 7-5 5-7-7z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="5.5" cy="4.5" r="1" fill="currentColor"/></svg>',
    "box": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1l6 3.5v7L8 15 2 11.5v-7L8 1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M2 4.5L8 8l6-3.5M8 8v7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>',
    "calendar": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><rect x="2" y="3" width="12" height="11" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M2 6.5h12M5.5 1.5v3m5-3v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
    "layers": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1l7 4-7 4-7-4 7-4z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M1 9.5l7 4 7-4M1 12.5l7 4 7-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" opacity=".55"/></svg>',
    "gauge": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="8" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M4 13h8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
    "grid": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="1.5" width="5.5" height="5.5" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="9" y="1.5" width="5.5" height="5.5" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="1.5" y="9" width="5.5" height="5.5" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/><rect x="9" y="9" width="5.5" height="5.5" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>',
    "image": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="1.5" width="13" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="5.5" cy="5.5" r="1.4" fill="currentColor"/><path d="M2 12l4-4 3 3 2.5-2.5L14.5 12" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>',
    "type": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 3.5h11M8 3.5V13M5.5 13h5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
    "palette": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="6" cy="6" r="1" fill="currentColor"/><circle cx="10.5" cy="5.5" r="1" fill="currentColor"/><circle cx="11" cy="9.5" r="1" fill="currentColor"/><circle cx="7.5" cy="11" r="1" fill="currentColor"/></svg>',
    "shield": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1l5.5 2v4.5c0 3.4-2.3 6-5.5 7.5C4.8 13.5 2.5 10.9 2.5 7.5V3L8 1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M5.5 7.5L7.5 9.5l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "globe": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M1.5 8h13M8 1.5c2 1.8 3 4 3 6.5s-1 4.7-3 6.5c-2-1.8-3-4-3-6.5s1-4.7 3-6.5z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>',
    "check": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 8.5L6 12l7.5-8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "user": '<svg class="i" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="5" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M2 14.5c.8-3 3-4.5 6-4.5s5.2 1.5 6 4.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
}

CONFIG = {
    "embercraft": {
        "tagline": "A warm editorial one-pager for specialty coffee roasters",
        "about": [
            "Embercraft targets independent craft businesses that want one decisive page instead of a multi-page site. The hero uses a generated dawn-roastery photograph under a paper scrim; the story section pairs editorial copy with a stat strip; the bean cards carry café-grade data — origin, process, roast level, tasting-note chips, prices and a roast-week badge — over generated bag photography.",
            "A dark band presents subscription cadences with an honest email-start flow, and hours plus contact close the page. Typography pairs Fraunces with Inter on a Kenya-Hara-anchored whitespace rhythm; the signature 'ember line' recurs throughout.",
        ],
        "inside": [
            "One-page layout: hero, story, weekly beans, visit, contact footer",
            "Café-grade bean cards: spec row, tasting-note chips, price, roast-week badge",
            "Subscription cadence band with honest email-start flow",
            "Responsive at 375 / 768 / 1440; mobile nav with proper toggle state",
            "Accessibility: skip link, landmarks, alt text, focus rings, reduced-motion support",
            "Generated imagery: hero, story, product, card cover — one consistent art direction",
        ],
        "gauntlet": "Passed · rounds 1–2 + browser QA",
        "uniqueness": "Unique — 4/4 dimensions vs catalog",
        "featured_line": "Landing page · specialty coffee roaster · warm editorial · English · v1.1.0",
    },
    "signal": {
        "tagline": "A dark technical one-pager for AI-agent analytics SaaS",
        "about": [
            "Signal targets technical teams shipping AI agents who want an instrument-panel landing page: a centered hero over a generated glow visual, a six-card feature grid (usage, spend, latency, guardrails, audit, alerts), three-tier pricing with a highlighted plan, a native-details FAQ, and an early-access band with an honest email flow.",
            "Space Grotesk + Inter on a near-black navy canvas with a single violet accent and the pulse-ring signature motif. The deliberate opposite register of Embercraft — proof the studio spans the palette.",
        ],
        "inside": [
            "One-page structure: hero, six features, 3-tier pricing, FAQ, waitlist band",
            "Native-details FAQ accordion — keyboard-native, no JS dependency",
            "Self-contained static HTML/CSS/JS — no build step, no required CDN",
            "Responsive at 375 / 768 / 1440",
            "Accessibility: skip link, landmarks, alt text, focus rings, reduced-motion support",
            "Generated visuals: hero glow + signal-rings, one consistent dark art direction",
        ],
        "gauntlet": "Passed · uniqueness gate 4/4 + visual QA",
        "uniqueness": "Unique — 4/4 dimensions vs catalog",
        "featured_line": "Landing page · AI-agent analytics SaaS · dark technical · English · v1.0.0",
    },
}

def human_size(n):
    return f"{n/1024:.0f} KB" if n < 1024*1024 else f"{n/1024/1024:.2f} MB"

def fact_row(icon, label, value):
    return (f'<div class="fact"><span class="fact-i">{ICONS[icon]}</span>'
            f'<span class="fact-l">{label}</span><span class="fact-v">{value}</span></div>')

reg = json.load(open(f"{B}/registry.json"))
canon = reg["deployment"]["lastUrl"].rstrip("/")

cards, pages = [], []
for e in reg["templates"]:
    slug = e["slug"]
    cfg = CONFIG[slug]
    man = {k: v for k, v in e.items() if k not in ("status", "releaseState")}
    files = man["files"]
    total = sum(f["bytes"] for f in files)
    n_sections = len(man["designDNA"]["layoutSkeleton"])
    n_images = sum(1 for f in files if "/assets/" in f["path"] and f["path"].endswith((".jpg", ".png")))
    n_fonts = len(man["designDNA"]["fonts"])
    palette = man["designDNA"]["palette"]
    swatches = "".join(f'<span class="swatch" style="background:{c}" title="{c}"></span>' for c in palette[:6])
    tags = "".join(f'<a class="tag-chip" href="../index.html">{html.escape(t)}</a>' for t in man["tags"][:5])
    tier_badge = '<span class="tier tier-free">Free</span>' if man["tier"] == "free" else '<span class="tier tier-paid">Paid</span>'

    gallery = "".join(
        f'<figure class="shot"><img src="../assets/templates/{slug}/{s}" alt="{html.escape(man["name"])} preview: {s.split("_",1)[-1].split(".")[0]}" style="width:100%; border-radius:14px; box-shadow:0 10px 30px rgba(43,33,27,.10);" loading="lazy"></figure>'
        for s in man["assets"]["gallery"])

    about_html = "".join(f"<p>{p}</p>" for p in cfg["about"])
    inside_html = "".join(f"<li>{x}</li>" for x in cfg["inside"])
    dna_html = f"""
        <div class="dna-block">
          <p class="dna-label">Palette</p>
          <div class="swatches">{swatches}</div>
          <p class="dna-label">Type</p>
          <p>{' + '.join(man['designDNA']['fonts'])}</p>
          <p class="dna-label">Signature element</p>
          <p>{man['designDNA']['signatureElement']}</p>
          <p class="dna-label">Preset anchor</p>
          <p>{man['designDNA']['presetAnchor']}</p>
        </div>"""

    # sidebar facts — every factor, all real
    facts = "".join([
        fact_row("box", "Version", man["version"]),
        fact_row("calendar", "Released", man["createdAt"][:10]),
        fact_row("calendar", "Updated", man["updatedAt"][:10]),
        fact_row("tag", "Category", man.get("category", man["archetype"])),
        fact_row("globe", "Language", man["language"]),
        fact_row("shield", "License", man["license"].replace(" (see licensing.html)", "")),
        fact_row("layers", "Files", f"{len(files)}"),
        fact_row("gauge", "Total size", human_size(total)),
        fact_row("grid", "Sections", f"{n_sections}"),
        fact_row("image", "Images", f"{n_images}"),
        fact_row("type", "Fonts", f"{n_fonts}"),
        fact_row("check", "Gauntlet", cfg["gauntlet"]),
        fact_row("check", "Uniqueness", cfg["uniqueness"]),
        fact_row("box", "Template ID", man["id"]),
    ])

    kit_rel = e.get("promptKit", f"./kits/{slug}/v1.0/").lstrip("./")
    kit_dir = f"{B}/site/{kit_rel}"
    kit_files = sorted(os.listdir(kit_dir))
    kit_links = "".join(f'<li><a href="../{kit_rel}{f}" download>{f}</a></li>' for f in kit_files if f.endswith(".md"))

    prompts = [
        ("build-it", "Build it", "build-prompt.md", "Download the template and build a personalized site — start here."),
        ("brand-customize", "Brand-customize it", "brand-customize-prompt.md", "Delta prompt: apply your brand to an existing build."),
        ("iterate-on-it", "Iterate on it", "iterate-prompt.md", "Delta prompt: request changes with the design rules enforced."),
        ("publish-it", "Publish it", "publish-prompt.md", "One prompt to deploy your finished site to your own Cloudflare."),
    ]
    blocks = []
    for pslug, ptitle, pfname, pblurb in prompts:
        ptext = open(os.path.join(kit_dir, pfname), encoding="utf-8").read()
        blocks.append(f'''      <details class="prompt-block" id="prompt-{pslug}">
        <summary>
          <span class="prompt-title">{ptitle}</span>
          <span class="prompt-blurb">{pblurb}</span>
          <button class="copy-btn" type="button" data-copy-target="pre-{pslug}" aria-label="Copy the {ptitle} prompt">Copy</button>
        </summary>
        <p class="prompt-meta"><a href="../{kit_rel}{pfname}" download>View raw ({pfname})</a> · placeholders in [BRACKETS] are yours</p>
        <pre id="pre-{pslug}">{html.escape(ptext)}</pre>
      </details>''')
    kit_html = "\n".join(blocks)

    page = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__NAME__ — __ARCH__ template · ByJTT Web Design Templates</title>
  <meta name="description" content="__DESC__">
  <link rel="icon" type="image/svg+xml" href="../assets/shared/favicon.svg">
  <link rel="stylesheet" href="../assets/shared/marketplace.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="../index.html"><span class="brand-mark" aria-hidden="true"></span> ByJTT Templates</a>
      <nav class="site-nav" aria-label="Primary">
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../templates.html" aria-current="page">Explore</a></li>
          <li><a href="../licensing.html">Licensing</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a class="machine-link" href="../catalog.json">catalog.json</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <div class="wrap crumb"><a href="../templates.html">Explore</a> <span aria-hidden="true">/</span> __NAME__</div>
    <section class="res-head">
      <div class="wrap res-head-grid">
        <div>
          <p class="res-cat">__CAT__ · __ARCH__</p>
          <h1>__NAME__ <span class="tier tier-free">__TIER__</span></h1>
          <p class="res-tag">__TAGLINE__</p>
          <div class="tag-row">__TAGS__</div>
        </div>
        <aside class="res-box">
          <p class="res-price">Free</p>
          <a class="btn btn-solid btn-full" href="__ZIP__" download>__DL__</a>
          <p class="res-box-note">__LIC_SHORT__ · full terms on the <a href="../licensing.html">licensing page</a></p>
          <div class="res-facts">__FACTS__</div>
        </aside>
      </div>
    </section>

    <section aria-labelledby="shots-title">
      <div class="wrap">
        <h2 class="section-title" id="shots-title">Preview</h2>
        <div class="shot-stack">__GALLERY__</div>
      </div>
    </section>

    <section class="band" aria-labelledby="about-title">
      <div class="wrap res-grid">
        <div>
          <h2 class="section-title" id="about-title">About this template</h2>
          __ABOUT__
          <h3 class="res-h3">What's inside</h3>
          <ul class="feature-list">__INSIDE__</ul>
          <h3 class="res-h3">Design DNA</h3>
          __DNA__
        </div>
        <aside>
          <div class="author-card">
            <p class="author-avatar" aria-hidden="true">B</p>
            <p class="author-name">ByJTT Studio</p>
            <p class="author-note">AI-run design studio. Every template passes a two-reviewer gauntlet and a uniqueness diff before listing.</p>
            <p class="author-links"><a href="https://github.com/jordan-thirkle/byjtt-web-design-templates">GitHub</a></p>
          </div>
          <div class="author-card">
            <p class="footer-h">Prompt kit</p>
            <ul class="kit-links">__KITLINKS__</ul>
          </div>
        </aside>
      </div>
    </section>

    <section aria-labelledby="kit-title">
      <div class="wrap">
        <span class="ember-hair" aria-hidden="true"></span>
        <h2 class="section-title" id="kit-title">Remix it with your agent — no account needed</h2>
        <p class="lead" style="margin-top:.8rem;">Copy a prompt into your own coding agent. Build it from the template package, brand it, iterate, then publish to your own Cloudflare. The full text is on the page — nothing hidden behind an account.</p>
        <p class="token-legend">Placeholders: <code>[YOUR-…]</code> = fill before or during the run · <code>{{…}}</code> = your agent will ask you. Kit files stay versioned at <code>/kits/__SLUG__/</code>.</p>
__KIT__
      </div>
    </section>

    <section aria-labelledby="agents-title">
      <div class="wrap">
        <span class="ember-hair" aria-hidden="true"></span>
        <h2 class="section-title" id="agents-title">Notes for AI agents</h2>
        <div class="two-col">
          <div>
            <ul class="feature-list">__BESTFOR__</ul>
          </div>
          <div>
            <p>Deep contract: <a href="../manifests/__SLUG__.json">manifests/__SLUG__.json</a> — files, assets, design DNA, license, changelog. Machine catalog: <a href="../catalog.json">catalog.json</a>.</p>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="../index.html"><span class="brand-mark" aria-hidden="true"></span> ByJTT Templates</a>
          <p class="footer-mission">One-shot website designs built by an AI studio — finished, unique, and published for humans and agents.</p>
          <p class="footer-live"><a href="https://templates.byjtt.com">templates.byjtt.com</a> · <a href="https://github.com/jordan-thirkle/byjtt-web-design-templates">GitHub</a></p>
        </div>
        <nav class="footer-nav" aria-label="Footer">
          <div>
            <p class="footer-h">Marketplace</p>
            <ul>
              <li><a href="../index.html">Home</a></li>
              <li><a href="../templates.html">Explore</a></li>
              <li><a href="../licensing.html">Licensing</a></li>
              <li><a href="../about.html">About</a></li>
            </ul>
          </div>
          <div>
            <p class="footer-h">For agents</p>
            <ul>
              <li><a href="../catalog.json">catalog.json</a></li>
              <li><a href="../.well-known/ai-catalog.json">ai-catalog.json</a></li>
              <li><a href="../llms.txt">llms.txt</a></li>
              <li><a href="../manifests/__SLUG__.json">__SLUG__ manifest</a></li>
            </ul>
          </div>
        </nav>
      </div>
      <p class="footer-fine">© 2026 ByJTT · __NAME__ is a fictional showcase brand. <a href="../licensing.html">License terms</a>.</p>
    </div>
  </footer>

  <script src="../assets/shared/marketplace.js" defer></script>
</body>
</html>
"""
    hints = "".join(f"<li><strong>Best for:</strong> {html.escape(h)}</li>" for h in man["agentHints"]["bestFor"]) + \
            "".join(f"<li><strong>Avoid if:</strong> {html.escape(h)}</li>" for h in man["agentHints"]["avoidIf"])
    page = (page
        .replace("__NAME__", man["name"]).replace("__ARCH__", man["archetype"].title())
        .replace("__DESC__", html.escape(man["description"]))
        .replace("__CAT__", man.get("category", man["archetype"]))
        .replace("__TIER__", man["tier"].title()).replace("__TAGLINE__", html.escape(cfg["tagline"]))
        .replace("__TAGS__", tags)
        .replace("__ZIP__", f"../assets/templates/{slug}/downloads/{slug}-v{man['version']}.zip")
        .replace("__DL__", "Download template (free)" if man["tier"] == "free" else f"Buy · ${man['price']['amount']}")
        .replace("__LIC_SHORT__", man["license"].replace(" (see licensing.html)", ""))
        .replace("__FACTS__", facts).replace("__GALLERY__", gallery)
        .replace("__ABOUT__", about_html).replace("__INSIDE__", inside_html)
        .replace("__DNA__", dna_html).replace("__KITLINKS__", kit_links)
        .replace("__KIT__", kit_html).replace("__BESTFOR__", hints)
        .replace("__SLUG__", slug))
    pages.append((slug, page))

    cards.append(f"""      <article class="res-card" data-cat="{man.get('category','')}" data-tier="{man['tier']}">
        <a class="res-thumb" href="templates/{slug}.html"><img src="assets/templates/{slug}/card.jpg" alt="{html.escape(man['name'])} cover" loading="lazy"></a>
        <div class="res-body">
          <div class="res-row1"><h3><a href="templates/{slug}.html">{html.escape(man['name'])}</a></h3><span class="tier tier-free">{man['tier'].title()}</span></div>
          <p class="res-tag">{html.escape(cfg['tagline'])}</p>
          <div class="res-meta">
            <span>{ICONS['box']} v{man['version']}</span>
            <span>{ICONS['layers']} {len(files)} files</span>
            <span>{ICONS['gauge']} {human_size(total)}</span>
            <span>{ICONS['calendar']} {man['updatedAt'][:10]}</span>
          </div>
          <div class="res-foot">
            <span class="res-cat-chip">{man.get('category','')}</span>
            <a class="btn btn-ghost btn-sm" href="templates/{slug}.html">View resource</a>
          </div>
        </div>
      </article>""")

# explore page
cards_html = "\n".join(cards)
cat_list = sorted({e.get("category", e["archetype"]) for e in reg["templates"]})
cat_btns = '<button class="filter-btn is-on" data-filter-cat="all">All</button>' + "".join(
    f'<button class="filter-btn" data-filter-cat="{c}">{c.title()}</button>' for c in cat_list)
tier_btns = ('<button class="filter-btn is-on" data-filter-tier="all">All</button>'
             '<button class="filter-btn" data-filter-tier="free">Free</button>'
             '<button class="filter-btn" data-filter-tier="paid">Paid</button>')

explore = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Explore templates — ByJTT Web Design Templates</title>
  <meta name="description" content="Explore the ByJTT template library: unique one-shot website designs with full specs, live previews and agent prompt kits.">
  <link rel="icon" type="image/svg+xml" href="assets/shared/favicon.svg">
  <link rel="stylesheet" href="assets/shared/marketplace.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span> ByJTT Templates</a>
      <nav class="site-nav" aria-label="Primary">
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="templates.html" aria-current="page">Explore</a></li>
          <li><a href="licensing.html">Licensing</a></li>
          <li><a href="about.html">About</a></li>
          <li><a class="machine-link" href="catalog.json">catalog.json</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="hero-band">
      <div class="wrap">
        <h1>Explore the library</h1>
        <span class="ember-rule" aria-hidden="true"></span>
        <p class="lead">Every resource below passed the studio gauntlet and a uniqueness diff against the whole catalog. Full specs on every page — nothing half-finished gets listed.</p>
      </div>
    </section>

    <section aria-labelledby="all-title">
      <div class="wrap">
        <div class="filter-bar" role="group" aria-label="Filter resources">
          <div class="filter-group"><span class="filter-label">Type</span>__CATBTN__</div>
          <div class="filter-group"><span class="filter-label">Tier</span>__TIERBTN__</div>
        </div>
        <div class="res-grid-lib" id="res-grid">
__CARDS__
        </div>
        <p class="empty-note" id="res-empty" hidden>No resources match those filters yet.</p>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span> ByJTT Templates</a>
          <p class="footer-mission">One-shot website designs built by an AI studio — finished, unique, and published for humans and agents.</p>
          <p class="footer-live"><a href="https://templates.byjtt.com">templates.byjtt.com</a> · <a href="https://github.com/jordan-thirkle/byjtt-web-design-templates">GitHub</a></p>
        </div>
        <nav class="footer-nav" aria-label="Footer">
          <div>
            <p class="footer-h">Marketplace</p>
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><a href="templates.html">Explore</a></li>
              <li><a href="licensing.html">Licensing</a></li>
              <li><a href="about.html">About</a></li>
            </ul>
          </div>
          <div>
            <p class="footer-h">For agents</p>
            <ul>
              <li><a href="catalog.json">catalog.json</a></li>
              <li><a href=".well-known/ai-catalog.json">ai-catalog.json</a></li>
              <li><a href="llms.txt">llms.txt</a></li>
              <li><a href="manifests/embercraft.json">embercraft manifest</a></li>
            </ul>
          </div>
        </nav>
      </div>
      <p class="footer-fine">© 2026 ByJTT · Templates licensed per the <a href="licensing.html">licensing page</a>.</p>
    </div>
  </footer>

  <script src="assets/shared/marketplace.js" defer></script>
</body>
</html>
""".replace("__CATBTN__", cat_btns).replace("__TIERBTN__", tier_btns).replace("__CARDS__", cards_html)
open(f"{B}/site/templates.html", "w").write(explore)
for slug, page in pages:
    open(f"{B}/site/templates/{slug}.html", "w").write(page)
print(f"generated: {len(pages)} resource pages + explore page ({len(cat_list)} categories)")

# index: nav label + featured section title
p = f"{B}/site/index.html"
t = open(p).read()
t = t.replace('<li><a href="templates.html">Templates</a></li>', '<li><a href="templates.html">Explore</a></li>')
t = t.replace('<h2 class="section-title" id="newest-title">Newest template</h2>',
              '<h2 class="section-title" id="newest-title">Featured resource</h2>')
t = t.replace('<p class="card-meta">Landing page · specialty coffee roaster · warm editorial · English</p>',
              '<p class="card-meta">Landing page · specialty coffee roaster · warm editorial · English</p>')
open(p, "w").write(t)
# licensing/about: nav label
for f in ("licensing.html", "about.html"):
    t = open(f"{B}/site/{f}").read()
    t = t.replace('<li><a href="templates.html">Templates</a></li>', '<li><a href="templates.html">Explore</a></li>')
    t = t.replace('<li><a href="templates.html">Explore</a></li>\n              <li><a href="licensing.html">', '<li><a href="templates.html">Explore</a></li>\n              <li><a href="licensing.html">')
    open(f"{B}/site/{f}", "w").write(t)
print("nav labels updated to Explore")
