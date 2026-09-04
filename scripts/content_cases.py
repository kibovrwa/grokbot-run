# -*- coding: utf-8 -*-
from html import escape

# Starter jobs are original briefs on this site. They follow the official
# "own one outcome, stop at review" pattern from docs.x.ai/grok-bot/use-cases
# and docs.x.ai/grok-bot/get-started. They are not a reprint of those pages.
JOBS = [
    {
        "id": "warmup",
        "tag": "Five minutes",
        "name": "Warm-up: one document",
        "owns": "A cited brief from a file you attach. No connector. No login.",
        "prompt": (
            "I attached one document. Give me (1) five bullets on what it says, "
            "and (2) every date, decision, and open question with a page or section cite. "
            "Leave the file unchanged."
        ),
    },
    {
        "id": "digest",
        "tag": "Chief of Staff",
        "name": "Morning attention list",
        "owns": "What changed, what needs you, and what can wait. One door, not twelve Bots.",
        "prompt": (
            "You are my only door today. Review yesterday across my inbox, calendar, "
            "and meeting notes against the priorities I pasted. Return only items that "
            "map to those priorities. For each: source, why it matters, the next step, "
            "and whether I owe a decision. Do not send messages, create more Bots, or change meetings."
        ),
    },
    {
        "id": "inbox",
        "tag": "Ops",
        "name": "Inbox to drafts",
        "owns": "A sorted pile plus replies in your voice. You still hit send.",
        "prompt": (
            "Walk this inbox. Group messages into needs me, can wait, and junk. "
            "Draft replies in my voice for the first group only. "
            "Do not send, archive, unsubscribe, or delete."
        ),
    },
    {
        "id": "sales",
        "tag": "Sales",
        "name": "Outbound research pack",
        "owns": "Scored accounts and review-ready drafts. No enroll, no send.",
        "prompt": (
            "Research the accounts in this list (or this CRM view). Score each against "
            "the ICP I attached and any recent intent you can show. Name up to three "
            "contacts per account and draft email plus LinkedIn in the style samples. "
            "Skip anyone already in a sequence. Return a review list. Do not send or enroll anyone."
        ),
    },
    {
        "id": "declutter",
        "tag": "Life",
        "name": "Declutter audit",
        "owns": "A numbered list of unused mail, Drive clutter, and paid subs. Approval before any cut.",
        "prompt": (
            "Audit email, Drive, and paid subscriptions. Return a numbered list of what "
            "looks unused and the evidence. Wait for my yes before you delete, unsubscribe, or spend."
        ),
    },
    {
        "id": "travel",
        "tag": "Life",
        "name": "Travel hunt",
        "owns": "Keep-or-switch options with fees. The last click stays yours.",
        "prompt": (
            "Find the upcoming trip in my calendar or the confirmation I pasted. "
            "Compare the booked fare and stay with three cheaper options, including change fees. "
            "Recommend keep or switch, with the total after fees. "
            "Do not book, cancel, or enter payment."
        ),
    },
]

GUIDES = [
    ("Official Get started", "Install, name the Bot, then a five-part first task.", "https://docs.x.ai/grok-bot/get-started"),
    ("Official use cases", "Eight roles with a first prompt each. Read-and-prepare, then a routine.", "https://docs.x.ai/grok-bot/use-cases"),
    ("@bot: jobs people ran this week", "Official X recap of 11 field jobs, each quoting the original post.", "https://x.com/bot/status/2090168861912170972"),
    ("Debbie: how to start", "Name the job, sign in on the computer, start with one Chief of Staff.", "https://debbie.codes/blog/how-to-get-started-with-grok-bot"),
    ("Peter Yang: five to try", "Advisor, YouTube researcher, X scout, inbox declutter, travel concierge.", "https://www.youtube.com/watch?v=MkVcHbviYOw"),
    ("Nate: two Bots, not twelve", "Review of a first day. Start with work that finishes, not a briefing.", "https://natesnewsletter.substack.com/p/grok-bot-review"),
    ("Honest early verdict", "One reversible job first. Shared computer and weekly usage are the real limits.", "https://greenlitbooks.com/field-notes/grok-bot-honest-assessment"),
    ("Run a first week", "Company OS files, a Chief of Staff, then a daily plan that cites sources.", "https://refoundai.com/blog/how-to-run-your-business-with-grok-bot/"),
    ("Grok Bot for PMs", "Official-adjacent roster: Chief of Staff plus narrow specialists. Sends stay behind review.", "https://x.ai/bot/guides/grok-bot-for-pms"),
]

