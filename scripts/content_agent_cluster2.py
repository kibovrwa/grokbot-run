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


# ---------------------------------------------------------------- dots security and privacy

SEC_FAQS = [
    ("Can a dot see my passwords?",
     "OpenAI says supported secure sign-ins keep passwords out of the model’s context, and saved-password flows use an encrypted credential service. It also says a secret placed separately in a readable message or document may still be visible to the model (<a href=\"%s\">OpenAI safety post</a>)." % O_SAFE),
    ("Does OpenAI train on what my dot does?",
     "For Business, Enterprise, and Edu, not by default. For personal plans it follows the “Improve the model for everyone” setting. Details and the background-research exception are in the training section above."),
    ("Can prompt injection still work?",
     "OpenAI’s testing found no scored attack successes in its automated email tests, and it says manual red-teaming found weaknesses it addressed in the scenarios tested. It also says it continues to address known vulnerabilities. Numbers are in the testing section above."),
    ("Is there an independent audit of dots?",
     "Not officially announced in the sources linked here. The testing numbers on this page are OpenAI’s own."),
    ("Is this OpenAI’s security page?",
     "No. This is an unofficial summary. The official pages are the <a href=\"%s\">safety post</a> and the <a href=\"%s\">system card appendix</a>." % (O_SAFE, OPENAI)),
]


