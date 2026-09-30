# -*- coding: utf-8 -*-
"""Per-error and explainer pages.

Facts are limited to official troubleshooting and Cursor Help (re-read for
this pass), plus staff notes already in the handbook snapshots. No new
product behavior, price, or menu path is introduced here.
"""
from html import escape

DOC_TROUBLE = "https://docs.x.ai/grok-bot/troubleshooting"
DOC_START = "https://docs.x.ai/grok-bot/get-started"
CURSOR_RECOVER = "https://cursor.com/help/grok-bot/computer-recovery"
CURSOR_PLANS = "https://cursor.com/help/grok-bot/plans"
CURSOR_PLUGINS = "https://cursor.com/help/grok-bot/connect-plugins"
CURSOR_DELETE = "https://cursor.com/help/grok-bot/delete-account"
STORE = "https://x.ai/bot"


def _faq_html(faqs):
    bits = ['<h2>FAQ</h2><div class="faq card">']
    for q, a in faqs:
        bits.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    bits.append("</div>")
    return "".join(bits)


def _related(items):
    lis = []
    for href, label, note in items:
        lis.append(
            "<li><a href=\"%s\">%s</a> — %s</li>"
            % (escape(href, quote=True), escape(label), escape(note))
        )
    return "<h2>Related</h2><ul>%s</ul>" % "".join(lis)


def _sources(pairs):
    lis = "".join(
        '<li><a href="%s">%s</a></li>' % (escape(url, quote=True), escape(name))
        for name, url in pairs
    )
    return "<h2>Sources</h2><ul>%s</ul>" % lis


def _render(kicker, h1, answer, cta_href, cta_label, rest, faqs, related, sources):
    return (
        '<section class="band"><div class="wrap prose">'
        '<p class="kicker">%s</p><h1>%s</h1>%s'
        '<div class="cta-row"><a class="btn btn-primary" href="%s">%s</a></div>'
        "%s%s%s%s</div></section>"
        % (
            escape(kicker),
            escape(h1),
            answer,
            escape(cta_href, quote=True),
            escape(cta_label),
            rest,
            _faq_html(faqs),
            _related(related),
            _sources(sources),
        )
    ), faqs


