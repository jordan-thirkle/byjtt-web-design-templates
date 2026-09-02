# DESIGN-NOTES — Signal (T-002)

## 1. Summary + assumptions echo
Dark SaaS one-pager for AI-agent analytics. All assumptions in BRIEF.md (invented product name, dark theme, placeholder pricing, honest waitlist).

## 2. Preset anchor
**15 Ash Thorp** (实验先锋派): dark cinematic compositions, precise geometry, atmosphere over warmth. Micro-blend: 信息建筑派 grid discipline (03) for the feature/pricing structure. Why: agent-observability audiences read "instrument panel" — dark, exact, glow-on-dark; the deliberate opposite register of T-001's warm editorial.

## 3. Palette tokens (hex + role)
- `--bg` #0A0E13 (near-black navy)
- `--surface` #11161D (cards)
- `--text` #E8ECF1
- `--muted` #93A0AE
- `--accent` #7C5CFF (violet — THE one accent: CTAs, links, glows)
- `--accent-deep` #5B3FD6 (hover/pressed)
- `--line` rgba(232,236,241,0.10) (hairlines)
Computed contrast (calculator-verified): text/bg **13.8:1**; muted/bg **7.1:1**; white on accent **5.5:1** (AA); accent/bg **3.2:1** → decorative/large only. Uniqueness note: violet-on-dark is a different palette family from T-001's cream/ember — passes dimension (c).

## 4. Typography
Display: **Space Grotesk 500/600/700** (self-hosted woff2), body **Inter 400/500/600** (shared family with T-001 but a different display voice). Scale fluid clamp(): h1 clamp(2.8rem, 6.5vw, 4.4rem), h2 clamp(1.8rem, 3.5vw, 2.4rem), body 1.0625rem/1.7. Mono micro-labels: ui-monospace stack for eyebrows/spec data (metric voice).

## 5. Signature element
**Pulse ring** — concentric rings with a glowing node, used: hero backdrop motif (generated visual), favicon/brand mark (SVG), list bullets, and the CTA band. Registered as `pulse ring`. Uniqueness vs T-001 `ember line`: different motif family — passes dimension (b) automatically.

## 6. Layout skeleton (ordered)
1. `nav` (sticky, blur)
2. `hero` (centered: eyebrow, h1, sub, dual CTA, generated glow visual below)
3. `features` (6-card grid: Usage, Spend, Latency, Guardrails, Audit, Alerts)
4. `pricing` (3 tiers: Starter $0 / Pro $29 / Scale custom)
5. `faq` (4 `<details>` accordion)
6. `waitlist` (dark→darker band, honest email CTA)
7. `footer`
Different block order/content family from T-001 (story/cards/visit) — passes dimension (a).

## 7. Motion policy
Fade-up reveals (gated behind `html.js`), hover lifts on cards, accordion `<details>` native. `prefers-reduced-motion` → all disabled. No parallax.

## 8. Image DNA (Seedream prompt fragments)
Base: "deep near-black navy background, soft violet (#7C5CFF) glow, abstract data streams and pulse rings, subtle grid, premium tech editorial, no text, no watermark". Slots: hero backdrop (wide), concentric signal rings (feature visual). Logo/mark: **authored as inline SVG** (geometric pulse-ring) — recorded deviation: geometric marks are sharper as vectors than as generations; skip the seedream-logo + remove-bg loop for this entry.

## 9. Accessibility decisions
Semantic landmarks, one h1, alt text, `<details>` FAQ is keyboard-native, focus-visible rings (violet), contrast per §3, reduced-motion honored, `<html lang="en">`.

## 10. Uniqueness statement + verdict (vs T-001 Embercraft)
Four-dimension diff vs T-001 (registry): (a) layout skeleton hero→features→pricing→faq→waitlist vs hero→story→cards→subscribe→visit — **different**; (b) signature element pulse ring vs ember line — **different**; (c) palette family navy/violet vs cream/ember — **different**; (d) image set abstract glow-tech vs warm morning photography — **different**. Verdict: **unique** (4/4 dimensions differ; zero matches on any single dimension).
