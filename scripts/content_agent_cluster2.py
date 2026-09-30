# -*- coding: utf-8 -*-
"""Second batch of Dots/Muse sibling notes. Each fact is stated once and linked from sibling pages."""
from html import escape
from content_agent_cluster import (
    _shell, OPENAI, CNBC, VERGE, TNW, TC_DOTS, WIRED, XAI, MUSE, MUSE_BIZ, TC_MUSE, YAHOO_MUSE, MUSE_CONNECTORS,
)

CONNECT = "https://www.meta.com/blog/meta-connect-2026-everything-we-announced/"
G_SEC = "https://docs.x.ai/grok-bot/approvals-security-and-privacy"
G_FAQ = "https://docs.x.ai/grok-bot/faq"
G_OVER = "https://docs.x.ai/grok-bot/overview"
O_INTRO = "https://openai.com/index/introducing-dots/"
O_SAFE = "https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/"
O_HELP = "https://help.openai.com/en/articles/20001530-getting-started-with-your-dot"
O_RECAP = "https://openai.com/index/devday-2026-recap/"
O_SOL = "https://openai.com/index/introducing-gpt-6-1-sol/"
V_CHARM = "https://www.theverge.com/tech/999944/meta-muse-charm-ai-interact-5g-modem"
TC_CHARM = "https://techcrunch.com/2026/09/23/meta-made-a-tamagotchi-like-wearable-for-its-muse-ai-agent/"
V_MKT = "https://www.theverge.com/ai-artificial-intelligence/1001886/meta-muse-ai-facebook-marketplace-security-concerns"
BI_MKT = "https://www.businessinsider.com/muse-agent-facebook-marketplace-address-setting-meta-always-allow-2026-9"
PC_MKT = "https://au.pcmag.com/ai/120110/muse-ai-shared-address-error-traced-to-confusion-about-marketplace-permissions"
CLAUDE_COWORK = "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork"
CLAUDE_MA = "https://claude.com/blog/claude-managed-agents"


def _faqs(pairs):
    return pairs


def _copy(id_, text):
    return '<pre><code id="%s">%s</code></pre>\n<button type="button" class="copy-btn" data-copy-target="%s">Copy</button>' % (id_, escape(text), id_)


# ---------------------------------------------------------------- muse vs grok bot

MVG_FAQS = [
    ("Which one runs on more than one computer?",
     "Neither page set says so. Grok Bot’s docs put all of your Bots on one shared cloud computer per user (<a href=\"%s\">FAQ</a>). Meta’s 8 September post describes one Muse Secure VM. Several Muses on one account are not described in the Meta posts checked here." % G_FAQ),
    ("Is there an official Muse to Grok Bot import?",
     "Not officially announced. Neither company’s pages checked here describe moving chats, memory, or connectors between the two."),
    ("Does Meta mention Grok Bot?",
     "Not in the Muse posts linked on this page. This comparison is built from each company’s own pages, not from a claim that one targets the other."),
    ("Which has the lower entry cost?",
     "Meta says Muse is free for most needs, with subscription plans for more, and prints no dollar amount. Grok Bot access is included with paid individual Cursor plans, Cursor Teams, or a linked SuperGrok plan, per <a href=\"%s\">its docs</a>. Dollar figures for each are on <a href=\"/muse/#price\">What is Muse</a> and <a href=\"/pricing/\">Grok Bot pricing</a>." % G_FAQ),
]


