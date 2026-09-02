# Gauntlet Report — Round 1 (T-001 Embercraft)

First run of the studio gauntlet: two independent adversarial reviewers (design/UX, code/policy) on the finished template + marketplace.

## Verdict before fixes: not publishable as-is
- Design review: 2 Blockers, 6 Majors, 6 Minor bundles
- Code review: 0 Blockers, 3 Majors, 9 Minors

## Blockers found (and fixed)
1. **No-JS content wipe** — `.reveal{opacity:0}` hid the story, cards, and visit sections when JavaScript was off. Fixed: hidden state gated behind a JS-added `html.js` class; QA now includes an explicit "JS disabled ⇒ all content visible" check.
2. **Phantom fonts** — Fraunces/Inter were declared in the design DNA, the manifest, the catalog, and the detail page, but never loaded — the design shipped in Georgia/system-ui. Fixed: 4 self-hosted woff2 files (~163 KB total) with @font-face; static-hosting compliant.

## Majors found (and fixed)
- White-on-ember buttons failed WCAG AA (4.25:1) while the QA checklist certified contrast with unverified numbers → buttons moved to `--ember-deep` (7.16:1), contrast table recomputed for every pair.
- Hero headline floated over an under-scrimmed bright photo → scrim strengthened to ≥0.82 paper coverage at the text zone.
- Licensing contradiction: free tier granted commercial use, undercutting the paid ladder → ladder made single-source (personal/non-commercial free; Commercial 5,000 / Extended 250,000 are paid), all four surfaces regenerated from it.
- Live-preview CTA shipped enabled at a not-yet-deployed path → now a disabled "Preview pending deployment" control that activates only from a host-reported URL.
- Inline `grid-template-columns` style beat the mobile media query (two 165px screenshots at 375px) → `.grid-2` class; all three gallery shots embedded.
- Manifest pointed `assets.card` at a nonexistent path → path lint added to the publish gate; pointer fixed.

## Also fixed (minors)
Square 64×64 favicon · 44px tap targets · global reduced-motion block · scroll-margin for sticky header · width/height on images (CLS) · photos recompressed (story 226KB, product 199KB) · dead 70KB logo.png purged from the shipped site · `role="status"` → `role="note"` · version + license name on the detail page · license string exact-match across manifest/catalog/registry · catalog↔manifest field-equality diff added to the gate.

## What the gauntlet verified as already solid
JSON validity ×5, manifest copies byte-identical, counts 1==1==1, honest `liveUrl:null`, real working zip (byte-compared), heading order, landmarks, alt text everywhere, no secrets/lorem, node --check clean, CSS tokens disciplined, copy specific and sensory, empty-state honesty.

## Systemic lesson
The two false QA pass records (contrast, disabled-state) were the deepest finding: the Phase 5 gate trusted narrative claims. Every QA tick now cites the machine check that proved it — see lessons-learned.md.
