# -*- coding: utf-8 -*-
"""Long-form download and fix pages for proven Grok Bot search intents.

Each page owns one job. Facts are limited to official docs and the failure
notes already reviewed for this handbook (fetch day 2026-09-20). No new
product behavior is invented here.
"""
from html import escape

DOC_START = "https://docs.x.ai/grok-bot/get-started"
DOC_TROUBLE = "https://docs.x.ai/grok-bot/troubleshooting"
CURSOR_START = "https://cursor.com/help/grok-bot/getting-started"
CURSOR_RECOVER = "https://cursor.com/help/grok-bot/computer-recovery"
CURSOR_PLANS = "https://cursor.com/help/grok-bot/plans"
STORE = "https://x.ai/bot"
APP_STORE = "https://apps.apple.com/us/app/grok-bot/id6794501026"
PLAY = "https://play.google.com/store/apps/details?id=ai.x.grok.bot"
SUPPORT = "mailto:hi@cursor.com"


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


def _page(kicker, h1, lede_html, body_html, faqs, related, sources):
    return (
        '<section class="band"><div class="wrap prose">'
        '<p class="kicker">%s</p><h1>%s</h1>%s%s%s%s%s'
        "</div></section>"
        % (escape(kicker), escape(h1), lede_html, body_html, _faq_html(faqs), _related(related), _sources(sources))
    )


MAC_FAQS = [
    ("Where is the Intel Mac download? The top button gave me Apple silicon.",
     "Cursor staff confirmed the primary Download for macOS button on x.ai/bot is the Apple silicon build. Scroll to Download Grok Bot, then More downloads, for Intel. About This Mac: Chip means Apple silicon, Processor means Intel."),
    ("How do I know if my Mac is Apple silicon or Intel?",
     "Open the Apple menu, then About This Mac. Chip means Apple silicon (M1 or later). Processor with an Intel name means the Intel build. Download the matching file."),
    ("macOS says the app is not supported. Is Grok Bot unavailable on Mac?",
     "Usually you opened the wrong chip package, or a file that did not come from x.ai/bot. Delete that file and download the matching official package. Both Apple silicon and Intel are listed on the official FAQ."),
    ("The Mac window is white after install. Should I download it again?",
     "Reinstall alone does not clear local config. Fully quit from the menu bar, rename ~/Library/Application Support/Grok Bot to Grok Bot.bak, then open the app again."),
]

WINDOWS_FAQS = [
    ("Where is the Grok Bot Windows download?",
     "On x.ai/bot. Choose x64 or Arm64 to match Settings, System, About, System type. Do not use a repackaged installer from somewhere else."),
    ("What if Installed apps shows Grok Bot twice?",
     "Uninstall the older copy and keep the latest. Then quit Grok Bot from the system tray, not only by closing the window, and open it once."),
    ("The Windows app ignores my proxy. What do staff say to try?",
     "Staff reports say the app does not follow the system HTTP proxy. People who needed a tunnel used TUN mode, which captures traffic at the adapter. Do not install a VPN inside the Agent Computer."),
    ("Windows setup ends on Can't reach your computer. Is that a bad install?",
     "Often it is DNS, a VPN, antivirus HTTPS scanning, or an expired plan that the app mislabels. Follow the can't-reach walkthrough before you Reset."),
]

PHONE_FAQS = [
    ("Is there an official Grok Bot iPhone app?",
     "Yes. The App Store listing is Grok Bot, and the xAI FAQ says iPhone needs iOS 18 or later. The same iOS app runs on iPad with iPadOS 18 or later."),
    ("Where do I download Grok Bot for Android?",
     "Google Play, package ai.x.grok.bot. The FAQ lists Android 9 or later. Official @bot pointed at that listing on 2026-09-02."),
    ("Does the phone get its own computer?",
     "No. Phone and desktop share one Cursor account, one roster, and one cloud computer. macOS and iOS also share one weekly usage bucket."),
    ("What still has to be done on the desktop app?",
     "Always allow for local execution, Teach a task, and the routine webhook URL plus sender key are desktop-only. Canva often fails on iOS; connect it on desktop and it syncs."),
]

LOGIN_FAQS = [
    ("Does Grok Bot have its own account?",
     "No. The welcome screen is Get started or Sign in with Cursor. The Cursor account holds the plan, the plugins, and the weekly usage."),
    ("Which Cursor account should I use?",
     "The one that will be billed. macOS and iOS share that account's weekly usage. A work account and a personal account do not merge rosters."),
    ("The browser popup never returns to the app. What should I do?",
     "Finish the Cursor page in that popup, including org SSO if your company requires it. Then fully quit Grok Bot and open it again. Do not create a second Cursor user to skip the popup."),
    ("After a password change the Mac app says the account is unavailable.",
     "That is usually a stale session, not a missing plan. Log out from that screen, fully quit, and sign in again."),
]

NOT_RESPONDING_FAQS = [
    ("Grok Bot is not responding. What do I check first?",
     "The computer status. A bot cannot finish a turn while the screen says Reconnecting or Couldn't reach Grok Bot's computer. If the computer is connected, then check Usage. Reset does not fix either case."),
    ("The app never said I hit a limit. Can that still be usage?",
     "Yes. iOS and desktop often omit the usage-limit notice. The Cursor usage screen is the source of truth. Spillover into On-Demand can also start with no in-app warning."),
    ("Will Reset make silent bots talk again?",
     "Do not Reset while the computer view still opens. Reset rebuilds from the last snapshot and can drop unsynced work. The box is often healthy."),
    ("Every bot says Bot failed to respond on my phone and my computer. Now what?",
     "If that lasts for hours and the computer screen is still visible, ask Cursor support before Reset. Include the version, OS, time, and conversation id. Do not send passwords or keys."),
]

STUCK_FAQS = [
    ("Grok Bot is stuck on Connecting and never finishes. What fixes that?",
     "New accounts that never saved Privacy Mode (not Legacy) on the Cursor dashboard can sit on Connecting forever. Save that choice, fully quit, and reopen. Retry, Recover, and Reset do not help until it is saved."),
    ("It is stuck on Setting up your Grok Bot. Is my network down?",
     "A free Cursor plan never gets a hosted computer, and the app can spin forever. That is a missing seat, not DNS. A team admin role alone is also not a seat."),
    ("Reset is stuck on Cleaning up. Should I Reset again?",
     "No. The backend has often already finished. Fully quit, then Recover. Resetting again is how people lose unsynced work."),
    ("Setup stopped at 50 percent Starting. Are my bots deleted?",
     "Staff describe this as a server-side bad state. Wait a few minutes. Bot data is usually still there. Do not stack another Reset on top."),
]

REACH_FAQS = [
    ("What does Can't reach your computer actually mean?",
     "The app cannot open the hosted computer's address. Chat may still work. The same sentence is also a known display bug when a trial or plan has ended and Retry or Recover fail because access is gone."),
    ("Which DNS should I try?",
     "Staff repeatedly point at 1.1.1.1 and 8.8.8.8, on both IPv4 and IPv6. A router can keep handing out the ISP resolver. Compare with a phone hotspot on another carrier before you Reset."),
    ("My browser works. Why doesn't Grok Bot?",
     "Antivirus HTTPS scanning swaps the certificate issuer. Grok Bot trusts public certificate authorities only. Turn off encrypted-connection scanning or exclude the app, fully quit, and reopen."),
    ("Desktop is stuck and iOS still works. Should I Reset?",
     "No. That split is a clue the bots are still there. Prefer Recover or Update, or wait for an official rebuild if the desktop is black. Reset can delete bots."),
]

WHITE_FAQS = [
    ("Grok Bot opens to a white screen. Will reinstalling fix it?",
     "Not by itself. Fully quit, rename ~/Library/Application Support/Grok Bot to Grok Bot.bak, and relaunch. That local config survives a reinstall."),
    ("The roster is empty. Were the bots deleted?",
     "Often no. Open Hidden Bots, and check the same Cursor account on the phone. Hide from sidebar does not delete a bot. Sleep can also show an empty list while the computer wakes. Do not Reset to look for them."),
    ("It looks like a brand-new account after a rebuild. Should I create a first Bot?",
     "No. Logging in while the computer is still starting shows the first-run screen. Fully quit and come back when the computer is up. Do not create a bot in that window."),
    ("The spinner is black and I am on the free Cursor plan.",
     "No hosted computer was provisioned. That is not your network and not a broken download. You need a plan that includes Grok Bot, or a real seat on a team."),
]

RECOVER_FAQS = [
    ("What is the difference between Update, Recover, and Reset?",
     "Update and Recover keep synced bots, files, and logins, and both remove installed apps on the computer. Reset keeps only the last snapshot, so recent unsynced bots and files can disappear. Reset is last."),
    ("Does Reset delete chat history?",
     "Chat history lives outside the computer. Reset can still drop files and logins that had not synced to the latest snapshot. Do not Reset to save a trial."),
    ("The Reset window is stuck behind Settings and I cannot click it.",
     "That is a known layout bug. Do not keep clicking blind. Fully quit the app. If you have not confirmed the computer is actually dead, stop and use the less destructive step."),
    ("When should I email support instead of pressing Reset?",
     "When Can't reach survives Recover, Reset, and reinstall for days, or every bot fails across phone and desktop while the computer is still visible. Email hi@cursor.com with version, OS, the exact line, the bot name, time and timezone, and the request id."),
]


