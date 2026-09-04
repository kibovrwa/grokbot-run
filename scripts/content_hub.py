# -*- coding: utf-8 -*-
from html import escape
from htmlutil import LESSONS

HUB_FAQS = [
    ("Where should I start if I have never opened Grok Bot?",
     "Read What Grok Bot is, then Install, then First Bot. Skip tools and alternatives until one job has returned a checkable draft."),
    ("Do I need this handbook if I already have the official docs?",
     "Official docs are the source of truth. This handbook is the reading order, the product split (not grok.com), and the failure modes the docs do not group by symptom."),
    ("How long is the path?",
     "Seven short lessons. One evening is enough to install, name one Bot, and run a read-only job. Skills and routines wait until two good runs."),
    ("I already have a roster. Do I start at lesson one?",
     "No. Open After week one: kill the mega-chat, pin a Chief of Staff, keep a what’s-left page, then save a skill. The seven lessons stay the first-week order."),
    ("I want to run X, Cursor, and MCP together. Where?",
     "Open X, Cursor, MCP after the roster works. That page is the stack: official X plugin as research, Cloud Agent for the repo, remote MCP only. After week one is how you manage Bots."),
]

GLOSSARY = [
    ("Grok Bot", "The official app from xAI / SpaceXAI with Cursor: a roster of named teammates plus one shared cloud computer. Not grok.com chat."),
    ("Bot", "One named teammate on your roster. It has a screen on the shared computer. Creating another Bot is not a security boundary."),
    ("Computer", "The persistent cloud machine assigned to your account. Browser, files, and terminal live here. Every Bot can see the same logins and cookies."),
    ("Screen", "The work surface one Bot uses on that computer. Parallel screens are not isolation. One computer-use task runs per screen."),
    ("Skill", "A reusable how: when to use it, inputs, steps, how to verify, what to return, and what needs approval. Save after a good run."),
    ("Routine", "A when: schedule or event on one Bot. Tests do real things. Put sends, deletes, and payments behind approval."),
    ("Teach a task", "Desktop recording of about ten minutes of screen actions (no microphone). The Bot drafts a skill. You still add stop rules."),
    ("Plugin / connector", "Account-level integration. Prefer a connector over clicking the web. Installed for the account, not locked to one Bot."),
    ("MCP", "Remote HTTP tools the computer can call. Localhost / stdio MCP on your laptop is unreachable from the cloud machine."),
    ("Share / template", "A public x.ai/bot link that copies identity, skills, and routines — not your computer or logins. Strip secrets before sharing."),
    ("Chief of Staff", "Community convention: one pinned Bot you talk to. It proposes specialists. Official docs only require name, job, and how it works."),
    ("Require Approval", "The human gate for sends, spend, and other writes. Description beats shouting stop later in chat."),
    ("Weekly usage", "Meter on the Cursor account. macOS and iOS share one bucket. Exhaustion can spill into On-Demand if that is enabled."),
    ("On-Demand", "Shared paid overflow after the weekly pool. The app may not warn you in-product. Watch the Cursor usage screen."),
    ("Cursor account", "The only login. There is no separate Grok Bot account. The same account holds the plan and the usage meter. Grok Bot is not a Cursor IDE panel."),
    ("Hermes", "A different named-bot host. Some skill packs port a roster there. A Hermes profile is not a Cursor Grok Bot."),
    ("grok.com / Grok", "Chat, Imagine, and Voice. Google often ranks it for “grok bot.” Wrong product for this handbook."),
    ("Grok Build", "Local coding CLI. Not Grok Bot. The community app grok-app is a GUI for Grok Build, not a Bot client."),
    ("Legacy Privacy Mode", "A Cursor setting that can block Grok Bot computer provisioning. Turn it off on the account you sign in with."),
]

GLOSS_FAQS = [
    ("Is a skill the same as a plugin?",
     "No. A skill is written instructions. A plugin or connector is an account-level integration that gives the computer real tools. You usually need both."),
    ("If I create a second Bot, are my logins isolated?",
     "No. Isolation is per user, not per Bot. Files, cookies, and sessions on the shared computer are visible to the whole roster."),
    ("Does a share link copy my computer?",
     "No. Official share copies identity, skills, and routines. It does not copy the cloud computer or the logins stored there."),
    ("Is Grok Build a Grok Bot client?",
     "No. Grok Build is a local coding CLI. grok-app is a desktop GUI for that CLI. Install Grok Bot from x.ai/bot."),
]

