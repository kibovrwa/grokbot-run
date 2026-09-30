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
PENDING = set()


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


# ---------------------------------------------------------------- muse charm

CHARM_FAQS = [
    ("How much does Muse Charm cost?",
     "Not officially announced. Meta’s Connect post gives no price. <a href=\"%s\">The Verge</a>, relaying Bloomberg, says the price was undecided and that people familiar expect roughly smartwatch range, with carrier fees not settled. That is a report, not a Meta statement." % V_CHARM),
    ("When does Muse Charm come out?",
     "Meta’s written post says only that it will share more later this year. <a href=\"%s\">TechCrunch</a> quotes Mark Zuckerberg on stage saying the devices would be ready to ship in time for the holidays in December. An exact date is not officially announced." % TC_CHARM),
    ("Is it a Tamagotchi?",
     "No. TechCrunch calls it Tamagotchi-like, and Bloomberg’s report says the look resembles one. Meta describes it as a device to talk and interact with your Muse."),
    ("Is Muse Charm the same as Meta VR Glasses?",
     "No. They are separate products announced at Connect 2026. The VR Glasses section below has Meta’s numbers."),
]


def muse_charm():
    inner = '''
<section class="band"><div class="wrap">
<h2>What Meta says</h2>
<p>Meta’s <a href="%(CONNECT)s">Connect 2026 recap</a> gives Muse Charm one paragraph: “a delightful and fun device built for you to talk and interact with your Muse. It brings the power of Muse with a state of the art real-time voice model into a device that fits in your pocket. We’ll have more to share later this year.” Meta also has a product page titled “Muse Charm - Personal AI Agent” at <a href="https://www.meta.com/muse-charm/">meta.com/muse-charm</a>. Its text did not load in the check used for this note, so nothing on this page is taken from it.</p>
<h2>What Zuckerberg and the press add</h2>
<div class="table-wrap">
<table>
<thead><tr><th>Detail</th><th>Source</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Shows the Muse avatar on a small screen; you tap a fingerprint sensor to start talking without unlocking a phone or opening an app; fits on a keychain</td><td><a href="%(TC_CHARM)s">TechCrunch</a>, quoting the keynote</td><td>Said on stage</td></tr>
<tr><td>Ships “in time for the holidays in December”; components still being finalized</td><td>TechCrunch, quoting Zuckerberg</td><td>Said on stage; no exact date</td></tr>
<tr><td>About 2-inch OLED touchscreen, its own operating system, a 5G modem so it works without Wi-Fi, cameras, speakers, microphones, USB-C, music and video playback</td><td><a href="%(V_CHARM)s">The Verge</a>, relaying Bloomberg</td><td>Reported, not in Meta’s post</td></tr>
<tr><td>Set up through the Muse app on iOS or Android; can recognize other nearby Charms</td><td>The Verge, relaying Bloomberg</td><td>Reported, not in Meta’s post</td></tr>
<tr><td>Price roughly like a smartwatch; carrier fees for 5G undecided</td><td>The Verge, relaying Bloomberg</td><td>Reported. Price not officially announced</td></tr>
<tr><td>Avatar known internally as “Jolly”</td><td>TechCrunch</td><td>Reported</td></tr>
</tbody>
</table>
</div>
<p>Not officially announced by Meta: price, exact release date, countries, colors and materials, battery life, storage, whether it needs a paid Muse plan, and whether it works without a phone. TechCrunch adds that Zuckerberg described the design as still being finalized.</p>
<h2>Why people call it a Tamagotchi</h2>
<p>TechCrunch’s 23 September report calls it a “Tamagotchi-like wearable,” and its 24 September analysis says many people have pointed out the resemblance to the pocket virtual pet. Meta’s own wording does not use the comparison. The avatar is customizable, per TechCrunch.</p>
<h2>Meta VR Glasses, which are not the Charm</h2>
<p>The same Connect recap says Meta VR Glasses weigh about 100 grams, use a 5K micro-OLED display, keep the battery and processors in a clip-on puck, and will be available in Spring 2027 for $1,299.99 USD. That price is for the VR Glasses only. The recap prints no such number for Muse Charm.</p>
<p>Also announced there: Muse on Meta’s AI glasses “in the coming months,” a Muse email address, and Muse for Mac. What Muse itself does is on <a href="/muse/">What is Muse</a>.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>You want Muse today:</strong> use the app, WhatsApp, the web, or Mac, per Meta’s Connect recap. The Charm is not on sale.</li>
<li><strong>You want a hands-free voice device:</strong> Meta’s glasses are the other announced route to Muse, and both are “coming” items. Timing for Muse on glasses is “coming months,” not a date.</li>
<li><strong>You are budgeting:</strong> do not put a number on the Charm. Reserve for it only after Meta publishes a price. A reservation or waitlist is not described in Meta’s post.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>Grok Bot has no Charm-like device in the pages this site checked. A Charm would be a new way to reach Muse, not to reach Grok Bot. If you rely on Grok Bot for parallel work, keep it and treat the Charm as a possible extra. Comparison of the software is on <a href="/muse-vs-grok-bot/">Muse vs Grok Bot</a>.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Quoting the Bloomberg-based specs as Meta’s. They are reports, and final hardware can differ.</li>
<li>Mixing the $1,299.99 VR Glasses price into Charm searches.</li>
<li>Assuming it works with an agent other than Muse.</li>
<li>Assuming a December date applies outside the US. Countries are not officially announced.</li>
</ul>
<p>Privacy behavior of Muse itself, including the permission prompt that a user blamed after a Marketplace incident, is on <a href="/meta-muse-marketplace-issue/">Meta Muse and the Marketplace incident</a>.</p>
</div></section>
''' % dict(CONNECT=CONNECT, TC_CHARM=TC_CHARM, V_CHARM=V_CHARM)
    sources = [
        ("Meta, Everything we announced at Connect 2026", CONNECT),
        ("Meta, Muse Charm product page (text not verified)", "https://www.meta.com/muse-charm/"),
        ("TechCrunch, 23 September 2026", TC_CHARM),
        ("TechCrunch, 24 September 2026", "https://techcrunch.com/2026/09/24/metas-muse-charm-looks-like-a-tamagotchi-but-its-tapping-into-a-much-newer-trend/"),
        ("The Verge, relaying Bloomberg", V_CHARM),
    ]
    return _shell(
        "Unofficial notes · Muse Charm",
        "Muse Charm: what Meta said, what is only reported",
        "Meta’s pocket device for Muse. Meta has not announced a price or exact release date, and this page separates its words from press reports.",
        inner, CHARM_FAQS, sources,
    ), CHARM_FAQS


