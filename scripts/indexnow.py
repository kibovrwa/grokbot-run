# -*- coding: utf-8 -*-
"""IndexNow key + submit helpers. The key file is public by design."""
import json
import urllib.request
from htmlutil import ROOT, SITE, canonical
from refresh_site import SITEMAP_URLS

# 32 hex chars. Served at /{KEY}.txt
KEY = "7c4e9a2f18b0d6e35a91c8f4b2d07e16"


def key_path():
    return "/%s.txt" % KEY


def write_key_files():
    text = KEY + "\n"
    (ROOT / "public" / ("%s.txt" % KEY)).write_text(text, encoding="utf-8")
    dest = ROOT / "dist" / ("%s.txt" % KEY)
    dest.write_text(text, encoding="utf-8")
    return dest


def sitemap_urls():
    return [canonical(p) for p in SITEMAP_URLS]


def submit(urls=None):
    urls = urls or sitemap_urls()
    payload = {
        "host": "grokbot.run",
        "key": KEY,
        "keyLocation": SITE + key_path(),
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    endpoints = (
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow",
    )
    results = []
    for endpoint in endpoints:
        req = urllib.request.Request(
            endpoint,
            data=body,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                results.append((endpoint, resp.status, resp.read()[:200]))
        except Exception as e:
            code = getattr(e, "code", None)
            results.append((endpoint, code or str(e), getattr(e, "read", lambda: b"")()[:200]))
    return results


def ping_sitemaps():
    sitemap = SITE + "/sitemap.xml"
    pings = (
        "https://www.bing.com/ping?sitemap=" + sitemap,
        "https://www.google.com/ping?sitemap=" + sitemap,
    )
    out = []
    for url in pings:
        req = urllib.request.Request(url, headers={"User-Agent": "grokbot.run-handbook/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                out.append((url, resp.status))
        except Exception as e:
            out.append((url, getattr(e, "code", None) or str(e)))
    return out


if __name__ == "__main__":
    write_key_files()
    print("key file", SITE + key_path())
    for row in submit():
        print("indexnow", row[0], row[1], row[2])
    for row in ping_sitemaps():
        print("ping", row[0], row[1])
