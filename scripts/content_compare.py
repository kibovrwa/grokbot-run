# -*- coding: utf-8 -*-
from html import escape

COMPARE_FAQS = [
    ("Is there an official open-source Grok Bot?",
     "No. xAI’s Grok Bot is a managed app. OpenMausBot, rakazo, and gawkbot are independent projects that copy the teammate-plus-computer idea. They are not drop-in clients for your Cursor Grok Bot roster."),
    ("Is OpenClaw the same product?",
     "No. OpenClaw is a self-hosted agent framework you operate. Grok Bot is a finished app with one cloud computer provisioned for your account. Same fantasy, different operator."),
    ("Do alternatives use my Grok Bot weekly usage?",
     "No. Official usage is metered on the Cursor account for the official computer. Self-hosted stacks burn your own model keys or local CLIs. Do not expect the Cursor Grok Bot pool to pay for rakazo."),
    ("Should I start on an alternative to save money?",
     "Only if you want to be the operator. Setup, uptime, keys, and approvals are yours. If you need a first reversible job this week, install the official app and stay on one Bot."),
    ("Is this the same as Claude, Hermes, or ChatGPT agents?",
     "No. Claude cowork and ChatGPT scheduled tasks are session tools. Hermes is another named-bot host. None of them is a Cursor Grok Bot login. The GitHub search “grokbot github” usually means these self-hosted repos, not xAI source."),
]


def compare():
    faqs = []
    for q, a in COMPARE_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">Compare</p>
<h1>Grok Bot alternatives — official vs self-hosted</h1>
<p class="lede">Grok Bot is the managed xAI / Cursor product: named teammates on one shared cloud computer. OpenMausBot, rakazo, gawkbot, and OpenClaw chase the same job on infrastructure you run. They are not unofficial builds of the official app.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/install/">Stay official: install</a>
  <a class="btn btn-secondary" href="/pricing/">Plans and trial</a>
  <a class="btn btn-ghost" href="/use-cases/#open-source">GitHub cards</a>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Pick by who keeps the machine up</h2>
<p class="lede">Most “best alternatives” lists get one official fact wrong: Bots do not each get a private computer. The official computer is assigned to the user. This table uses that fact. Stars checked 2026-09-04. No invented prices.</p>
<div class="table-wrap compare-desktop">
<table>
<thead>
<tr><th></th><th>Official Grok Bot</th><th>OpenMausBot</th><th>rakazo</th><th>gawkbot</th><th>OpenClaw</th></tr>
</thead>
<tbody>
<tr><td>What it is</td><td>Finished app + managed cloud PC</td><td>Self-hosted roster + VM the bots can use</td><td>Self-hosted teammates, BYO model and sandbox</td><td>Local-first bots, npx install</td><td>Framework you assemble and host</td></tr>
<tr><td>Operator</td><td>xAI / Cursor</td><td>You</td><td>You</td><td>You</td><td>You</td></tr>
<tr><td>Computer</td><td>One shared cloud machine per account</td><td>VM or local machine you attach</td><td>Sandbox you choose</td><td>Local VM or a cloud option</td><td>Wherever you deploy it</td></tr>
<tr><td>Login</td><td>Cursor account only</td><td>Your existing CLI logins / keys</td><td>Your model keys</td><td>Your model keys</td><td>Your keys and host</td></tr>
<tr><td>Approval</td><td>Require Approval in the official app</td><td>Project-specific</td><td>Project-specific</td><td>Gate on every send</td><td>Whatever you wire</td></tr>
<tr><td>License / source</td><td>Closed product · <a href="https://x.ai/bot">x.ai/bot</a></td><td>Apache-2.0 · ~2.1k★</td><td>Apache-2.0 · ~1.9k★</td><td>Open repo · ~1.3k★</td><td>Open framework · not a Grok Bot client</td></tr>
</tbody>
</table>
</div>
<div class="compare-cards">
<article class="card"><h3>Official Grok Bot</h3><p>Finished app. One shared cloud PC per account. Cursor login. Require Approval in the app. Closed product — <a href="https://x.ai/bot">x.ai/bot</a>.</p></article>
<article class="card"><h3>OpenMausBot</h3><p>You operate it. Roster plus a VM you attach. BYO CLIs. Apache-2.0 · ~2.1k★.</p></article>
<article class="card"><h3>rakazo</h3><p>You operate it. BYO model and sandbox. Web, desktop, mobile. Apache-2.0 · ~1.9k★.</p></article>
<article class="card"><h3>gawkbot</h3><p>You operate it. Local-first, <code>npx gawkbot</code>, gate on every send. ~1.3k★.</p></article>
<article class="card"><h3>OpenClaw</h3><p>Framework you assemble. Not a Grok Bot client and not your official computer.</p></article>
</div>
</div></section>

<section class="band"><div class="wrap">
<div class="grid-2">
<article class="card">
<h3>Stay on official Grok Bot when</h3>
<p>You want phone + desktop on one roster, routines while the laptop is closed, and someone else to Recover the computer. Start with <a href="/learn/install/">install</a>, one job on <a href="/use-cases/">use cases</a>, and the <a href="/pricing/">dated plan snapshot</a>.</p>
</article>
<article class="card">
<h3>Look at self-host when</h3>
<p>You already run model keys or local CLIs, you need the machine on your network, or you refuse a managed VM. Read the repo README before any credential. Full list: <a href="/tools/">tools catalog</a>.</p>
</article>
</div>
<div class="callout warn">
<p><strong>Do not install a reconstructed official client.</strong> Archived TypeScript rebuilds of Grok Bot 0.18 are study artifacts, not a supported alternative. This page also skips grok.com prompt dumps — that is a different product.</p>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>The four names people actually mean</h2>
<div class="grid-2">
<a class="card" href="https://github.com/milind-soni/OpenMausBot"><h3>OpenMausBot · 2.1k★</h3><p>Highest-star self-hosted take: named bots plus a VM. BYO claude / codex / grok CLIs. Not affiliated with xAI.</p></a>
<a class="card" href="https://github.com/elie222/rakazo"><h3>rakazo · 1.9k★</h3><p>Bring your own model and sandbox. Web, desktop, mobile. Closest “always-on teammate” copy that is not a client clone.</p></a>
<a class="card" href="https://github.com/najmuzzaman-mohammad/gawkbot"><h3>gawkbot · 1.3k★</h3><p>Local-first. <code>npx gawkbot</code>. Approval gate on every send. Useful if you want the idea on your laptop first.</p></a>
<a class="card" href="/learn/what-is-grok-bot/"><h3>OpenClaw and chat agents</h3><p>OpenClaw is a framework. ChatGPT / Claude cowork are session tools. None of them is a Grok Bot login, and none shares your official computer.</p></a>
</div>
<p class="lede">Companion repos that keep the official app: <a href="https://github.com/OnlyTerp/opengrok">opengrok</a> (model picker inside the official client), <a href="https://github.com/xai-org/plugin-marketplace">xAI plugin marketplace</a>, <a href="/use-cases/#skills">skills worth installing</a>.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>FAQ</h2>
<div class="faq card">%s</div>
<p class="muted">Reviews this site used as contrast, not as a reprint: MindStudio, Eigent, Vellum, and the field notes on <a href="/sources/">Sources</a>.</p>
</div></section>
''' % "".join(faqs), COMPARE_FAQS
