# -*- coding: utf-8 -*-
"""Rebuild chrome + regenerable pages without wiping dist/ playbook data."""
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmlutil import ROOT, SITE, page, write, header_html, footer_html, canonical, faq_jsonld, howto_jsonld, itemlist_jsonld, FIND_JS
from seo_pages import PAGES
from content_home import home
from content_pricing import pricing, PRICING_FAQS
from content_learn import what_is, install, first_bot, computer, skills, plugins, cost, INSTALL_FAQS, COMPUTER_FAQS
from content_trouble import troubleshooting
from content_tools import tools_index, tool_detail
from content_hub import learn_index, glossary, cursor_and_grok
from content_compare import compare
from content_operator import operator, OPERATOR_FAQS
from content_ops import ops, OPS_FAQS
from content_cases import use_cases, JOBS

DIST = ROOT / "dist"
SITEMAP_URLS = [
    "/",
    "/learn/",
    "/learn/what-is-grok-bot/",
    "/learn/install/",
    "/learn/first-bot/",
    "/learn/computer/",
    "/learn/skills-routines/",
    "/learn/plugins/",
    "/learn/cost-and-pitfalls/",
    "/learn/operator/",
    "/learn/ops/",
    "/learn/glossary/",
    "/learn/cursor/",
    "/compare/",
    "/use-cases/",
    "/troubleshooting/",
    "/tools/",
    "/tools/grok-bot-cli/",
    "/tools/grok-bot-skill/",
    "/tools/grokbot-tui/",
    "/tools/usage-menu-bar/",
    "/tools/linux-port/",
    "/pricing/",
    "/sources/",
]


def path_from_file(f):
    rel = f.relative_to(DIST).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + str(f.relative_to(DIST).parent).replace("\\", "/") + "/"


def rewrite_chrome(html, path):
    css = (ROOT / "src/css/site.css").read_text(encoding="utf-8")
    html = re.sub(r"<style>.*?</style>", "<style>%s</style>" % css, html, count=1, flags=re.S)
    html = re.sub(r"<header class=\"site\">.*?</header>", header_html(path), html, count=1, flags=re.S)
    html = re.sub(r"<footer class=\"site\">.*?</footer>", footer_html(), html, count=1, flags=re.S)
    html = re.sub(r'\s*<link rel="alternate" hreflang="zh-CN"[^>]*>', "", html)
    html = re.sub(r'\s*<meta property="og:locale:alternate"[^>]*>', "", html)
    html = re.sub(r'<a class="lang-switch"[^>]*>.*?</a>', "", html)
    html = html.replace("Chinese long-form guides", "Chinese guides")
    html = html.replace("Orange Book and Blue Book", "Sources")
    html = html.replace("Grok Bot 攻略", "Grok Bot")
    html = html.replace("193 tools, 40 Field Cases", "199 tools, plus Field Cases")
    html = html.replace("193 tools, plus Field Cases", "199 tools, plus Field Cases")
    html = html.replace(
        '<li><a href="https://docs.x.ai/grok-bot/use-cases">Official use-cases</a> timed out. Official job examples instead use sentences already fetched from overview / x.ai/bot.</li>',
        '<li><a href="https://docs.x.ai/grok-bot/use-cases">Official use-cases</a> opened on 2026-09-04. Starter jobs on this site follow that page’s read-and-prepare pattern; they are not a reprint.</li>',
    )
    find_tag = '<script data-find-js>%s</script>' % FIND_JS
    if "data-find-js" in html:
        html = re.sub(r"<script data-find-js>.*?</script>", find_tag, html, count=1, flags=re.S)
    else:
        html = html.replace("</body>", find_tag + "</body>", 1)
    return html


def write_sitemap():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in SITEMAP_URLS:
        lines.append("<url><loc>%s</loc><lastmod>2026-09-20</lastmod></url>" % canonical(u))
    lines.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_redirects():
    extra = [
        "/learn/zh-guides /sources/ 301",
        "/learn/zh-guides/ /sources/ 301",
        "/learn/zh-guides/index.html /sources/ 301",
        "/learn/guides /sources/ 301",
        "/learn/guides/ /sources/ 301",
    ]
    src = ROOT / "public" / "_redirects"
    base = src.read_text(encoding="utf-8").rstrip() + "\n"
    seen = set(base.splitlines())
    extra = [e for e in extra if e not in seen]
    aliases = ["# generated trailing-slash / index.html aliases", "/index.html / 301"]
    for u in SITEMAP_URLS:
        if u == "/":
            continue
        bare = u.rstrip("/")
        aliases.append("%s %s 301" % (bare, u))
        aliases.append("%s/index.html %s 301" % (bare, u))
    text = base + "\n".join(extra + aliases) + "\n"
    (DIST / "_redirects").write_text(text, encoding="utf-8")