CURSOR_FAQS = [
    ("Is Grok Bot inside the Cursor IDE?",
     "No. Grok Bot is its own desktop and phone app. It uses your Cursor account for login, plan, plugins, and weekly usage. You do not chat with Bots in the Cursor editor."),
    ("Do I need Cursor Ultra for Grok Bot?",
     "Not on the 2026-09-04 official Help page: paid personal Cursor plans and Teams include it, and some SuperGrok / X plans can link. FAQ and Get started listed a narrower set. Open Pricing for the dated conflict."),
    ("Does Grok Bot index my Cursor codebase?",
     "Staff on the Cursor forum: there is no codebase plugin. Coding work goes to a Cursor Cloud Agent already connected to GitHub. The Bot computer is not your laptop repo. Operator handoff: X, Cursor, MCP."),
    ("Is Hermes the same as Grok Bot?",
     "No. Hermes is a different named-bot host. Some skill packs (Aaron Marketing, hermes-bot-kit) port the roster idea. A Hermes profile is not a Cursor Grok Bot."),
]


def cursor_and_grok():
    faqs = []
    for q, a in CURSOR_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">Cursor and Grok Bot</p>
<h1>Cursor Grok Bot: one account, two apps</h1>
<p class="meta">People search “cursor grokbot” as if Grok Bot were a Cursor IDE panel. It is not. This page is the relationship. Plans: <a href="/pricing/">pricing</a>. Sign-in steps: <a href="/learn/install/">install</a>.</p>
<p>Grok Bot and Cursor share an account, a plugin library, and a usage meter. They do not share a window. You download Grok Bot from <a href="https://x.ai/bot">x.ai/bot</a>, open that app, and choose Sign in with Cursor. The hosted computer is provisioned for that Cursor account. Close the laptop and cloud turns still run — that is the Bot product, not the editor.</p>
<h2>What the Cursor account actually holds</h2>
<ul>
<li><strong>Login.</strong> There is no separate Grok Bot user. The welcome screen is Get started or Sign in with Cursor. Org SSO follows the Cursor org, not a second signup.</li>
<li><strong>Plan and weekly usage.</strong> The Bot pool lives on the Cursor account. macOS and iOS share one bucket. Exhaustion can spill into On-Demand. Watch the Cursor usage screen, not a Bot-only invoice.</li>
<li><strong>Plugins.</strong> Grok Bot inherits the Cursor plugin marketplace under Cursor plugin policy. Install Compound Engineering or Vercel once in Cursor; do not clone those repos onto the Bot computer. Details: <a href="/learn/plugins/">plugins</a> and <a href="/use-cases/#skills">skills</a>.</li>
<li><strong>Team admin is not a seat.</strong> Assign yourself Standard or Premium, or switch to an account that has one. A free Cursor plan can spin forever on “Setting up” because the computer is never provisioned.</li>
</ul>
<div class="callout warn">
<p><strong>Legacy Privacy Mode can block the computer.</strong> Turn it off on the Cursor account you will sign in with before you blame DNS. Coding in the Cursor IDE still does not grant the Bot a copy of your local repo.</p>
</div>
<h2>What Cursor Grok Bot is not</h2>
<ul>
<li>Not a Cursor sidebar chat. Agent chat in the IDE is a different surface.</li>
<li>Not Grok the model picker inside Cursor. Model names change; the Bot product is teammate + computer + approval.</li>
<li>Not Hermes Bot Mode, Claude cowork, or ChatGPT scheduled tasks. Those are other hosts. Compare self-hosted stacks on <a href="/compare/">alternatives</a>.</li>
<li>Not grok.com. Google still ranks grok.com for many grokbot queries.</li>
</ul>
<h2>FAQ</h2>
<div class="faq card">%s</div>
<p>Already running a roster: <a href="/learn/ops/">X, Cursor Cloud Agents, MCP, and the computer</a>. New here: <a href="/learn/install/">install and sign in</a>, then one job on <a href="/learn/first-bot/">First Bot</a>.</p>
</div></section>
''' % "".join(faqs), CURSOR_FAQS


def learn_index():
    cards = []
    blurbs = {
        "/learn/what-is-grok-bot/": "Split Grok Bot from grok.com, Grok the model, Grok Build, and grok-app.",
        "/learn/install/": "Official packages, Cursor login, iOS and Android, Legacy Privacy Mode.",
        "/learn/first-bot/": "One name, one job, copyable briefs that stop at drafts.",
        "/learn/computer/": "One shared cloud PC. Screens are not a fence. Recover before Reset.",
        "/learn/skills-routines/": "How versus when. Teach a task, then automate.",
        "/learn/plugins/": "Connectors first. Remote MCP only. Common OAuth failures.",
        "/learn/cost-and-pitfalls/": "Weekly pool, On-Demand spillover, and week-burning habits.",
    }
    for i, (href, label) in enumerate(LESSONS, 1):
        cards.append(
            '<a class="step" href="%s"><div class="num">%02d</div><div><h3>%s</h3><p>%s</p></div></a>'
            % (href, i, escape(label), escape(blurbs[href]))
        )
    faqs = []
    for q, a in HUB_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">Handbook</p>
<h1>Grok Bot handbook — read in this order</h1>
<p class="lede">Seven lessons from “which product is this?” to a first reversible job. Official docs stay the source of truth. This site is the order, the disambiguation, and the failure map.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/what-is-grok-bot/">Start with what it is</a>
  <a class="btn btn-secondary" href="/learn/install/">Skip to install</a>
  <a class="btn btn-ghost" href="/learn/operator/">Already running</a>
</div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Already running</h2>
  <p class="lede">Skip the first-week order if you already have a roster. The operator path is built from named X field posts.</p>
  <div class="grid-3">
    <a class="card" href="/learn/operator/"><h3>After week one</h3><p>One door, what’s-left page, Teach a task, routine after two good runs.</p></a>
    <a class="card" href="/learn/ops/"><h3>X, Cursor, MCP</h3><p>Scout X, brief a Cloud Agent, add remote MCP. You still approve.</p></a>
    <a class="card" href="/learn/cost-and-pitfalls/"><h3>Usage and On-Demand</h3><p>Weekly pool, spillover, chatty Chief-of-Staff threads.</p></a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Lessons</h2>
<p class="lede">Finish one page before opening the next. Do not install twelve Bots on day one.</p>
<div class="roadmap">%s</div>
</div></section>

<section class="band"><div class="wrap">
<h2>After the lessons</h2>
<div class="grid-3">
  <a class="card" href="/learn/cursor/"><h3>Cursor and Grok Bot</h3><p>One account, two apps. Not a Cursor IDE panel. Login, usage, and plugins.</p></a>
  <a class="card" href="/compare/"><h3>Alternatives / GitHub</h3><p>Official managed computer versus OpenMausBot, rakazo, gawkbot, OpenClaw.</p></a>
  <a class="card" href="/use-cases/"><h3>Starter jobs</h3><p>Copy a brief. Then the jobs people posted on X.</p></a>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>FAQ</h2>
<div class="faq card">%s</div>
</div></section>
''' % ("".join(cards), "".join(faqs)), HUB_FAQS


def glossary():
    rows = []
    for term, blurb in GLOSSARY:
        rows.append("<dt>%s</dt><dd>%s</dd>" % (escape(term), escape(blurb)))
    faqs = []
    for q, a in GLOSS_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">Reference</p>
<h1>Grok Bot glossary</h1>
<p class="meta">Original short definitions for this handbook. Official wording lives on <a href="https://docs.x.ai/grok-bot/overview">xAI docs</a>. Longer lessons: <a href="/learn/">handbook</a>.</p>
<p>People bounce between five words — Bot, computer, skill, routine, plugin — and treat them as one. They are not. Use this page when a tutorial collapses them, then return to the lesson that owns the job.</p>
<dl class="terms">%s</dl>
<h2>Common collisions</h2>
<div class="faq card">%s</div>
<p>Next: <a href="/learn/what-is-grok-bot/">what Grok Bot is</a>, <a href="/learn/skills-routines/">skills and routines</a>, or <a href="/compare/">official vs alternatives</a>.</p>
</div></section>
''' % ("".join(rows), "".join(faqs)), GLOSS_FAQS
