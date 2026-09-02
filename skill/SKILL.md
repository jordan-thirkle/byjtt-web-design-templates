---
name: byjtt-web-design-templates
description: Produce perfect, unique, one-shot website designs — AI-generated imagery, personalized design systems, and the full design/build/QA lifecycle — then publish them as catalog entries on the ByJTT Web Design Templates for Agents / AI marketplace, a static template-selection library humans browse and AI agents read via a machine-readable catalog, with free and paid tiers. Use when the user asks to create a new ByJTT template design, publish, update, or retire a template on the ByJTT marketplace, or bootstrap, rebuild, or maintain the ByJTT marketplace site itself. Do not use for bespoke multi-page client applications (defer to website-builder).
---

# ByJTT Web Design Templates — Design Studio & Publisher

One skill, two jobs: (1) run a one-shot design studio that turns a brief into a finished, unique website design; (2) run the marketplace that stores, showcases, and sells those designs.

- **Marketplace**: "ByJTT Web Design Templates for Agents / AI" — a static site where humans browse a visual catalog and AI agents pick templates from machine-readable files.
- **Everything ships finished**: no placeholders, no lorem ipsum, no half-built pages.

## Non-negotiables

1. **One shot.** Never interrogate the user. Fill every gap with a documented default, mark it ASSUMED in BRIEF.md, and ship.
2. **Unique every time.** A new template must differ from every existing entry on layout skeleton, signature element, palette, and image set (diff rules: references/template-lifecycle.md, Phase 5).
3. **Registry is the single source of truth.** `byjtt-templates/registry.json` in the agent workspace beats any site file. Site pages and catalogs are generated views — regenerate them from the registry, never hand-patch.
4. **Honest commerce.** Static hosting cannot process payments. Paid tiers show price plus a user-configured external purchase link (e.g., Stripe Payment Link, Gumroad) or a visible "purchase coming soon" state. Never render a fake checkout, payment form, or confirmation.
5. **Host-reported truth only.** Deployment URLs come from the host app after `projects.json` is updated. Never guess, invent, or promise URLs. Formal public release happens only when the user clicks publish in the host UI.
6. **Content language** = the language of the request that commissioned the template or marketplace text. Set `<html lang>` and all user-visible strings accordingly.
7. **Static-only hosting.** Entry `index.html` (relative path, inside the project folder), relative asset paths, no server runtime, no secrets, no `node_modules`. Respect host caps: ≤5,000 files, ≤100 MB source, ≤50 MB upload body — compress generated images before they enter the site root.

## Architecture at a glance

| Surface | Location | Role |
|---|---|---|
| Registry (source of truth) | `byjtt-templates/registry.json` (agent workspace) | Every template, ID counter, deployment history |
| Template workbenches | `byjtt-templates/templates/<slug>/` | BRIEF.md, DESIGN-NOTES.md, QA-CHECKLIST.md, manifest.json, changelog.md, assets/, site/ |
| Marketplace site | project folder allocated by `website_delivery_start` | Human pages + generated catalogs |
| Human pages | `index.html`, `templates.html`, `templates/<slug>.html`, `licensing.html`, `about.html` | Browse, detail, license terms |
| Machine catalogs | site-root `catalog.json`, `manifests/<slug>.json`, `/.well-known/ai-catalog.json` | Agent discovery and deep selection |

## Workflow

Read **references/template-lifecycle.md** before running any phase — it holds the full procedure, failure handling, and gates. Phase 0 runs once; Phases 1–8 run per template; Phases 9–10 are standing obligations.

| Phase | Purpose | Gate (must pass before the next phase) |
|---|---|---|
| 0 Bootstrap (once) | Stand up the marketplace skeleton + workspace registry via `website_delivery_start` | All pages and catalogs exist and parse; registry written |
| 1 Intake | Brief → `BRIEF.md` with documented assumptions | Zero open questions; nothing asked of the user |
| 2 Design direction | Aesthetic anchor via aesthetic-preset-library; palette, type, one signature element → `DESIGN-NOTES.md` | Written uniqueness statement vs registry |
| 3 Assets | Generate a consistent image set (autoglm-generate-image-seedream); favicon/logo via autoglm-remove-bg | All assets exist; OG is 1200×630; favicon verified transparent |
| 4 Build | Self-contained static site: real copy, responsive, accessible, stateful | Static audit passes (links, alt, lang, caps, no secrets) |
| 5 QA + uniqueness | QA checklist + 4-dimension uniqueness diff vs registry | 100% pass, or forced-mutation loop |
| 6 Package | `manifest.json` + `T-###` ID + semver | Manifest validates; slug and ID unique |
| 7 Listing sync | Regenerate `catalog.json`, `/.well-known/ai-catalog.json`, detail page, cards from the registry | Sync invariants hold |
| 8 Deploy handoff | Update `projects.json` **last**; record host-reported result | Host-confirmed deployment recorded |
| 9–10 Standing | Agent contract + maintenance: semver bumps, changelogs, re-run gates | Checked at every sync |

## The "for Agents / AI" layer

`catalog.json` alone must let an agent enumerate every template, filter by archetype/tier/language, judge visual fit from `designDNA` without fetching HTML, and locate the manifest. Keep `/.well-known/ai-catalog.json` (AI Catalog pattern) in sync at every listing. Schemas, stability guarantees, and the canonical selection algorithm: references/catalog-and-metadata.md.

## Free vs paid

Free tier = full quality, no watermarks, no strings — it is the funnel. Paid tier = per-item price display plus an external purchase link the user configures, or an honest "purchase coming soon" state. License ladder and plain-English terms: references/listing-and-licensing.md. Pricing decisions belong to the user; never invent or quote market prices.

## Guardrails

- Never fabricate URLs, prices, licenses, or deployment success.
- The machine contract describes what actually ships: fonts, license strings, and asset paths are linted against the build, never assumed.
- No secrets, `.env` files, tokens, or API keys anywhere under the site root; no `node_modules`, no stray source files that should not ship.
- Slugs and `T-###` IDs are immutable and never reused, even after retirement.
- Every version bump gets a changelog entry; MINOR and MAJOR bumps re-pass Phase 5 gates.
- Keep the Seedream prompts for every generated image in DESIGN-NOTES.md so assets can be regenerated.
- External actions — first public release, enabling purchase links — need the user's explicit go-ahead.

## References

- **references/template-lifecycle.md** — full phase-by-phase procedure with gates. Read before Phase 0.
- **references/catalog-and-metadata.md** — registry, catalog, and manifest schemas; slug/ID rules; versioning; agent-consumption contract. Read at Phases 0, 6, 7, 10 and whenever a schema changes.
- **references/listing-and-licensing.md** — listing standards (cover, gallery, demo), free/paid tier policy, license ladder text. Read at Phases 6–7 and for any licensing question.
- **references/example-catalog-entry.json**, **references/example-manifest.json** — filled samples of both machine files.
