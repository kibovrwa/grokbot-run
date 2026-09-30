# -*- coding: utf-8 -*-
"""Unofficial Dots notes. Every claim maps to a link in SOURCES."""
from html import escape

# Checked 2026-09-30 against the pages linked below.
# Not written: a separate Dots price sheet, a public app-store listing,
# a general signup waitlist, an agent named Alfred, or any OpenAI mark.

SOURCES = [
    ("OpenAI, GPT-6 Astra deployment safety appendix, section 12 (29 September 2026)",
     "https://deploymentsafety.openai.com/gpt-6-astra/alignment-for-dots"),
    ("CNBC, DevDay 2026 live updates (29 September 2026)",
     "https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html"),
    ("The Verge (29 September 2026)",
     "https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor"),
    ("9to5Google (29 September 2026)",
     "https://9to5google.com/2026/09/29/openai-dots-agent/"),
    ("TechCrunch (29 September 2026)",
     "https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/"),
    ("WIRED (29 September 2026)",
     "https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/"),
    ("The Next Web (29 September 2026)",
     "https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday"),
]

DOTS_FAQS = [
    ("What are OpenAI dots?",
     "OpenAI’s 29 September 2026 safety appendix calls them always-on agents powered by GPT-6 Astra. Each dot has its own cloud computer and browser. CNBC, The Verge, and 9to5Google report that OpenAI said they can connect to more than 4,000 apps, and that eligible ChatGPT Pro and Business Premium users get them first."),
    ("How do I turn on ChatGPT dots?",
     "9to5Google says you create the dot in the ChatGPT desktop app and can then use mobile. TechCrunch says you can also launch it from Codex or ChatGPT. CNBC says you name one primary dot and message it in ChatGPT, Slack, or Teams. A click-by-click setup is not officially announced."),
    ("Is there a separate OpenAI dots price?",
     "Not officially announced. The Next Web, citing OpenAI, says the first dot is included in Pro and Business Premium at no extra cost. This page does not repeat conflicting dollar figures from the press."),
    ("Are OpenAI dots the same as Grok Bot or Muse?",
     "No. Grok Bot is xAI’s teammate app. Muse is Meta’s personal agent. The short comparisons are on this page; the longer tables are linked."),
]


def _sources():
    items = []
    for label, url in SOURCES:
        items.append('<li><a href="%s">%s</a></li>' % (escape(url), escape(label)))
    return "<ul>\n%s\n</ul>" % "\n".join(items)


def _faqs(pairs):
    bits = []
    for q, a in pairs:
        bits.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return "\n".join(bits)


def dots():
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">Unofficial notes · not an OpenAI page</p>
<h1>OpenAI dots: how to turn one on, and how it differs</h1>
<p class="lede">OpenAI dots are the always-on agents announced at DevDay on 29 September 2026. Same-day news already covers the launch. This page is the part those stories skip: who can turn one on, what is not officially announced, and how it differs from Grok Bot and Muse.</p>
<div class="callout warn">
<p><strong>Unofficial information page.</strong> Not affiliated with, endorsed by, or operated by OpenAI. No OpenAI mark is used. Where a company has not stated a fact, this page says not officially announced.</p>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Which dots this is</h2>
<p>OpenAI’s <a href="https://deploymentsafety.openai.com/gpt-6-astra/alignment-for-dots">safety appendix</a> that day calls them always-on agents powered by GPT-6 Astra, each with its own cloud computer and browser. <a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a>, <a href="https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor">The Verge</a>, and <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> report that OpenAI said they connect to more than 4,000 apps and roll out first to ChatGPT Pro and Business Premium in eligible markets.</p>
<p>This is not <a href="https://studio.dots.ai/">Xiaohongshu’s dots studio</a>, not the <a href="https://en.wikipedia.org/wiki/Dots_(video_game)">Playdots mobile game</a> that shut down on 25 March 2023, and not <a href="https://the-dots.com/legal/terms">The Dots</a> professional network.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>How to turn on ChatGPT dots</h2>
<p>A button-by-button setup is not officially announced. The launch reports agree on these doors.</p>
<ol>
<li><strong>Check the plan.</strong> Eligibility is in the next section. If the plan is not on that list, a way in is not officially announced.</li>
<li><strong>Create it in ChatGPT.</strong> <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> says the first create is in the ChatGPT desktop app, then mobile works. <a href="https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/">TechCrunch</a> says people launch it from Codex or ChatGPT. <a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a> says you name one primary dot. A separate app download is not officially announced; see <a href="/dots-download/">download</a>.</li>
<li><strong>Talk to it where it already lives.</strong> CNBC says ChatGPT, Slack, and Microsoft Teams. 9to5Google and The Verge also describe a voice call from ChatGPT. Texting is not the same sentence in every report; see <a href="/dots-waitlist/">waitlist</a>.</li>
<li><strong>Watch the cloud computer.</strong> 9to5Google says you can open it during a task. <a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">WIRED</a> says it asks before sensitive actions such as installing software or changing a password.</li>
</ol>
</div></section>

