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
    ("What is Dots?",
     "OpenAI’s 29 September 2026 safety appendix calls dots always-on agents powered by GPT-6 Astra. Each dot has its own cloud computer and browser, uses connected tools, and follows up across ChatGPT, text message, email, and Slack."),
    ("How do you use a Dot?",
     "9to5Google says you create the Dot in the ChatGPT desktop app and can then use mobile. TechCrunch says it can be launched from Codex or ChatGPT. CNBC says you name one primary dot and message it in ChatGPT, Slack, or Teams. Plan, region, and price are on the pricing note."),
    ("Where are the other notes?",
     "Pricing, release date, download, waitlist, Dots versus Grok Bot, Dots versus Muse, alternatives, and a shorter FAQ each have their own page, linked under More notes."),
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
<p class="kicker">Unofficial notes · 29 September 2026</p>
<h1>What is Dots, OpenAI's always-on agent</h1>
<p class="lede">Dots is the always-on agent OpenAI launched at DevDay on 29 September 2026. It runs on GPT-6 Astra and has its own cloud computer. This page is not an OpenAI site and does not use OpenAI marks.</p>
<div class="callout warn">
<p><strong>Unofficial information page.</strong> Not affiliated with, endorsed by, or operated by OpenAI. Sentences below follow the linked sources. A detail those sources do not state is left out.</p>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>What OpenAI says it is</h2>
<p>OpenAI’s <a href="https://deploymentsafety.openai.com/gpt-6-astra/alignment-for-dots">GPT-6 Astra deployment safety appendix</a>, updated 29 September 2026, says it is launching dots as always-on agents built on existing model and agent capabilities and powered by GPT-6 Astra. The same section says each dot has its own cloud computer and browser, uses connected tools, handles recurring work, and follows up across ChatGPT, text message, email, and Slack, often by delegating work to subagents. It also describes a time-budget setting for how long a dot works, and extra checks aimed at proactive, long-running work.</p>
<p><a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC’s DevDay live blog</a> reports that Sam Altman, in the San Francisco keynote, described Dots as remarkably capable always-on agents and as a new form factor for work. CNBC also reports that people start with one primary dot, give it a name, and customize it, and that OpenAI expects teams of dots later. <a href="https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor">The Verge</a> describes the launch as OpenAI’s response to Meta’s Muse.</p>
<p>CNBC, The Verge, and <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> report that OpenAI said Dots can connect to more than 4,000 apps through plugins, learn from feedback, and keep working toward goals. 9to5Google, quoting OpenAI, adds that a dot can do read-only “proactive research” on connected tools when it is not on an assigned task, and that you can open its cloud computer while it works.</p>
<p>If you meant the xAI app on this site, that is a different product: <a href="/learn/what-is-grok-bot/">what Grok Bot is</a>.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>How to use a Dot</h2>
<p>The sources do not publish a click-by-click setup. They do agree on the doors that exist on launch day.</p>
<ol>
<li><strong>Plan and market.</strong> Who can open a Dot, and whether that is an extra charge, is on the <a href="/dots-pricing/">pricing note</a>. The calendar date is on the <a href="/dots-release-date/">release note</a>.</li>
<li><strong>Where you create it.</strong> <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> says a Dot is created in the ChatGPT desktop app and can then be used on mobile. <a href="https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/">TechCrunch</a> says people can launch Dots from Codex or ChatGPT. <a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a> says you name one primary dot. There is no separate installer in those reports; see <a href="/dots-download/">download</a>.</li>
<li><strong>Where you talk to it.</strong> CNBC says you can message it in ChatGPT, Slack, and Microsoft Teams. 9to5Google and <a href="https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor">The Verge</a> also describe a voice call from ChatGPT. Texting is a different sentence in each report; the <a href="/dots-waitlist/">waitlist note</a> keeps those sentences together.</li>
<li><strong>Watching it work.</strong> 9to5Google says you can view the dot’s cloud computer during a task and can grant access to your own computer. The Verge says you and colleagues can also work with a dot in ChatGPT Space. <a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">WIRED</a> says Dots are designed to ask before sensitive actions such as installing software or changing a password, and that Custom Rules can require permission. The Next Web says changing a password stays with the user, and that saved-password sign-in is not shown to the model.</li>
</ol>
<p>OpenAI’s safety appendix is the long public note on prompt-injection testing, confirmation policy, and monitors for this setup. This page does not restate those tables.</p>
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
<li><a href="/muse/">What Muse is</a></li>
</ul>
<p class="muted">Related on this site: <a href="/learn/what-is-grok-bot/">What Grok Bot is</a> · <a href="/compare/">Grok Bot alternatives</a> · <a href="/">Grok Bot guide</a></p>
</div></section>
''' % (_faqs(DOTS_FAQS), _sources())