def muse_vs_grok_bot():
    inner = '''
<section class="band"><div class="wrap">
<h2>Muse and Grok Bot, row by row</h2>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Muse (Meta)</th><th>Grok Bot (xAI)</th></tr></thead>
<tbody>
<tr><td>Where the work runs</td><td>Muse Secure VM, a dedicated cloud computer with its own browser (<a href="%(MUSE)s">Meta, 8 September</a>).</td><td>One persistent cloud computer per user with a browser, filesystem, and terminal (<a href="%(G_OVER)s">docs</a>).</td></tr>
<tr><td>Who shares that computer</td><td>Not published beyond “dedicated.”</td><td>Every Bot on your account. The docs say not to use separate Bots as a security boundary.</td></tr>
<tr><td>How many agents</td><td>Meta’s posts describe “your Muse.” Several at once are not described in the posts checked.</td><td>Many Bots in parallel, each with its own screen on the shared computer, per the <a href="%(G_FAQ)s">FAQ</a>.</td></tr>
<tr><td>Where you talk to it</td><td>Muse app, WhatsApp, the web, and a Mac version, per the <a href="%(CONNECT)s">Connect post</a>. Glasses are “coming soon.”</td><td>Desktop on macOS, Windows, Linux; iPhone, iPad, Android (<a href="%(G_OVER)s">docs</a>).</td></tr>
<tr><td>Approval model</td><td>A separate Sentinel must approve anything that reaches the internet; nothing publishes, sends, or spends without approval (<a href="%(MUSE_BIZ)s">29 September</a>).</td><td>Approvals with Allow once, Always allow, Deny; optional Auto Review with “Ask first” and “Allow automatically” rules (<a href="%(G_SEC)s">docs</a>).</td></tr>
<tr><td>Passwords</td><td>Muse does not see passwords or payment methods; they go to secure storage.</td><td>Password, passkey, 2FA, and CAPTCHA steps are handed to you through Agent Computer takeover.</td></tr>
<tr><td>Your own computer</td><td>Muse for Mac can drive apps “with your permission” (Connect post).</td><td>Setting “Execution on Local Computer”; the default is Ask every time.</td></tr>
<tr><td>Who can use it</td><td>US, plus Canada for the small-business rollout (29 September post).</td><td>Paid individual Cursor plans, Cursor Teams, or a linked SuperGrok plan. Enterprise access is “rolling out,” per the FAQ.</td></tr>
<tr><td>Price</td><td>Free for most needs; subscriptions exist; no dollar amount in Meta’s posts.</td><td>Weekly usage included with the plan. Not restated here; see <a href="/pricing/">Grok Bot pricing</a>.</td></tr>
</tbody>
</table>
</div>
<p>The short three-way row lives on <a href="/muse-vs/">Muse vs</a>. Dots is on its own page: <a href="/dots-vs-muse/">Dots vs Muse</a> and <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Personal errands and shopping in the US or Canada:</strong> Muse. The Connect post lists shopping and payment connectors, and checkout waits for your approval.</li>
<li><strong>Several named roles working in parallel, with a plan you already pay for:</strong> Grok Bot. Muse’s posts do not describe that.</li>
<li><strong>Tasks that need a wall between roles:</strong> neither page set gives you one on a single account. Grok Bot says so directly. Meta’s Muse Confidential VM, encrypted with a key only the person holds, is “later this year” in the 8 September post, and no date is officially announced.</li>
<li><strong>Nothing to spend yet:</strong> Muse’s free allowance. Grok Bot needs a paid plan per its docs.</li>
</ul>
<h3>Use both, or move</h3>
<p>No migration path is officially announced. If you run both, treat them as two accounts with two computers. Re-create the standing rules by hand in each: Muse’s approval prompts on one side, Grok Bot’s Auto Review rules on the other. Keep credentials out of chat in both.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Choosing a persistent “always” answer to the first permission prompt. Both products have one. <a href="%(V_MKT)s">The Verge</a> reports one Muse user who did that on 29 September.</li>
<li>Treating Bots as separated. On Grok Bot they share files, browser sessions, and logins.</li>
<li>Assuming Auto Review is enough. The docs call it model-based and say it should complement, not replace, least privilege and explicit boundaries.</li>
</ul>
<h3>Copyable boundary prompt</h3>
<p>Grok Bot’s security docs publish this example of a request with a stop line. It is copied as written, not adapted.</p>
%(prompt)s
<p class="muted">Source: <a href="%(G_SEC)s">docs.x.ai, Approvals, security, and privacy</a>. Meta’s own published prompts are on <a href="/muse/#how">What is Muse</a>.</p>
</div></section>
''' % dict(MUSE=MUSE, G_OVER=G_OVER, G_FAQ=G_FAQ, CONNECT=CONNECT, MUSE_BIZ=MUSE_BIZ, G_SEC=G_SEC, V_MKT=V_MKT,
           prompt=_copy("gb-boundary", "Reconcile the campaign data and draft a recommended budget change. Do not change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact."))
    sources = [
        ("Meta, Introducing Muse, 8 September 2026", MUSE),
        ("Meta, Muse for Small Business, 29 September 2026", MUSE_BIZ),
        ("Meta, Connect 2026 announcements", CONNECT),
        ("xAI docs, Grok Bot overview", G_OVER),
        ("xAI docs, Grok Bot FAQ", G_FAQ),
        ("xAI docs, Approvals, security, and privacy", G_SEC),
        ("x.ai/bot", XAI),
    ]
    return _shell(
        "Unofficial notes · comparison",
        "Muse vs Grok Bot: where they differ, by their own pages",
        "Meta’s Muse and xAI’s Grok Bot side by side, using each company’s published pages. This site is about Grok Bot but is not xAI’s.",
        inner, MVG_FAQS, sources,
    ), MVG_FAQS


CLUSTER2 = [
    ("/muse-vs-grok-bot/", "Muse vs Grok Bot: where they differ, by their own pages", muse_vs_grok_bot),
]
