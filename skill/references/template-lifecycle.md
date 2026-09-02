# Template Lifecycle — Full Procedure

Phases 0 runs once; Phases 1–8 run per template; Phases 9–10 are standing obligations. Every phase ends in a gate; never advance past a failed gate. Slug/ID rules, path maps, and versioning definitions live in references/catalog-and-metadata.md.

## Contents

- [Phase 0 — Marketplace Bootstrap](#phase-0--marketplace-bootstrap-once)
- [Phase 1 — Intake](#phase-1--intake)
- [Phase 2 — Design Direction](#phase-2--design-direction)
- [Phase 3 — Asset Generation](#phase-3--asset-generation)
- [Phase 4 — Build](#phase-4--build)
- [Phase 5 — QA + Uniqueness Gates](#phase-5--qa--uniqueness-gates)
- [Phase 6 — Packaging & Manifest](#phase-6--packaging--manifest)
- [Phase 7 — Catalog & Listing Sync](#phase-7--catalog--listing-sync)
- [Phase 8 — Deployment Handoff](#phase-8--deployment-handoff)
- [Phase 9 — Agent-Consumption Contract](#phase-9--agent-consumption-contract-standing)
- [Phase 10 — Maintenance & Versioning](#phase-10--maintenance--versioning)
- [DESIGN-NOTES.md required contents](#design-notesmd-required-contents)

## Phase 0 — Marketplace Bootstrap (once)

**Purpose:** Stand up the marketplace skeleton (human pages + machine catalogs) and the workspace registry.
**Skip rule:** if `byjtt-templates/registry.json` exists, skip to Phase 1 — never rebuild over live state.

Actions:
1. Call `website_delivery_start`. Use its returned project identity exactly (project id, folder name, entry file, project folder, projects.json path) — never rename or pick a different folder. `deliveryMode=create` means a brand-new site; `deliveryMode=update` means an existing ByJTT site — preserve its established content language and structure. If the returned keys are missing or unexpected, re-call `website_delivery_start`; if the session does not carry the managed-website protocol, follow the `fc-nginx-website` skill for hosting rules.
2. Build the static skeleton with file tools: `index.html` (positioning hero, featured/newest strip, tier explainer), `templates.html` (catalog grid with an empty state), `templates/_detail-pattern.html` (detail-page pattern stub — per-template detail pages are first generated at Phase 7), `licensing.html` (tier rights + external-purchase disclosure), `about.html`, `catalog.json`, `manifests/` (empty), `assets/shared/` (base CSS, marketplace logo/favicon), `/.well-known/ai-catalog.json`.
3. Create `byjtt-templates/registry.json` per the schema in references/catalog-and-metadata.md.
4. Link catalog + licensing from every page footer. Follow the managed-website protocol current in the session for delivery mechanics; write `projects.json` only as the last step of a deployment (Phase 8), never during bootstrap scaffolding.

Failure: `website_delivery_start` fails → retry once; still failing → build the skeleton under `byjtt-templates/site-staging/` instead, set `deployment.state = "pending"` with `projectId`/`folderName`/`projectsJsonPath` left null, and re-attempt bootstrap on a later run before Phase 7/8. JSON validation (`exec`: `python3 -m json.tool`) → fix and re-validate.

**Gate:** all five human pages + `catalog.json` + `/.well-known/ai-catalog.json` exist and parse; registry exists; footers link catalog + licensing; hosting contract respected.

## Phase 1 — Intake

**Purpose:** Convert the commissioning message into a deterministic build spec. Never interrogate the user; never ask clarifying questions.

Actions:
1. Extract: subject/industry, audience, tone, archetype (landing / portfolio / restaurant / SaaS / event / docs / blog …), explicit constraints (colors, fonts, named sections), tier hint, language.
2. Fill every missing dimension with a documented default (missing tone → "confident, modern"; missing archetype → infer from subject; missing sections → archetype default). Record each with the word ASSUMED.
3. Provisionally assign a unique slug (conventions in references/catalog-and-metadata.md) and write `byjtt-templates/templates/<slug>/BRIEF.md`.

`BRIEF.md` required contents: subject, audience, tone, language, archetype, section list, explicit constraints, tier hint (default free until a purchase link is configured), the full ASSUMED list, and the provisional slug.

Failure: empty or contradictory brief → most conservative defaults for the inferred subject, all flagged ASSUMED; contradictions → last-mentioned wins, noted.

**Gate:** `BRIEF.md` exists with language + archetype resolved and zero open questions.

## Phase 2 — Design Direction

**Purpose:** Lock a unique, coherent design DNA before any pixels exist.

Actions:
1. Read `/Users/jordanthirkle/.openclaw-autoclaw/skills/aesthetic-preset-library/SKILL.md`; select one preset as anchor (or a justified two-preset blend across different schools) matched to subject and tone.
2. Scan the registry's existing `designDNA` summaries; choose a direction that differs (different preset, or a mutated signature element / palette family if the preset repeats).
3. Define: palette tokens (hex + role: bg/surface/text/accent ×2), type pairing + scale, ordered layout skeleton, motion policy incl. `prefers-reduced-motion`, and exactly one **signature element** (a memorable motif reused across hero, sections, favicon).
4. Write the image DNA — reusable Seedream prompt fragments (style words, palette words, lighting, subject rules) — into the notes.
5. Write `byjtt-templates/templates/<slug>/DESIGN-NOTES.md` (required contents at the end of this file).

Failure: skill file missing → author direction from BRIEF alone and note it. Direction collides with an existing entry → force a different preset or mutate the signature element.

**Gate:** DESIGN-NOTES.md contains palette hexes, type stack, named signature element, layout skeleton, and a written uniqueness statement citing why it differs from every registry entry.

## Phase 3 — Asset Generation

**Purpose:** Produce the full visual asset set from the design DNA with cross-image consistency.

Canonical asset checklist (all items required unless noted): `hero.png`, `card.png`, `og.png` (exactly 1200×630), `favicon.png` (transparent), `logo.png`, and 3–6 numbered gallery screenshots named `01_hero.png`, `02_…`, `03_…` (numbered-gallery convention).

Actions:
1. Read `/Users/jordanthirkle/.openclaw-autoclaw/skills/autoglm-generate-image-seedream/SKILL.md`. Compose every prompt from the image DNA fragments (palette + style + signature motif) so the set reads as one art direction. Mood, not layout; short prompts; generate 3–5 variants for the hero and pick the best.
2. Generate the hero first (text→image: `generate-image-seedream.py "<prompt>"`). For each later image (gallery set + card), pass the hero as reference via image-to-image (`generate-image-seedream.py "<query>" "<public hero URL>"`; upload the local hero first with the skill's `upload-mix.py` and use the returned OSS URL).
3. Generate the logo/mark on a flat solid backdrop, then read `/Users/jordanthirkle/.openclaw-autoclaw/skills/autoglm-remove-bg/SKILL.md` and run its procedure (including its mandatory autoglm-image-recognition quality check) for transparent `favicon.png` / `logo.png`. Never prompt the generator for "transparent background".
4. Produce `og.png` at exactly 1200×630 (generate natively or crop/resize via `exec` with `sips`/Pillow; verify with `sips -g pixelWidth -g pixelHeight`).
5. Save everything under `byjtt-templates/templates/<slug>/assets/` and compress before any site-root use (host caps: ≤5,000 files, ≤100 MB source, ≤50 MB upload body).

Failure: Seedream rejects or mangles a prompt → simplify (keep palette + style anchors), retry ≤3, then drop that asset and note it. remove-bg fails → regenerate the mark on an explicit flat backdrop, strip again. OG size wrong → resize, re-verify.

**Gate:** every checklist item exists; OG verified 1200×630; favicon verified transparent; spot-check (image view or autoglm-image-recognition) that palette + signature element are present and the set is consistent.

## Phase 4 — Build

**Purpose:** Implement the template site: real content, responsive, accessible, stateful.

Actions — build under `byjtt-templates/templates/<slug>/site/` with `write`/`apply_patch`:
1. `index.html` + `css/styles.css` + `js/main.js`; copy chosen assets into `site/assets/`. Self-contained: no build step, no required CDN (optional webfonts must have system-font fallbacks), no server runtime, no secrets, no `node_modules`.
2. Real copy in the commissioning language — product-flavored, specific, zero lorem ipsum; title/meta description in the same language.
3. `<html lang>` = actual content language; semantic landmarks; alt text on every image; contrast ≥ 4.5:1; visible focus styles; skip link; labeled forms with inline validation UI.
4. Responsive at 375 / 768 / 1440; interactive states: hover, focus, active, disabled, mobile nav toggle, accordion/tabs as the skeleton requires; JS enhancements degrade to CSS-only equivalents.
5. Meta: title, description, OG tags pointing at `assets/og.png`, twitter card, favicon link.

Failure: JS feature breaks → ship the CSS-only fallback. Overflow at a breakpoint → fix layout, re-check. Any secret temptation → static placeholder copy instead.

**Gate (static audit via `exec`):** all internal links/images resolve to existing files; no `node_modules`/`.env`/secret-looking strings; `lang` matches language; every `<img>` has alt; file set within host caps; no lorem ipsum. Additional hard lints: every font named in the design DNA has a loading mechanism (`@font-face`/`<link>`) in the shipped head; no inline layout styles (`grid-template-columns` and friends) — media queries must win; scroll/reveal animations hide content only under a JS-added `html.js` class (no-JS ⇒ everything visible); images carry `width`/`height`.

## Phase 5 — QA + Uniqueness Gates

**Purpose:** Prove the template is defect-free and genuinely distinct.

Actions:
1. Tick `byjtt-templates/templates/<slug>/QA-CHECKLIST.md`: links resolve; meta/OG present; all three widths verified (resize a browser preview or capture screenshots at 375/768/1440 and inspect); states exercised; contrast spot-check; `prefers-reduced-motion` respected; keyboard tab order; favicon/OG paths correct; language consistency; host caps. QA ticks must cite machine checks (computed contrast ratios per token pair including white-on-accent buttons; grep-proof state rules like `:disabled`; square favicon; no unreferenced assets before zipping) — narrative passes do not count. Full-bleed hero over a generated image: scrim must guarantee ≥0.75 background coverage at the headline zone, checked against the real asset.
2. Uniqueness diff against every **non-retired** registry entry on 4 dimensions: (a) layout skeleton / block order, (b) signature element, (c) palette (hue distance + role mapping), (d) image-set composition (subject + style). **Fail** if any single existing entry matches on ≥2 dimensions; identical signature element = automatic fail.
3. Record the per-entry comparison and verdict in DESIGN-NOTES.md ("Uniqueness verdict").

Failure: uniqueness fail → return to Phase 2 with a forced mutation (different preset, or new signature element / palette family), regenerate affected assets, rebuild affected sections, re-run gates. Hard stop after 2 full uniqueness retries → change archetype defaults in BRIEF.md (documented) and restart direction.

**Gate:** QA checklist 100% pass AND uniqueness verdict = unique. No packaging before this gate.

## Phase 6 — Packaging & Manifest

**Purpose:** Turn the passed build into a first-class, machine-readable catalog unit.

Actions:
1. Finalize the slug (globally unique, never reused). Assign the `T-###` ID by incrementing `registry.idCounter`.
2. Write `byjtt-templates/templates/<slug>/manifest.json` — required fields listed in references/catalog-and-metadata.md.
3. Honest paid tier: `purchaseUrl` set → detail page links out; `purchaseUrl` null while `tier:"paid"` → `purchaseState:"coming-soon"` and the UI shows a disabled "Purchase coming soon" state. No fake checkout, no payment JS. Paid manifests set `license` to exactly `ByJTT Commercial License` or `ByJTT Extended License` (ladder in references/listing-and-licensing.md).
4. Validate via `exec`: JSON parse, required-field check, semver regex.

Failure: slug collision → append a numeric suffix and record it in the registry; never silently rename. Missing field → backfill from BRIEF/DESIGN-NOTES; unknown value → conservative default + note.

**Gate:** manifest parses, all required fields present, semver valid, slug + ID unique vs registry, tier/purchase coherent (paid ⇒ purchaseUrl or coming-soon). Registry entry appended with `status:"staged"`, `releaseState:"unreleased"`.

## Phase 7 — Catalog & Listing Sync

**Purpose:** Publish the template to every human + machine surface, generated in one direction: registry ⇒ site.

Actions:
1. Copy into the marketplace project folder (target = the project folder from `website_delivery_start`; if it is not yet allocated, stage under `byjtt-templates/site-staging/` and copy over once it is):
   - preview assets → `assets/templates/<slug>/` (card, numbered gallery screenshots, og);
   - the template's built `site/` output → `previews/<slug>/` (this becomes the template's live-preview path after deployment);
   - for the free tier: a downloadable `.zip` of the template site (workspace-built content artifact, not an upload step) → `assets/templates/<slug>/downloads/<slug>-v<version>.zip`.
2. Rebuild site `catalog.json` **from the registry** (never hand-edit): `schemaVersion`, `generatedAt`, `count`, full `entries[]` including `agentHints`, `detailPage`, `manifestUrl:"./manifests/<slug>.json"`, `thumbnail`.
3. Copy the manifest → site `manifests/<slug>.json`; rebuild `/.well-known/ai-catalog.json` from the registry (mapping in references/catalog-and-metadata.md).
4. Generate the detail page `templates/<slug>.html` from the manifest: hero, preview state (live URL only once host-reported — before that show "preview pending deployment"), gallery, feature list, palette/type strip, signature-element callout, tier + purchase/download state (honest: free ⇒ download link; paid ⇒ purchase link or coming-soon), license link, agent-notes box.
5. Insert/update the catalog card in `templates.html` and the newest strip on `index.html` (image-led thumbnail, name, tags, tier badge, detail link).
6. Update the registry entry: `status:"listed"`, `updatedAt`.

Failure: any mismatch (count, fields, dead link) → regenerate `catalog.json`, ai-catalog.json, and touched pages entirely from the registry; registry wins. Partial page-edit failure → rebuild that page from the manifest rather than patching.

**Gate (sync invariants):** `catalog.json.count == entries[] length == number of non-retired registry templates`; every field present in a catalog entry equals the corresponding manifest field (license string exact-match against the ladder in references/listing-and-licensing.md); every entry has an existing detail page + manifest file; thumbnail, every screenshot, and (free tier) the download zip resolve to existing files under the marketplace project folder; path-lint every `manifest.files[]` and `assets.*` value against the filesystem; ai-catalog.json lists every listed template; every card links to a real page; footer links intact.

## Phase 8 — Deployment Handoff

**Purpose:** Ship the updated marketplace through the host's real deployment; record only the host-reported result.

Actions:
1. Final pre-flight via `exec`: host caps, `index.html` present at the site root, no node_modules/secrets/runtime deps, both catalogs valid.
2. Ensure all site files are in the project folder from the `website_delivery_start` contract (entry `index.html`, relative asset paths, only the entry subtree ships).
3. Update `projects.json` at the returned projects.json path as the **single last action**: read it first, keep the top-level JSON array, update/append only this project's item (preserve `id`/`createdAt` and all other projects; include the `deployment` object with `"provider":"function-compute","environment":"nginx","autoPreview":true`), and never touch any `deploymentResult` field. Then read it back and validate: parses, still an array, target id present exactly once, other projects intact.
4. Obtain the host-reported result without inventing anything: re-read `projectsJsonPath` a bounded number of times for the host-written `deploymentResult`; if it does not appear, ask the user to confirm the preview URL shown by the host UI. Once confirmed, record into the registry: `deployment.state = "active"`, `deployment.lastUrl`, `deployedAt`, and per-template `preview.liveUrl = <host-reported marketplace base>/previews/<slug>/`; set template `status:"deployed"`, `releaseState:"deployed-preview"`.
5. Formal public release: the user clicks publish in the host UI. On user confirmation (or the host UI showing the published URL), set the template's `releaseState:"published"` at the next registry write. Never self-declare "publicly released".

Failure: host reports failure → keep file state, surface the exact host error, do not blind-retry; prune oversize assets and re-run pre-flight if caps caused it. `projects.json` written but no host result → template stays `status:"listed"`, `releaseState:"unreleased"` until a host-reported result exists.

**Gate:** `projects.json` updated exactly once per release, after all content files; host-confirmed result + real URL recorded.

## Phase 9 — Agent-Consumption Contract (standing)

Maintained at Phases 0/6/7 — full contract in references/catalog-and-metadata.md. Invariants: `catalog.json` at the site root is permanent; `schemaVersion` changes are additive within a version; `id` and `slug` are immutable; every entry carries `detailPage`, `manifestUrl`, `thumbnail`, `updatedAt`; URLs are site-relative in `catalog.json` and root-absolute in `/.well-known/ai-catalog.json`; `agentHints` are written as conditions, not adjectives.

**Gate (checked at every sync):** a fresh read of `catalog.json` alone suffices to (a) enumerate templates, (b) filter by archetype/tier/language, (c) judge visual distinctness from designDNA, (d) obtain the manifest URL.

## Phase 10 — Maintenance & Versioning

Actions:
1. Bump the template's semver per the PATCH/MINOR/MAJOR definitions in references/catalog-and-metadata.md.
2. Update `manifest.version` / `updatedAt`, prepend a `changelog[]` entry, append to `changelog.md`.
3. Re-run Phase 5 gates for every MINOR/MAJOR (PATCH keeps QA, skips uniqueness).
4. Re-run Phase 7 sync, then Phase 8 deployment (projects.json last, again).
5. Retirements: never reuse slug/ID; remove from catalog.json + ai-catalog.json; keep the detail page as a `status:"retired"` notice; note in the global changelog.

Failure: bump forgotten → Phase 7 invariant fails on version mismatch; fix before deploy. Uniqueness now failing because of a *newer* template → mark the older manifest `supersededBy` and offer a MAJOR refresh.

**Gate:** every bump has a changelog entry; MINOR/MAJOR re-passed both gates; registry ↔ catalogs ↔ pages agree post-deploy.

## DESIGN-NOTES.md required contents

1. Brief summary + BRIEF assumptions echo. 2. Preset anchor + why chosen. 3. Palette tokens (hex + role). 4. Typography pairing + scale. 5. Signature element + where it appears. 6. Ordered layout skeleton. 7. Motion + reduced-motion policy. 8. Image DNA (reusable Seedream prompt fragments). 9. Accessibility decisions. 10. Uniqueness statement + per-entry diff verdict.