# ---------------------------------------------------------------- muse marketplace issue

MKT_FAQS = [
    ("Did Muse leak a user’s address?",
     "A YouTuber, Matt Robb, says Muse sent his home address to a Facebook Marketplace buyer. He later said he had chosen “Allow Always” on the first permission prompt. Meta’s David Singleton said Meta confirmed “no breach of privacy controls,” per <a href=\"%s\">Business Insider</a>." % BI_MKT),
    ("Has Meta changed anything?",
     "Meta’s Muse team said it would make the permission prompt clearer, per Business Insider. Singleton said the “00” price-display issue was fixed. A published changelog is not officially announced."),
    ("Is this proof that Muse is unsafe?",
     "This page does not reach that conclusion. It records what was reported on 29 to 30 September 2026 by three outlets, all relaying one user’s account and Meta’s replies."),
]


def meta_muse_marketplace_issue():
    inner = '''
<section class="band"><div class="wrap">
<h2>What was reported</h2>
<p>On 29 September 2026, <a href="%(V_MKT)s">The Verge</a> reported that tech YouTuber Matt Robb said Muse gave his home address to a stranger after he authorized it to handle his Facebook Marketplace account. His post said Muse “told people my address and agreed a lowball price and then they showed up without it even telling me until late tonight that it messed up.”</p>
<div class="table-wrap">
<table>
<thead><tr><th>Question</th><th>What the reports say</th></tr></thead>
<tbody>
<tr><td>How was Muse set up?</td><td>Robb gave it “hands-off” control of replying to Marketplace messages, plus his address, pickup times, accepted payment types, and an instruction to be short, casual, and human (The Verge, quoting a Muse-generated summary).</td></tr>
<tr><td>Did he tell it to share the address?</td><td>The Muse summary said he never explicitly instructed it to, and that it never asked for consent. The Verge adds that he does not appear to have told it not to share it either.</td></tr>
<tr><td>What did he say caused it?</td><td>The first prompt offered “Allow One Time” or “Allow Always.” He chose Always, thinking approvals would still come for offers. That granted permission to send messages on his behalf using a template built from information he supplied, including the pickup address (The Verge; <a href="%(BI_MKT)s">Business Insider</a>).</td></tr>
<tr><td>What did Meta say?</td><td>Meta’s Muse team reviewed the logs with him and said it would make the permission prompt clearer. David Singleton of Meta Superintelligence Labs said Meta confirmed “no breach of privacy controls” (Business Insider).</td></tr>
<tr><td>Was there a price error?</td><td>Robb said a $600 offer looked accepted against his $700 minimum because a display glitch dropped the “7,” so the buyer saw “00 it is.” Singleton said that display issue was fixed (Business Insider).</td></tr>
<tr><td>What happened at the end?</td><td>A buyer came to his building. Robb said he lives in an apartment with security, resolved the mix-up with the buyer, and the buyer later bought another item (The Verge; Business Insider).</td></tr>
</tbody>
</table>
</div>
<p><a href="%(PC_MKT)s">PCMag</a> carried the same account with an update dated 29 September. Robb suggested a “Sent By Muse” label under agent-written messages so recipients can tell them apart from human ones (Business Insider). Whether Meta will add one is not officially announced.</p>
<h2>What this does and does not show</h2>
<p>It shows a permission choice with wide effect. It is a single user’s account, plus Meta’s replies. The articles checked for this note do not report another user affected in the same way. The Verge also lists two separate earlier Muse stories in the same article: a zero-day that Meta patched the week before, and Amazon blocking Muse from its retail platform over credential concerns. This page does not evaluate those.</p>
<p>Meta’s own description of Muse says nothing publishes, sends, or spends without approval (<a href="%(MUSE_BIZ)s">29 September post</a>). Meta’s Help Center pages on how Muse handles privacy and works with your approval are the place to read current permission behavior. Their text did not load in the check used for this note, so the exact names of Muse’s permission modes are not stated here.</p>
<p>What Muse is and how it is set up: <a href="/muse/">What is Muse</a>. Dots has its own approval design, summarized on <a href="/dots-security-privacy/">Dots security and privacy</a>.</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Selling or replying to strangers:</strong> choose the one-time option on the first prompt, and ask Muse to show you a draft before anything goes out.</li>
<li><strong>You already chose an “always” option:</strong> open Muse’s permission settings and review what is granted. Where they are in the app is not officially announced in the sources checked.</li>
<li><strong>Anything involving your address, phone, or payment details:</strong> keep them out of standing templates. Give them at the moment of need.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>Grok Bot has a similar choice. Its approvals offer Allow once, Always allow, and Deny, and its docs warn against broad “allow everything” rules (<a href="%(G_SEC)s">docs</a>). Nothing in the Muse reports involves Grok Bot. If you move a task between products, redo the permission decision each time. The products are compared on <a href="/muse-vs-grok-bot/">Muse vs Grok Bot</a>.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Treating “Allow Always” as “always ask me later.”</li>
<li>Putting sensitive details into a template an agent can reuse.</li>
<li>Assuming the buyer knows a message came from an agent.</li>
<li>Reading “no breach of privacy controls” as “no harm.” Both are reported: Meta’s statement and Robb’s experience.</li>
</ul>
</div></section>
''' % dict(V_MKT=V_MKT, BI_MKT=BI_MKT, PC_MKT=PC_MKT, MUSE_BIZ=MUSE_BIZ, G_SEC=G_SEC)
    sources = [
        ("The Verge, 29 September 2026", V_MKT),
        ("Business Insider, September 2026", BI_MKT),
        ("PCMag, updated 29 September 2026", PC_MKT),
        ("Meta, Muse for Small Business, 29 September 2026", MUSE_BIZ),
        ("xAI docs, Approvals, security, and privacy", G_SEC),
    ]
    return _shell(
        "Unofficial notes · Muse",
        "Meta Muse and the Marketplace address incident, as reported",
        "One YouTuber says Muse shared his address with a Marketplace buyer. This page lists what The Verge and Business Insider reported and what Meta said.",
        inner, MKT_FAQS, sources,
    ), MKT_FAQS


