# -*- coding: utf-8 -*-
from html import escape
import json
from pathlib import Path

GROUPS = [
    {
        "id": "reach",
        "title": "Can't reach your computer / stuck Reconnecting",
        "symptom": "Chat still works, or you cannot get in at all; messages say Can't reach your computer, Reconnecting, black screen, or blank.",
        "tries": [
            "Fully quit the app (on macOS use menu-bar Quit, not just close the window), then reopen. Official ops guidance starts here for most app issues.",
            "If Retry / Recover computer is offered, take that path first — do not Reset.",
            "Check DNS for *.cursorvm.com. Staff repeatedly point at 1.1.1.1 / 8.8.8.8, and both IPv4 and IPv6 (router RA can keep using ISP DNS). Compare with a phone hotspot on another carrier.",
        ],
        "dont": "A temporarily unreachable computer does not mean Bots are gone. If the desktop is black but the same account still works on iOS, do not Reset (that can delete Bots) — wait for an official rebuild. Days of Can't reach after Recover/Reset/reinstall usually mean a stuck hosted box that only staff can restore.",
        "sources": [
            ("Official Troubleshooting", "https://docs.x.ai/grok-bot/troubleshooting"),
            ("Reconnect screenshots", "https://forum.cursor.com/t/grok-bot-reconnect-issue/168500"),
            ("createAgent / DNS", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
            ("cursorvm dropped by VPN", "https://forum.cursor.com/t/grok-bot-desktop-on-macos-is-permanently-stuck-on-reconnecting-to-your-computer/169119"),
            ("WARP blank screen", "https://forum.cursor.com/t/blank-screen-after-opening-grok-bot/169966"),
            ("JioFiber IPv6 DNS", "https://forum.cursor.com/t/cant-reach-your-computer-from-last-72-hours/169970"),
            ("Windows ignores system proxy — use TUN", "https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281"),
            ("Zscaler tunnel", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-on-windows-11/170294"),
            ("apex works but subdomain Query refused", "https://forum.cursor.com/t/grok-bot-0-30-0-windows-setup-fails-with-cant-reach-your-computer-all-network-checks-pass/170035"),
        ],
    },
    {
        "id": "reset",
        "title": "Reset vs Recover vs Update",
        "symptom": "You want to “rebuild the computer,” Reset stuck on Cleaning up / 50% Starting, or the Reset dialog opens behind Settings and cannot be clicked.",
        "tries": [
            "Update Agent Computer: new image, durable state kept.",
            "Recover Agent Computer: replace the computer when unreachable, still trying to keep durable state.",
            "Reset Agent Computer: return to the latest durable snapshot; unsynced work may be lost. Official docs call this last resort.",
        ],
        "dont": "Chat history lives outside the box. Exhausted trial does not delete data — Bots stop answering but Computer view can still export; do not Reset to “save” a trial. Stuck on Cleaning up: backend often already finished — fully quit then Recover, do not Reset again. 50% Starting is a server-side bad state; wait a few minutes; Bot data is usually still there. When a status dialog looks scary, do not click yet — try re-login and phone cellular verification first.",
        "sources": [
            ("Official order", "https://docs.x.ai/grok-bot/troubleshooting"),
            ("Recovery guide", "https://cursor.com/help/grok-bot/computer-recovery"),
            ("Trial exhaustion", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
            ("Cleaning up fake hang", "https://forum.cursor.com/t/grok-bot-hanging-at-cleaning-up-phase-after-resetting/169364"),
            ("50% Starting", "https://forum.cursor.com/t/currently-down-grok-bot-retrying-back-end-vm/169834"),
            ("Reset window behind Settings", "https://forum.cursor.com/t/the-reset-computer-window-opens-behind-the-settings-window-and-is-invisible-and-unclickable/169177"),
        ],
    },
    {
        "id": "usage",
        "title": "Weekly usage spills into On-Demand / trial burns instantly",
        "symptom": "Meter at 100%, credits or on-demand charges start, Bot suddenly stops answering, dual limit banners.",
        "tries": [
            "Check Grok Bot weekly usage on the plans screen — not only the Cursor IDE allowance.",
            "If you do not want paid spillover: set On-Demand cap to $0. Note this does not stop promo/referral credits from being drained.",
            "Shrink routine windows; delete idle specialist Bots that poke each other (every Bot↔Bot message counts against weekly usage). Dual banners are usually blocked retries, not double billing.",
        ],
        "dont": "Do not assume “stay quiet” in chat stops the meter. Do not treat Pro’s Other Models $20 as the Bot weekly pool. Cloud Agents launched by Grok Bot bill Cursor plan usage separately.",
        "sources": [
            ("Plans and billing", "https://cursor.com/help/grok-bot/plans"),
            ("No-warning spillover", "https://forum.cursor.com/t/grok-bot-gives-no-warning-before-weekly-usage-spills-into-paid-on-demand/169679"),
            ("Pro separate weekly pool", "https://forum.cursor.com/t/grok-bot-spend-cursor-usage-i-cant-accept-it/169796"),
            ("Draining Cursor credits", "https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982"),
            ("Bot↔Bot reviews burn weekly", "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"),
            ("Trial exhaustion still exportable", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
        ],
    },
    {
        "id": "oauth",
        "title": "Plugin OAuth failures (Zoom / Gmail / Notion / Canva / X / GitHub)",
        "symptom": "Connect spins, Invalid redirect, Connected but tools=0, broken Authorization header.",
        "tries": [
            "Follow Connect plugins: Reopen the auth tab; in Teams ask whether Disabled by team admin.",
            "Notion: use Re-authenticate, not Connect again.",
            "Broken GitHub header: long-press account → Remove → sign in again. Canva fails on iOS: connect from desktop; it syncs to phone. When the Gmail plugin is broken, authorize Gmail from Cursor (shared connection).",
        ],
        "dont": "Zoom 4700 has no user-side workaround (localhost callback rejected) — do not keep editing Zoom app config. Do not paste bearer tokens into chat. X login risk controls on the cloud computer are a known phenomenon, not proof your account is “broken.”",
        "sources": [
            ("Connect plugins / Zoom 4700", "https://cursor.com/help/grok-bot/connect-plugins"),
            ("Notion redirect", "https://forum.cursor.com/t/grok-bot-notion-plugin-oauth-invalid-redirect-uri/169234"),
            ("Gmail plugin", "https://forum.cursor.com/t/grok-bot-unable-to-authenticate-via-gmail-plugin/169782"),
            ("Gmail attachments metadata only", "https://forum.cursor.com/t/grok-bot-gmail-connector-can-list-attachments-but-cannot-download-their-bytes/169261"),
            ("Canva iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
            ("X plugin", "https://forum.cursor.com/t/official-x-plugin-auth-is-broken-on-cursor-cloud-grok-bot-and-desktop-refresh/169592"),
            ("GitHub header", "https://forum.cursor.com/t/grokbot-and-github/170137"),
            ("X login lock", "https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541"),
        ],
    },
    {
        "id": "linux",
        "title": "Linux / local execution / official vs community packages",
        "symptom": "Linux desktop cannot connect, ListMachines empty, local-exec drops, Always allow still blocks ExternalShell.",
        "tries": [
            "Confirm you installed the official deb/rpm/AppImage from x.ai/bot. Very old unofficial 0.18 builds were rejected; staff once said Grok Bot was not formally on Linux — as of the FAQ fetch day, Linux is listed as an official platform.",
            "Local execution: Settings → Execution on Local Computer. Always Allow lives only on that desktop; iOS can only approve one-shot. Linux 0.30.0 empty ListMachines is a known defect; unlock gnome-keyring/KWallet, kill leftover processes, reopen.",
            "Mac chat works but local shows offline: fully quit. Windows leftover local-exec-daemon: quit from tray, end Grok Bot and daemon in Task Manager, wait about a minute, re-register.",
        ],
        "dont": "Do not treat community AUR/COPR/Wine ports as official support. Local stdio MCP is unreachable from the cloud computer. Always allow is not forever-allow.",
        "sources": [
            ("Official Linux install", "https://docs.x.ai/grok-bot/get-started"),
            ("Local MCP unsupported", "https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182"),
            ("Arch request thread", "https://forum.cursor.com/t/native-grok-bot-desktop-app-for-arch-linux-and-linux-generally/168084"),
            ("Linux 0.18 rejected", "https://forum.cursor.com/t/grok-bot-couldnt-finish-setup/170010"),
            ("Linux local exec", "https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157"),
            ("ExternalShell still blocked", "https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180"),
            ("iOS cannot Always allow", "https://forum.cursor.com/t/authorization-death-by-1000-clicks/170087"),
        ],
    },
    {
        "id": "white",
        "title": "White screen / black screen / empty roster (usually not a deleted box)",
        "symptom": "Opens to white, black spinner after install, empty roster after reconnect.",
        "tries": [
            "Fresh install white window: fully quit, rename ~/Library/Application Support/Grok Bot to Grok Bot.bak, relaunch. Reinstall alone does not clear local config.",
            "Empty roster + black/white loading: Agent Computer waking from sleep is slow — nothing was deleted. Do not Reset; wait for the box, fully quit, open again.",
            "Looks like a new user after rebuild: logging in while the computer is still starting shows first-run UI. Fully quit. Do not create a “first Bot” in that window.",
        ],
        "dont": "Free-plan black spinner means no hosted computer was provisioned (no seat) — not your network. Team admin role alone does not grant a computer. Stale sessions after password change show “account unavailable.”",
        "sources": [
            ("Local config white screen", "https://forum.cursor.com/t/grok-bot-shows-white-screen-upon-opening-and-is-unusable/169815"),
            ("Empty roster sleep", "https://forum.cursor.com/t/grok-bot-bug-report/170104"),
            ("Empty workspace after rebuild", "https://forum.cursor.com/t/bots-workspace-missing-all-things-getting-new-user-experience/169448"),
            ("Free plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
            ("Admin without seat", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-during-initial-setup-on-mac/170251"),
            ("Stale session after password change", "https://forum.cursor.com/t/grok-bot-mac-blocked-after-password-change-app-says-unavailable-spending-shows-supergrok-plus/170389"),
        ],
    },
]

def troubleshooting():
    blocks = []
    for g in GROUPS:
        lis = "".join("<li>%s</li>" % escape(t) for t in g["tries"])
        src = "".join('<li><a href="%s">%s</a></li>' % (escape(u), escape(n)) for n, u in g["sources"])
        blocks.append(
            '<article class="card" id="%s"><h2>%s</h2><p><strong>Symptom.</strong> %s</p><h3>Try first</h3><ol>%s</ol><div class="callout warn"><p><strong>When not to Reset.</strong> %s</p></div><h3>Sources</h3><ul>%s</ul></article>'
            % (g["id"], escape(g["title"]), escape(g["symptom"]), lis, escape(g["dont"]), src)
        )
    intro = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Playbooks</p>
<h1>Grok Bot not working — fixes by symptom</h1>
<p>Official guidance starts with the least destructive step. Cloud work can continue while the desktop is disconnected. Below groups <a href="https://docs.x.ai/grok-bot/troubleshooting">official troubleshooting</a>, the <a href="https://cursor.com/help/grok-bot/getting-started">Cursor getting-started table</a>, and staff posts from awesome “Community &amp; Failure Modes” by symptom — without restating all eighty-nine threads one by one.</p>
<p>Before contacting support, collect: Grok Bot version, OS, exact error, Bot or routine name, time and timezone, request/conversation ID, and what you already tried (Retry / restart / Update). Do not attach passwords, codes, or keys. Email <a href="mailto:hi@cursor.com">hi@cursor.com</a>.</p>
</div></section>
<section class="band"><div class="wrap" style="display:flex;flex-direction:column;gap:16px">
'''
    failures = json.loads(Path("/workspace/playbook-data/failures.json").read_text(encoding="utf-8"))
    items = []
    for f in failures:
        items.append(
            '<li class="source-item"><a href="%s">%s</a><span class="source-note">%s</span></li>'
            % (escape(f["url"], quote=True), escape(f["title"]), escape(f.get("one_line", "")))
        )
    registry = (
        '</div></section><section class="band"><div class="wrap">'
        '<h2>All failure sources (%d)</h2>'
        '<p class="lede">The playbooks above group common symptoms; below keeps all %d input sources for edge cases not expanded separately. Threads are field evidence, not official promises.</p>'
        '<ul class="source-list">%s</ul></div></section>'
    ) % (len(failures), len(failures), "".join(items))
    return intro + "".join(blocks) + registry
