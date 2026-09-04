<!-- ByJTT prompt kit: signal v1.0 · brand-customize-prompt.md · kit version 1 · 2026-09-04.
     Delta prompt: assumes build-prompt.md has already run. Do not stack on top of it. -->

# Brand-customize the Signal build (delta)

The template is already built in this workspace. Apply a brand pass without re-downloading.
Same rules: plain language, never delete what exists, never quietly downgrade a request,
honest one-line answers when something fails.

## Inputs (fill in or ask me)
- Product name: {{BRAND_NAME}}
- One-line pitch: {{PITCH}}
- Accent color (hex, optional — default is the template violet #7C5CFF): {{ACCENT}}
- Domain (optional): {{DOMAIN}}

## Steps
1. Rewrite the visible copy in the new brand's voice while keeping the instrument-panel tone
   (short, precise, technical-but-human). Keep every section: hero, features, pricing, FAQ,
   waitlist, footer.
2. If a new accent was given, change only the CSS custom properties `--accent` and
   `--accent-deep` (and the derived glow shadows). This design runs on exactly one accent —
   do not introduce a second.
3. Update the contact email, pricing tiers if I provided real ones, and the footer domain.
4. Re-verify: three widths (375/768/1440), fonts and images load, contrast on the dark
   background still ≥ 4.5:1 for body text, no placeholder text remains.
5. Show me the preview URL and a one-line change summary. Then wait — for publishing, use
   `publish-prompt.md`.
