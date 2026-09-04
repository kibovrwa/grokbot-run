# -*- coding: utf-8 -*-
from html import escape
import json, re
from htmlutil import ROOT

def load(name):
    return json.loads((ROOT / "src/data" / name).read_text(encoding="utf-8"))

def classify(item):
    blob = (item.get("name") or "") + " " + (item.get("blurb") or "") + " " + (item.get("url") or "")
    b = blob.lower()
    if "ronglecat/grok-app" in b or ("grok-app" in b and "build" in b):
        return ["Related / easy to confuse"]
    tags = []
    if re.search(r"\bcli\b|command.line|\bgbot\b|\bgbq\b|\bgbu\b", b):
        tags.append("CLI")
    if "tui" in b:
        tags.append("TUI")
    if "linux" in b or "aur" in b or ".deb" in b or "appimage" in b or "copr" in b or "fedora" in b or "nix flake" in b or "arch linux" in b:
        tags.append("Linux")
    if "usage" in b or "meter" in b or "menu bar" in b or "quota" in b:
        tags.append("Usage")
    if "mcp" in b:
        tags.append("MCP")
    if "plugin" in b or "skill" in b:
        tags.append("Plugins / skills")
    if not tags:
        tags.append("Other")
    return tags

DETAIL_URLS = {
    "https://github.com/ScriptedAlchemy/grok-bot-cli": "/tools/grok-bot-cli/",
    "https://github.com/adamanz/grok-bot-skill": "/tools/grok-bot-skill/",
    "https://github.com/smarzban/grokbot-tui": "/tools/grokbot-tui/",
    "https://github.com/diegocp01/grok_bot_usage_menu_bar": "/tools/usage-menu-bar/",
    "https://github.com/Nichokas/grokbot-linux-port": "/tools/linux-port/",
}