def mac_download():
    lede = '''
<p class="meta">Official Mac path from <a href="%s">Get started</a> and the xAI FAQ (fetched 2026-09-20). This page is the Mac download. All platforms: <a href="/learn/install/">install</a>. This site does not host the file.</p>
<div class="callout">
<p><strong>Intel Mac: skip the top Download for macOS button.</strong> Cursor staff confirmed that button is Apple silicon (forum, 2026-08-19). Scroll to Download Grok Bot, then <strong>More downloads</strong>, and take Intel. Chip in About This Mac means Apple silicon; Processor means Intel. The file is only on <a href="%s">x.ai/bot</a>. This site does not host it.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="%s">Download on x.ai/bot</a>
  <a class="btn btn-secondary" href="/learn/login/">Sign in with Cursor</a>
  <a class="btn btn-ghost" href="/pricing/">See if your plan includes it</a>
</div>
''' % (DOC_START, STORE, STORE)
    body = '''
<h2>Check the chip before you download</h2>
<p>A Mac download fails in a boring way: the file is fine, and it is the wrong file. Open the Apple menu and choose About This Mac. Read the chip line before you click anything on the product page.</p>
<ul>
<li><strong>Chip</strong> says Apple M1, M2, M3, M4, or a later M-series name. Download the Apple silicon build.</li>
<li><strong>Processor</strong> names an Intel chip. Download the Intel build.</li>
<li>Do not guess from the year on the laptop lid. Apple sold Intel and Apple silicon machines in overlapping years.</li>
</ul>
<p>Both chips are official. The trap is which control downloads which file. People who follow a docs link and click the big macOS button on an Intel Mac get “app is not supported,” then download the same arm64 file again. Delete that dmg. Go back to x.ai/bot, scroll past the hero, open More downloads, and take Intel. Do not search for a patched build.</p>
<p>The Homebrew cask <code>grok-bot</code> installs the same app and, when checked on 2026-09-22, was version 0.56.1 and required macOS 12 or later. xAI’s Get started page does not publish a minimum macOS version, so treat 12 as the cask’s requirement. The cask will not show you the chip choice. If you need to see Apple silicon versus Intel, use the product page. A mirror dmg is still the wrong file.</p>
<h2>Install it the way the docs describe</h2>
<ol>
<li>Download the matching package from x.ai/bot. If the browser offers a third-party host, close it and start again from the product page.</li>
<li>Open the dmg. Drag Grok Bot into Applications. Do not keep launching the copy that sits inside the mounted disk image. Updates and a clean quit both assume the app lives in Applications.</li>
<li>Eject the disk image. Open Grok Bot from Applications.</li>
<li>If macOS asks you to confirm, choose Open. That prompt is Gatekeeper on a downloaded app, not a Grok Bot error code.</li>
<li>If the app is blocked with no Open button, go to System Settings, then Privacy and Security, and use Open Anyway for Grok Bot. Then open it from Applications again.</li>
</ol>
<p>If macOS says the app is damaged, do not hunt for a patched copy. A damaged-app warning on a fresh download usually means the file was altered, blocked, or not the official build. Trash it and download again from x.ai/bot. This handbook will not give you a quarantine-removal command. The safe path is a clean official file plus the Open button.</p>
<h2>Sign in, then stop</h2>
<p>On the welcome screen choose Get started, or Sign in with Cursor. Finish Cursor in the browser popup, including company SSO if the account requires it, and return to the app. The first-run questions about tools you use only change suggestions. They do not connect those tools. The computer initializes in the background. The last screen is Meet a future teammate. Do not create twelve bots on that screen.</p>
<p>Before the popup, confirm three things. The Cursor account is one that includes Grok Bot, or you are ready to link personal SuperGrok on that same email. Cursor is not left on Legacy Privacy Mode; switch to Privacy Mode and save it, or a new account can sit on Connecting forever. You have one real task ready, because an empty demo still spends trial usage. The login page walks through a popup that never returns. Plan conflicts stay on the pricing snapshot, which does not invent list prices.</p>
<h2>Quit means the menu bar</h2>
<p>Closing the Mac window leaves Grok Bot running. When a step says fully quit, use the menu-bar Quit, or the equivalent Quit item, then open the app again. A half-closed window is why a retry looks like it did nothing. The same rule shows up in almost every Mac failure report staff answered: quit, then reopen, before Recover, and long before Reset.</p>
<h2>White window on first open</h2>
<p>A fresh Mac install can open to a white window that never draws the roster. Reinstalling does not clear the local config that causes it. Fully quit from the menu bar. In Finder, choose Go, then Go to Folder, and open <code>~/Library/Application Support/</code>. Rename the folder <code>Grok Bot</code> to <code>Grok Bot.bak</code>. Open the app from Applications again. Keep the .bak folder until the roster loads, then delete it only if you do not need anything that was stored locally. The full blank-screen split, including a black spinner and an empty roster after sleep, is on the white-screen page. Do not Reset a Mac just because the first window was white.</p>
<h2>When the download worked and the product still will not start</h2>
<p>A successful Mac install can still stop on a sentence. Match the sentence instead of downloading a third time.</p>
<ul>
<li><strong>Connecting</strong> that never ends, especially on a new Cursor account: save Privacy Mode, quit, reopen. That is the stuck page.</li>
<li><strong>Setting up</strong> forever on a free plan: no computer was provisioned. A download cannot fix a missing seat.</li>
<li><strong>Can't reach your computer</strong> or <strong>Reconnecting</strong>: DNS, VPN, or antivirus scanning. The can't-reach page is the test order. If the same account still works on iPhone, the bots are not gone. Do not Reset.</li>
<li><strong>Not responding</strong> after the computer view opens: often weekly usage. Check the meter before you touch the computer buttons.</li>
</ul>
<p>Mac and iPhone share one weekly usage bucket on the same Cursor account. Installing the phone app does not give you a second pool or a second computer. Linux and Windows are separate downloads from the same product page. They are not a fallback when the Mac chip package was wrong.</p>
'''
    related = [
        ("/", "Grok Bot guide", "First job, shared computer, and the reading order."),
        ("/learn/install/", "All-platform install", "Windows, Linux, phone, and the same Cursor login."),
        ("/learn/login/", "Cursor login", "No second account, SSO, and a stale session after a password change."),
        ("/troubleshooting/white-screen/", "White or black screen", "Local config, sleep, and the fake new-user window."),
        ("/learn/first-bot/", "First Bot", "One job after the roster appears. Stop at a draft."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("x.ai/bot", STORE),
        ("Intel build is under More downloads", "https://forum.cursor.com/t/grok-bot-w-cursor-ultra-on-intel-chip-mac/168752"),
        ("Homebrew cask grok-bot", "https://formulae.brew.sh/cask/grok-bot"),
        ("White screen after open", "https://forum.cursor.com/t/grok-bot-shows-white-screen-upon-opening-and-is-unusable/169815"),
    ]
    return _page("Mac download", "Download Grok Bot for Mac: the top button is Apple silicon", lede, body, MAC_FAQS, related, sources)


def windows_download():
    lede = '''
<p class="meta">Windows steps from <a href="%s">Get started</a> and staff notes on double installs, proxies, and tunnels. Fetched 2026-09-20. Mac steps: <a href="/learn/mac-download/">Mac download</a>. The installer itself is only on <a href="%s">x.ai/bot</a>.</p>
<div class="callout">
<p><strong>One official installer, one installed copy.</strong> Pick x64 or Arm64 from x.ai/bot. If Windows already lists Grok Bot twice, remove the older one before you debug the network.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="%s">Download on x.ai/bot</a>
  <a class="btn btn-secondary" href="/learn/login/">Sign in with Cursor</a>
  <a class="btn btn-ghost" href="/troubleshooting/cant-reach/">Can't reach after install</a>
</div>
''' % (DOC_START, STORE, STORE)
    body = '''
<h2>Pick x64 or Arm64 on purpose</h2>
<p>Open Settings, then System, then About, and read System type. That line is the whole architecture choice. x64 is the usual 64-bit Intel or AMD PC. Arm64 is a Windows on Arm machine. The product page offers both. The FAQ lists Windows on x64 and Arm64, so a failed launch is not evidence that Windows is unsupported.</p>
<p>Download only from x.ai/bot. A search result that wraps the installer in another site is how people end up with a build the app later rejects. Run the installer, then open Grok Bot from the Start menu. Sign in with Cursor in the browser popup. There is still no Grok Bot account to register on the desktop.</p>
<h2>Two copies is a stuck app</h2>
<p>Settings, then Apps, then Installed apps. If Grok Bot appears twice, uninstall the older copy and keep the latest. Close the window after that is not enough. Quit from the system tray so the leftover process dies, then open the remaining copy once. People hit Can't reach your computer on a fresh Windows profile when an older install was still registered beside the new one. Fix the duplicate before you change DNS, and before you Reset a computer that may not be the problem.</p>
<p>The same tray quit matters later. Staff tell Windows users who still have a local-exec daemon to quit from the tray, end Grok Bot and the daemon in Task Manager, wait about a minute, and re-register. That is a local-execution cleanup, not a reinstall of the cloud computer. Do not confuse it with Recover.</p>
<h2>Proxy, TUN, and company tunnels</h2>
<p>If the installer finished and the app stops at Can't reach your computer, the download is probably fine. Staff have said the computer on their side was up the whole time, and recreating it does not help, because the Windows app connects <strong>directly</strong>. It does not use the system proxy or a local HTTP proxy such as 127.0.0.1:7890. DNS and browser checks that go through the proxy can pass while the app still fails.</p>
<p>Staff test, in PowerShell, after you fully quit Grok Bot and switch the tunnel from system-proxy mode to TUN (also called Enhanced, Global, or virtual network adapter):</p>
<pre><code>curl.exe --noproxy "*" -I https://test123.us10.cursorvm.com</code></pre>
<p>A working path returns quickly with <code>HTTP/1.1 404 Not Found</code> and <code>Server: awselb/2.0</code>. The 404 is success: that hostname is only a probe, and the load balancer answered. A hang, timeout, or connection reset means the app will fail the same way. Fix TUN, then open Grok Bot. Do not install that tunnel inside the Agent Computer.</p>
<p>Do the opposite inside the product. Never install a VPN, proxy, or DNS changer on the Agent Computer. A bot-installed VPN can cut the always-on path so every bot on the account fails until Recover restores routing. A company Zscaler-style tunnel has also left Windows 11 on a black loading screen. A phone hotspot on another carrier is the clean A/B test: if the hotspot works and the office network does not, the installer is fine and the path is not. The can't-reach page has the DNS and antivirus order. Antivirus products that scan HTTPS replace the certificate issuer, and Grok Bot trusts public authorities only, so the browser can load while the app cannot.</p>
<h2>What a finished install looks like</h2>
<p>You should get a Cursor browser popup, then a roster starting in the background, then Meet a future teammate. Tool questions on that path do not connect Gmail, GitHub, or anything else. If the popup never completes, use the login page. If the screen says Connecting and never leaves, save Privacy Mode on the Cursor dashboard before another reinstall. If it says Setting up and you are on a free Cursor plan, the hosted computer was never created. Downloading the exe again will not provision a seat.</p>
<p>The app checks for updates on its own. Settings → Updates → Check for Updates, then Restart to Update, replaces the desktop app. It does not reset the computer. The computer update is the other control in that same screen, Update under Grok Bot's Computer. You do not need a forum installer to get the current build. A white window that survives reinstall can be local config: fully quit, and rename <code>%APPDATA%\\Grok Bot</code> to <code>Grok Bot.bak</code>, the Windows twin of the Mac Application Support folder. Linux packages are under More downloads on the same product page.</p>
<h2>After Windows is open</h2>
<p>Use one bot and one cited job. The first-bot lesson is the short brief. If bots later go silent while the computer view still opens, that is weekly usage more often than a broken Windows install. Uninstalling Windows will not refill the meter. Pricing explains which plans include access, without invented dollar amounts.</p>
'''
    related = [
        ("/", "Grok Bot guide", "Start here if the app is not installed yet."),
        ("/learn/install/", "Install overview", "Official packages for every platform, then Cursor login."),
        ("/learn/mac-download/", "Mac download", "Apple silicon versus Intel, Gatekeeper, and the white window."),
        ("/troubleshooting/cant-reach/", "Can't reach your computer", "DNS, hotspot, antivirus scanning, and when not to Reset."),
        ("/tools/linux-port/", "Linux packages", "Official deb, rpm, and AppImage versus community ports."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("x.ai/bot", STORE),
        ("Windows fresh profile, can't reach", "https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281"),
        ("Zscaler and a black screen", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-on-windows-11/170294"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Windows download", "Download and install Grok Bot on Windows", lede, body, WINDOWS_FAQS, related, sources)


def phone_download():
    lede = '''
<p class="meta">Store links and limits from the xAI FAQ and Cursor Help, fetched 2026-09-20. Desktop packages stay on <a href="%s">x.ai/bot</a>. Phone does not replace the Mac or Windows install when you need Teach a task or Always allow.</p>
<div class="callout">
<p><strong>iPhone, iPad, and Android are official.</strong> Same Cursor login, same roster, same cloud computer. The phone is not a second machine and not a private login.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="%s">iPhone and iPad on the App Store</a>
  <a class="btn btn-secondary" href="%s">Android on Google Play</a>
  <a class="btn btn-ghost" href="%s">Desktop on x.ai/bot</a>
</div>
''' % (STORE, APP_STORE, PLAY, STORE)
    body = '''
<h2>Which store, and which OS version</h2>
<p>Download the phone apps from the stores, not from a file host. iPhone uses the App Store listing named Grok Bot. The FAQ says iOS 18 or later. That same iOS app runs on iPad with iPadOS 18 or later. Launch-day iPhone-only is out of date. Android is Google Play, package id <code>ai.x.grok.bot</code>, Android 9 or later. Official @bot pointed at that Play listing on 2026-09-02. If a search result sends you to a different Android package name, close it.</p>
<p>Install, open the app, and sign in with the Cursor account you already use on the desktop, or the account you want usage to land on. There is no phone-only Grok Bot user. Org SSO is the same Cursor org flow. After login, the roster and the computer sync. Closing the phone does not stop cloud turns or routines, just as closing the laptop does not.</p>
<h2>What the phone is for</h2>
<p>On the phone you can chat, watch the computer, take over when a login or two-factor prompt is stuck, and open Plugins from the top-left avatar. That is enough to approve a draft on a train or to see whether bots are alive while the desktop app is having a bad day. It is not enough to pretend the laptop install failed and the phone is a full replacement.</p>
<div class="table-wrap"><table>
<thead><tr><th>Job</th><th>Phone</th><th>Desktop</th></tr></thead>
<tbody>
<tr><td>Chat, watch the computer, take over a stuck login</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Plugins from the avatar</td><td>Yes, with limits</td><td>Yes</td></tr>
<tr><td>Always allow for local execution</td><td>No. iOS can approve one shot</td><td>Yes. The choice stays on that desktop</td></tr>
<tr><td>Teach a task (screen recording, no mic)</td><td>No</td><td>Yes</td></tr>
<tr><td>Routine webhook URL and sender key</td><td>No. Staff say these are desktop-only</td><td>Yes</td></tr>
<tr><td>Canva connector</td><td>Often fails. Connect on desktop; it syncs</td><td>Yes</td></tr>
</tbody>
</table></div>
<p>Read that table before you reinstall the desktop app because a phone button is missing. The missing button is the product split, not a corrupt phone install. Local stdio MCP on the laptop is still unreachable from the cloud computer no matter which phone you add. Connectors are account-level. Prefer a connector over asking the bot to click the website, on phone or desktop.</p>
<h2>The phone as a test when the desktop looks dead</h2>
<p>If the Mac or Windows preview is black, or stuck on Reconnecting, and the same Cursor account still works on the phone, the bots were not deleted. Prefer Recover or Update on the desktop. Reset from panic can delete bots. If desktop and phone are both stuck, including the phone on cellular, staff often call that server-side: hold off on Reset, Recover, Update, and signing out until you have a reason beyond the spinner. Days of Can't reach after you have already recovered, reset, and reinstalled usually mean a stuck hosted computer that only staff can restore.</p>
<p>The other direction matters too. A silent roster on both phone and desktop, while the computer view still opens, is often the weekly meter. macOS and iOS share one usage bucket. Installing the iPhone app does not refill it. The not-responding page is the check. Do not delete the phone app to fix a full meter.</p>
<h2>Deleting the app is not a reset button</h2>
<div class="callout warn">
<p><strong>iOS Delete Account deletes the Cursor account</strong>, plus agents, chats, and the computer. Desktop sign-out only signs out. There is no separate Grok Bot account to delete. Use Cursor Help if you meant to leave the device, not the account. This site cannot undo that deletion.</p>
</div>
<p>After a normal install, go back to one job on the desktop or the phone. The first-bot brief is the same on both. Pricing is where plan and SuperGrok linking live. Linking SuperGrok is a usage grant on that Cursor email, and you cannot unlink it yourself later.</p>
'''
    related = [
        ("/", "Grok Bot guide", "What the product is, then the first reversible job."),
        ("/learn/install/", "Desktop install", "Mac, Windows, and Linux packages plus the same login."),
        ("/learn/mac-download/", "Mac download", "Use the phone test if the Mac screen is black."),
        ("/troubleshooting/not-responding/", "Not responding", "Shared weekly usage when both phone and desktop go quiet."),
        ("/learn/computer/", "Shared computer", "One machine. The phone does not isolate a life bot from a work bot."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("App Store", APP_STORE),
        ("Google Play", PLAY),
        ("Cursor getting started", CURSOR_START),
        ("Canva on iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
        ("iOS cannot Always allow", "https://forum.cursor.com/t/authorization-death-by-1000-clicks/170087"),
    ]
    return _page("Phone download", "Download Grok Bot for iPhone, iPad, and Android", lede, body, PHONE_FAQS, related, sources)


def login_page():
    lede = '''
<p class="meta">Login facts from <a href="%s">Get started</a> and <a href="%s">Cursor getting started</a>. Fetch day 2026-09-20. The packages are on <a href="/learn/install/">install</a>. Plan names and conflicts are on <a href="/pricing/">pricing</a>, not on this page.</p>
<div class="callout">
<p><strong>Sign in with Cursor.</strong> Grok Bot does not have a password of its own. The account you pick is the account that holds the plan, the plugins, and the weekly usage.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/install/">Get the official app</a>
  <a class="btn btn-secondary" href="%s">Product page</a>
  <a class="btn btn-ghost" href="/learn/cursor/">Cursor and Grok Bot</a>
</div>
''' % (DOC_START, CURSOR_START, STORE)
    body = '''
<h2>There is nothing to register</h2>
<p>People search for a Grok Bot login because the download finished and the next screen looks like a new product. It is the same Cursor user you already have, opened in a different app. Grok Bot is not a panel inside the Cursor IDE, and it is not grok.com. You do not create a Grok Bot email, and you do not paste an API key into the welcome screen to finish setup.</p>
<p>Official sign-in, from troubleshooting re-read 2026-09-22, when the popup seems to die:</p>
<ol>
<li>Keep Grok Bot open while authentication runs in the browser.</li>
<li>Confirm the browser shows a successful Cursor sign-in.</li>
<li>Return to the app yourself if it does not regain focus.</li>
<li>Try Get started, or Sign In with Cursor from Settings, again.</li>
<li>Confirm the account has Grok Bot access. An error about Legacy Privacy Mode means the data setting does not allow the storage Grok Bot needs. Change it on the Cursor account, or ask the org admin. Reset will not change that setting.</li>
</ol>
<p>If your company requires SSO, complete the org flow in that browser. Do not open a personal Cursor account beside the work account. Those are two users, two meters, and two computers, and they do not share a roster.</p>
<p>If access is a SuperGrok subscription, link it when the app asks. On desktop, Settings → Usage &amp; Billing offers Link SuperGrok Heavy. The label names the tier that applies to your account. On iPhone and Android the access screen offers Link Grok Account, then Finished Linking? Refresh My Status. Linking is not a second Grok Bot account.</p>
<p>When the popup closes, you should be back in the app. First-run introduces bots, the shared computer, and routines, and asks which tools you use often. Those answers only affect suggestions. They do not connect Gmail, Slack, or GitHub. Connecting a tool is a later plugin step. The computer initializes in the background. The last screen is Meet a future teammate.</p>
<h2>Pick the account that will pay</h2>
<p>Cursor Help is explicit: sign in with the Cursor account that will bear the usage. macOS and iOS share one weekly bucket on that account. If you sign the phone into a different Cursor user than the laptop, you will think sync is broken. It is not syncing because it is not the same user. Team admin on a company account is also not a seat. Assign yourself a Standard or Premium seat, or switch to an account that has one, before you blame the popup.</p>
<p>A free Cursor plan can sit on Setting up forever. Staff describe that as a copy bug: without a paid seat the hosted computer is never provisioned. Retry will not create the computer. The pricing page is the dated snapshot of which plans include Grok Bot and how SuperGrok linking works. Linking personal SuperGrok or X Premium+ is a usage grant, not a second subscription, and once linked you cannot unlink it or move it to another Cursor account yourself.</p>
<h2>Save Privacy Mode or Connecting never ends</h2>
<p>Grok Bot needs cloud storage. If the Cursor account is still on Legacy Privacy Mode, switch to Privacy Mode and explicitly save it on the Cursor dashboard. New accounts that never save that choice can sit on Connecting forever. Retry, Recover, and Reset all fail until the choice is saved. Fully quit the app after you save it, then open and sign in again. This is the single most common reason a brand-new login looks like a dead download.</p>
<h2>When the popup or the session is the bug</h2>
<ul>
<li><strong>The popup never hands you back.</strong> Finish the Cursor page, including any SSO redirect. Fully quit Grok Bot (menu-bar Quit on macOS, tray quit on Windows) and reopen. Do not create a second account.</li>
<li><strong>Password change, then Account unavailable.</strong> Usually a stale session. Log out from that screen, fully quit, and sign in again. Spending still showing SuperGrok on the web does not mean the desktop session refreshed.</li>
<li><strong>Can't reach your computer right after login.</strong> Sometimes the network. Sometimes an expired trial that the app mislabels as a network error. Retry and Recover fail because access ended. Pick a plan that includes Grok Bot, or link SuperGrok on the same email, then quit and reopen. The app should say access ended. The network wording is a known display bug.</li>
<li><strong>You wanted to leave, and you tapped Delete Account on iOS.</strong> That deletes the Cursor account plus agents, chats, and the computer. Desktop only signs out. There is no smaller Grok Bot account underneath.</li>
</ul>
<h2>After login, do one job</h2>
<p>A finished login is a roster on one shared computer, not a finished setup of twelve specialists. Go to the first-bot lesson and paste a brief that stops at a draft. If the roster is missing and the window is white or black, that is the white-screen page, not a second login. If bots accept messages and never answer, check usage before you sign out and back in. Signing out does not refill the weekly pool.</p>
'''
    related = [
        ("/", "Grok Bot guide", "The product split, then a first job you can check."),
        ("/learn/install/", "Download and install", "Official Mac, Windows, Linux, and phone packages."),
        ("/learn/cursor/", "Cursor and Grok Bot", "One account, two apps. Not an IDE sidebar."),
        ("/learn/mac-download/", "Mac download", "Chip choice and Gatekeeper before the login screen."),
        ("/pricing/", "Plans", "Which accounts include Grok Bot, without invented prices."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("Cursor getting started", CURSOR_START),
        ("Link SuperGrok", "https://cursor.com/help/grok-bot/supergrok"),
        ("Stale session after password change", "https://forum.cursor.com/t/grok-bot-mac-blocked-after-password-change-app-says-unavailable-spending-shows-supergrok-plus/170389"),
        ("Free plan stuck on Setting up", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
    ]
    return _page("Login", "Sign in to Grok Bot with your Cursor account", lede, body, LOGIN_FAQS, related, sources)


def not_responding():
    lede = '''
<p class="meta">Silent bots, from <a href="%s">plans and billing</a> and staff posts. The computer can be healthy while every bot looks dead. Short index: <a href="/troubleshooting/">Grok Bot not working</a>. Do not start with Reset.</p>
<div class="callout warn">
<p><strong>Read the computer line before the usage meter.</strong> Official help: a bot cannot finish a turn while the computer says Reconnecting or Couldn't reach Grok Bot's computer. Retry, do not Reset, then send again. If the computer is connected and the same prompt still fails, that is a support report, not a Reset. A full weekly meter is the other silence, and Reset will not refill it.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/cost-and-pitfalls/">How weekly usage works</a>
  <a class="btn btn-secondary" href="/pricing/">If access actually ended</a>
  <a class="btn btn-ghost" href="/troubleshooting/stuck/">Stuck on a spinner instead</a>
</div>
''' % CURSOR_PLANS
    body = '''
<h2>Three different failures share this search</h2>
<p>Grok Bot not responding is what people type for three different screens. Cursor Help’s own order is computer status first, then the prompt, then support. Usage is the field case that the banner often hides. Do them in this order.</p>
<ol>
<li><strong>The app is open, the computer view loads, and bots do not answer.</strong> Stay on this page. This is the usage case.</li>
<li><strong>The app is stuck on Connecting, Setting up, Cleaning up, or a percent bar.</strong> That is the stuck page. Usage is not the first test.</li>
<li><strong>The words on screen are Can't reach your computer, Reconnecting, or a blank desktop.</strong> That is the can't-reach page, unless the computer view still works and only the replies are missing.</li>
</ol>
<p>A white or black window with no roster is the white-screen page. Reinstalling from x.ai/bot does not answer a silent bot, and it does not clear a full meter.</p>
<h2>Confirm the computer is actually there</h2>
<p>Open the computer view. If it loads a desktop, the hosted machine is up. Staff and the billing notes treat this split as the whole diagnosis: silent bots with the computer still visible are weekly usage, not a dead box. Messages may still send. You see your bubble. No reply runs. iOS and the desktop app often skip the sentence usage limit reached, so the absence of a banner proves nothing. Dual banners, when they do appear, are usually blocked retries, not two bills.</p>
<p>Check Settings, then Usage, in the app, or the Cursor dashboard. Read the meter and the weekly reset time. Do this before Recover, Update, or Reset. Those three buttons change the computer. They do not add usage. Pro's Other Models amount is not the Grok Bot weekly pool. Cloud Agents that a bot launches bill Cursor plan usage separately. If you only look at the IDE usage chart, you can miss the bot pool and reset a healthy computer.</p>
<h2>If the meter is full</h2>
<p>You have two honest options. Neither one is Reset.</p>
<ul>
<li><strong>Wait</strong> for the weekly reset shown on the usage screen. Routines that came due during the block were skipped. They do not queue up and run later as a surprise batch of sends. Messages you already sent during the block reply in a batch once usage is available again.</li>
<li><strong>Resume now</strong> by enabling On-Demand on the same Cursor account and setting a spend limit you accept. Bots should reply within a couple of minutes. The app may not warn you in the chat before paid spillover starts. If you do not want paid spillover, set the On-Demand cap to $0. That stops the paid tier. It does not stop promo or referral credits from being drained first. Charge order is weekly pool, then credits, then paid On-Demand.</li>
</ul>
<p>Shrink routine windows while you are here. Delete idle specialist bots that poke each other. Every bot-to-bot message counts against the weekly pool, including review threads you asked them to stop. Telling a bot stay quiet in chat does not freeze the meter if a routine or another bot is still talking. The cost page is the longer version of this trap. This page is only the decision when the symptom is silence.</p>
<h2>If the meter is not full</h2>
<p>Then it is not the weekly pool, and you still should not Reset first. Work through the less destructive list. Fully quit the app and reopen. On macOS that is menu-bar Quit. On Windows, quit the tray. If one connector action hangs and the rest of the roster is fine, that is a plugin failure, not a dead computer. Zoom error 4700, Notion redirect, Gmail, Canva on iOS, X, and a broken GitHub header each have their own note on the troubleshooting index. Do not paste a bearer token into chat to get around them.</p>
<p>If every bot says Bot failed to respond or Couldn't send your message for hours, on the phone and on the desktop, while the computer screen is still visible, stop. Ask support before Reset. Reset rebuilds from the last snapshot and can drop the newest unsynced edits. Email hi@cursor.com with the Grok Bot version, the OS, the exact error line, the bot or routine name, the time and timezone, the request or conversation id, and what you already tried. Do not attach passwords, codes, or keys.</p>
<h2>Trial ended is silence of a different kind</h2>
<p>An exhausted trial does not delete data. Bots stop answering, and the computer view can still export. Do not Reset to save a trial. Expired access can also wear the Can't reach your computer label even though the cause is the plan. If Retry and Recover fail and the account no longer includes Grok Bot, pick a plan that includes it or link SuperGrok on the same email, then fully quit and reopen. Pricing keeps the dated plan notes. This page will not invent a price.</p>
'''
    related = [
        ("/", "Grok Bot guide", "If you are not installed yet, start with the download, not Reset."),
        ("/troubleshooting/", "Not working index", "Every symptom card, including plugins and Linux."),
        ("/learn/cost-and-pitfalls/", "Usage and On-Demand", "Pool, credits, and the week-burning habits."),
        ("/troubleshooting/cant-reach/", "Can't reach", "Use this when the computer view itself will not open."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "What each button keeps, after you know it is not usage."),
    ]
    sources = [
        ("Plans and billing", CURSOR_PLANS),
        ("No warning before On-Demand", "https://forum.cursor.com/t/grok-bot-gives-no-warning-before-weekly-usage-spills-into-paid-on-demand/169679"),
        ("Bot-to-bot reviews burn the week", "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"),
        ("Trial still exportable", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Not responding", "Grok Bot not responding: computer first, then usage", lede, body, NOT_RESPONDING_FAQS, related, sources)


def stuck():
    lede = '''
<p class="meta">Progress labels that never finish, from official troubleshooting and staff posts. Fetch context 2026-09-20. If bots are merely silent, use <a href="/troubleshooting/not-responding/">not responding</a>. If the sentence is Can't reach, use <a href="/troubleshooting/cant-reach/">that test</a>.</p>
<div class="callout">
<p><strong>If the label is still changing, wait.</strong> xAI says initial setup and an image update can take several minutes. Keep the app open until Starting your computer or Updating your computer finishes. Retry, restart, and Update are for when progress stops or fails. A moving bar is not a Reset.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/login/">Login and Privacy Mode</a>
  <a class="btn btn-secondary" href="/pricing/">Missing seat or ended trial</a>
  <a class="btn btn-ghost" href="/troubleshooting/recover-vs-reset/">Recover versus Reset</a>
</div>
'''
    body = '''
<h2>Read the label, then do one thing</h2>
<p>Grok Bot stuck is not a single defect. Write down the label. If it still changes, stop reading and leave the app open. Official order once it fails or freezes: Retry from the error, restart Grok Bot, check for an app update (Settings → Updates → Check for Updates; Restart to Update does not reset the computer), then Update under Grok Bot's Computer if the machine is still unreachable. Reset is only after those fail.</p>
<div class="table-wrap"><table>
<thead><tr><th>Label you see</th><th>What staff say it usually is</th><th>First move</th></tr></thead>
<tbody>
<tr><td>Connecting, forever, on a new account</td><td>Privacy Mode was never saved</td><td>Save Privacy Mode on the Cursor dashboard, fully quit, reopen</td></tr>
<tr><td>Setting up your Grok Bot, or a black spinner on a free plan</td><td>No hosted computer was provisioned</td><td>A real seat or a plan that includes Grok Bot. Not a new download</td></tr>
<tr><td>Reconnecting, or Showing saved messages</td><td>DNS, while the computer may be healthy</td><td>Hotspot test, then the can't-reach page. Retry will not fix a resolver</td></tr>
<tr><td>Cleaning up, after Reset</td><td>The backend often already finished</td><td>Fully quit, then Recover. Do not Reset again</td></tr>
<tr><td>50 percent Starting</td><td>A server-side bad state</td><td>Wait a few minutes. Data is usually still there</td></tr>
<tr><td>White window, empty roster, or a fake first-run</td><td>Local config, sleep, or a computer that is still booting</td><td>White-screen page. Do not create a first bot in that window</td></tr>
</tbody>
</table></div>
<h2>Connecting that never completes</h2>
<p>This shows up on new Cursor accounts that have not saved a privacy choice. Grok Bot needs cloud storage. Legacy Privacy Mode blocks that. Switching the control is not enough: you have to save Privacy Mode (not Legacy) on the Cursor dashboard. Until that save exists, Retry, Recover, and Reset all fail, and a reinstall fails too. Fully quit after the save. On a Mac, menu-bar Quit. On Windows, the tray. Then open the app and let the login finish. The login page has the rest of the popup and SSO notes. Do not create a second Cursor user because the first one sat on Connecting for an hour.</p>
<h2>Setting up, and the black spinner that is not your Wi-Fi</h2>
<p>A free Cursor plan does not get a hosted computer. The app can spin on Setting up your Grok Bot anyway. Staff called the copy a known bug: it looks like setup, and it is a missing seat. The same black loading screen happens when someone is a team admin and never assigned themselves a Standard or Premium seat. Admin is not a computer. Download the Mac or Windows package again only after a seat exists. Until then every network test is noise. Pricing is the snapshot of which plans include access. This page does not add a free tier the product does not have.</p>
<h2>Cleaning up and 50 percent Starting</h2>
<p>These two appear after someone already pressed Reset. They feel like proof you should press it again. They are not.</p>
<p>Stuck on Cleaning up: the backend has often finished, and the desktop is waiting on a session that will not notice. Fully quit the app, reopen, and use Recover if the computer is still unreachable. Do not launch a second Reset to finish the first one. The second pass is how unsynced work disappears.</p>
<p>Stopped at 50 percent Starting: staff describe a server-side bad state. Wait a few minutes. Bot data is usually still on the account. Stacking Reset on a percent bar does not push the percent. If a status dialog looks alarming, do not click yet. Try signing in again and check the phone on cellular before you confirm anything destructive. The Reset dialog can also open behind Settings, where it is invisible and cannot be clicked. Fully quit. Do not click around the window hoping you hit the right control.</p>
<h2>Reconnecting in the middle of a session</h2>
<p>Mid-session Reconnecting, or Showing saved messages, while you have reason to think the Agent Computer is healthy, is the DNS class of bug. Retry, Recover, and Reset do not teach your resolver a name it cannot look up. A rebuilt computer lands in the same DNS zone. Go to the can't-reach page and run the hotspot test before any computer button. If the phone on another network works, you have your answer.</p>
<h2>What to collect if it is still stuck</h2>
<p>After the one move that matches the label, stop changing things. Email hi@cursor.com with the version, the OS, the exact label, the bot name if you have one, the time and timezone, and the request id if the app shows one. Say whether phone and desktop fail together. Do not send passwords, backup codes, or API keys. If both devices fail, including cellular, staff often want you to wait rather than Reset. The recover page explains what Update, Recover, and Reset each keep, for the moment a button really is the next step.</p>
'''
    related = [
        ("/", "Grok Bot guide", "Install path if you never got a roster at all."),
        ("/troubleshooting/", "Not working index", "The short cards for every symptom."),
        ("/troubleshooting/cant-reach/", "Can't reach your computer", "DNS, VPN, and antivirus when the label is Reconnecting."),
        ("/troubleshooting/not-responding/", "Not responding", "Computer is up, replies are not. Check usage."),
        ("/learn/mac-download/", "Mac download", "Wrong chip and the white window are install problems, not Reset problems."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Cursor getting started", CURSOR_START),
        ("Cleaning up hang", "https://forum.cursor.com/t/grok-bot-hanging-at-cleaning-up-phase-after-resetting/169364"),
        ("50 percent Starting", "https://forum.cursor.com/t/currently-down-grok-bot-retrying-back-end-vm/169834"),
        ("Reset window behind Settings", "https://forum.cursor.com/t/the-reset-computer-window-opens-behind-the-settings-window-and-is-invisible-and-unclickable/169177"),
        ("Privacy Mode and first setup", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
    ]
    return _page("Stuck", "Grok Bot stuck on Setting up, Starting, or Connecting", lede, body, STUCK_FAQS, related, sources)


def cant_reach():
    lede = '''
<p class="meta">Network failures and the access-ended display bug, from <a href="%s">official troubleshooting</a> and staff posts. If the computer view opens and only replies are missing, go to <a href="/troubleshooting/not-responding/">not responding</a> instead.</p>
<div class="callout warn">
<p><strong>Retry, then quit, before any DNS change or Reset.</strong> xAI’s order is Retry, restart, Recover computer when offered, then Settings → Updates → Update under Grok Bot's Computer. Bots and chats are not automatically gone. A resolver that refuses <code>cursorvm.com</code> subdomains will fail the same way after you rebuild the computer.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/troubleshooting/recover-vs-reset/">When a button is actually next</a>
  <a class="btn btn-secondary" href="/pricing/">If the trial or plan ended</a>
  <a class="btn btn-ghost" href="/learn/install/">Reinstall only the official app</a>
</div>
''' % DOC_TROUBLE
    body = '''
<h2>The button order, then the network</h2>
<p>Can't reach your computer, Couldn't reach Grok Bot's computer, and Reconnecting are the same family. Do the product buttons before you touch DNS. Choose Retry or reopen the conversation. Restart the app (menu-bar Quit on Mac, not the window close). Choose Recover computer when the unreachable state offers it. The confirmation dialog calls it Recover Grok Bot's Computer. If Recover is not there, Settings → Updates → Update under Grok Bot's Computer. On iPhone and Android the same controls are Update Computer and Reset Computer under Settings → Bot → Bot Computer. Wait for the replacement. Reset only if recovery and update fail and you accept losing recent unsynced work.</p>
<p>Chat sometimes still works. The hosted computer is a name under <code>cursorvm.com</code>, not the apex you can ping in a browser. Cloud work can continue while the desktop is disconnected, which is why the phone test matters more than the desktop wording.</p>
<p>The same wording is a known display bug when a trial or plan has ended. Retry and Recover fail because the account no longer has Grok Bot access, not because DNS died tonight. The app should say access ended. If the account lost the plan, pick one that includes Grok Bot or link SuperGrok on the same email, fully quit, and reopen. Do not burn an evening on 1.1.1.1 for a billing problem. The pricing page is the plan snapshot.</p>
<h2>Test in this order</h2>
<ol>
<li><strong>Fully quit and reopen.</strong> Menu-bar Quit on macOS. Tray quit on Windows. Closing the window leaves the process up, and Retry then does nothing visible.</li>
<li><strong>If Retry or Recover is offered, take that path before Reset.</strong> Recover keeps synced bots, files, and logins, and removes installed apps on the computer. Reset can also drop unsynced work.</li>
<li><strong>Hotspot on another carrier.</strong> Join the phone hotspot from the computer and open Grok Bot. If the hotspot works, your home or office path is the fault. Stop resetting the computer. If the hotspot fails too, and the phone app on cellular also fails, treat it as server-side and slow down.</li>
<li><strong>DNS for a subdomain, not the apex.</strong> The app connects to a per-computer hostname under cursorvm.com. The apex can resolve while every subdomain returns Query refused. Test a wildcard name, and read the Server line in the lookup so you see which resolver actually answered. Staff point at 1.1.1.1 and 8.8.8.8. On IPv6, a router advertisement can keep the ISP resolver and silently ignore your IPv4 DNS change. Set IPv6 DNS as well (the thread that fixed this used 2606:4700:4700::1111) or the IPv4 change never runs. Then fully quit and reopen.</li>
<li><strong>Antivirus HTTPS scanning.</strong> Kaspersky, ESET, Avast, AVG, Bitdefender, Norton, Trend Micro, Sophos, and similar products can break the app while the browser still loads. Grok Bot trusts public certificate authorities only. Encrypted-connection scanning swaps the issuer. Turn that scanning off, or exclude Grok Bot, fully quit from the tray or menu bar, and reopen.</li>
<li><strong>VPN and company tunnels outside the app.</strong> WARP has left a blank screen. Zscaler-style tunnels have left Windows 11 on a black loader. Windows builds have ignored the system HTTP proxy; staff reports say a TUN-mode tunnel is what works when a proxy is mandatory. None of that belongs inside the Agent Computer.</li>
</ol>
<div class="callout warn">
<p><strong>Never install a VPN, proxy, or DNS change inside the Agent Computer.</strong> A bot that installs a VPN can cut the always-on path. Every bot on the account then fails to reconnect until Recover restores routing.</p>
</div>
<h2>Desktop versus phone</h2>
<p>Use the phone as a second view of the same account, not as a new account.</p>
<ul>
<li><strong>Desktop black or Reconnecting, iOS works</strong> on the same login: bots are not gone. Do not Reset. Prefer Recover or Update, or wait if staff have said an official rebuild is coming. Reset can delete bots.</li>
<li><strong>Desktop and iOS both stuck</strong>, and the phone is on cellular so it is not your Wi-Fi: often server-side. Hold off on Reset, Recover, Update, and signing out.</li>
<li><strong>Days of Can't reach</strong> after Recover, Reset, and a reinstall: usually a stuck hosted box that only staff can restore. Email hi@cursor.com. Include version, OS, the exact sentence, time and timezone, and what you already clicked.</li>
<li><strong>Mid-session Reconnecting or Showing saved messages</strong> while the computer is otherwise healthy: same DNS class. A new computer from Reset lands in the DNS zone your resolver already cannot look up.</li>
</ul>
<h2>Windows-only traps that look like a bad download</h2>
<p>Two installed copies: Settings, Apps, Installed apps. Remove the older Grok Bot, quit the tray, open one. The other Windows failure is a proxy the app ignores. It connects directly, so browser checks through a system proxy can pass while Grok Bot fails. Staff’s probe, after TUN mode is on:</p>
<pre><code>curl.exe --noproxy "*" -I https://test123.us10.cursorvm.com</code></pre>
<p>A fast <code>404</code> with <code>Server: awselb/2.0</code> means the direct path works. The hostname is only a probe. A hang or reset means the app will fail too. Do not install the tunnel inside the Agent Computer. Full install notes: <a href="/learn/windows-download/">Windows download</a>. Re-downloading the installer does not change DNS.</p>
<p>When the network test passes and the label is still wrong, go back to access. Expired trial, lost seat, Legacy Privacy Mode never saved. Those three masquerade as reachability. The stuck page sorts Connecting and Setting up. The recover page is where Update, Recover, and Reset are compared after the tests above have failed for a reason other than your resolver.</p>
'''
    related = [
        ("/", "Grok Bot guide", "What the shared computer is, if the wording is new."),
        ("/troubleshooting/", "Not working index", "Usage, plugins, and Linux sit beside this card."),
        ("/troubleshooting/stuck/", "Stuck on a label", "Connecting, Setting up, Cleaning up, 50 percent."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "Only after the hotspot and DNS tests."),
        ("/learn/windows-download/", "Windows download", "One copy, tray quit, and TUN versus a system proxy."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Computer recovery", CURSOR_RECOVER),
        ("DNS and first setup", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
        ("VPN drops cursorvm", "https://forum.cursor.com/t/grok-bot-desktop-on-macos-is-permanently-stuck-on-reconnecting-to-your-computer/169119"),
        ("IPv6 DNS", "https://forum.cursor.com/t/cant-reach-your-computer-from-last-72-hours/169970"),
        ("Query refused on the subdomain", "https://forum.cursor.com/t/grok-bot-0-30-0-windows-setup-fails-with-cant-reach-your-computer-all-network-checks-pass/170035"),
        ("Windows app ignores the system proxy", "https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281"),
        ("WARP blank screen", "https://forum.cursor.com/t/blank-screen-after-opening-grok-bot/169966"),
    ]
    return _page("Can't reach", "Can't reach your computer in Grok Bot", lede, body, REACH_FAQS, related, sources)


def white_screen():
    lede = '''
<p class="meta">Blank windows and empty rosters, from staff posts. A white screen is usually local config or a waking computer, not a deleted account. Downloads: <a href="/learn/mac-download/">Mac</a> and <a href="/learn/windows-download/">Windows</a>.</p>
<div class="callout warn">
<p><strong>Do not Reset to find a missing bot.</strong> Cursor Help: open the same account on the phone, then Hidden Bots in the sidebar. Hide from sidebar removes the row only. The bot stays active. Chats are stored outside the computer, so a blank window is not deleted history.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/learn/mac-download/">Mac install, if the file was wrong</a>
  <a class="btn btn-secondary" href="/troubleshooting/stuck/">Spinner with a label</a>
  <a class="btn btn-ghost" href="/learn/login/">Stale login instead</a>
</div>
'''
    body = '''
<h2>Three blanks that are not the same bug</h2>
<p>People say white screen, black screen, and empty roster as if they were one reinstall. Split them. The fix for a local Mac config folder will not provision a free-plan computer, and Reset will not repaint a window whose config is still broken.</p>
<ul>
<li><strong>White window right after install</strong>, usually Mac. The package may be fine. Local config is not.</li>
<li><strong>Black spinner</strong> with no desktop, especially on first setup. Either the computer is still coming up, a tunnel is blocking it, or no computer was ever provisioned.</li>
<li><strong>Empty roster</strong> after you already had bots. Often sleep. Sometimes you logged in while a rebuild was still starting, and the app showed the new-user flow.</li>
</ul>
<h2>White window on Mac</h2>
<p>Fully quit with the menu-bar Quit item. In Finder, Go to Folder, open <code>~/Library/Application Support/</code>, and rename <code>Grok Bot</code> to <code>Grok Bot.bak</code>. On Windows the twin folder is <code>%APPDATA%\\Grok Bot</code>. Open the app from Applications or the Start menu, not from the installer. Reinstall alone does not clear that folder, which is why a second download from x.ai/bot changes nothing. Keep the .bak folder until you see the roster. This is local app state. It is not the cloud computer, and renaming it is not Reset. If the app hangs on every launch after a real quit, Cursor Help says contact support with the platform and version from About, rather than Reset.</p>
<p>If macOS never got as far as a window because it said the app is not supported or damaged, stop treating it as a white screen. That is the wrong chip package or a bad file. The Mac download page is the Gatekeeper and Apple silicon path. Drag a fresh official build into Applications after you trash the bad one.</p>
<h2>Black spinner</h2>
<p>A black loading screen during initial setup has two common causes, and they ask for opposite fixes. On a free Cursor plan, or a team admin without a Standard or Premium seat, no hosted computer is provisioned. The spinner is the app waiting for a machine that will not be created. Network tweaks will not help. You need access, then a full quit and reopen. On a paid seat, a black screen can instead be the tunnel: WARP has produced a blank screen, and a Zscaler-style tunnel has stuck Windows 11 on a black loader. Use a phone hotspot before you conclude the install is corrupt. The can't-reach page lists that order.</p>
<p>A black or white loader next to an empty roster, after you previously had bots, is the wake-from-sleep case below. Do not mix it up with the free-plan spinner. If you had a roster yesterday, you are not in the missing-seat case today unless the plan actually changed.</p>
<h2>Empty roster after reconnect</h2>
<p>Check Hidden Bots before you assume the roster was wiped. Cursor Help: Hide from sidebar only removes the row. Open Hidden Bots or Show Hidden Bots, then Unhide. Sections and hidden rows sync between iPhone and desktop. Deleting a sidebar section moves bots to Unassigned. It does not delete them. Also open the same Cursor account on the phone. A different login is an empty roster with your bots still on the other account.</p>
<p>The Agent Computer waking from sleep is slow. The app can show an empty roster and a loader while the machine comes back. Nothing was deleted. Wait. Fully quit. Open again. Do not Reset to force the list to repaint. Reset is how an empty-looking roster becomes an actually empty computer. A low-disk warning is also not data loss: Disk Saver proposes cleanup and deletes nothing until you confirm.</p>
<p>The crueler variant shows up after a rebuild. Logging in while the computer is still starting draws the first-run UI, as if you were a new user with no bots. Fully quit. Do not create a first bot in that window. A bot created there is a new teammate on a computer that was about to show the old ones, and you will not be able to tell which is which. Come back when the computer view is a desktop you recognize. Then open the roster before you type anything.</p>
<h2>What still is not a white screen</h2>
<p>Account unavailable after a password change is a stale session. Log out, fully quit, sign in. That screen is the login page. Not responding, with the computer visible, is usage. Can't reach, with those words on screen, is the network page. If you have tried the rename, the seat check, and a patient reopen, and both phone and desktop are blank for days, email hi@cursor.com rather than Reset. Include the version and whether iOS on cellular is blank too.</p>
'''
    related = [
        ("/", "Grok Bot guide", "Confirm you installed Grok Bot and not grok.com or Grok Build."),
        ("/learn/mac-download/", "Mac download", "Chip package, Applications, and Gatekeeper."),
        ("/troubleshooting/stuck/", "Stuck labels", "Connecting and Setting up, when there is text under the spinner."),
        ("/troubleshooting/cant-reach/", "Can't reach", "Hotspot, DNS, and tunnels that paint a blank screen."),
        ("/learn/first-bot/", "First Bot", "Only after a real roster is visible. Not during a fake first-run."),
    ]
    sources = [
        ("White screen on open", "https://forum.cursor.com/t/grok-bot-shows-white-screen-upon-opening-and-is-unusable/169815"),
        ("Empty roster and sleep", "https://forum.cursor.com/t/grok-bot-bug-report/170104"),
        ("New-user screen after rebuild", "https://forum.cursor.com/t/bots-workspace-missing-all-things-getting-new-user-experience/169448"),
        ("Free-plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
        ("Admin without a seat", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-during-initial-setup-on-mac/170251"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Blank screen", "Grok Bot white screen, empty roster, or hidden bots", lede, body, WHITE_FAQS, related, sources)


def recover_vs_reset():
    lede = '''
<p class="meta">Official order from <a href="%s">troubleshooting</a> and <a href="%s">computer recovery</a>. Buttons are last, not first. Usage silence: <a href="/troubleshooting/not-responding/">not responding</a>. Network: <a href="/troubleshooting/cant-reach/">can't reach</a>.</p>
<div class="callout warn">
<p><strong>Update and Recover keep synced bots, files, and logins. All three buttons remove installed apps on the computer.</strong> Reset is the only one that can also drop recent bots and files that have not synced. Chats live outside the computer. Backup not ready means wait for a backup, not Reset.</p>
</div>
<div class="cta-row">
  <a class="btn btn-primary" href="/troubleshooting/">Start from the symptom</a>
  <a class="btn btn-secondary" href="/learn/install/">Official reinstall</a>
  <a class="btn btn-ghost" href="/pricing/">Access ended, not a dead computer</a>
</div>
''' % (DOC_TROUBLE, CURSOR_RECOVER)
    body = '''
<h2>The order, before the table</h2>
<p>Cursor Help and xAI troubleshooting, re-read 2026-09-22, use the same order. Wait and Retry if the computer says Reconnecting or Couldn't reach Grok Bot's computer. Fully quit and reopen. Update from Settings → Updates if an update is offered. Recover if it still cannot reconnect, or if an update looks stuck and Recover computer is shown. On a slow update, Keep waiting is the safe default. Reset only after those steps. Do not start a second Update or Reset while one is already running. If Recover or Reset fails, use Retry Recovery or Retry Reset once, then stop.</p>
<p>On iPhone and Android, Update Computer and Reset Computer are under Settings → Bot → Bot Computer. The desktop confirmation says Recover Grok Bot's Computer. Before any button: if the computer view is up and bots are silent, open Usage. If the phone on the same account still works, the bots are not gone. If both devices fail, including cellular, wait before you click.</p>
<h2>What each control keeps</h2>
<div class="table-wrap"><table>
<thead><tr><th>Control</th><th>Keeps</th><th>Removes</th></tr></thead>
<tbody>
<tr><td>Update</td><td>Synced bots, files, and logins. Now or scheduled.</td><td>Installed apps and packages. A turn that cannot pause is discarded.</td></tr>
<tr><td>Recover</td><td>Bots, files, and logins. Recreates the computer.</td><td>Installed apps and packages.</td></tr>
<tr><td>Reset</td><td>Only the last snapshot.</td><td>Recent unsynced bots and files, plus installed apps.</td></tr>
</tbody>
</table></div>
<p>Chat history lives outside the computer. Reset is not how you protect chats. Deleting files inside the computer does not delete chats. Synced computer files usually return when the computer reopens. If it is still empty after Recover, stop and contact support. Files that live only on your Mac or Windows machine are not in that copy. Backup not ready means the backup has not finished. Wait for the update to be offered again. Do not Reset to force it. Agent busy means a bot could not pause. Let it finish, then update again. An exhausted trial does not delete data either. Export while the view still opens, then decide. Reset will not extend a trial.</p>
<h2>Hangs that look like you must click again</h2>
<ul>
<li><strong>Cleaning up never ends.</strong> The backend has often finished. Fully quit, reopen, and Recover if the computer is still down. A second Reset does not complete the first one.</li>
<li><strong>50 percent Starting.</strong> A server-side bad state. Wait a few minutes. Bot data is usually still there. Do not stack another Reset because the number is ugly.</li>
<li><strong>The Reset window opens behind Settings</strong> and cannot be clicked. Fully quit. Do not click blind through the stack. You can confirm a destructive action you cannot see.</li>
<li><strong>A scary status dialog.</strong> Do not confirm it yet. Sign in again. Check the phone on cellular. Then decide with the table above.</li>
</ul>
<h2>Cases where Reset is the wrong kindness</h2>
<p>Desktop black, iOS fine: wait or Recover. Do not Reset. Staff have said a Reset in that split can delete bots while an official rebuild was the real fix. Resolver cannot find the computer, and staff have said the computer is healthy: do not Recover or Reset either. The new machine is in the same DNS zone. Fix DNS, or move to a hotspot, and the current computer answers. Bot-installed VPN inside the computer: Recover is the routing restore, not a casual Reset. Days of Can't reach after you have already done Recover, Reset, and reinstall: stop. That hosted box needs staff. More clicks from you are not a faster queue.</p>
<h2>What to send support</h2>
<p>Email hi@cursor.com when the table says you are past self-serve, or when every bot fails for hours on every device while the computer is still visible. Include the Grok Bot version, the operating system, the exact error sentence, the bot or routine name, the time and timezone, the request or conversation id, and the list of what you already tried, in order. Do not attach passwords, two-factor codes, or keys. Say whether iOS on cellular matches the desktop. That one fact changes the advice from Recover to wait.</p>
<p>If you are here because the app was never installed, or the Mac said the app is not supported, you do not have a computer to reset. Use the download pages. A new official install plus Cursor login is the whole fix. Reset is a control inside a signed-in app, not a step on x.ai/bot.</p>
'''
    related = [
        ("/", "Grok Bot guide", "Shared computer, in one page, before you wipe one."),
        ("/troubleshooting/", "Not working index", "Pick the symptom if you have not yet."),
        ("/troubleshooting/not-responding/", "Not responding", "Usage, when the computer view still opens."),
        ("/troubleshooting/cant-reach/", "Can't reach", "DNS and antivirus before either button."),
        ("/learn/computer/", "Shared computer", "One machine for every bot. Chats are stored outside it."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Computer recovery", CURSOR_RECOVER),
        ("Cleaning up", "https://forum.cursor.com/t/grok-bot-hanging-at-cleaning-up-phase-after-resetting/169364"),
        ("50 percent Starting", "https://forum.cursor.com/t/currently-down-grok-bot-retrying-back-end-vm/169834"),
        ("Reset behind Settings", "https://forum.cursor.com/t/the-reset-computer-window-opens-behind-the-settings-window-and-is-invisible-and-unclickable/169177"),
        ("Trial exhaustion", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
    ]
    return _page("Recover or Reset", "Update, Recover, or Reset Grok Bot's computer", lede, body, RECOVER_FAQS, related, sources)


SUPPORT = [
    {
        "path": "/learn/mac-download/",
        "body": mac_download,
        "faqs": MAC_FAQS,
        "howto": (
            "Download Grok Bot for Mac",
            "Match Apple silicon or Intel, install from the official dmg into Applications, then sign in with Cursor.",
            [
                ("Read About This Mac", "Chip means Apple silicon. Processor means Intel."),
                ("Download the matching build", "Top macOS button is Apple silicon. Intel is under More downloads on x.ai/bot."),
                ("Drag to Applications and open", "Choose Open if macOS asks. Do not keep launching from the disk image."),
                ("Sign in with Cursor", "No separate Grok Bot account. Save Privacy Mode if Connecting never finishes."),
            ],
        ),
    },
    {
        "path": "/learn/windows-download/",
        "body": windows_download,
        "faqs": WINDOWS_FAQS,
        "howto": (
            "Install Grok Bot on Windows",
            "Pick x64 or Arm64, keep a single installed copy, quit the tray, and sign in with Cursor.",
            [
                ("Read System type", "Settings, System, About. x64 and Arm64 are different downloads."),
                ("Run the official installer", "Download it from x.ai/bot, then open the app from the Start menu."),
                ("Remove a duplicate copy", "If Installed apps lists Grok Bot twice, uninstall the older one."),
                ("Quit the tray and sign in", "Sign in with Cursor. Do not install a VPN inside the Agent Computer."),
            ],
        ),
    },
    {
        "path": "/learn/phone-download/",
        "body": phone_download,
        "faqs": PHONE_FAQS,
        "howto": (
            "Download Grok Bot on a phone",
            "Install the official iOS or Android app and sign in with the same Cursor account as the desktop.",
            [
                ("Pick the official store", "App Store for iPhone and iPad. Google Play package ai.x.grok.bot for Android."),
                ("Check the OS version", "iOS 18 or later, iPadOS 18 or later, or Android 9 or later."),
                ("Sign in with Cursor", "The phone joins the same roster and the same cloud computer."),
                ("Leave desktop-only jobs on the desktop", "Always allow, Teach a task, and the routine webhook stay on the desktop app."),
            ],
        ),
    },
    {
        "path": "/learn/login/",
        "body": login_page,
        "faqs": LOGIN_FAQS,
        "howto": (
            "Sign in to Grok Bot",
            "Use the Cursor account that holds the plan, finish the browser popup, and save Privacy Mode.",
            [
                ("Open the official app", "There is no separate Grok Bot registration."),
                ("Choose Sign in with Cursor", "Finish the browser popup, including org SSO if required."),
                ("Save Privacy Mode", "Legacy Privacy Mode leaves new accounts on Connecting forever."),
                ("Confirm the roster", "Then run one job. Do not create twelve bots on the first screen."),
            ],
        ),
    },
    {
        "path": "/troubleshooting/not-responding/",
        "body": not_responding,
        "faqs": NOT_RESPONDING_FAQS,
        "howto": (
            "Fix Grok Bot when it is not responding",
            "If the computer view opens, check weekly usage before Recover or Reset.",
            [
                ("See whether the computer view opens", "A visible computer means this is probably not a dead machine."),
                ("Open Usage", "Read the meter and the weekly reset time. The app may omit the limit banner."),
                ("Choose wait or On-Demand", "A zero cap blocks paid spillover and does not block credits."),
                ("Write support before Reset", "Hours of Bot failed to respond on every device, with the computer still visible, is a support case."),
            ],
        ),
    },
    {
        "path": "/troubleshooting/stuck/",
        "body": stuck,
        "faqs": STUCK_FAQS,
        "howto": (
            "Unstick Grok Bot setup",
            "Match Connecting, Setting up, Cleaning up, or 50 percent Starting to one move.",
            [
                ("Write down the label", "The words under the spinner pick the fix."),
                ("Save Privacy Mode if it says Connecting", "Then fully quit and reopen. Reset does not save that setting."),
                ("Check the seat if it says Setting up", "A free plan or an admin without a seat never gets a computer."),
                ("Quit instead of Resetting again", "Cleaning up and 50 percent Starting are not a cue for a second Reset."),
            ],
        ),
    },
    {
        "path": "/troubleshooting/cant-reach/",
        "body": cant_reach,
        "faqs": REACH_FAQS,
        "howto": (
            "Fix Can't reach your computer",
            "Quit, compare a phone hotspot, then fix DNS or HTTPS scanning before Reset.",
            [
                ("Fully quit and reopen", "Then Retry or Recover if offered. Reset stays last."),
                ("Try a phone hotspot", "If the hotspot works, stop rebuilding the computer."),
                ("Set public DNS on IPv4 and IPv6", "Staff point at 1.1.1.1 and 8.8.8.8. Router advertisements can keep the ISP resolver."),
                ("Turn off antivirus HTTPS scanning", "The app trusts public certificate authorities only."),
            ],
        ),
    },
    {
        "path": "/troubleshooting/white-screen/",
        "body": white_screen,
        "faqs": WHITE_FAQS,
        "howto": (
            "Fix a Grok Bot white or black screen",
            "Clear Mac local config, wait out sleep, and do not create a bot on a fake first-run screen.",
            [
                ("Fully quit", "Menu-bar Quit on macOS. Closing the window is not quitting."),
                ("Rename the Mac config folder", "Application Support/Grok Bot becomes Grok Bot.bak. Reinstall does not do this."),
                ("Wait if the roster is empty after sleep", "Nothing was deleted. Do not Reset."),
                ("Do not create a bot on the first-run screen during boot", "Fully quit and return when the computer is actually up."),
            ],
        ),
    },
    {
        "path": "/troubleshooting/recover-vs-reset/",
        "body": recover_vs_reset,
        "faqs": RECOVER_FAQS,
        "howto": (
            "Choose Recover, Update, or Reset",
            "Use the least destructive computer control after usage and network checks.",
            [
                ("Rule out usage and DNS", "A full meter or a bad resolver will survive every button."),
                ("Update if the computer still answers", "Synced bots, files, and logins stay. Installed apps on the computer are removed."),
                ("Recover if it is unreachable", "Recreates the computer. Same keep and remove split as Update."),
                ("Reset last", "Reset returns to the latest snapshot and can drop unsynced work."),
            ],
        ),
    },
]
