# -*- coding: utf-8 -*-
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GROUPS = [
    {
        "id": "reach",
        "title": "Can't reach your computer / stuck Reconnecting",
        "symptom": "Chat still works, or you cannot get in at all; messages say Can't reach your computer, Reconnecting, black screen, or blank. The same wording can also appear after a trial or plan ends.",
        "tries": [
            "Fully quit the app (on macOS use menu-bar Quit, not just close the window), then reopen. Official ops guidance starts here for most app issues.",
            "If Retry / Recover computer is offered, take that path first — do not Reset.",
            "Check DNS for *.cursorvm.com. Staff repeatedly point at 1.1.1.1 / 8.8.8.8, and both IPv4 and IPv6 (router RA can keep using ISP DNS). Compare with a phone hotspot on another carrier. Mid-session Reconnecting / Showing saved messages while the Agent Computer is healthy is the same DNS class — Retry, Recover, and Reset do not fix a resolver that cannot look up the computer address.",
            "On Windows, open Settings → Apps → Installed apps. If Grok Bot is installed twice, uninstall the older copy and keep only the latest, then fully quit from the tray and reopen.",
            "New account that never finishes Connecting: save Privacy Mode (not Legacy) on the Cursor dashboard, fully quit Grok Bot, reopen. Until that choice is saved, Retry / Recover / Reset can all fail.",
            "Expired trial or lost plan access can masquerade as Can't reach your computer. Staff: Retry / Recover fail because the account no longer has Grok Bot access — pick a plan that includes it, or link SuperGrok on the same email, then fully quit and reopen. The app should say access ended; the network wording is a known display bug.",
            "Antivirus HTTPS scanning (Kaspersky, ESET, Avast/AVG, Bitdefender, Norton, Trend Micro, Sophos, and similar) can break the app while the browser still works. Grok Bot trusts public CAs only; encrypted-connection scanning swaps the issuer. Turn off Encrypted connections / SSL scanning or exclude Grok Bot, fully quit from the tray, and reopen. A phone hotspot is a useful A/B test when the home network is inspected.",
            "Never install a VPN/proxy or change DNS inside the Agent Computer. A Bot-installed VPN can cut the always-on path so every Bot on the account cannot reconnect until Recover restores routing.",
        ],
        "dont": "A temporarily unreachable computer does not mean Bots are gone. Recover before Reset. If the desktop is black but the same account still works on iOS, do not Reset (that can delete Bots) — wait for an official rebuild. If desktop AND iOS (even on cellular) are both stuck, staff say that is often server-side: hold off on Reset / Recover / Update and signing out. Days of Can't reach after Recover/Reset/reinstall usually mean a stuck hosted box that only staff can restore. When staff say the computer is healthy but your network cannot resolve its address, do not keep Reset / Recover either — a rebuilt computer lands in the same DNS zone your resolver already fails.",
        "more": ("/troubleshooting/cant-reach/", "Walkthrough: can't reach your computer"),
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
            "Update, under Settings → Updates → Grok Bot's Computer: latest computer version. Synced bots, files, and logins stay. Installed apps and packages are removed. A turn that cannot pause is discarded.",
            "Recover computer (the dialog says Recover Grok Bot's Computer): recreates the computer. Same keep/remove split as Update. On a slow update, Keep waiting is the safe default.",
            "Reset: last saved snapshot only. Recent unsynced bots and files can go, and installed apps go too. Official last resort. Do not start a second Reset while one is running.",
        ],
        "dont": "Recover before Reset. Chat history lives outside the box. Exhausted trial does not delete data — Bots stop answering but Computer view can still export; do not Reset to “save” a trial. Stuck on Cleaning up: backend often already finished — fully quit then Recover, do not Reset again. 50% Starting is a server-side bad state; wait a few minutes; Bot data is usually still there. When a status dialog looks scary, do not click yet — try re-login and phone cellular verification first. If every Bot says “Bot failed to respond” or “Couldn't send your message” for hours across devices while the computer screen is still visible, ask support before Reset — Reset rebuilds from the last snapshot and can drop the newest unsynced edits.",
        "more": ("/troubleshooting/recover-vs-reset/", "Walkthrough: Recover, Update, or Reset"),
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
        "title": "Weekly usage / silent bots (computer still visible)",
        "symptom": "Not responding or stopped working while the Agent Computer still opens; meter at 100%; credits or on-demand charges start; dual limit banners; or no usage banner at all.",
        "tries": [
            "Silent bots / not responding with the computer still visible is often weekly usage, not a dead box. Messages may still send as bubbles, but replies never run; iOS and desktop often omit the “usage limit reached” notice. Check Settings → Usage (or the Cursor dashboard) for the meter and weekly reset time before you touch Recover / Reset / Update.",
            "To resume before the weekly reset: enable On-Demand on the same Cursor account and set a spend limit you accept — bots should reply within a couple of minutes. Queued messages sent during the block reply in a batch once usage is available; routines due during the block were skipped.",
            "If you do not want paid spillover: set On-Demand cap to $0. Note this does not stop promo/referral credits from being drained first (charge order: weekly pool → credits → paid On-Demand).",
            "Shrink routine windows; delete idle specialist Bots that poke each other (every Bot↔Bot message counts against weekly usage). Dual banners are usually blocked retries, not double billing.",
        ],
        "dont": "Do not Reset / Recover / Update when every Bot is silent but the computer view still opens — the box is often fine and Reset can wipe data. Do not assume “stay quiet” in chat stops the meter. Do not treat Pro’s Other Models $20 as the Bot weekly pool. Cloud Agents launched by Grok Bot bill Cursor plan usage separately.",
        "more": ("/troubleshooting/not-responding/", "Walkthrough: not responding or stopped working"),
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
        "more": ("/tools/linux-port/", "Linux packages: official versus community"),
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
        "dont": "Free-plan black spinner means no hosted computer was provisioned (no seat) — not your network. Team admin role alone does not grant a computer. Stale sessions after password change show “account unavailable.” New accounts that never saved Privacy Mode (not Legacy) also never finish Connecting — fix that on the Cursor dashboard before Reset.",
        "more": ("/troubleshooting/white-screen/", "Walkthrough: white screen, black screen, empty roster"),
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

def _cards(rows):
    bits = []
    for href, title, note in rows:
        bits.append(
            '<a class="card" href="%s"><h3>%s</h3><p>%s</p></a>'
            % (escape(href, quote=True), escape(title), escape(note))
        )
    return '<div class="grid-3">%s</div>' % "".join(bits)


def troubleshooting():
    intro = '''
<section class="band"><div class="wrap prose">
<p class="kicker">Playbooks</p>
<h1>Grok Bot not working — quit and Retry before you Reset</h1>
<p><strong>Fully quit, then Retry. Do not Reset while the screen says Reconnecting or Could not reach Grok Bot computer.</strong> Cursor Help: bots, files, and logins are safe during reconnect. Cloud work can continue while the desktop app is disconnected.</p>
<p>The two updates are different. Settings, Updates, Check for Updates replaces the app. Update under Grok Bot computer rebuilds the machine. Match the sentence on the screen to one page below. The long steps live on that page, not here.</p>
</div></section>
<section class="band"><div class="wrap">
<h2 id="reach">Can’t reach, DNS, and a phone that will not join</h2><span id="linux"></span>
<p class="lede">Retry first. A resolver that cannot look up cursorvm.com will fail the same way after Reset.</p>
''' + _cards([
        ("/troubleshooting/cant-reach/", "Can’t reach your computer", "Hotspot, antivirus scanning, and the button order before DNS."),
        ("/troubleshooting/dns-error/", "DNS error", "Subdomain lookup refused. Set IPv4 and IPv6, or use another carrier."),
        ("/troubleshooting/stuck/", "Stuck on a label", "Connecting, Setting up, Cleaning up, or 50 percent. If the bar still moves, wait."),
        ("/troubleshooting/phone-not-connecting/", "Phone not connecting", "The phone shares the cloud computer. It does not attach to the laptop."),
        ("/troubleshooting/linux-setup/", "Linux setup failed", "Official deb, rpm, or AppImage. Old 0.18 builds were rejected."),
        ("/troubleshooting/sign-in/", "Sign-in does not complete", "Lost browser popup, Privacy Mode, or an expired Mac session."),
    ]) + '''
<h2 id="white">White screen, install, and uninstall</h2>
<p class="lede">A blank window is not proof the bots were deleted. Hidden Bots and the other device come first.</p>
''' + _cards([
        ("/troubleshooting/white-screen/", "White screen or missing bots", "Local config, sleep, or a fake first-run window. Do not Reset to find chats."),
        ("/troubleshooting/install-failed/", "Install failed on Mac or Windows", "Wrong chip, a second Windows copy, or a free plan with no computer."),
        ("/troubleshooting/uninstall/", "How to uninstall", "Removing the app leaves the Cursor account. Delete Account does not."),
        ("/learn/install/", "Download and install", "Official Mac, Windows, Linux, and phone packages. This site is not the store."),
    ]) + '''
<h2 id="reset">Update, Recover, Reset, and silence</h2><span id="usage"></span>
<p class="lede">Update and Recover keep synced bots and files. Reset can drop unsynced work. None of them refill usage.</p>
''' + _cards([
        ("/troubleshooting/recover-vs-reset/", "Update vs Recover vs Reset", "What each button keeps. Backup not ready means wait."),
        ("/troubleshooting/update-failed/", "Update failed", "App update and computer update are different buttons."),
        ("/troubleshooting/not-responding/", "Not responding", "Computer status first, then a bot waiting on you, then usage."),
        ("/troubleshooting/usage-limit/", "Usage limit", "Weekly pool and On-Demand. No prices on that page."),
        ("/troubleshooting/waiting-for-login/", "Waiting for login", "Take over the computer. Do not paste a password into chat."),
        ("/learn/is-grok-bot-free/", "Is Grok Bot free", "No consumer free tier. The price table stays on Pricing."),
    ]) + '''
<h2 id="oauth">Plugins, routines, files, and the local machine</h2>
<p class="lede">These are not a dead cloud computer. Reset does not repair OAuth, a queue, or the local helper.</p>
''' + _cards([
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth failed", "Gmail, Notion, GitHub, Zoom 4700, Canva, and X."),
        ("/troubleshooting/routine-did-not-run/", "Routine did not run", "Schedule, a paused meter, or a run sitting in the queue."),
        ("/troubleshooting/approval-stuck/", "Approval needed stuck", "A card that timed out, or an Ask first rule."),
        ("/troubleshooting/attachment/", "Attachment cannot be read", "Size, encryption, and waiting for the thumbnail."),
        ("/troubleshooting/local-computer/", "Local computer not connected", "The helper on your machine. Chat can still work."),
        ("/tools/linux-port/", "Linux packages", "Official packages versus the community port."),
    ]) + '''
<p class="lede">Version for support is the account menu, About, Copy version info. Request ID is right-click the message, Copy request ID. Email <a href="mailto:hi@cursor.com">hi@cursor.com</a>. No passwords or keys. One-line staff notes for threads that do not have their own page stay in the list under this index.</p>
</div></section>
'''
    fail_path = ROOT / "src" / "data" / "community-failure-modes.json"
    failures = json.loads(fail_path.read_text(encoding="utf-8"))
    items = []
    for f in failures:
        title = f.get("title") or f.get("name") or f.get("url", "")
        note = f.get("one_line") or f.get("blurb") or ""
        items.append(
            '<li class="source-item"><a href="%s">%s</a><span class="source-note">%s</span></li>'
            % (escape(f["url"], quote=True), escape(title), escape(note))
        )
    registry = (
        '<section class="band"><div class="wrap">'
        '<h2>All failure sources (%d)</h2>'
        '<p class="lede">The cards above are the long pages. This list keeps all %d input sources for edge cases that do not have their own page. Threads are field evidence, not official promises.</p>'
        '<ul class="source-list">%s</ul></div></section>'
    ) % (len(failures), len(failures), "".join(items))
    return intro + registry
