# -*- coding: utf-8 -*-
"""Second batch of Dots/Muse sibling notes. Each fact is stated once and linked from sibling pages."""
from html import escape
from content_agent_cluster import (
    OPENAI, CNBC, VERGE, TNW, TC_DOTS, WIRED, XAI, MUSE, MUSE_BIZ, TC_MUSE, YAHOO_MUSE, MUSE_CONNECTORS,
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


import re as _re

# Pages not shipped yet: links to them render as plain text until they are live.
PENDING = {"/openai-devday-2026-dots-recap/",
           "/muse-charm/", "/meta-muse-marketplace-issue/"}


def _strip(text):
    def r(m):
        return m.group(2) if m.group(1) in PENDING else m.group(0)
    return _re.sub(r'<a href="(/[^"#]*/)(?:#[^"]*)?">(.*?)</a>', r, text)


def _shell(kicker, h1, lede, inner, faqs, sources):
    from content_agent_cluster import _shell as _s
    return _s(kicker, h1, lede, _strip(inner), [(q, _strip(a)) for q, a in faqs], sources)


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


# ---------------------------------------------------------------- dots vs chatgpt (and Claude)

VSC_FAQS = [
    ("Are dots a separate product from ChatGPT?",
     "They are created and used inside ChatGPT. The <a href=\"%s\">Help Center</a> calls a dot an always-on agent in ChatGPT, with its own cloud computer." % O_HELP),
    ("Can I get a dot on Free, Go, or Plus?",
     "Not officially announced. OpenAI’s pages name Pro, Business Premium, and an Enterprise beta. <a href=\"/how-to-get-openai-dots/\">How to get OpenAI dots</a> has the eligibility list."),
    ("Is there a Claude version of dots?",
     "Anthropic has not published a comparison and has not named a product as a Dots equivalent. Its help center describes Claude Cowork running tasks in the cloud on paid plans. OpenAI’s pages do not name a Claude equivalent either."),
    ("Which model do dots use?",
     "GPT-6 Astra, per OpenAI. GPT-6.1 Sol was announced the same day; the sources checked do not say dots run on it. See <a href=\"/openai-devday-2026-dots-recap/\">the DevDay recap</a>."),
]


def dots_vs_chatgpt():
    inner = '''
<section class="band"><div class="wrap">
<h2>Dots and a normal ChatGPT chat</h2>
<p>OpenAI’s <a href="%(O_HELP)s">Help Center</a> answers this directly: a dot is an always-on agent in ChatGPT that can take on ongoing responsibility and keep making progress between conversations. It has its own cloud computer, works across the apps you connect, and remembers context.</p>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Dots</th><th>ChatGPT conversations</th></tr></thead>
<tbody>
<tr><td>Works when you are away</td><td>Yes: background research, reminders, and recurring tasks you schedule (<a href="%(O_HELP)s">Help Center</a>).</td><td>Not described on the pages checked for this note.</td></tr>
<tr><td>Own computer</td><td>Each dot has its own cloud computer and browser, and you can open it from its profile.</td><td>Not published as a per-conversation computer.</td></tr>
<tr><td>Memory</td><td>Gets memories from ChatGPT and makes its own. Deleting a dot’s own memories means resetting the dot.</td><td>Shared ChatGPT memory settings.</td></tr>
<tr><td>Where you reach it</td><td>ChatGPT on desktop, web, and mobile after creation; Slack; Microsoft Teams. Texting is a limited US Pro beta.</td><td>ChatGPT apps.</td></tr>
<tr><td>Who can use it</td><td>Pro outside the EEA, Switzerland, and the UK; Business Premium in supported regions; Enterprise beta if an admin enables it.</td><td>Per plan.</td></tr>
<tr><td>Usage meter</td><td>For the first month, dots usage does not count toward eligible Pro, Business, and Enterprise allowances; terms after that are not officially announced (<a href="%(O_HELP)s">Help Center</a>).</td><td>Normal plan limits.</td></tr>
<tr><td>Acting on its own</td><td>Built-in confirmations plus Custom Rules. Details on <a href="/dots-security-privacy/">Dots security and privacy</a>.</td><td>Not restated here.</td></tr>
</tbody>
</table>
</div>
<p>Dots and ChatGPT share connected apps and memory settings. OpenAI’s <a href="%(O_SAFE)s">safety post</a> says the Plugins settings are shared across ChatGPT, ChatGPT Work, and Codex. <a href="%(TNW)s">The Next Web</a> reports that tasks a dot starts in Codex or ChatGPT Work count toward usage limits, while conversations with the dot do not.</p>
<h2>Dots and Claude</h2>
<p>There is no official Anthropic or OpenAI page that compares the two. Not officially announced. What each company publishes about its own product:</p>
<div class="table-wrap">
<table>
<thead><tr><th></th><th>Dots (OpenAI)</th><th>Claude Cowork (Anthropic)</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>An always-on agent inside ChatGPT with its own cloud computer.</td><td>Claude’s agentic mode for multi-step tasks, using the same architecture as Claude Code without a terminal (<a href="%(CLAUDE_COWORK)s">help center</a>).</td></tr>
<tr><td>Where it runs</td><td>Cloud computer per dot.</td><td>Sessions run remotely in the cloud, marked beta. On 6 October 2026 new Cowork tasks on Pro and Max are described as running in the cloud.</td></tr>
<tr><td>Plans</td><td>Pro, Business Premium, Enterprise beta.</td><td>Pro, Max, Team, Enterprise; availability differs by surface.</td></tr>
<tr><td>Scheduled work</td><td>Reminders and recurring checks.</td><td>Scheduled tasks.</td></tr>
<tr><td>For developers</td><td>Agents API with computer use and Bedrock Managed Agents are separate announcements in the <a href="/openai-devday-2026-dots-recap/">DevDay recap</a>.</td><td>Claude Managed Agents is an API suite for building cloud-hosted agents, in public beta (<a href="%(CLAUDE_MA)s">Anthropic</a>).</td></tr>
</tbody>
</table>
</div>
<p>These rows line up by category, not by verified equivalence. Speed, quality, and price comparisons between the two are not officially announced, and none is invented here.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>You already pay for ChatGPT Pro or Business Premium and want a long-running helper:</strong> try a dot first. The first is included at no extra cost, per <a href="%(O_INTRO)s">OpenAI</a>.</li>
<li><strong>You are on Free, Go, or Plus:</strong> not officially announced for dots. Plain ChatGPT is what these plans describe.</li>
<li><strong>You live in the EEA, Switzerland, or the UK on a personal plan:</strong> Pro dots exclude those markets at launch. Business Premium is listed for all supported regions.</li>
<li><strong>You want a cloud agent on a Claude plan:</strong> read Anthropic’s Cowork article for your plan and surface, since availability differs.</li>
<li><strong>You want named agents in parallel on a Cursor plan:</strong> Grok Bot. Compare on <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>None of the three companies publishes an import path for another’s agents. Treat each as its own account and rebuild standing instructions by hand. Keep the same rule in each place, for example “never send email without asking,” and check that each product actually enforces it.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Expecting a dot to appear in a plan that OpenAI has not listed.</li>
<li>Planning around free dots usage. Terms after the first month are not officially announced.</li>
<li>Reading a benchmark for one model as a claim about the product. GPT-6.1 Sol has its own page and its own numbers.</li>
<li>Treating Cowork and dots as interchangeable. Their plan gates and surfaces differ.</li>
</ul>
</div></section>
''' % dict(O_HELP=O_HELP, O_SAFE=O_SAFE, TNW=TNW, O_INTRO=O_INTRO, CLAUDE_COWORK=CLAUDE_COWORK, CLAUDE_MA=CLAUDE_MA)
    sources = [
        ("OpenAI Help Center, Getting started with your dot", O_HELP),
        ("OpenAI, Introducing dots, 29 September 2026", O_INTRO),
        ("OpenAI, dots safety post", O_SAFE),
        ("The Next Web, 29 September 2026", TNW),
        ("Anthropic Help Center, Get started with Claude Cowork", CLAUDE_COWORK),
        ("Anthropic, Claude Managed Agents", CLAUDE_MA),
    ]
    return _shell(
        "Unofficial notes · comparison",
        "Dots vs ChatGPT, and how Claude differs",
        "What separates an OpenAI dot from a regular ChatGPT chat, and what Anthropic publishes about Claude Cowork, without a made-up head-to-head.",
        inner, VSC_FAQS, sources,
    ), VSC_FAQS


# ---------------------------------------------------------------- how to get openai dots

HOW_FAQS = [
    ("Can I create a dot on my phone?",
     "No. The <a href=\"%s\">Help Center</a> says you cannot currently create a dot on mobile and that dots are not supported on mobile web. Once created, you can talk to it in the mobile app when mobile access is available." % O_HELP),
    ("I am on Plus. Can I get one?",
     "Not officially announced. OpenAI’s pages list Pro, Business Premium, and an Enterprise beta."),
    ("Why do I not see it yet if I am on Pro?",
     "The Help Center says dots roll out gradually and access may take several days to reach an account. Pro excludes the European Economic Area, Switzerland, and the UK."),
    ("Is there a waitlist?",
     "Only for texting. See <a href=\"/dots-waitlist/\">Dots waitlist</a>. The Help Center calls texting a limited beta for Pro users in the US."),
]


def how_to_get_openai_dots():
    inner = '''
<section class="band"><div class="wrap">
<h2>Check the gates in this order</h2>
<ol>
<li><strong>Plan.</strong> Pro, Business Premium, or Enterprise (including Edu and Healthcare) as a beta that a workspace admin must turn on; it is off by default (<a href="%(O_RECAP)s">DevDay recap</a>). Free, Go, and Plus: not officially announced.</li>
<li><strong>Region.</strong> Pro: not the European Economic Area, Switzerland, or the UK. Business Premium: all supported ChatGPT regions (<a href="%(O_HELP)s">Help Center</a>).</li>
<li><strong>Rollout.</strong> Gradual, and it may take several days to reach your account. The Help Center asks you to check back.</li>
<li><strong>Surface.</strong> Create the dot in the ChatGPT desktop app (also available on Windows) or in ChatGPT on desktop web, then follow the onboarding prompts.</li>
</ol>
<h2>After you have access</h2>
<ol>
<li>Name it during setup. The default handle is @yourname-dot, and naming it changes the handle to @yourname-agentname.</li>
<li>Pick a character or a pet, or let the dot generate a pet.</li>
<li>Connect apps in the Plugins settings, and Slack or texting from desktop.</li>
<li>Decide on your own computer. Access is optional and starts off. You turn it on from the desktop app with Allow access and undo it with Revoke access.</li>
<li>Give it a first task and read its Custom Rules before you rely on it. What those rules protect is on <a href="/dots-security-privacy/">Dots security and privacy</a>.</li>
</ol>
<p>Not available at launch, per the Help Center: creating a dot on mobile, a standalone email address for the dot, and calls started by the dot. It can use your personal email account if you connect it.</p>
<h2>What it costs to get one</h2>
<p>OpenAI says the first dot is included at no extra cost, and that for the next month dots usage does not count toward eligible Pro, Business, and Enterprise plan allowances. Terms after that are not officially announced. More on <a href="/dots-pricing/">Dots pricing</a>.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Eligible and in a supported region:</strong> create it on desktop, name it, connect one app, and run one small task before widening access.</li>
<li><strong>On Pro in the EEA, Switzerland, or the UK:</strong> not covered at launch. No date for those markets is officially announced.</li>
<li><strong>Enterprise:</strong> ask a workspace admin to enable the beta. What an admin can configure beyond that switch is not officially announced in the sources checked.</li>
<li><strong>Not eligible yet:</strong> <a href="/dots-alternatives/">Dots alternatives</a> lists the products named in the launch coverage, including Grok Bot.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>A dot and a Grok Bot are separate accounts on separate computers. If you already run Grok Bot, do not disconnect anything to try a dot. Add one connection at a time and keep the tasks apart until you know which product handles which. There is no official import from either side.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Trying to create the dot on a phone. Creation is desktop only.</li>
<li>Turning on local computer access for the first task. It is optional and can wait.</li>
<li>Enabling texting expecting it everywhere. It is a limited beta for Pro users in the US, and Business and Enterprise workspaces do not have it. Reply STOP to stop outgoing texts.</li>
<li>Assuming resetting only clears chat. Reset deletes the dot with its conversations, memories, and scheduled tasks.</li>
</ul>
</div></section>
''' % dict(O_HELP=O_HELP, O_RECAP=O_RECAP)
    sources = [
        ("OpenAI Help Center, Getting started with your dot", O_HELP),
        ("OpenAI, Introducing dots, 29 September 2026", O_INTRO),
        ("OpenAI, DevDay 2026 recap", O_RECAP),
        ("The Next Web, 29 September 2026", TNW),
    ]
    return _shell(
        "Unofficial notes · access",
        "How to get OpenAI dots: plan, region, and setup",
        "Who can create a dot, where it is not available, and the setup order from OpenAI’s Help Center. This is not OpenAI’s page.",
        inner, HOW_FAQS, sources,
    ), HOW_FAQS


# ---------------------------------------------------------------- dots not officially announced

NOA_FAQS = [
    ("Why does this page exist?",
     "Search results for dots mix confirmed facts with rumor. This page keeps the gaps in one place. Each row cites the OpenAI wording that shows the gap."),
    ("Where do I check whether something has since been announced?",
     "Start with OpenAI’s <a href=\"%s\">Help Center article</a>, then the <a href=\"%s\">launch post</a>. This site’s pages were checked on 30 September 2026 and may lag." % (O_HELP, O_INTRO)),
]


def dots_not_officially_announced():
    inner = '''
<section class="band"><div class="wrap">
<h2>What OpenAI has said is coming, or not yet available</h2>
<div class="table-wrap">
<table>
<thead><tr><th>Topic</th><th>What the sources say</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Free, Go, or Plus access</td><td>OpenAI names Pro, Business Premium, and an Enterprise beta. Plans below those are not named.</td><td>Not officially announced</td></tr>
<tr><td>Usage terms after month one</td><td>The <a href="%(O_HELP)s">Help Center</a>: dots usage does not count toward allowances for the next month, and “after this period, we’ll share usage terms for each plan.”</td><td>Not officially announced</td></tr>
<tr><td>Price of extra dots or more capacity</td><td>The <a href="%(O_INTRO)s">launch post</a> says that in the future you will be able to add more dots and scale speed or monthly work. No price is given.</td><td>Not officially announced</td></tr>
<tr><td>Pro in the EEA, Switzerland, and the UK</td><td>Excluded at launch. No later date is given in the sources checked.</td><td>Not officially announced</td></tr>
<tr><td>Texting for everyone</td><td>The launch post says “coming soon.” The Help Center describes a limited beta through a third-party provider for Pro users in the US, not in Business or Enterprise.</td><td>Limited beta only</td></tr>
<tr><td>Teams of dots</td><td>“Over time, we envision teams of dots working together on your behalf.”</td><td>Not officially announced</td></tr>
<tr><td>Creating a dot on mobile</td><td>The Help Center says you cannot currently create one on mobile.</td><td>Not available now</td></tr>
<tr><td>A standalone email address for the dot</td><td>The Help Center: at launch you cannot give your dot its own standalone email address.</td><td>Not available at launch</td></tr>
<tr><td>A dot calling you</td><td>The Help Center: your dot cannot initiate calls to you at launch.</td><td>Not available at launch</td></tr>
<tr><td>Specialist dots for companies</td><td>Focused enterprise pilots, and an integration with Microsoft Agent 365 that OpenAI says it is working on.</td><td>Preview and pilots</td></tr>
<tr><td>Which model version dots run on</td><td>GPT-6 Astra, per OpenAI. Whether dots move to GPT-6.1 Sol is not stated in the sources checked.</td><td>Not officially announced</td></tr>
<tr><td>An independent security audit</td><td>The <a href="/dots-security-privacy/">test numbers</a> are OpenAI’s own.</td><td>Not officially announced</td></tr>
<tr><td>A comparison with Claude or Grok Bot</td><td>OpenAI’s dots pages do not name either. See <a href="/dots-vs-chatgpt/">Dots vs ChatGPT</a> and <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</td><td>Not officially announced</td></tr>
<tr><td>Import or shared login with another agent</td><td>None of the sources describe one.</td><td>Not officially announced</td></tr>
</tbody>
</table>
</div>
<h2>Claims to treat carefully</h2>
<ul>
<li><strong>“Dots is just hosted OpenClaw.”</strong> Nothing in OpenAI’s dots pages says this. The DevDay recap lists OpenClaw only among 16 partners for “Sign in with ChatGPT.”</li>
<li><strong>Dollar prices in press coverage.</strong> Outlets differ, and OpenAI’s dots pages linked here print none. Use <a href="/dots-pricing/">Dots pricing</a> for how this site handles it.</li>
<li><strong>Employee comparisons with Muse.</strong> A newsletter relayed a social post attributed to an OpenAI employee. It is anecdotal and not used here.</li>
</ul>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Budgeting:</strong> plan around the first dot being included and the first month being outside your allowance. Leave the period after it as a variable, because terms are not officially announced.</li>
<li><strong>Rolling out to a team:</strong> assume the Enterprise beta has admin-only enablement and off by default. Ask your OpenAI contact about anything beyond that.</li>
<li><strong>Needing texting or a dot-owned email today:</strong> neither is a general feature yet. Consider what else covers the channel.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>Nothing on this page changes what you can do with Grok Bot today. The two products are compared on <a href="/dots-vs-grokbot/">their own page</a>. If a missing feature blocks you, staying on the product that already has it is a valid choice.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Quoting a “coming soon” line as a date.</li>
<li>Treating a limited beta as general availability.</li>
<li>Counting a social post or forum comment as a source.</li>
<li>Reading “not officially announced” as “will not happen.” It means the sources checked do not say.</li>
</ul>
</div></section>
''' % dict(O_HELP=O_HELP, O_INTRO=O_INTRO)
    sources = [
        ("OpenAI, Introducing dots, 29 September 2026", O_INTRO),
        ("OpenAI Help Center, Getting started with your dot", O_HELP),
        ("OpenAI, DevDay 2026 recap", O_RECAP),
        ("OpenAI, GPT-6 Astra system card, dots appendix", OPENAI),
    ]
    return _shell(
        "Unofficial notes · gaps",
        "Dots: what is not officially announced",
        "One list of what OpenAI has not announced for dots, or has marked coming soon, limited beta, or unavailable at launch.",
        inner, NOA_FAQS, sources,
    ), NOA_FAQS


CLUSTER2 = [
    ("/muse-vs-grok-bot/", "Muse vs Grok Bot: where they differ, by their own pages", muse_vs_grok_bot),
    ("/dots-security-privacy/", "Dots security and privacy: what OpenAI says and tested", dots_security_privacy),
    ("/dots-vs-chatgpt/", "Dots vs ChatGPT, and how Claude differs", dots_vs_chatgpt),
    ("/how-to-get-openai-dots/", "How to get OpenAI dots: plan, region, and setup", how_to_get_openai_dots),
    ("/dots-not-officially-announced/", "Dots: what is not officially announced", dots_not_officially_announced),
]
