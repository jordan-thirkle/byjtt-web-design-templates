# Listing Standards, Tiers & Licensing

Grounded in published marketplace practice (sources at the end). Where evidence was not retrievable, this file says so — do not invent market "facts".

## Contents

- [Listing standards](#listing-standards)
- [Free vs paid tier policy](#free-vs-paid-tier-policy)
- [License ladder (plain English)](#license-ladder-plain-english)
- [Universal prohibitions](#universal-prohibitions)
- [Pricing rules](#pricing-rules)
- [Sources](#sources)

## Listing standards

Proven conventions from established marketplaces — apply them to every card, detail page, and gallery:

1. **Image-led previews.** Marketplaces report that image-led covers convert better than text-heavy marketing graphics (Envato item presentation requirements). The card thumbnail and detail hero must be image-led, never a wall of text.
2. **Live demo is part of the product.** Envato makes a hosted live preview mandatory for web themes. ByJTT equivalent: `preview.liveUrl` — but only ever set it from a host-reported deployment URL. Before deployment, show "preview pending deployment", never a guessed URL.
3. **Numbered preview gallery.** Follow the `01_`, `02_`, `03_`… ordering convention for gallery screenshots (`assets/templates/<slug>/01_hero.png`, …). Consistent multi-shot galleries build trust.
4. **The description is binding.** Marketplace support policies treat "works as described" as enforceable. Whatever `manifest.description` and the detail page claim — sections, behavior, responsive behavior — must be true of the shipped template. Write descriptions after the build passes Phase 5, not before.
5. **Curated, not flooded.** Quality over quantity: every listing passes the same Phase 5 gates regardless of tier (Creative Tim and UI8 both keep free products at full quality; curation is the brand).

## Free vs paid tier policy

**Single source of truth:** every marketplace page, manifest, and card copies this ladder verbatim. Never grant commercial use to the free tier — the paid ladder must always have something real to unlock.

- **Free tier = the funnel.** Full-quality template, complete files, no watermarks, no crippled features, no nag screens. (UI8 Freebies: "no strings attached"; Creative Tim maintains a real free catalog.) Rights: personal, non-commercial end products; attribution appreciated, never required.
- **Paid tier = per-item purchase.** Price display + a `purchaseUrl` the user configures (external Stripe Payment Link, Gumroad, or similar). Static hosting cannot process payments — never render a checkout form, payment JS, or fake confirmation.
- **Missing purchase link** → `purchaseState:"coming-soon"`, visible disabled "Purchase coming soon" state on the detail page. Never hide the tier or fake availability.
- **Tier display** on every card and detail page: badge (`Free` / price), license name, and the licensing page link.

## License ladder (plain English)

Publish the full ladder in `licensing.html` using the "Simple Human Explanation" pattern (plain-English summary first, formal terms below). Default ladder, adapted from Creative Market's published tiers:

| Tier | Rights |
|---|---|
| **Free / Personal** | Use in personal, non-commercial end products. Attribution appreciated, not required (ByJTT design decision — state it explicitly in licensing.html). |
| **Commercial** | Use in end products for a business, up to **5,000** end products / sales. |
| **Extended** | Up to **250,000** end products / sales, and required whenever end users must pay to access the end product (Envato rule: Regular = free end product, Extended = users pay to access). |

Definitions to state verbatim-ish in licensing.html:
- An **End Product** is a final, completed work that adds significant value beyond the template itself.
- An End Product is **not** a UI kit, theme, or template, and not a tool that extracts or re-exposes the template's assets.
- Licenses are non-exclusive, worldwide, and lifetime for the purchased version; ownership of the template files stays with ByJTT.

## Universal prohibitions

Mirror the prohibitions that every major marketplace enforces; put them in licensing.html and the paid-tier manifest notes:

- No redistributing or reselling the template (even modified) as a template, theme, or UI kit.
- No extraction tools or bulk-download tooling built on the template files.
- No using the templates to build a competing template marketplace or an automated template generator.
- No open-sourcing or re-licensing the template code without written consent.

## Pricing rules

- Prices are **user decisions**. The skill sets `price` only from an explicit user instruction for that template.
- Research found **no verified typical price range** for single HTML/landing-page templates (an isolated "$10" search snippet and custom-design-service figures exist, but neither measures template prices). Do not quote "market rates" to the user; if asked, say pricing evidence was not verified.

## Sources

Retrieved while researching marketplace practice (Envato author requirements; Creative Market templates use cases; UI8 terms; Creative Tim license; API Evangelist AI Catalog standard):

- Envato — Item Presentation Requirements: <https://help.author.envato.com/hc/en-us/articles/360000424863-Item-Presentation-Requirements>
- ThemeForest — Item Support Policy ("works as described"): <https://themeforest.net/page/item_support_policy>
- ThemeForest — License FAQ (Regular vs Extended): <https://themeforest.net/licenses/faq>
- Creative Market — Templates Use Cases (Personal / Commercial 5,000 / Extended 250,000): <https://support.creativemarket.com/hc/en-us/articles/360031367014-Templates-Use-Cases>
- UI8 — Terms (End Product definition; Freebies; non-refundable digital goods): <https://ui8.net/terms> and <https://ui8.net/categories/freebies>
- Creative Tim — License (Simple Human Explanation; prohibitions): <https://www.creative-tim.com/license>
- API Evangelist — AI Catalog Standard (`/.well-known/ai-catalog.json`): <https://standards.apievangelist.com/store/ai-catalog/>
