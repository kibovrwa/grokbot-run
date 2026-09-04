# Build and deploy notes

## Local

From `/workspace/grok-bot-playbook`.

- `npm run build` generates static HTML in `dist/` and runs the checker.
- `npm run check` validates internal links, unique titles, one H1/canonical/description, and rendered counts 193/54/89/42.
- `npm run preview` or `npm run dev` serves `dist/` at `http://localhost:4173`.

Requires Python 3 and Node/npm. There are no npm package dependencies.

## Cloudflare Pages

Create a Pages project for this repository. Set the build command to `npm run build` and the output directory to `dist`. No runtime environment variables are required. `wrangler.toml` declares `pages_build_output_dir = "dist"`. After authenticating Wrangler, you can also upload the existing `dist/` directory to the Pages project.

## Spaceship DNS

Wait until Cloudflare Pages creates the project and provides its `*.pages.dev` hostname. Add the intended custom domain in Cloudflare Pages first and follow the verification prompt. For a subdomain whose DNS remains at Spaceship, create the CNAME Cloudflare specifies and point it to the assigned Pages hostname. For an apex domain, follow Cloudflare's exact custom-domain records; alternatively change the authoritative nameservers at Spaceship to the pair Cloudflare assigns and then manage DNS in Cloudflare. Remove conflicting records, wait for DNS and certificate issuance, and verify HTTPS plus the canonical host before redirecting aliases.

## Data update workflow

Reviewed snapshots live in `/workspace/playbook-data/tools.json`, `cases.json`, `failures.json`, and `official.json`. Preserve their schemas, update Chinese editorial summaries in `scripts/content_*.py`, and change snapshot dates only after checking sources. Run `npm run build`, review pricing conflicts and third-party labels locally, then deploy. Generator and checker assertions protect the expected counts.