# Official @bot weekly recap (2026-08-19). Each line quotes a field post.
X_WEEK = [
    ("Text a robot vacuum", "Yun-Ta", "https://x.com/yunta_tsai/status/2089223114416898288"),
    ("Build a site, buy the domain, deploy", "Wayne Sutton", "https://x.com/waynesutton/status/2088416215203295346"),
    ("24/7 digital declutter", "Peter Yang", "https://x.com/petergyang/status/2089724101070086482"),
    ("Support mail and refunds", "Gergely Orosz", "https://x.com/GergelyOrosz/status/2090085668768694562"),
    ("Custom game art assets", "Danny Limanseta", "https://x.com/DannyLimanseta/status/2087228218797617404"),
    ("Office manager for a shop", "Jon ONeill", "https://x.com/HouseHackerJon/status/2087635639701573962"),
    ("Play a retro game on the cloud PC", "Peter Yang", "https://x.com/petergyang/status/2089502606079197347"),
    ("Sit in on a missed meeting", "Kiara", "https://x.com/kiaraplds/status/2088321112073547835"),
    ("Drive an Arduino LED ticker", "KettlebellDan", "https://x.com/KettlebellDan/status/2089387837204693202"),
    ("Chase merchant refunds", "Darian Shirazi", "https://x.com/darian314/status/2089381004524093752"),
    ("Overnight sales prospecting", "Krista Letz", "https://x.com/kristaletz/status/2089103618121314689"),
]

# High-star GitHub fetched 2026-09-04. Skip reconstructed clients and grok.com prompt dumps.
OSS = [
    ("OpenMausBot · 2.1k★", "Self-hosted alternative with a VM the bots can use. Apache-2.0. Not the official client.", "https://github.com/milind-soni/OpenMausBot"),
    ("rakazo · 1.9k★", "Bring your own model and sandbox. Web, Electron, Expo. Apache-2.0.", "https://github.com/elie222/rakazo"),
    ("gawkbot · 1.3k★", "Local-first: npx gawkbot. Approval gate on every send. Not xAI’s cloud computer.", "https://github.com/najmuzzaman-mohammad/gawkbot"),
    ("opengrok · 417★", "Model picker inside the official Grok Bot app. Keys stay on your machine. Third-party.", "https://github.com/OnlyTerp/opengrok"),
    ("plugin-marketplace · 211★", "Official xAI .grok-plugin catalog that Grok Bot inherits under Cursor plugin policy.", "https://github.com/xai-org/plugin-marketplace"),
    ("botdirectory.ai · 160★", "Paste-ready agent prompts for Grok Bot and Rakazo. Community directory.", "https://github.com/elie222/botdirectory.ai"),
    ("awesome-grok-bot · 220★", "Upstream CC0 list this catalog is built from.", "https://github.com/RongleCat/awesome-grok-bot"),
]

# Skills with a documented Grok Bot install path and real maintenance. Skip 0–1★ dumps.
SKILLS = [
    ("Compound Engineering · 24.8k★", "Install once in the Cursor marketplace. Grok Bot inherits that plugin library. Do not clone the repo onto the Bot computer.", "https://github.com/EveryInc/compound-engineering-plugin"),
    ("superpowers · marketplace", "Largest general skill pack Grok Bot can load through Cursor: plan, debug, write.", "https://github.com/obra/superpowers"),
    ("Aaron Marketing Skills · 2.7k★", "120 marketing skills as an 8-bot staff on Grok Bot. Named teammates, not a SKILL.md dump.", "https://github.com/aaron-he-zhu/aaron-marketing-skills"),
    ("Grok Ship · 156★", "Grok-Bot-native software factory. Tell a Bot to follow GROK_SHIP.md. Scout vs ship; you merge.", "https://github.com/kunchenguid/grok-ship"),
    ("Gojiberry Sales OS · 93★", "Outbound pack with a hosted MCP. Intent, enrich, LinkedIn, replies — do not invent contacts.", "https://github.com/romangojiberryAI/gojiberryai-sales-os"),
    ("Vercel plugin · 275★", "Official Vercel connector: deployments, logs, domains. Watch the OAuth redirect thread.", "https://github.com/vercel/vercel-plugin"),
    ("xAI plugin marketplace · 211★", "Official .grok-plugin catalog. Browse here, then install through Cursor / Grok Bot plugins.", "https://github.com/xai-org/plugin-marketplace"),
]

