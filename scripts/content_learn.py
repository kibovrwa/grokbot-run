# -*- coding: utf-8 -*-
from html import escape
from htmlutil import pager

def _p(path):
    return pager(path, "en")


def _faq_html(faqs):
    bits = ['<h2>FAQ</h2><div class="faq card">']
    for q, a in faqs:
        bits.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    bits.append("</div>")
    return "".join(bits)


INSTALL_DIAGRAM = '''
<figure class="diagram">
<svg viewBox="0 0 520 168" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Install then Cursor login then roster">
  <rect x="8" y="28" width="140" height="112" rx="16" fill="#1E1E1E"/>
  <rect x="48" y="48" width="60" height="60" rx="18" fill="#F6F4EF"/>
  <ellipse cx="68.2" cy="74.4" rx="6.2" ry="11.4" fill="#111"/>
  <ellipse cx="87.8" cy="74.4" rx="6.2" ry="11.4" fill="#111"/>
  <text x="78" y="126" text-anchor="middle" fill="#EDEBE4" font-size="12" font-family="ui-sans-serif,system-ui">App</text>
  <path d="M160 84h36" stroke="#6B6B6B" stroke-width="2"/>
  <rect x="204" y="28" width="140" height="112" rx="16" fill="#1E1E1E"/>
  <text x="274" y="78" text-anchor="middle" fill="#F6F4EF" font-size="14" font-family="ui-sans-serif,system-ui">Cursor</text>
  <text x="274" y="100" text-anchor="middle" fill="#8A8A86" font-size="11" font-family="ui-sans-serif,system-ui">browser sign-in</text>
  <path d="M356 84h36" stroke="#6B6B6B" stroke-width="2"/>
  <rect x="400" y="28" width="112" height="112" rx="16" fill="#1E1E1E"/>
  <rect x="416" y="48" width="22" height="22" rx="6" fill="#EDE8DC"/>
  <rect x="444" y="48" width="22" height="22" rx="6" fill="#F26B2A"/>
  <rect x="472" y="48" width="22" height="22" rx="6" fill="#2EC4B6"/>
  <text x="456" y="98" text-anchor="middle" fill="#F6F4EF" font-size="12" font-family="ui-sans-serif,system-ui">Roster</text>
  <text x="456" y="116" text-anchor="middle" fill="#8A8A86" font-size="11" font-family="ui-sans-serif,system-ui">one computer</text>
</svg>
<figcaption>Official path: install the app, sign in with Cursor, then meet the roster. There is no second Grok Bot account.</figcaption>
</figure>
'''

COMPUTER_DIAGRAM = '''
<figure class="diagram">
<svg viewBox="0 0 520 200" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="One shared computer with three Bot screens">
  <rect x="24" y="18" width="472" height="164" rx="18" fill="#1E1E1E"/>
  <text x="260" y="44" text-anchor="middle" fill="#8A8A86" font-size="12" font-family="ui-sans-serif,system-ui">One cloud computer · assigned to the user</text>
  <rect x="48" y="64" width="128" height="92" rx="12" fill="#141414" stroke="#2A2A2A"/>
  <rect x="90" y="78" width="44" height="44" rx="12" fill="#EDE8DC"/>
  <ellipse cx="104.8" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <ellipse cx="119.2" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <text x="112" y="140" text-anchor="middle" fill="#EDEBE4" font-size="11" font-family="ui-sans-serif,system-ui">Chief screen</text>
  <rect x="196" y="64" width="128" height="92" rx="12" fill="#141414" stroke="#2A2A2A"/>
  <rect x="238" y="78" width="44" height="44" rx="12" fill="#F26B2A"/>
  <ellipse cx="252.8" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <ellipse cx="267.2" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <text x="260" y="140" text-anchor="middle" fill="#EDEBE4" font-size="11" font-family="ui-sans-serif,system-ui">Sales screen</text>
  <rect x="344" y="64" width="128" height="92" rx="12" fill="#141414" stroke="#2A2A2A"/>
  <rect x="386" y="78" width="44" height="44" rx="12" fill="#2EC4B6"/>
  <ellipse cx="400.8" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <ellipse cx="415.2" cy="97.4" rx="4.4" ry="8.2" fill="#111"/>
  <text x="408" y="140" text-anchor="middle" fill="#EDEBE4" font-size="11" font-family="ui-sans-serif,system-ui">Inbox screen</text>
</svg>
<figcaption>Three screens, one machine. Cookies, files, and logins are shared. A new Bot is not a security fence.</figcaption>
</figure>
'''

INSTALL_FAQS = [
    ("Is there a separate Grok Bot account?",
     "No. Sign in with the Cursor account that holds the plan and usage. Linking SuperGrok or X Premium+ is a usage grant on that same Cursor account."),
    ("Which download should I use?",
     "Only x.ai/bot for desktop, the App Store for iPhone and iPad, and Google Play for Android. Linux packages are under More downloads. This handbook is not the store. Skip community ports unless official packages fail."),
    ("Why does macOS say the app is not supported?",
     "You likely picked the Intel build on Apple silicon, or the reverse, or a non-official dmg. Official FAQ lists macOS Apple silicon and Intel. That message is not proof Grok Bot is unavailable on Mac."),
    ("Why does the app sit on Setting up?",
     "Free Cursor plans never get a computer. Team admin without a paid seat is the same. That is a copy bug, not your network."),
    ("Why does Can't reach appear after my trial ended?",
     "Staff: ended trial or lost plan access can wrongly show Can't reach while Retry/Recover fail. Pick a plan that includes Grok Bot or link SuperGrok on the same email, fully quit, and reopen — it is usually access, not DNS."),
    ("Can I run Grok Bot only from my phone?",
     "Yes for chat, watching the computer, and most plugins. iPhone needs iOS 18+; the same iOS app runs on iPad with iPadOS 18+. Android 9+. Launch-day iPhone-only is history. Routine webhook URL and sender key appear on desktop only. macOS and iOS share one weekly bucket. If the desktop is black but iOS still works, Recover — do not Reset."),
]