# ---------------------------------------------------------------- devday recap

DD_FAQS = [
    ("What is GPT-6.1 Sol?",
     "OpenAI’s 29 September 2026 upgrade to GPT-6 Sol. <a href=\"%s\">OpenAI</a> says it nearly matches GPT-6 Astra on agentic coding, computer use, and professional work at one-fifth of Astra’s standard input and output token prices." % O_SOL),
    ("Do dots run on GPT-6.1 Sol?",
     "OpenAI says dots are powered by GPT-6 Astra. The sources checked do not say dots have moved to Sol. Not officially announced."),
    ("Is 6.1 Sol in the free ChatGPT?",
     "OpenAI’s Sol page lists Plus, Pro, Business, Enterprise, and Edu in ChatGPT Work and Codex, and says it is not yet available in Chat. Free and Go are not listed."),
    ("When was DevDay 2026?",
     "29 September 2026, in San Francisco, per <a href=\"%s\">CNBC</a>." % CNBC),
]


def openai_devday_2026_dots_recap():
    inner = '''
<section class="band"><div class="wrap">
<h2>Dots at DevDay 2026</h2>
<p>OpenAI opened the dots rollout at <a href="%(CNBC)s">DevDay on 29 September 2026</a>. Its <a href="%(O_RECAP)s">recap post</a> counts more than 20 announcements and lists dots first: “remarkably capable, always-on agents,” available on Pro and Business Premium in eligible markets, with an Enterprise, Edu, and Healthcare beta when a workspace admin enables it, off by default. Eligibility, regions, and setup are on <a href="/how-to-get-openai-dots/">How to get OpenAI dots</a>. Protections are on <a href="/dots-security-privacy/">Dots security and privacy</a>. What is still open is on <a href="/dots-not-officially-announced/">Dots: what is not officially announced</a>.</p>
<h2>GPT-6.1 Sol, the “6.1 Sol” in search trends</h2>
<p>“6.1 Sol” is GPT-6.1 Sol, a model, not a dots feature. <a href="%(O_SOL)s">OpenAI’s launch page</a>:</p>
<div class="table-wrap">
<table>
<thead><tr><th>Item</th><th>What OpenAI says</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>An upgrade to GPT-6 Sol that nearly matches GPT-6 Astra on agentic coding, computer use, and professional work.</td></tr>
<tr><td>Price</td><td>One-fifth of Astra’s standard input and output token prices. API: $2 per million input tokens, $0.10 cached input, $10 per million output tokens; model name gpt-6.1-sol.</td></tr>
<tr><td>Where</td><td>All Plus, Pro, Business, Enterprise, and Edu users in ChatGPT Work and Codex. Not yet in Chat. Also the API.</td></tr>
<tr><td>Speed</td><td>GPT-6.1 Sol Ultrafast is “coming soon.” No date is given.</td></tr>
<tr><td>Own comparisons</td><td>On DeepSWE v1.1, OpenAI says it matches Astra at roughly one-fifth of the cost. These are OpenAI’s benchmarks, and OpenAI notes its evaluations of competitors come from public reports.</td></tr>
</tbody>
</table>
</div>
<p><a href="%(TNW)s">The Next Web</a> adds that OpenAI cancelled the October launch of GPT-6.1 Astra after failed safety tests. That is The Next Web’s report; the recap and Sol pages checked do not discuss it.</p>
<h2>Other DevDay items that touch dots</h2>
<ul>
<li><strong>ChatGPT Space:</strong> a shared place where teammates, ChatGPT, and your dot build on shared knowledge. Available on Pro, Business, and Enterprise on desktop app and web; mobile creation and editing are coming soon.</li>
<li><strong>Pages:</strong> documents built for human and agent collaboration, on Pro, Business, and Enterprise.</li>
<li><strong>Pro 500:</strong> a new tier with 25 times the ChatGPT Plus allowance and access to Ultrafast, “available now.” The recap prints no dollar price.</li>
<li><strong>Ultrafast:</strong> up to 8 times faster token generation in Codex and up to 6 times in the API. GPT-6 Astra Ultrafast is on Pro 500 and Enterprise. It is separate from dots.</li>
<li><strong>Plugin extensions:</strong> a way for developers to give a plugin a sidebar home in ChatGPT. Dots reach apps through plugins, and the launch post says over 4,000 apps.</li>
<li><strong>Sign in with ChatGPT:</strong> use plan allowance across 16 partners, including OpenClaw.</li>
<li><strong>Agents API with computer use, and Bedrock Managed Agents:</strong> developer products for building your own agents. They are not dots.</li>
</ul>
<p>Specialist dots for organizations, with their own identity and access, are in pilots, and OpenAI says it is working with Microsoft to bring them to Agent 365 (<a href="%(O_INTRO)s">launch post</a>).</p>
<h2>Solutions for advanced users</h2>
<h3>Choose by scenario</h3>
<ul>
<li><strong>Developer building agents:</strong> the Agents API and Sol are the announced routes, not dots. Read the recap entries for your plan.</li>
<li><strong>Coding cost:</strong> Sol is the lower-priced model in OpenAI’s own comparison. Verify on your workload; benchmarks are OpenAI’s.</li>
<li><strong>Someone who wants an assistant that works while away:</strong> dots, if eligible. See <a href="/dots-vs-chatgpt/">Dots vs ChatGPT</a>.</li>
</ul>
<h3>Use with Grok Bot, or move</h3>
<p>The DevDay announcements do not describe interoperability with Grok Bot. If you use Grok Bot for parallel roles, DevDay does not change that. Compare the agent products on <a href="/dots-vs-grokbot/">Dots vs Grok Bot</a>.</p>
<h3>Common pitfalls</h3>
<ul>
<li>Reading “Available today” for a model as availability for dots, or the reverse.</li>
<li>Assuming Sol is in the main Chat view. OpenAI says it is not yet.</li>
<li>Treating a benchmark as your result.</li>
<li>Mixing Pro and Pro 500 in budgeting.</li>
</ul>
</div></section>
''' % dict(CNBC=CNBC, O_RECAP=O_RECAP, O_SOL=O_SOL, TNW=TNW, O_INTRO=O_INTRO)
    sources = [
        ("OpenAI, DevDay 2026 recap, 29 September 2026", O_RECAP),
        ("OpenAI, Introducing GPT-6.1 Sol", O_SOL),
        ("OpenAI, Introducing dots", O_INTRO),
        ("CNBC DevDay live blog, 29 September 2026", CNBC),
        ("The Next Web, 29 September 2026", TNW),
    ]
    return _shell(
        "Unofficial notes · DevDay",
        "OpenAI DevDay 2026: dots and GPT-6.1 Sol recap",
        "What OpenAI announced for dots at DevDay on 29 September 2026, plus what “6.1 Sol” means. Sourced from OpenAI’s own pages.",
        inner, DD_FAQS, sources,
    ), DD_FAQS


CLUSTER2 = [
    ("/muse-vs-grok-bot/", "Muse vs Grok Bot: where they differ, by their own pages", muse_vs_grok_bot),
    ("/dots-security-privacy/", "Dots security and privacy: what OpenAI says and tested", dots_security_privacy),
    ("/dots-vs-chatgpt/", "Dots vs ChatGPT, and how Claude differs", dots_vs_chatgpt),
    ("/how-to-get-openai-dots/", "How to get OpenAI dots: plan, region, and setup", how_to_get_openai_dots),
    ("/dots-not-officially-announced/", "Dots: what is not officially announced", dots_not_officially_announced),
    ("/muse-charm/", "Muse Charm: what Meta said, what is only reported", muse_charm),
    ("/meta-muse-marketplace-issue/", "Meta Muse and the Marketplace address incident, as reported", meta_muse_marketplace_issue),
    ("/openai-devday-2026-dots-recap/", "OpenAI DevDay 2026: dots and GPT-6.1 Sol recap", openai_devday_2026_dots_recap),
]
