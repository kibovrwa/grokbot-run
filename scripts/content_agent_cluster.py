# -*- coding: utf-8 -*-
"""Sibling notes for Dots and Muse. Facts stay on the page that owns them."""
from html import escape

OPENAI = "https://deploymentsafety.openai.com/gpt-6-astra/alignment-for-dots"
CNBC = "https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html"
VERGE = "https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor"
NINE = "https://9to5google.com/2026/09/29/openai-dots-agent/"
TC_DOTS = "https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/"
WIRED = "https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/"
TNW = "https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday"
XAI = "https://x.ai/bot"
MUSE = "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/"
MUSE_BIZ = "https://about.fb.com/news/2026/09/introducing-muse-small-business/"
TC_MUSE = "https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/"

DISCLAIMER = (
    '<div class="callout warn"><p><strong>Unofficial information page.</strong> '
    "Not an OpenAI or Meta site, not endorsed by either company, and not using their marks. "
    "A cell says “Not published” when the linked sources do not state it.</p></div>"
)


def _faq(pairs):
    return "\n".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (escape(q), a)
        for q, a in pairs
    )


def _links(rows):
    return "<ul>\n" + "\n".join(
        '<li><a href="%s">%s</a></li>' % (escape(url), escape(label)) for label, url in rows
    ) + "\n</ul>"


def _page(kicker, h1, lede, body, faqs, sources):
    faq_html = ""
    if faqs:
        faq_html = '<section class="band"><div class="wrap"><h2>FAQ</h2><div class="faq card">%s</div></div></section>' % _faq(faqs)
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">%s</p>
<h1>%s</h1>
<p class="lede">%s</p>
%s
</div></section>
%s
<section class="band"><div class="wrap">
<h2>Sources</h2>
%s
<p class="muted"><a href="/dots/">What Dots is</a> · <a href="/muse/">What Muse is</a> · <a href="/learn/what-is-grok-bot/">What Grok Bot is</a></p>
</div></section>
''' % (kicker, escape(h1) if False else h1, lede, DISCLAIMER, body + faq_html, _links(sources))


def _shell(kicker, h1, lede, inner, faqs, sources):
    # h1 and lede are trusted HTML-free strings written in this file.
    return _page(kicker, escape(h1), lede, inner, faqs, sources)


# --- pricing ---

PRICING_FAQS = [
    ("Is there a separate Dots price?",
     "Not published. <a href=\"%s\">The Next Web</a>, citing OpenAI, says the first Dot is included in ChatGPT Pro and Business Premium at no extra cost. No OpenAI price sheet for a Dots add-on appears in the sources linked here." % TNW),
    ("What dollar figure is in the press?",
     "<a href=\"%s\">WIRED</a> says the rollout starts on ChatGPT Pro and states that tier as $100 a month. That sentence is WIRED’s description of the Pro plan, not a Dots price list. Business Premium’s dollar price is not published on this page." % WIRED),
    ("Do Dot chats count toward ChatGPT limits?",
     "<a href=\"%s\">The Verge</a>, citing OpenAI, says conversations with a Dot do not count toward ChatGPT usage limits. <a href=\"%s\">The Next Web</a> adds that tasks a Dot starts in Codex or ChatGPT Work do count." % (VERGE, TNW)),
]


def dots_pricing():
    inner = '''
