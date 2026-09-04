# -*- coding: utf-8 -*-
def pricing():
    return """
<section class="band"><div class="wrap prose">
<p class="kicker">Snapshot dated 2026-09-04</p>
<h1>Grok Bot pricing: free, plans, and enterprise trial</h1>
<p>There is no standalone Grok Bot price. Access is bundled with Cursor or a linkable personal SuperGrok / X subscription, with weekly-resetting usage. How that Cursor account relates to the Bot app — login, plugins, not an IDE panel — is on <a href="/learn/cursor/">Cursor and Grok Bot</a>. Below is an official-source contrast for <strong>fetch day 2026-09-04</strong>. If a page does not state a number, this site does not invent one.</p>
<div class="callout">
<p><strong>Enterprise two-week trial (official news, 2026-09).</strong> <a href="https://x.ai/news/grok-bot-for-enterprise">x.ai/news/grok-bot-for-enterprise</a> says Grok and Cursor Enterprise customers get Grok Bot free for the next two weeks and can invite the whole organization, including people without an existing seat. That window is time-limited — open the news post, not a finance reprint, for the current end date. It is not a consumer free tier.</p>
</div>
<h2>What official pages say (side by side, not adjudicated)</h2>
<table>
<thead><tr><th>Source</th><th>Fetched</th><th>Eligibility wording</th></tr></thead>
<tbody>
<tr><td><a href="https://cursor.com/help/grok-bot/plans">cursor.com/help/grok-bot/plans</a></td><td>2026-09-04</td><td>All paid personal Cursor plans (Pro / Pro+ / Ultra) and Cursor Teams include Grok Bot. You can also link personal SuperGrok, Plus, Heavy, or X Premium+. Lite and SuperGrok Team/Enterprise cannot link. Linking is a usage grant, not a Cursor plan, and cannot be unlinked by you.</td></tr>
<tr><td><a href="https://docs.x.ai/grok-bot/faq">docs.x.ai/grok-bot/faq</a></td><td>2026-09-04</td><td>Lists SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Cursor Ultra, Cursor Teams Standard and Premium. Does not name Cursor Pro or base SuperGrok in that paragraph. Also: if you have both Cursor and SuperGrok, Grok Bot uses the side with more usage.</td></tr>
<tr><td><a href="https://docs.x.ai/grok-bot/get-started">Get started</a></td><td>2026-09-04</td><td>Before you start you need: SuperGrok Plus, Heavy, Cursor Pro+, Ultra, or Teams Standard/Premium.</td></tr>
<tr><td><a href="https://x.ai/news/grok-bot-more-plans">x.ai/news/grok-bot-more-plans</a></td><td>In-article date 2026-08-26</td><td>Grok Bot is now included with SuperGrok, Cursor Pro, and all Cursor Teams plans. Body list includes SuperGrok / Plus / Heavy and Cursor Pro / Pro+ / Ultra plus Teams Standard and Premium.</td></tr>
<tr><td><a href="https://cursor.com/help/grok-bot/supergrok">Link SuperGrok</a></td><td>2026-09-04</td><td>Heavy has the highest linked usage, then Plus, then SuperGrok, then X Premium+ below Plus. Team/Enterprise/Lite are ineligible. Linking is permanent.</td></tr>
</tbody>
</table>
<div class="callout warn"><p><strong>Conflict.</strong> FAQ / Get started on the fetch day did not put Cursor Pro and base SuperGrok on the list; Cursor Help and the August 26 news post did. Trust the page you open, not this table alone.</p></div>
<h2>Mechanics (official Help — no specific allowance numbers)</h2>
<ul>
<li>Weekly usage is metered on the Cursor account; macOS and iOS share one bucket.</li>
<li>When it runs out, if on-demand is enabled, spend can continue on shared on-demand.</li>
<li>Trial is usage credits plus a 7-day window, debited by agent steps and tokens — not by message count. Spent credits are not restored.</li>
<li>No separate Grok Bot subscription is required.</li>
<li>Price cards on x.ai/bot had concrete numbers stripped by page structure at fetch time; this site <strong>does not fill blanks</strong>. Open <a href="https://x.ai/bot">x.ai/bot</a> for current list prices.</li>
</ul>
<h2>Third-party surveys (dated contrast only — not a price list)</h2>
<p><a href="https://cellcog.ai/blog/grok-bot-pricing/">CellCog</a> says updated 2026-09-03 and lists eight paths with USD figures. Those numbers were compiled by that author from pages they cite — <strong>this site does not republish them as fact</strong>. If you need USD figures, open that article and Cursor / xAI pricing side by side and check they still match.</p>
<p>MindStudio’s setup piece (2026-08-12) still says “needs Cursor Ultra” — stale relative to the August 26 news post.</p>
<p>AI Builder Club (updated 2026-08-30) narrates the timeline from launch-day high tiers to the August 21 expansion and August 26 expansion again; its USD figures likewise belong in the original.</p>
<p>If you do not want a managed seat, read <a href="/compare/">Grok Bot alternatives</a>. Those repos are not unofficial clients, and this site does not invent their prices either.</p>
<p>Next: put weekly usage where it matters — <a href="/learn/cost-and-pitfalls/">cost and pitfalls</a>; connectivity or billing oddities — <a href="/troubleshooting/">troubleshooting</a>.</p>
<h2>FAQ</h2>
<div class="faq card">
<details><summary>Is Grok Bot free?</summary><p>There is no consumer free tier and no standalone SKU. Access is bundled with paid Cursor or a linkable SuperGrok / X plan. Enterprise had a separate two-week org trial — open the dated news post.</p></details>
<details><summary>Which plan do I need?</summary><p>Official pages disagree on Cursor Pro and base SuperGrok. Cursor Help and the August 26 news post include them; the xAI FAQ and Get started on fetch day did not. Open those originals. This site does not pick a winner.</p></details>
<details><summary>Does linking SuperGrok create a second bill?</summary><p>No. Linking is a usage grant on the same Cursor account. You cannot unlink it yourself. It does not open a Grok-side meter.</p></details>
</div>
</div></section>
"""

PRICING_FAQS = [
    ("Is Grok Bot free?",
     "There is no consumer free tier and no standalone SKU. Access is bundled with paid Cursor or a linkable SuperGrok / X plan. Enterprise had a separate two-week org trial — open the dated news post."),
    ("Which plan do I need?",
     "Official pages disagree on Cursor Pro and base SuperGrok. Cursor Help and the August 26 news post include them; the xAI FAQ and Get started on fetch day did not. Open those originals. This site does not pick a winner."),
    ("Does linking SuperGrok create a second bill?",
     "No. Linking is a usage grant on the same Cursor account. You cannot unlink it yourself. It does not open a Grok-side meter."),
]