def patch_sources(html):
    if "Related community guides" in html:
        return html
    block = """
<section class="source-section">
<h2>Related community guides</h2>
<p class="lede">Linked only. This site does not reprint them.</p>
<ul class="source-list">
<li class="source-item"><a href="https://github.com/KinGao294/grok-bot-orange-book">Orange Book</a><span class="muted">Community ops notes on multi-Bot teams, routines, and cost control. Cross-check pricing here — mid-August plan lists went stale fast.</span></li>
<li class="source-item"><a href="https://github.com/rockyzhuo/grok-bot-blue-book">Blue Book</a><span class="muted">Companion ops manual: artifact contracts and route templates. Isolation is still per user, not per Bot.</span></li>
<li class="source-item"><a href="https://github.com/RongleCat/awesome-grok-bot">awesome-grok-bot</a><span class="muted">Upstream CC0 list this catalog and the field-case table are built from.</span></li>
</ul>
</section>
"""
    return html.replace(
        '<section class="source-section">\n<h2>Official materials',
        block + '<section class="source-section">\n<h2>Official materials',
        1,
    )


def main():
    shutil.copy2(ROOT / "public" / "brand" / "grok-bot-face.svg", DIST / "brand" / "grok-bot-face.svg")
    on_dark = ROOT / "public" / "brand" / "grok-bot-face-on-dark.svg"
    if on_dark.exists():
        shutil.copy2(on_dark, DIST / "brand" / "grok-bot-face-on-dark.svg")
    if (ROOT / "public" / "og.png").exists():
        shutil.copy2(ROOT / "public" / "og.png", DIST / "og.png")

    body, faqs = home()
    m = PAGES["/"]
    write("/", page("/", m["title"], m["description"], body, jsonld=[faq_jsonld(faqs)]))
    pm = PAGES["/pricing/"]
    write("/pricing/", page("/pricing/", pm["title"], pm["description"], pricing(), jsonld=[faq_jsonld(PRICING_FAQS)]))
    um = PAGES["/use-cases/"]
    jobs_ld = itemlist_jsonld(
        "Grok Bot starter jobs",
        [(j["name"], SITE + "/use-cases/#starter-jobs") for j in JOBS],
    )
    write("/use-cases/", page("/use-cases/", um["title"], um["description"], use_cases(), jsonld=[jobs_ld]))
    tm = PAGES["/tools/"]
    write("/tools/", page("/tools/", tm["title"], tm["description"], tools_index()))

    hub_body, hub_faqs = learn_index()
    hm = PAGES["/learn/"]
    write("/learn/", page("/learn/", hm["title"], hm["description"], hub_body, jsonld=[faq_jsonld(hub_faqs)]))
    gloss_body, gloss_faqs = glossary()
    gm = PAGES["/learn/glossary/"]
    write("/learn/glossary/", page("/learn/glossary/", gm["title"], gm["description"], gloss_body, jsonld=[faq_jsonld(gloss_faqs)]))
    cur_body, cur_faqs = cursor_and_grok()
    cm = PAGES["/learn/cursor/"]
    write("/learn/cursor/", page("/learn/cursor/", cm["title"], cm["description"], cur_body, jsonld=[faq_jsonld(cur_faqs)]))
    cmp_body, cmp_faqs = compare()
    cpm = PAGES["/compare/"]
    opm = PAGES["/learn/operator/"]
    write("/learn/operator/", page("/learn/operator/", opm["title"], opm["description"], operator()[0], jsonld=[faq_jsonld(OPERATOR_FAQS)]))
    opx = PAGES["/learn/ops/"]
    write("/learn/ops/", page("/learn/ops/", opx["title"], opx["description"], ops()[0], jsonld=[
        faq_jsonld(OPS_FAQS),
        howto_jsonld(
            "Run X, Cursor, MCP, and the Grok Bot computer",
            "Map the four surfaces, scout X without posting, brief a Cloud Agent, then add only remote MCP.",
            [
                ("Draw the stack", "Bot app, shared computer, plugins, Cloud Agent, official X plugin. One account."),
                ("Scout X, do not post", "Use the official X connector for research. Drafts go in /workspace. You publish."),
                ("Brief a Cloud Agent", "Write a /workspace brief. Cursor opens the PR. You merge."),
                ("Add remote MCP only", "Public HTTPS. No localhost. No Bearer token in chat."),
            ],
        ),
    ]))
    write("/compare/", page("/compare/", cpm["title"], cpm["description"], cmp_body, jsonld=[
        faq_jsonld(cmp_faqs),
        itemlist_jsonld("Grok Bot alternatives", [
            ("Official Grok Bot", "https://x.ai/bot"),
            ("OpenMausBot", "https://github.com/milind-soni/OpenMausBot"),
            ("rakazo", "https://github.com/elie222/rakazo"),
            ("gawkbot", "https://github.com/najmuzzaman-mohammad/gawkbot"),
        ]),
    ]))

    first_howto = howto_jsonld(
        "Create a first Grok Bot",
        "Name one job, paste a read-and-prepare brief, watch the shared computer, then save a skill after two good runs.",
        [
            ("Name one job", "Short name. One outcome. Do not create twelve Bots on day one."),
            ("Paste a read-only brief", "Say what to return and when to stop. Do not send, delete, or pay."),
            ("Watch the computer", "Take over for password and 2FA. Never paste those into chat."),
            ("Save a skill later", "After two good runs, keep the method. Routines wait until then."),
        ],
    )

    learn = {
        "/learn/what-is-grok-bot/": what_is,
        "/learn/install/": install,
        "/learn/first-bot/": first_bot,
        "/learn/computer/": computer,
        "/learn/skills-routines/": skills,
        "/learn/plugins/": plugins,
        "/learn/cost-and-pitfalls/": cost,
    }
    for path, fn in learn.items():
        meta = PAGES[path]
        extra = []
        if path == "/learn/first-bot/":
            extra.append(first_howto)
        if path == "/learn/install/":
            extra.append(faq_jsonld(INSTALL_FAQS))
        if path == "/learn/computer/":
            extra.append(faq_jsonld(COMPUTER_FAQS))
        write(path, page(path, meta["title"], meta["description"], fn(), jsonld=extra or None))

    tm_help = PAGES["/troubleshooting/"]
    write("/troubleshooting/", page("/troubleshooting/", tm_help["title"], tm_help["description"], troubleshooting()))

    details = {
        "cli": "/tools/grok-bot-cli/",
        "skill": "/tools/grok-bot-skill/",
        "tui": "/tools/grokbot-tui/",
        "usage": "/tools/usage-menu-bar/",
        "linux": "/tools/linux-port/",
    }
    for key, path in details.items():
        meta = PAGES[path]
        write(path, page(path, meta["title"], meta["description"], tool_detail(key)))

    written = {"/", "/pricing/", "/use-cases/", "/tools/", "/learn/", "/learn/glossary/", "/learn/cursor/", "/learn/operator/", "/learn/ops/", "/compare/", "/troubleshooting/"}
    written.update(learn)
    written.update(details.values())
    n = len(written)
    for f in sorted(DIST.rglob("*.html")):
        path = path_from_file(f)
        if path in written:
            continue
        html = f.read_text(encoding="utf-8")
        html = rewrite_chrome(html, path)
        if path == "/sources/":
            html = patch_sources(html)
        f.write_text(html, encoding="utf-8")
        n += 1

    zh = DIST / "learn" / "zh-guides"
    if zh.exists():
        shutil.rmtree(zh)

    write_sitemap()
    write_redirects()
    (DIST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE, encoding="utf-8"
    )
    llms = ROOT / "public" / "llms.txt"
    if llms.exists():
        shutil.copy2(llms, DIST / "llms.txt")
    headers = ROOT / "public" / "_headers"
    if headers.exists():
        shutil.copy2(headers, DIST / "_headers")
    from indexnow import KEY, write_key_files
    from search_index import write_index
    write_key_files()
    rows = write_index()
    print("refreshed", n, "pages; search", rows, "rows; indexnow", KEY)


if __name__ == "__main__":
    main()