COMPUTER_FAQS = [
    ("Does each Bot get its own computer?",
     "No. Every Bot on the account uses one persistent cloud computer. Screens let them work in parallel. Screens are not isolation."),
    ("Should I paste a password into chat?",
     "No. Take over the computer for passwords, 2FA, CAPTCHAs, and payments. Use the secrets card for supported connectors."),
    ("When should I Reset the computer?",
     "Last. Retry, restart, Recover, then Update under Settings, Updates. Update and Recover keep synced bots and remove installed apps. Reset can also drop unsynced bots and files."),
]

def what_is():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 1</p>
<h1>What is Grok Bot — not grok.com or Grok Build</h1>
<p class="meta">This page answers “which product is grokbot / grok bot?” Install steps: <a href="/learn/install/">Install and sign in</a>.</p>
<p>Grok Bot is the always-on AI teammate shipped by xAI / SpaceXAI together with Cursor. Per the official overview: a Bot is a <strong>persistent, named agent</strong> you message like a colleague; it can sign into apps and websites, finish work in the background, and return only when it needs your decision. <a href="https://docs.x.ai/grok-bot/overview">docs.x.ai/grok-bot/overview</a> states this plainly: it has its own cloud computer (browser, filesystem, terminal); multiple Bots share that one computer and can pass context and hand off work.</p>
<p>The product page <a href="https://x.ai/bot">x.ai/bot</a> says: dispatch Bots from desktop or phone; they work in parallel, keep context about how you work, and find you when approval is needed. The official FAQ also stresses: close the laptop or App and cloud turns and routines keep running. <a href="https://docs.x.ai/grok-bot/faq">FAQ</a></p>
<h2>It is not these three things</h2>
<p>The most common community mix-up is collapsing three Grok-branded products into one. This playbook forces the split:</p>
<ul>
<li><strong>Not grok.com chat.</strong> grok.com / the Grok app is a conversational assistant (plus Imagine, Voice, Build, and so on). Grok Bot is a different line: roster, cloud computer, routines. Coverage such as The Verge also keeps them separate — see <a href="/sources/">Sources</a>.</li>
<li><strong>Not Grok 4.x model evals.</strong> Models can change generations; the Bot product sells “teammate + computer + approval,” not a benchmark score.</li>
<li><strong>Not Grok Build, and not grok-app.</strong> Grok Build is a local coding CLI. The community project <a href="https://github.com/RongleCat/grok-app">RongleCat/grok-app</a> is a desktop GUI (Tauri) for the <strong>local Grok Build CLI</strong> — <em>not</em> a Grok Bot client. This site only mentions it under “related / easy to confuse” in the <a href="/tools/">tools catalog</a>.</li>
</ul>
<h2>Five official differences (check the originals)</h2>
<ol>
<li><strong>It has its own computer.</strong> A persistent cloud VM with browser, filesystem, and terminal; sites without a clean API get clicked the way a human would. <a href="https://docs.x.ai/grok-bot/overview">Overview</a> · <a href="https://docs.x.ai/grok-bot/computer-and-apps">Computer and apps</a></li>
<li><strong>No workflow canvas required to start.</strong> Create a Bot, send a message, authorize as needed. The same Bot is reachable from desktop and phone. <a href="https://docs.x.ai/grok-bot/get-started">Get started</a></li>
<li><strong>Multiple Bots coordinate themselves.</strong> They share one <strong>user-isolated</strong> computer, can message each other, join group chats, and hand off — you are not the router.</li>
<li><strong>It can watch you demonstrate once.</strong> Teach a task stores up to about ten minutes of screen actions as a skill draft (no microphone recording). <a href="https://docs.x.ai/grok-bot/skills-routines-and-automations">Skills and routines</a></li>
<li><strong>State is durable.</strong> Name, memory, files, browser sessions, and preferences survive across turns instead of wiping the environment each time.</li>
</ol>
<div class="callout warn">
<p><strong>The isolation boundary is the user, not the Bot.</strong> Official wording: the computer is assigned to the account, not to a single Bot. Files, cookies, and logins are visible to every Bot on the roster. Do not treat “create another Bot” as security isolation. Forum pin: <a href="https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476">Bots are not a security boundary</a>. The next lesson digs in: <a href="/learn/computer/">shared cloud computer</a>.</p>
</div>
<h2>Who can use it (official wording on 2026-09-20)</h2>
<p>Eligibility follows the official pages on the fetch day. Cursor Help <a href="https://cursor.com/help/grok-bot/plans">Plans and billing</a> and the xAI <a href="https://docs.x.ai/grok-bot/faq">FAQ</a> (both fetched 2026-09-20) now say Grok Bot is included with every paid individual Cursor plan — including Pro — and with Cursor Teams. You can also link personal SuperGrok, SuperGrok Plus, SuperGrok Heavy, or X Premium+ (X Premium+ is named on Cursor Help; the FAQ names SuperGrok / Plus / Heavy). The September 4 conflict, when the FAQ omitted Pro, is largely resolved. Remaining wording still differs on stacking versus “whichever has more usage,” so open the originals — this site does not invent USD prices. Dated contrast: <a href="/pricing/">pricing snapshot</a>.</p>
<h2>Common misconceptions</h2>
<ul>
<li>Hearing “each Bot has its own screen” as “each Bot has its own computer.” Official text: one shared computer, one screen per Bot; screens are not a security boundary.</li>
<li>Assuming Grok Bot indexes your Cursor codebase. Staff on the forum: there is no codebase plugin; coding work goes to a Cursor Cloud Agent already connected to GitHub.</li>
<li>Treating community Linux ports, usage widgets, or terminal TUIs as official clients. They are third-party — see the <a href="/tools/">tools catalog</a>.</li>
</ul>
<p>Words colliding? Open the <a href="/learn/glossary/">glossary</a>. Shopping for a self-hosted stack instead of a seat? That is a different product family — <a href="/compare/">official vs alternatives</a>.</p>
<p>Next: grab the installer from the official download page and confirm your Cursor account is not on Legacy Privacy Mode — <a href="/learn/install/">install the desktop app and finish sign-in</a>.</p>
%s
</div></section>
''' % pager("/learn/what-is-grok-bot/")
    return body

def install():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 2</p>
<h1>Download and install Grok Bot, then sign in with Cursor</h1>
<p class="meta">Official steps from <a href="https://docs.x.ai/grok-bot/get-started">Get started</a>, re-read 2026-09-22. Mac, Windows, and phone each have a longer page. Stuck after install? <a href="/troubleshooting/stuck/">Wait if the bar is still moving</a>.</p>
<div class="callout">
<p><strong>Download from <a href="https://x.ai/bot">x.ai/bot</a>, then sign in with Cursor.</strong> The top macOS button is Apple silicon. Intel is under More downloads. This handbook is not the store. Access still depends on your plan: Get started (2026-09-22) lists every paid individual Cursor plan, Cursor Teams, or a linked SuperGrok, Plus, or Heavy subscription. Older pages that say Ultra only are stale. Conflicts stay on <a href="/pricing/">pricing</a>.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="https://x.ai/bot">Download on x.ai/bot</a>
  <a class="btn btn-secondary" href="/learn/mac-download/">Intel Mac? Read this first</a>
  <a class="btn btn-ghost" href="/learn/login/">Then sign in</a>
</div>
<p>Download path: open x.ai/bot for the Mac / Windows / Linux package, the App Store for iPhone or iPad, or Google Play for Android — then sign in with Cursor. There is <strong>no separate Grok Bot account</strong>. Confirm three things before you click download. First, you are on an <strong>eligible plan</strong>, or you are ready to link personal SuperGrok / X Premium+ on the plans screen (linking is a usage grant, not another Cursor subscription, and <strong>once linked you cannot unlink or move it to another Cursor account yourself</strong> — see <a href="https://cursor.com/help/grok-bot/supergrok">Link SuperGrok</a>). Second, Grok Bot needs cloud storage: if Cursor is still on Legacy Privacy Mode, switch to Privacy Mode and explicitly save it — new accounts that never save Privacy Mode can sit on Connecting forever, and Retry/Recover/Reset will not help until that choice is saved. Third, have a real first task that needs a real login — empty demos burn trial usage fast.</p>
<h2>Officially supported platforms</h2>
<p>Per the xAI FAQ (fetched 2026-09-20): macOS (Apple silicon and Intel), Windows (x64 and Arm64), Linux (x64 and Arm64; deb / rpm / AppImage), iPhone (iOS 18+), Android 9+. The iOS app also runs on iPad with iPadOS 18+. Launch-day iPhone-only is history. Linux packages are under More downloads on <a href="https://x.ai/bot">x.ai/bot</a>. Community threads still discuss Linux as a second-class citizen and third-party repacks — those entries live in the <a href="/tools/">tools catalog</a>; do not confuse them with official packages.</p>
<h2>Pick the download that matches the machine</h2>
<ul>
<li><a href="/learn/mac-download/">Mac download</a> — top button is Apple silicon; Intel is under More downloads.</li>
<li><a href="/learn/windows-download/">Windows download</a> — x64 or Arm64, one installed copy, tray quit, proxy and Zscaler.</li>
<li><a href="/learn/phone-download/">iPhone, iPad, and Android</a> — official stores, and the jobs that stay on desktop.</li>
<li><a href="/learn/login/">Cursor login</a> — no second account, SSO, Privacy Mode, and a stale session after a password change.</li>
<li><a href="/tools/linux-port/">Linux packages</a> — official deb, rpm, and AppImage versus community ports.</li>
</ul>
<p>Download only from official entry points:</p>
<ul>
<li>Product and desktop packages: <a href="https://x.ai/bot">x.ai/bot</a></li>
<li>iOS and iPad: <a href="https://apps.apple.com/us/app/grok-bot/id6794501026">App Store · Grok Bot</a></li>
<li>Android: <a href="https://play.google.com/store/apps/details?id=ai.x.grok.bot">Google Play · ai.x.grok.bot</a> (announced by official @bot on 2026-09-02)</li>
</ul>
<h2>Mac download: Apple silicon vs Intel</h2>
<p>The longer Mac path is <a href="/learn/mac-download/">Download Grok Bot for Mac</a>. Short version: Apple menu → About This Mac. A <strong>Chip</strong> field means Apple silicon; use the top Download for macOS button. A <strong>Processor</strong> field means Intel; scroll to Download Grok Bot, then <strong>More downloads</strong>. Cursor staff confirmed the top button is the Apple silicon build (forum, 2026-08-19).</p>
<p>If macOS says the app is not supported, you took that top button on an Intel Mac, or a file that did not come from x.ai/bot. Delete it. Intel users should not download a third time from the same button.</p>
<h2>Desktop install (official order)</h2>
<ol>
<li><strong>macOS:</strong> pick Apple silicon or Intel as above → open the official dmg → drag to Applications → open; choose Open if macOS asks.</li>
<li><strong>Windows:</strong> pick x64 or Arm64 → run the installer → open from the Start menu. Architecture: Settings → System → About → System type. Two copies and the tray quit are on <a href="/learn/windows-download/">Windows download</a>.</li>
<li><strong>Linux:</strong> pick deb / rpm / AppImage for your distro under More downloads; <code>uname -m</code> of x86_64 means x64, aarch64 means Arm64. The app checks for updates automatically. You can also use Settings → Updates → Check for Updates. That updates the app. It does not reset the computer.</li>
</ol>
<h2>Sign in</h2>
<p>Popup never returns, or the Mac says the account is unavailable after a password change? Use <a href="/learn/login/">Grok Bot login</a>. Short version: Grok Bot has <strong>no separate account</strong>. On the welcome screen choose Get started, or Sign In with Cursor in settings, finish Cursor auth in the browser popup, then return to the app. If your org requires SSO, follow the org flow — do not open a separate personal account. First-run introduces Bots, the shared computer, and routines, and asks which tools you use often — those answers only affect suggestions and <em>do not</em> connect the tools for you. The computer initializes in the background; the last screen is Meet a future teammate.</p>
''' + INSTALL_DIAGRAM + '''
<p>The official product page shows the same three beats: install, Cursor login, then a roster of named faces on one computer. This handbook keeps that order. Do not create twelve Bots on the first screen.</p>
<p>Cursor Help also reminds you: sign in with the <strong>Cursor account that will bear the usage</strong>; macOS and iOS share one weekly usage bucket.</p>
<h2>Phone: iOS, iPad, Android, and what stays on desktop</h2>
<p>Store links, OS versions, and the desktop-only jobs are on <a href="/learn/phone-download/">iPhone, iPad, and Android</a>. The same roster and the same computer sync after Cursor login. Official @bot (2026-09-02) pointed Android at Google Play; iPhone is the App Store build, iOS 18+. The xAI FAQ (fetched 2026-09-20) says the same iOS app also runs on iPad with iPadOS 18+ — launch-day iPhone-only is history. Close the phone app and cloud turns plus routines keep running, the same as closing the laptop.</p>
<p>On phone you can chat, watch the computer, take over for a stuck login, and open Plugins from the top-left avatar. Some connectors fail the iOS redirect (Canva is the documented case) — connect once on desktop and the connector syncs to iPhone. Staff note: the routine webhook URL and sender key appear on desktop only. Teach a task is a desktop screen recording. Do not treat the phone as a second computer or a private login.</p>
<p>If the desktop preview is black or stuck Reconnecting but the same account still works on iOS, that is a clue the Bots are not gone. Prefer Recover / Update. Reset from panic can delete Bots. Details: <a href="/learn/computer/">shared computer</a> and <a href="/troubleshooting/cant-reach/">can’t reach</a>.</p>
<h2>Before you create the first Bot</h2>
<p>Official advice: short name, one primary job, how it should work. Focused Bots accumulate useful context faster than an “everything assistant.” Later, use New → Create new agent to split by role. Docs put the account-wide Bot + group-chat cap at 50.</p>
<h2>Common misconceptions</h2>
<ul>
<li>Free Cursor plans spin forever on “Setting up.” Staff: without a paid seat the hosted computer is never provisioned — known copy bug, not your network.</li>
<li>Team admin role ≠ seat. Assign yourself a Standard/Premium seat, or switch to an account that has one.</li>
<li>After a password change, Mac still says the account is unavailable — usually a stale session. Log out from that screen, fully quit, sign in again; do not treat it as missing entitlement.</li>
<li>Expired free trial or lost plan access can look like “Can’t reach your computer” with failed Retry/Recover. Staff: that is often access ending, not DNS — pick a plan that includes Grok Bot or link SuperGrok, then fully quit and reopen. More symptom playbooks: <a href="/troubleshooting/">troubleshooting</a>.</li>
<li>Deleting Grok Bot has no separate account to delete: desktop only signs out; iOS Delete Account deletes the Cursor account plus agents, chats, and computer. See Cursor Help Delete account.</li>
</ul>
<p>Once the roster appears, do not create twelve Bots at once. Community convention: start with one Chief of Staff and let it propose the team — <a href="/learn/first-bot/">create your first Bot in Chief of Staff mode</a>.</p>
''' + _faq_html(INSTALL_FAQS) + '''
%s
</div></section>
''' % pager("/learn/install/")
    return body

