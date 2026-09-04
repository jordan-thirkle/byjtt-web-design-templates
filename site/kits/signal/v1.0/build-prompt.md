<!-- ByJTT prompt kit: signal v1.0 · build-prompt.md · kit version 1 · 2026-09-04.
     Copy this whole file into your coding agent. Placeholders in [BRACKETS] are yours to fill
     (or leave them — your agent will ask). Your agent works on a copy in its own workspace. -->

# Build a website from the "Signal" template

You are building a finished website for me from a professionally designed template.
I may not be a programmer: use plain language, give short status updates as you go,
and never end by telling me to run commands myself — do the work, then show me the result.

## Safety rails
- Never delete or overwrite anything already in your workspace unless I ask.
- Never quietly downgrade a request. If something can't be done, stop and say so in one line.
- This template is a dark, single-accent SaaS landing page. Don't add extra accent colors,
  warm photography, or a backend unless I explicitly ask.
- Never add a fake checkout, fake signup endpoint, or placeholder text — the template ships
  with honest states; keep them honest.

## Inputs (fill these in; ask me for any I left blank)
- Product name: [YOUR-PRODUCT]
- One-line pitch: [YOUR-PITCH]
- Contact email: [YOUR-EMAIL]
- Pricing tiers (optional — defaults are template placeholders): [YOUR-TIERS]
- Domain (if you have one): [YOUR-DOMAIN]

## Steps
1. Download the template package:
   `curl -L -o signal.zip https://byjtt-templates.pages.dev/assets/templates/signal/downloads/signal-v1.0.0.zip`
   and unzip it into a folder called `site`.
2. Read `manifest.json` inside the package first — it is the binding contract: the file
   inventory, design tokens (palette #0A0E13 / #7C5CFF violet, Space Grotesk + Inter,
   pulse-ring signature), page structure (hero, features, pricing, FAQ, waitlist), and the
   license summary. Personalize; don't redesign.
3. Replace every `[YOUR-…]` placeholder in the copy with my inputs above and log each
   replacement in a checklist you show me at the end. Pricing tiers are template
   placeholders — swap in my real tiers or keep them clearly labeled as examples.
4. Serve locally (`python3 -m http.server 8080` inside `site`) and verify before showing me:
   renders at 375 / 768 / 1440, every image and font loads, FAQ accordion opens with the
   keyboard, no placeholder text anywhere.
5. Show me the local preview URL and the checklist. Then wait — iterate with
   `iterate-prompt.md`, or continue to `publish-prompt.md`.

## License note (keep this in the footer)
ByJTT Free Template License: personal, non-commercial end products; attribution appreciated,
not required. Commercial use needs the paid license — see
https://byjtt-templates.pages.dev/licensing.html
