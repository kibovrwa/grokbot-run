# -*- coding: utf-8 -*-
from html import escape
import json
from pathlib import Path
from htmlutil import ROOT

def _items(path, title_key):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    out = []
    for x in data:
        title = x.get(title_key) or x.get("name") or x.get("title") or ""
        note = x.get("one_line") or x.get("blurb") or ""
        out.append(
            '<li class="source-item"><a href="%s">%s</a><span class="source-note">%s</span></li>'
            % (escape(x["url"], quote=True), escape(title), escape(note))
        )
    return "".join(out), len(data)

def sources():
    official_html, n_off = _items("/workspace/playbook-data/official.json", "name")
    fail_html, n_fail = _items("/workspace/playbook-data/failures.json", "title")
    return """
<section class="band"><div class="wrap">
<p class="kicker">Bibliography</p>
<h1>Sources and fetch notes</h1>
<p class="lede">Fetch window 2026-09-04. Facts sit in three layers: official materials, community failure threads, and third-party catalogs plus field cases. When official docs conflict on eligibility, this site shows both links and does not adjudicate.</p>
<div class="grid-3">
<article class="card"><h3>Official materials · %d</h3><p>xAI / Cursor Help / official repos and app entry points that back hard facts on install, computer, plugins, and usage.</p></article>
<article class="card"><h3>Failure sources · %d</h3><p>Forum field reports and staff replies used for symptom grouping; one thread is not a guarantee it reproduces on every device.</p></article>
<article class="card"><h3>Catalog and cases</h3><p>199 tools, plus Field Cases. This site writes original short summaries only — no third-party body text copied.</p></article>
</div>
<section class="source-section">
<h2>Official materials (%d)</h2>
<ul class="source-list">%s</ul>
</section>
<section class="source-section">
<h2>Community failure sources (%d)</h2>
<ul class="source-list">%s</ul>
</section>
<section class="source-section prose">
<h2>Fetch failures or full text not opened</h2>
<ul>
<li><a href="https://www.datacamp.com/tutorial/grok-bot-tutorial">DataCamp tutorial</a> timed out on full text. Used search summary + awesome one-liner and linked back.</li>
<li><a href="https://x.ai/news/introducing-grok-bot">Introducing Grok Bot</a> timed out once; launch date 2026-08-11 comes from awesome plus opened secondary accounts; the entry remains in the official list for cross-check.</li>
<li><a href="https://docs.x.ai/grok-bot/use-cases">Official use-cases</a> opened on 2026-09-04. Starter jobs on this site follow that page’s read-and-prepare pattern; they are not a reprint.</li>
<li>Some raw READMEs timed out; used GitHub repo-page summaries instead.</li>
</ul>
<p>Per-URL Field Cases and failure modes also appear on <a href="/use-cases/">Cases</a> and <a href="/troubleshooting/">Fixes</a>. Upstream list: <a href="https://github.com/RongleCat/awesome-grok-bot">awesome-grok-bot</a> (CC0).</p>
</section>
</div></section>
""" % (n_off, n_fail, n_off, official_html, n_fail, fail_html)