def first_bot():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 3</p>
<h1>How to use Grok Bot: first Bot and Chief of Staff</h1>
<p class="meta">This is a community convention, not a mandated official architecture. Officially you only need: name, primary job, how it works.</p>
<p>Official Get started uses an example named Piper whose job is product-performance investigation: keep links and screenshots, separate evidence from hypotheses, report highest-impact issues first, never change production settings. Cursor Help makes step one even shorter: name, shape, color, title, then describe the outcome in a new chat. That is enough. Community tutorials additionally converge on a pattern that shows up again and again: <strong>you mainly talk to one pinned Chief of Staff, who creates specialist Bots, hands off work, and reports blockers</strong>.</p>
<p>Debbie’s getting-started notes (<a href="https://debbie.codes/blog/how-to-get-started-with-grok-bot">How to Get Started with Grok Bot</a>, 2026-08-14) roughly: add a Chief of Staff from day zero and let it build the team around what you do; you manage one person while the others report to each other. She added a Chief of Staff later herself — coding, LinkedIn, X, email first, then video editing and travel — and regrets not starting that way. She also warns: do not open a Bot for every sub-task; she almost created a thumbnail specialist and was stopped because that was just another handoff.</p>
<p>AI Builder Club’s survey (<a href="https://www.aibuilderclub.com/blog/grok-bot-guide">How to Use Grok Bot</a>, updated 2026-08-30) checked tutorials available then: three of Finn, Berman, and Herk’s four long videos independently taught the same pattern. Their opener is not pasting a giant system prompt — it is dumping “who you are and how you work” to the first Bot, asking how it would set up Grok Bot for you, then approving its plan. This page does not copy those long prompts; open the originals for exact wording.</p>
<p>MindStudio’s setup piece (<a href="https://www.mindstudio.ai/blog/grok-bot-setup-guide">setup guide</a>, 2026-08-12) clarifies the description field: Grok Bot uses the description as a routing signal, so a general assistant can hand coding work to a developer Bot. That article’s eligibility claim still says “needs Cursor Ultra” — against the official pages we fetched on 2026-09-04 that is stale; prefer the <a href="/pricing/">pricing snapshot</a>.</p>
<p>DataCamp’s tutorial (<a href="https://www.datacamp.com/tutorial/grok-bot-tutorial">Grok Bot Tutorial</a>) takes a deeper single-Bot path: build a learning guide named Scout that reads a learner profile, checks course pages, saves the method as a skill, then hangs it on a Monday routine. That proves Chief of Staff is not the only valid shape — if you have one repeating research job, one Scout is enough.</p>
<h2>A first task that will not hurt you</h2>
<p>Official Get started wants five parts in the request: outcome, sources, constraints, deliverable, and when to stop for review. In the Chief of Staff scene, write the constraint as “plan first; do not create more Bots, send email, or place orders without approval.” Approval boundaries in the description beat shouting stop later in chat. Copy a longer set of jobs on <a href="/use-cases/#starter-jobs">starter use cases</a>.</p>
<div class="job-card">
<p class="kicker">No connector</p>
<h3>Warm-up on one file</h3>
<p>Attach a document. Leave the file unchanged.</p>
<pre><code>I attached one document. Give me (1) five bullets on what it says, and (2) every date, decision, and open question with a page or section cite. Leave the file unchanged.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<div class="job-card">
<p class="kicker">Chief of Staff</p>
<h3>Then one real door</h3>
<p>After the warm-up works, pin one Bot and stop creating more until it can report blockers.</p>
<pre><code>You are my only door today. Review yesterday across my inbox, calendar, and meeting notes against the priorities I pasted. Return only items that map to those priorities. For each: source, why it matters, the next step, and whether I owe a decision. Do not send messages, create more Bots, or change meetings.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
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
<h2>Common misconceptions</h2>
<ul>
<li>Creating twelve Bots on day one. Nate’s review title is literally “eight hours, twelve Bots” — that is a review, not your daily ops. Chatty Chief-of-Staff threads themselves burn weekly usage.</li>
<li>Pasting a long prompt into chat as a secret. Share links copy identity, skills, and routines — <strong>not</strong> your computer and logins — but secrets in the config still leak. Strip confidentials before sharing.</li>
<li>Letting the Chief of Staff “send / post / pay” by default. Debbie’s LinkedIn case posted only after she said post; the flights case stopped at the last click. Default should stop at drafts.</li>
</ul>
<p>Once the roster can turn over work, you must understand they sit on one machine — <a href="/learn/computer/">all Bots share one cloud computer</a>.</p>
%s
</div></section>
''' % pager("/learn/first-bot/")
    return body

def computer():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 4</p>
<h1>The Grok Bot computer is shared — not a security boundary</h1>
<p>This is the page you must not skip. Official computer docs: every Bot under the account uses the <strong>same</strong> persistent cloud computer; browser cookies and login state are shared, files are visible to each other, shell credentials are shared, and progress written by one Bot can be continued by another. The computer is assigned to the <strong>user</strong>, not to a single Bot. If you do not want another Bot to touch a credential or file, do not put it on this computer.</p>
''' + COMPUTER_DIAGRAM + '''
<p>The official product page shows many named faces working at once. That is one account, one machine, several screens — the same construction as the roster on this site’s homepage. A second Bot does not get a private VM.</p>
<p>Each Bot has its own screen on that computer, so they can use the browser and desktop tools in parallel — but one screen runs one computer-use task at a time. Screens are a work surface, <strong>not a security boundary</strong>. The Cursor forum thread <a href="https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476">Bots are not a security boundary</a> put that consensus in the title. Some internal writers said “own computer” when they meant “own screen”; xAI docs correct the loose wording.</p>
<h2>How you watch and take over</h2>
<p>Open Agent Computer from the chat; the preview shows clicks, typing, and current state. Close Grok Bot or shut the laptop and cloud work keeps going. For passwords, passkeys, 2FA, CAPTCHAs, payments, or sites that insist on a human, the Bot should hand the computer to you: open the computer, take over, finish only the stuck step, return control, and let it continue. <strong>Do not paste passwords or one-time codes into ordinary chat.</strong> When a supported connector shows a secrets card, fill it there — values are masked, stay out of the conversation, and are not shown to the model.</p>
<p>Sessions usually persist, so you need not re-login for every task. Because the browser is shared, logging one Bot in opens the door for everyone on the roster. Some sites expire, time out quickly, or re-verify — have the Bot stop and notify you instead of bypassing checks.</p>
<h2>The workspace survives updates; packages may not</h2>
<p>The shared workspace is <code>/workspace</code>. Have Bots keep project files there and organize by project folder. Files, browser state, and supported logins are designed to survive ordinary computer updates and recovery. Temp directories, manually installed packages, and uncommitted app state should be treated as disposable. Staff also note: Update Computer keeps files and logins but rebuilds the OS image, so apt/apps/daemons disappear; idle machines sleep and background processes die. Keep a software list in a file and have the Bot reinstall after updates.</p>
<p>Recovery order, from xAI troubleshooting re-read 2026-09-22: Retry, restart the app, Recover computer when offered, then Settings → Updates → Update under Grok Bot's Computer. Reset only if those fail and you accept losing recent unsynced work. Update and Recover keep synced bots, files, and logins, and they remove installed apps on the computer. Reset can drop unsynced bots and files. Chat history lives outside the box. Which button removes what: <a href="/troubleshooting/recover-vs-reset/">Update versus Recover versus Reset</a>.</p>
<h2>Local computer is a different permission surface</h2>
<p>The cloud computer is not the Mac/Windows in front of you. Only when Settings → General → Agent → Execution on Local Computer is on and you approve does a Bot run commands locally. Default is ask every time. Keep Never allowed unless you have a clear reason. Staff also note: a Grok Bot login counts as a Cursor device, and the cloud workspace may count as another — that can hit Too many computers.</p>
<h2>Common misconceptions</h2>
<ul>
<li>Using “life Bot / work Bot” as isolation. They see the same logins.</li>
<li>Pasting API keys into chat. Use the secrets card; see <a href="https://cursor.com/help/grok-bot/secrets">Store secrets securely</a>.</li>
<li>Resetting when the computer is briefly unreachable. Prefer Recover / Update. When the desktop is black but iOS still works, Reset can delete Bots — wait for an official rebuild.</li>
<li>Treating WhatsApp linked-device sessions as durable state. Refresh keeps /workspace, browser profile, and ~/.config, but not ~/.local/state.</li>
</ul>
<p>Once computer use is stable, save “done right once” — <a href="/learn/skills-routines/">skills first, then routines</a>. Stack with X and Cloud Agents: <a href="/learn/ops/">ops</a>.</p>
''' + _faq_html(COMPUTER_FAQS) + '''
%s
</div></section>
''' % pager("/learn/computer/")
    return body

