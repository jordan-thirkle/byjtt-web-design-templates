# v2 Accounts Design — Worker + D1 + OAuth

Design for adding sign-in / register / purchases to the ByJTT marketplace without giving up
the static v1. Principle: **v1 artifacts (catalog.json, manifests, kits, static pages) stay
exactly as they are — v2 adds an API layer and gates downloads, not pages.**

## 1. Architecture

```
                    ┌────────────────────────────┐
   Browser ───────► │  Static site (unchanged)   │  catalog.json / pages / kits
                    └─────────────┬──────────────┘
                                  │ fetch (/api/*)
                    ┌─────────────▼──────────────┐
                    │  Worker API (same zone)    │  /api/auth/*  /api/purchases/*  /api/downloads/*
                    │  sessions in KV, OAuth     │
                    └───────┬───────────┬────────┘
                            │           │
                     ┌──────▼───┐  ┌────▼─────────────┐
                     │  D1      │  │  R2              │
                     │ users,   │  │  licensed kits,  │
                     │ purchases│  │  receipts        │
                     └──────────┘  └────┬─────────────┘
                                        │ webhook
                                 ┌──────▼─────┐
                                 │  Stripe    │  Payment Links → webhook → license
                                 └────────────┘
```

- **Worker with Static Assets** (Cloudflare's current recommendation over Pages Functions for
  new work): the static site deploys unchanged; the Worker adds `/api/*` routes in front.
- **D1** (SQLite) for identity + commerce records; **KV** for sessions; **R2** for the paid
  kit payloads and receipts.
- **OAuth**: GitHub + Google (the audience already has both). Authorization Code + PKCE;
  session = signed, HttpOnly, SameSite=Lax cookie backed by KV (TTL 30 days, sliding).
- **Payments**: keep v1's honest static price display; paid checkout moves to Stripe
  Payment Links (no PCI on our side) whose webhook writes the purchase + issues a
  single-use download grant.

## 2. Data model (D1)

```sql
users          (id TEXT PK, email TEXT UNIQUE, display_name, oauth_provider,
                oauth_subject, created_at)
sessions       (sid TEXT PK, user_id, expires_at, created_at)      -- or KV-only
purchases      (id TEXT PK, user_id, template_id, tier TEXT,        -- commercial|extended
                amount_cents INT, currency, stripe_session_id UNIQUE,
                license_key TEXT UNIQUE, status, created_at)
downloads      (id TEXT PK, purchase_id, kit_version, served_at)
template_versions (template_id, version, released_at, notes)        -- matches manifest changelogs
```

License rules mirror the ladder: free tier downloads need no account; Commercial/Extended
purchases bind a license_key to a user and unlock the paid kit version + updates for that
template_id.

## 3. API surface (Worker)

| Route | Auth | Purpose |
|---|---|---|
| `GET /api/auth/:provider/start` | — | OAuth redirect (PKCE, state cookie) |
| `GET /api/auth/:provider/callback` | — | exchange code, create/find user, set session |
| `POST /api/auth/logout` | session | clear KV session + cookie |
| `GET /api/me` | session | email, purchases, license keys |
| `POST /api/checkout` | session | create Stripe Payment Link session for tier+template |
| `POST /api/stripe/webhook` | Stripe sig | verify signature, write purchase + license_key |
| `GET /api/download/:template/:version` | session + license (free tier: none) | stream kit from R2, log download |

Free-tier flow needs **zero accounts**: `GET /api/download/embercraft/1.1.0` with no session
serves the free zip (rate-limited) — v1 behavior preserved. Paid tiers 401 without a valid
license_key for that template_id.

## 4. Flows

- **Register/sign-in**: "Sign in" → `/api/auth/github/start` → provider consent → callback
  sets session → redirect back to the page the user came from. No passwords ever stored.
- **Buy (paid template)**: sign in → checkout → Stripe Payment Link → webhook marks purchase
  active → detail page now shows "Download v1.1 (Commercial license)" for that user.
- **Iterate**: the v1 prompt kit is unchanged; logged-in buyers additionally get a
  `license_key` line the publish prompt can echo in the footer (Commercial attribution
  optional, Extended not required).

## 5. Security notes

- Cookie: `HttpOnly; Secure; SameSite=Lax`; session IDs random 128-bit; KV TTL 30d.
- Stripe webhook: verify signature with the signing secret (Worker secret binding), reject
  replayed events by event id.
- OAuth: state + PKCE verifier in short-TLV KV; redirect allowlist (same origin only).
- Secrets via Worker secret bindings only — never in the repo (the v1 lesson: the Cloudflare
  token pasted in chat should be rotated; v2 secrets live in bindings).
- Download route: license check server-side; R2 objects are private (no public buckets).

## 6. Migration path from v1

1. Ship the Worker in front of the existing static deployment (zero content changes).
2. Add sign-in + `/api/me` (no gating yet) — optional for users.
3. Move paid purchases to Stripe Payment Links + webhook.
4. Gate paid downloads only; free downloads stay open forever.
5. Optionally add the Workshop-Console-style page (from the prompt-kit research) that
   composes prompts client-side for logged-in buyers.

Estimated v2 scope: 1 Worker (~400 lines), 5 D1 migrations, 2 OAuth apps, 1 Stripe account —
no change to templates, kits, or the catalog contract.