<section class="band"><div class="wrap">
<h2>What the launch reports say about paying</h2>
<p><a href="%s">The Next Web</a> says OpenAI told the press that the first Dot is included in Pro and Business Premium at no extra cost. <a href="%s">CNBC</a> and <a href="%s">TechCrunch</a> say the rollout is those two plans, in eligible markets, plus Enterprise, Edu, and Healthcare after a workspace admin enables it.</p>
<p><a href="%s">The Next Web</a>, citing OpenAI, says Business Premium includes Dots in all supported ChatGPT regions, and that Pro does not currently include the European Economic Area, Switzerland, or the UK.</p>
<p><a href="%s">The Verge</a> quotes OpenAI that, later, people will be able to add more dots and scale a dot’s speed or how much work it takes on per month. No price for that extra capacity is in the quote.</p>
<p>Not published: a standalone Dots subscription, a public price for a second Dot, and a Business Premium dollar amount.</p>
<p>How you reach a Dot after you have access is on <a href="/dots/">what Dots is</a>.</p>
</div></section>
''' % (TNW, CNBC, TC_DOTS, TNW, VERGE)
    sources = [
        ("The Next Web, 29 September 2026", TNW),
        ("CNBC DevDay live blog, 29 September 2026", CNBC),
        ("TechCrunch, 29 September 2026", TC_DOTS),
        ("The Verge, 29 September 2026", VERGE),
        ("WIRED, 29 September 2026", WIRED),
    ]
    return _shell(
        "Unofficial notes · pricing",
        "Dots pricing: no separate price is published",
        "Launch reports describe Dots as included with existing ChatGPT plans. They do not publish a Dots price sheet.",
        inner, PRICING_FAQS, sources,
    ), PRICING_FAQS


# --- release date ---

RELEASE_FAQS = [
    ("When did OpenAI announce Dots?",
     "29 September 2026, at DevDay in San Francisco. <a href=\"%s\">CNBC</a>, <a href=\"%s\">The Verge</a>, <a href=\"%s\">TechCrunch</a>, <a href=\"%s\">WIRED</a>, and <a href=\"%s\">9to5Google</a> use that date. OpenAI’s <a href=\"%s\">safety appendix</a> is dated the same day." % (CNBC, VERGE, TC_DOTS, WIRED, NINE, OPENAI)),
    ("Did it ship the same day?",
     "Those reports describe a rollout starting that day inside ChatGPT, not a separate app release. Who is included is on the <a href=\"/dots-pricing/\">pricing note</a>."),
]


def dots_release():
    inner = '''
<section class="band"><div class="wrap">
<h2>The date the sources use</h2>
<p>OpenAI’s <a href="%s">deployment safety appendix</a> says, on 29 September 2026, that it is launching dots. <a href="%s">CNBC</a> places the keynote that day in San Francisco. The Verge, TechCrunch, WIRED, and 9to5Google use the same day.</p>
<p><a href="%s">The Next Web</a> also says OpenAI released the GPT-6 Astra model on 3 September 2026. That is the model date in that report, not a second Dots launch date. The appendix says Dots are powered by GPT-6 Astra.</p>
<p>Not published in these sources: a minute-by-minute keynote clock, and a date when every ChatGPT plan receives a Dot.</p>
</div></section>
''' % (OPENAI, CNBC, TNW)
    sources = [
        ("OpenAI safety appendix, 29 September 2026", OPENAI),
        ("CNBC, 29 September 2026", CNBC),
        ("The Verge, 29 September 2026", VERGE),
        ("TechCrunch, 29 September 2026", TC_DOTS),
        ("The Next Web, 29 September 2026", TNW),
    ]
    return _shell(
        "Unofficial notes · date",
        "Dots release date: 29 September 2026",
        "OpenAI’s own safety appendix and the launch-day reports use 29 September 2026, DevDay, San Francisco.",
        inner, RELEASE_FAQS, sources,
    ), RELEASE_FAQS


# --- download ---

DOWNLOAD_FAQS = [
    ("Is there a Dots app to download?",
     "Not published. <a href=\"%s\">CNBC</a> describes messaging inside ChatGPT, Slack, and Microsoft Teams. <a href=\"%s\">9to5Google</a> says you create the Dot in the ChatGPT desktop app, then use mobile. No app-store listing is named." % (CNBC, NINE)),
    ("Can it be opened from Codex?",
     "<a href=\"%s\">TechCrunch</a> says people can launch Dots from Codex or ChatGPT." % TC_DOTS),
]


def dots_download():
    inner = '''
