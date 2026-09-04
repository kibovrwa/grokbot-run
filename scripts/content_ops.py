# -*- coding: utf-8 -*-
from html import escape

OPS_FAQS = [
    ("Can the Bot post to my X account by itself?",
     "Treat publish as a human gate. Official @bot (2026-08-29) announced connect-your-profile plus included API credits. Min Choi’s follow-up lists read, search, archive, and public-account pulls. This site does not treat “schedule and post everywhere” threads as a shipped write API. Draft in /workspace. You hit post."),
    ("Why didn’t a Cursor Cloud Agent start from Grok Bot?",
     "Two different GitHub grants. Cursor’s GitHub app is what Cloud Agents use. The Bot-side GitHub / remote MCP plugin is a second path. A dated forum report also shows launch failing with a GitHub rate-limit line that was not the user’s own quota — paste the full error, do not retry in a loop."),
    ("Can I attach localhost MCP or a Bearer token for X?",
     "No. Grok Bot only reaches public HTTPS MCP from the cloud computer. Do not paste an X Bearer token or API key into chat. Connect the official X plugin, or stop if tools stay at zero."),
    ("Is a second Bot a fence between my X login and work mail?",
     "No. Isolation is per user. Every Bot sees the same computer, cookies, and connectors. Keep the X session on this box only if the whole roster may see it."),
]


def ops():
    faqs = []
    for q, a in OPS_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">Already running · stack</p>
<h1>How operators run X, Cursor, MCP, and the cloud computer</h1>
<p class="lede">Four surfaces, one account. Grok Bot is the signed-in computer. Cursor Cloud Agent is the repo VM that opens a PR. MCP is remote tools. The official X plugin is a research pipe first. You still approve publishes.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="#stack">The stack map</a>
  <a class="btn btn-secondary" href="/learn/operator/">After week one</a>
  <a class="btn btn-ghost" href="/learn/plugins/">Plugins and MCP</a>
</div>
</div></section>

<section class="band" id="stack"><div class="wrap prose">
<p class="meta">Fetched and re-checked against public posts through 2026-09-04, plus a fresh X pass on 2026-09-04. Isolation is still per user. Screens are not a fence. Official packages stay on <a href="https://x.ai/bot">x.ai/bot</a>.</p>

<h2>1. Draw the map before you hire another Bot</h2>
<p>Operators who last past week two stop treating “Grok Bot” as one blob. Simon Loewen’s field note is the clean split: <em>Cloud Agent = the repo VM that opens a PR; Grok Bot = the signed-in computer that keeps going when the laptop closes</em>. Staff on the Cursor forum: there is no codebase plugin. Coding work goes to a Cloud Agent already connected to GitHub.</p>
<ol>
<li><strong>Grok Bot app</strong> — roster, chat, approvals. Not a Cursor IDE panel. Relationship: <a href="/learn/cursor/">Cursor and Grok Bot</a>.</li>
<li><strong>Shared cloud computer</strong> — browser, <code>/workspace</code>, terminal. One machine per user. Lesson: <a href="/learn/computer/">shared computer</a>.</li>
<li><strong>Plugins / remote MCP</strong> — account-level tools. Prefer a connector. No localhost. Lesson: <a href="/learn/plugins/">plugins</a>.</li>
<li><strong>Cursor Cloud Agent</strong> — a different VM on a GitHub repo. The Bot can brief it. You merge.</li>
<li><strong>Official X plugin</strong> — connect the profile; @bot says a developer account and included credits appear. Read and search first.</li>
</ol>
<p>Puneet Singh’s debugging order matches official computer docs: memory in <code>/workspace</code> → MCP / connector → public web → signed-in browser on the box → desktop GUI. Do not open Chrome because the page is there.</p>
<p class="muted">Sources: <a href="https://x.com/SimonLoeweztl8/status/2094837259744784635">Simon Loewen</a> · <a href="https://x.com/iPuneetSingh/status/2095078470783283453">Puneet Singh</a> · Cursor forum: no codebase plugin · <a href="https://x.com/bot/status/2093822274067706170">@bot X support</a>.</p>

