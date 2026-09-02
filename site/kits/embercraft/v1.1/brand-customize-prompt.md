<!-- ByJTT prompt kit: embercraft v1.1 · brand-customize-prompt.md · kit version 1 · 2026-09-02.
     Delta prompt: assumes build-prompt.md has already run and the template is built in your
     agent's workspace. Do not stack on top of build-prompt.md. -->

# Brand-customize the Embercraft build (delta)

The template is already built in this workspace. Apply a brand pass without re-downloading
anything. Same rules as before: plain language, never delete what exists, never quietly
downgrade a request, honest one-line answers when something fails.

## Inputs (fill in or ask me)
- Brand name: {{BRAND_NAME}}
- Tagline: {{TAGLINE}}
- Primary accent color (hex, optional): {{PRIMARY_COLOR}}
- Domain for the footer (optional): {{DOMAIN}}

## Steps
1. Rewrite the visible copy in the new brand's voice while keeping the template's editorial
   tone (short sentences, sensory language, no filler). Keep every section: hero, story,
   beans/offer cards, subscription cadences, visit, contact.
2. If a new accent color was given, update the CSS custom properties only — the template's
   tokens are `--ember` / `--ember-deep` for accents and buttons. Do not introduce extra
   accent colors; this design runs on exactly one.
3. Update the contact email, address lines, opening hours, and the footer domain link.
4. Keep the license footer line intact (see `licensing.html` in the package for terms).
5. Re-verify: three widths (375/768/1440), all images load, contrast still readable on the
   cream background, and no placeholder text remains anywhere.
6. Show me the updated preview URL and a one-line summary of what changed. Then wait —
   for publishing, use `publish-prompt.md`.