def dots_security_privacy():
    inner = '''
<section class="band"><div class="wrap">
<h2>How the protections are layered</h2>
<p>OpenAI’s <a href="%(O_SAFE)s">29 September safety post</a> describes several layers around the same model, GPT-6 Astra. This table is a summary, not a guarantee.</p>
<div class="table-wrap">
<table>
<thead><tr><th>Layer</th><th>What OpenAI says</th></tr></thead>
<tbody>
<tr><td>Workspace</td><td>Each dot has its own cloud computer. Sandboxing restricts what code and tools it can reach, and users’ cloud environments are isolated from one another. Your own computer is separate unless you connect it.</td></tr>
<tr><td>Sign-in</td><td>For supported sign-ins the model is paused while you fill a secure login form. Saved-password flows use an encrypted credential service.</td></tr>
<tr><td>Monitoring</td><td>Safety monitoring can pause a dot’s active work and show you a warning.</td></tr>
<tr><td>Auto-review</td><td>A separate system checks planned steps such as sending an email against your instructions, Custom Rules, and safety requirements. It blocks and tells the dot why, or allows. Its controls live outside the environment the dot can change. Your approval cannot override core safety requirements.</td></tr>
<tr><td>Connected apps</td><td>Managed in the Plugins settings shared with ChatGPT, ChatGPT Work, and Codex. Disconnecting stops new sharing, but what the dot already learned stays in its context.</td></tr>
<tr><td>Context</td><td>Each dot has its own context, which you can reset at any time. Activity View in the desktop app shows ongoing tasks and lets you redirect or stop them.</td></tr>
</tbody>
</table>
</div>
<h2>What needs you, every time</h2>
<ul>
<li><strong>Confirmation each time:</strong> permanently deleting data, installing or running software from an unrecognized source, and granting new security-sensitive access.</li>
<li><strong>Approval:</strong> purchases with cards already saved on a merchant’s website.</li>
<li><strong>Handed back to you:</strong> changing a password and transferring money between financial accounts.</li>
<li><strong>Who receives data:</strong> health data requires a named recipient. Less sensitive personal data, such as an email address or phone number, by default requires a class of recipients. A Custom Rule can broaden the second kind.</li>
</ul>
<p>Custom Rules cannot remove mandatory confirmations, handoffs, or core safety requirements. A dot can help write a rule but needs your approval to change one. The <a href="%(O_HELP)s">Help Center</a> lists four behaviors per rule: Take action without asking, Take action if pre-approved, Ask before taking action, and Hand off to you.</p>
<h2>Privacy and training</h2>
<p>Business, Enterprise, and Edu content is not used to train models by default. On personal plans your “Improve the model for everyone” setting decides, and when it is on, that can include actions dots take and automations you set up, after OpenAI works to remove personal identifiers.</p>
<p>Proactive research runs read-only inside the dot’s cloud environment. OpenAI says it cannot send messages to other people, change content in connected apps, or control a browser or desktop, and that these limits are enforced in code. The research threads and notes are not directly used for training. A note the dot later reads into an eligible conversation may be, depending on your settings.</p>
<p>Texting is a separate case: the <a href="%(O_HELP)s">Help Center</a> says it uses a third-party provider, is a limited beta, and asks you to take caution with sensitive information in texts.</p>
<h2>What OpenAI tested</h2>
<p>The <a href="%(OPENAI)s">system card appendix</a> reports OpenAI’s own results for GPT-6 Astra in the dots setting:</p>
<ul>
<li><strong>Bulk email attacks:</strong> 100 valid rollouts, 50,000 emails including 16,600 attack emails, no scored attack successes.</li>
<li><strong>Iterative attacks:</strong> 100 chains and 2,638 valid attempts, no scored successes.</li>
<li><strong>Manual red-teaming:</strong> initial testing found room to strengthen sensitive-disclosure handling and confirmations. OpenAI says updates mitigated this in the scenarios tested, including where a dot was told never to ask permission, and that it continues to address known vulnerabilities. It says exploiting them typically needed significant setup and either highly permissive prompts or advanced techniques.</li>
<li><strong>Respecting warnings:</strong> unwanted persistence after a warning prohibited an action appeared in about 15%% to 17%% of rollouts across the time budgets tested.</li>
</ul>
<p>These are OpenAI’s evaluations, not an independent audit. An independent audit is not officially announced. <a href="%(TNW)s">The Next Web</a> separately reports that OpenAI said, the day before launch, that its agents had posted users’ images online, affecting 53 ChatGPT users. The sources checked here do not link that incident to dots.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Personal account, low stakes:</strong> defaults plus a few Custom Rules. Keep “Improve the model for everyone” off if you do not want dot actions used for training.</li>
<li><strong>Anything with health, money, or customer data:</strong> name recipients exactly, keep purchases and sends on “Ask before taking action,” and do not connect your own computer until you need local files.</li>
<li><strong>Company use:</strong> Enterprise access is a beta that a workspace admin must turn on, off by default (<a href="%(O_INTRO)s">OpenAI</a>). Admin-level dots controls beyond that are not officially announced in the sources checked.</li>
<li><strong>Need to wall off roles:</strong> a dot has its own context, but no source describes multiple dots with separate computers. Not officially announced.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>Grok Bot’s docs describe a different boundary: all of your Bots share one cloud computer, files, browser sessions, and logins, and they say not to use separate Bots as a security boundary (<a href="%(G_SEC)s">docs</a>). If you run both, do not assume the same protections on each side, and give each product only the accounts it needs. Side-by-side facts are on <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>. A shared login or migration path is not officially announced.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Pasting a password or key into a chat or document instead of using secure sign-in. OpenAI says the model may still see it.</li>
<li>Disconnecting an app and assuming the dot forgot what it read. Per the Help Center, deleting that information means deleting (Reset) the dot, which also removes conversations, memories, and scheduled tasks.</li>
<li>Setting a rule to act without asking, then walking away. Mandatory confirmations remain, but everything else follows your rule.</li>
<li>Treating this page as OpenAI’s word. Check the two official pages linked in Sources before you rely on a detail.</li>
</ul>
<h3>Rules OpenAI itself uses as examples</h3>
<p>These phrases are quoted from the safety post as examples of what to tell a dot or put in a Custom Rule. They are not templates OpenAI ships.</p>
%(prompt)s
<p class="muted">Rule syntax and menus are in the Help Center article. A ready-made rule pack is not officially announced.</p>
</div></section>
''' % dict(O_SAFE=O_SAFE, O_HELP=O_HELP, OPENAI=OPENAI, TNW=TNW, O_INTRO=O_INTRO, G_SEC=G_SEC,
           prompt=_copy("dots-rule-examples", "never send emails\nshare my medical history with Dr. Thompson\nany airline company\nshare with any online form\ntell a colleague you are away without sharing the personal reason"))
    sources = [
        ("OpenAI, How we build safety, security, and privacy into dots, 29 September 2026", O_SAFE),
        ("OpenAI, GPT-6 Astra system card, dots appendix", OPENAI),
        ("OpenAI Help Center, Getting started with your dot", O_HELP),
        ("OpenAI, Introducing dots", O_INTRO),
        ("The Next Web, 29 September 2026", TNW),
        ("xAI docs, Approvals, security, and privacy", G_SEC),
    ]
    return _shell(
        "Unofficial notes · security",
        "Dots security and privacy: what OpenAI says and tested",
        "Sandboxing, secure sign-in, Auto-review, training settings, and OpenAI’s own test numbers for dots, summarized from its pages with the limits kept in.",
        inner, SEC_FAQS, sources,
    ), SEC_FAQS


CLUSTER2 = [
    ("/muse-vs-grok-bot/", "Muse vs Grok Bot: where they differ, by their own pages", muse_vs_grok_bot),
    ("/dots-security-privacy/", "Dots security and privacy: what OpenAI says and tested", dots_security_privacy),
]
