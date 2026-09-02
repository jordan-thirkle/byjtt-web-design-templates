# DESIGN-NOTES — Embercraft (T-001)

## 1. Summary + assumptions echo
One-page specialty-coffee-roaster template, warm editorial direction, free tier, English. All assumptions recorded in BRIEF.md (brand name invented, one-page archetype, no checkout).

## 2. Preset anchor
**18 Kenya Hara** (aesthetic-preset-library, 东方哲学派): emptiness, generous whitespace, tactile paper tones, restraint. Why: a craft roaster sells provenance and calm — Hara's whitespace lets the generated photography carry warmth while the layout stays quiet and editorial. Micro-blend: Müller-Brockmann-style strict grid (10/11) for structure, but palette and mood stay Hara.

## 3. Palette tokens (hex + role)
- `--paper` #FAF6F0 (bg)
- `--surface` #F1E9DE (cards, bands)
- `--ink` #2B211B (text — espresso)
- `--muted` #6B5A4E (secondary text)
- `--ember` #C25E33 (accent — decorative: hairlines, focus rings, large display accents only)
- `--ember-deep` #8A3B1F (interactive accent: buttons, links-hover)
Computed contrast (calculator-verified post-gauntlet): ink/paper **14.6:1**; muted/paper **6.1:1**; muted/surface **5.46:1**; white on ember-deep **7.16:1** (AA for all button text); ember/paper **3.9:1** — decorative use only, never body text or small labels.

## 4. Typography
Display: **Fraunces 600** — self-hosted woff2 (`assets/fonts/fraunces-600.woff2`) with Georgia fallback (verified loaded via @font-face post-gauntlet).
Body: **Inter 400/500/600** — self-hosted woff2 with system-ui fallback.
Scale: fluid clamp() — h1 clamp(2.6rem, 6vw, 4.2rem), h2 clamp(1.8rem, 3.5vw, 2.4rem), body 1.0625rem/1.7.

## 5. Signature element
**The ember line** — a 2px horizontal hairline that fades left→right from #2B211B through #C25E33 to transparent. Appears: under the hero headline, above each section heading, as footer top border, and abstracted in the favicon mark. Registered in designDNA as `ember line`.

## 6. Layout skeleton (ordered)
1. `hero` — full-bleed generated photograph, headline + subhead overlay on paper scrim, CTA pair
2. `roast-story` — 2-col: story image + editorial copy with drop stat strip
3. `menu-highlights` — 3 product cards (name, origin, tasting notes, price)
4. `visit` — hours + address + map placeholder note
5. `contact/footer` — email link, ember-line top border, license/copyright line

## 7. Motion policy
IntersectionObserver fade-up (opacity + 12px translate, 500ms ease-out, staggered ≤3 items). `prefers-reduced-motion: reduce` → animations disabled, content fully visible. No parallax, no autoplay.

## 8. Image DNA (Seedream prompt fragments)
Base: "warm editorial photograph, soft morning window light, film grain, cream and burnt-orange palette, specialty coffee roastery, shallow depth of field, no text, no watermark". Subject slots: roastery bar at dawn (hero); hands over fresh beans (story); kraft bags on wooden shelf (product); cup on counter (card); flat logo mark burnt-orange on solid cream (logo — generated separately, then remove-bg).

## 9. Accessibility decisions
Semantic landmarks (header/main/section/footer), one h1, alt text on all photos, skip link, visible focus rings (2px ember outline offset 2), contrast per §3, keyboard-reachable nav + cards, reduced-motion honored, `<html lang="en">`.

## 10. Uniqueness statement
Registry is empty at design time (first entry) — direction sets the baseline DNA. Distinctive by construction: Hara-anchored whitespace rhythm + ember-line signature + warm editorial photography set; future entries must differ per Phase 5 rules.