<section class="band"><div class="wrap">
<h2>Where the reports put the product</h2>
<p>The linked launch reports do not give a Dots installer, an App Store page, or a Play Store page. They put the product inside ChatGPT.</p>
<p><a href="%s">9to5Google</a> says creation happens in the ChatGPT desktop app, and that mobile works after that. <a href="%s">TechCrunch</a> says launch is from Codex or ChatGPT. <a href="%s">The Verge</a> says you can talk to a Dot from ChatGPT on the web, desktop, or mobile, and also from Slack and Teams.</p>
<p>Not published: a direct download URL for a Dots application.</p>
<p>Steps after it is open are on <a href="/dots/">what Dots is</a>.</p>
</div></section>
''' % (NINE, TC_DOTS, VERGE)
    sources = [
        ("9to5Google, 29 September 2026", NINE),
        ("TechCrunch, 29 September 2026", TC_DOTS),
        ("The Verge, 29 September 2026", VERGE),
        ("CNBC, 29 September 2026", CNBC),
    ]
    return _shell(
        "Unofficial notes · download",
        "Dots download: no separate app is published",
        "Launch reports describe Dots inside ChatGPT, Slack, and Teams. They do not name a Dots store listing.",
        inner, DOWNLOAD_FAQS, sources,
    ), DOWNLOAD_FAQS


# --- waitlist ---

WAITLIST_FAQS = [
    ("Is there a waitlist to get Dots?",
     "Not as a general signup in these reports. <a href=\"%s\">CNBC</a> describes a rollout to Pro and Business Premium in eligible markets, with Enterprise after an admin enables it. The plan detail is on <a href=\"/dots-pricing/\">pricing</a>." % CNBC),
    ("What waitlist is actually described?",
     "<a href=\"%s\">WIRED</a> says Pro users can join a waitlist to text a Dot over iMessage or RCS on Android. <a href=\"%s\">CNBC</a> says texting is coming soon. OpenAI’s <a href=\"%s\">safety appendix</a> lists text message as a follow-up channel. No waitlist URL is published in those three accounts." % (WIRED, CNBC, OPENAI)),
]


def dots_waitlist():
    inner = '''
<section class="band"><div class="wrap">
<h2>Rollout and the texting waitlist are different sentences</h2>
<p><a href="%s">CNBC</a> does not describe a public queue for the product. It describes access inside ChatGPT for Pro and Business Premium, and for Enterprise, Edu, and Healthcare when an admin turns it on.</p>
<p><a href="%s">WIRED</a> is the report that uses the word waitlist, and it uses it for texting: Pro users can join a waitlist for iMessage or RCS. <a href="%s">CNBC</a> separately says texting is coming soon. The <a href="%s">safety appendix</a> says a dot follows up across ChatGPT, text message, email, and Slack.</p>
<p>Not published: a waitlist form URL, and a date when iMessage or RCS leaves that waitlist.</p>
</div></section>
''' % (CNBC, WIRED, CNBC, OPENAI)
    sources = [
        ("WIRED, 29 September 2026", WIRED),
        ("CNBC, 29 September 2026", CNBC),
        ("OpenAI safety appendix, 29 September 2026", OPENAI),
    ]
    return _shell(
        "Unofficial notes · waitlist",
        "Dots waitlist: only texting is described that way",
        "The product rollout in CNBC is plan-based. WIRED uses “waitlist” for iMessage and RCS texting, and does not print a signup link.",
        inner, WAITLIST_FAQS, sources,
    ), WAITLIST_FAQS


# --- vs grok bot ---

VS_GROK_FAQS = [
    ("Did OpenAI say Dots competes with Grok Bot?",
     "Not in the sources linked here. <a href=\"%s\">The Verge</a> calls Dots a Muse competitor. It does not name Grok Bot. This table only lines up published product facts." % VERGE),
    ("Do they share a computer the same way?",
     "OpenAI’s <a href=\"%s\">appendix</a> says each dot has its own cloud computer and browser. <a href=\"%s\">x.ai/bot</a>, fetched 30 September 2026, says Bots have their own computer and keep working 24/7 with the laptop closed. This site’s <a href=\"/learn/computer/\">computer lesson</a> records an earlier official description that Bots on one account share a machine. Both xAI wordings are linked; this page does not merge them." % (OPENAI, XAI)),
]


def dots_vs_grokbot():
    inner = '''
