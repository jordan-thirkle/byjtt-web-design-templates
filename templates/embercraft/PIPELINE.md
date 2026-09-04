# PIPELINE — Embercraft (T-001) · full build provenance

Every step that produced this template, in order. Prompts are verbatim. Current version: **1.1.0**.

## 0. Identity
- Template ID: T-001 · Slug: `embercraft` · First released: 2026-09-02
- Design DNA: 18 Kenya Hara anchor · palette paper #FAF6F0 / surface #F1E9DE / ink #2B211B / ember #C25E33 / ember-deep #8A3B1F · Fraunces + Inter · signature "ember line"

## 1. Artifacts — Seedream generations (2026-09-02)
All generations via `autoglm-generate-image-seedream`, base DNA: "warm editorial photograph, soft morning window light, film grain, cream and burnt-orange palette, specialty coffee roastery, shallow depth of field, no text, no watermark".

| Asset | Mode | Prompt (verbatim) | Result |
|---|---|---|---|
| hero.jpg | text→image | "wide cinematic view of a specialty coffee roastery bar at dawn, brass drum roaster with gentle steam, kraft paper bean bags on reclaimed wood counter, " + BASE | 3136×1344 → 1600px, 171 KB |
| story.jpg | image→image (hero ref via upload-mix OSS URL) | "close-up of hands cupping freshly roasted coffee beans above a cooling tray, " + BASE | 2048² → 1600², 226 KB (q70) |
| product.jpg | image→image (hero ref) | "three kraft paper coffee bags with blank burnt-orange labels standing on a wooden shelf against a cream plaster wall, " + BASE | 2048² → 1600², 199 KB (q60) |
| card.jpg | image→image (hero ref) | "a ceramic pour-over cup of black coffee on a wooden counter, blurred roastery glow behind, " + BASE | 1200px, 178 KB |
| logo.jpg | text→image | "minimal flat vector-style logo mark of a single coffee bean merged with a small ember flame, burnt orange (#C25E33) on solid plain cream background (#FAF6F0), simple geometric shapes, centered with generous margins, flat solid background, no text, no letters, no watermark" | 108 KB source |

Post-processing: sips resample/crop; og.jpg center-cropped to exactly 1200×630; numbered gallery copies 01_hero/02_story/03_product.

## 2. Logo transparency — 3-round QA loop (mandatory remove-bg + recognition)
1. `remove-bg.py logo.jpg → logo-transparent.png` tol 40 → recognition: FAIL (white fringe halo + stray fragments, corners).
2. Retry tol 55 + --min-area=400 → recognition: FAIL (one stray fragment top-left + dead canvas space).
3. tol 55 + --min-area=2000 + custom largest-connected-component cleanup (BFS, keep logo component only, 152,702 px of 167,823) + PIL bbox trim → **logo-final.png 383×535** → recognition: **PASS (suitable to ship)** → favicon padded square 64×64 (PIL) → 46→64 square, 5.3 KB.

## 3. Fonts
Self-hosted Google Fonts latin subsets: fraunces-600.woff2 (18.1 KB), inter-400/500/600.woff2 (48.4 KB each) — added in v1.0 gauntlet fix (fonts were claimed in v1.0.0 but not loaded — Blocker fixed).

## 4. Build
Files authored with write/apply_patch: index.html, css/styles.css, js/main.js. Stack: static HTML/CSS/JS, no build step, no CDN. HTML lang="en".

## 5. QA history
- Static audit v1.0.0: FAIL initially (1 broken ref + false "placeholder" positive) → fixed → PASS.
- Gauntlet round 1 (2026-09-02, two independent reviewers): 2 Blockers (no-JS content wipe; phantom fonts) + 4 Majors (AA contrast fail on buttons + falsely certified QA records; license-ladder contradiction; live-preview CTA at undeployed URL; inline grid style broke mobile gallery) + minors → ALL FIXED (see docs/gauntlet-report.md).
- Machine-file fixes: license string exact-match; assets.card dead path; catalog↔manifest field-equality diff added to gate.
- v1.1.0 (2026-09-02, benchmark-driven): café-grade cards, subscription band, freshness storytelling, eyebrows, 3 bag images (see §6).
- Gauntlet round 2 (2026-09-04): headless-Chrome screenshots at 375/768/1440 + vision QA + DOM overflow probe (puppeteer-core) → found 24px horizontal overflow from `.sub-grid` at 375px → FIXED (media query) → probe over=0px.

## 6. Artifacts — bag photography (v1.1.0, hero-referenced)
| Asset | Prompt (verbatim) | Result |
|---|---|---|
| bag-dawn.jpg | "close-up of a single kraft paper coffee bag with a blank burnt-orange label standing on a reclaimed wood counter, gentle steam wisp behind, " + BASE | 1600², 148 KB |
| bag-ember.jpg | "two kraft paper coffee bags with blank burnt-orange labels side by side on a cream plaster shelf against a warm wall, " + BASE | 1600², 183 KB |
| bag-midnight.jpg | "a kraft paper coffee bag tipped with roasted beans scattered across dark walnut wood, moody warm sidelight, " + BASE | 1600×685, 88 KB |

## 7. Deploy history (Cloudflare Pages, project byjtt-templates)
| Date | Build | Change |
|---|---|---|
| 2026-09-02 | 9cf44832 | First deploy (marketplace + Embercraft v1.0.0), 27 files |
| 2026-09-02 | 51a9ab46 | Canonical flip to Cloudflare + custom domain wiring |
| 2026-09-02 | (multiple) | Gauntlet fixes; v1.1.0 release; library/explore v1.3 |
| 2026-09-04 | latest | v1.3 library shell; sub-grid overflow fix |

GitHub Pages mirror (gh-pages branch) synced at every release; custom domain templates.byjtt.com (CNAME, proxied).

## 8. Version history
- 1.0.0 (2026-09-02): initial release after QA + uniqueness gates.
- 1.1.0 (2026-09-02): MINOR — benchmark-driven refinements + new subscription section + mobile overflow fix.
