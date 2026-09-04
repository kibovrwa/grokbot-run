# Deploy grokbot.run (short path)

1. **Git init** — In this folder: `git init`, add files (respect `.gitignore`), commit. Keep `dist/` so Pages can ship without Python if needed.
2. **Push GitHub** — Create a public or private repo, add `origin`, push the main branch.
3. **Cloudflare Pages** — New project → connect the repo. Build: `npm run build`. Output: `dist`. Or upload `dist/` / Wrangler Pages deploy after auth. Confirm the `*.pages.dev` URL loads.
4. **Custom domain** — Only after the Pages hostname exists: add `grokbot.run` in Pages → Custom domains, then at Spaceship add the CNAME/apex records Cloudflare shows (see BUILD-NOTES.md). Wait for cert + HTTPS.
5. **Search Console** — Verify the property, submit `https://grokbot.run/sitemap.xml`. Spot-check `og.png` and a few canonicals.
6. **Tomorrow backlinks** — Work through BACKLINKS.md (awesome-grok-bot PR, own READMEs, tool-author See also, forum answers with symptom anchors). No spam, no fake affiliation.