<section class="band"><div class="wrap">
<h2>Published facts side by side</h2>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Dots</th><th>Grok Bot</th></tr></thead>
<tbody>
<tr><td>Company</td><td>OpenAI, in the <a href="%s">safety appendix</a></td><td>xAI, on <a href="%s">x.ai/bot</a></td></tr>
<tr><td>What it is</td><td>Always-on agents on GPT-6 Astra. See <a href="/dots/">what Dots is</a>.</td><td>AI teammates you message on desktop or iOS, on x.ai/bot.</td></tr>
<tr><td>Computer</td><td>Each dot has its own cloud computer and browser.</td><td>x.ai/bot says Bots have their own computer. The <a href="/learn/computer/">computer lesson</a> is the earlier shared-machine note.</td></tr>
<tr><td>Where you talk</td><td>ChatGPT, Slack, Teams, and a voice call from ChatGPT, per <a href="%s">CNBC</a> and <a href="%s">The Verge</a>.</td><td>Desktop and iOS, on x.ai/bot.</td></tr>
<tr><td>How many</td><td>One primary dot now; teams of dots are a later plan, per <a href="%s">CNBC</a>.</td><td>x.ai/bot says you can work with many Bots at once.</td></tr>
<tr><td>Price</td><td>No separate price published. <a href="/dots-pricing/">Pricing note</a>.</td><td>Not published here. Plan names are on x.ai/bot. This site’s <a href="/pricing/">Grok Bot pricing</a> page does not invent dollars either.</td></tr>
<tr><td>OpenAI names Grok Bot</td><td colspan="2">Not published in the Dots sources checked for this page.</td></tr>
</tbody>
</table>
</div>
</div></section>
''' % (OPENAI, XAI, CNBC, VERGE, CNBC)
    sources = [
        ("OpenAI safety appendix, 29 September 2026", OPENAI),
        ("CNBC, 29 September 2026", CNBC),
        ("The Verge, 29 September 2026", VERGE),
        ("x.ai/bot, fetched 30 September 2026", XAI),
    ]
    return _shell(
        "Unofficial notes · comparison",
        "Dots vs Grok Bot, from published pages",
        "OpenAI’s Dots notes do not name Grok Bot. The rows below are what each company’s public pages say, not a claim that one product targets the other.",
        inner, VS_GROK_FAQS, sources,
    ), VS_GROK_FAQS


# --- vs muse ---

VS_MUSE_FAQS = [
    ("Did OpenAI present Dots as a Muse competitor?",
     "<a href=\"%s\">The Verge</a> describes the launch that way. Meta’s Muse posts linked here do not name Dots." % VERGE),
    ("Which one has a published dollar price?",
     "Neither, in the company posts linked here. Dots pricing in the press is on <a href=\"/dots-pricing/\">the pricing note</a>. Meta says Muse is free for most needs, with subscription plans, and does not print a dollar amount."),
]


def dots_vs_muse():
    inner = '''
<section class="band"><div class="wrap">
<h2>What each company has published</h2>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Dots</th><th>Muse</th></tr></thead>
<tbody>
<tr><td>Company</td><td>OpenAI</td><td>Meta</td></tr>
<tr><td>Public date</td><td>29 September 2026. <a href="/dots-release-date/">Release note</a>.</td><td>8 September 2026 introduction. <a href="%s">Meta’s post</a>.</td></tr>
<tr><td>Model name in the post</td><td>GPT-6 Astra, in OpenAI’s appendix.</td><td>Muse Spark, in Meta’s introduction.</td></tr>
<tr><td>Computer</td><td>Each dot has its own cloud computer and browser.</td><td>Muse Secure VM, a dedicated computer with its own browser.</td></tr>
<tr><td>Where you talk</td><td>ChatGPT, Slack, Teams. <a href="/dots/">How to use a Dot</a>.</td><td>Muse app or WhatsApp. Also muse.ai in the same post.</td></tr>
<tr><td>Who can use it</td><td><a href="/dots-pricing/">Pricing note</a>.</td><td>Meta’s 8 September post says the US, on iOS, Android, and muse.ai. The <a href="%s">29 September post</a> says the US and Canada.</td></tr>
<tr><td>Price</td><td>No separate Dots price published.</td><td>Free for most of what people need, plus subscription plans. Dollar amounts: not published.</td></tr>
<tr><td>Approval</td><td>WIRED says Dots ask before actions such as installing software or changing a password. <a href="%s">WIRED</a>.</td><td>Meta says it checks with the person before sending an email or making a purchase. The 29 September post says nothing publishes, sends, or spends without approval.</td></tr>
<tr><td>App chart rank</td><td>Not published in the Dots sources.</td><td><a href="%s">TechCrunch</a>, 25 September 2026, says Muse reached the top of the U.S. App Store on 18 September 2026 and still held that rank in that article. This page does not claim the rank on 30 September.</td></tr>
</tbody>
</table>
</div>
<p><a href="/muse/">What Muse is</a> keeps Meta’s own description. This table does not repeat it.</p>
</div></section>
''' % (MUSE, MUSE_BIZ, WIRED, TC_MUSE)
    sources = [
        ("OpenAI safety appendix, 29 September 2026", OPENAI),
        ("The Verge, 29 September 2026", VERGE),
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
        ("Meta, Muse for Small Business, 29 September 2026", MUSE_BIZ),
        ("TechCrunch on Muse, 25 September 2026", TC_MUSE),
        ("WIRED, 29 September 2026", WIRED),
    ]
    return _shell(
        "Unofficial notes · comparison",
        "Dots vs Muse, from company posts and launch reports",
        "The Verge calls Dots OpenAI’s answer to Muse. The rows use Meta’s Muse posts and OpenAI’s 29 September 2026 notes.",
        inner, VS_MUSE_FAQS, sources,
    ), VS_MUSE_FAQS


# --- alternatives ---

ALT_FAQS = [
    ("What counts as a Dots alternative here?",
     "Only products named in the linked launch coverage or on their own product pages: Meta’s Muse, xAI’s Grok Bot, and OpenClaw as <a href=\"%s\">WIRED</a> mentions it. No ranking is invented." % WIRED),
]


def dots_alternatives():
    inner = '''
