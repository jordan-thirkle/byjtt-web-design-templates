# ByJTT Web Design Templates for Agents / AI

A design studio on AI rails. A reusable agent skill turns a one-line brief into a **finished, unique, one-shot website design** — generated imagery, real copy, responsive and accessible — then publishes it to a static marketplace that **humans browse and AI agents read as data**.

- Live marketplace: https://byjtt-templates.pages.dev (Cloudflare Pages, canonical) · custom domain: https://templates.byjtt.com · mirror: https://jordan-thirkle.github.io/byjtt-web-design-templates
- Machine catalog: [`site/catalog.json`](site/catalog.json) · agent discovery: [`site/.well-known/ai-catalog.json`](site/.well-known/ai-catalog.json)

## Repo map

| Path | What it is |
|---|---|
| `skill/` | The reusable studio skill (`SKILL.md` + `references/`) that runs the whole lifecycle |
| `site/` | The marketplace itself — the static site deployed to Cloudflare Pages |
| `templates/embercraft/` | Template T-001 workbench: brief, design notes, QA checklist, manifest, changelog, generated assets, and the template site |
| `templates/embercraft/site/` | The deployable template output (what buyers get in the zip) |
| `docs/` | Gauntlet reports and lessons fed back into the skill |
| `registry.json` | Workspace source of truth: every template, IDs, deployment history |

## The rules the studio never breaks

1. **One shot** — the studio never interrogates the user; it ships with documented assumptions.
2. **Unique every time** — every template must differ from all catalog entries on layout skeleton, signature element, palette, and image set; identical signature element = automatic fail.
3. **Honest commerce** — static hosting can't process payments; paid tiers use price display + external purchase links, never a fake checkout.
4. **Host-reported truth only** — URLs are recorded from deployment responses, never invented.
5. **Everything ships finished** — no lorem ipsum, no placeholders, no half-states.

## Quickstart

**Use a template:** open [`site/templates.html`](site/templates.html), pick one, download the zip (free tier). The zip is the complete site — open `index.html` in a browser or drop the folder on any static host.

**Browse as an agent:** fetch `site/catalog.json`, filter entries by `archetype` / `language` / `tier`, judge visual fit from `designDNA`, then fetch `manifests/<slug>.json` for the full file list and license.

**Run the studio skill:** install `skill/` into your agent's skills directory (e.g. `~/.openclaw-autoclaw/skills/byjtt-web-design-templates/`), then commission a template: *"Create a free-tier landing-page template for X."*

## Marketplace deployment

The marketplace is a static directory (`site/`) currently live on **GitHub Pages** (gh-pages branch). To move to Cloudflare Pages: create an API token with Cloudflare Pages:Edit, then `wrangler pages deploy site --project-name byjtt-templates` — or ask the agent to deploy via API. Rebuild checklist before any deploy: all internal links resolve, `catalog.json` and `manifests/` are regenerated from `registry.json` (never hand-edited), the `.well-known/ai-catalog.json` copy is root-absolute, and `projects.json`-style triggers are not used here.

## Licenses

- **Repo & skill:** MIT (see [LICENSE](LICENSE)).
- **Templates:** each template carries its own license, listed in its manifest and on the [licensing page](site/licensing.html) — Free Template License for free templates; Commercial / Extended licenses apply to paid templates.

## Status

**v1.0.0 "First Light"** — feature-complete marketplace edition: studio skill, two gauntlet-tested templates (T-001 Embercraft v1.1.0, T-002 Signal v1.0.0), versioned agent prompt kits, human + machine catalogs, three hosting surfaces (Cloudflare Pages canonical, templates.byjtt.com custom domain, GitHub Pages mirror), and the full docs set. Post-1.0 roadmap: v2 accounts (Worker + D1 + OAuth, see [`docs/v2-accounts-design.md`](docs/v2-accounts-design.md)) and the improvement backlog in [`docs/lessons-learned.md`](docs/lessons-learned.md).
