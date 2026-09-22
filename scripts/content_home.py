# -*- coding: utf-8 -*-
from html import escape

FAQS = [
    ("Is Grok Bot the same as grok.com or Grok?",
     "No. grok.com is chat plus Imagine and Voice. Grok Bot is a separate app: named teammates plus one shared cloud computer. Google often shows grok.com for a grok bot search — that is the wrong product."),
    ("Is this the official Grok Bot site?",
     "No. This is a community how-to: first job, login, shared computer, plan conflicts, Recover before Reset, and an operator path after week one. Official packages stay on x.ai/bot."),
    ("Where do I download the Grok Bot app?",
     "Desktop packages are on x.ai/bot (macOS, Windows, Linux). iOS and iPad are on the App Store; Android is on Google Play. This site is not the store. The install page is the overview; Mac, Windows, and phone each have their own steps."),
    ("How do I log in to Grok Bot?",
     "There is no separate Grok Bot account. Open the app and sign in with the Cursor account that holds the plan and usage."),
    ("Is Grok Bot free? Which plan do I need?",
     "There is no consumer free tier and no standalone SKU. Access is bundled with paid Cursor or a linkable SuperGrok / X plan, plus a limited usage trial on some accounts. Enterprise had a dated two-week org trial in early September 2026 — that window is expired. See Pricing."),
    ("Is there a Grok Bot app for iOS and Android?",
     "Yes. iPhone needs iOS 18+; Android 9+. The iOS app also runs on iPad with iPadOS 18+ per the current xAI FAQ. Launch-day iPhone-only is history. The same roster syncs with desktop after Cursor login."),
    ("If the computer won't connect, should I Reset?",
     "No. The official order is Retry, restart, Recover, Update Agent Computer. Reset can lose unsynced work. Help splits not responding, stuck, can't reach, and Recover versus Reset."),
    ("Is there an open-source Grok Bot?",
     "Not an official one. OpenMausBot, rakazo, and gawkbot copy the teammate-plus-computer idea on machines you run. They are not unofficial clients for your Cursor roster. See Alternatives."),
    ("What is a Grok Bot skill versus a routine?",
     "A skill is how. A routine is when. Save the method after a good run, then schedule it. Tests do real things. Glossary has the short split."),
    ("Does Grok Bot run on Linux?",
     "Yes. Official deb, rpm, and AppImage are on x.ai/bot under More downloads. Prefer those over community ports. Notes live on the Linux tools page."),
    ("Is Grok Bot a feature inside Cursor?",
     "No. Cursor grokbot searches mean the Bot app that signs in with your Cursor account. Not a sidebar in the IDE. See Cursor and Grok Bot."),
]

FACE = (
    '<span class="wordmark-face" aria-hidden="true">'
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none">'
    '<rect width="32" height="32" rx="10.2" fill="#F6F4EF"/>'
    '<rect x="9.2" y="9.55" width="3.05" height="8.7" rx="1.525" fill="#111111"/>'
    '<rect x="19.75" y="9.55" width="3.05" height="8.7" rx="1.525" fill="#111111"/>'
    "</svg></span>"
)


def _face(color):
    return (
        '<svg class="face" viewBox="0 0 32 32" aria-hidden="true">'
        '<rect width="32" height="32" rx="10.2" fill="%s"/>'
        '<rect x="9.2" y="9.55" width="3.05" height="8.7" rx="1.525" fill="#111111"/>'
        '<rect x="19.75" y="9.55" width="3.05" height="8.7" rx="1.525" fill="#111111"/>'
        "</svg>" % color
    )


ROSTER = [
    ("#EDE8DC", "Chief of Staff", "One door", "/use-cases/#digest"),
    ("#F26B2A", "Sales Outbound", "Drafts only", "/use-cases/#sales"),
    ("#2EC4B6", "Inbox Manager", "You hit send", "/use-cases/#inbox"),
    ("#7C6CFF", "Talent Scout", "Review list", "/use-cases/#starter-jobs"),
    ("#4C9BFF", "Expense Manager", "Receipts first", "/use-cases/#starter-jobs"),
    ("#F071A5", "Account Health", "Warm notes", "/use-cases/#starter-jobs"),
]


