# -*- coding: utf-8 -*-
def pricing():
    return """
<section class="band"><div class="wrap prose">
<p class="kicker">Snapshot dated 2026-09-20</p>
<h1>Grok Bot pricing: free, plans, and enterprise trial</h1>
<p>There is no standalone Grok Bot price. Access is bundled with Cursor or a linkable personal SuperGrok / X subscription, with weekly-resetting usage. How that Cursor account relates to the Bot app — login, plugins, not an IDE panel — is on <a href="/learn/cursor/">Cursor and Grok Bot</a>. Below is an official-source contrast for <strong>fetch day 2026-09-20</strong>. If a page does not state a number, this site does not invent one.</p>
<div class="callout warn">
<p><strong>Enterprise two-week trial is a dated announcement, not a current offer.</strong> The early-September 2026 news post <a href="https://x.ai/news/grok-bot-for-enterprise">x.ai/news/grok-bot-for-enterprise</a> still says Grok and Cursor Enterprise customers get Grok Bot free for the “next two weeks” and can invite the whole organization, including people without an existing seat. That window from early September is expired as of this fetch. Treat the page as a historical announcement. It was never a consumer free tier. Open the news post and your account team for whatever Enterprise access exists now.</p>
</div>
<h2>What official pages say (side by side)</h2>
<table>
<thead><tr><th>Source</th><th>Fetched</th><th>Eligibility wording</th></tr></thead>
<tbody>
<tr><td><a href="https://cursor.com/help/grok-bot/plans">cursor.com/help/grok-bot/plans</a></td><td>2026-09-20</td><td>Grok Bot is included on every paid individual Cursor plan (Pro / Pro+ / Ultra) and on Cursor Teams. You can also link personal SuperGrok, Plus, Heavy, or X Premium+. Lite and SuperGrok Team/Enterprise cannot link. Linking is a usage grant, not a Cursor plan, and cannot be unlinked by you. Cursor Help says a Cursor plan and a SuperGrok / X Premium+ link do not stack.</td></tr>
<tr><td><a href="https://docs.x.ai/grok-bot/faq">docs.x.ai/grok-bot/faq</a></td><td>2026-09-20</td><td>Included with every paid individual Cursor plan and with Cursor Teams; you can link an individual SuperGrok, SuperGrok Plus, or SuperGrok Heavy subscription. The September 4 omission of Pro is gone. Also: if you have both Cursor and SuperGrok, Grok Bot uses the side with more usage. X Premium+ is not named in that FAQ paragraph.</td></tr>
<tr><td><a href="https://docs.x.ai/grok-bot/get-started">Get started</a></td><td>2026-09-20</td><td>Access is included with every paid individual Cursor plan and with the Cursor Teams plan, or through an individual SuperGrok link. The older “Plus / Heavy / Pro+ only” gate is gone on this page.</td></tr>
<tr><td><a href="https://x.ai/news/grok-bot-more-plans">x.ai/news/grok-bot-more-plans</a></td><td>In-article date 2026-08-26</td><td>Grok Bot is now included with SuperGrok, Cursor Pro, and all Cursor Teams plans. Body list includes SuperGrok / Plus / Heavy and Cursor Pro / Pro+ / Ultra plus Teams Standard and Premium.</td></tr>
<tr><td><a href="https://cursor.com/help/grok-bot/supergrok">Link SuperGrok</a></td><td>2026-09-20</td><td>Individual SuperGrok, Plus, Heavy, and X Premium+ grant usage. Team/Enterprise/Lite are ineligible. Linking is permanent.</td></tr>
</tbody>
</table>
<div class="callout"><p><strong>The September 4 Pro-omission conflict is largely resolved.</strong> Help and the FAQ now both include Pro and every other paid individual Cursor plan. Remaining differences: stacking (Help says no; FAQ still says “whichever has more usage”) and whether X Premium+ is named. Trust the page you open. This site does not invent USD list prices.</p></div>
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
<p>MindStudio’s setup piece (2026-08-12) still says “needs Cursor Ultra” — stale relative to current Help and FAQ.</p>
<p>AI Builder Club (updated 2026-08-30) narrates the timeline from launch-day high tiers to the August 21 expansion and August 26 expansion again; its USD figures likewise belong in the original.</p>
<p>If you do not want a managed seat, read <a href="/compare/">Grok Bot alternatives</a>. Those repos are not unofficial clients, and this site does not invent their prices either.</p>
<p>Next: put weekly usage where it matters — <a href="/learn/cost-and-pitfalls/">cost and pitfalls</a>; connectivity or billing oddities — <a href="/troubleshooting/">troubleshooting</a>.</p>
<h2>FAQ</h2>
<div class="faq card">
<details><summary>Is Grok Bot free?</summary><p>There is no consumer free tier and no standalone SKU. Access is bundled with paid Cursor or a linkable SuperGrok / X plan. Enterprise had a separate two-week org trial announced in early September 2026 — that window is expired; treat the news post as dated.</p></details>
<details><summary>Which plan do I need?</summary><p>On fetch day 2026-09-20, Cursor Help and the xAI FAQ both include every paid individual Cursor plan (including Pro) and Cursor Teams. You can also link personal SuperGrok / Plus / Heavy / X Premium+. Open those originals. This site does not invent USD numbers.</p></details>
<details><summary>Does linking SuperGrok create a second bill?</summary><p>No. Linking is a usage grant on the same Cursor account. You cannot unlink it yourself. It does not open a Grok-side meter.</p></details>
</div>
</div></section>
"""


PRICING_FAQS = [
    ("Is Grok Bot free?",
     "There is no consumer free tier and no standalone SKU. Access is bundled with paid Cursor or a linkable SuperGrok / X plan. Enterprise had a separate two-week org trial announced in early September 2026 — that window is expired; treat the news post as dated."),
    ("Which plan do I need?",
     "On fetch day 2026-09-20, Cursor Help and the xAI FAQ both include every paid individual Cursor plan (including Pro) and Cursor Teams. You can also link personal SuperGrok / Plus / Heavy / X Premium+. Open those originals. This site does not invent USD numbers."),
    ("Does linking SuperGrok create a second bill?",
     "No. Linking is a usage grant on the same Cursor account. You cannot unlink it yourself. It does not open a Grok-side meter."),
]