def skills():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 5</p>
<h1>Grok Bot skills, routines, and Teach a task</h1>
<p>Official docs split two building blocks cleanly: a <strong>skill</strong> is a reusable “how” instruction; a <strong>routine</strong> tells a specific Bot “when” — on a schedule, or by event when supported. The right order is: complete one successful task, harden the method, save it as a skill, <em>then</em> automate. Skip the middle and the routine inherits every unspoken assumption, then runs for days before you notice bad output — operators and official docs say the same thing.</p>
<p>If you already have a roster, read this page as step 3–4 of <a href="/learn/operator/">after week one</a>. Johnny Nel: each Bot is a job; the mega-chat is the failure mode. Nate’s public CoS walkthrough: the coordinator delegates first and does not do specialist work. mrfundman: Teach a task on a real CMS instead of writing the script first.</p>
<h2>Copy this skill, then edit the brackets</h2>
<p>Official fields: when to use it, inputs and permissions, steps, how to verify, what to return, and what must be approved. This template is original to this site. It is not a reprint of a share link.</p>
<div class="job-card">
<p class="kicker">Skill draft</p>
<h3>How — after one good run</h3>
<pre><code>When to use: [one job this Bot owns]
Inputs: [file, connector, or /workspace path]
Permissions: read unless I name a write
Steps:
1. [first checkable action]
2. [second]
Verify: [what “done” looks like, with a cite]
Return: [format I can review in one screen]
Must be approved before: send, delete, pay, create Bots, change production
If a source is missing: stop and report. Do not invent.
Do not: treat last week’s chat as the source of truth — read the file.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<h2>Saving a skill</h2>
<p>A skill should state: when to use it, inputs and permissions, steps, how to verify, what to return, and what must be approved. Skills are available to your Bots, but a given Bot still needs the matching connector or login to execute. On desktop, type <code>/</code> to cite saved skills and <code>@</code> to cite Bots, groups, routines, and connectors. Private skills are enabled per Bot; if the / menu is empty, open Settings → Plugins → Yours.</p>
<p>When Teach a task is available: open a 1:1 chat and computer view → Teach a task → describe the outcome you will demonstrate → do it once → stop recording → review the skill the Bot wrote → test with a safe example before scheduling. Teaching records at most about ten minutes of visible computer actions and does not record the microphone. Do not expose secrets while demonstrating. Learned skills are <strong>drafts</strong> — you still add decision rules, failure handling, and approval boundaries. If the control is missing, you can ask in chat: write a skill from the task we just finished.</p>
<h2>Routines</h2>
<p>Describe to the Bot that should own the repeating work: owner, timezone, input sources, expected outcome, approval boundaries, and what to do when a source is missing. Background routines can run with the laptop closed. Event triggers come from Cursor account integrations (for example a Slack or GitHub notification); that path is not the same as the Slack/GitHub <em>plugin</em> and may need separate authorization. Keep match rules narrow: “every new message” creates noise, burns usage, and acts on irrelevant input.</p>
<p>After create or edit, use Test run. Official warning: tests do <strong>real</strong> things — navigate sites, change files, call connected tools. Use safe inputs; put write actions behind approval. Cap: 50 routines per Bot; the app keeps the latest 20 runs per routine. Deletes take effect immediately with no undo; deleting a Bot takes its routines. After long absences the product may ask whether to keep routines running; no answer pauses them.</p>
<div class="job-card">
<p class="kicker">Routine brief</p>
<h3>When — after two good runs</h3>
<pre><code>Owner Bot: [name]
Timezone: [tz]
Trigger: [weekdays 09:00 — not every Slack message]
Input: [the file or connector from the skill]
Expected outcome: [the same deliverable that already worked twice]
Approval: drafts only. Do not send, delete, or pay.
If the source is missing or stale: report the failure. Do not reuse old data.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p>Staff have added two practical details: routine webhook URL and sender key appear only on desktop, not iOS; “Next run: Run now” display can lag 10–37 minutes in queue, and some runs finish without posting to chat — do not rebuild the routine; ask the Bot for an immediate check.</p>
<h2>Design for trust</h2>
<ul>
<li>Automate preparation, not execution.</li>
<li>Draft, reconcile, and recommend first; send, buy, delete, publish, or change production only with approval.</li>
<li>Say what happens with missing or stale data; retries should be idempotent; partial completion should report where it stopped.</li>
<li>Re-test when a site, connector, or source format changes.</li>
</ul>
<h2>Common misconceptions</h2>
<ul>
<li>Setting routines to run around the clock. Cost-focused tutorials almost always switch to working hours so idle browsing does not eat the weekly pool.</li>
<li>Using “stay quiet” between Bots as a hard constraint. Staff: every Bot-to-Bot message consumes weekly usage; quiet in chat is only a hint. Reliable pattern: one Command Agent plus sub-agents that stop when done, and delete unused specialist Bots.</li>
<li>Seeing skills in a template preview but getting an empty skills array after import. Until fixed: copy skill text from the preview and have the new Bot rebuild them.</li>
</ul>
<p>Skills need real tools — next lesson: <a href="/learn/plugins/">plugins first, browser as fallback</a>. Already running: <a href="/learn/operator/">the six-step path</a>.</p>
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
%s
</div></section>
''' % pager("/learn/skills-routines/")
    return body

def plugins():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 6</p>
<h1>Grok Bot plugins first, browser as fallback</h1>
<p>Grok Bot’s integration surface is called Plugins in the app and co-locates connectors, MCP, and packaged skills. Official computer docs are clear: <strong>prefer a connector when one exists</strong> — usually more stable than clicking the web; use the cloud browser when there is no connector or when a visual flow is not exposed. Cursor Help <a href="https://cursor.com/help/grok-bot/connect-plugins">Connect plugins</a>: sidebar Plugins, or a Connect card in chat; on phone tap the top-left avatar then Plugins. Authorization finishes in the browser; if you see Waiting for authorization, use Reopen to bring the tab back. The Cursor account relationship — login, usage, inherited marketplace — is on <a href="/learn/cursor/">Cursor and Grok Bot</a>.</p>
<p>Installed connectors are <strong>account-level</strong>, not isolated to one Bot. MindStudio also observed: authorize GitHub for one Bot and later Bots can use it. Team admins can disable marketplace plugins in Cursor Teams; you then see Disabled by team admin.</p>
<p>Do not put secrets in chat or ordinary files. Use the official secrets card. <a href="https://github.com/xai-org/plugin-marketplace">xai-org/plugin-marketplace</a> is the .grok-plugin marketplace Grok Bot inherits under Cursor’s plugin policy. High-star packs with a documented Grok Bot install path sit on <a href="/use-cases/#skills">use cases → Skills</a> — Compound Engineering installs in the Cursor marketplace; do not clone it onto the Bot computer. Skip 0–1★ “195 SKILL.md” dumps.</p>
<h2>Pick the surface before you click</h2>
<ol>
<li><strong>Official connector exists</strong> — use it. Wayne Sutton’s site-from-the-phone post ran Convex and Cloudflare plugins, not a shopping crawl. Gergely Orosz put support mail and Stripe behind a human confirm. Box wrote back through MCP after reconciling a pack.</li>
<li><strong>The job is visual-only</strong> — cloud browser, then Teach a task. Official docs: prefer a connector when one exists.</li>
<li><strong>You have a public HTTPS MCP</strong> — ask the Bot in chat to add it (next section). Localhost on your laptop is unreachable.</li>
<li><strong>You need the company VPN or keys on your machine</strong> — Execution on Local Computer, or leave the managed box — <a href="/compare/">alternatives</a>.</li>
</ol>
<h2>Remote MCP — not stdio on your laptop</h2>
<p>Staff confirmed: Grok Bot <strong>cannot</strong> attach local or stdio MCP; use remote HTTP MCP or the cloud browser. There is no “custom connector” settings form — ask the Bot in chat to add an MCP server (public HTTPS streamable HTTP/SSE), confirm details, and new tools appear from the next message. An MCP that only listens on localhost on your PC is unreachable from the cloud computer.</p>
<h2>Auth that was still broken at fetch time (still documented in Help)</h2>
<ul>
<li><strong>Zoom error 4700:</strong> the catalog Zoom plugin hard-codes the callback as http://localhost:8787/callback; Zoom rejects it. Official Help: no workaround — wait for them to remove localhost. <a href="https://cursor.com/help/grok-bot/connect-plugins">Connect plugins</a></li>
<li><strong>Gmail plugin OAuth:</strong> staff say the Grok Bot side is broken; authorizing Gmail from Cursor (a different path) shares the connection into Grok Bot. The Gmail connector can also list attachment metadata but not download bytes — use the cloud browser or put files on Drive.</li>
<li><strong>Notion Invalid redirect_uri:</strong> login state lives on the account, so retry fails; use Re-authenticate instead of Connect.</li>
<li><strong>Canva Invalid redirect URI on iOS:</strong> app link and web redirect mismatch; connect from desktop and the connector syncs to iPhone.</li>
<li><strong>Official X plugin:</strong> connect/refresh failures across desktop / Cloud / Grok Bot (including connected with tools=0) — waiting on X-side app config fixes.</li>
<li><strong>GitHub “connected” but Authorization header badly formatted:</strong> long-press the account → Remove → sign in again.</li>
</ul>
<p>Drive MCP is file-level only; to edit Google Doc body or Sheet cells, use the separate Docs / Sheets connectors added from the marketplace under the same Google account.</p>
<h2>Common misconceptions</h2>
<ul>
<li>Treating Slack event wakeups as “installing Grok Bot as a Slack App.” The awesome list has a dedicated note separating those.</li>
<li>Installing a company VPN client on the Bot computer. Staff warn: the cloud computer cannot join enterprise VPN today; bad installs can take the box offline. For internal sites use Execution on Local Computer on a machine already on VPN, or Team Setup docs (Tailscale / Cloudflare Tunnel).</li>
<li>Installing every marketplace plugin. Connect only what the workflow needs; prefer read-only service accounts when possible.</li>
</ul>
<p>More plugins make weekly usage and approval rules the main topic — <a href="/learn/cost-and-pitfalls/">cost, spillover, and approval pitfalls</a>. Operator order: <a href="/learn/operator/">after week one</a>. Stack (X, Cloud Agent, MCP): <a href="/learn/ops/">ops</a>.</p>
%s
</div></section>
''' % pager("/learn/plugins/")
    return body

