#!/usr/bin/env python3
"""Regenerate site/catalog.json + site/manifests/*.json + workbench manifests from registry.json.
The registry is the single source of truth (byjtt skill Phase 7). Usage: python3 regen-catalog.py"""
import json, os, sys, datetime

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
CAT_MAP = {"landing": "landing-pages", "portfolio": "portfolio", "restaurant": "restaurant",
           "saas": "saas", "event": "event", "docs": "docs", "blog": "blog"}
CATEGORIES = ["landing-pages", "portfolio", "restaurant", "saas", "event", "docs", "blog"]

reg = json.load(open(f"{B}/registry.json"))
canonical = reg.get("deployment", {}).get("lastUrl") or "https://byjtt-templates.pages.dev"
canonical = canonical.rstrip("/") or "https://byjtt-templates.pages.dev"
generated = reg.get("_generatedAt")

entries = []
for e in reg["templates"]:
    if e.get("status") == "retired":
        continue
    slug = e["slug"]
    manifest = {k: v for k, v in e.items() if k not in ("status", "releaseState")}
    json.dump(manifest, open(f"{B}/templates/{slug}/manifest.json", "w"), indent=2, ensure_ascii=False)
    json.dump(manifest, open(f"{B}/site/manifests/{slug}.json", "w"), indent=2, ensure_ascii=False)
    entries.append({
        "id": e["id"], "slug": slug, "name": e["name"], "version": e["version"],
        "language": e["language"], "archetype": e["archetype"],
        "category": e.get("category") or CAT_MAP.get(e["archetype"], "landing-pages"),
        "description": e["description"], "tags": e["tags"], "tier": e["tier"],
        "price": e["price"], "purchaseState": e["purchaseState"], "purchaseUrl": e["purchaseUrl"],
        "license": e["license"], "detailPage": f"./templates/{slug}.html",
        "manifestUrl": f"./manifests/{slug}.json",
        "thumbnail": f"./assets/templates/{slug}/card.jpg",
        "preview": {"liveUrl": e["preview"]["liveUrl"], "screenshots": e["preview"]["screenshots"]},
        "designDNA": {k: v for k, v in e["designDNA"].items() if k not in ("typeScale", "presetAnchor")},
        "agentHints": e["agentHints"], "promptKit": e.get("promptKit"), "updatedAt": e["updatedAt"],
    })

catalog = {
    "schemaVersion": "1.0.0",
    "generatedAt": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "marketplace": reg["marketplace"]["name"], "canonicalUrl": canonical, "categories": CATEGORIES,
    "count": len(entries), "entries": entries,
}
json.dump(catalog, open(f"{B}/site/catalog.json", "w"), indent=2, ensure_ascii=False)
print(f"catalog regenerated: {len(entries)} entries, canonical {canonical}")
ai = {
    "schemaVersion": "1.0.0", "name": reg["marketplace"]["name"],
    "id": "urn:byjtt:web-design-templates",
    "description": "One-shot unique website design templates with free and paid tiers. Machine catalog: /catalog.json; per-template contracts: /manifests/<slug>.json.",
    "entries": [{"type": "product", "name": x["name"], "url": f"{canonical}{x['detailPage'][1:]}"} for x in entries],
    "links": [{"rel": "catalog", "href": f"{canonical}/catalog.json"}, {"rel": "licensing", "href": f"{canonical}/licensing.html"}],
}
json.dump(ai, open(f"{B}/site/.well-known/ai-catalog.json", "w"), indent=2, ensure_ascii=False)
print(f"ai-catalog regenerated: {len(ai['entries'])} entries")