<h2>2. Run X as research. Publish stays with you</h2>
<p>Official <a href="https://x.com/bot/status/2093822274067706170">@bot (2026-08-29)</a>: connect your X profile; a developer account is created automatically with included credits. Min Choi’s same-day post is the capability list operators actually use: timeline, posts, mentions, likes, Spaces, advanced search, full-archive, any public account’s recent posts, and who liked. That is a <strong>research database</strong>, not a license to fire the social team.</p>
<p>Peter Yang’s public “five to try” already had an X scout: watch a niche, return angles, you write. Field replies converge on the same gate ygns178 wrote out loud: read mentions, draft in your tone, post only after you approve. Greg Isenberg’s newsletter-desk thread is the same shape for long-form — agents prepare, the operator ships.</p>
<p>If the official X plugin shows connected with tools=0, or refresh fails, that is still documented on the <a href="/learn/plugins/">plugins</a> page. Stop. Do not open x.com login in the cloud browser to type a password. Do not paste a Bearer token. Do not treat a 29-platform scheduler post as the official write path.</p>
<div class="job-card">
<p class="kicker">X · scout</p>
<h3>Angles only. I write.</h3>
<pre><code>You scout X. I write.

Use the official X connector if it is connected and tools appear. If connect failed or tools stay at zero, stop and tell me. Do not open x.com login. Do not ask for a Bearer token or API key.

Watch this niche and these accounts: [list]. Last 24 hours unless I say otherwise.

Return at most 8 posts. For each: url, first line, why it moved, whether I have a receipt they do not. If nothing is moving, say “quiet window.”

Never like, follow, reply, quote, bookmark, or post. Never draft a copycat.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<div class="job-card">
<p class="kicker">X · mentions</p>
<h3>Drafts in a file. I hit reply.</h3>
<pre><code>Read my mentions from the official X connector, not the cloud browser. Draft replies in the voice samples in /workspace/voice.md. Write drafts to /workspace/x-drafts.md with the original url and a one-line risk flag.

Do not post, reply, like, or follow. Flag legal, payment, or account-security asks. If the connector has no tools, stop.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p class="muted">Sources: <a href="https://x.com/bot/status/2093822274067706170">@bot</a> · <a href="https://x.com/minchoi/status/2093907058290512047">Min Choi</a> · <a href="https://www.youtube.com/watch?v=MkVcHbviYOw">Peter Yang five to try</a> · <a href="https://x.com/gregisenberg/status/2090901264309875088">Greg Isenberg</a>.</p>

<h2>3. Cursor does the repo. The Bot writes the brief</h2>
<p>n2parko’s SpaceXAI product shots showed a roster handing off PRs. _duyet runs one Bot per repo and talks to a leader that delegates. M3NT8L’s field note: when you connect GitHub in Grok Bot and ask for coding work, the Bot delegates to a Cursor Cloud Agent (whatever model Cursor offers). iam4x wires Sentry → Cloud Agent → PR for review. Michael Fenech’s CoS brief is the operator sentence: investigate, spin a Cloud Agent, open a PR. Timed “three minutes later” claims stay in the original.</p>
<p>The handoff is still a file. CitiZenSleuthX asked for shared threads between Grok Bot and Cloud Agent runs started in the Cursor app — there isn’t one. People copy a <code>/workspace</code> brief. Compound Engineering and similar packs install once in the Cursor marketplace; Grok Bot inherits that library. Do not clone those repos onto the Bot computer. Community CLI <a href="/tools/grok-bot-skill/">grok-bot-skill</a> is the other direction: a coding agent calling a Bot, not the official app.</p>
<p>Launch can fail. A dated Cursor forum thread: Grok Bot returns “GitHub is rate limiting requests” while the user’s own GitHub quota is fine. Two grants also confuse people — Cursor’s GitHub app (Cloud Agent) is not the Bot-side GitHub / remote MCP plugin. If launch fails, paste the full error. Do not retry in a loop. You merge.</p>
<div class="job-card">
<p class="kicker">Cursor · Cloud Agent</p>
<h3>Brief the repo VM. I merge.</h3>
<pre><code>Write /workspace/cloud-agent-brief.md for a Cursor Cloud Agent.

Include: repo, branch, failing test or issue url, what “done” looks like, files you must not touch, and that I merge the PR.

Do not start the Cloud Agent until I say go. If launch returns a GitHub rate-limit line or “reconnect GitHub,” stop and paste the full error. Do not retry in a loop.

