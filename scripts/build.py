# -*- coding: utf-8 -*-
import sys, shutil, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmlutil import ROOT, SITE, page, write, LESSONS
from seo_pages import meta
from content_home import home, FAQS
from content_learn import what_is, install, first_bot, computer, skills, plugins, cost
from content_cases import use_cases, CASES
from content_trouble import troubleshooting
from content_tools import tools_index, tool_detail
from content_pricing import pricing
from content_sources import sources

DIST = ROOT / "dist"

def main():
    missing = [
        path for path in (
            Path("/workspace/playbook-data/failures.json"),
            Path("/workspace/playbook-data/official.json"),
        ) if not path.exists()
    ]
    if missing:
        raise SystemExit(
            "Refusing to wipe dist/: missing playbook data %s. "
            "Copy snapshots into place or restore dist/ from the last good build."
            % ", ".join(str(p) for p in missing)
        )
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    brand_src = ROOT / "public" / "brand"
    brand_dst = DIST / "brand"
    shutil.copytree(brand_src, brand_dst)
    for extra in (ROOT / "public").iterdir():
        if extra.name == "brand":
            continue
        dest = DIST / extra.name
        if extra.is_file():
            shutil.copy2(extra, dest)

    home_body, faqs = home()
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    t, d = meta("/")
    write("/", page("/", t, d, home_body, jsonld=[faq_ld]))

    pages = [
        ("/learn/what-is-grok-bot/", what_is()),
        ("/learn/install/", install()),
        ("/learn/first-bot/", first_bot()),
        ("/learn/computer/", computer()),
        ("/learn/skills-routines/", skills()),
        ("/learn/plugins/", plugins()),
        ("/learn/cost-and-pitfalls/", cost()),
        ("/use-cases/", use_cases()),
        ("/troubleshooting/", troubleshooting()),
        ("/tools/", tools_index()),
        ("/pricing/", pricing()),
        ("/sources/", sources()),
    ]
    for path, body in pages:
        title, desc = meta(path)
        write(path, page(path, title, desc, body))

    details = {
        "cli": "/tools/grok-bot-cli/",
        "skill": "/tools/grok-bot-skill/",
        "tui": "/tools/grokbot-tui/",
        "usage": "/tools/usage-menu-bar/",
        "linux": "/tools/linux-port/",
    }
    for key, path in details.items():
        t, d = meta(path)
        write(path, page(path, t, d, tool_detail(key)))

    (DIST / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE, encoding="utf-8")
    urls = ["/", "/learn/what-is-grok-bot/", "/learn/install/", "/learn/first-bot/", "/learn/computer/",
            "/learn/skills-routines/", "/learn/plugins/", "/learn/cost-and-pitfalls/",
            "/use-cases/", "/troubleshooting/", "/tools/", "/tools/grok-bot-cli/", "/tools/grok-bot-skill/",
            "/tools/grokbot-tui/", "/tools/usage-menu-bar/", "/tools/linux-port/", "/pricing/", "/sources/"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" if u == "/" else SITE + u.rstrip("/") + "/"
        sm.append("<url><loc>%s</loc></url>" % loc)
    sm.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

    extra = ["# generated trailing-slash / index.html aliases"]
    extra.append("/index.html / 301")
    for u in urls:
        if u == "/":
            continue
        bare = u.rstrip("/")
        extra.append("%s %s 301" % (bare, u))
        extra.append("%s/index.html %s 301" % (bare, u))
    redirects = (DIST / "_redirects").read_text(encoding="utf-8").rstrip() + "\n" + "\n".join(extra) + "\n"
    (DIST / "_redirects").write_text(redirects, encoding="utf-8")
    print("wrote", len(urls), "urls into", DIST)

if __name__ == "__main__":
    main()