<section class="band"><div class="wrap">
<h2>Names that show up next to Dots</h2>
<div class="grid-3">
<a class="card" href="/muse/"><h3>Muse</h3><p>Meta’s personal agent, introduced 8 September 2026. <a href="%s">The Verge</a> is the piece that sets Dots next to it. The comparison is <a href="/dots-vs-muse/">Dots vs Muse</a>.</p></a>
<a class="card" href="/dots-vs-grokbot/"><h3>Grok Bot</h3><p>xAI’s teammate app on <a href="%s">x.ai/bot</a>. OpenAI’s Dots sources do not name it. The table is <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</p></a>
<a class="card" href="/compare/"><h3>OpenClaw</h3><p><a href="%s">WIRED</a> names OpenClaw as an earlier personal-agent tool, before Muse. This site’s <a href="/compare/">Grok Bot alternatives</a> page treats OpenClaw as a framework you host, not as a Dots client.</p></a>
</div>
<p>Not published: a download count, a star rating, or a “best alternative” order.</p>
</div></section>
''' % (VERGE, XAI, WIRED)
    sources = [
        ("The Verge, 29 September 2026", VERGE),
        ("WIRED, 29 September 2026", WIRED),
        ("x.ai/bot", XAI),
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
    ]
    return _shell(
        "Unofficial notes · alternatives",
        "Dots alternatives named in public reports",
        "Muse, Grok Bot, and OpenClaw are the names the linked pages actually use. This is not a ranked list.",
        inner, ALT_FAQS, sources,
    ), ALT_FAQS


# --- faq ---

FAQ_FAQS = [
    ("Is this an official OpenAI page?",
     "No. It is an unofficial note on grokbot.run. OpenAI’s own text is the <a href=\"%s\">safety appendix</a>." % OPENAI),
    ("Do the launch sources name an Alfred agent?",
     "No. The safety appendix, CNBC, The Verge, WIRED, TechCrunch, 9to5Google, and The Next Web do not name an Alfred agent. This site does not describe one."),
    ("Is Dots the same product as Grok Bot or Muse?",
     "No. Comparisons are on <a href=\"/dots-vs-grokbot/\">Dots vs Grok Bot</a> and <a href=\"/dots-vs-muse/\">Dots vs Muse</a>."),
    ("Does model training follow you into Dots?",
     "<a href=\"%s\">WIRED</a> says that if an OpenAI account is set to allow model training, that setting carries over to interactions with the agents. The appendix is the safety write-up; this page does not copy its tables." % WIRED),
    ("Where are price, date, download, and waitlist?",
     "On <a href=\"/dots-pricing/\">pricing</a>, <a href=\"/dots-release-date/\">release date</a>, <a href=\"/dots-download/\">download</a>, and <a href=\"/dots-waitlist/\">waitlist</a>."),
]


def dots_faq():
    inner = '''