The Bot computer is not the repo VM. Do not clone the repo onto this box. Do not paste a GitHub PAT into chat.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p class="muted">Sources: <a href="https://x.com/n2parko/status/2087251704744235298">n2parko</a> · <a href="https://x.com/_duyet/status/2090492642924847165">_duyet</a> · <a href="https://x.com/M3NT8L/status/2091662235039158290">M3NT8L</a> · <a href="https://x.com/iam4x/status/2090403658374545418">iam4x</a> · <a href="https://x.com/CitiZenSleuthX/status/2093736538186072301">CitiZenSleuthX</a> · <a href="https://forum.cursor.com/t/grokbot-cant-start-cloud-agent-from-cursor/168697">forum: launch rate-limit</a>.</p>

<h2>4. MCP is remote. Money and sends still need you</h2>
<p>Official computer docs: prefer a connector when one exists. Staff: Grok Bot cannot attach local or stdio MCP. Ask the Bot in chat to add a public HTTPS streamable HTTP/SSE server. An MCP that only listens on localhost on your laptop is unreachable from the cloud box.</p>
<p>Wayne Sutton shipped a site from the phone on Convex and Cloudflare plugins, not a cloud-browser shopping spree. Gergely Orosz connected support mail and Stripe and still required a human before money moved. Box wrote back through MCP after a reconcile. Gojiberry’s sales pack is a hosted MCP — do not invent contacts. The GitHub remote MCP plugin is a different grant from Cursor’s GitHub app; treat them as two doors.</p>
<div class="job-card">
<p class="kicker">MCP · add</p>
<h3>Public HTTPS only</h3>
<pre><code>Add this remote MCP: [https URL]. Confirm it is public HTTPS (streamable HTTP or SSE), not localhost and not stdio on my laptop.

After it appears, list the new tools in /workspace/tools.md. Do not send, pay, delete, or write until I approve.

If add fails, stop. Do not install a VPN client on this computer. Do not paste API keys into chat — use the secrets card.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p class="muted">Sources: <a href="https://docs.x.ai/grok-bot/skills-routines-and-automations">official skills / computer docs</a> · <a href="https://x.com/waynesutton/status/2088416215203295346">Wayne Sutton</a> · <a href="https://x.com/GergelyOrosz/status/2090085668768694562">Gergely Orosz</a> · <a href="https://cursor.com/help/grok-bot/connect-plugins">Connect plugins</a>.</p>

<h2>5. The computer is the factory floor</h2>
<p>Lee Robinson’s public notes: thin client, always-on box, browser as a tool. That is design, not a second fence. Every connector you install is account-level — the X session, GitHub, Stripe, and mail are visible to the whole roster. Keep standing rules and source-of-truth files in <code>/workspace</code>. Logos52 dumps what a fleet writes there; jblack4vols keeps dated logs. That is how the next run reads a file instead of last Tuesday’s chat — same rule as <a href="/learn/operator/">after week one</a>.</p>
<p>Execution on Local Computer is a different surface: only when you turn it on and approve. Default is ask every time. The cloud box cannot join an enterprise VPN; a bad VPN client can take the machine offline. Internal sites: local execution on a machine already on VPN, or Tailscale / Cloudflare Tunnel per Team Setup docs.</p>
<p class="muted">Sources: <a href="https://x.com/leerob/status/2089169319099777364">Lee Robinson</a> · <a href="https://forum.cursor.com/t/grok-bot-ship-real-session-fences-bots-are-not-a-security-boundary/168476">Bots are not a security boundary</a> · <a href="/learn/computer/">shared computer</a>.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>What this page will not take from X</h2>
<div class="grid-2">
  <article class="card"><h3>Agency-killer posts</h3><p>“Your bot can now post to every network and replace the agency” stays in the original. This site does not restate that as a shipped write API.</p></article>
  <article class="card"><h3>Bundle and headcount math</h3><p>Plan-vs-plan dollar stacks and “one seat replaces a department” stay in the original. Open <a href="/pricing/">the dated snapshot</a>.</p></article>
</div>
<p>Reconstructed 2,000-word “Head of Content” templates and 0–1★ SKILL dumps stay off this page. Copy the short briefs above, then edit the brackets.</p>
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
''' % "".join(faqs), OPS_FAQS
