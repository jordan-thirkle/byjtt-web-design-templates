# Catalog & Metadata — Schemas, Conventions, Agent Contract

## Contents

- [File inventory](#file-inventory)
- [registry.json (workspace source of truth)](#registryjson-workspace-source-of-truth)
- [catalog.json (site machine catalog)](#catalogjson-site-machine-catalog)
- [manifest.json (per-template contract)](#manifestjson-per-template-contract)
- [/.well-known/ai-catalog.json (agent discovery)](#well-knownai-catalogjson-agent-discovery)
- [Slug / ID conventions](#slug--id-conventions)
- [Path maps](#path-maps)
- [Versioning rules](#versioning-rules)
- [Canonical selection algorithm for agents](#canonical-selection-algorithm-for-agents)

## File inventory

| File | Where | Generated from | Purpose |
|---|---|---|---|
| `byjtt-templates/registry.json` | agent workspace | hand of truth | source of truth for everything |
| `catalog.json` | site root | registry (Phase 7) | one-call enumeration for agents |
| `manifests/<slug>.json` | site | template manifest (Phase 7 copy) | deep contract per template |
| `/.well-known/ai-catalog.json` | site | registry (Phase 7) | emerging agent-discovery pattern |
| `templates/<slug>.html`, `templates.html`, `index.html` | site | registry + manifest (Phase 7) | human surfaces |

Rule: the registry wins on any conflict; site files are generated views. Regenerate, never hand-patch.

## registry.json (workspace source of truth)

```json
{
  "schemaVersion": "1.0.0",
  "idCounter": 0,
  "marketplace": { "name": "ByJTT Web Design Templates for Agents / AI" },
  "deployment": {
    "projectId": null,
    "folderName": null,
    "entryFile": "index.html",
    "projectsJsonPath": null,
    "state": "pending",
    "lastUrl": null,
    "deployedAt": null
  },
  "templates": []
}
```

`deployment.projectId` / `folderName` / `projectsJsonPath` are filled from `website_delivery_start`; they stay `null` if bootstrap fell back to `byjtt-templates/site-staging/`. `deployment.state` is `pending` until the first host-confirmed deployment sets it `active`.

Each `templates[]` entry carries all manifest fields (below) plus workflow status:

| Field | Type | Notes |
|---|---|---|
| `id` | string | `T-###`, immutable, from `idCounter` |
| `slug` | string | kebab-case, immutable, never reused |
| `status` | enum | `staged` → `listed` → `deployed` (→ `retired`) |
| `releaseState` | enum | `unreleased` → `deployed-preview` → `published` (user clicks publish) |
| everything else | — | identical to `manifest.json` fields |

## catalog.json (site machine catalog)

```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "<ISO-8601>",
  "marketplace": "ByJTT Web Design Templates for Agents / AI",
  "count": 1,
  "entries": [
    {
      "id": "T-001",
      "slug": "ember-bistro",
      "name": "Ember Bistro",
      "version": "1.0.0",
      "language": "en",
      "archetype": "restaurant",
      "description": "One-paragraph, binding description: the page must work exactly as described here.",
      "tags": ["restaurant", "warm", "editorial"],
      "tier": "free",
      "price": null,
      "purchaseState": "not-applicable",
      "purchaseUrl": null,
      "license": "ByJTT Free Template License",
      "detailPage": "./templates/ember-bistro.html",
      "manifestUrl": "./manifests/ember-bistro.json",
      "thumbnail": "./assets/templates/ember-bistro/card.png",
      "preview": { "liveUrl": null, "screenshots": ["./assets/templates/ember-bistro/01_hero.png"] },
      "designDNA": {
        "palette": ["#2B1D16", "#F6EFE6", "#C96F3B"],
        "fonts": ["Fraunces", "Inter"],
        "signatureElement": "ember-glow divider",
        "layoutSkeleton": ["hero", "menu-highlights", "story", "hours", "contact"]
      },
      "agentHints": {
        "bestFor": ["restaurant or cafe one-pagers with photography-heavy heroes"],
        "avoidIf": ["dark-mode required", "multi-page navigation needed"]
      },
      "updatedAt": "<ISO-8601>"
    }
  ]
}
```

The catalog entry is a deliberate subset of the manifest; the catalog's `designDNA` is the manifest's `designDNA` minus `typeScale` and `presetAnchor`.

Invariants: `count == entries[] length == number of non-retired registry templates`; every field present in a catalog entry equals the corresponding manifest field; every entry has an existing detail page + manifest; `manifestUrl`/`detailPage`/`thumbnail` are site-relative paths that resolve to real files; `preview.liveUrl` is either null or a host-reported URL.

## manifest.json (per-template contract)

Required fields (all must be present; validate at Phase 6):

| Field | Type | Notes |
|---|---|---|
| `id` / `slug` / `name` | string | identity; immutable |
| `version` | string | semver, starts `1.0.0` after Phase 5 gates |
| `language` | string | BCP-47 of the content language |
| `archetype` | string | landing / portfolio / restaurant / SaaS / event / docs / blog / … |
| `description` | string | binding: "works as described" |
| `longDescription` | string | detail-page copy |
| `tags[]` | string[] | discovery keywords |
| `tier` | enum | `free` \| `paid` |
| `price` | object \| null | `{ "amount": 29, "currency": "USD" }` — set by the user only |
| `purchaseState` | enum | `ready` \| `coming-soon` \| `not-applicable` |
| `purchaseUrl` | string \| null | user-configured external link (Stripe Payment Link, Gumroad) |
| `license` | string | free ⇒ `ByJTT Free Template License`; paid ⇒ exactly `ByJTT Commercial License` or `ByJTT Extended License`, anchored into `licensing.html` |
| `entryFile` | string | `index.html` |
| `files[]` | array | `{ "path": "...", "bytes": 1234 }` — covers the deployable template output (`site/` contents); design working assets are inventoried under `assets` |
| `assets` | object | `{ og, favicon, card, hero, gallery[] }` |
| `designDNA` | object | palette, fonts, typeScale, signatureElement, layoutSkeleton, presetAnchor |
| `preview` | object | `{ liveUrl (host-reported or null), screenshots[] }` |
| `agentHints` | object | `bestFor[]` / `avoidIf[]` as conditions, not adjectives |
| `changelog[]` | array | `{ "version", "date", "notes" }`, newest first |
| `supersededBy` | string \| null | set on retirement/supersede |
| `createdAt` / `updatedAt` | string | ISO-8601 |

## /.well-known/ai-catalog.json (agent discovery)

Minimal mapping of the registry to the AI Catalog pattern (a static well-known manifest agents can probe). Regenerate from the registry at Phase 7; additive-only within a `schemaVersion`; each entry carries a type and points at a URL (URL reference and inline description are mutually exclusive).

**URL rule:** URLs inside `/.well-known/ai-catalog.json` must be root-absolute (`/templates/…`) or fully qualified — the file is served from `/.well-known/`, so site-relative `./` paths would resolve to `/.well-known/templates/…` and 404. Site-relative `./` paths are only valid inside site-root `catalog.json`.

```json
{
  "schemaVersion": "1.0.0",
  "name": "ByJTT Web Design Templates for Agents / AI",
  "id": "urn:byjtt:web-design-templates",
  "description": "One-shot unique website design templates with free and paid tiers.",
  "entries": [
    { "type": "product", "name": "Ember Bistro", "url": "/templates/ember-bistro.html" }
  ],
  "links": [
    { "rel": "catalog", "href": "/catalog.json" },
    { "rel": "licensing", "href": "/licensing.html" }
  ]
}
```

## Slug / ID conventions

- Slug: lowercase kebab-case `[a-z0-9-]+`, 3–40 chars, semantic and evocative; globally unique **forever** (never reused, even after retirement); assigned at Phase 1, finalized at Phase 6; collisions resolved with a recorded numeric suffix.
- ID: `T-###` zero-padded, monotonic via `registry.idCounter`; immutable machine primary key.

## Path maps

- Workspace: `byjtt-templates/registry.json`; `byjtt-templates/templates/<slug>/{BRIEF.md, DESIGN-NOTES.md, QA-CHECKLIST.md, manifest.json, changelog.md, assets/, site/}`; bootstrap fallback `byjtt-templates/site-staging/`.
- Marketplace site: `index.html`, `templates.html`, `templates/<slug>.html`, `templates/_detail-pattern.html` (bootstrap stub), `licensing.html`, `about.html`, `catalog.json`, `manifests/<slug>.json`, `/.well-known/ai-catalog.json`, `assets/shared/`, `assets/templates/<slug>/…`, `assets/templates/<slug>/downloads/<slug>-v<version>.zip` (free tier), `previews/<slug>/` (template live-preview path).

## Versioning rules

- Per-template semver from `1.0.0` (only after Phase 5 gates pass). **PATCH** = copy fixes, meta/alt/link fixes; **MINOR** = new sections or images, palette tweaks inside the same direction; **MAJOR** = layout-skeleton, palette-family, or signature-element change (anything an agent could have "learned" from designDNA).
- `schemaVersion` (catalog + ai-catalog format itself) is separate: additive-only within a version; breaking change = bump + migration note. `generatedAt` refreshed on every rebuild.
- Every bump → `changelog[]` entry + `changelog.md` append; MINOR/MAJOR re-run Phase 5 gates.

## Canonical selection algorithm for agents

Documented for consumers of `catalog.json`:

1. **Enumerate** — fetch site-root `catalog.json`; one call lists the whole marketplace.
2. **Filter (hard predicates)** — `language`, `tier`, `archetype`, `price`.
3. **Score (soft)** — tag/tone match; `designDNA` distance against brand constraints; `agentHints.bestFor` / `avoidIf` as include/exclude conditions.
4. **Verify** — fetch `manifests/<slug>.json`; sanity-check version, files, license.
5. **Integrate** — use `preview.liveUrl` if present; otherwise build from `files[]` + `entryFile`.

Stability guarantees: `catalog.json` site-root location is permanent; `schemaVersion` changes are additive within a version and announced; `id`/`slug` immutable; every entry carries `detailPage`, `manifestUrl`, `thumbnail`, `updatedAt`; site-relative paths in `catalog.json` resolve from the site root, and `/.well-known/ai-catalog.json` URLs are root-absolute; deployed URLs are host-reported truth only.
