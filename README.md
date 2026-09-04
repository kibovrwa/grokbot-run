# Grok Bot Guide

Unofficial English community handbook for **Grok Bot** (Cursor / xAI): named teammates plus one shared cloud computer. Not grok.com chat. Not an official xAI or Cursor product page.

**Site:** [https://grokbot.run](https://grokbot.run)

Official packages stay on [x.ai/bot](https://x.ai/bot). Sign in with the Cursor account that holds the plan and the usage. There is no extra Grok Bot account. Brand marks appear only for identification. Pricing and eligibility change; treat dated snapshots as pointers to primary sources, not guarantees.

## Start here

| Job | Page |
| --- | --- |
| Install and Cursor login | https://grokbot.run/learn/install/ |
| First Bot, one cited brief | https://grokbot.run/learn/first-bot/ |
| The computer is shared | https://grokbot.run/learn/computer/ |
| After week one (manage a roster) | https://grokbot.run/learn/operator/ |
| X, Cursor Cloud Agents, MCP | https://grokbot.run/learn/ops/ |
| Dated plan conflicts (no invented USD) | https://grokbot.run/pricing/ |
| Can’t reach / Recover before Reset | https://grokbot.run/troubleshooting/ |
| Cursor login is not an IDE panel | https://grokbot.run/learn/cursor/ |

## What this is not

- Not the official download storefront
- Not a reconstructed client, prompt dump, or skill pack
- Isolation is per **user**, not per Bot. Screens are not a security fence.

## What is in the repo

| Path | Role |
|------|------|
| `src/` | CSS and reviewed JSON snapshots |
| `scripts/` | Python static-site generator + checker |
| `public/` | Static assets (`og.png`, brand SVGs, `_headers`) |
| `dist/` | Built HTML (committed so you can deploy without Python) |
| `BUILD-NOTES.md` | Local build, Cloudflare Pages, Spaceship DNS, data updates |
| `BACKLINKS.md` | Legitimate link-building checklist (do tomorrow) |
| `DEPLOY.md` | Short deploy sequence (GitHub to Pages to DNS to Search Console) |

## Local commands

From the project root:

- `npm run build` generates static HTML in `dist/` and runs the checker.
- `npm run check` validates internal links, unique titles, one H1/canonical/description, and rendered counts 199/54/89/42.
- `npm run preview` or `npm run dev` serves `dist/` at `http://localhost:4173`.

Requires Python 3 and Node/npm. There are no npm package dependencies.

### Deploy with or without rebuilding

- **With Python:** use the build script above, then point Cloudflare Pages at the repo (or upload `dist/`).
- **Without Python:** `dist/` is committed. Set Pages build to a no-op or upload `dist/` as-is. Still rebuild when you change `src/` or `scripts/`.

## Cloudflare Pages

| Setting | Value |
|---------|-------|
| Build command | `npm run build` |
| Output directory | `dist` |
| Node | any recent LTS (no install step required) |

Create a Pages project for this repository. Set the build command to `npm run build` and the output directory to `dist`. No runtime environment variables are required. `wrangler.toml` declares `pages_build_output_dir = "dist"`. After authenticating Wrangler, you can also upload the existing `dist/` directory to the Pages project.

## Custom domain (Spaceship DNS)

Wait until the Pages hostname (`*.pages.dev`) exists, then add `grokbot.run`. Add the intended custom domain in Cloudflare Pages first and follow the verification prompt. For a subdomain whose DNS remains at Spaceship, create the CNAME Cloudflare specifies and point it to the assigned Pages hostname. For an apex domain, follow Cloudflare's exact custom-domain records; alternatively change the authoritative nameservers at Spaceship to the pair Cloudflare assigns and then manage DNS in Cloudflare. Remove conflicting records, wait for DNS and certificate issuance, and verify HTTPS plus the canonical host before redirecting aliases.

Details: [BUILD-NOTES.md](./BUILD-NOTES.md).

## Data updates

Reviewed snapshots live in `/workspace/playbook-data/tools.json`, `cases.json`, `failures.json`, and `official.json`. Preserve their schemas, update Chinese editorial summaries in `scripts/content_*.py`, and change snapshot dates only after checking sources. Run `npm run build`, review pricing conflicts and third-party labels locally, then deploy. Generator and checker assertions protect the expected counts.

## Tomorrow

Follow [BACKLINKS.md](./BACKLINKS.md) for high-leverage, non-spammy links (awesome-grok-bot PR, tool-author See also, Search Console sitemap).

## Contact

`hello@grokbot.run` — site mail, not xAI or Cursor support.
