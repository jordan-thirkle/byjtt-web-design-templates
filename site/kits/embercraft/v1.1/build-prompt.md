<!-- ByJTT prompt kit: embercraft v1.1 · build-prompt.md · kit version 1 · 2026-09-02.
     Copy this whole file into your coding agent. Placeholders in [BRACKETS] are yours to fill
     (or just leave them and let your agent ask you). Do not edit the file itself — your agent
     works on a copy in its own workspace. -->

# Build a website from the "Embercraft" template

You are building a finished website for me from a professionally designed template.
I may not be a programmer: use plain language, give short status updates as you go,
and never end by telling me to run commands myself — do the work, then show me the result.

## Safety rails
- Never delete or overwrite anything already in your workspace unless I ask.
- Never quietly downgrade a request. If something can't be done, stop and say so in one line.
- Never add a fake checkout, fake newsletter endpoint, or placeholder text — the template
  ships with honest states; keep them honest.
- The template is static HTML/CSS/JS. Don't add a backend unless I ask (the publish prompt
  will refuse to deploy a backend — tell me early if I ask for one).

## Inputs (fill these in; ask me for any I left blank)
- Brand name: [YOUR-BRAND]
- Tagline: [YOUR-TAGLINE]
- City / address lines: [YOUR-ADDRESS]
- Contact email: [YOUR-EMAIL]
- Domain (if you have one): [YOUR-DOMAIN]

## Steps
1. Download the template package:
   `curl -L -o embercraft.zip https://byjtt-templates.pages.dev/assets/templates/embercraft/downloads/embercraft-v1.1.0.zip`
   and unzip it — a folder named `embercraft/` will appear; that folder is your working directory.
2. The package also contains `manifest.json` (the binding spec), `LICENSE.txt`, and a `README.md`. Read `manifest.json` first. It is the binding contract: the file
   inventory, design tokens (palette, fonts, signature element), page structure, and the
   license summary. Follow it — don't redesign the template, personalize it.
3. Replace every `[YOUR-…]` placeholder in the copy with my inputs above, and log each
   replacement in a short checklist you show me at the end.
4. Serve it locally (e.g. `python3 -m http.server 8080` inside `site`) and verify before
   showing me: it renders at phone width (375px), tablet (768px) and desktop (1440px);
   every image loads; no "lorem" text anywhere; the contact links work.
5. Show me the local preview URL and the replacement checklist. Then wait for my feedback
   — iterate with `iterate-prompt.md` if I want changes, or continue to `publish-prompt.md`.

## License note (keep this in the footer)
This template is licensed under the ByJTT Free Template License: personal, non-commercial
end products, attribution appreciated but not required. Commercial use needs the paid
license — see https://byjtt-templates.pages.dev/licensing.html
