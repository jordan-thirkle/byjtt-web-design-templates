# QA-CHECKLIST — Embercraft (T-001)

Re-verified after gauntlet round 1 fixes (2026-09-02). Claims are machine-verified, not narrative: every tick cites the check that proved it.

- [x] All internal links/images resolve — automated sweep across site + previews: PASS (consolidate.py)
- [x] JS disabled ⇒ all content visible — reveal hidden state gated behind `html.js` (CSS `.js .reveal` + JS `classList.add("js")`): verified by grep
- [x] Fonts declared = fonts shipped — `designDNA.fonts` [Fraunces, Inter] backed by 4 self-hosted `@font-face` woff2 files (18–48 KB each): verified by grep + files[]
- [x] Computed contrast (calculator-derived): ink/paper 14.6:1 · muted/paper 6.1:1 · muted/surface 5.46:1 · white-on-ember-deep buttons 7.16:1 (AA) · ember/paper 3.9:1 = decorative only
- [x] `:disabled` / `[aria-disabled]` style exists in CSS (grep-verified) — used by the preview-pending button
- [x] Hero scrim: paper coverage ≥0.82 at the text block zone (strengthened post-gauntlet)
- [x] Tap targets ≥44px: nav toggle + marketplace nav links (CSS min-width/min-height)
- [x] Reduced motion: global `* { transition/animation: none !important }` block (grep-verified)
- [x] No inline layout styles (`grid-template-columns` etc. banned); gallery uses `.grid-2` class — media queries win at 375px
- [x] Images carry width/height attributes (CLS); photos ≤1600px wide, ≤226KB (hero 171KB, story 226KB, product 199KB, og 126KB)
- [x] Favicon: square 64×64 transparent PNG (PIL-padded), verified via sips/PIL
- [x] Meta: title/description/og:*/twitter card + favicon paths correct; og:image `assets/og.jpg` 1200×630 (sips-verified)
- [x] Machine contract: manifest ↔ catalog field-equality diff PASS; license string exact-match (`ByJTT Free Template License`) across manifest/catalog/registry/pages; path lint on files[] + assets.card PASS
- [x] Honest commerce: free tier — no purchase UI, `purchaseState:"not-applicable"`, real download zip (byte-compared against site tree); preview CTA disabled ("Preview pending deployment") until a host-reported URL exists
- [x] No lorem/TODO/placeholder strings (the phrase "no placeholders" in marketing copy is intentional content)
- [x] No secrets, node_modules, or server runtime deps; static-only hosting respected
- [x] Uniqueness: catalog-empty baseline at design time; DNA registered (DESIGN-NOTES §10)
