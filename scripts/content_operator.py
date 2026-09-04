# -*- coding: utf-8 -*-
from html import escape

OPERATOR_FAQS = [
    ("I already have twelve Bots. Where do I start?",
     "Do not add a thirteenth. Pin one Chief of Staff whose only job is to inventory the roster, name what each Bot owns, and keep a what’s-left page. Debbie’s getting-started notes and Johnny Nel’s job-board post both treat the mega-chat as the failure mode."),
    ("When should I turn a job into a routine?",
     "After two checkable runs of the same method, and after you have saved a skill with approval boundaries. Official docs: Test run does real things. Field posts that skip this step are the ones that go quiet after week two."),
    ("Can I quote someone’s billed outcome?",
     "No. This page cites named posts as patterns. Dollar recoveries, “one plan replaces a department,” and timed “15 minute” claims stay in the original. Open the source."),
]


def operator():
    faqs = []
    for q, a in OPERATOR_FAQS:
        faqs.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    return '''
<section class="hero"><div class="wrap">
<p class="kicker">Already running</p>
<h1>How operators run Grok Bot after week one</h1>
<p class="lede">Hiring Bots is easy. Managing them is the job. This path is built from official docs plus named field posts — Debbie, Nate, Peter Yang, Johnny Nel, s1rozha, Gergely Orosz, and the official @bot recap. Not billed outcomes.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="#path">The six-step path</a>
  <a class="btn btn-secondary" href="/use-cases/">54 field cases</a>
  <a class="btn btn-ghost" href="/learn/first-bot/">Still on day one?</a>
</div>
</div></section>

<section class="band" id="path"><div class="wrap prose">
<p class="meta">Fetched and re-checked against public posts through 2026-09-04, plus a fresh X pass on 2026-09-04. Isolation is still per user. Screens are not a fence. Official packages stay on <a href="https://x.ai/bot">x.ai/bot</a>.</p>

<h2>1. Kill the mega-chat</h2>
<p>Johnny Nel’s job-board post puts it in one line: <em>one Chief of Staff plus specialists, not one mega-chat</em>. Each Bot is a job, not a whole company. Nate’s getting-started videos make the Chief of Staff refuse specialist work — otherwise everything bottlenecks through one agent. Debbie’s notes: start with one door, let it propose the team, do not open a Bot for every sub-task.</p>
<p>If your sidebar is already a crowd, the first operator job is an audit, not a new hire. Ask the pinned Bot to list every teammate, the last useful output, and what to merge. That is Debbie’s move: turn the Chief of Staff on the roster you already built.</p>
<div class="job-card">
<p class="kicker">Standing rules · Chief of Staff</p>
<h3>You talk to one door</h3>
<pre><code>You are the only Bot I talk to. Before you do a task, check whether another Bot already owns it and delegate. Only do the work yourself if no specialist fits. Bring results back here.

Keep a what’s-left page in /workspace. For each item: owner Bot, source, next step, whether I owe a decision.

Never: send email or posts, create or delete Bots, pay, or invent a “done” if a specialist produced nothing.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p class="muted">Sources: <a href="https://x.com/johnnynelai/status/2090051654468989071">Johnny Nel</a> · <a href="https://debbie.codes/blog/how-to-get-started-with-grok-bot">Debbie</a> · Nate’s CoS description as shown in public walkthroughs (delegate first). Official PM guide: <a href="https://x.ai/bot/guides/grok-bot-for-pms">Grok Bot for PMs</a>.</p>

<h2>2. One job per Bot — then stop using it as chat</h2>
<p>s1rozha’s field note: Email Bot on a 7:30 timer, sponsor-lead labels on another timer, calendar Bot separate. The trick is stopping using Grok Bot as chat. Ben Lang’s internal list (quoted in community follow-ups) and Johnny’s board add a second artifact: a Notion or <code>/workspace</code> page you can ask “what’s left.”</p>
<div class="job-card">
<p class="kicker">What’s-left page</p>
<h3>Outstanding work, one file</h3>
<pre><code>Create or update /workspace/whats-left.md. One row per open item: date, owner Bot, source (link or path), status, what you need from me. Do not start new work that is not on this page. If a specialist stalled, retry once, then flag me.</code></pre>
<button type="button" class="copy-btn" data-copy>Copy</button>
</div>
<p class="muted">Sources: <a href="https://x.com/s1rozha_/status/2091585690957996515">s1rozha</a> · <a href="https://x.com/johnnynelai/status/2090051654468989071">Johnny Nel</a> · <a href="https://x.com/benln/status/2087929147406299313">Ben Lang</a>.</p>

<h2>3. Teach once. The skill is still a draft</h2>
<p>Official Teach a task: demonstrate up to about ten minutes of screen, no microphone, then review the skill the Bot wrote. mrfundman used it on a real WordPress update instead of writing a deploy script first. Community tips posts converge on the same order: do the thing once, never start from a 2,000-word prompt.</p>
<p>The learned skill is a <strong>draft</strong>. Add when to use it, what “done” looks like, what happens if the source is missing, and what must be approved. Then test on a <em>different</em> safe input. Details and the copyable template: <a href="/learn/skills-routines/">skills and routines</a>.</p>
<p class="muted">Sources: <a href="https://docs.x.ai/grok-bot/skills-routines-and-automations">official skills docs</a> · <a href="https://x.com/mrfundman/status/2089760255890571404">mrfundman</a> · <a href="https://x.com/ReallyPhant/status/2089736697785331982">ReallyPhant tips</a>.</p>

<h2>4. Routine only after two good runs</h2>
<p>KC’s widely bookmarked “Hiring is easy / managing is the skill” post says most multi-bot setups go quiet after 10–14 days. Treat that as a warning, not a measurement we repeated. The operator fix in official docs is boring: Test run does real things; cap is 50 routines per Bot; keep the latest 20 runs; delete has no undo.</p>
<p>s1rozha and the YouTube “support Bot via routines” demo both schedule <em>after</em> the method exists. Event triggers (Slack / GitHub) are not the same as installing those plugins. Working hours beat 24/7 browsing if you care about the weekly pool — <a href="/learn/cost-and-pitfalls/">usage and On-Demand</a>.</p>
<p class="muted">Sources: <a href="https://x.com/karanC_12/status/2090092775656267934">KC</a> · <a href="https://www.youtube.com/watch?v=bUALqTpUze0">routines support demo</a> · official routine example in xAI docs.</p>

<h2>5. Connectors first. Money stays with you</h2>
<p>Wayne Sutton’s site-from-the-phone post used Convex and Cloudflare plugins, not a cloud-browser shopping spree. Gergely Orosz connected support mail and Stripe and still required a human before money moved. Official @bot later shipped Stripe Link the same way: the Bot raises a spend request; you approve; a one-use card appears.</p>
<p>Darian Shirazi’s refund chase is the same shape: find the work, draft the mail, do not treat the author’s fee comparison as our number. Installed connectors are account-level — every Bot can see them. How to add remote MCP (not localhost): <a href="/learn/plugins/">plugins</a>.</p>
<p class="muted">Sources: <a href="https://x.com/waynesutton/status/2088416215203295346">Wayne Sutton</a> · <a href="https://x.com/GergelyOrosz/status/2090085668768694562">Gergely Orosz</a> · <a href="https://x.com/bot/status/2093419921007108385">@bot Stripe Link</a> · <a href="https://x.com/darian314/status/2089381004524093752">Darian Shirazi</a>.</p>

<h2>6. Put memory in /workspace, not in chat</h2>
<p>RefoundAI’s first-week writeup: standing rules in the Bot description, source-of-truth files, a daily plan that cites sources, then a routine. Logos52 publishes weekday dumps of what a fleet writes under <code>/workspace</code>. jblack4vols keeps dated decision logs per Bot. That is how you survive the 10–14 day fade: the next run reads a file, not last Tuesday’s chat.</p>
<p>The computer is still one machine. Lee Robinson and Logan’s posts are design notes — thin client, always-on box, browser as a tool — not a license to treat a second Bot as a fence. Shared-computer lesson: <a href="/learn/computer/">one computer per user</a>.</p>
<p class="muted">Sources: <a href="https://refoundai.com/blog/how-to-run-your-business-with-grok-bot/">RefoundAI</a> · <a href="https://github.com/Logos52/grok-bot-packets">Logos52 packets</a> · <a href="https://github.com/jblack4vols/grok-bot">jblack4vols logs</a> · <a href="https://x.com/leerob/status/2089169319099777364">Lee Robinson</a>.</p>
</div></section>

<section class="band"><div class="wrap">
<h2>Jobs people actually ran (then stop copying the roster)</h2>
<p class="lede">Official <a href="https://x.com/bot/status/2090168861912170972">@bot recap</a> quoted eleven field posts. Use them as job ideas after step 1, not as a day-one org chart. Full cards: <a href="/use-cases/">use cases</a>.</p>
<div class="mistakes">
  <a class="mistake" href="https://x.com/petergyang/status/2089724101070086482"><p class="tag">Peter Yang</p><h3>Declutter with approval</h3><p>Audit mail, Drive, subs. Wait before delete.</p></a>
  <a class="mistake" href="https://x.com/GergelyOrosz/status/2090085668768694562"><p class="tag">Gergely Orosz</p><h3>Support plus refunds</h3><p>Human confirmation before money moves.</p></a>
  <a class="mistake" href="https://x.com/kristaletz/status/2089103618121314689"><p class="tag">Krista Letz</p><h3>Overnight prospecting</h3><p>Chief of Staff plus per-account specialists. Pattern, not a quota.</p></a>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>What this path will not take from X</h2>
<div class="grid-2">
  <article class="card"><h3>Eligibility screenshots</h3><p>Replies that say “needs Heavy or Ultra only” are stale against the 2026-08-26 news post and Cursor Help. Open <a href="/pricing/">the dated snapshot</a>.</p></article>
  <article class="card"><h3>Department-replacement math</h3><p>Posts that map one plan to five hires stay in the original. This site does not restate billed headcount.</p></article>
</div>
<p>When the roster is quiet and you need X, Cursor Cloud Agents, or remote MCP as one stack — <a href="/learn/ops/">how operators run those four surfaces</a>. If you want the machine on your network instead of the managed box, that is a different product family — <a href="/compare/">official vs self-hosted</a>.</p>
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
''' % "".join(faqs), OPERATOR_FAQS
