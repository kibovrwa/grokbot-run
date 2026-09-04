# -*- coding: utf-8 -*-
"""Per-URL keyword map from two live Google SERPs (CN, 2026-09-04).

SERP A — "grok bot" (Google rewrite of grokbot):
  Owners: x.ai/bot + sitelinks, grok.com (wrong product), Play, App Store,
  Cursor Help, YouTube, Lenny. Related: Grok 官网, app, Cursor grok bot,
  free, login, android, ios, plan.
  Do not fight x.ai/stores for the exact brand.

SERP B — grokbot / 您是不是要找 grok bot:
  Owners: grokbot.aihuangshu.com (橙皮书×Awesome 合并手册), App Store,
  财联社/东财「企业试用两周」, grokbot.cooking (无关), AWS Grok 广告,
  B站/YouTube, x.ai designing post, treg plugin.
  Domain grokbot.run can compete here as the clean fact hub — not a reprint.

Each URL owns one cluster. Do not repeat the same primary on two pages.
"""

# path -> title, description (110–160), primary, also, do_not
PAGES = {
    "/": {
        "title": "Grok Bot guide: how to start, login, plans, and fixes",
        "description": "How to start Grok Bot: Cursor login, a first job you can paste, one shared computer, dated plan conflicts, and Recover before Reset.",
        "h1": "How to start Grok Bot without burning a week",
        "primary": "Grok Bot guide / grokbot (modifier, not exact brand)",
        "also": "hub for related searches",
        "do_not": "exact 'Grok Bot' vs x.ai; Grok 官网",
    },
    "/learn/what-is-grok-bot/": {
        "title": "What is Grok Bot? Not grok.com, Grok, or Grok Build",
        "description": "What is Grok Bot: a named teammate plus one cloud computer. Why grok.com ranks for grok bot, how it differs from Grok chat, Grok Build, and grok-app.",
        "h1": "What is Grok Bot — not grok.com or Grok Build",
        "primary": "what is grok bot; grok bot vs grok / grok.com",
        "also": "grokbot meaning; grok-app",
        "do_not": "download, pricing numbers",
    },
    "/learn/install/": {
        "title": "Grok Bot app: download, login, iOS and Android",
        "description": "Grok Bot app download for Mac, Windows, Linux, iOS, and Android. Login is Cursor — no separate account. App Store, Google Play, and Legacy Privacy Mode.",
        "h1": "Install the Grok Bot app and log in",
        "primary": "grok bot app; grok bot login; grok bot ios; grok bot android",
        "also": "install grok bot; download grok bot; grok bot mac/windows",
        "do_not": "free/plan (pricing); how to use first Bot",
    },
    "/learn/first-bot/": {
        "title": "How to use Grok Bot: first Bot and Chief of Staff",
        "description": "How to use Grok Bot after login: short name, one job, Chief of Staff, and copyable first tasks that stop at drafts. Warm-up plus a morning digest.",
        "h1": "How to use Grok Bot: first Bot and Chief of Staff",
        "primary": "how to use grok bot; grok bot tutorial; first grok bot",
        "also": "chief of staff grok bot",
        "do_not": "app download; pricing",
    },
    "/learn/computer/": {
        "title": "Grok Bot computer: one shared cloud PC, not isolation",
        "description": "Grok Bot computer facts: all Bots share one user-assigned cloud computer and logins. Screens are not a security boundary. Recover and Update before Reset.",
        "h1": "The Grok Bot computer is shared — not a security boundary",
        "primary": "grok bot computer; shared computer; not a security boundary",
        "also": "isolation; cookies; /workspace",
        "do_not": "can't reach (troubleshooting)",
    },
    "/learn/skills-routines/": {
        "title": "Grok Bot skills, routines, and Teach a task",
        "description": "Grok Bot skills are how; routines are when. Teach a task records about ten minutes of screen, no mic. Save a skill after one good run, then automate.",
        "h1": "Grok Bot skills, routines, and Teach a task",
        "primary": "grok bot skills; grok bot routines; teach a task",
        "also": "grok bot automation",
        "do_not": "plugins/MCP OAuth bugs",
    },
    "/learn/plugins/": {
        "title": "Grok Bot plugins and MCP: connectors before the browser",
        "description": "Grok Bot plugins and remote MCP: prefer connectors over clicking the web. No local stdio. Fixes for Zoom 4700, Gmail, Notion, Canva, X, and GitHub OAuth.",
        "h1": "Grok Bot plugins first, browser as fallback",
        "primary": "grok bot plugins; grok bot mcp; grok bot connectors",
        "also": "zoom 4700; gmail oauth",
        "do_not": "third-party CLI catalog",
    },
    "/learn/operator/": {
        "title": "How operators run Grok Bot after week one",
        "description": "How operators run Grok Bot after week one: one Chief of Staff, Teach a task, a what's-left page, then routines. Named X field posts, no invented bills.",
        "h1": "How operators run Grok Bot after week one",
        "primary": "grok bot chief of staff; grok bot routines; manage grok bots",
        "also": "teach a task; multi-bot; operator",
        "do_not": "first install; invented prices",
    },
    "/learn/ops/": {
        "title": "Grok Bot ops: X, Cursor Cloud Agents, MCP, and the computer",
        "description": "How operators run X, Cursor Cloud Agents, remote MCP, and the shared Grok Bot computer. Named field posts. Drafts stay behind approval.",
        "h1": "How operators run X, Cursor, MCP, and the cloud computer",
        "primary": "grok bot twitter; grok bot x plugin; grok bot cloud agent",
        "also": "grok bot mcp workflow; operate x with grok bot",
        "do_not": "first install; OAuth bug list; isolation lecture; invented prices",
    },
    "/learn/cost-and-pitfalls/": {
        "title": "Grok Bot usage, On-Demand spillover, and cost pitfalls",
        "description": "Grok Bot weekly usage can spill into On-Demand with no in-app warning. How the pool and trial work, eligibility conflicts, and pitfalls that burn the week.",
        "h1": "Grok Bot usage, On-Demand, and cost pitfalls",
        "primary": "grok bot usage; on-demand; weekly pool; trial burns",
        "also": "no in-app warning",
        "do_not": "plan list / is it free (pricing)",
    },
    "/pricing/": {
        "title": "Grok Bot pricing: free, plan, Cursor, enterprise trial",
        "description": "Grok Bot pricing: is it free, which plan, Cursor access, and the enterprise two-week trial. Dated official eligibility — no invented list prices.",
        "h1": "Grok Bot pricing: free, plans, and enterprise trial",
        "primary": "grok bot free; grok bot plan; grokbot pricing; enterprise trial",
        "also": "grok bot cost; 企业试用两周",
        "do_not": "On-Demand spillover mechanics (cost page)",
    },
    "/troubleshooting/": {
        "title": "Grok Bot not working: can't reach computer, Reset, DNS",
        "description": "Grok Bot not working? Fixes for can't reach your computer, Reset vs Recover, usage spillover, plugin OAuth, Linux, and white screens, plus 89 failure sources.",
        "h1": "Grok Bot not working — fixes by symptom",
        "primary": "grok bot not working; can't reach your computer; reset",
        "also": "reconnecting; white screen; dns",
        "do_not": "what the computer is (computer lesson)",
    },
    "/learn/": {
        "title": "Grok Bot handbook: lessons from install to first job",
        "description": "Grok Bot handbook in reading order: what it is, install and Cursor login, first Bot, shared computer, skills, plugins, and cost. Start here if you are new.",
        "h1": "Grok Bot handbook — read in this order",
        "primary": "grok bot handbook; grok bot lessons",
        "also": "how grok bot works (order)",
        "do_not": "what is (lesson 1); how to use (first Bot)",
    },
    "/learn/glossary/": {
        "title": "Grok Bot glossary: Bot, computer, skill, routine, plugin",
        "description": "Grok Bot glossary for Bot, shared computer, skill, routine, plugin, MCP, Teach a task, and share templates. Short definitions, not a reprint of the docs.",
        "h1": "Grok Bot glossary",
        "primary": "grok bot glossary; skill vs routine vs plugin",
        "also": "what is a grok bot computer",
        "do_not": "full skills lesson; plugin OAuth bugs",
    },
    "/learn/cursor/": {
        "title": "Cursor Grok Bot: login, usage, and plugins — not the IDE",
        "description": "Cursor grokbot is not a Cursor IDE panel. Grok Bot is its own app: Cursor login, weekly usage, inherited plugins. Ultra is not required on every official page.",
        "h1": "Cursor Grok Bot: one account, two apps",
        "primary": "cursor grokbot; cursor grok bot; grok bot cursor account",
        "also": "cursor login; hermes vs grok bot",
        "do_not": "plan price list; install package steps",
    },
    "/compare/": {
        "title": "Grok Bot alternatives: OpenMausBot, rakazo, gawkbot, OpenClaw",
        "description": "Grok Bot alternatives compared: official managed computer vs OpenMausBot, rakazo, gawkbot, and OpenClaw. When to stay official and when to self-host.",
        "h1": "Grok Bot alternatives — official vs self-hosted",
        "primary": "grok bot alternative; open source grok bot; grok bot vs openclaw",
        "also": "rakazo; gawkbot; OpenMausBot; grokbot github",
        "do_not": "pricing numbers; official app download steps",
    },
    "/use-cases/": {
        "title": "Grok Bot use cases: starter jobs and field examples",
        "description": "Grok Bot use cases: copyable first jobs, X field posts, skills worth installing, and high-star GitHub alternatives. Each card links out.",
        "h1": "Grok Bot use cases — start with one job",
        "primary": "grok bot use cases; grok bot examples",
        "also": "sales; shopping; ops; first job",
        "do_not": "app download; pricing numbers",
    },
    "/tools/": {
        "title": "Grok Bot tools: CLI, TUI, Linux ports, usage meters",
        "description": "Grok Bot tools catalog: 199 CLI, TUI, plugin, MCP, Linux, and usage-meter entries. grok-app is a Grok Build GUI, not a Grok Bot client. Source links included.",
        "h1": "Grok Bot tools catalog",
        "primary": "grok bot tools; grok bot cli (hub)",
        "also": "grok-app disambiguation",
        "do_not": "official app download",
    },
    "/tools/grok-bot-cli/": {
        "title": "grok-bot-cli: terminal roster and messages for Grok Bot",
        "description": "grok-bot-cli is a macOS CLI that reuses a signed-in Grok Bot desktop session to list Bots and send messages. Install notes, risks, and the GitHub source.",
        "h1": "grok-bot-cli",
        "primary": "grok-bot-cli",
        "also": "",
        "do_not": "official app",
    },
    "/tools/grok-bot-skill/": {
        "title": "grok-bot-skill: let coding agents call Grok Bot teammates",
        "description": "grok-bot-skill lets Cursor or Claude coding agents call Grok Bot teammates. How it differs from the official app, install notes, risks, and source.",
        "h1": "grok-bot-skill",
        "primary": "grok-bot-skill",
        "also": "",
        "do_not": "",
    },
    "/tools/grokbot-tui/": {
        "title": "grokbot-tui: terminal UI for Grok Bot",
        "description": "grokbot-tui is a community terminal UI for Grok Bot keyboard workflows. Platforms, install path, differences from the desktop app, risks, and GitHub source.",
        "h1": "grokbot-tui",
        "primary": "grokbot-tui",
        "also": "",
        "do_not": "",
    },
    "/tools/usage-menu-bar/": {
        "title": "Grok Bot weekly usage menu bar for macOS",
        "description": "macOS menu bar meter for Grok Bot weekly usage. Cross-check the Cursor plans screen; install notes, limits, risks, and the upstream GitHub source.",
        "h1": "Grok Bot usage menu bar",
        "primary": "grok bot usage meter; menu bar",
        "also": "",
        "do_not": "pricing table",
    },
    "/tools/linux-port/": {
        "title": "Grok Bot Linux: official packages vs community port",
        "description": "Grok Bot Linux download: prefer official deb, rpm, and AppImage from x.ai/bot. Community port notes, rejected old builds, and GitHub source.",
        "h1": "Grok Bot on Linux: official packages vs community port",
        "primary": "grok bot linux",
        "also": "deb rpm appimage",
        "do_not": "ios/android",
    },
    "/sources/": {
        "title": "Grok Bot sources and fetch notes",
        "description": "Bibliography for this Grok Bot guide: 42 official materials, 89 failure threads, catalog and cases, plus URLs that timed out on fetch day 2026-09-04.",
        "h1": "Sources and fetch notes",
        "primary": "(citation, no head-term fight)",
        "also": "",
        "do_not": "guide / pricing / install",
    },
}


def meta(path):
    return PAGES[path]["title"], PAGES[path]["description"]
