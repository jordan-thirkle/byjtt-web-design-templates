# Lessons Learned — First Template Run

Everything the first gauntlet taught us, split into (A) studio-process lessons now fed back into the skill and (B) landscape-informed backlog candidates for v1.

## A. Gauntlet lessons (round 1, T-001)

| # | Lesson | Skill status |
|---|---|---|
| 1 | Any scroll/reveal animation must gate its hidden state behind a JS-added `html.js` class — content must never depend on JS to be visible | ✅ encoded in Phase 4/5 gates |
| 2 | Fonts named in `designDNA.fonts` must have a real loading mechanism (`@font-face`/link) in the shipped site — otherwise the catalog lies to agents | ✅ encoded in Phase 4 gate |
| 3 | Contrast must be **computed** from the actual hex pairs at shipped sizes (white-on-accent buttons included); QA ticks must cite the number | ✅ encoded in Phase 5 |
| 4 | QA claims must be machine-verifiable — Embercraft certified a `:disabled` style that didn't exist; every tick now cites its check | ✅ encoded in Phase 5 |
| 5 | Hero-over-image rule: scrim must guarantee ≥0.75 paper coverage at the headline zone, checked against the real generated image | ✅ encoded in Phase 5 |
| 6 | License ladder is single-source: marketplace pages copy `listing-and-licensing.md` verbatim; free tier is personal/non-commercial — never grant commercial use for free | ✅ encoded in listing reference |
| 7 | Preview state machine: `liveUrl:null` ⇒ disabled "Preview pending deployment"; enable only from a host-reported URL | ✅ was already specified; now enforced in Phase 7 gate |
| 8 | Ban inline layout styles on template/listing pages (media queries must always win); embed every numbered gallery shot | ✅ encoded in Phase 4/7 |
| 9 | Publish-time path lint: every path in `manifest.files[]` and `assets.*` must resolve on disk; catalog↔manifest field-equality diff; license string exact-match | ✅ encoded in Phase 7 |
| 10 | Favicon must be square; photos ≤1600px/≤250KB; no unreferenced assets in the zip | ✅ encoded in Phase 3/5 |

## B. Landscape-informed backlog (v1 candidates)

Grounded in research on v0, Lovable, bolt.new/bolt.diy, anthropics/skills, awesome-claude-skills, ClawHub/OpenClaw registries, Smithery, HTML5UP, Start Bootstrap, Cruip, Tailwind Plus, Flowbite (sources in the full research file):

1. **`/llms.txt`** alongside `catalog.json` and `/.well-known/ai-catalog.json`, cross-linked from every page ([llmstxt.org](https://llmstxt.org/)) — full agent-discovery parity.
2. **Per-template standard bundle**: README + LICENSE + frontmatter-style metadata in each template folder, mirroring the [anthropics/skills](https://github.com/anthropics/skills) self-contained convention so humans and agents parse the same artifact.
3. **Deterministic publish gate**: schema-validate catalogs, verify every demo URL and screenshot resolves *before* listing — avoids the "published but never indexed" gap reported on [v0 community templates](https://community.vercel.com/t/community-template-submission/6299).
4. **Remix affordance per template**: "how to remix" section (download / git clone / one-line install) — the [Lovable](https://docs.lovable.dev/features/publish)/[bolt.diy](https://github.com/stackblitz-labs/bolt.diy) lesson, with fork rights stated explicitly per tier (avoid forced-remix ambiguity).
5. **Tier mechanic decision**: HTML5UP funnel (free = attribution-in-footer, paid = attribution-free) vs our current free-personal/paid-commercial ladder — decide once, encode the exact attribution snippet in the skill ([HTML5UP license](https://html5up.net/license), [Start Bootstrap MIT](https://startbootstrap.com)).
6. **GitHub distribution kit**: topic tags (`website-template`, `ai-agents`…), screenshots in README, submit-once checklist for [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) / [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) inclusion; keep canonical machine metadata in our own static site since registries get re-aggregated (ClawHub lesson; see also [Smithery](https://smithery.ai/docs/build/publish)).
7. **Category taxonomy** in `catalog.json` (machine-readable buckets) powering both agent filtering and human gallery filters.
8. **Semver + changelog in manifests** so agents detect template updates ([Smithery per-version installability](https://smithery.ai/docs/build/publish)) — partially in place; formalize.

## Decisions taken today

- License ladder: free = personal/non-commercial (attribution appreciated, not required); Commercial (≤5,000) and Extended (≤250,000) are paid-tier unlocks. Single-sourced in the skill.
- Deployment provider: Cloudflare Pages via direct-upload API (registry carries `provider` + note as first-class fields).
- QA records must cite machine checks; narrative passes no longer count.