<section class="band"><div class="wrap">
<h2>Price and who qualifies</h2>
<p><a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a> and <a href="https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/">TechCrunch</a> say the rollout is ChatGPT Pro and Business Premium in eligible markets. Enterprise, including Edu and Healthcare, can try it when a workspace admin enables it. <a href="https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday">The Next Web</a>, citing OpenAI, says Business Premium includes it in all supported ChatGPT regions, and that Pro does not currently include the European Economic Area, Switzerland, or the UK.</p>
<p>The same Next Web report says the first dot is included in those plans at no extra cost. A separate OpenAI dots price is not officially announced. Press accounts of the Pro plan’s dollar amount do not agree, so no dollar figure is repeated here. The longer note is <a href="/dots-pricing/">Dots pricing</a>. The date is <a href="/dots-release-date/">29 September 2026</a>.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>OpenAI dots vs Grok Bot</h2>
<p>OpenAI’s Dots sources do not name Grok Bot. <a href="https://x.ai/bot">x.ai/bot</a> is a different company’s app. The longer table is <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</p>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>OpenAI dots</th><th>Grok Bot</th></tr></thead>
<tbody>
<tr><td>Company</td><td>OpenAI</td><td>xAI</td></tr>
<tr><td>Computer</td><td>Each dot has its own cloud computer and browser, in OpenAI’s appendix.</td><td>x.ai/bot says Bots have their own computer and keep working with the laptop closed.</td></tr>
<tr><td>Where you talk</td><td>ChatGPT, Slack, Teams.</td><td>Desktop and iOS, on x.ai/bot.</td></tr>
<tr><td>How many</td><td>One primary dot now. Teams of dots are a later plan, per CNBC.</td><td>x.ai/bot says many Bots at once.</td></tr>
<tr><td>Price</td><td>Separate price: not officially announced.</td><td>Not copied here. See <a href="/pricing/">Grok Bot pricing</a>.</td></tr>
</tbody>
</table>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>OpenAI dots vs Muse</h2>
<p><a href="https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor">The Verge</a> describes the launch as OpenAI’s answer to Muse. Meta’s own posts do not name dots. The longer table is <a href="/dots-vs-muse/">Dots vs Muse</a>.</p>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>OpenAI dots</th><th>Muse</th></tr></thead>
<tbody>
<tr><td>Company</td><td>OpenAI, 29 September 2026</td><td>Meta, <a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">8 September 2026</a></td></tr>
<tr><td>Computer</td><td>Each dot’s cloud computer and browser</td><td>Muse Secure VM, its own browser</td></tr>
<tr><td>Where you talk</td><td>ChatGPT, Slack, Teams</td><td>Muse app, WhatsApp, muse.ai</td></tr>
<tr><td>Who gets it</td><td>Pro and Business Premium in eligible markets</td><td>Meta’s later post says the US and Canada</td></tr>
<tr><td>Price</td><td>Separate price: not officially announced</td><td>Free for most needs, plus subscriptions. Dollars: not officially announced</td></tr>
</tbody>
</table>
</div>
</div></section>

<section class="band" id="field-setup"><div class="wrap">
<h2>Field setup</h2>
<p>The tables above are the choice. If the work already sits in ChatGPT, Slack, or Teams, the published door is OpenAI dots. If it already sits in the xAI app, the published door is Grok Bot. If it already sits in the Muse app or WhatsApp, the published door is Muse. A ranking is not officially announced. Dollars stay on <a href="/dots-pricing/">pricing</a>.</p>
<p>OpenAI’s appendix puts each dot on its own cloud computer. Running that dot on hardware you own is not officially announced. <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> says you can still grant it access to your computer. Grok Bot’s helper on your machine is a different product: <a href="/troubleshooting/local-computer/">local computer not connected</a>.</p>
<p>No launch source describes a shared login, a shared computer, or an import from Grok Bot or Muse. That bridge is not officially announced. A Grok Bot first job stays on <a href="/learn/first-bot/">its own lesson</a>.</p>
<p>If mobile shows nothing, <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a>’s order is desktop create first. An installer is not officially announced.</p>
<p>Official starter prompt: not officially announced. The block below only restates two published constraints. It is not an OpenAI template.</p>
<pre><code id="dot-brief">One primary dot.
Name:
Job:
Ask before you install software or change a password.</code></pre>
<button type="button" class="copy-btn" data-copy-target="dot-brief">Copy</button>
<p class="muted">Name and “one primary dot” are from <a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a>. The ask-first line is from <a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">WIRED</a> (install software, change a password).</p>
</div></section>

<section class="band"><div class="wrap">
<h2>Questions people ask first</h2>
<div class="faq card">
%s
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Sources checked 30 September 2026</h2>
<p>Press links are launch-day reports. The deployment-safety appendix is OpenAI’s own text. No OpenAI logo is used here.</p>
%s
<h2>More notes</h2>
<ul>
<li><a href="/dots-pricing/">Dots pricing</a></li>
<li><a href="/dots-release-date/">Dots release date</a></li>
<li><a href="/dots-download/">Dots download and app</a></li>
<li><a href="/dots-waitlist/">Dots waitlist</a></li>
<li><a href="/dots-vs-grokbot/">Dots vs Grok Bot</a></li>
<li><a href="/dots-vs-muse/">Dots vs Muse</a></li>
<li><a href="/dots-alternatives/">Dots alternatives</a></li>
<li><a href="/dots-faq/">Dots FAQ</a></li>
<li><a href="/dots-security-privacy/">Dots security and privacy</a></li>
<li><a href="/dots-vs-chatgpt/">Dots vs ChatGPT and Claude</a></li>
<li><a href="/how-to-get-openai-dots/">How to get OpenAI dots</a></li>
<li><a href="/muse/">What Muse is</a></li>
</ul>
<p class="muted">Related on this site: <a href="/learn/what-is-grok-bot/">What Grok Bot is</a> · <a href="/compare/">Grok Bot alternatives</a> · <a href="/">Grok Bot guide</a></p>
</div></section>
''' % (_faqs(DOTS_FAQS), _sources())
