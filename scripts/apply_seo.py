# -*- coding: utf-8 -*-
"""Rewrite titles/descriptions/H1s on dist pages from seo_pages.PAGES.
Regenerates the homepage (no playbook-data required).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmlutil import ROOT, page, write
from seo_pages import PAGES
from content_home import home
from content_pricing import pricing

DIST = ROOT / "dist"


def file_for(path):
    if path == "/":
        return DIST / "index.html"
    return DIST / path.strip("/") / "index.html"


def replace_meta(html, title, description):
    html = re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, html, count=1, flags=re.S)
    html = re.sub(
        r'<meta name="description" content=".*?"',
        '<meta name="description" content="%s"' % description,
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content=".*?"',
        '<meta property="og:title" content="%s"' % title,
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content=".*?"',
        '<meta property="og:description" content="%s"' % description,
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:title" content=".*?"',
        '<meta name="twitter:title" content="%s"' % title,
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="twitter:description" content=".*?"',
        '<meta name="twitter:description" content="%s"' % description,
        html,
        count=1,
    )
    return html


def replace_h1(html, new_h1):
    return re.sub(r"<h1[^>]*>.*?</h1>", "<h1>%s</h1>" % new_h1, html, count=1, flags=re.S)


def main():
    body, faqs = home()
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    home_meta = PAGES["/"]
    write("/", page("/", home_meta["title"], home_meta["description"], body, jsonld=[faq_ld]))
    pmeta = PAGES["/pricing/"]
    write("/pricing/", page("/pricing/", pmeta["title"], pmeta["description"], pricing()))

    n = 2
    for path, meta in PAGES.items():
        if path in ("/", "/pricing/"):
            continue
        dest = file_for(path)
        if not dest.exists():
            print("skip missing", path)
            continue
        html = dest.read_text(encoding="utf-8")
        html = replace_meta(html, meta["title"], meta["description"])
        html = replace_h1(html, meta["h1"])
        dest.write_text(html, encoding="utf-8")
        n += 1
    print("seo-applied", n, "pages")


if __name__ == "__main__":
    main()