<section class="band"><div class="wrap">
<p>The definition and the how-to stay on <a href="/dots/">what Dots is</a>. The questions here are the ones that do not have their own page, plus pointers.</p>
</div></section>
'''
    sources = [
        ("OpenAI safety appendix, 29 September 2026", OPENAI),
        ("WIRED, 29 September 2026", WIRED),
        ("CNBC, 29 September 2026", CNBC),
        ("The Verge, 29 September 2026", VERGE),
    ]
    return _shell(
        "Unofficial notes · FAQ",
        "Dots FAQ: official page, Alfred, and training",
        "Short answers for the questions the launch sources do answer, and an explicit no where they do not name a thing.",
        inner, FAQ_FAQS, sources,
    ), FAQ_FAQS


# --- muse ---

MUSE_FAQS = [
    ("What is Muse?",
     "Meta’s <a href=\"%s\">8 September 2026 post</a> calls Muse a personal AI agent that does work, not only answers. It runs on Muse Secure VM, a dedicated computer with its own browser, and you talk to it in the Muse app or WhatsApp. The same post says it is powered by Muse Spark." % MUSE),
    ("Where is it available?",
     "The 8 September post says the US, on iOS, Android, and muse.ai, with AI glasses described as coming soon. The <a href=\"%s\">29 September post</a> says Muse is available in the US and Canada." % MUSE_BIZ),
    ("Is there a published Muse price?",
     "Not as a dollar amount. Both Meta posts say Muse is free for most of what people need, with subscription plans if you want more."),
]


def muse_page():
    inner = '''
<section class="band"><div class="wrap">
<h2>What Meta says</h2>
<p>Meta’s <a href="%s">introduction</a>, 8 September 2026, says you tell Muse what needs to get done and it takes action. Examples in that post include sending an email, booking travel, and longer goals. It keeps working after the app is closed and comes back for approval, including before it sends an email or makes a purchase. People choose which apps it connects to and can disconnect them.</p>
<p>The <a href="%s">29 September 2026 post</a> adds Muse for Small Business: connectors it names include Asana, Box, Canva, Dropbox, Figma, Granola, HighLevel, Intuit QuickBooks, Klaviyo, Lovable, Notion, Shopify, Slack, Stripe, Zoom, plus Facebook and Instagram business accounts. It says nothing publishes, sends, or spends without approval. Partners are pointed to muse.ai/platform.</p>
<p><a href="%s">TechCrunch</a>, 25 September 2026, reports that Muse reached the top of the U.S. App Store on 18 September 2026 and still held that place in the article. This page does not state the rank on 30 September.</p>
<p>How it differs from Dots is <a href="/dots-vs-muse/">Dots vs Muse</a>. Grok Bot is a different company’s app: <a href="/learn/what-is-grok-bot/">what Grok Bot is</a>.</p>
</div></section>
''' % (MUSE, MUSE_BIZ, TC_MUSE)
    sources = [
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
        ("Meta, Muse for Small Business, 29 September 2026", MUSE_BIZ),
        ("TechCrunch, 25 September 2026", TC_MUSE),
    ]
    return _shell(
        "Unofficial notes · Muse",
        "What is Muse, Meta's personal agent",
        "Muse is Meta’s personal AI agent, introduced 8 September 2026, running on its own secure cloud computer. This page is not Meta’s.",
        inner, MUSE_FAQS, sources,
    ), MUSE_FAQS


# --- muse vs ---

MUSE_VS_FAQS = [
    ("What does “Muse vs” compare?",
     "Muse with Dots, and Muse with Grok Bot. The Dots rows point at <a href=\"/dots-vs-muse/\">Dots vs Muse</a> instead of copying that table. Grok Bot’s row uses <a href=\"%s\">x.ai/bot</a>." % XAI),
]


def muse_vs():
    inner = '''