def plugin_oauth():
    answer = '''
<p>Grok Bot plugin OAuth failed when the browser tab never finishes, or the plugin says Connected and still exposes no tools. Reopen the authorization tab and finish it with the account you meant. Do not paste a bearer token into chat.</p>
<p>Connectors are stored on the Cursor account, not on one Bot. A second click on Connect often stacks a new attempt on a login that is already half saved.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is Connect again, then Reset the computer when the spinner survives. Reset rebuilds the hosted machine. It does not clear an OAuth record. Notion is the documented case: staff say the sign-in lives on the account, so retrying Connect fails, and Re-authenticate is the control that clears it. Zoom error 4700 is not a setting you own. The catalog plugin hard-codes the callback as http://localhost:8787/callback. Zoom rejects the hostname localhost. Official Help says there is no user workaround until that redirect moves off localhost. Editing a Zoom app in your own developer console does not change the catalog callback.</p>
<p>A team admin can also turn marketplace plugins off. The label is Disabled by team admin. That is policy, not a bad redirect, and another Connect click will not override it.</p>
<h2>Steps</h2>
<ol>
<li>Open Marketplace from the sidebar, then Your plugins, and confirm the plugin is under Installed. On the phone, tap the top-left avatar, then Plugins. Official troubleshooting starts here.</li>
<li>Reopen the plugin detail and choose the authentication action. If the app says Waiting for authorization, use Reopen so the browser tab comes back. Keep Grok Bot open while the browser finishes.</li>
<li>Complete the browser prompt with the intended account. Return to Grok Bot and retry the task. If the source service revoked access, remove the plugin and connect it again.</li>
<li>Check whether the connector wants an organization variable or an administrator setting. A finished OAuth screen can still leave the tool dark when that value is missing.</li>
<li>Notion Invalid redirect_uri: use Re-authenticate, not Connect again.</li>
<li>Gmail: staff say the Grok Bot plugin OAuth path is broken. Authorize Gmail from Cursor. That path is different, and the connection is shared into Grok Bot until the plugin is fixed.</li>
<li>GitHub that shows Connected but fails with Authorization header is badly formatted: press and hold the account, choose Remove, then sign in again. That is the staff workaround for a tracked bug.</li>
<li>Canva Invalid redirect URI on iPhone: staff call it an app-link versus web-redirect mismatch, not your Canva settings. Connect Canva from desktop Grok Bot on the same account. The connector syncs to the phone.</li>
<li>Official X plugin: staff say connect and refresh fail across the Cursor desktop, Cloud Agents, and Grok Bot, including Connected with tools equal to zero. There is no clean workaround in that note while X-side app configuration is fixed. X login risk controls on the cloud computer are a separate, known phenomenon. They are not proof the Cursor account is broken.</li>
</ol>
<h2>Limits</h2>
<p>The Gmail connector can list attachment metadata and still have no tool that downloads the bytes. Staff say to use the cloud browser or park the file in Drive. Drive itself is file-level. Editing a Google Doc body or Sheet cells is the separate Docs or Sheets connector, added from the marketplace on the same Google account.</p>
<p>The Phantom plugin runs on its own MCP server. Staff say each new authorization creates a separate dedicated agent wallet, not your personal Phantom wallet. A reconnect can show a new address while funds stay on the old agent wallet. Recover that from chat history or through Phantom support. Connecting again on purpose to “get the old address back” creates another wallet.</p>
<p>There is no settings form for a custom connector. Tell the Bot in chat to add an MCP server that is public HTTPS, streamable HTTP or SSE, confirm the details, and the tools show up on the next message. An MCP that only listens on localhost on your PC is unreachable from the cloud computer. Local stdio MCP is the same refusal.</p>
<p>Zoom 4700 and the broken X plugin are waiting on the vendor side. This page will not invent a redirect host or a header format for you to paste. Secrets belong on the official secrets card, masked, out of the transcript.</p>
'''
    faqs = [
        ("The plugin says Connected. Why are there no tools?",
         "Connected only means an auth record exists. Staff have seen the official X plugin report Connected with zero tools, and GitHub report Connected with a badly formatted Authorization header. Remove and sign in again for GitHub. X has no clean workaround in the staff note."),
        ("Should I Reset the computer because Gmail will not connect?",
         "No. Reset changes the computer. Gmail staff guidance is to authorize Gmail from Cursor so the shared connection is available to Grok Bot. Reset will not repair that OAuth path."),
        ("Can I fix Zoom error 4700 in my own Zoom app?",
         "No. Official Help says the catalog callback is hardcoded to localhost and Zoom rejects it. There is no user-side workaround until the redirect changes."),
        ("Canva works on my Mac and fails on my iPhone. Which settings do I change?",
         "None on the Canva side, according to staff. Connect Canva once from desktop Grok Bot on the same Cursor account. The connector then syncs to the phone."),
        ("Are plugins private to one Bot?",
         "No. Installed connectors are account-level. Authorizing GitHub for one Bot leaves it available to later Bots on that account."),
    ]
    related = [
        ("/learn/plugins/", "Plugins and MCP", "Connectors before the browser, and remote MCP only."),
        ("/troubleshooting/", "Not working index", "Pick a different screen if this is not an OAuth failure."),
        ("/troubleshooting/attachment/", "Attachment cannot be read", "File caps in chat, separate from the Gmail byte limit."),
        ("/learn/computer/", "Shared computer", "Logins on the computer are visible to every Bot."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Connect plugins", CURSOR_PLUGINS),
        ("Notion redirect", "https://forum.cursor.com/t/grok-bot-notion-plugin-oauth-invalid-redirect-uri/169234"),
        ("Gmail plugin", "https://forum.cursor.com/t/grok-bot-unable-to-authenticate-via-gmail-plugin/169782"),
        ("Gmail attachment bytes", "https://forum.cursor.com/t/grok-bot-gmail-connector-can-list-attachments-but-cannot-download-their-bytes/169261"),
        ("GitHub header", "https://forum.cursor.com/t/grokbot-and-github/170137"),
        ("Canva on iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
        ("X plugin", "https://forum.cursor.com/t/official-x-plugin-auth-is-broken-on-cursor-cloud-grok-bot-and-desktop-refresh/169592"),
    ]
    return _render(
        "Plugins",
        "Grok Bot plugin OAuth failed",
        answer,
        "/learn/plugins/?utm_source=guide&utm_campaign=plugin-oauth",
        "Plugins lesson: connectors before the browser",
        rest, faqs, related, sources,
    )


def usage_limit():
    answer = '''
<p>A Grok Bot usage limit is a full weekly pool on the Cursor account. If the computer view still opens and every bot is silent, read Usage before you touch Recover or Reset.</p>
<p>The desktop app and the iPhone app often skip the sentence that usage is exhausted. A missing banner does not mean the meter has room.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>Reset, Recover, and Update change the computer. They do not refill a weekly pool. People press them because the chat looks dead: your message still appears as a bubble, and no reply runs. That split, computer visible and bots silent, is the usage case in the staff billing notes. A full meter that you clear by rebuilding the machine comes back on the same account an hour later, with unsynced work missing.</p>
<p>On-Demand can start with no in-app warning. The spend order staff describe is the Grok Bot weekly pool, then promo or referral credits, then paid On-Demand. A zero On-Demand cap stops the paid tier. It does not stop those credits from being drained first. Dual banners, when they show up, are blocked retries, not two bills.</p>
<h2>Steps</h2>
<ol>
<li>Open the computer view. If the screen says Reconnecting or Could not reach Grok Bot computer, stop. That bot cannot finish a turn until the computer is back. Use the can&apos;t-reach page. This page is only for a computer that actually opens.</li>
<li>Open Settings, then Usage, in the app, or the usage screen on the Cursor dashboard. Read the meter and the weekly reset time. Pro&apos;s Other Models allowance is a different pool. It is not the Grok Bot weekly pool. Cloud Agents that a bot launches bill Cursor plan usage separately. The IDE chart can look fine while the bot pool is empty.</li>
<li>If the meter is full and you can wait, wait for the reset time on that screen. Messages you already sent during the block reply in a batch once usage is available. Routines that came due during the block were skipped. They do not queue up and fire later as a surprise set of sends.</li>
<li>If you need replies before the reset, enable On-Demand on the same Cursor account and set a spend limit you accept. Staff say bots should reply within a couple of minutes. The chat may not warn you before paid spillover starts. Dollar amounts and plan names belong on the pricing page, not here.</li>
<li>If you do not want paid spillover, set the On-Demand cap to zero. Then still assume credits can move. Pause heavy work as the weekly meter nears the top if a credit drain is also unacceptable.</li>
<li>Shrink routine windows. Delete idle specialist bots that message each other. Every bot-to-bot message spends a weekly turn, including review threads you asked them to stop. Saying stay quiet in chat is only a hint. Staff describe a sturdier pattern: one Command Agent with subagents that finish and stop, and deletion of unused specialists. Deleting a bot also clears that bot&apos;s chat, so save anything you need first.</li>
</ol>
<h2>Limits</h2>
<p>If the meter is not full, silence is not this page. Fully quit and reopen. A single connector that hangs while the rest of the roster answers is the plugin page. If every bot says Bot failed to respond, or Could not send your message, for hours on the phone and the desktop while the computer is still visible, ask Cursor support before Reset. Reset rebuilds from the last snapshot and can drop the newest unsynced edits. One staff thread also separates an overbooked notice followed by Bot failed to respond: they called that service-side model load, not your meter and not your computer. This handbook does not have a model picker to document, and it will not invent one. Wait, or write support with the version and the request id.</p>
<p>An exhausted trial does not delete data. Bots stop answering. The computer view can still export. Do not Reset to save a trial. Expired access can also wear the Can&apos;t reach label even though the cause is the plan. The pricing page is the eligibility snapshot. This page does not state a price.</p>
'''
    faqs = [
        ("The app never said I hit a limit. Can the meter still be full?",
         "Yes. iOS and desktop often omit the usage notice. The Cursor usage screen is the check. Absence of a banner proves nothing."),
        ("Does a zero On-Demand cap freeze every charge?",
         "It stops paid On-Demand. Staff say it does not stop promo or referral credits, which are spent after the weekly pool and before paid On-Demand."),
        ("Will installing the iPhone app give me a second pool?",
         "No. macOS and iOS share one weekly bucket on the same Cursor account."),
        ("I told the bots to stay quiet. Why did the meter still move?",
         "Staff say that sentence is only a hint. Bot-to-bot messages and routines still spend turns. Delete unused specialist bots after you save chats you need."),
        ("Where are the plan prices?",
         "On the pricing page, which links to the official sources. This page explains the meter only."),
    ]
    related = [
        ("/learn/cost-and-pitfalls/", "Usage and On-Demand", "The longer pitfalls lesson. Prices stay off that page too."),
        ("/pricing/", "Pricing snapshot", "Whether the account includes Grok Bot. No invented dollar amounts."),
        ("/troubleshooting/not-responding/", "Not responding", "Computer status first, then this meter."),
        ("/troubleshooting/", "Not working index", "Other screens that look like silence."),
    ]
    sources = [
        ("Plans and billing", CURSOR_PLANS),
        ("Official troubleshooting", DOC_TROUBLE),
        ("No warning before On-Demand", "https://forum.cursor.com/t/grok-bot-gives-no-warning-before-weekly-usage-spills-into-paid-on-demand/169679"),
        ("Bot-to-bot reviews", "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"),
        ("Trial still exportable", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
    ]
    return _render(
        "Usage",
        "Grok Bot usage limit",
        answer,
        "/learn/cost-and-pitfalls/?utm_source=guide&utm_campaign=usage-limit",
        "How weekly usage and On-Demand work",
        rest, faqs, related, sources,
    )


def dns_error():
    answer = '''
<p>A Grok Bot DNS error means your resolver cannot look up the computer hostname under cursorvm.com. The apex name can answer while every subdomain returns Query refused.</p>
<p>Retry, Recover, and Reset do not teach that resolver a name. A rebuilt computer is another hostname in the same zone.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to rebuild the computer because the sentence says it cannot be reached. Staff have answered threads where the cloud computer was healthy the whole time. The Mac never finished reconnecting because traffic to cursorvm.com was dropped, or because the subdomain lookup was refused. Reset allocates a new name your resolver still cannot resolve. You then spend the evening on Cleaning up for a network fault.</p>
<p>The same on-screen sentence is also a known display bug when a trial or plan has ended. If Retry and Recover fail because the account no longer includes Grok Bot, DNS changes will not help. The pricing page is that check. Do not burn an evening on a public resolver for a billing problem.</p>
<h2>Steps</h2>
<ol>
<li>Fully quit Grok Bot and reopen it. On a Mac that is menu-bar Quit, not closing the window. On Windows, quit from the tray. Then choose Retry if it is offered. Do this before you edit DNS, so a stuck process is not what you are measuring.</li>
<li>Join a phone hotspot on another carrier and open Grok Bot from the computer. If the hotspot works, the home or office path is the fault. Stop resetting the computer. If the hotspot fails and the phone app on cellular also fails, treat it as server-side and slow down. Desktop and iOS both stuck, with the phone off your Wi-Fi, is the case staff often tell people not to Reset, Recover, Update, or sign out of.</li>
<li>Look up a hostname under cursorvm.com, not the apex. The app connects to a per-computer subdomain. Staff have used names of the shape test123 under a region host such as us8 or us10. Read the Server line in the lookup so you see which resolver actually answered. Apex success plus Query refused on the subdomain is this bug.</li>
<li>Staff point at 1.1.1.1 and 8.8.8.8 for IPv4. On IPv6, a router advertisement can keep handing out the ISP resolver after you change only IPv4, so the new IPv4 servers never get the query. The thread that cleared a multi-day failure set IPv6 DNS as well, using 2606:4700:4700::1111, then fully quit and reopened the app.</li>
<li>On Windows the app ignores the system HTTP proxy and connects directly. Browser checks that travel through a proxy can pass while Grok Bot fails. Staff&apos;s probe, after a TUN-mode tunnel is on, is a direct request that skips the proxy to a test hostname under cursorvm.com. A fast 404 whose server banner is awselb/2.0 means the direct path works. The hostname is only a probe. A hang means the app will fail too. Region in that report was us10, not us8. Do not install that tunnel inside the Agent Computer.</li>
</ol>
<h2>Limits</h2>
<p>Never change DNS, or install a VPN or proxy, inside the Agent Computer. A bot that installs a VPN can cut the always-on path so every bot on the account fails until Recover restores routing. That is a different outage from the one on your laptop resolver, and Recover is the routing restore, not a casual Reset.</p>
<p>Antivirus products that scan HTTPS, Cloudflare WARP, and a Zscaler-style tunnel can blank the screen while DNS is fine. WARP can intercept the computer even on a hotspot. Zscaler can keep tunneling on a hotspot; staff have told people to quit Grok Bot, pause Zscaler, and ask IT to allowlist both *.cursorvm.com and **.cursorvm.com. Those are path blocks. Use them when the lookup itself succeeds. The can&apos;t-reach page is the full order, including the button sequence before any resolver edit.</p>
<p>Days of Can&apos;t reach after you have already recovered, reset, and reinstalled usually mean a stuck hosted box that only staff can restore. Email hi@cursor.com. Another public DNS server will not shorten that queue.</p>
'''
    faqs = [
        ("The website cursorvm.com opens. Why does Grok Bot still fail?",
         "The app does not use the apex. It uses a per-computer subdomain. The apex can resolve while the subdomain returns Query refused."),
        ("I set 1.1.1.1 and nothing changed. What did staff add?",
         "IPv6. Router advertisements can keep the ISP resolver. Set IPv6 DNS as well, then fully quit and reopen. One fixed thread used 2606:4700:4700::1111."),
        ("Will Reset give me a computer on a DNS name that works?",
         "No. The replacement is in the same zone. If staff have said the computer is healthy, do not Reset or Recover. Fix the resolver or move to a hotspot."),
        ("My phone on cellular works and the desktop does not. Is that DNS?",
         "It is your desktop path, which includes DNS. The bots were not deleted. Do not Reset. Prefer a hotspot test, then Recover or Update only if the computer is actually unreachable after the network is fixed."),
        ("Should I change DNS inside the Agent Computer?",
         "No. Staff warn that a VPN or DNS change inside the computer can knock every bot offline until Recover restores routing."),
    ]
    related = [
        ("/troubleshooting/cant-reach/", "Can&apos;t reach your computer", "Button order, hotspot, antivirus, and VPN, around this resolver check."),
        ("/troubleshooting/stuck/", "Stuck on a label", "Connecting and Setting up, when the words are not a DNS refusal."),
        ("/pricing/", "Pricing", "When the same sentence is an ended plan, not a resolver."),
        ("/troubleshooting/", "Not working index", "Every other screen."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Query refused on the subdomain", "https://forum.cursor.com/t/grok-bot-0-30-0-windows-setup-fails-with-cant-reach-your-computer-all-network-checks-pass/170035"),
        ("IPv6 DNS", "https://forum.cursor.com/t/cant-reach-your-computer-from-last-72-hours/169970"),
        ("VPN drops cursorvm", "https://forum.cursor.com/t/grok-bot-desktop-on-macos-is-permanently-stuck-on-reconnecting-to-your-computer/169119"),
        ("Windows ignores the system proxy", "https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281"),
        ("Zscaler", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-on-windows-11/170294"),
    ]
    return _render(
        "Network",
        "Grok Bot DNS error",
        answer,
        "/troubleshooting/cant-reach/?utm_source=guide&utm_campaign=dns-error",
        "Full can&apos;t-reach order, after this resolver check",
        rest, faqs, related, sources,
    )


def install_failed():
    answer = '''
<p>Grok Bot install failed on a Mac is usually the wrong chip package. On Windows it is usually a second installed copy, or a direct connection the proxy never sees. Downloading the same file again does not fix either one.</p>
<p>A free Cursor plan can also spin forever on Setting up, because no hosted computer was provisioned. That is not a corrupt installer.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to run the installer again. The top Download for macOS button on x.ai/bot is the Apple silicon build. Cursor staff confirmed that. An Intel Mac that takes it gets an app macOS calls unsupported, and the next click downloads the same file. Intel is under More downloads. About This Mac: Chip means Apple silicon, Processor means Intel.</p>
<p>Reinstall also leaves the local config folder in place. A white window after a fresh Mac install is that folder, not the dmg. Fully quit, rename ~/Library/Application Support/Grok Bot to Grok Bot.bak, and relaunch. The Windows twin is %APPDATA%\\Grok Bot. Reinstall alone will not clear it.</p>
<h2>Steps</h2>
<ol>
<li>Confirm the file came from x.ai/bot, the App Store listing, or Google Play package ai.x.grok.bot. This site does not host the binary. A repackaged installer is out of scope here.</li>
<li>Mac: match the chip, open the dmg, drag Grok Bot to Applications, eject the image, and open the app from Applications. If macOS asks, choose Open. If there is no Open button, System Settings, Privacy and Security, Open Anyway, then launch from Applications again. Do not keep launching the copy inside the mounted image.</li>
<li>Windows: match Settings, System, About, System type, x64 or Arm64. If Installed apps lists Grok Bot twice, uninstall the older copy, keep the latest, quit from the system tray, and open one copy. Closing the window leaves the process up.</li>
<li>Windows that ends on Can&apos;t reach your computer after a clean profile: the app connects directly and ignores the system HTTP proxy. A browser test through the proxy can pass while the app fails. The DNS page has the direct-connection probe. Do not install a VPN inside the Agent Computer.</li>
<li>White flash, then the Windows process closes: staff said the cloud computer was healthy. The usual causes they named are local: endpoint security, a locked %APPDATA% folder, or a partial install. They said it is not the GPU. Quit security overlays long enough to test, fix the local folder, and install a single official copy. Do not Reset a computer the phone can still open.</li>
<li>New account stuck on Connecting: save Privacy Mode, not Legacy, on the Cursor dashboard, fully quit, and reopen. Until that choice is saved, Retry, Recover, Reset, and another installer all fail.</li>
<li>Endless Setting up, or a black spinner, on a free Cursor plan: no hosted computer exists. A team admin role is not a seat either. Assign a Standard or Premium seat, or sign in with an account that has one, then fully quit and reopen. Network tests are noise until a seat exists.</li>
</ol>
<h2>Limits</h2>
<p>Linux failures are a different page. Very old unofficial 0.18 builds were rejected. Current official Linux packages are deb, rpm, and AppImage under More downloads. A community port is not a fix for a bad Mac chip.</p>
<p>If the installer finished and the only problem is a silent bot with the computer visible, that is usage, not a bad package. If the words are Can&apos;t reach and a hotspot on another carrier works, that is DNS or a tunnel, not the exe. Gatekeeper prompts are macOS confirming a downloaded app, not a Grok Bot error code. This page does not publish a minimum macOS version, because the xAI Get started page we use does not state one.</p>
'''
    faqs = [
        ("macOS says the app is not supported. Is Grok Bot unavailable on Mac?",
         "Usually you opened the Apple silicon package on an Intel Mac, or a file that did not come from x.ai/bot. Intel is under More downloads. Both chips are official."),
        ("I reinstalled and the window is still white. What is left?",
         "The local config folder. Fully quit, rename Application Support/Grok Bot on a Mac or %APPDATA%\\Grok Bot on Windows to a .bak name, and relaunch. Reinstall does not do that."),
        ("Windows lists Grok Bot twice. Which one do I keep?",
         "Uninstall the older copy from Settings, Apps, Installed apps. Quit the tray. Open the remaining copy once."),
        ("Setting up never ends and I am on the free Cursor plan. Will a new download help?",
         "No. Staff say no hosted computer is provisioned without a paid seat or a linked plan that includes Grok Bot. The spinner instead of an access message is a known display bug."),
        ("The app flashed white and quit on Windows. Should I Reset?",
         "Not from that symptom. Staff said the cloud computer was healthy and the crash was local: endpoint security, a locked application-data folder, or a partial install."),
    ]
    related = [
        ("/learn/install/", "Install and sign in", "Official packages and the Cursor login."),
        ("/learn/mac-download/", "Mac download", "Apple silicon versus Intel, in one place."),
        ("/learn/windows-download/", "Windows download", "One copy, tray quit, and the direct connection."),
        ("/troubleshooting/white-screen/", "White or black screen", "When the package is fine and the window is not."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("Official troubleshooting", DOC_TROUBLE),
        ("White screen is local config", "https://forum.cursor.com/t/grok-bot-shows-white-screen-upon-opening-and-is-unusable/169815"),
        ("Windows white flash then close", "https://forum.cursor.com/t/grok-bot-0-24-0-windows-10-x64-white-screen-flashes-then-app-closes/169380"),
        ("Free plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
        ("Admin without a seat", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-during-initial-setup-on-mac/170251"),
    ]
    return _render(
        "Install",
        "Grok Bot install failed on Mac or Windows",
        answer,
        "/learn/install/?utm_source=guide&utm_campaign=install-failed",
        "Official install steps",
        rest, faqs, related, sources,
    )


def update_failed():
    answer = '''
<p>Grok Bot update failed on one of two different buttons. Settings, Updates, Check for Updates, then Restart to Update, replaces the desktop app and does not reset the cloud computer.</p>
<p>Update under Grok Bot&apos;s Computer rebuilds that machine. On a slow update, Keep waiting is the safe default. Backup not ready means wait, not Reset.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to press Reset because the update sits still, or because the dialog says Backup not ready or Agent busy. Official computer recovery says the opposite. Backup not ready means the computer&apos;s data is not safely backed up yet. Grok Bot offers the update again after the backup finishes. Reset to force it can drop unsynced bots and files. Agent busy means a bot could not pause in time, so the computer was not updated. Let that bot finish, then update again.</p>
<p>Do not start a second Update or Reset while one is already running. Repeated resets can interrupt a restore that is still finishing. If Recover or Reset fails, use Retry Recovery or Retry Reset once, then stop and contact support.</p>
<h2>Steps</h2>
<ol>
<li>Decide which update you started. The app update is Check for Updates and Restart to Update. The computer update is Update under Grok Bot&apos;s Computer in the same Settings, Updates section. On iPhone and Android the computer controls are Update Computer and Reset Computer under Settings, Bot, Bot Computer.</li>
<li>If the label still changes, or it says Update still running, leave it. An update can take several minutes while a large image downloads or data transfers. Reconnecting and Recover usually take a few minutes. Continue in Background is allowed. Choose Recover only if the update looks stuck and the app offers Recover computer. If recovery is not offered, keep waiting.</li>
<li>Update and Recover keep synced bots, files, and logins. Both remove installed apps and packages on the computer. A turn that cannot pause is discarded. Reset is the only one that can also drop recent bots and files that have not synced. Chat history lives outside the computer, so an update is not how you protect chats, and it is not how you delete them either.</li>
<li>After the computer comes back, apt packages, daemons, and other installed software are gone even when /workspace files survived. Keep a package list in a file and ask the Bot to reinstall. Idle machines also sleep, and background processes die. That is expected after an image rebuild, not a second failure of the update button.</li>
<li>WhatsApp linked-device state is an exception staff called out. A computer refresh keeps /workspace, the browser profile, and ~/.config. It does not keep ~/.local/state, so a WhatsApp linked-device session can vanish. Plan to link that device again. Do not treat the missing session as proof the whole computer reset itself.</li>
<li>Can&apos;t reach plus failed Recover and Reset, right after an update, is sometimes a lost app login rather than a dead machine. Staff said bots, files, and logins live on the remote computer, and Recover or Reset need a working session. Fully quit, sign out and sign in, or reinstall the app and sign in. Then retry the computer control once.</li>
</ol>
<h2>Limits</h2>
<p>If the computer view is up and bots are only silent, do not update or reset to refill usage. If the phone on the same account still works and the desktop is black, do not Reset. If both devices fail, including cellular, wait before another computer button. Days of failure after Update, Recover, and Reset already ran are a staff restore, not a third click.</p>
<p>Cleaning up that never ends after a Reset often means the backend finished and the dialog missed the signal. Fully quit, reopen, and Recover if the computer is still down. Do not launch a second Reset to finish the first. Stopped at 50 percent Starting is a server-side bad state. Wait a few minutes. Bot data is usually still there.</p>
'''
    faqs = [
        ("Does Restart to Update wipe my bots?",
         "No. That control updates the desktop app. Updating the desktop app does not reset the cloud computer. The computer control is the separate Update under Grok Bot computer."),
        ("The dialog says Backup not ready. What do I click?",
         "Nothing destructive. Wait until the update is offered again. Do not Reset to force a backup that has not finished."),
        ("It says Agent busy. Is the update broken?",
         "A bot could not pause. Let it finish, then update again. Do not stack a second update on top."),
        ("My packages disappeared after a successful update. Is that a bug in the button?",
         "Staff say Update keeps files and logins and rebuilds the OS image, so apt packages, apps, and daemons are removed. Keep a list in a file and reinstall."),
        ("Recover and Reset both failed after the update. What did staff try first?",
         "A fresh login. Fully quit, sign out and back in, because those computer buttons need a working app session."),
    ]
    related = [
        ("/troubleshooting/recover-vs-reset/", "Update versus Recover versus Reset", "What each control keeps and removes."),
        ("/learn/computer/", "Shared computer", "Files in /workspace versus packages that do not survive."),
        ("/troubleshooting/stuck/", "Stuck labels", "Cleaning up and 50 percent Starting."),
        ("/troubleshooting/", "Not working index", "If the failure is not an update."),
    ]
    sources = [
        ("Computer recovery", CURSOR_RECOVER),
        ("Official troubleshooting", DOC_TROUBLE),
        ("Update then lost session", "https://forum.cursor.com/t/unable-to-reconnect-to-my-grok-bots-computer-after-attempted-update/170000"),
        ("Packages wiped", "https://forum.cursor.com/t/cloud-computer-wipes-packages-after-rebuild/169847"),
        ("WhatsApp session", "https://forum.cursor.com/t/computer-refresh-wipes-whatsapp-linked-device-session-in-grok-bot/169025"),
        ("Cleaning up", "https://forum.cursor.com/t/grok-bot-hanging-at-cleaning-up-phase-after-resetting/169364"),
    ]
    return _render(
        "Update",
        "Grok Bot update failed",
        answer,
        "/troubleshooting/recover-vs-reset/?utm_source=guide&utm_campaign=update-failed",
        "What Update, Recover, and Reset each remove",
        rest, faqs, related, sources,
    )


def phone_not_connecting():
    answer = '''
<p>The Grok Bot phone app does not connect to the laptop. It signs into the same Cursor account and shows the same cloud computer the desktop uses.</p>
<p>If the iPhone works and the desktop is black or stuck reconnecting, the bots were not deleted. Do not Reset from the desktop out of panic.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to Reset the computer, reinstall the phone app, or sign into a second Cursor account so the phone “attaches” to the Mac. None of those create a link between the two devices. There is one roster and one hosted computer per Cursor account. A second login is an empty roster with your bots still on the first account. Reset can delete bots while an official rebuild was the real fix for a desktop that is black and an iPhone that still works.</p>
<p>The other failure looks like the opposite. Desktop and iOS are both stuck, and the phone is on cellular, so it is not your Wi-Fi. Staff often call that server-side. Hold off on Reset, Recover, Update, and signing out until you have a reason beyond the spinner.</p>
<h2>Steps</h2>
<ol>
<li>Install from the official store only. iPhone needs iOS 18 or later. The same iOS app runs on iPad with iPadOS 18 or later. Android is Google Play package ai.x.grok.bot, Android 9 or later. Then sign in with the Cursor account that already has the desktop roster.</li>
<li>On the phone, computer controls are Update Computer and Reset Computer under Settings, Bot, Bot Computer. They are the same class of control as the desktop, not a pairing button for the laptop.</li>
<li>Desktop black or Reconnecting, iOS fine on the same login: prefer Recover or Update on the desktop, or wait if you were told an official rebuild is coming. Do not Reset to force the Mac to match the phone.</li>
<li>Both devices stuck, phone on cellular: stop clicking. Email hi@cursor.com with the version, OS, the exact sentence, whether both devices fail, and what you already pressed.</li>
<li>A silent roster on both phone and desktop, while the computer view still opens, is often the weekly meter. macOS and iOS share one usage bucket. Installing the phone app does not refill it. Do not delete the phone app to fix a full meter.</li>
</ol>
<h2>Limits</h2>
<p>Several jobs stay on the desktop even when the phone is connected to the account. Always allow for local execution lives only in the desktop app on that machine. iOS can approve one shot, and those approvals clear on every new message. The routine webhook URL and sender key appear only on the desktop. Teach a task is a desktop recording. Canva that fails with Invalid redirect URI on iOS should be connected from the desktop; it then syncs.</p>
<p>iOS 1.3.2 sends a question list as soon as you tap one option. Multi-select before send needs a newer Grok Bot app build. That is a client bug, not a failed connection to the computer.</p>
<p>The phone can chat, watch the computer, take over a stuck login, and open Plugins from the top-left avatar. It is not a full replacement for a laptop install that failed the chip check or the Windows architecture check. Fix that install on the desktop page. Days of Can&apos;t reach on every device after Recover, Reset, and reinstall are a stuck hosted computer for staff, not a phone setting.</p>
'''
    faqs = [
        ("Does the phone get its own computer?",
         "No. Phone and desktop share one Cursor account, one roster, and one cloud computer."),
        ("The Mac is black and the iPhone still shows my bots. What do I press?",
         "Not Reset. Staff say Reset in that split can delete bots. Prefer Recover or Update, or wait for a staff rebuild if you were told one is coming."),
        ("Both the phone and the desktop are stuck, and the phone is on cellular. Is that my Wi-Fi?",
         "No. Staff often treat that as server-side. Hold off on Reset, Recover, Update, and signing out."),
        ("Why can I not turn on Always allow from the iPhone?",
         "Staff say Always allow for local-computer actions lives only on the desktop app for that machine. iOS can only one-time-approve, and those approvals clear on every new message."),
        ("Will the phone app fix a full weekly meter?",
         "No. macOS and iOS share the bucket. A quiet roster on both, with the computer still visible, is the usage page."),
    ]
    related = [
        ("/learn/phone-download/", "iPhone and Android download", "Official stores, OS versions, and desktop-only jobs."),
        ("/troubleshooting/cant-reach/", "Can&apos;t reach", "When the sentence is about the computer, not the phone pairing."),
        ("/troubleshooting/usage-limit/", "Usage limit", "Shared weekly pool when both devices go quiet."),
        ("/troubleshooting/", "Not working index", "Other screens."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Computer recovery", CURSOR_RECOVER),
        ("iOS cannot Always allow", "https://forum.cursor.com/t/authorization-death-by-1000-clicks/170087"),
        ("Webhook URL is desktop-only", "https://forum.cursor.com/t/webhook-url-missing-on-ios/169589"),
        ("Canva on iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
        ("iOS question list", "https://forum.cursor.com/t/multiple-choice-list-doesn-t-work-on-grok-bot-mobile/169830"),
    ]
    return _render(
        "Phone",
        "Grok Bot phone app not connecting to computer",
        answer,
        "/learn/phone-download/?utm_source=guide&utm_campaign=phone-not-connecting",
        "Official phone install",
        rest, faqs, related, sources,
    )


def uninstall():
    answer = '''
<p>Uninstalling Grok Bot removes the app from that device. It does not delete the Cursor account, the bots, the chats, or the cloud computer.</p>
<p>Account deletion is a different control, and Cursor Help says it is permanent. Do not use it because the desktop window looks wrong.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>People reach for Reset, or for iOS Delete Account, when they only wanted the Mac or Windows app gone. Reset rebuilds the hosted computer from the last snapshot and can drop unsynced bots and files. Installed apps on that computer are removed by Update, Recover, and Reset alike. None of those buttons uninstall the desktop client.</p>
<p>iOS Delete Account deletes the Cursor account. Cursor Help lists what goes with it: Grok Bot access, agents, chats, computers, and connected plugins, plus Cursor chat history and settings. Data is removed within 30 days. That is not an uninstall of a laptop app you can reinstall tonight and find the roster waiting.</p>
<h2>Steps</h2>
<ol>
<li>Decide which thing you are removing. The app on one device, or the Cursor account itself. If you still want the bots, stop at the app. Desktop Grok Bot can sign you out. Signing out is not deletion. Cursor Help is explicit: signing out or uninstalling the app leaves the account in place.</li>
<li>Windows: the documented removal control in this handbook is Settings, Apps, Installed apps. If two copies are listed, uninstall the older one and keep the latest, then quit the tray. The same Installed apps list is where a remaining copy is removed when you are leaving the desktop app. Quit from the tray so a leftover process does not keep running. This handbook does not have a separate official Uninstall item inside Grok Bot&apos;s own menus.</li>
<li>Mac: the official install puts the app in Applications. This handbook does not have a distinct xAI click-path titled Uninstall. Removing that application is still not account deletion. Renaming ~/Library/Application Support/Grok Bot is the white-screen fix for local config. It is not an uninstall, and it is not Reset. Keep the renamed folder until you know you do not need it.</li>
<li>Phone: removing the store app is an uninstall of the client. Delete Account is elsewhere. Cursor Help: open Grok Bot, tap the account avatar, tap the account, tap Delete Account, confirm, then in the browser type Delete and confirm again. The browser asks you to sign in so deletion re-proves identity. Skip that entire path unless you mean to delete the Cursor account.</li>
<li>To delete the account from the desktop or the web, Cursor Help says there is no separate Grok Bot account. Cancel an active subscription first. Then open cursor.com/dashboard, scroll to Advanced Account Settings, and click Delete Account. Personal accounts see that control. A Cursor Teams or Enterprise seat may not. Ask a team admin or contact support. Do not keep clicking Reset on the computer while you look for it.</li>
</ol>
<h2>Limits</h2>
<p>Files on your Mac or Windows machine stay on that machine. A subscription bought through the App Store is canceled in Apple&apos;s settings, not by deleting the Cursor account. A linked SuperGrok subscription is separate and is canceled on Grok if you no longer want it. A linked X Premium+ subscription is separate and is canceled on X. Cursor Help states those exceptions. This page does not restate prices.</p>
<p>Linux package removal is not given a command in the official pages this handbook uses. Remove the official deb, rpm, or AppImage the way you installed that package, and do not treat a community port&apos;s instructions as xAI&apos;s. Uninstalling any desktop build still leaves the Cursor account until you use the delete flow above.</p>
<p>After the app is gone, a later install from x.ai/bot or the official stores signs into the same account and shows the same computer, unless you deleted the account. If the goal was a white window or a duplicate Windows copy, use those fixes and keep the account.</p>
'''
    faqs = [
        ("If I uninstall the Mac app, are my bots deleted?",
         "No. Cursor Help says uninstalling the app or signing out leaves the Cursor account in place. Bots and the computer stay until you delete that account or Reset the computer."),
        ("What does iOS Delete Account actually remove?",
         "The Cursor account and Grok Bot access, agents, chats, computers, and connected plugins, plus Cursor chat history and settings. Cursor Help says the data is removed within 30 days."),
        ("I only have a duplicate Windows install. Do I delete the account?",
         "No. Uninstall the older copy from Installed apps, quit the tray, and open the remaining app."),
        ("I do not see Delete Account on the dashboard. Did the button move?",
         "Cursor Help says the control appears for personal accounts. A Teams or Enterprise seat may need an admin or support. It is not hidden inside Reset."),
        ("Does renaming the Application Support folder uninstall Grok Bot?",
         "No. That rename is the local-config fix for a white window. The app is still installed. The cloud computer is untouched."),
    ]
    related = [
        ("/learn/install/", "Install", "Official packages, if you are putting the app back."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "Computer buttons are not an uninstall."),
        ("/troubleshooting/white-screen/", "White screen", "The config-folder rename, which is not deletion."),
        ("/pricing/", "Pricing", "Cancel a subscription on the official billing pages, not here."),
    ]
    sources = [
        ("Delete your Grok Bot account", CURSOR_DELETE),
        ("Official troubleshooting", DOC_TROUBLE),
        ("Get started", DOC_START),
    ]
    return _render(
        "Uninstall",
        "How to uninstall Grok Bot",
        answer,
        "/learn/install/?utm_source=guide&utm_campaign=uninstall",
        "Official install, if you are putting it back",
        rest, faqs, related, sources,
    )


def is_free():
    answer = '''
<p>Grok Bot is not a consumer free tier, and it is not a separate product with its own checkout. Access is bundled with a paid Cursor plan or a linkable personal SuperGrok or X plan.</p>
<p>The eligibility table and every price stay on the pricing page. This page only explains why a free-looking spinner is not a free computer.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to install the app on a free Cursor plan and wait for Setting up your Grok Bot to finish. Staff say a free plan never gets a hosted computer. The spinner, instead of a sentence that access is missing, is a known display bug. Another download, a DNS change, or Reset will not provision a machine that the plan does not include. A team admin role is also not a seat. Assign yourself a Standard or Premium seat, or sign in with an account that has one.</p>
<p>A limited usage trial is a different thing from that spinner. The pricing snapshot, from Cursor Help, describes the trial as usage credits plus a 7-day window, debited by agent steps and tokens, not by how many messages you send. A large task can exhaust the credits at once. Spent trial credits are not restored. When they are gone, bots can stop answering while the computer view can still export. Do not Reset to stretch a trial. None of those sentences is a price.</p>
<h2>What official pages already agree on</h2>
<p>On the fetch dated 2026-09-20, Cursor Help and the xAI FAQ both include Grok Bot on every paid individual Cursor plan, including Pro, and on Cursor Teams. You can also link personal SuperGrok, Plus, or Heavy. Help also names X Premium+. The xAI FAQ paragraph we stored does not name X Premium+ in that same sentence. Help says a Cursor plan and a SuperGrok or X Premium+ link do not stack. The FAQ still says that if you have both, Grok Bot uses the side with more usage. This site does not pick a winner. Open both originals from the pricing page.</p>
<p>Linking is a usage grant on that same Cursor account. It does not open a second meter on the Grok side, and it does not change your Cursor plan. Cursor Help says you cannot unlink it yourself. Lite and SuperGrok Team or Enterprise cannot link. Staff have also said legacy request-based Cursor pricing does not include Grok Bot unless you opt into usage-based pricing. That is an eligibility gate, not a number this page will invent.</p>
<p>There is no separate Grok Bot subscription to buy. Metering sits on the Cursor account. macOS and iOS share one weekly bucket. When weekly usage runs out, continued spend depends on whether On-Demand is enabled. The usage page explains that order without dollar amounts.</p>
<h2>Limits</h2>
<p>The early-September 2026 announcement that Grok and Cursor Enterprise customers would get Grok Bot free for the next two weeks, including people without a seat, is a dated news post. The pricing snapshot treats that window as expired. It was never a consumer free tier. Read the news post before you tell an organization it is still open.</p>
<p>Third-party articles that still say Grok Bot requires Cursor Ultra are behind the Help and FAQ wording from 2026-09-20. This page will not copy their dollar figures. If you need a current list price, open x.ai/bot and the Cursor plans page yourself. If you do not want a managed seat at all, the alternatives page compares self-hosted projects. Those are not unofficial clients for your Cursor roster, and this site does not price them either.</p>
'''
    faqs = [
        ("Is there a free Grok Bot plan I can stay on?",
         "Not a consumer free tier. A free Cursor plan does not get a hosted computer. A limited usage trial on some accounts is credits plus a time window, and spent credits are not restored."),
        ("Does linking SuperGrok create a second bill on grok.com?",
         "Cursor Help describes linking as a usage grant on the same Cursor account, not a second meter. You cannot unlink it yourself. Read their page before you link. Prices are not repeated here."),
        ("Why do two official pages disagree about stacking?",
         "On the 2026-09-20 fetch, Help says a Cursor plan and a SuperGrok link do not stack. The xAI FAQ says Grok Bot uses whichever side has more usage. Open both. This site does not invent a resolution."),
        ("The app has been on Setting up for an hour. Am I in the trial?",
         "If the Cursor plan is free, or you are an admin without a seat, staff say no computer is provisioned. That is not the trial running slowly."),
        ("Where do I read actual prices?",
         "The pricing page links the official sources and refuses to fill blanks. Do not expect dollar amounts on this page."),
    ]
    related = [
        ("/pricing/", "Pricing snapshot", "Official eligibility wording, side by side, with no invented USD."),
        ("/learn/cost-and-pitfalls/", "Usage and On-Demand", "What happens when the weekly pool runs out."),
        ("/troubleshooting/stuck/", "Stuck on Setting up", "The spinner that means a missing seat."),
        ("/compare/", "Alternatives", "Self-hosted projects, if you do not want a managed seat."),
    ]
    sources = [
        ("Plans and billing", CURSOR_PLANS),
        ("Get started", DOC_START),
        ("xAI FAQ", "https://docs.x.ai/grok-bot/faq"),
        ("More plans announcement", "https://x.ai/news/grok-bot-more-plans"),
        ("Enterprise trial announcement", "https://x.ai/news/grok-bot-for-enterprise"),
        ("Free plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
    ]
    return _render(
        "Access",
        "Is Grok Bot free",
        answer,
        "/pricing/?utm_source=guide&utm_campaign=is-grok-bot-free",
        "Pricing snapshot, including the eligibility table",
        rest, faqs, related, sources,
    )


def linux_setup():
    answer = '''
<p>Grok Bot Linux setup failed on very old unofficial builds because those builds were rejected. The supported packages now are the official deb, rpm, and AppImage on x.ai/bot.</p>
<p>A community port, an AUR copy, or a Wine wrapper is not staff support. Fix the official package before you blame your network.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to keep a 0.18 tree that a forum post once offered, or to Reset the computer because setup says it cannot be reached. Staff said Can&apos;t reach your computer on Linux Grok Bot 0.18.0 was not the network. That old build was rejected. In that same reply they listed supported platforms as macOS, Windows, and iOS, and said a formal Linux desktop was not available yet. The xAI FAQ fetched for this handbook on 2026-09-20 lists Linux x64 and Arm64, with deb, rpm, and AppImage under More downloads. Both statements are in the record. The one to follow for a new install is the later FAQ: use the official package. A rejected 0.18 binary will still fail setup, and Reset cannot make the backend accept it.</p>
<p>Mixing an official install and a community port in the same prefix leaves two binaries and no way to see which one is talking to the account. Uninstall the extra one before you collect logs.</p>
<h2>Steps</h2>
<ol>
<li>Open x.ai/bot, then More downloads. Pick deb, rpm, or AppImage for the distro, and match the CPU. uname -m of x86_64 is the x64 build. aarch64 is Arm64. Sign in with the Cursor account that holds the plan. There is no separate Grok Bot account.</li>
<li>The app checks for updates on its own. Settings, Updates, Check for Updates replaces the desktop app. It does not reset the cloud computer. The computer control is Update under Grok Bot&apos;s Computer, same as on Mac and Windows.</li>
<li>Empty ListMachines, or local execution failing, on Grok Bot 0.30.0 for Linux is a known defect. Staff said a fix was already merged for a later desktop update. The interim workaround they gave: an unlocked system keyring, gnome-keyring or KWallet, fully quit leftover Grok Bot processes, then relaunch. Do not treat that as a packaging bug in the deb.</li>
<li>If the official package launches and the computer view opens, stop. You do not need the community port. Use Nichokas/grokbot-linux-port only after the official package fails on that distro, and only after you read the README for the version it targets. Wine wrappers and random third-party repacks are outside staff support.</li>
</ol>
<h2>Limits</h2>
<p>Local stdio MCP is unreachable from the cloud computer on every platform, including an official Linux package. Remote HTTP MCP or the cloud browser is the integration path. Execution on Local Computer is a different permission: it runs on the Linux machine in front of you after you approve it. It is not a way to put the Bot on a company VPN. Staff warn that installing a VPN client on the Bot computer can take the machine offline.</p>
<p>Always allow for local execution is desktop-only and can still fail to cover every shell, which is the local-computer page. Device limits still apply: a Grok Bot login can count as a Cursor device, and the cloud workspace may count as another, toward Too many computers. After Update Computer, apt packages and daemons are gone even if files in /workspace survived. Keep a short install list in a file. This page does not publish distro-specific install commands beyond the package types the FAQ names.</p>
'''
    faqs = [
        ("Staff said Linux was not supported. Is that still the install advice?",
         "That reply was about rejected 0.18 builds. The xAI FAQ fetched 2026-09-20 lists Linux x64 and Arm64 as official. Use the package on x.ai/bot, not the old unofficial build."),
        ("ListMachines is empty on 0.30.0. Do I reinstall the deb?",
         "Staff called it a known bug with a fix merged for a later desktop update. Interim: unlock gnome-keyring or KWallet, quit leftover processes, and relaunch."),
        ("Can I attach a local MCP server from the Linux box?",
         "Not a stdio or localhost server. The cloud computer cannot reach it. Use public HTTPS MCP, or the cloud browser."),
        ("Will a community AUR package get staff help?",
         "No. Prefer the official deb, rpm, or AppImage. Community ports are not staff-supported, and very old ones were rejected at setup."),
        ("Does updating the Linux app reset the computer?",
         "No. Check for Updates restarts the app. Update under Grok Bot computer is the separate control, and it removes installed packages on the computer."),
    ]
    related = [
        ("/tools/linux-port/", "Linux packages", "Official packages versus the community port."),
        ("/learn/install/", "Install", "The same Cursor login as Mac and Windows."),
        ("/troubleshooting/local-computer/", "Local computer", "Keyring, daemons, and Always allow."),
        ("/troubleshooting/dns-error/", "DNS error", "If the official build is fine and the hostname will not resolve."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("Linux 0.18 rejected", "https://forum.cursor.com/t/grok-bot-couldnt-finish-setup/170010"),
        ("Linux local execution", "https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157"),
        ("Local MCP", "https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182"),
    ]
    return _render(
        "Linux",
        "Grok Bot Linux setup failed",
        answer,
        "/tools/linux-port/?utm_source=guide&utm_campaign=linux-setup",
        "Official packages versus the community port",
        rest, faqs, related, sources,
    )


def local_computer():
    answer = '''
<p>Grok Bot local computer not connected means the helper on the machine in front of you lost its link. Chat can keep working, and the cloud computer can be healthy. Fully quit and let the helper register again before you Reset that cloud machine.</p>
<p>Official troubleshooting separates the two permissions. Cloud work and local work are not the same switch.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>Recover and Reset rebuild the hosted computer. They do not re-register local-exec-daemon on your Mac, Windows PC, or Linux box. People press them because Settings says the local machine is offline, or because a command on the laptop fails while the bot still chats. Staff have confirmed the split: chat stays up, the local-computer link drops, and a full quit reconnects. One Mac path was fixed in 0.23. Later builds still show the helper starting and then failing registration, so quit remains the first step rather than a rebuild.</p>
<p>Settings can also lie the other way. After a large copy off the computer, or a shell that times out, staff say the machine can leave the agent list for about a minute while Settings still says connected. Resetting during that minute does not speed the minute up.</p>
<h2>Steps</h2>
<ol>
<li>Open the control official troubleshooting names: Settings, General, Bot, Execution on Local Computer. The same help page also points at the computer&apos;s row under Settings, Computer, Computers. Staff posts shorten the label to Execution on Local Computer. If an older screenshot disagrees, follow the labels on the current troubleshooting page. Keep local access off unless the task needs files or commands on the machine in front of you. The handbook default, from the computer lesson, is to ask every time.</li>
<li>Mac, chat up, local shown offline: fully quit from the menu bar and reopen. If it drops again, the log staff asked for is ~/.grokbot/local-exec-daemon.log. After an update, a full quit plus sign-out is what staff said recreates a helper that fails registration. Desktop 0.31.0 was the build they said was rolling out for that report. Do not invent a newer build number than the one in that note.</li>
<li>Windows leftover daemon on 0.30.0: quit from the tray, end remaining Grok Bot and local-exec-daemon processes in Task Manager, relaunch, and wait about a minute to re-register. A different 0.27.0 report stayed disconnected after a clean registration. Staff said to fully quit every Grok process and launch once, and if it still fails it is service-side.</li>
<li>Large CopyFromBox or a timed-out shell: split the copy, wait about a minute before you retry, and if it stays stuck use Cmd+Q, then the staff cleanup pkill -f local-exec-daemon, then reopen. That command is their workaround for a wedged helper, not a reset of the cloud computer.</li>
<li>Linux 0.30.0 empty ListMachines: unlock gnome-keyring or KWallet, quit leftover processes, relaunch. Details are on the Linux setup page.</li>
</ol>
<h2>Limits</h2>
<p>Always allow lives only in the desktop app on that machine. iOS can only approve one action at a time, and those approvals clear on every new message. Always allow is still not a promise that every shell runs. Staff have a thread where ExternalShell stayed blocked despite Always allow. Do not widen rules to allow everything in the browser to compensate. Require Approval still outranks Always Allow.</p>
<p>The cloud computer cannot join a corporate VPN. Do not install a VPN client on it. Staff say that can knock the box offline. Internal sites that need the VPN should use Execution on Local Computer on a machine that is already on the VPN. YubiKey, in the same staff note, is a desktop control under Settings, Security Key, on macOS or Windows. This page does not expand that into a key-setup guide.</p>
<p>A Grok Bot login counts as its own Cursor device, and the cloud workspace can count as another, toward Too many computers. That device limit is not fixed by reinstalling the local helper.</p>
'''
    faqs = [
        ("Chat works and the local machine says offline. Is the cloud computer dead?",
         "No. Staff treat that as the local helper dropping its link. Fully quit and reopen before Recover or Reset."),
        ("Settings says connected, but file copies fail. What happened?",
         "A large copy or a timed-out shell can drop the machine from the agent list for about a minute while Settings still says connected. Wait, split the copy, and only then quit and clear the daemon."),
        ("Where is the control, exactly?",
         "Official troubleshooting: Settings, General, Bot, Execution on Local Computer, or the row under Settings, Computer, Computers. Staff posts use the shorter name Execution on Local Computer."),
        ("Can I set Always allow on the iPhone so the desktop stops asking?",
         "No. Always allow is stored on that desktop. The phone can approve a single action, and the approval clears on the next message."),
        ("Will local execution put the bot on my office VPN?",
         "Only by running the command on a computer that is already on the VPN. Installing a VPN client on the cloud computer is what staff say can take that machine offline."),
    ]
    related = [
        ("/learn/computer/", "Shared computer", "Cloud machine versus the laptop in front of you."),
        ("/troubleshooting/linux-setup/", "Linux setup", "Keyring and empty ListMachines."),
        ("/troubleshooting/phone-not-connecting/", "Phone app", "Why Always allow is missing on iOS."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "Use these on the cloud computer, not on the local helper."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Mac local offline", "https://forum.cursor.com/t/grok-bot-mac-chat-works-local-computer-reported-offline/168973"),
        ("Helper registration", "https://forum.cursor.com/t/grok-bot-cannot-access-my-local-computer/169924"),
        ("Windows leftover daemon", "https://forum.cursor.com/t/new-report-windows-leftover-daemon-on-0-30-0/170121"),
        ("Copy timeout", "https://forum.cursor.com/t/grok-bot-local-computer-execution-looks-connected-in-settings-but-is-not-actually-usable-for-file-i-o/169877"),
        ("ExternalShell still blocked", "https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180"),
        ("VPN and security keys", "https://forum.cursor.com/t/vpn-sso-passkey-and-yubikey-within-grokbot/170148"),
    ]
    return _render(
        "Local computer",
        "Grok Bot local computer not connected",
        answer,
        "/learn/computer/?utm_source=guide&utm_campaign=local-computer",
        "What the shared computer is, and what it is not",
        rest, faqs, related, sources,
    )


def routine_did_not_run():
    answer = '''
<p>A Grok Bot routine did not run because it is disabled, the schedule or time zone is wrong, usage is paused, or the run sat in a queue. Deleting the routine is not the first fix.</p>
<p>Staff say a label of Next run: Run now often means the slot already fired and waited, sometimes 10 to 37 minutes. Some runs finish without posting anything in chat.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to delete the routine and create it again, or to rewrite the bot&apos;s instructions, because the clock looks stuck. Staff say editing bot instructions, or which platform created the routine, does not break the schedule. Recreating it throws away the run history you would have used to see the failure. A routine that came due while weekly usage was blocked was skipped. It does not queue up and run later as a surprise send when the meter refills. Creating a twin routine will not replay the skipped slot.</p>
<h2>Steps</h2>
<ol>
<li>Open the routine. Official troubleshooting says to verify that it is enabled, that the schedule and time zone are correct, that the owning bot still exists, that required plugins are still authenticated, that the computer can reach the source system, and that usage or account access is not paused.</li>
<li>Read recent run history before you edit anything. If the history shows a run that finished with no chat line, that matches the staff note: some runs complete without posting. Message the bot and ask for an on-demand check-in instead of rebuilding the schedule.</li>
<li>If the label says Next run: Run now for a long time, wait through the queue window staff described, on the order of 10 to 37 minutes, before you call it dead. Do not recreate the routine while that wait is the documented behavior.</li>
<li>Use Test run only with safe input. Official warning: tests do real things. They can navigate sites, change files, and call connected tools. Put write actions behind approval.</li>
<li>For an event trigger, confirm the source channel, repository, and matching rule are still valid. Event triggers come from Cursor account integrations. That path is not the same authorization as the Slack or GitHub plugin, and it may need to be granted separately. A narrow rule matters: every new message burns usage and acts on mail you did not mean.</li>
</ol>
<h2>Limits</h2>
<p>The webhook URL and the sender key for a webhook routine appear only on the desktop app, not on iOS. Open the trigger card on the desktop. Updating the phone will not reveal that URL.</p>
<p>The product cap recorded in the skills lesson is 50 routines per bot, and the app keeps the latest 20 runs per routine. Deletes take effect immediately and have no undo. Deleting a bot deletes its routines. After a long absence the product may ask whether to keep routines running. No answer pauses them. That pause is not a failed cron on your laptop. Background routines can run with the laptop closed. Idle sleep of the cloud computer, which kills background processes and can drop installed packages, is a separate fact about the machine. Do not confuse a sleeping package daemon with a skipped routine unless the run history says the routine itself failed.</p>
<p>A webhook POST that returned an internal error was a server-side rollback in one staff thread. The same request worked after they reverted the change. If your routine&apos;s history shows that class of error, write support with the time. Recreating the routine does not roll back their API.</p>
'''
    faqs = [
        ("Next run says Run now for half an hour. Is the schedule broken?",
         "Staff say the slot often fired and sat in a queue, commonly 10 to 37 minutes. Some finished runs never post to chat. Check history, then message the bot, before you delete the routine."),
        ("I edited the bot instructions. Did that clear the schedule?",
         "Staff say editing instructions, or which platform created the routine, does not break the schedule."),
        ("The weekly meter was full overnight. Will this morning replay every skipped run?",
         "No. Routines that came due during the block were skipped. They do not run later as a batch. Messages you sent by hand during the block are the ones that reply in a batch."),
        ("Where is the webhook URL on my iPhone?",
         "Nowhere. Staff say the POST URL and sender key appear only on the desktop app."),
        ("Can I test a routine that sends mail?",
         "Only if you accept that Test run performs real actions. Official docs say to use safe inputs and to keep writes behind approval."),
    ]
    related = [
        ("/learn/skills-routines/", "Skills and routines", "Save a skill after a good run, then schedule it."),
        ("/troubleshooting/usage-limit/", "Usage limit", "A paused meter skips routines that come due."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "A routine whose connector is no longer authenticated."),
        ("/troubleshooting/", "Not working index", "If the bot itself is silent, not just the schedule."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Routines sit in a queue", "https://forum.cursor.com/t/grok-bot-routines-dont-auto-run-on-schedule/170358"),
        ("Webhook URL is desktop-only", "https://forum.cursor.com/t/webhook-url-missing-on-ios/169589"),
        ("Webhook server error", "https://forum.cursor.com/t/grok-bot-webhooks-are-failing-with-internal-server-error/169323"),
    ]
    return _render(
        "Routines",
        "Grok Bot routine did not run",
        answer,
        "/learn/skills-routines/?utm_source=guide&utm_campaign=routine-did-not-run",
        "Skills first, then routines",
        rest, faqs, related, sources,
    )


def approval_stuck():
    answer = '''
<p>Grok Bot approval needed stuck is usually a card that already timed out, or an Ask first rule that outranks Allow automatically. Rebuilding the computer does not delete that rule.</p>
<p>Read the proposed target before you approve anything. If the card is no longer clickable, cancel it or send a replacement instruction.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to Reset, or to flip Always allow, because a homepage tile still says Approval needed and the bot has nothing in front of you. Staff say that tile is often an approval card that timed out after about 10 minutes unanswered. The tile is supposed to clear when the card expires. When it does not, open the agent and send a short message, or restart the app. Reset would rebuild the computer and can drop unsynced work, and it would not remove an Ask first rule that is still on the account.</p>
<p>The cost lesson records the same precedence from the product: Require Approval outranks Always Allow. A wide rule such as allow everything in the browser does not beat an Ask first rule, including a team rule an admin requires.</p>
<h2>Steps</h2>
<ol>
<li>Open the card and read the target and the arguments. Approve only if that action is the one you wanted. Official troubleshooting says that if the card is no longer actionable, reject or cancel it when that control exists, send the bot a replacement instruction, and ask it to regenerate the action with the corrected scope.</li>
<li>If the homepage tile remains and the bot has nothing pending, use the staff workaround: open the agent and send a short message, or restart the app. Do not click Reset to clear a badge.</li>
<li>If the same class of action keeps asking, open Settings, General, Bot, Auto-review. Look for a matching Ask first rule, including team rules. Ask first takes precedence over Allow automatically. Personal auto-review rules live on the current desktop and sync to its Grok Bot computer. Check them again after you switch desktops. A rule you set on the office Mac is not automatically the rule on a home Mac until that sync has happened.</li>
<li>A different stuck reminder, the one that says the bot is waiting for help on its computer after login already succeeded another way, clears only when you answer that card or send any chat message. It does not dismiss itself. That card is covered on the waiting-for-login page. Do not confuse it with Auto-review.</li>
</ol>
<h2>Limits</h2>
<p>Always allow for local-computer actions is desktop-only, and ExternalShell can still be blocked despite it. Turning it on to escape an approval card can allow local commands you did not mean, without clearing an Ask first rule. iOS cannot set Always allow at all.</p>
<p>This page does not list every team policy an admin can require. If the rule is locked and you cannot see Auto-review change it, ask the admin. Support mail is hi@cursor.com when a card is stuck and the restart plus a chat message did not clear the badge. Include the bot name and the time. Do not include the secret the card was asking for.</p>
'''
    faqs = [
        ("The homepage says Approval needed and the bot has nothing to approve. What is the tile?",
         "Staff say it is usually a card that timed out after about ten minutes. Open the agent and send a short message, or restart the app. The tile is supposed to clear when the card expires."),
        ("I set Allow automatically. Why does it still ask?",
         "Ask first rules take precedence over Allow automatically, including team rules an admin requires. Check Settings, General, Bot, Auto-review."),
        ("Will Reset clear a stuck approval?",
         "No. Reset rebuilds the computer. It does not delete an Ask first rule, and it can drop unsynced bots and files."),
        ("I switched Macs and the rules feel different. Did I lose them?",
         "Personal auto-review rules live on the current desktop and sync to its Grok Bot computer. Check again after a desktop switch."),
        ("The bot already logged in, but the waiting card is still there. Is that Auto-review?",
         "Not necessarily. Staff say that reminder clears only when you answer the card or send a chat message. It does not notice that login finished another way."),
    ]
    related = [
        ("/learn/computer/", "Shared computer", "Takeover, secrets, and what Reset actually removes."),
        ("/learn/cost-and-pitfalls/", "Approvals and usage", "Require Approval outranks Always Allow."),
        ("/troubleshooting/waiting-for-login/", "Waiting for login", "The card that wants you on the computer, not in Auto-review."),
        ("/troubleshooting/local-computer/", "Local computer", "Where Always allow actually lives."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Homepage approval tile", "https://forum.cursor.com/t/grok-bot-approval-needed-stays-on-agent-view-homepage-when-coder-has-nothing-to-approve/170127"),
        ("Waiting card does not auto-dismiss", "https://forum.cursor.com/t/grok-bot-wrangler-box-auth-reminder-stays-stuck-after-auth-already-succeeded-via-another-path/170052"),
    ]
    return _render(
        "Approval",
        "Grok Bot approval needed stuck",
        answer,
        "/learn/computer/?utm_source=guide&utm_campaign=approval-stuck",
        "Shared computer: takeover and approvals",
        rest, faqs, related, sources,
    )


def attachment():
    answer = '''
<p>Grok Bot attachment cannot be read when the file is over the size cap, still uploading, encrypted, or not a supported type. Wait until the upload finishes before you send.</p>
<p>Official troubleshooting caps a file at 25 MB, or 200 MB for video, and caps a desktop send at six attachments.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to drop the file again, or to press Enter the moment the picker closes. Staff say a screenshot reaches chat through the composer plus button, or by dragging a file you already saved, and only after the thumbnail is visible. A drag from another app, or Enter before the thumbnail, usually drops the attachment. Sending a second time with the same half-uploaded file repeats the failure. Resetting the computer does not raise the size cap and does not decrypt a file.</p>
<h2>Steps</h2>
<ol>
<li>Check the limits official troubleshooting lists. The file is no larger than 25 MB, or 200 MB for video. You did not select more than six attachments at once on desktop. The file is not encrypted or password-protected. The upload finished before you sent. The type is one the product supports.</li>
<li>If the format is unusual, export it as PDF, CSV, plain text, or an image and attach that. Do not remove document protection if the resulting file would violate your data policy. The help page states that limit on purpose.</li>
<li>For an image into chat: use the composer plus button or drag a saved file, then wait for the thumbnail, then send. If the thumbnail never appears, the send did not include the file, even if the bubble looks busy.</li>
<li>The in-app file viewer only offers Download today, in the staff note on file contents. For markdown or plain text you can click-drag to select and copy. Word and PDF files will not highlight that way. Ask the bot to paste the full text into chat and use the message Copy action. That is a viewer limit, not a failed upload.</li>
</ol>
<p>That Copy action puts the answer on the clipboard. If you need it as a Word file, a raw paste keeps the Markdown marks; <a href="https://chatgpt2word.com/how-to-export-chatgpt-to-word">how to export a chat answer to a Word .docx</a> turns the same clipboard into headings and tables, and the steps apply to a Grok reply as well as ChatGPT.</p>
<h2>Limits</h2>
<p>Forum upload by the assistant is a separate limitation staff acknowledged. The bot cannot attach the screenshot to a Cursor forum post or a support mail for you. Attach it yourself, or reply on the support email with the file.</p>
<p>The Gmail connector can list attachment metadata and still cannot download the bytes. That is a plugin gap, not the 25 MB chat cap. Use the cloud browser or put the file in Drive, and read the plugin page before you keep re-authenticating Gmail in the hope the bytes appear.</p>
<p>This page does not publish a full list of MIME types. Official troubleshooting says to try the export formats above when a type is refused, and it does not name a longer allow-list we could copy. Six attachments is the desktop number they published. This handbook does not have a different phone cap to state, so it will not invent one.</p>
'''
    faqs = [
        ("What is the size limit?",
         "Official troubleshooting: 25 MB for a file, or 200 MB for video. More than six attachments at once on desktop is also refused."),
        ("I hit Enter and the image vanished. What did I skip?",
         "The thumbnail. Staff say to use the composer plus button or drag a saved file, and to wait until the thumbnail is visible before send."),
        ("The file is a password-protected PDF. Can the bot open it if I type the password in chat?",
         "Do not paste the password into chat. Official troubleshooting says not to remove protection when that would violate your data policy, and encrypted files are on the cannot-read list."),
        ("The viewer has no Copy button. How do I get the text?",
         "Staff say the viewer offers Download. Markdown and text can be selected and copied. For Word or PDF, ask the bot to paste the text into the chat and copy that message."),
        ("Gmail shows the attachment name and not the file. Is that the 25 MB cap?",
         "No. Staff say the Gmail connector lists metadata and has no download tool. That limit is on the plugin page."),
    ]
    related = [
        ("/learn/computer/", "Shared computer", "Where files on the computer live, separate from a chat upload."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "Gmail can list attachment names and still not download bytes."),
        ("/learn/first-bot/", "First Bot", "A first task that attaches one document and leaves it unchanged."),
        ("/troubleshooting/", "Not working index", "If the failure is the computer, not the file."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Composer thumbnail", "https://forum.cursor.com/t/grok-bot-cannot-attach-inline-images-to-cursor-bug-reports-chat-drop-and-forum-upload/170255"),
        ("Viewer copy versus download", "https://forum.cursor.com/t/file-contents-and-grokbot/170421"),
        ("Gmail attachment bytes", "https://forum.cursor.com/t/grok-bot-gmail-connector-can-list-attachments-but-cannot-download-their-bytes/169261"),
    ]
    return _render(
        "Files",
        "Grok Bot attachment cannot be read",
        answer,
        "/learn/computer/?utm_source=guide&utm_campaign=attachment",
        "Where computer files live",
        rest, faqs, related, sources,
    )


def sign_in():
    answer = '''
<p>Grok Bot sign-in does not complete when the app loses the browser, Legacy Privacy Mode blocks the storage it needs, or the Mac is still holding an expired session. There is no separate Grok Bot account to create.</p>
<p>Keep the app open, finish Cursor in the browser, and return to the app yourself if focus never comes back.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to make a second Cursor user, or to Reset a computer you cannot see yet, because the popup vanished. Official troubleshooting says to keep Grok Bot open while the browser runs, confirm the browser shows a successful Cursor sign-in, return to the app manually, and try Get started or Sign in with Cursor again. Then confirm the account has Grok Bot access. A second Cursor user does not finish the first popup. It creates an empty roster.</p>
<p>An error about Legacy Privacy Mode means the account data setting does not allow the storage Grok Bot needs. Switching the control is not enough. Save Privacy Mode, not Legacy, on the Cursor dashboard. Until that save exists, Retry, Recover, and Reset all fail, and so does another install. Fully quit after the save, then sign in again.</p>
<h2>Steps</h2>
<ol>
<li>Follow the five official checks above before any computer button. If the organization uses SSO, finish the organization login. Do not sign in with a different personal account to skip it.</li>
<li>After a password change, the Mac can say the account is not available yet even though the plan and the cloud computer are fine. Staff call that an expired session. Log out from the bottom of that screen, fully quit with Cmd+Q, reopen, and sign in with the new password. Check Access followed by a download prompt is a misleading expired-session screen, not a missing entitlement.</li>
<li>Too many computers is a device cap, not a bad password. Staff say a Grok Bot login counts as its own Cursor device, and the cloud workspace can count as a second one. Signing out of a session you no longer use is the direction that note implies. This handbook does not have an official click-path, beyond that fact, for raising the cap. Do not Reset the cloud computer to free a device slot. Write support if you cannot tell which session is the extra one.</li>
<li>A deleted Cursor account can leave the Grok link orphaned so it cannot be relinked, in the staff thread on that failure. This handbook has no self-serve repair for that case. Contact hi@cursor.com. Do not create a fresh Cursor user and expect the old bots to appear on it.</li>
</ol>
<h2>Limits</h2>
<p>Sign-in is not the same screen as Setting up, Connecting forever after Privacy Mode is already saved, or Can&apos;t reach once you are in. Those are the stuck and DNS pages. A white window after a successful login is local config, not another account. Usage silence after a good login is the meter.</p>
<p>Desktop sign-out does not delete the account. iOS Delete Account does. If you only needed a clean login, stop at sign-out. The uninstall page has the delete flow so you do not take it by accident.</p>
'''
    faqs = [
        ("The browser says I am signed in, and the app never notices. What next?",
         "Return to the app yourself. Official troubleshooting says focus does not always come back. Keep Grok Bot open during the browser step. Do not open a second Cursor account."),
        ("It mentions Legacy Privacy Mode. Will Reset fix that?",
         "No. Save Privacy Mode on the Cursor dashboard. Retry, Recover, and Reset all fail until that choice is saved. Then fully quit and sign in again."),
        ("After a password change the Mac says Grok Bot is not on this account. My plan still shows. What is that?",
         "Staff call it an expired session. Log out on that screen, Cmd+Q, and sign in with the new password. The download prompt on that screen is misleading."),
        ("What is Too many computers?",
         "Staff say the Grok Bot login is its own Cursor device, and the cloud workspace can count as another. Resetting the computer does not free the slot."),
        ("I deleted the Cursor account. Can I relink Grok Bot?",
         "The staff thread says deletion can orphan the link and block relinking. This handbook has no self-serve undo. Contact Cursor support."),
    ]
    related = [
        ("/learn/login/", "Cursor login", "The normal sign-in, without the failure cases."),
        ("/troubleshooting/stuck/", "Stuck on Connecting", "Privacy Mode that was never saved."),
        ("/troubleshooting/uninstall/", "Uninstall", "Sign-out versus deleting the Cursor account."),
        ("/learn/is-grok-bot-free/", "Is Grok Bot free", "When the account has no Grok Bot access to begin with."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Stale session after password change", "https://forum.cursor.com/t/grok-bot-mac-blocked-after-password-change-app-says-unavailable-spending-shows-supergrok-plus/170389"),
        ("Too many computers", "https://forum.cursor.com/t/does-logging-into-grokbot-count-as-a-separate-computer/169289"),
        ("Deleted account orphans the link", "https://forum.cursor.com/t/deleted-cursor-account-leaves-grok-link-orphaned-and-blocks-relinking/168783"),
        ("Privacy Mode and first setup", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
    ]
    return _render(
        "Sign-in",
        "Grok Bot sign-in does not complete",
        answer,
        "/learn/login/?utm_source=guide&utm_campaign=sign-in",
        "Sign in with Cursor",
        rest, faqs, related, sources,
    )


def waiting_for_login():
    answer = '''
<p>Grok Bot stuck waiting for login means the bot is on a page that wants a human. Open the computer and take over that step. Do not paste the password or the verification code into chat.</p>
<p>A bot cannot start a second computer-use task on the same screen until the current one finishes or you redirect it.</p>
'''
    rest = '''
<h2>Why the native method fails</h2>
<p>The native method is to Reset, or to type the password into the transcript, because the bot has stopped talking. Official troubleshooting treats a stuck bot as a status check: read the sidebar and the conversation, open the computer, and look for a question, an approval, a login, a CAPTCHA, or a secret request. Send a short redirect if the approach is wrong. Send Stop now if the work should end. None of that is a computer rebuild.</p>
<p>Staff add a sentence you can use when takeover never appears: ask the bot to hand you the computer. For a passkey prompt, use Try another way rather than fighting the passkey on a machine that does not have your device. The cloud computer cannot complete a passkey that lives on your phone unless you are the one holding that phone.</p>
<h2>Steps</h2>
<ol>
<li>Open Agent Computer from the chat and see whether the bot is waiting on a page. If it is a login, take over, sign in yourself, finish two-factor or the CAPTCHA, confirm the signed-in page has loaded, return control, and tell the bot to continue from that page.</li>
<li>Do not paste a password or a one-time code into ordinary chat. When a connector shows a secrets card, fill it there. Values are masked, stay out of the conversation, and are not shown to the model.</li>
<li>Some sites expire the session or ask again on every sensitive action. Official troubleshooting says that cannot always be avoided. Have the bot stop and notify you instead of bypassing the check.</li>
<li>A reminder that says the bot is waiting for help on its computer, after you already finished login another way, clears only when you answer that card or send any chat message. Staff say it does not auto-dismiss. Clicking around the computer without answering the card leaves the reminder up.</li>
<li>If the computer itself says Reconnecting, the bot cannot finish the turn no matter how you redirect it. That is the can&apos;t-reach page. If every bot is silent and the computer view is fine, that is usage. This page is the case where one bot is visibly waiting.</li>
</ol>
<h2>Limits</h2>
<p>Takeover does not put the cloud computer on a corporate VPN. Staff say the machine cannot join that VPN today, and a VPN client installed on it can knock it offline. Sites that exist only inside the VPN need Execution on Local Computer on a machine that is already on the VPN, which is the local-computer page. Public SSO in the browser, such as an Atlassian Cloud login, is the takeover path above, not a VPN install.</p>
<p>iOS can watch and take over a stuck login. It cannot set Always allow, and it cannot show a routine webhook URL. If the desktop is black and the phone on the same account still works, do not Reset. You can finish the login from the phone, or Recover the desktop, without deleting bots.</p>
<p>An approval card that timed out is the approval page, not this one. Mixing them leads people to type a password into a card that was only asking to allow a shell command.</p>
'''
    faqs = [
        ("The bot never offered Take over. What do I say?",
         "Staff say to ask it to hand you the computer. Then sign in yourself. For a passkey, choose Try another way."),
        ("Can I paste the two-factor code so it goes faster?",
         "No. Official troubleshooting says not to paste a password or verification code into ordinary chat. Take over the computer, or use the secrets card when the connector shows one."),
        ("I finished the login in another window and the waiting card is still there.",
         "Answer that card, or send any chat message. Staff say the reminder does not notice that login already succeeded."),
        ("Will Reset get the bot off the login page?",
         "It might destroy unsynced work and still leave you signing in again on the new computer. Take over first. Reset is the last resort on the recover page."),
        ("The site is inside our office VPN. Can the bot join it?",
         "Not by installing a VPN client on the cloud computer. Staff say that can take the machine offline. Use local execution on a computer that is already on the VPN."),
    ]
    related = [
        ("/learn/computer/", "Shared computer", "How takeover and the secrets card work."),
        ("/troubleshooting/approval-stuck/", "Approval needed stuck", "A timed-out card, which is not a password prompt."),
        ("/troubleshooting/sign-in/", "Sign-in does not complete", "Your Cursor login, as opposed to a website login."),
        ("/troubleshooting/local-computer/", "Local computer", "Internal sites that the cloud machine cannot VPN into."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Hand me the computer", "https://forum.cursor.com/t/grok-bot-failed-to-open-its-computer-and-couldnt-recognize-the-issue/169179"),
        ("Waiting card", "https://forum.cursor.com/t/grok-bot-wrangler-box-auth-reminder-stays-stuck-after-auth-already-succeeded-via-another-path/170052"),
        ("VPN, SSO, passkeys", "https://forum.cursor.com/t/vpn-sso-passkey-and-yubikey-within-grokbot/170148"),
    ]
    return _render(
        "Waiting",
        "Grok Bot stuck waiting for login",
        answer,
        "/learn/computer/?utm_source=guide&utm_campaign=waiting-for-login",
        "Take over the shared computer",
        rest, faqs, related, sources,
    )


FIXES = [
    ("/troubleshooting/plugin-oauth/", plugin_oauth),
    ("/troubleshooting/usage-limit/", usage_limit),
    ("/troubleshooting/dns-error/", dns_error),
    ("/troubleshooting/install-failed/", install_failed),
    ("/troubleshooting/update-failed/", update_failed),
    ("/troubleshooting/phone-not-connecting/", phone_not_connecting),
    ("/troubleshooting/uninstall/", uninstall),
    ("/learn/is-grok-bot-free/", is_free),
    ("/troubleshooting/linux-setup/", linux_setup),
    ("/troubleshooting/local-computer/", local_computer),
    ("/troubleshooting/routine-did-not-run/", routine_did_not_run),
    ("/troubleshooting/approval-stuck/", approval_stuck),
    ("/troubleshooting/attachment/", attachment),
    ("/troubleshooting/sign-in/", sign_in),
    ("/troubleshooting/waiting-for-login/", waiting_for_login),
]