def cost():
    body = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Lesson 7</p>
<h1>Grok Bot usage, On-Demand, and cost pitfalls</h1>
<p>Grok Bot has <strong>no separate SKU</strong>. You buy Cursor or SuperGrok / X, and Bot appears as a bundled feature with weekly-resetting usage. Numbers and eligibility change; this page covers mechanics and pitfalls. Dated price/eligibility contrast: <a href="/pricing/">pricing snapshot</a>.</p>
<h2>How usage works (official)</h2>
<p>Cursor Help <a href="https://cursor.com/help/grok-bot/plans">Plans and billing</a>: paid access includes weekly-resetting usage; when it runs out, if the account has on-demand enabled, overage can go to shared on-demand spend. Metering is on the Cursor account, not on Grok or X. Linking SuperGrok / X Premium+ is a usage grant for <strong>that same</strong> Cursor account — it does not open a second meter on the Grok side and does not change your Cursor plan. Linking is permanent.</p>
<p>Trial is usage credits, not a fixed number of days (plus a 7-day window). Credits debit by agent steps and tokens, not by how many messages you send. A large task can exhaust them at once. Spent trial credits are not restored. macOS and iOS share one bucket.</p>
<p>Staff later corrected several easy-to-spread points (forum; see troubleshooting sources):</p>
<ul>
<li>On Pro, Grok Bot has its own weekly pool, separate from Cursor plan usage; spillover still enters shared On-Demand.</li>
<li>Spend order: Grok Bot weekly pool → promo/referral credits → paid On-Demand. No in-app warning.</li>
<li>Setting the On-Demand cap to $0 blocks paid spillover but <strong>does not</strong> stop credits from being drained.</li>
<li>Pro’s $20 Other Models allowance is not the Grok Bot weekly pool.</li>
<li>Cursor Cloud Agents launched by Grok Bot consume Cursor plan usage; Grok Bot chat is a different allowance.</li>
</ul>
<h2>Eligibility (official pages on 2026-09-20)</h2>
<p>Cursor Help and the xAI FAQ now both include every paid individual Cursor plan (including Pro) and Cursor Teams. You can also link personal SuperGrok / Plus / Heavy / X Premium+. Lite and SuperGrok Team/Enterprise still cannot link. Remaining wording still differs on whether Cursor and SuperGrok grants stack. Open the originals on the <a href="/pricing/">pricing snapshot</a>; this site does not invent USD figures.</p>
<h2>Pitfalls already showing up repeatedly in the community</h2>
<ul>
<li><strong>Weekly usage can burn in a day.</strong> An xAI engineer has publicly acknowledged that complaint direction. Chatty Chief-of-Staff threads and sorting a decade of inbox are user hypotheses, not our measurements. Mitigations: keep routines in working hours; use connectors instead of pure browsing for heavy work; keep Chief-of-Staff chats short; do not bulk-sort history on day one. KC’s public note that many multi-bot setups go quiet after 10–14 days is a warning to put memory in <code>/workspace</code>, not a number we repeated — see <a href="/learn/operator/">after week one</a>.</li>
<li><strong>Auto-review is best-effort.</strong> Require Approval outranks Always Allow; do not write wide rules like “allow everything in the browser.” Personal Auto-review rules live on the current desktop and sync to its Grok Bot computer — check again after switching desktops.</li>
<li><strong>Bots are not a security boundary.</strong> See <a href="/learn/computer/">shared computer</a>.</li>
<li><strong>Cloud computers sleep and can auto-update when idle.</strong> Dead background processes are not a failure mode by themselves.</li>
</ul>
<h2>Common misconceptions</h2>
<ul>
<li>Assuming linking SuperGrok Heavy still bundles Cursor Ultra. Staff announced that promo ended on 2026-08-21; linking is only a usage grant. Older Help pages lagged — third-party pricing surveys cite dated wording; we do not treat them as a price list.</li>
<li>Leaving On-Demand uncapped after the weekly pool is gone.</li>
<li>Treating skills inside a Bot template as already installed.</li>
</ul>
<h2>Operator checklist (after the first good week)</h2>
<ul>
<li>One pinned door. Specialist Bots do not also sit in the same mega-chat.</li>
<li>Routines fire in working hours unless the job is truly overnight (Krista Letz’s prospecting pattern — still stop at drafts).</li>
<li>On-Demand cap is a number you chose, not the default leftover.</li>
<li>Auto-review: Require Approval outranks Always Allow. Re-check after you switch desktops.</li>
<li>Cloud Agents launched by a Bot spend the Cursor plan pool, not the Bot weekly pool.</li>
</ul>
<p>Next: <a href="/learn/operator/">the operator path</a>, then what others shipped — <a href="/use-cases/">use cases</a> — or <a href="/troubleshooting/not-responding/">not responding</a> if bots go silent while the computer still opens.</p>
%s
</div></section>
''' % pager("/learn/cost-and-pitfalls/")
    return body