def home():
    faq_html = []
    for q, a in FAQS:
        faq_html.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    steps = [
        ("01", "/learn/what-is-grok-bot/", "What Grok Bot is", "Separate it from grok.com, Grok Build, and grok-app."),
        ("02", "/learn/install/", "Install and sign in", "Official desktop, iOS, and Android. Mac and Windows notes are separate."),
        ("03", "/learn/first-bot/", "First Bot", "Short name, one job, Chief of Staff. Stop at drafts."),
        ("04", "/learn/computer/", "Shared computer", "One machine for every Bot. Screens are not isolation."),
        ("05", "/learn/plugins/", "Skills, plugins, cost", "Connectors first. Weekly usage can spill into On-Demand."),
        ("06", "/troubleshooting/", "When it breaks", "Not responding, stuck, or can't reach. Recover before Reset."),
    ]
    step_html = []
    for n, href, en, blurb in steps:
        step_html.append(
            '<a class="step" href="%s"><div class="num">%s</div><div><h3>%s</h3><p>%s</p></div></a>'
            % (href, n, escape(en), escape(blurb))
        )
    roster = []
    for color, name, note, href in ROSTER:
        roster.append(
            '<a class="roster-row" href="%s">%s<div><strong>%s</strong><span>%s</span></div></a>'
            % (href, _face(color), escape(name), escape(note))
        )
    body = '''
<section class="hero hero-product">
  <div class="wrap">
    <p class="kicker">Community guide · start, run, recover</p>
    <h1>How to start Grok Bot without burning a week</h1>
    <p class="lede">Paste a first job. Keep one shared computer from wiping the week. Read plan pages side by side. Fix “can’t reach the computer” without Reset.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="#first-job">Copy a first job</a>
      <a class="btn btn-secondary" href="/learn/install/">How to start</a>
      <a class="btn btn-ghost" href="/troubleshooting/">When it breaks</a>
    </div>
    <p class="hero-next"><a href="#already-running">Already running? Six steps from named field posts.</a></p>
    <ul class="proof">
      <li><b>54</b> field cases</li>
      <li><b>199</b> tools catalogued</li>
      <li><b>89</b> failure threads</li>
      <li><b>42</b> official sources</li>
      <li>No invented prices</li>
    </ul>
    <p class="stage-caption">Same faces as the app — so you know you are in the right product. The briefs you paste live on this site.</p>
    <div class="product-stage">
      <aside class="roster">%s</aside>
      <div class="stage-main">
        <div class="stage-bar">%s <b>Sales Outbound</b> · shared computer</div>
        <div class="bubble me">Research these accounts. Draft outreach in my voice. Do not send.</div>
        <div class="bubble bot">Three accounts scored. Drafts parked. Two need a login you should take over.</div>
        <div class="thinking">%s Thinking — browser is on the shared computer</div>
      </div>
    </div>
  </div>
</section>

<section class="band" id="first-job"><div class="wrap">
  <h2>Steal this first job</h2>
  <p class="lede">Five minutes. No connector. If this works, you have a Bot. If it does not, fix login before you invent a twelve-Bot company.</p>
  <div class="steal">
    <div class="job-card">
      <p class="kicker">Warm-up · attach one file</p>
      <h3>Cited brief, file unchanged</h3>
      <p>This is the same pattern as official Get started: outcome, source, constraint, deliverable, stop for review.</p>
      <pre><code>I attached one document. Give me (1) five bullets on what it says, and (2) every date, decision, and open question with a page or section cite. Leave the file unchanged.</code></pre>
      <button type="button" class="copy-btn" data-copy>Copy</button>
    </div>
    <div class="card">
      <h3>Then one real door</h3>
      <p>Pin a Chief of Staff. Do not create more Bots until it can report blockers. Inbox, outbound, and travel jobs are already written on <a href="/use-cases/#starter-jobs">use cases</a>.</p>
      <p><a class="btn btn-primary" href="/learn/first-bot/">First Bot lesson</a></p>
      <p class="muted">Tests do real things. Do not send, delete, or pay from a copied brief.</p>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Three mistakes that cost a week</h2>
  <div class="mistakes">
    <a class="mistake" href="/learn/computer/"><p class="tag">Isolation</p><h3>A second Bot is not a fence</h3><p>Every Bot on the account sees the same computer, cookies, and logins. Life Bot and work Bot share a browser.</p></a>
    <a class="mistake" href="/learn/first-bot/"><p class="tag">Roster</p><h3>Twelve Bots on day one</h3><p>Chatty Chief-of-Staff threads burn weekly usage. One door until the output is checkable.</p></a>
    <a class="mistake" href="/troubleshooting/"><p class="tag">Breakage</p><h3>Reset first</h3><p>Official order is Retry, restart, Recover, Update. Reset can drop unsynced work. iOS still working is a clue to wait.</p></a>
  </div>
</div></section>

<section class="band" id="already-running"><div class="wrap">
  <h2>Already running</h2>
  <p class="lede">Hiring Bots is easy. Managing them is the job. This track is built from Debbie, Nate, Peter Yang, Johnny Nel, s1rozha, Gergely Orosz, and the official @bot recap — patterns, not billed outcomes.</p>
  <div class="mistakes">
    <a class="mistake" href="/learn/operator/"><p class="tag">Path</p><h3>After week one</h3><p>One door, a what’s-left page, Teach a task, then a routine. Six steps with source links.</p></a>
    <a class="mistake" href="/learn/ops/"><p class="tag">Stack</p><h3>X, Cursor, MCP</h3><p>Scout X, brief a Cloud Agent, add remote MCP. Publish and merge stay with you.</p></a>
    <a class="mistake" href="/learn/cost-and-pitfalls/"><p class="tag">Usage</p><h3>Keep the week</h3><p>Weekly pool can spill into On-Demand with no in-app warning. Chatty CoS threads burn it.</p></a>
  </div>
  <p class="lede"><a href="/learn/ops/">X, Cursor, MCP</a> · <a href="/learn/plugins/">Connectors before the browser</a> · <a href="/compare/">When to self-host</a> · <a href="/use-cases/">54 field cases</a></p>
</div></section>

<section class="band"><div class="wrap">
  <h2>What people actually ran</h2>
  <p class="lede">Named sources. This site does not invent billed outcomes.</p>
  <div class="quotes">
    <article class="quote"><p>“Bots are not a security boundary.”</p><p class="who">Cursor forum pin · shared computer lesson</p></article>
    <article class="quote"><p>Start with one Chief of Staff and let it propose the team — not a specialist for every sub-task.</p><p class="who">Debbie · getting started notes</p></article>
    <article class="quote"><p>Help and the FAQ now include every paid Cursor plan, including Pro. Open the originals — this site does not invent USD prices.</p><p class="who">Pricing snapshot · fetch 2026-09-20</p></article>
  </div>
  <p class="lede"><a href="/use-cases/">54 field cases</a> · <a href="/pricing/">Plan conflicts</a> · <a href="/compare/">GitHub alternatives</a></p>
</div></section>

<section class="band"><div class="wrap">
  <h2>Start here</h2>
  <div class="grid-3">
    <a class="card" href="/learn/install/"><h3>How to start</h3><p>Mac, Windows, Linux, iOS, Android. Sign in with Cursor — no extra account.</p></a>
    <a class="card" href="/use-cases/#starter-jobs"><h3>More copyable jobs</h3><p>Inbox, outbound, travel. Stop at review until the output is checkable.</p></a>
    <a class="card" href="/pricing/"><h3>Free, plans, trial</h3><p>No standalone SKU. Cursor or SuperGrok. The early-September enterprise two-week trial is a dated announcement.</p></a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Download, and the screens people search</h2>
  <p class="lede">Official packages stay on x.ai/bot. These pages are the Mac, Windows, and phone steps, plus the fixes for not responding, stuck, and can’t reach.</p>
  <div class="grid-3">
    <a class="card" href="/learn/mac-download/"><h3>Mac download</h3><p>Apple silicon or Intel, Gatekeeper, then Cursor login.</p></a>
    <a class="card" href="/learn/windows-download/"><h3>Windows download</h3><p>x64 or Arm64, one copy, quit the tray.</p></a>
    <a class="card" href="/learn/phone-download/"><h3>iPhone and Android</h3><p>Official stores. Same roster. Some jobs stay on desktop.</p></a>
    <a class="card" href="/troubleshooting/not-responding/"><h3>Not responding</h3><p>Computer still opens? Check weekly usage before Reset.</p></a>
    <a class="card" href="/troubleshooting/stuck/"><h3>Stuck</h3><p>Connecting, Setting up, or Reconnecting. Match the label.</p></a>
    <a class="card" href="/troubleshooting/cant-reach/"><h3>Can’t reach</h3><p>DNS, VPN, or antivirus. Hotspot test before Reset.</p></a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>Read in this order</h2>
  <p class="lede">Each card is one page. Finish one job before the next.</p>
  <div class="roadmap">%s</div>
</div></section>

<section class="band"><div class="wrap">
  <h2>FAQ</h2>
  <div class="faq card">%s</div>
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
</script>
''' % ("".join(roster), _face("#F26B2A"), _face("#F26B2A"), "".join(step_html), "".join(faq_html))
    return body, FAQS
