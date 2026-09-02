<!-- ByJTT prompt kit: embercraft v1.1 · publish-prompt.md · kit version 1 · 2026-09-02.
     Use when the build is done and I want it live. -->

# Publish the Embercraft build (one prompt)

You are publishing my finished static website. Be honest about what publishing means:
this template is static-only. If I've asked you to add a backend (database, logins, server
code), STOP now and tell me in one line that publishing needs a different plan — do not
deploy something that won't work.

## Safety rails
- Before touching anything: put the project under git (`git init` if needed) and commit the
  current state. Publishing must never destroy my only copy.
- The sign-in step is MINE, not yours: when login is needed, tell me to run the login
  command in a browser and WAIT for me to say it's done. Never ask me to paste passwords,
  tokens, or cookies to you.
- Never deploy from a folder with missing files; run the checks below first.

## Steps (Cloudflare Pages — free tier works)
1. Preflight: confirm `site/index.html` exists, all internal links resolve, and there are no
   secret-looking strings in the files. Tell me the result in one line.
2. Check that Node.js is installed (`node --version`, 18+ is fine). If not, tell me to
   install it and wait.
3. Tell me to run: `npx wrangler login` — a browser tab opens; I approve it; wait for me.
4. Deploy: `npx wrangler pages deploy . --project-name <a-name-I-choose>` from the site
   folder. Report the exact live URL it prints.
5. Optional if I gave a domain: add the custom domain in the Cloudflare dashboard
   (Pages project → Custom domains) — the dashboard clicks are mine; you verify afterwards
   with a curl status check.

## Not using Cloudflare?
Say the word and use the fallback instead: GitHub Pages (push the site folder to a
`gh-pages` branch and enable Pages in the repo settings) or Netlify Drop (drag the folder
at app.netlify.com/drop). Same honesty rules.

## After it's live
- Confirm the URL loads (curl status 200) and tell me it's public.
- Remind me to keep the license footer line (ByJTT Free Template License: personal,
  non-commercial; commercial use needs the paid license — see the marketplace licensing page).
