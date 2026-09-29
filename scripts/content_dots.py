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
     "CNBC says the rollout is inside ChatGPT for Pro and Business Premium users in eligible markets, and for Enterprise, Edu, and Healthcare after an admin enables it. 9to5Google says you create the Dot in the ChatGPT desktop app and can then use mobile. TechCrunch says it can be launched from Codex or ChatGPT. CNBC also says you start with one primary dot, name it, and message it in ChatGPT, Slack, or Teams."),
    ("Is there a Dots app or download?",
     "The sources linked on this page do not describe a separate Dots listing in an app store. They describe Dots inside ChatGPT, plus Slack and Microsoft Teams."),
    ("Is there a separate Dots price?",
     "OpenAI has not published a separate Dots price in the sources linked here. The Next Web, citing OpenAI, says the first Dot is included in Pro and Business Premium at no extra cost. WIRED describes the rollout as starting on ChatGPT Pro and states that tier’s price as $100 a month. Those are press descriptions, not an OpenAI price sheet."),
    ("When was Dots announced?",
     "CNBC, The Verge, TechCrunch, WIRED, and 9to5Google date the announcement to OpenAI DevDay on 29 September 2026 in San Francisco. OpenAI’s safety appendix is dated the same day."),
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
<li><strong>Plan and market.</strong> <a href="https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html">CNBC</a> and <a href="https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/">TechCrunch</a> say Dots is rolling out in ChatGPT for Pro and Business Premium users in eligible markets. Enterprise, including Edu and Healthcare, can try it when a workspace admin enables it. <a href="https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday">The Next Web</a>, citing an OpenAI statement, says Business Premium includes Dots in all supported ChatGPT regions, and that Pro does not currently include the European Economic Area, Switzerland, or the UK.</li>
<li><strong>Where you create it.</strong> <a href="https://9to5google.com/2026/09/29/openai-dots-agent/">9to5Google</a> says a Dot is created in the ChatGPT desktop app and can then be used on mobile. TechCrunch says people can launch Dots from Codex or ChatGPT. CNBC says you name one primary dot.</li>
<li><strong>Where you talk to it.</strong> CNBC says you can message it in ChatGPT, Slack, and Microsoft Teams, and that texting is coming soon. 9to5Google and The Verge also describe a voice call from ChatGPT. OpenAI’s safety appendix lists follow-ups across ChatGPT, text message, email, and Slack. <a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">WIRED</a> says Pro users can join a waitlist to text a Dot over iMessage or RCS on Android. Those three accounts are not the same sentence; each is linked.</li>
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
<p class="muted">Related on this site: <a href="/learn/what-is-grok-bot/">What Grok Bot is</a> · <a href="/compare/">Grok Bot alternatives</a> · <a href="/">Grok Bot guide</a></p>
</div></section>
''' % (_faqs(DOTS_FAQS), _sources())