X_THREADS = [
    ("Five starter workflows", "GrokBotDev", "Inbox detox, a weekly “be happier” pass, a grocery team, a morning YouTube brief, then one Chief of Staff.", "https://x.com/GrokBotDev/status/2092676148220117421"),
    ("21 jobs from the official recap", "klöss", "Chief of Staff, office manager, inbox purge, outbound in your voice, CRM hygiene, refund recovery — a map of the @bot thread.", "https://x.com/kloss_xyz/status/2090579024313799107"),
    ("Chief of Staff in 15 minutes", "Dan McAteer", "Pasted a CoS guide, connected Gmail, Slack, Jira, and Granola. Field note, not a billed outcome.", "https://x.com/daniel_mac8/status/2091978532477940014"),
    ("One job per Bot", "s1rozha", "Email Bot at 7:30, sponsor-lead labels on a timer, calendar Bot separate. The trick is stopping using it as chat.", "https://x.com/s1rozha_/status/2091585690957996515"),
    ("One-person company stack", "Greg Isenberg", "Friend’s newsletter desk on Grok Bot agents. Best-practices thread — treat as a pattern, not a revenue claim.", "https://x.com/gregisenberg/status/2090901264309875088"),
    ("Connect Stripe Link, then shop", "@bot", "Official: Bot raises a spend request; you approve; a one-use card appears. US first. Approval stays with you.", "https://x.com/bot/status/2093419921007108385"),
]

