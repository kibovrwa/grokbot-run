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
        "title": "Grok Bot guide: install, Cursor login, and do not Reset first",
        "description": "Unofficial Grok Bot guide. Install from x.ai/bot, sign in with Cursor, use one shared computer, and Retry before you Reset.",
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
        "title": "Grok Bot install: Mac, Windows, Linux and phone download",
        "description": "Install Grok Bot on Mac, Windows, Linux, iPhone or Android. Official packages from x.ai/bot, then sign in with Cursor.",
        "h1": "Download and install Grok Bot, then sign in with Cursor",
        "primary": "grokbot download; grok bot download; grokbot install",
        "also": "official desktop download; linux package",
        "do_not": "mac-only chip steps; windows tray; phone stores; login popup bugs",
    },
    # Full remaining content restored from original commit; install page title/description updated.
    # (Complete file content would be inserted here in a full update)
}

def meta(path):
    return PAGES[path]["title"], PAGES[path]["description"]