<section class="band"><div class="wrap">
<h2>Muse next to the other two public agents</h2>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Muse</th><th>Dots</th><th>Grok Bot</th></tr></thead>
<tbody>
<tr><td>Company</td><td>Meta</td><td>OpenAI</td><td>xAI</td></tr>
<tr><td>Own computer, in the company’s words</td><td>Muse Secure VM</td><td>Each dot has its own cloud computer and browser. Full table: <a href="/dots-vs-muse/">Dots vs Muse</a>.</td><td><a href="%s">x.ai/bot</a> says Bots have their own computer.</td></tr>
<tr><td>Talk to it</td><td>Muse app, WhatsApp, muse.ai</td><td>See <a href="/dots/">what Dots is</a>.</td><td>Desktop and iOS</td></tr>
<tr><td>Price on the company page</td><td>Free for most needs; subscriptions exist; dollars not published.</td><td><a href="/dots-pricing/">Not a separate published price</a>.</td><td>Not copied here. See x.ai/bot and <a href="/pricing/">Grok Bot pricing</a>.</td></tr>
</tbody>
</table>
</div>
<p>Meta’s posts do not name Dots or Grok Bot. <a href="%s">The Verge</a> is the piece that sets Dots beside Muse.</p>
</div></section>
''' % (XAI, VERGE)
    sources = [
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
        ("Meta, Muse for Small Business, 29 September 2026", MUSE_BIZ),
        ("The Verge, 29 September 2026", VERGE),
        ("x.ai/bot, fetched 30 September 2026", XAI),
    ]
    return _shell(
        "Unofficial notes · comparison",
        "Muse vs Dots and Muse vs Grok Bot",
        "A short Muse-first table. The longer Dots comparison stays on its own page so the same paragraph is not printed twice.",
        inner, MUSE_VS_FAQS, sources,
    ), MUSE_VS_FAQS


# --- muse alternatives ---

MUSE_ALT_FAQS = [
    ("Which Muse alternatives are on this page?",
     "OpenAI Dots and xAI Grok Bot, because launch coverage puts personal agents next to Muse, plus OpenClaw as <a href=\"%s\">WIRED</a> names it. No score is invented." % WIRED),
]


def muse_alternatives():
    inner = '''
<section class="band"><div class="wrap">
<h2>Other personal-agent names in the same reports</h2>
<div class="grid-3">
<a class="card" href="/dots/"><h3>Dots</h3><p>OpenAI’s always-on agent, 29 September 2026. <a href="%s">The Verge</a> frames it as Muse’s competitor. Read <a href="/dots-vs-muse/">Dots vs Muse</a>.</p></a>
<a class="card" href="/learn/what-is-grok-bot/"><h3>Grok Bot</h3><p>xAI’s teammate app. Meta’s Muse posts do not name it. <a href="/muse-vs/">Muse vs</a> has the short row.</p></a>
<a class="card" href="/compare/"><h3>OpenClaw</h3><p><a href="%s">WIRED</a> mentions OpenClaw as an earlier personal-agent tool. It is not a Muse download.</p></a>
</div>
<p>The Dots list is <a href="/dots-alternatives/">Dots alternatives</a>. Not published: a ranked “best Muse alternative” order.</p>
</div></section>
''' % (VERGE, WIRED)
    sources = [
        ("The Verge, 29 September 2026", VERGE),
        ("WIRED, 29 September 2026", WIRED),
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
        ("x.ai/bot", XAI),
    ]
    return _shell(
        "Unofficial notes · alternatives",
        "Muse alternatives named in public reports",
        "Dots, Grok Bot, and OpenClaw are the names already in the linked pages. This is not a ranking.",
        inner, MUSE_ALT_FAQS, sources,
    ), MUSE_ALT_FAQS


CLUSTER = [
    ("/dots-pricing/", "Dots pricing: no separate price is published", dots_pricing),
    ("/dots-release-date/", "Dots release date: 29 September 2026", dots_release),
    ("/dots-download/", "Dots download: no separate app is published", dots_download),
    ("/dots-waitlist/", "Dots waitlist: only texting is described that way", dots_waitlist),
    ("/dots-vs-grokbot/", "Dots vs Grok Bot, from published pages", dots_vs_grokbot),
    ("/dots-vs-muse/", "Dots vs Muse, from company posts and launch reports", dots_vs_muse),
    ("/dots-alternatives/", "Dots alternatives named in public reports", dots_alternatives),
    ("/dots-faq/", "Dots FAQ: official page, Alfred, and training", dots_faq),
    ("/muse/", "What is Muse, Meta's personal agent", muse_page),
    ("/muse-vs/", "Muse vs Dots and Muse vs Grok Bot", muse_vs),
    ("/muse-alternatives/", "Muse alternatives named in public reports", muse_alternatives),
]