# English summaries keyed by source URL. Do not invent outcomes.
CASES = [
    {"cat": "Engineering / product teams", "who": "n2parko", "job": "Product roster and PR handoffs",
     "en": "SpaceXAI product publicly showed a roster of Chief of Staff + eng manager + five eng ICs + Databricks + PM, with screenshots of agents handing off PRs. This site did not independently verify outcomes beyond those screenshots.",
     "url": "https://x.com/n2parko/status/2087251704744235298"},
    {"cat": "Architecture observations", "who": "Lee Robinson", "job": "Four technical bets",
     "en": "Public discussion of product shape: thin UI, thin client / thick server, always-on computer, browser as a first-class tool. Design observation, not a completed business case.",
     "url": "https://x.com/leerob/status/2089169319099777364"},
    {"cat": "Life / shopping", "who": "Debbie", "job": "Booking flights",
     "en": "Author had a Bot act as travel assistant on airline sites. Her conclusion: nearly usable, but missing the last click; the video shows the attempt and failure points. She did not claim a completed ticket.",
     "url": "https://debbie.codes/blog/i-tested-if-grok-bot-could-book-my-flights"},
    {"cat": "Life / shopping", "who": "Debbie", "job": "Sunday-night gluten-free beer",
     "en": "Chief of Staff + home Bot: added paper towels from the phone and completed an order; built a gluten-free beer cart on a grocery site and picked a delivery window. Login was hard on phone; desktop takeover got in. Author stresses this is computer use, not chat.",
     "url": "https://debbie.codes/blog/i-sent-grok-bot-to-buy-my-gluten-free-beer"},
    {"cat": "Life / shopping", "who": "Yun-Ta", "job": "Booking a table while walking",
     "en": "Mixed Chinese/English voice; Bot scanned the calendar and booked a restaurant. Outcome as claimed by the author; this site did not reproduce it.",
     "url": "https://x.com/yunta_tsai/status/2087415205756391461"},
    {"cat": "Engineering / product teams", "who": "Gota", "job": "One roster, twelve jobs",
     "en": "Public roster covering image factory, research briefs, 3D, travel debates, unsubscribe, running a local LLM in a VM, and more. Job list, not a per-item acceptance report.",
     "url": "https://x.com/gota_bara/status/2087666940450152841"},
    {"cat": "Ops / admin", "who": "Box", "job": "Credit committee pack",
     "en": "Reconciled materials, then wrote back to Box via MCP. Details in the original post.",
     "url": "https://x.com/Box/status/2087275866950938662"},
    {"cat": "Engineering / product teams", "who": "mrfundman", "job": "Teaching a WordPress update once",
     "en": "Used Teach a task on a real CMS instead of writing a deploy script first.",
     "url": "https://x.com/mrfundman/status/2089760255890571404"},
    {"cat": "Engineering / product teams", "who": "KettlebellDan", "job": "Arduino updates",
     "en": "Bot pushed hardware updates so the author did not have to watch X. Same author also has an LED ticker case.",
     "url": "https://x.com/KettlebellDan/status/2089920364419874937"},
    {"cat": "Engineering / product teams", "who": "Nate", "job": "Eight hours, twelve Bots",
     "en": "Review article asks whether a high-tier seat is worth it and shows a real day-one roster. Dollar amounts follow the original; this site does not restate unverified bills.",
     "url": "https://natesnewsletter.substack.com/p/grok-bot-review"},
    {"cat": "Ops / admin", "who": "YouTube demo", "job": "~19 minutes to 24/7 support",
     "en": "Uses routines to stand up a support Bot instead of rewriting a ticketing system. Duration from title/summary; this site did not time it.",
     "url": "https://www.youtube.com/watch?v=bUALqTpUze0"},
    {"cat": "Engineering / product teams", "who": "Farzad", "job": "Webby / Shotry / Writey",
     "en": "Named specialists plus an orchestrator — a shape that keeps recurring in the community. Original post includes team screenshots.",
     "url": "https://x.com/farzyness/status/2087340859138224540"},
    {"cat": "Research / briefs", "who": "Sid", "job": "Polymarket daily settlement brief",
     "en": "Bot scanned markets that settled that day and wrote a report.",
     "url": "https://x.com/sidshekhar24/status/2089735218861326727"},
    {"cat": "Architecture observations", "who": "Logan", "job": "The unlock is the computer, not 4.6",
     "en": "Argument: without API, MCP, or a hosted browser, a Bot uses software like a human. Commentary, not a work ticket.",
     "url": "https://x.com/LoganJastremski/status/2089903051557491092"},
    {"cat": "Architecture observations", "who": "Japanese note", "job": "A week on the shared VM",
     "en": "Japanese hands-on notes on living on the shared VM. Read the original; this site does not excerpt long passages.",
     "url": "https://note.com/azumimusuhi/n/n0485219790bb"},
    {"cat": "Ops / admin", "who": "Peter Yang", "job": "Declutter Bot",
     "en": "Demo: audit email, Drive, and paid subscriptions; wait for approval before delete.",
     "url": "https://x.com/petergyang/status/2089724101070086482"},
    {"cat": "Ops / admin", "who": "Gergely Orosz", "job": "Stripe support refunds",
     "en": "Connected a Bot to support email and Stripe to proxy refunds, with human confirmation before money moves.",
     "url": "https://x.com/GergelyOrosz/status/2090085668768694562"},
    {"cat": "Ops / admin", "who": "Mike P", "job": "Cleaning a huge inbox",
     "en": "Had a Bot walk two Gmail accounts and toss junk the owner would not touch by hand. Original post states scale; this site does not rewrite the numbers.",
     "url": "https://x.com/mikepat711/status/2089879632929554498"},
    {"cat": "Life / shopping", "who": "Yun-Ta", "job": "Texting a robot vacuum",
     "en": "Chief Engineer Bot talked with @maticrobots so the human could text the vacuum from anywhere.",
     "url": "https://x.com/yunta_tsai/status/2089223114416898288"},
    {"cat": "Engineering / product teams", "who": "Wayne Sutton", "job": "Ship a site from two phone prompts",
     "en": "Convex + Cloudflare plugins; tryground.dev live demo; bought domain and redirects from the phone. Details follow the original post.",
     "url": "https://x.com/waynesutton/status/2088416215203295346"},
    {"cat": "Creative production", "who": "Danny Limanseta", "job": "Card assets in two hours",
     "en": "Bot read the codebase, opened the author’s image-gen page, cropped transparent PNGs, and wired card assets back into the game. Counts follow the original post.",
     "url": "https://x.com/DannyLimanseta/status/2087228218797617404"},
    {"cat": "Ops / admin", "who": "Jon ONeill", "job": "Plumbing-shop office manager",
     "en": "Drain-and-sewer shop owner handed office-manager work to a Bot in the first 24 hours.",
     "url": "https://x.com/HouseHackerJon/status/2087635639701573962"},
    {"cat": "Life / shopping", "who": "Ben Lang", "job": "Internal job list",
     "en": "Public internal work examples: Starlink-leaning flights, recipes to Whole Foods, film-scan EXIF, contractor quotes, and more.",
     "url": "https://x.com/benln/status/2087929147406299313"},
    {"cat": "Research / briefs", "who": "Gavin Baker", "job": "Podcast summaries",
     "en": "Author compared Grok Bot to another Claude Code moment and said a podcast-summary setup came together quickly. Duration wording follows the original post.",
     "url": "https://x.com/GavinSBaker/status/2089379355692527813"},
    {"cat": "Sales / GTM", "who": "Krista Letz", "job": "Enterprise GTM roster",
     "en": "SpaceXAI enterprise sales roster: Chief of Staff, overnight prospecting, per-account specialists, live slide updates.",
     "url": "https://x.com/kristaletz/status/2089103618121314689"},
    {"cat": "Creative production", "who": "Peter Yang", "job": "Playing Commander Keen on the cloud desktop",
     "en": "Installed and played Commander Keen on the Grok Bot cloud desktop; author mentioned latency. Point: this is a real computer.",
     "url": "https://x.com/petergyang/status/2089502606079197347"},
    {"cat": "Meeting notes", "who": "Kiara", "job": "Bot sits in on a missed meeting",
     "en": "SpaceXAI field engineer had a Bot join a meeting she missed, introduce itself, and take notes.",
     "url": "https://x.com/kiaraplds/status/2088321112073547835"},
    {"cat": "Engineering / product teams", "who": "KettlebellDan", "job": "Arduino LED ticker",
     "en": "Bot talked to Arduino; the light board scrolled prices, spark lines, and SpaceX news. Code and hardware follow the original post.",
     "url": "https://x.com/KettlebellDan/status/2089387837204693202"},
    {"cat": "Ops / admin", "who": "Darian Shirazi", "job": "Chasing five merchant refunds",
     "en": "Bot found unrefunded returns in email and wrote five merchants. Author claimed recovery exceeded the monthly fee; that comparison is from the post — this site did not see the bill.",
     "url": "https://x.com/darian314/status/2089381004524093752"},
    {"cat": "Engineering / product teams", "who": "Grokularity", "job": "Site built by a Bot team",
     "en": "Non-coder said a Grok Bot team stood up grokularity.xyz in a day: humans read; only verified Grok agents write.",
     "url": "https://grokularity.xyz"},
    {"cat": "Sales / GTM", "who": "thoughtpilot99", "job": "Signal outbound recipe",
     "en": "GitHub recipe: hunt buyer signals, return a ranked list, draft two outreach scripts for a human to send.",
     "url": "https://github.com/thoughtpilot99/signal-outbound-grok-bot"},
    {"cat": "Trading experiments", "who": "jjregier", "job": "Grok-Bot-Fund",
     "en": "Personal paper-to-live “hedge fund” desk with three Grok Bot teammates on the cloud computer; versioned playbook merges only via human PRs. Experimental — read the repo; not a return promise.",
     "url": "https://github.com/jjregier/Grok-Bot-Fund"},
    {"cat": "Research / briefs", "who": "WebDevJasonCameron", "job": "Market research desk",
     "en": "File-based market research desk: company mission, analyst instructions, scored opportunities, decision log, same repo layout.",
     "url": "https://github.com/WebDevJasonCameron/ExploreGrokBot"},
    {"cat": "Engineering / product teams", "who": "mtrxdev", "job": "build-brief into local grok",
     "en": "Reusable desk that interrogates a raw idea into a grounded Grok Build brief (PROFILE + BOT-SKILL + check gates), print-first, then paste into local grok. Target output is Grok Build, not Grok Bot itself.",
     "url": "https://github.com/mtrxdev/build-brief"},
    {"cat": "Trading experiments", "who": "HammeredSmithy", "job": "Bull Desk / Webull",
     "en": "Seven-agent trading desk ported to Webull OpenAPI (US users): research, positions, id-gated execution approval and review; paper sandbox before live keys. Experimental.",
     "url": "https://github.com/HammeredSmithy/bull-trade"},
    {"cat": "Sales / GTM", "who": "jay-sahnan", "job": "Self-serve growth team",
     "en": "Shareable multi-Bot growth team (growth lead + specialists), narrow roles with handoffs; human approval before shipping or outreach.",
     "url": "https://github.com/jay-sahnan/growth-grok-bots"},
    {"cat": "Research / briefs", "who": "palehonk0-o", "job": "Market memory pack",
     "en": "Evidence-first implementation pack: use Grok Bot to turn public pages into decision briefs, paired with a public X article walkthrough.",
     "url": "https://github.com/palehonk0-o/grokbot-market-memory"},
    {"cat": "Engineering / product teams", "who": "Logos52", "job": "Fleet public packet dump",
     "en": "Weekday public dump of files a Grok Bot fleet writes under /workspace on the shared cloud computer, mirrored for Mac /fold skill intake.",
     "url": "https://github.com/Logos52/grok-bot-packets"},
    {"cat": "Engineering / product teams", "who": "jblack4vols", "job": "Per-Bot durable knowledge log",
     "en": "Durable logs for a real roster: decisions, delivered work, and long-term preferences dated in America/New_York.",
     "url": "https://github.com/jblack4vols/grok-bot"},
    {"cat": "Ops / admin", "who": "bilauitmcuti", "job": "UiTM calendar + MCP",
     "en": "Malaysia UiTM academic calendar assistant on Grok Bot; remote MCP supplies class, holiday, and exam dates.",
     "url": "https://github.com/bilauitmcuti/bot"},
    {"cat": "Architecture observations", "who": "Greenlit Books", "job": "One reversible job, not a reorg",
     "en": "Field note: the product is approachable, still early. Start with a checkable, reversible workflow. Weekly usage, the shared computer, and money folklore are the real limits. Dollar claims in social posts are mostly unverifiable.",
     "url": "https://greenlitbooks.com/field-notes/grok-bot-honest-assessment"},
    {"cat": "Ops / admin", "who": "Refound", "job": "Five-day company OS",
     "en": "Written first-week: put standing rules in the Bot description, cite source-of-truth files, plan the day with sources shown, then hang a routine only after the brief is reviewable. External actions stay behind approval.",
     "url": "https://refoundai.com/blog/how-to-run-your-business-with-grok-bot/"},
    {"cat": "Engineering / product teams", "who": "xAI guides", "job": "PM roster that stays quiet",
     "en": "Official-adjacent PM writeup: Chief of Staff owns calendar, Slack, and inbox; specialists stay narrow. Author still reviews external sends, purchases, and deletes.",
     "url": "https://x.ai/bot/guides/grok-bot-for-pms"},
    {"cat": "Architecture observations", "who": "xAI docs", "job": "Eight official starter roles",
     "en": "Official use-cases page: sales outbound, talent scout, paid media, expense manager, product performance, bug reproduction, account health, Chief of Staff. Each role owns one outcome and starts as read-and-prepare work.",
     "url": "https://docs.x.ai/grok-bot/use-cases"},
    {"cat": "Research / briefs", "who": "Composio", "job": "Parallel research swarm",
     "en": "Practitioner guide: persistent teammates on a cloud computer, then bonus jobs such as a competitive-intel swarm, an open-source audit, and a fact-check engine. Treat as a pattern list, not a shipped outcome report.",
     "url": "https://composio.dev/content/guide-to-frok-bot"},
    {"cat": "Life / shopping", "who": "techAU", "job": "Shopping with Stripe Link",
     "en": "Field writeup of Bot shopping via Stripe Link: the Bot can raise a spend request; you approve in Link; only then does a one-time card appear at checkout. Vague briefs produce vague carts. Approval still sits with you.",
     "url": "https://techau.com.au/grok-bot-can-now-go-shopping/"},
    {"cat": "Architecture observations", "who": "@bot", "job": "Official weekly field recap",
     "en": "Official 2026-08-19 thread: eleven jobs people actually ran that week, each quoting the original post. Vacuum, site deploy, declutter, refunds, game art, office manager, meetings, LED ticker, prospecting.",
     "url": "https://x.com/bot/status/2090168861912170972"},
    {"cat": "Life / shopping", "who": "@bot", "job": "Buy things with Stripe Link",
     "en": "Official 2026-08-28: connect Link, send the Bot shopping, approve every spend request, then a single-use card is minted. US first; mobile later. This is delegated checkout, not unattended spending.",
     "url": "https://x.com/bot/status/2093419921007108385"},
    {"cat": "Ops / admin", "who": "GrokBotDev", "job": "Five starter workflows",
     "en": "X thread with five first jobs: six-month newsletter detox (keep vs unsubscribe), a weekly “be happier” pass from mail and calendar, a three-Bot grocery team, a 7am YouTube summary, then one Chief of Staff.",
     "url": "https://x.com/GrokBotDev/status/2092676148220117421"},
    {"cat": "Architecture observations", "who": "klöss", "job": "21 jobs mapped from @bot",
     "en": "Community map of the official weekly recap: Chief of Staff, office manager, inbox purge, outbound in voice, CRM hygiene, refund recovery, and more. A list, not a per-item acceptance report.",
     "url": "https://x.com/kloss_xyz/status/2090579024313799107"},
    {"cat": "Ops / admin", "who": "Dan McAteer", "job": "Chief of Staff in 15 minutes",
     "en": "Author said a CoS was working in about 15 minutes after connecting Gmail, Slack, Jira, and Granola. Duration and connectors follow the post; this site did not time it.",
     "url": "https://x.com/daniel_mac8/status/2091978532477940014"},
    {"cat": "Ops / admin", "who": "s1rozha", "job": "One job per Bot, on a timer",
     "en": "Public setup: an email Bot at 7:30, sponsor-lead labels on a work-hours timer, a separate calendar Bot. Author’s point: stop using Grok Bot as chat.",
     "url": "https://x.com/s1rozha_/status/2091585690957996515"},
    {"cat": "Sales / GTM", "who": "Greg Isenberg", "job": "Newsletter desk as a one-person company",
     "en": "Thread: a friend runs a newsletter business on Grok Bot agents, with a best-practices list for non-technical operators. Pattern post — not a verified P&L.",
     "url": "https://x.com/gregisenberg/status/2090901264309875088"},
    {"cat": "Ops / admin", "who": "RoundtableSpace", "job": "Daily job list for a first roster",
     "en": "Public job menu: inbox, daily briefing, expenses, calendar, research, account management, notes prep. A menu of roles, not a shipped-outcome report.",
     "url": "https://x.com/RoundtableSpace/status/2089030676678938899"},
]


