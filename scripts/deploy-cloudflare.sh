#!/usr/bin/env bash
# Deploy the ByJTT marketplace (site/) to Cloudflare Pages.
# Usage:  CLOUDFLARE_API_TOKEN=<token with Cloudflare Pages:Edit> ./scripts/deploy-cloudflare.sh
set -euo pipefail
: "${CLOUDFLARE_API_TOKEN:?Set CLOUDFLARE_API_TOKEN to a token with Account > Cloudflare Pages > Edit}"
cd "$(dirname "$0")/.."

# Idempotent project creation (ignore failure if it already exists)
npx --yes wrangler@latest pages project create byjtt-templates --production-branch main 2>/dev/null || true

# Direct upload of the whole site tree
npx --yes wrangler@latest pages deploy site \
  --project-name byjtt-templates \
  --branch main \
  --commit-dirty=true

echo "Live at: https://byjtt-templates.pages.dev"
