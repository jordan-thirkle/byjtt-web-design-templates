# PIPELINE — Signal (T-002) · full build provenance

Every step that produced this template, in order. Prompts are verbatim. Current version: **1.0.0**.

## 0. Identity
- Template ID: T-002 · Slug: `signal` · First released: 2026-09-02
- Design DNA: 15 Ash Thorp anchor · palette bg #0A0E13 / surface #11161D / text #E8ECF1 / muted #93A0AE / accent #7C5CFF / accent-deep #5B3FD6 · Space Grotesk + Inter · signature "pulse ring"
- Uniqueness gate: 4/4 dimensions differ vs T-001 (skeleton, signature, palette family, image set) — first real two-entry test.

## 1. Artifacts — Seedream generations (2026-09-02)
Base DNA: "deep near-black navy background, soft violet (#7C5CFF) glow, abstract data streams and pulse rings, subtle grid, premium tech editorial, no text, no watermark".

| Asset | Mode | Prompt (verbatim) | Result |
|---|---|---|---|
| hero.jpg | text→image | "abstract dark product visual for an AI observability dashboard: deep near-black navy background with soft violet (#7C5CFF) glowing data streams, nodes and pulse rings, subtle grid, cinematic depth, clean modern SaaS aesthetic, wide composition, no text, no letters, no UI labels, no watermark" | → 1600px |
| visual.jpg | text→image | "abstract dark visualization: concentric signal rings with glowing violet nodes and thin connection lines over deep near-black navy, soft depth of field, premium tech editorial style, no text, no watermark" | → 1600² |

Post-processing: sips resample; og.jpg center-crop 1200×630 from hero; card.jpg 1200px from hero; numbered gallery 01_hero/02_visual.

## 2. Logo / favicon — authored as SVG (recorded deviation)
Geometric pulse-ring mark authored as inline SVG (`favicon.svg`, 3 concentric rings + core) instead of the seedream→remove-bg loop. Recorded reason: geometric marks are sharper as vectors; the remove-bg QA loop exists for organic marks. Deviation accepted and documented.

## 3. Fonts
Self-hosted latin subsets: spacegrotesk-500/600/700.woff2, inter-400/500/600.woff2 (Inter files reused from the studio font set).

## 4. Build
Files authored with write tool: index.html, css/styles.css, js/main.js. Stack: static HTML/CSS/JS; native `<details>` FAQ; js-gated reveal; honest mailto waitlist.

## 5. QA history
- Automated audit: links resolve, JSON valid, lang correct — PASS on first sweep.
- Uniqueness sanity check in CI-style audit: 3/3 registry DNA fields differ (+ image set) → 4/4 total.
- Gauntlet (2026-09-04): headless-Chrome screenshots at 375/768/1440 + AutoGLM vision review → **CLEAN**; DOM overflow probe → 0px at all widths. No fixes required.

## 6. Deploy history (Cloudflare Pages, project byjtt-templates)
| Date | Build | Change |
|---|---|---|
| 2026-09-04 | 64834f1c | First deploy (T-002 Signal v1.0.0 + prompt kit) |
| 2026-09-04 | latest | Library v1.3 resource page |

## 7. Version history
- 1.0.0 (2026-09-02): initial release; first template to pass the uniqueness gate against an existing entry.