def _job_html(job):
    return (
        '<article class="job-card" id="job-%s">'
        '<p class="kicker">%s</p>'
        "<h3>%s</h3>"
        "<p>%s</p>"
        "<pre><code>%s</code></pre>"
        '<button type="button" class="copy-btn" data-copy>Copy</button>'
        "</article>"
        % (
            escape(job["id"]),
            escape(job["tag"]),
            escape(job["name"]),
            escape(job["owns"]),
            escape(job["prompt"]),
        )
    )


def use_cases():
    cats = []
    for c in CASES:
        if c["cat"] not in cats:
            cats.append(c["cat"])
    btns = ['<button type="button" data-filter="all" aria-pressed="true">All %d</button>' % len(CASES)]
    for cat in cats:
        n = sum(1 for c in CASES if c["cat"] == cat)
        btns.append('<button type="button" data-filter="%s">%s %d</button>' % (escape(cat), escape(cat), n))
    cards = []
    for c in CASES:
        cards.append(
            '<article class="case-card" data-cat="%s"><p class="kicker">%s · %s</p><h3>%s</h3><p>%s</p><p><a href="%s">Source</a></p></article>'
            % (escape(c["cat"]), escape(c["cat"]), escape(c["who"]), escape(c["job"]), escape(c["en"]), escape(c["url"]))
        )
    guides = []
    for name, blurb, url in GUIDES:
        guides.append(
            '<a class="card" href="%s"><h3>%s</h3><p>%s</p></a>'
            % (escape(url), escape(name), escape(blurb))
        )
    x_week = []
    for job, who, url in X_WEEK:
        x_week.append(
            '<a class="card" href="%s"><h3>%s</h3><p>%s · original post</p></a>'
            % (escape(url), escape(job), escape(who))
        )
    x_threads = []
    for name, who, blurb, url in X_THREADS:
        x_threads.append(
            '<a class="card" href="%s"><p class="kicker">X · %s</p><h3>%s</h3><p>%s</p></a>'
            % (escape(url), escape(who), escape(name), escape(blurb))
        )
    oss = []
    for name, blurb, url in OSS:
        oss.append(
            '<a class="card" href="%s"><h3>%s</h3><p>%s</p></a>'
            % (escape(url), escape(name), escape(blurb))
        )
    skills = []
    for name, blurb, url in SKILLS:
        skills.append(
            '<a class="card" href="%s"><h3>%s</h3><p>%s</p></a>'
            % (escape(url), escape(name), escape(blurb))
        )
    body = '''
<section class="hero"><div class="wrap">
<p class="kicker">Use cases</p>
<h1>Grok Bot use cases — start with one job</h1>
<p class="lede">Pick one reversible job. Name the Bot after that job. Paste a brief that says what to return and when to stop. Do not stand up twelve Bots on day one.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="#starter-jobs">Copy a starter job</a>
  <a class="btn btn-secondary" href="#from-x">From X</a>
  <a class="btn btn-ghost" href="#skills">Skills</a>
  <a class="btn btn-ghost" href="#open-source">GitHub</a>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>How a first job should look</h2>
<p class="lede">Official Get started asks for five parts. Community writeups that actually shipped work use the same shape.</p>
<div class="grid-3">
<article class="card"><h3>One outcome</h3><p>A review list, a cited brief, or a keep-or-switch card — not “be my assistant.”</p></article>
<article class="card"><h3>Named sources</h3><p>Inbox, CRM view, attached file, or the site you will take over to sign in.</p></article>
<article class="card"><h3>A hard stop</h3><p>Do not send, enroll, delete, book, or pay until you say so. Description beats a later “stop.”</p></article>
</div>
</div></section>

<section class="band" id="starter-jobs"><div class="wrap">
<h2>Copy a starter job</h2>
<p class="lede">Original briefs on this site, written to the official pattern: own one outcome, start as read-and-prepare, keep money and sends behind approval. Open the <a href="https://docs.x.ai/grok-bot/use-cases">official use-cases</a> for the longer role list.</p>
<div class="job-grid">%s</div>
</div></section>

<section class="band" id="from-x"><div class="wrap">
<h2>From X — jobs people actually posted</h2>
<p class="lede">Official <a href="https://x.com/bot/status/2090168861912170972">@bot recap</a> on 2026-08-19 quoted eleven field posts (fetched 2026-09-04). Each card is the original. This site does not invent outcomes.</p>
<div class="grid-3">%s</div>
<h2>Threads worth opening</h2>
<p class="lede">High-signal X writeups that teach a first roster. Open the post; do not treat a list as a shipped result.</p>
<div class="grid-2">%s</div>
</div></section>

<section class="band" id="skills"><div class="wrap">
<h2>Skills worth installing first</h2>
<p class="lede">Most “Grok Bot skill” repos on GitHub are 0–1★ dumps. These have a documented Grok Bot or Cursor-marketplace install path and recent maintenance (checked 2026-09-04). A skill you save after two good runs still beats a random pack. Full catalog: <a href="/tools/">Tools</a>.</p>
<div class="grid-2">%s</div>
<div class="callout">
<p><strong>Skip the 195-skill catalogs.</strong> Repos that only ship a pile of SKILL.md files with no stars, no license review, and no Grok Bot install steps stay off this list.</p>
</div>
</div></section>

<section class="band" id="open-source"><div class="wrap">
<h2>High-star GitHub — not the official app</h2>
<p class="lede">Self-hosted alternatives and companion repos. They are not xAI’s Grok Bot. Side-by-side: <a href="/compare/">official vs OpenMausBot, rakazo, gawkbot, OpenClaw</a>. Reconstructed clients and grok.com prompt dumps are omitted on purpose.</p>
<div class="grid-2">%s</div>
</div></section>

<section class="band"><div class="wrap">
<h2>First week</h2>
<div class="roadmap">
<a class="step" href="/learn/install/"><div class="num">1</div><div><h3>Install and sign in</h3><p>Desktop or phone. Cursor account. Have one real login ready — empty demos burn the week.</p></div></a>
<a class="step" href="/learn/first-bot/"><div class="num">2</div><div><h3>One Bot, one job</h3><p>Short name. Paste a starter brief. Watch the computer. Take over for password and 2FA — never paste those into chat.</p></div></a>
<a class="step" href="/learn/computer/"><div class="num">3</div><div><h3>Correct, then save a skill</h3><p>Fix the output once. Ask it to keep that format. Save the method. All Bots share one computer.</p></div></a>
<a class="step" href="/learn/skills-routines/"><div class="num">4</div><div><h3>Routine only after two good runs</h3><p>Schedule the digest or the research pack. Tests do real things. Keep writes behind approval.</p></div></a>
</div>
<div class="callout warn">
<p><strong>Do not start with money, customer sends, or twelve Bots.</strong> Nate’s “eight hours, twelve Bots” is a review, not an ops plan. Debbie’s flights case stopped at the last click. Gergely’s refunds case still needed a human before money moved.</p>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Read these first</h2>
<p class="lede">Guides that teach a first roster. This site does not reprint them.</p>
<div class="grid-2">%s</div>
</div></section>

<section class="band" id="field-cases"><div class="wrap">
<p class="kicker">Field cases</p>
<h2>What people actually handed off</h2>
<p class="lede">%d sourced examples. English summaries here are original: who, what job, what the source claimed. Not independently reproduced. Numbers or returns not written in the source are never invented. Upstream list: <a href="https://github.com/RongleCat/awesome-grok-bot">awesome-grok-bot</a> (CC0).</p>
<div class="filters" data-filters>%s</div>
<input class="search" data-search placeholder="Filter by name, job, or keyword">
<div data-list>%s</div>
<p class="muted">Tutorials and failure modes: <a href="/sources/">Sources</a> and <a href="/troubleshooting/">Help</a>.</p>
</div></section>
<script>
document.querySelectorAll('[data-copy]').forEach(btn=>{
  btn.addEventListener('click', async ()=>{
    const pre=btn.parentElement.querySelector('pre');
    try {
      await navigator.clipboard.writeText(pre.innerText.trim());
      btn.textContent='Copied';
      setTimeout(()=>btn.textContent='Copy', 1600);
    } catch (e) { btn.textContent='Copy failed'; }
  });
});
const filters=document.querySelector('[data-filters]');
const list=document.querySelector('[data-list]');
const search=document.querySelector('[data-search]');
let cat='all';
function apply(){
  const q=(search.value||'').toLowerCase();
  filters.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed', b.getAttribute('data-filter')===cat ? 'true':'false'));
  list.querySelectorAll('.case-card').forEach(card=>{
    const okCat = cat==='all' || card.getAttribute('data-cat')===cat;
    const okQ = !q || card.textContent.toLowerCase().includes(q);
    card.classList.toggle('hidden', !(okCat && okQ));
  });
}
filters.addEventListener('click', e=>{
  const b=e.target.closest('button'); if(!b) return;
  cat=b.getAttribute('data-filter'); apply();
});
search.addEventListener('input', apply);
const pre=new URLSearchParams(location.search).get('q');
if(pre){ search.value=pre; }
apply();
</script>
''' % ("".join(_job_html(j) for j in JOBS), "".join(x_week), "".join(x_threads), "".join(skills), "".join(oss), "".join(guides), len(CASES), "".join(btns), "".join(cards))
    return body