def tools_index():
    buckets = {
        "skills-plugins-mcp.json": 0,
        "open-source-alternatives.json": 0,
        "tutorials-guides.json": 0,
    }
    items = []
    for src in buckets:
        loaded = load(src)
        buckets[src] = len(loaded)
        extra = []
        if src == "open-source-alternatives.json":
            extra = ["Alternatives"]
        for it in loaded:
            tags = classify(it)
            for t in extra:
                if t not in tags:
                    tags.append(t)
            items.append({**it, "tags": tags})
    seen = set()
    uniq = []
    for it in items:
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        uniq.append(it)
    items = uniq
    tagset = []
    for it in items:
        for t in it["tags"]:
            if t not in tagset:
                tagset.append(t)
    btns = ['<button type="button" data-filter="all" aria-pressed="true">All %d</button>' % len(items)]
    for t in tagset:
        btns.append('<button type="button" data-filter="%s">%s</button>' % (escape(t), escape(t)))
    rows = []
    for it in items:
        tags = " ".join(it["tags"])
        extra = ""
        if it["url"] in DETAIL_URLS:
            extra = ' · <a href="%s">Site detail page</a>' % DETAIL_URLS[it["url"]]
        note = ""
        if "Related / easy to confuse" in it["tags"] or "grok-app" in (it.get("name") or "").lower():
            note = " Note: if this points at grok-app, that is a Grok Build GUI — not Grok Bot."
        rows.append(
            '<article class="tool-row" data-tags="%s"><h3>%s</h3><p>%s%s</p><p class="muted">%s · <a href="%s">Source</a>%s</p></article>'
            % (escape(tags), escape(it["name"]), escape(it["blurb"] or "See original"), note,
               escape(", ".join(it["tags"])), escape(it["url"]), extra)
        )
    js = """<script>
const filters=document.querySelector('[data-filters]');
const list=document.querySelector('[data-list]');
const search=document.querySelector('[data-search]');
let tag='all';
function apply(){
  const q=(search.value||'').toLowerCase();
  filters.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed', b.getAttribute('data-filter')===tag?'true':'false'));
  list.querySelectorAll('.tool-row').forEach(row=>{
    const tags=row.getAttribute('data-tags')||'';
    const okT = tag==='all' || tags.indexOf(tag)>=0;
    const okQ = !q || row.textContent.toLowerCase().includes(q);
    row.classList.toggle('hidden', !(okT && okQ));
  });
}
filters.addEventListener('click', e=>{ const b=e.target.closest('button'); if(!b) return; tag=b.getAttribute('data-filter'); apply(); });
search.addEventListener('input', apply);
</script>"""
    featured = [
        ("Compound Engineering", "https://github.com/EveryInc/compound-engineering-plugin", "Install in the Cursor marketplace. Grok Bot inherits it. Do not clone onto the Bot computer."),
        ("Grok Ship", "https://github.com/kunchenguid/grok-ship", "Scout vs ship. Crewmates drive Cursor cloud agents. Review before any PR."),
        ("Vercel plugin", "https://github.com/vercel/vercel-plugin", "Deployments, logs, domains. Official marketplace plugin Grok Bot can inherit."),
        ("gawkbot", "https://github.com/najmuzzaman-mohammad/gawkbot", "Local-first alternative. npx install. Not the official app."),
        ("OpenMausBot", "https://github.com/milind-soni/OpenMausBot", "Highest-star self-hosted roster plus a VM you run."),
        ("Official Linux packages", "/tools/linux-port/", "deb / rpm / AppImage from x.ai/bot first. Community port is fallback only."),
        ("grok-bot-cli", "/tools/grok-bot-cli/", "Terminal roster and messages. Reuses a signed-in macOS desktop session."),
    ]
    feat_html = []
    for name, url, blurb in featured:
        feat_html.append(
            '<a class="card nested" href="%s"><h3>%s</h3><p>%s</p></a>'
            % (escape(url), escape(name), escape(blurb))
        )
    return '''
<section class="band"><div class="wrap">
<p class="kicker">Catalog</p>
<h1>Grok Bot tools catalog</h1>
<p class="lede">Catalog from awesome-grok-bot plus later additions: %d entries — Skills/Plugins/MCP %d, Open-Source Alternatives %d, Tutorials &amp; Guides %d (CC0, fetched 2026-09-04). High-star self-hosted stacks are compared on <a href="/compare/">alternatives</a>. Each row keeps one-line job + source; check the original repo for license, maintenance, and permissions.</p>
<h2>Start with these seven</h2>
<div class="featured">%s</div>
<div class="callout warn"><p><strong>grok-app is not a Grok Bot client.</strong> <a href="https://github.com/RongleCat/grok-app">RongleCat/grok-app</a> is a desktop workbench (Tauri) for the local Grok Build CLI.</p></div>
<div class="filters" data-filters>%s</div>
<input class="search" data-search placeholder="Search tool name or job">
<div data-list>%s</div>
</div></section>
%s
''' % (
        len(items),
        buckets["skills-plugins-mcp.json"],
        buckets["open-source-alternatives.json"],
        buckets["tutorials-guides.json"],
        "".join(feat_html),
        "".join(btns),
        "".join(rows),
        js,
    )


def tool_detail(key):
    import json
    from html import escape
    data = json.loads((ROOT / "src/data/tool-details.json").read_text(encoding="utf-8"))
    d = data[key]
    parts = [
        '<section class="band"><div class="wrap prose">',
        '<p class="kicker">Third-party tool</p>',
        '<h1>%s</h1>' % escape(d["title"]),
        '<p class="meta"><a href="/tools/">Back to the third-party tools catalog</a></p>',
        '<h2>What job it does</h2>',
        '<p>%s</p>' % escape(d["job"]),
        '<h2>Platforms</h2>',
        '<p>%s</p>' % escape(d["platforms"]),
        '<h2>Install</h2>',
        '<p>%s</p>' % escape(d["install"]),
        '<h2>How it differs from the official app</h2>',
        '<p>%s</p>' % escape(d.get("differs") or ""),
    ]
    for sec in d.get("sections") or []:
        parts.append("<h2>%s</h2>" % escape(sec["h"]))
        parts.append("<p>%s</p>" % escape(sec["p"]))
    parts.extend([
        '<h2>Risks</h2>',
        '<div class="callout warn"><p>%s</p></div>' % escape(d["risk"]),
        '<h2>License and source</h2>',
        '<p><strong>License.</strong> %s</p>' % escape(d["license"]),
        '<p><a class="btn btn-primary" href="%s">Open GitHub source</a> <a class="btn btn-secondary" href="/learn/install/">Prefer official install</a> <a class="btn btn-ghost" href="/troubleshooting/">Symptom-based fixes</a></p>' % escape(d["source"]),
        '<p class="muted">Third-party tools can touch a local session. They do not replace Require Approval, secrets cards, or Recover/Update in the official desktop app.</p>',
        '</div></section>',
    ])
    return "".join(parts)
