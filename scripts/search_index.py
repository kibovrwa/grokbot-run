# -*- coding: utf-8 -*-
"""Build a compact lookup index: titles, H2-style labels, symptoms, tool names."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmlutil import ROOT, SITE
from seo_pages import PAGES
from content_hub import GLOSSARY
from content_trouble import GROUPS
from content_cases import JOBS
from content_tools import DETAIL_URLS, load


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:48] or "term"


def _add(items, title, href, kind, *keys):
    blob = " ".join(x for x in (title, kind) + keys if x)
    items.append({
        "t": title,
        "h": href,
        "k": kind,
        "q": blob.lower(),
    })


def build():
    items = []
    for path, meta in PAGES.items():
        extra = " ".join(filter(None, [
            meta.get("primary", ""),
            meta.get("also", ""),
            meta.get("h1", ""),
        ]))
        _add(items, meta["title"], path, "Page", meta.get("description", ""), extra)

    aliases = (
        ("Can't reach your computer", "/troubleshooting/cant-reach/", "Help", "reconnecting black screen blank cursorvm dns vpn"),
        ("Reset vs Recover vs Update", "/troubleshooting/recover-vs-reset/", "Help", "cleaning up 50% starting last resort"),
        ("Weekly usage and On-Demand", "/troubleshooting/not-responding/", "Help", "trial burns spillover bot to bot silent"),
        ("Plugin OAuth (Zoom Gmail Notion X GitHub)", "/troubleshooting/#oauth", "Help", "zoom 4700 tools=0 bearer token"),
        ("Linux and local execution", "/troubleshooting/#linux", "Help", "deb rpm appimage stdio mcp"),
        ("White or black screen", "/troubleshooting/white-screen/", "Help", "empty roster setting up free plan"),
        ("After week one", "/learn/operator/", "Guide", "chief of staff roster mega-chat what's-left"),
        ("X, Cursor, MCP, cloud computer", "/learn/ops/", "Guide", "twitter x plugin cloud agent remote mcp"),
        ("Cloud Agent handoff", "/learn/ops/", "Guide", "cursor cloud agent pull request github"),
        ("Official X plugin", "/learn/ops/", "Guide", "twitter scout mentions research database"),
        ("Grok Bot Mac download", "/learn/mac-download/", "Download", "grokbot mac download apple silicon intel"),
        ("Grok Bot Windows download", "/learn/windows-download/", "Download", "grokbot windows install x64 arm64"),
        ("Grok Bot not responding", "/troubleshooting/not-responding/", "Help", "stopped working silent bots failed to respond"),
        ("Grok Bot stuck", "/troubleshooting/stuck/", "Help", "connecting setting up reconnecting cleaning up"),
    )
    for title, href, kind, keys in aliases:
        _add(items, title, href, kind, keys)

    for g in GROUPS:
        _add(items, g["title"], "/troubleshooting/#%s" % g["id"], "Help", g["symptom"])

    for term, blurb in GLOSSARY:
        _add(items, term, "/learn/glossary/#%s" % slug(term), "Term", blurb)

    for job in JOBS:
        _add(items, job["name"], "/use-cases/#job-%s" % job["id"], "Job", job.get("tag", ""), job.get("owns", ""))

    seen = set()
    for src in ("skills-plugins-mcp.json", "open-source-alternatives.json", "tutorials-guides.json"):
        for it in load(src):
            name = it.get("name") or ""
            url = it.get("url") or ""
            if not name or name in seen:
                continue
            seen.add(name)
            href = DETAIL_URLS.get(url) or ("/tools/?q=" + quote(name, safe=""))
            _add(items, name, href, "Tool", it.get("blurb") or "")

    return items


def write_index():
    items = build()
    text = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    for dest in (ROOT / "public" / "search.json", ROOT / "dist" / "search.json"):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text + "\n", encoding="utf-8")
    return len(items)


if __name__ == "__main__":
    print("search.json", write_index(), "rows")
