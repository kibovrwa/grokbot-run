# -*- coding: utf-8 -*-
"""Per-error pages split off the troubleshooting hub.

Facts are limited to copy already on this site, the reviewed failure
snapshots, and the official URLs those pages cite. No new UI paths,
error strings, prices, or product behavior.
"""
from content_support import (
    CURSOR_PLANS,
    CURSOR_RECOVER,
    DOC_START,
    DOC_TROUBLE,
    STORE,
    _page,
)

DOC_FAQ = "https://docs.x.ai/grok-bot/faq"
CONNECT = "https://cursor.com/help/grok-bot/connect-plugins"


def _spec(path, body, faqs, howto):
    return {"path": path, "body": body, "faqs": faqs, "howto": howto, "article": True}


# --- DNS -----------------------------------------------------------------

DNS_FAQS = [
    ("What hostname is Grok Bot actually looking up?",
     "A per-computer name under cursorvm.com, not the apex. The apex can resolve while every subdomain returns Query refused."),
    ("Which DNS addresses do staff point at?",
     "1.1.1.1 and 8.8.8.8, on both IPv4 and IPv6. A router advertisement can keep the ISP resolver after you change only IPv4. One thread that cleared this also set IPv6 to 2606:4700:4700::1111."),
    ("Should I Reset if staff say the computer is healthy?",
     "No. A rebuilt computer lands in the same DNS zone. Fix the resolver or use a hotspot. Reset does not teach your network a name it cannot look up."),
    ("The browser loads. Why is that not proof DNS is fine?",
     "Browser checks can use a different resolver, a proxy, or the apex name. Grok Bot connects directly to the computer subdomain."),
]

def dns_error():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. DNS notes from staff posts already cited on <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a>. Fetch context through 2026-09-22.</p>
<div class="callout warn">
<p><strong>A Grok Bot DNS error means your resolver cannot look up the computer&#x27;s subdomain.</strong> Retry, then a phone hotspot. Do not Reset while staff say the hosted computer is healthy. A new computer is created in the same DNS zone.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>The app does not connect to a generic website you can open in a browser tab. It connects to a per-computer hostname under <code>cursorvm.com</code>. The apex name can answer while every subdomain returns Query refused. That split is the whole bug in the Windows setup thread where ordinary network checks passed and the app still said Can&#x27;t reach your computer.</p>
<p>Staff have also described a healthy cloud computer whose Mac never finished reconnecting because traffic to cursorvm.com was dropped by a VPN or firewall. Mid-session Reconnecting, or Showing saved messages, while the Agent Computer is otherwise healthy, is the same class. The first-setup failure called createAgent can be this DNS block, or it can be a computer that was never created yet. Those two are not the same click. If no computer exists, there is nothing to Reset.</p>
<h2>What to do</h2>
<ol>
<li>Fully quit. Menu-bar Quit on macOS. Tray quit on Windows. Closing the window leaves the process up.</li>
<li>Choose Retry if the screen offers it. Recover only when the unreachable state offers Recover. The longer button order is on <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a>.</li>
<li>Join a phone hotspot on another carrier and open Grok Bot from that path. If the hotspot works, stop rebuilding the computer. The home or office resolver is the fault.</li>
<li>If you stay on the home network, set DNS to 1.1.1.1 or 8.8.8.8 on IPv4 and on IPv6. A router advertisement can keep handing out the ISP resolver after an IPv4-only change, which is the JioFiber report. The thread that fixed the IPv6 side used <code>2606:4700:4700::1111</code>.</li>
<li>Read which resolver answered. Staff tell people to look up a wildcard-style probe such as <code>test123.us8.cursorvm.com</code> and notice Query refused on the subdomain while the apex still works. Then fully quit and reopen.</li>
</ol>
<p>Windows adds a second trap that looks like DNS and is not. The app ignores the system HTTP proxy and connects directly, so checks that travel through the proxy can pass. That probe is on <a href="/troubleshooting/windows-proxy/">Windows proxy</a>. Antivirus products that scan HTTPS are on <a href="/troubleshooting/antivirus/">antivirus</a>.</p>
<h2>Limits</h2>
<ul>
<li>Do not install a VPN, proxy, or DNS changer inside the Agent Computer. A bot-installed VPN can cut the always-on path until Recover restores routing.</li>
<li>Do not keep Reset or Recover when the only failure is a resolver. The replacement computer uses the same zone.</li>
<li>If desktop and iOS both fail, including the phone on cellular, staff often treat that as server-side. Hold off on DNS theater and on Reset.</li>
<li>An ended trial can wear the same Can&#x27;t reach sentence. That is access, not DNS. See <a href="/troubleshooting/trial-ended/">trial ended</a>.</li>
<li>This page does not publish a new resolver, a hosts-file recipe, or a region list beyond the probe hostnames already in the staff threads (us8 and us10).</li>
</ul>
<p>When the lookup succeeds and the screen is still wrong, go back to the hub and match the label. <a href="/troubleshooting/">Grok Bot not working</a> is the index.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Symptom index. Start there if the label is not a DNS failure."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "Retry, hotspot, antivirus, and when the wording is a plan bug."),
        ("/troubleshooting/windows-proxy/", "Windows proxy", "Direct connection. A proxy that the browser uses and the app ignores."),
        ("/troubleshooting/antivirus/", "Antivirus HTTPS scanning", "The browser loads because the issuer was swapped."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "Only after the resolver is not the cause."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("createAgent and ISP DNS", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
        ("Query refused on the subdomain", "https://forum.cursor.com/t/grok-bot-0-30-0-windows-setup-fails-with-cant-reach-your-computer-all-network-checks-pass/170035"),
        ("IPv6 DNS kept by the router", "https://forum.cursor.com/t/cant-reach-your-computer-from-last-72-hours/169970"),
        ("VPN dropped cursorvm.com", "https://forum.cursor.com/t/grok-bot-desktop-on-macos-is-permanently-stuck-on-reconnecting-to-your-computer/169119"),
        ("Mac black screen, iOS still works", "https://forum.cursor.com/t/grok-bot-desktop-never-joins-existing-ios-bots-latest-app-stuck-on-black-screen/169940"),
    ]
    return _page("DNS", "Grok Bot DNS error", lede, body, DNS_FAQS, related, sources)


# --- Plugin OAuth --------------------------------------------------------

OAUTH_FAQS = [
    ("Gmail connect spins in Grok Bot. Where do staff say to authorize it?",
     "From Cursor, not from another attempt inside the broken Grok Bot plugin. That Cursor connection is shared into Grok Bot until the plugin path is fixed."),
    ("Notion says Invalid redirect_uri. Why does Connect again fail?",
     "The sign-in is stored on the account, so a second Connect hits the same state. Use Re-authenticate."),
    ("GitHub says Connected, then Authorization header is badly formatted.",
     "Press and hold that account, choose Remove, then sign in again. Do not paste a token into chat."),
    ("Zoom shows error 4700. Can I edit the Zoom app to fix it?",
     "No. The catalog plugin hard-codes http://localhost:8787/callback, and Zoom rejects the hostname localhost. Official Help says there is no user workaround."),
    ("Canva fails only on the iPhone.",
     "Connect Canva from desktop Grok Bot on the same account. The connector then syncs to the phone. It is an app-link versus web-redirect mismatch, not your Canva settings."),
]

def plugin_oauth():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Connector notes from <a href="%s">Connect plugins</a> and the staff threads already listed on the hub. The plugin lesson is <a href="/learn/plugins/">plugins and MCP</a>.</p>
<div class="callout warn">
<p><strong>Match the connector. Do not paste a bearer token into chat.</strong> Notion wants Re-authenticate. Gmail wants the Cursor authorization path. GitHub wants the account removed and added again. Zoom error 4700 has no user-side fix.</p>
</div>
''' % CONNECT
    body = '''
<h2>Why it happens</h2>
<p>Plugins are account-level. A connector you authorize is not private to one bot, and a bad authorization is also stored on the account. That is why pressing Connect again often repeats the failure: the app is replaying a redirect or a header it already saved. Team admins can disable marketplace plugins; the label for that is Disabled by team admin, which is not an OAuth bug.</p>
<p>The other family is a redirect the vendor will not accept. Zoom&#x27;s catalog plugin hard-codes <code>http://localhost:8787/callback</code>, and Zoom rejects the hostname localhost with error 4700. Canva on iOS 1.4.0 fails with Invalid redirect URI because the app link and the web redirect do not match. The official X plugin has failed connect and refresh across desktop, Cloud Agents, and Grok Bot, including a state staff described as connected but tools=0, while they waited on X-side app config. None of those are fixed by editing your own OAuth app.</p>
<h2>What to do</h2>
<ol>
<li>Reopen the authorization tab if the card says Waiting for authorization. On the phone, plugins are under the top-left avatar. On desktop, sidebar Plugins or the Connect card in chat.</li>
<li>Gmail: stop retrying the Grok Bot plugin. Authorize Gmail from Cursor. Staff say that path is different and the connection is shared with Grok Bot.</li>
<li>Notion: choose Re-authenticate, not Connect. Invalid redirect_uri sticks because the sign-in already lives on the account.</li>
<li>GitHub: if the UI says Connected and calls then fail with Authorization header is badly formatted, press and hold the account, Remove, then sign in again.</li>
<li>Canva on iPhone: connect from desktop Grok Bot on the same Cursor account. It syncs to the phone.</li>
<li>Zoom 4700 and the official X plugin with tools=0: stop. There is no reviewed user workaround. Do not keep rewriting a Zoom app, and do not paste a token into the chat to bypass either one.</li>
</ol>
<h2>What OAuth success still does not do</h2>
<p>A working Gmail connector lists attachment metadata and does not download the bytes. Staff say there is no download tool. Use the cloud browser, or park the file in Drive. Drive itself is file-level. Editing a Google Doc body or Sheet cells is the separate Docs and Sheets connectors, added from the marketplace on the same Google account.</p>
<p>There is no settings form for a custom connector. Ask the bot in chat to add a public HTTPS MCP server (streamable HTTP or SSE). Tools show up on the next message. An MCP that only listens on localhost on your PC is unreachable from the cloud computer. Local stdio MCP is unsupported. Details: <a href="/learn/plugins/">plugins</a> and <a href="/troubleshooting/local-execution/">local computer</a>.</p>
<h2>Limits</h2>
<ul>
<li>One connector hanging does not mean the computer is dead. The rest of the roster can be fine. Do not Reset to fix Zoom.</li>
<li>X login locks on the cloud computer are a different problem from the X plugin. See <a href="/troubleshooting/x-login/">X login locked</a>.</li>
<li>This page does not invent a new redirect URL, a client secret, or a Zoom setting that staff said does not exist.</li>
</ul>
<p>Index of every other screen: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Back to the symptom index."),
        ("/learn/plugins/", "Plugins and MCP", "When to use a connector instead of the browser."),
        ("/troubleshooting/x-login/", "X login locked", "Risk controls on the cloud computer, separate from plugin tools=0."),
        ("/troubleshooting/phone-not-connecting/", "Phone", "Canva on iOS is fixed from the desktop app."),
        ("/troubleshooting/not-responding/", "Not responding", "A silent roster is usage, not a bad OAuth header."),
    ]
    sources = [
        ("Connect plugins", CONNECT),
        ("Notion redirect", "https://forum.cursor.com/t/grok-bot-notion-plugin-oauth-invalid-redirect-uri/169234"),
        ("Gmail plugin", "https://forum.cursor.com/t/grok-bot-unable-to-authenticate-via-gmail-plugin/169782"),
        ("Gmail attachments are metadata only", "https://forum.cursor.com/t/grok-bot-gmail-connector-can-list-attachments-but-cannot-download-their-bytes/169261"),
        ("GitHub header", "https://forum.cursor.com/t/grokbot-and-github/170137"),
        ("Zoom error 4700", "https://forum.cursor.com/t/grok-bot-zoom-plugin-oauth-hardcodes-http-localhost-8787-callback-zoom-rejects-hostname-localhost-error-4700/169991"),
        ("Canva on iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
        ("X plugin tools=0", "https://forum.cursor.com/t/official-x-plugin-auth-is-broken-on-cursor-cloud-grok-bot-and-desktop-refresh/169592"),
    ]
    return _page("Plugins", "Grok Bot plugin OAuth failed", lede, body, OAUTH_FAQS, related, sources)


# --- Usage limit ---------------------------------------------------------

USAGE_FAQS = [
    ("The app never said I hit a limit. Can the meter still be full?",
     "Yes. iOS and desktop often omit the usage-limit notice. Settings, then Usage, or the Cursor dashboard, is the check. Spillover into On-Demand can also start with no in-app warning."),
    ("What does a $0 On-Demand cap stop?",
     "Paid spillover. It does not stop promo or referral credits. Charge order is the Grok Bot weekly pool, then those credits, then paid On-Demand."),
    ("Do bot-to-bot reviews count?",
     "Yes. Each bot-to-bot message burns a weekly-usage turn. Asking them in chat to stay quiet is only a hint. Deleting an idle specialist also clears that bot&#x27;s chat, so save first."),
    ("Will Reset clear the limit?",
     "No. Reset rebuilds the computer from the last snapshot. It does not add usage. If the computer view still opens, do not Reset for silence."),
    ("Is Pro&#x27;s Other Models credit the bot pool?",
     "No. Staff say that credit is not the Grok Bot weekly pool. Cloud Agents a bot launches bill Cursor plan usage separately. Plan eligibility, without a price invented here, is on the pricing page."),
]

def usage_limit():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Mechanics from <a href="%s">plans and billing</a> and staff posts. Dollar plan prices stay on <a href="/pricing/">pricing</a>. If bots are silent, also read <a href="/troubleshooting/not-responding/">not responding</a>.</p>
<div class="callout">
<p><strong>A Grok Bot usage limit is a weekly pool on the Cursor account, not a dead computer.</strong> The app often hides the banner. On-Demand can start charging with no in-app warning. Reset will not refill the meter.</p>
</div>
''' % CURSOR_PLANS
    body = '''
<h2>Why it happens</h2>
<p>Paid access includes weekly-resetting usage. When that pool is gone, and On-Demand is enabled, overage can move to shared On-Demand spend. Metering sits on the Cursor account. Staff describe the charge order as the Grok Bot weekly pool, then promo or referral credits, then paid On-Demand. There is no in-app warning before that handoff. A cap of $0 stops the paid tier and does not stop the credits in the middle.</p>
<p>On Pro, the bot pool is separate from Cursor plan usage. Pro&#x27;s Other Models credit is not the bot pool. With On-Demand off, the bot can still drain Cursor credits before it stops. Cloud Agents that Grok Bot starts run in your Cursor account and burn Cursor plan usage. Grok Bot chat is a different allowance. If you only watch the IDE chart, you can miss the bot meter and Reset a healthy computer.</p>
<p>Silence is the usual symptom. Messages may still appear as your bubbles. Replies never run. iOS and desktop often skip the sentence usage limit reached. Two limit banners are usually blocked retries, not two bills. An exhausted trial is a different silence: data stays, bots stop, and the computer view can still export. That case is <a href="/troubleshooting/trial-ended/">trial ended</a>.</p>
<h2>What to do</h2>
<ol>
<li>Confirm the computer view opens. If the label is Reconnecting or Can&#x27;t reach, this is the wrong page. Use <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a>.</li>
<li>Open Settings, then Usage, or the Cursor dashboard. Read the meter and the weekly reset time before any computer button.</li>
<li>To wait: leave On-Demand alone and use the reset time on that screen. Messages you already sent during the block reply in a batch once usage returns. Routines that came due during the block were skipped. They do not run later as a surprise batch of sends.</li>
<li>To resume now: enable On-Demand on the same Cursor account and set a spend limit you accept. Staff say bots should reply within a couple of minutes. If you do not want paid spillover, set the cap to $0 and still expect credits to drain first.</li>
<li>Shrink the week. Keep routine windows smaller. Delete idle specialist bots that message each other. Every bot-to-bot turn counts, including reviews you asked them to stop. Telling a bot to stay quiet in chat does not freeze the meter. Deleting a bot also clears that bot&#x27;s chat. Save what you need first. Staff also point at one Command Agent with subagents, because those finish and stop, unlike idle specialists that can still be woken.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not list plan prices. Eligibility and the dated conflicts are only on <a href="/pricing/">pricing</a>. The longer pitfall list is <a href="/learn/cost-and-pitfalls/">cost and pitfalls</a>.</li>
<li>Linking SuperGrok is a usage grant on the same Cursor account. It is not a second meter. Linking rules are on the pricing snapshot.</li>
<li>Do not Reset, Recover, or Update to fix a full meter. Those buttons change the computer.</li>
<li>macOS and iOS share one weekly bucket. The phone app is not a second pool.</li>
<li>If every bot says Bot failed to respond for hours on both devices while the computer is visible and the meter is not full, that can be model load (staff: overbooked, then Bot failed to respond) or a stuck computer. Ask hi@cursor.com before Reset. Include version, OS, time, and request id. No passwords or keys.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Pick a different screen if the computer view is closed."),
        ("/troubleshooting/not-responding/", "Not responding", "Computer status first, then this meter."),
        ("/learn/cost-and-pitfalls/", "Cost and pitfalls", "Pool, credits, and habits that burn a week."),
        ("/pricing/", "Pricing", "Which accounts include Grok Bot. No prices copied onto this page."),
        ("/troubleshooting/routines/", "Routines not running", "A skipped slot during a usage block is not a broken schedule."),
    ]
    sources = [
        ("Plans and billing", CURSOR_PLANS),
        ("No warning before On-Demand", "https://forum.cursor.com/t/grok-bot-gives-no-warning-before-weekly-usage-spills-into-paid-on-demand/169679"),
        ("Pro pool is separate", "https://forum.cursor.com/t/grok-bot-spend-cursor-usage-i-cant-accept-it/169796"),
        ("Credits drain before On-Demand", "https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982"),
        ("Other Models credit is not the bot pool", "https://forum.cursor.com/t/is-grok-bot-usage-separate-from-cursor-plan/169658"),
        ("Bot-to-bot reviews", "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"),
        ("Cloud Agent usage is separate", "https://forum.cursor.com/t/query-about-grok-bot-cursor-agent-usage-and-model-selection/169160"),
    ]
    return _page("Usage", "Grok Bot usage limit and on-demand charges", lede, body, USAGE_FAQS, related, sources)


# --- Install failed ------------------------------------------------------

INSTALL_FAQS = [
    ("macOS says the app is not supported. Is Grok Bot unavailable on Mac?",
     "Usually the chip package is wrong, or the file did not come from x.ai/bot. Chip in About This Mac means Apple silicon. Processor means Intel. The top macOS button is the Apple silicon build. Intel is under More downloads."),
    ("Windows lists Grok Bot twice. Which one do I remove?",
     "Uninstall the older copy under Settings, Apps, Installed apps, and keep the latest. Then quit from the tray and open the remaining copy once."),
    ("The window is white after a fresh install. Will reinstalling fix it?",
     "Not by itself. Fully quit and rename the local Grok Bot config folder. On Mac that is ~/Library/Application Support/Grok Bot. On Windows it is %APPDATA%\\Grok Bot. Reinstall leaves that folder in place."),
    ("It sits on Setting up forever. Is the installer corrupt?",
     "On a free Cursor plan, or a team admin with no paid seat, no computer is provisioned. The spinner is a known copy bug. A new download will not create the seat."),
    ("Is there a full uninstall guide here?",
     "No. The only reviewed uninstall step is removing an older duplicate Windows install. This handbook does not have a Mac, iPhone, or Android removal procedure, and it does not claim that deleting the app deletes the hosted computer."),
]

def install_failed():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Install failures already described on <a href="/learn/mac-download/">Mac</a>, <a href="/learn/windows-download/">Windows</a>, and staff posts. The file is only on <a href="%s">x.ai/bot</a>.</p>
<div class="callout warn">
<p><strong>Most Grok Bot install failures are the wrong Mac chip, a second Windows copy, or a missing seat.</strong> Download again only from x.ai/bot. Reinstall does not clear the local config folder, and it does not provision a free-plan computer.</p>
</div>
''' % STORE
    body = '''
<h2>Why it happens</h2>
<p>The product page offers more than one file. The top Download for macOS button is the Apple silicon build. Intel is under More downloads. About This Mac tells you which one you need: Chip means Apple silicon, Processor means Intel. Opening the wrong package produces not supported. A file that did not come from x.ai/bot can also be rejected or reported as damaged. This handbook will not give you a quarantine-removal command. Trash the bad file and download the matching official package.</p>
<p>Windows fails in a different boring way. Settings, System, About, System type picks x64 or Arm64. If Installed apps lists Grok Bot twice, the older copy can sit beside the new one and the fresh profile ends on Can&#x27;t reach your computer. A white flash and then the process dying, on the 0.24.0 Windows report, was a healthy cloud computer plus a local problem: endpoint security, a locked %%APPDATA%% folder, or a partial install. Staff said it was not the GPU.</p>
<p>A third failure never reaches a desktop because no computer was created. A free Cursor plan does not get a hosted machine, and a team admin role is not a seat. The app can still spin on Setting up. That is <a href="/troubleshooting/no-seat/">no seat</a>, not a corrupt installer. A new account that never saved Privacy Mode sits on Connecting instead. That is <a href="/troubleshooting/privacy-mode/">Privacy Mode</a>.</p>
<h2>What to do</h2>
<ol>
<li>Confirm the file came from x.ai/bot. Mac: match Chip or Processor, drag into Applications, eject the disk image, and open the Applications copy. If macOS asks, choose Open. If there is no Open button, System Settings, Privacy and Security, Open Anyway, then open from Applications again.</li>
<li>Windows: match x64 or Arm64, run that installer, and open the app from the Start menu. If two copies are installed, uninstall the older one, quit the tray, and open once.</li>
<li>White window: fully quit, then rename the local config folder to Grok Bot.bak and relaunch. Keep the .bak folder until the roster loads. The longer blank-screen split is <a href="/troubleshooting/white-screen/">white screen</a>.</li>
<li>White flash, then Windows closes the app: treat it as local (security tool, locked app data, partial install). Do not Reset a cloud computer staff already called healthy.</li>
<li>If the installer finished and the sentence is Can&#x27;t reach, the download is probably fine. Continue with <a href="/troubleshooting/dns-error/">DNS</a>, <a href="/troubleshooting/windows-proxy/">Windows proxy</a>, or <a href="/troubleshooting/antivirus/">antivirus</a>. Linux packages that are rejected are <a href="/troubleshooting/linux/">Linux</a>, not a Mac chip problem.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>How to uninstall Grok Bot, as a full removal of Mac, Windows, iPhone, and Android, is not in the reviewed sources. The only documented uninstall click is the older Windows copy under Installed apps. Removing the desktop app is not described as Reset, and this page will not claim it deletes or keeps bots.</li>
<li>Homebrew cask grok-bot is the same app and, when checked on 2026-09-22, required macOS 12 or later. xAI Get started does not publish that minimum. The cask does not show the chip choice. Use the product page when you must pick Intel.</li>
<li>Do not hunt a forum installer. The app checks for updates itself. That update is a different control from the computer update, covered on <a href="/troubleshooting/update-failed/">update failed</a>.</li>
<li>Sign in with Cursor after the window exists. There is no separate Grok Bot account. Login stalls are <a href="/learn/login/">Cursor login</a>.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>. Official steps: <a href="%s">Get started</a>.</p>
''' % DOC_START
    related = [
        ("/troubleshooting/", "Not working", "If the app is installed and a later screen fails."),
        ("/learn/mac-download/", "Mac download", "Chip, Gatekeeper, and the white window."),
        ("/learn/windows-download/", "Windows download", "x64 or Arm64, one copy, tray quit."),
        ("/troubleshooting/no-seat/", "No seat", "Setting up forever on a free plan or an admin without a seat."),
        ("/troubleshooting/linux/", "Linux not connecting", "Official deb, rpm, and AppImage versus a rejected old build."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("x.ai/bot", STORE),
        ("Intel is under More downloads", "https://forum.cursor.com/t/grok-bot-w-cursor-ultra-on-intel-chip-mac/168752"),
        ("White screen is local config", "https://forum.cursor.com/t/grok-bot-shows-white-screen-upon-opening-and-is-unusable/169815"),
        ("Windows white flash then the app closes", "https://forum.cursor.com/t/grok-bot-0-24-0-windows-10-x64-white-screen-flashes-then-app-closes/169380"),
        ("Free plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
    ]
    return _page("Install", "Grok Bot install failed on Mac or Windows", lede, body, INSTALL_FAQS, related, sources)


# --- Update failed -------------------------------------------------------

UPDATE_FAQS = [
    ("Which update did I start?",
     "Settings, Updates, Check for Updates, then Restart to Update, replaces the desktop app and does not reset the computer. Update under Grok Bot&#x27;s Computer replaces the machine image."),
    ("A computer update is slow. Should I Reset?",
     "No. Keep waiting is the safe default. Recover is for when the update looks stuck and the app offers Recover computer. Do not start a second update while one is running."),
    ("Will the update delete my bots?",
     "Update and Recover keep synced bots, files, and logins. They remove installed apps and packages. A turn that cannot pause is discarded. Reset is the control that can drop unsynced work."),
    ("Packages I installed are gone after Update.",
     "Staff: Update Computer rebuilds the OS image, so apt packages, apps, and daemons go. Keep a package list in a file and ask the bot to reinstall. Files and logins are the part that stays."),
]

def update_failed():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Two different updates, from <a href="%s">computer recovery</a> and <a href="%s">troubleshooting</a>. What each button keeps is also on <a href="/troubleshooting/recover-vs-reset/">Recover versus Reset</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot update failed usually means the computer image, not the desktop app.</strong> Check for Updates restarts the app and leaves the computer alone. Update under Grok Bot&#x27;s Computer keeps synced bots and removes installed apps. On a slow run, Keep waiting.</p>
</div>
''' % (CURSOR_RECOVER, DOC_TROUBLE)
    body = '''
<h2>Why it happens</h2>
<p>The product has two updates in one screen, and people mix them. The desktop app updates itself from Settings, then Updates, then Check for Updates. Restart to Update replaces that app. It does not reset the computer. The computer update is the other control: Update under Grok Bot&#x27;s Computer. On iPhone and Android the matching controls are Update Computer and Reset Computer under Settings, Bot, Bot Computer.</p>
<p>The computer update keeps synced bots, files, and logins, and it removes installed apps and packages because it rebuilds the OS image. A turn that cannot pause is discarded. Idle machines can also auto-update, and they sleep, so background processes die. That looks like an update broke the box when the image was replaced on purpose. WhatsApp linked-device sessions are a sharper version of the same split: a computer refresh keeps /workspace, the browser profile, and ~/.config, and it does not keep ~/.local/state, so the WhatsApp link vanishes.</p>
<p>A failed reconnect after an attempted update is often a lost app login, not a destroyed machine. Staff say bots, files, and logins live on the remote computer, and Recover or Reset need a working session. If the session is gone, those buttons fail until you sign in again.</p>
<h2>What to do</h2>
<ol>
<li>Read the control you clicked. If you only restarted the desktop app, the computer was not updated. Open it again and sign in if the window asks.</li>
<li>If the computer update is still moving, leave it. Several minutes is normal for an image update. Keep waiting is the safe default. Do not start a second Update or Reset while one is running.</li>
<li>If it looks stuck and the app offers Recover computer, that recreate uses the same keep-and-remove split as Update. The confirmation dialog says Recover Grok Bot&#x27;s Computer. If Recover or Reset fails once, use Retry Recovery or Retry Reset once, then stop.</li>
<li>If Can&#x27;t reach follows the update and Recover will not start, fully quit, sign out, and sign in (or reinstall the official app and sign in). Then retry the computer button. A button cannot recover a session the app has already dropped.</li>
<li>After a successful image update, expect apt packages, extra apps, and daemons to be gone. Keep the package list in a file on the computer and ask the bot to reinstall. Do not treat that wipe as data loss of synced files.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>Backup not ready means the backup has not finished. Wait until the update is offered again. Do not Reset to force it. Agent busy means a bot could not pause. Let the turn finish, then update again.</li>
<li>Reset is still last. It keeps only the last snapshot, so recent unsynced bots and files can go. Chats live outside the computer. The comparison table is on <a href="/troubleshooting/recover-vs-reset/">Recover versus Reset</a>.</li>
<li>Cleaning up that never ends, or a stop at 50 percent Starting, are hangs after Reset, not reasons to update again. Fully quit. The stuck page has those two labels.</li>
<li>This page does not publish a build number you should be on. Staff have pointed at Settings, Updates, and X for releases, and they have said there was no public changelog at the time of that answer.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Match the label if this was not an update."),
        ("/troubleshooting/recover-vs-reset/", "Recover versus Reset", "What Update, Recover, and Reset each remove."),
        ("/troubleshooting/stuck/", "Stuck", "Cleaning up and 50 percent Starting."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "When the words after the update are a network failure."),
        ("/learn/computer/", "Shared computer", "Files in /workspace are the part designed to survive an update."),
    ]
    sources = [
        ("Computer recovery", CURSOR_RECOVER),
        ("Official troubleshooting", DOC_TROUBLE),
        ("Can&#x27;t reconnect after an update", "https://forum.cursor.com/t/unable-to-reconnect-to-my-grok-bots-computer-after-attempted-update/170000"),
        ("Packages wiped, files kept", "https://forum.cursor.com/t/cloud-computer-wipes-packages-after-rebuild/169847"),
        ("WhatsApp session and ~/.local/state", "https://forum.cursor.com/t/computer-refresh-wipes-whatsapp-linked-device-session-in-grok-bot/169025"),
        ("Update, Recover, and Reset all failed", "https://forum.cursor.com/t/grok-bot-0-30-0-agent-computer-unreachable-after-update-recover-and-reset-all-failed/170258"),
    ]
    return _page("Update", "Grok Bot update failed", lede, body, UPDATE_FAQS, related, sources)


# --- Phone ---------------------------------------------------------------

PHONE_FAQS = [
    ("Does the phone get its own computer?",
     "No. Phone and desktop share one Cursor account, one roster, and one cloud computer. macOS and iOS also share one weekly usage bucket."),
    ("Desktop says Can&#x27;t reach and the iPhone still shows the bots. Do I Reset?",
     "No. That split means the bots are still there. Prefer Recover or Update, or wait. Reset can delete bots. If both the desktop and the phone on cellular are stuck, staff often call that server-side and say to hold off."),
    ("Where are Update and Reset on the phone?",
     "Settings, Bot, Bot Computer. The desktop confirmation for the same Recover action says Recover Grok Bot&#x27;s Computer."),
    ("Why can the phone not set Always Allow?",
     "Always Allow for local-computer actions lives only in the desktop app on that machine. iOS can approve one action at a time, and those approvals clear on every new message."),
    ("The webhook URL is missing on iOS.",
     "Staff: a webhook routine&#x27;s POST URL and sender key only appear on the desktop app. Open the trigger card there."),
]

def phone_not_connecting():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Phone and desktop share one computer, from the install notes and staff posts. Store listings: <a href="/learn/phone-download/">iPhone and Android</a>.</p>
<div class="callout warn">
<p><strong>The Grok Bot phone app does not connect to your laptop. It connects to the same cloud computer as the desktop app.</strong> If the iPhone works and the desktop does not, the bots are not gone. Do not Reset to make the phone invent a second machine.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>There is one roster. Signing the phone into a different Cursor account looks like the computer disappeared, because you are looking at a different user. Signing the same account in shows the same bots, the same files, and the same weekly pool on macOS and iOS. The phone is a second view, not a second VM, and not a cable link to the Mac or PC on your desk.</p>
<p>The desktop can fail while that view stays healthy. Staff have said a Mac black screen with working iOS bots was a local DNS block to a healthy cloud computer, not a reason to recreate it. The reverse also happens: both clients stuck, including the phone on cellular, which staff treat as server-side. A third case is a feature that was never on the phone. The webhook URL and sender key are desktop-only. Always Allow for local execution is desktop-only. Teach a task is desktop-only. Canva&#x27;s OAuth redirect fails on iOS and succeeds from the desktop app, then syncs.</p>
<h2>What to do</h2>
<ol>
<li>Confirm both apps use the same Cursor login. A work account and a personal account do not merge rosters.</li>
<li>If the phone shows the bots and the desktop says Reconnecting, Can&#x27;t reach, or a black window, stop. Do not Reset. Use <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a> and <a href="/troubleshooting/dns-error/">DNS</a> on the desktop. iOS still working is the clue the hosted bots are intact.</li>
<li>If both are stuck and the phone is on cellular, hold off on Reset, Recover, Update, and signing out. That pattern is the one staff describe as server-side. Email hi@cursor.com with version, OS, the exact line, time and timezone, and whether cellular failed too.</li>
<li>Use the phone as a check before a scary desktop dialog. Staff have said to re-login and verify on mobile cellular before confirming a partial-state Reset. Update Computer and Reset Computer on the phone are under Settings, Bot, Bot Computer.</li>
<li>For a missing webhook, Always Allow, or Teach a task, move to the desktop app. iOS can only one-time-approve local actions, and those approvals clear on every new message. Set Always Allow under desktop Settings, Execution on Local Computer.</li>
<li>Canva Invalid redirect URI on iOS: connect Canva from desktop Grok Bot. See <a href="/troubleshooting/plugin-oauth/">plugin OAuth</a>.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>iOS 1.3.2 sends a question list as soon as you tap one option. Multi-select before send needs a newer Grok Bot app build. That is a composer bug, not a failed computer connection.</li>
<li>Delete Account on iOS deletes the Cursor account plus agents, chats, and the computer. Desktop sign-out does not. There is no smaller Grok Bot account underneath.</li>
<li>The phone will not fix a full weekly meter. Both devices share it. See <a href="/troubleshooting/usage-limit/">usage limit</a>.</li>
<li>This page does not describe a pairing code, a QR link from the phone to the laptop, or a phone-only computer. Those are not in the reviewed notes.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Desktop labels that are not a phone bug."),
        ("/learn/phone-download/", "Phone download", "Official stores and OS versions."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "Desktop down, phone up, is this page&#x27;s split."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "Canva on iOS, and the other connector failures."),
        ("/troubleshooting/local-execution/", "Local computer", "Always Allow is desktop-only."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Mac black screen, iOS bots still there", "https://forum.cursor.com/t/grok-bot-desktop-never-joins-existing-ios-bots-latest-app-stuck-on-black-screen/169940"),
        ("Webhook URL is desktop-only", "https://forum.cursor.com/t/webhook-url-missing-on-ios/169589"),
        ("iOS cannot Always Allow", "https://forum.cursor.com/t/authorization-death-by-1000-clicks/170087"),
        ("iOS sends the question list on first tap", "https://forum.cursor.com/t/multiple-choice-list-doesn-t-work-on-grok-bot-mobile/169830"),
        ("Canva on iOS", "https://forum.cursor.com/t/grok-bot-canva-connector-failing/170431"),
    ]
    return _page("Phone", "Grok Bot phone app not connecting to the computer", lede, body, PHONE_FAQS, related, sources)


# --- Local execution -----------------------------------------------------

LOCAL_FAQS = [
    ("Chat works, but the Mac says the local computer is offline. What now?",
     "Fully quit and reopen. Staff describe a helper that registers and then drops its server link. If it fails again, the log they asked for is ~/.grokbot/local-exec-daemon.log."),
    ("I set Always Allow and ExternalShell is still blocked.",
     "Do not assume Always Allow means always. Staff have confirmed allow-lists still fail. iOS cannot set Always Allow at all. It only one-time-approves, and that approval clears on the next message."),
    ("Windows still shows the local machine as unreachable after I quit.",
     "Quit from the tray, end leftover Grok Bot and local-exec-daemon processes in Task Manager, relaunch, and wait about a minute to re-register."),
    ("Can the cloud computer join my company VPN?",
     "No. Staff say not to install a VPN client on it, because that can knock the box offline. Internal sites need Execution on Local Computer on a machine that is already on the VPN."),
]

def local_execution():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Local-exec notes from staff posts. The cloud computer is a different machine: <a href="/learn/computer/">shared computer</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot local computer offline can sit next to a working chat.</strong> Fully quit and reopen before you Reset the cloud computer. Always Allow exists only on the desktop that will run the commands.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>The cloud computer is not the Mac or PC in front of you. Local execution is a helper on that desk machine. Staff have watched it register and then drop the server link, so Settings or the agent says offline while chat still works. A later report says the helper can start and then fail registration after an update. Full quit plus sign-out recreates it. Staff said desktop 0.31.0 was rolling out for that registration failure. This page does not claim that build is what you have today.</p>
<p>Windows has its own leftover process. A 0.30.0 fix covered one macOS daemon that exited and did not respawn. The Windows local-exec-daemon is a different known failure. On 0.27.0, staff also saw the agent say the local machine is not connected after a clean registration and a new identity. If one clean launch still fails, they called that service-side.</p>
<p>A large CopyFromBox, or a Shell that timed out, can drop the machine from the agent list for about a minute while Settings still says connected. That looks like a lie in the UI because both sentences are briefly true.</p>
<h2>What to do</h2>
<ol>
<li>Fully quit. Mac: menu-bar Quit. If the helper is stuck after a large copy, staff also used Cmd+Q and then <code>pkill -f local-exec-daemon</code> before reopening. Windows: quit the tray, end Grok Bot and local-exec-daemon in Task Manager, wait about a minute, relaunch.</li>
<li>If the helper died after an update, sign out as well as quitting, then sign in so the helper is recreated.</li>
<li>Set Always Allow only on the desktop that should run the commands: Settings, Execution on Local Computer. iOS cannot do this. The computer lesson also describes the control under Settings, General, Agent. This handbook does not add a third path.</li>
<li>Split large copies. Wait a minute before you retry a transfer that just timed out. Settings can still say connected during that minute.</li>
<li>If chat is fine and only the local machine is offline, do not Reset the cloud computer. Reset does not respawn a daemon on your laptop.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>ExternalShell can stay blocked after Always Allow. Staff confirmed allow-lists still fail. Always Allow is not forever-allow.</li>
<li>Local and stdio MCP on your PC are unreachable from the cloud computer. Ask for a public HTTPS MCP, or use the cloud browser. See <a href="/learn/plugins/">plugins</a>.</li>
<li>Do not install a corporate VPN client on the Agent Computer. Staff say the cloud computer cannot join one today, and a bad install can take the box offline. Atlassian Cloud and other public SSO can use browser takeover. YubiKey is supported on macOS and Windows under Settings, Security Key. Sites that exist only on the VPN need local execution on the machine that already has the VPN.</li>
<li>Linux empty ListMachines is the next page, not a Mac quit. <a href="/troubleshooting/linux/">Linux not connecting</a>.</li>
<li>If the failure survives a full quit and a single relaunch, send the log path staff named and stop stacking resets.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Cloud-computer labels are a different index."),
        ("/learn/computer/", "Shared computer", "Cloud machine versus the laptop in front of you."),
        ("/troubleshooting/linux/", "Linux", "Empty ListMachines and the keyring workaround."),
        ("/troubleshooting/phone-not-connecting/", "Phone", "iOS cannot set Always Allow."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "Localhost MCP is not a connector you can click."),
    ]
    sources = [
        ("Chat up, local computer offline", "https://forum.cursor.com/t/grok-bot-mac-chat-works-local-computer-reported-offline/168973"),
        ("Helper drops after register", "https://forum.cursor.com/t/local-execution-stays-offline-while-chat-still-works/169821"),
        ("Registration fails after an update", "https://forum.cursor.com/t/grok-bot-cannot-access-my-local-computer/169924"),
        ("Windows leftover daemon", "https://forum.cursor.com/t/new-report-windows-leftover-daemon-on-0-30-0/170121"),
        ("Windows 0.27.0 stays disconnected", "https://forum.cursor.com/t/grok-bot-0-27-0-windows-local-host-permanently-isn-t-connected-after-clean-registration-new-identity-server-side/169594"),
        ("Always Allow is desktop-only", "https://forum.cursor.com/t/authorization-death-by-1000-clicks/170087"),
        ("ExternalShell still blocked", "https://forum.cursor.com/t/grok-bot-externalshell-blocked-despite-always-allow/168180"),
        ("CopyFromBox drops the machine for a minute", "https://forum.cursor.com/t/grok-bot-local-computer-execution-looks-connected-in-settings-but-is-not-actually-usable-for-file-i-o/169877"),
        ("No VPN client on the cloud computer", "https://forum.cursor.com/t/vpn-sso-passkey-and-yubikey-within-grokbot/170148"),
        ("Local MCP is unsupported", "https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182"),
    ]
    return _page("Local computer", "Grok Bot local computer offline", lede, body, LOCAL_FAQS, related, sources)


# --- Linux ---------------------------------------------------------------

LINUX_FAQS = [
    ("Is there an official Grok Bot Linux app?",
     "As of the FAQ fetch used on this site, Linux is an official platform. Download deb, rpm, or AppImage from x.ai/bot under More downloads. An older staff reply said Grok Bot was not formally on Linux and rejected the 0.18 build. Prefer the current FAQ over that older rejection."),
    ("Linux 0.30 shows an empty ListMachines. What is the interim step?",
     "Staff: a fix was already merged for a later desktop update. Until you have it, unlock the system keyring (gnome-keyring or KWallet), fully quit leftover Grok Bot processes, and relaunch."),
    ("Can I use an AUR, COPR, or Wine package instead?",
     "Those are community ports, not official support. This handbook does not treat them as the product. The comparison lives on the Linux tools page."),
    ("Local MCP on the Linux box is invisible to the bot.",
     "That is expected. Grok Bot cannot attach local or stdio MCP. Use a public HTTPS MCP or the cloud browser."),
]

def linux_not_connecting():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Package choice is <a href="/tools/linux-port/">Linux packages</a>. Connection failures below are the staff notes, not a new installer.</p>
<div class="callout warn">
<p><strong>Install the official deb, rpm, or AppImage from x.ai/bot before you debug the network.</strong> Very old unofficial 0.18 builds were rejected. Empty ListMachines on Linux 0.30.0 is a known desktop bug with a keyring workaround, not a Reset of the cloud computer.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>Linux went through two different staff answers, and both are still in the record. One reply on the 0.18 thread said Grok Bot was not officially available on Linux yet, that the old build was rejected, and that Can&#x27;t reach your computer on that build was not your network. Supported platforms in that answer were macOS, Windows, and iOS. Later, the FAQ fetch this site uses lists Linux as an official platform, with deb, rpm, and AppImage under More downloads on x.ai/bot. If you are on a current official package, do not follow the 0.18 rejection as if it still described your file. If you are still on that old build, the network is the wrong layer.</p>
<p>A separate bug is local execution. On Grok Bot 0.30.0 Linux, ListMachines can come back empty. Staff said a fix was already merged for the next desktop update. The interim step is an unlocked system keyring, then a real quit of leftover processes. Community AUR, COPR, and Wine packages are outside that support. They are catalogued on the tools page so you can see they are not the official client.</p>
<h2>What to do</h2>
<ol>
<li>Download deb, rpm, or AppImage from x.ai/bot, More downloads. Remove a very old unofficial 0.18 build instead of fighting its Can&#x27;t reach sentence.</li>
<li>If the official app is installed and the cloud computer will not open, use the same order as every other desktop: quit, Retry, hotspot, then <a href="/troubleshooting/dns-error/">DNS</a>. Do not start with Reset.</li>
<li>If the cloud computer is up and local execution is the empty list: unlock gnome-keyring or KWallet, fully quit leftover Grok Bot processes, and relaunch. Wait for the desktop update staff said contained the fix rather than reinstalling the cloud machine.</li>
<li>Keep local MCP off your debugging list. Stdio and localhost servers on the PC are unreachable from the cloud computer.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not ship a package, a checksum, or a distro-specific unit file. Official files stay on x.ai/bot. Community ports stay on <a href="/tools/linux-port/">Linux packages</a>.</li>
<li>An early staff note that there was no official Debian or Fedora app conflicts with the later FAQ. Trust the FAQ date on <a href="/sources/">sources</a> over a forum sentence from before Linux was listed.</li>
<li>Always Allow and the Windows daemon are <a href="/troubleshooting/local-execution/">local computer offline</a>. The keyring step is the Linux-specific part.</li>
<li>A free plan still does not get a computer on Linux. The spinner is <a href="/troubleshooting/no-seat/">no seat</a>.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Symptom index for every platform."),
        ("/tools/linux-port/", "Linux packages", "Official packages versus community ports."),
        ("/troubleshooting/local-execution/", "Local computer", "Daemon, Always Allow, and a dropped helper."),
        ("/troubleshooting/dns-error/", "DNS error", "When the official app is installed and the subdomain will not resolve."),
        ("/learn/install/", "Install", "Mac, Windows, Linux, and phone from one overview."),
    ]
    sources = [
        ("Get started", DOC_START),
        ("FAQ", DOC_FAQ),
        ("0.18 build rejected", "https://forum.cursor.com/t/grok-bot-couldnt-finish-setup/170010"),
        ("Linux ListMachines empty", "https://forum.cursor.com/t/grokbot-linux-execution-on-local-computer-not-working/170157"),
        ("Local MCP unsupported", "https://forum.cursor.com/t/does-grok-bot-support-local-mcp-e-g-workflowy/168182"),
        ("Arch and Linux request thread", "https://forum.cursor.com/t/native-grok-bot-desktop-app-for-arch-linux-and-linux-generally/168084"),
    ]
    return _page("Linux", "Grok Bot Linux not connecting", lede, body, LINUX_FAQS, related, sources)


# --- Trial ended ---------------------------------------------------------

TRIAL_FAQS = [
    ("Does the trial ending delete bots and files?",
     "Staff: no. Bots stop replying. The computer view can still export. Reset is what can drop unsynced work. Do not Reset to save a trial."),
    ("The screen says Can&#x27;t reach your computer. How is that a billing problem?",
     "Ended access can wear that sentence. Retry and Recover fail because the account no longer has Grok Bot, not because DNS died. The app should say access ended. The network wording is a known display bug."),
    ("What restores access?",
     "A plan that includes Grok Bot, or a linkable SuperGrok on the same email, then a full quit and reopen. Which plans those are, with the dated conflicts, is only on the pricing page. This page does not add a price."),
    ("The meter hit 100 percent but I still have a plan. Is that the trial?",
     "No. That is the weekly pool. See usage limit. Trial exhaustion and a full week are both silence, and neither one is fixed by Reset."),
]

def trial_ended():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Trial behavior from staff and <a href="%s">plans and billing</a>. Which accounts include Grok Bot: <a href="/pricing/">pricing</a>. No prices on this page.</p>
<div class="callout warn">
<p><strong>When a Grok Bot trial ends, bots stop answering and the data is still there.</strong> The app can mislabel that as Can&#x27;t reach your computer. Do not Reset to save the trial. Export from the computer view, then fix access.</p>
</div>
''' % CURSOR_PLANS
    body = '''
<h2>Why it happens</h2>
<p>The trial is usage credits, not a pile of days you can point at, plus a 7-day window described on the cost page. Credits debit by agent steps and tokens. A large task can exhaust them at once. Spent trial credits are not restored. When they are gone, bots stop replying. Staff were explicit that the cloud workspace is not deleted: the computer view still lets you export until you Reset.</p>
<p>The nasty part is the label. Retry and Recover fail because the account no longer has Grok Bot access. The app should say access ended. Instead it can say Can&#x27;t reach your computer, which sends people into DNS and Reset. That display bug is why a hotspot test that fails on every network, on an account whose plan is gone, is not a resolver problem. Legacy request-based Cursor pricing also does not include Grok Bot unless you opt into usage-based pricing. A free Cursor plan never provisions a computer at all. That spinner is <a href="/troubleshooting/no-seat/">no seat</a>, which can look like a trial that never started.</p>
<h2>What to do</h2>
<ol>
<li>Open the computer view if it still loads. Export what you need before any Reset. Reset will not extend a trial, and it can drop unsynced bots and files.</li>
<li>Check the Cursor account. If access ended, pick a plan that includes Grok Bot or link personal SuperGrok on the same email. Linking rules and the conflicts between official pages are on <a href="/pricing/">pricing</a>. Come back here only after that page, not for a dollar figure.</li>
<li>Fully quit and reopen. Menu-bar Quit or the Windows tray. A window close does not refresh entitlement.</li>
<li>If the plan is fine and only the weekly meter is full, you are on <a href="/troubleshooting/usage-limit/">usage limit</a>. On-Demand and the $0 cap are explained there. They are not a new trial.</li>
<li>If the plan is fine and the words really are a network failure, stop treating this as billing. <a href="/troubleshooting/dns-error/">DNS</a> and <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a> are the tests.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not quote list prices, does not extend the early-September 2026 enterprise two-week announcement, and does not invent a free consumer tier. The pricing page says that announcement&#x27;s window is expired and was never a consumer free tier.</li>
<li>Linking SuperGrok is a usage grant on the same Cursor account. You cannot unlink it yourself. It does not open a second Grok-side meter. Stacking wording still differs across official pages. Trust the page you open.</li>
<li>macOS and iOS share the bucket. Installing the phone app does not grant a second trial.</li>
<li>Days of Can&#x27;t reach after Recover, Reset, and reinstall, on an account that still has access, are a stuck hosted box for staff. That is not an expired trial. Email hi@cursor.com.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Other labels that are not an ended plan."),
        ("/pricing/", "Pricing", "Dated plan snapshot. The only page with that contrast."),
        ("/troubleshooting/usage-limit/", "Usage limit", "Weekly pool and On-Demand, after you still have access."),
        ("/troubleshooting/no-seat/", "No seat", "Free plan or admin with no computer provisioned."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "Use this when access is fine and the path is not."),
    ]
    sources = [
        ("Plans and billing", CURSOR_PLANS),
        ("Trial exhaustion still exportable", "https://forum.cursor.com/t/grok-bot-cloud-workspace-inaccessible-after-trial-exhaustion-ticket-t-e97475-pending/169010"),
        ("Access is paid plans, not legacy requests", "https://forum.cursor.com/t/cursor-says-grok-bot-is-included-with-pro-now-do-you-actually-have-access-yet/169808"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Access", "Grok Bot trial ended", lede, body, TRIAL_FAQS, related, sources)


# --- Privacy Mode --------------------------------------------------------

PRIVACY_FAQS = [
    ("Grok Bot is stuck on Connecting. What has to be saved?",
     "Privacy Mode, not Legacy, on the Cursor dashboard. Switching the control without saving does nothing. Until the save exists, Retry, Recover, Reset, and reinstall all fail."),
    ("Where is that setting?",
     "The reviewed notes say the Cursor dashboard, saved as Privacy Mode rather than Legacy. This handbook does not add a deeper click path than that."),
    ("createAgent failed and there is no Reset button. Is that the same bug?",
     "Not always. First setup can fail before a computer exists, so there is nothing to Reset. It can also be DNS. Match the sentence. If it says Can&#x27;t reach, run the DNS test after Privacy Mode is saved."),
    ("Should I make a second Cursor user?",
     "No. A second user is a second account, not a fix for an unsaved privacy choice on the first one."),
]

def privacy_mode():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Connecting that never finishes, from staff notes already used on <a href="/troubleshooting/stuck/">stuck</a> and <a href="/learn/login/">login</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot stuck on Connecting, on a new account, usually means Privacy Mode was never saved.</strong> Legacy Privacy Mode blocks the cloud computer. Save Privacy Mode on the Cursor dashboard, fully quit, and reopen. Reset cannot save that setting.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>Grok Bot needs cloud storage for the computer. Legacy Privacy Mode blocks that storage. The dashboard control can look switched while the account is still on Legacy, because the choice was not saved. New Cursor accounts are the ones that sit on Connecting forever in this state. The app will offer Retry, Recover, and Reset. All three fail, and a reinstall fails, until the saved choice exists. You are rebuilding a machine the account is not allowed to create.</p>
<p>A cousin bug is first-setup createAgent. Staff said that call can fail before a computer exists, which is why Reset is missing, and they also said bad DNS for cursorvm.com can block the computer while other Cursor API calls still work. Read the sentence. Connecting with no computer yet is this page. Can&#x27;t reach after a computer should have been created is <a href="/troubleshooting/dns-error/">DNS</a> once Privacy Mode is actually saved.</p>
<h2>What to do</h2>
<ol>
<li>Open the Cursor dashboard and save Privacy Mode. Not Legacy. Saving is the step. Toggling and closing the tab is how people repeat the hour.</li>
<li>Fully quit Grok Bot. Menu-bar Quit on macOS. Tray quit on Windows. Then open the app and let the Cursor login finish, including company SSO if the account requires it.</li>
<li>Do not create a second Cursor user to skip the spinner. Do not Reset. There is often no computer yet, and Reset does not write the privacy choice.</li>
<li>If Connecting continues after a confirmed save and a real quit, stop changing accounts. Check <a href="/troubleshooting/no-seat/">no seat</a> if the label changed to Setting up, and <a href="/learn/login/">login</a> if the browser popup never returned.</li>
</ol>
<h2>What still fails until the save exists</h2>
<p>Once a computer exists, the official order is Retry, restart the app, check for an app update, then Update under Grok Bot&#x27;s Computer, and Reset last. On Connecting, that order does not apply yet. Retry, Recover, and Reset all return to the same spinner because the account still has no cloud storage. Reinstalling the Mac or Windows package leaves the Cursor account untouched, so the spinner comes back. Finish the Cursor browser popup, including company SSO if the account requires it, and return to the app. A popup that never comes back is the login page.</p>
<h2>Limits</h2>
<ul>
<li>This page does not document a menu inside the Grok Bot app that replaces the Cursor dashboard save. The reviewed instruction is the dashboard.</li>
<li>Privacy Mode is not the weekly usage meter and not an ended trial. Those silences happen after a computer exists.</li>
<li>A stale session after a password change says the account is unavailable. That is <a href="/troubleshooting/account-unavailable/">account unavailable</a>, not Legacy mode.</li>
<li>The stuck page still owns the other labels: Setting up, Cleaning up, and 50 percent Starting. Use it when the words are not Connecting.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Index if the label changed."),
        ("/troubleshooting/stuck/", "Stuck", "Setting up, Cleaning up, and 50 percent."),
        ("/learn/login/", "Cursor login", "Popup, SSO, and which account you sign in."),
        ("/troubleshooting/no-seat/", "No seat", "Setting up on a free plan after login works."),
        ("/troubleshooting/dns-error/", "DNS error", "createAgent that is actually a subdomain lookup."),
    ]
    sources = [
        ("Cursor getting started", "https://cursor.com/help/grok-bot/getting-started"),
        ("First setup, createAgent, DNS", "https://forum.cursor.com/t/grok-bot-0-23-0-first-setup-fails-createagent-can-t-reach-your-computer/169007"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Privacy", "Grok Bot stuck on Connecting", lede, body, PRIVACY_FAQS, related, sources)


# --- No seat -------------------------------------------------------------

SEAT_FAQS = [
    ("I am on the free Cursor plan and Grok Bot spins on Setting up. Is my network down?",
     "No. A free plan does not get a hosted computer. Staff called the spinner, instead of an access message, a known copy bug."),
    ("I am a team admin. Why is there still no computer?",
     "Admin is not a seat. Grok Bot is included with a paid team seat, Standard or Premium, not with the admin role. Assign yourself a seat under Cursor dashboard Members, fully quit, and reopen. Or sign in with an account that already has a seat."),
    ("Will a new download create the computer?",
     "No. Install the official app only after a seat exists. Until then every DNS test is noise."),
    ("Where are the plan names written down?",
     "On the pricing page, as a dated snapshot of official sources. This page does not repeat prices or add a free tier."),
]

def no_seat():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Missing-computer notes from staff. Plan names: <a href="/pricing/">pricing</a>. A white window with a local config folder is a different bug: <a href="/troubleshooting/white-screen/">white screen</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot stuck on Setting up, on a free plan or a team admin with no seat, means no computer was provisioned.</strong> The black spinner is not your Wi-Fi. Assign a real seat, fully quit, and reopen.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>The hosted computer is created for an account that includes Grok Bot. A free Cursor plan does not get one. The app can still sit on Setting up your Grok Bot, or a black loading screen, because the copy never says access is missing. Staff called that a known UX bug on the 0.30.0 Mac report. The same black screen happens when the signed-in user is a team admin and nobody assigned them a paid team seat. Standard or Premium is the seat. The admin role is not.</p>
<p>That is the opposite of a paid seat whose desktop cannot resolve cursorvm.com. In the DNS case the computer exists and iOS on the same account often still works. In the no-seat case there is no machine to wake, so a hotspot changes nothing, and Reset has nothing to rebuild. Legacy request-based pricing is a third gate: staff said those accounts do not get Grok Bot unless they opt into usage-based pricing. The dated list of who is included is on the pricing page, not here.</p>
<h2>What to do</h2>
<ol>
<li>Look at the Cursor account before you touch DNS. Free plan, or a team member with no seat, stops the diagnosis.</li>
<li>On a team: Cursor dashboard, Members, assign yourself a Standard or Premium seat. Fully quit Grok Bot and reopen. Or sign in with an account that already has a seat.</li>
<li>On a free individual plan: a download from x.ai/bot will not provision the machine. Use <a href="/pricing/">pricing</a> to see which paid Cursor plans and which SuperGrok links include access. Then quit and reopen after the account actually has it.</li>
<li>If you had a working roster yesterday, you are not in this case unless the plan or the seat changed. An empty list after sleep is <a href="/troubleshooting/white-screen/">white screen</a>. A paid seat that cannot resolve the subdomain is <a href="/troubleshooting/dns-error/">DNS</a>.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not invent a free tier, a promo code, or a price. Enterprise&#x27;s early-September 2026 two-week org trial is a dated announcement on the pricing page. That window is expired there, and it was never described as a consumer free tier.</li>
<li>Connecting forever on a brand-new account that has not saved Privacy Mode is the previous page, even if you do have a seat.</li>
<li>An ended trial on an account that used to work is <a href="/troubleshooting/trial-ended/">trial ended</a>. Export first. The spinner on a never-provisioned account has nothing to export.</li>
<li>Do not Reset. There is no computer, and the button will not create a seat.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Index of labels that mean a computer does exist."),
        ("/pricing/", "Pricing", "Which accounts include Grok Bot."),
        ("/troubleshooting/privacy-mode/", "Privacy Mode", "Connecting forever before a computer can be created."),
        ("/troubleshooting/trial-ended/", "Trial ended", "Access that used to work and then stopped."),
        ("/troubleshooting/white-screen/", "White or black screen", "Local config and a sleeping computer, after a seat exists."),
    ]
    sources = [
        ("Free plan spinner", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-setting-up-your-grok-bot-on-macos/169981"),
        ("Admin without a seat", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-during-initial-setup-on-mac/170251"),
        ("Paid plans, not legacy requests", "https://forum.cursor.com/t/cursor-says-grok-bot-is-included-with-pro-now-do-you-actually-have-access-yet/169808"),
        ("Plans and billing", CURSOR_PLANS),
    ]
    return _page("Seat", "Grok Bot stuck on Setting up", lede, body, SEAT_FAQS, related, sources)


# --- Antivirus -----------------------------------------------------------

AV_FAQS = [
    ("The browser works. Why does Grok Bot fail?",
     "Encrypted-connection scanning swaps the certificate issuer. Grok Bot trusts public certificate authorities only. The browser can accept the scanner&#x27;s certificate. The app does not."),
    ("Which products do the notes name?",
     "Kaspersky, ESET, Avast, AVG, Bitdefender, Norton, Trend Micro, Sophos, and similar HTTPS scanners. Zscaler is called out separately as a tunnel that can stay up on a hotspot."),
    ("What is the test that avoids guessing?",
     "A phone hotspot on another carrier, with the scanner and the company tunnel paused. If that path works, stop resetting the computer."),
    ("Should I install a certificate inside the Agent Computer?",
     "No. Do not install a VPN, proxy, or DNS changer on the hosted computer. Exclude Grok Bot on the desktop, or turn the scanning off, then fully quit and reopen."),
]

def antivirus():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. HTTPS-scanning notes already used on <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a>. This is not the Windows system-proxy case.</p>
<div class="callout warn">
<p><strong>Antivirus HTTPS scanning can break Grok Bot while every site still loads in the browser.</strong> The app trusts public certificate authorities only. Turn off encrypted-connection scanning or exclude Grok Bot, fully quit, and reopen.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>Scanners that inspect HTTPS present their own certificate. Browsers are often configured to trust that local issuer. Grok Bot is not. Staff and the troubleshooting notes name Kaspersky, ESET, Avast, AVG, Bitdefender, Norton, Trend Micro, Sophos, and similar products. The symptom is Can&#x27;t reach, a failed setup, or a socket the browser does not see, on a network where ordinary pages work.</p>
<p>Company tunnels overlap this and are not the same checkbox. Zscaler Client Connector has left Windows 11 on a black spinner on both the office LAN and a phone hotspot, because the tunnel was still up on the hotspot. Staff said to quit Grok Bot, pause or disable Zscaler, and relaunch, and to ask IT to allowlist or exclude SSL inspection for <code>*.cursorvm.com</code> and <code>**.cursorvm.com</code>. Both wildcard levels are in that note. Cloudflare WARP has produced a blank screen by intercepting the same traffic, including on a hotspot. Builds after 0.28.0 are described as showing an error and retry instead of a blank screen. This page does not claim your build number.</p>
<h2>What to do</h2>
<ol>
<li>Fully quit Grok Bot before you change the scanner. Otherwise you are testing a process that still holds the old connection.</li>
<li>Turn off encrypted-connection scanning, SSL scanning, or the product&#x27;s equivalent, or exclude the Grok Bot app. Then reopen.</li>
<li>If a company tunnel is installed, pause it and retry. For Zscaler, ask IT for the two cursorvm.com wildcard exclusions above rather than Reset.</li>
<li>For WARP, turn it off or use the split-tunnel or excluded-route control the blank-screen thread names. A hotspot that still runs WARP is not a clean test.</li>
<li>A clean hotspot on another carrier, with the scanner and the tunnel paused, is the A/B test. If it works, the computer is fine. Continue on <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a> only for the button order, not for another Reset.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>Do not install the scanner&#x27;s root certificate onto the Agent Computer, and do not install a VPN there to escape the scanner. A bot-installed VPN can disconnect every bot until Recover.</li>
<li>DNS Query refused is a different failure. Fixing a certificate will not make a subdomain resolve. See <a href="/troubleshooting/dns-error/">DNS error</a>.</li>
<li>Windows ignoring the system proxy is <a href="/troubleshooting/windows-proxy/">Windows proxy</a>. TUN mode is that page.</li>
<li>A white flash and the Windows process exiting can be endpoint security or a locked %APPDATA% folder. That local case is on <a href="/troubleshooting/install-failed/">install failed</a>. The cloud computer in that report was healthy.</li>
<li>This page does not rank antivirus products or claim a specific exclusion checkbox name beyond the scanning behavior staff described.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Start here if the screen is not a certificate error."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "Retry and Recover before you blame the scanner."),
        ("/troubleshooting/dns-error/", "DNS error", "Subdomain lookup, when the issuer is not the problem."),
        ("/troubleshooting/windows-proxy/", "Windows proxy", "Direct connection versus a local HTTP proxy."),
        ("/troubleshooting/white-screen/", "Blank screen", "WARP can paint a blank window."),
    ]
    sources = [
        ("Official troubleshooting", DOC_TROUBLE),
        ("Zscaler on LAN and hotspot", "https://forum.cursor.com/t/grok-bot-0-30-0-stuck-on-black-loading-screen-on-windows-11/170294"),
        ("WARP blank screen", "https://forum.cursor.com/t/blank-screen-after-opening-grok-bot/169966"),
        ("Windows process exits, endpoint security", "https://forum.cursor.com/t/grok-bot-0-24-0-windows-10-x64-white-screen-flashes-then-app-closes/169380"),
    ]
    return _page("Antivirus", "Grok Bot blocked by antivirus", lede, body, AV_FAQS, related, sources)


# --- Windows proxy -------------------------------------------------------

PROXY_FAQS = [
    ("Does Grok Bot use the Windows system proxy?",
     "No. Staff say it connects directly to the Agent Computer. A local HTTP proxy such as 127.0.0.1:7890 is ignored. DNS and browser checks that go through the proxy can pass while the app fails."),
    ("What does the curl probe mean?",
     "After TUN mode is on, curl.exe --noproxy * -I against https://test123.us10.cursorvm.com should return quickly with HTTP/1.1 404 Not Found and Server: awselb/2.0. The 404 is success. The hostname is only a probe. A hang or a reset means the app will fail the same way."),
    ("Which region string do I use?",
     "The staff thread that confirmed TUN used us10, and noted the region may be us10 rather than us8. This page does not invent other region codes."),
    ("Can I put that proxy on the Agent Computer instead?",
     "No. Never install a VPN, proxy, or DNS changer inside the Agent Computer. A bot-installed VPN can cut the always-on path until Recover."),
]

def windows_proxy():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. The direct-connection test from the Windows staff thread, also summarized on <a href="/learn/windows-download/">Windows download</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot on Windows ignores the system proxy and connects directly.</strong> Switch the tunnel from system-proxy mode to TUN, fully quit the app, and run the noproxy probe. A fast 404 from awselb means the path works.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>People prove the network with a browser, or with curl that inherits the system proxy, and then watch setup fail with Can&#x27;t reach your computer. Staff said the computer on their side was up, and recreating it does not help, because the Windows app never used that proxy. It connects directly. TUN mode, also called Enhanced, Global, or a virtual network adapter, captures traffic at the adapter so the direct connection is inside the tunnel. System-proxy mode does not.</p>
<p>A fresh Windows profile can hit this after a backend fix, which makes it look like a bad install. Two installed copies can also end on the same sentence. Remove the older copy first, on <a href="/troubleshooting/install-failed/">install failed</a>, so you are not debugging a proxy with the wrong binary.</p>
<h2>What to do</h2>
<ol>
<li>Fully quit Grok Bot, including the tray.</li>
<li>Switch the VPN or proxy from system-proxy mode to TUN. Do not install that tunnel inside the Agent Computer.</li>
<li>In PowerShell, run the staff probe. The confirmed hostname in the thread that fixed setup was <code>test123.us10.cursorvm.com</code>:</li>
</ol>
<pre><code>curl.exe --noproxy "*" -I https://test123.us10.cursorvm.com</code></pre>
<ol start="4">
<li>A quick <code>HTTP/1.1 404 Not Found</code> with <code>Server: awselb/2.0</code> means the load balancer answered. Open Grok Bot. A hang, timeout, or connection reset means the app will fail until TUN or the path changes.</li>
<li>If the probe works and the app still fails, check IPv4 and IPv6 DNS. Query refused on a cursorvm.com subdomain while the apex works is <a href="/troubleshooting/dns-error/">DNS error</a>, including when the region in the name is us8 rather than us10.</li>
<li>If a Zscaler-style tunnel is what your network requires, pausing it is <a href="/troubleshooting/antivirus/">antivirus and tunnels</a>, not another proxy mode.</li>
</ol>
<h2>A passing probe is not the whole diagnosis</h2>
<p>The 404 only means a direct connection reached a cursorvm.com load balancer. It does not mean a seat exists, that Privacy Mode is saved, or that a trial is still active. If the probe hangs, fix TUN before you open Grok Bot again. If the probe is fast and the app still says Can&#x27;t reach, read the DNS page: Query refused on a subdomain while the apex works. The TUN thread used us10. The Query refused thread used us8. This page does not add another region code. Two copies under Installed apps can fail with the same sentence. Remove the older copy before you blame the tunnel.</p>
<h2>Limits</h2>
<ul>
<li>The 404 is not a Grok Bot outage. The probe host is not your computer.</li>
<li>This page does not add proxy software, a port, or a region besides us10 and the us8 name already used in the DNS thread.</li>
<li>Mac and phone clients are not this Windows direct-connect note. A phone hotspot is still the clean A/B test on every platform.</li>
<li>Reset stays last. A rebuilt computer still has to be reached directly.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "If the label is not a Windows network failure."),
        ("/learn/windows-download/", "Windows download", "x64 or Arm64 and a single installed copy."),
        ("/troubleshooting/dns-error/", "DNS error", "Subdomain Query refused after the direct path works."),
        ("/troubleshooting/antivirus/", "Antivirus", "HTTPS scanning and Zscaler."),
        ("/troubleshooting/cant-reach/", "Can&#x27;t reach", "The button order around this probe."),
    ]
    sources = [
        ("Windows app ignores the system proxy", "https://forum.cursor.com/t/grok-bot-windows-fresh-profile-setup-fails-with-can-t-reach-your-computer-after-backend-fix/170281"),
        ("Query refused, us8 probe", "https://forum.cursor.com/t/grok-bot-0-30-0-windows-setup-fails-with-cant-reach-your-computer-all-network-checks-pass/170035"),
        ("Official troubleshooting", DOC_TROUBLE),
    ]
    return _page("Windows", "Grok Bot ignores the Windows system proxy", lede, body, PROXY_FAQS, related, sources)


# --- Cloud agent ---------------------------------------------------------

CLOUD_FAQS = [
    ("I launched a cloud agent from Grok Bot and cursor.com/agents is empty. Where is it?",
     "Enable Source, then Grok Bot. The agent is running under your account and stays hidden until that filter is on. Turn it on once per client: the website and the desktop sidebar are separate."),
    ("Open in Cursor did not open the desktop app. What did staff say?",
     "Middle-click Open in Cursor opens the same agent in the browser."),
    ("The agent started on Fast even though my default is not Fast.",
     "Staff: Grok-spawned agents can do that. Hover Cursor Grok 4.6, Edit, and uncheck Fast. Switch the follow-up box back if it flips."),
    ("Why is /review-bugbot missing?",
     "It is decided at create time and does not attach to agents Grok Bot created. Start a new agent from cursor.com/agents on the same PR branch and include /review-bugbot there."),
]

def cloud_agent():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Filter and billing notes from staff. The operator stack is <a href="/learn/ops/">X, Cursor, MCP</a>.</p>
<div class="callout">
<p><strong>A Grok Bot cloud agent that is missing in Cursor is usually hidden by the Source filter.</strong> Enable Source, then Grok Bot, on cursor.com/agents and again in the desktop sidebar. The agent was not deleted.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>Agents that Grok Bot launches run in your Cursor account. They keep running during the handoff. The agents list hides them until Source, then Grok Bot, is enabled. The filter is per client. Turning it on in the browser does not turn it on in the desktop sidebar, and the reverse is also true. People read an empty list as a failed launch and start a second agent.</p>
<p>Two other mismatches show up after the agent is visible. Unnamed-model agents use your Cloud Agent default, and Grok-spawned agents can still start in Fast when that default is not Fast. Usage for those agents bills Cursor plan usage, not the Grok Bot weekly chat pool. And /review or /review-bugbot does not attach to an agent Grok Bot created, because that choice is made at create time.</p>
<h2>What to do</h2>
<ol>
<li>Open cursor.com/agents and enable Source, then Grok Bot. Repeat in the desktop sidebar if that list is also empty.</li>
<li>Middle-click Open in Cursor when you want the browser view of the same agent.</li>
<li>If the run is on Fast against your wishes: hover Cursor Grok 4.6, choose Edit, uncheck Fast, and fix the follow-up box if it flips back.</li>
<li>For Bugbot, do not look for a toggle on the Grok-created agent. Start a new agent from cursor.com/agents on the same pull-request branch and include /review-bugbot in that run.</li>
<li>If the bot cannot see the repository at all, that is not a hidden agent. Grok Bot has no codebase plugin. See <a href="/troubleshooting/codebase/">codebase</a>.</li>
</ol>
<p>If the filter is already on and the row is still missing, check which Cursor account is signed in. A work login and a personal login do not share an agents list. Then check the other client. The website filter and the desktop sidebar filter are independent, so a list you fixed in the browser can still look empty in the IDE. Spend for that agent is Cursor plan usage, not the Grok Bot weekly chat pool. An empty chat meter is not proof the agent never started. An agent with no model name uses your Cloud Agent default.</p>
<h2>Limits</h2>
<ul>
<li>This page does not claim the filter survives a new browser profile. Staff said once per client.</li>
<li>Chat silence while an agent is running is <a href="/troubleshooting/usage-limit/">usage limit</a>, not a missing row.</li>
<li>There is no reviewed way to bolt /review-bugbot onto an agent that was already created by Grok Bot.</li>
<li>The official X plugin failing with tools=0 is <a href="/troubleshooting/plugin-oauth/">plugin OAuth</a>, not a missing agent row.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Chat and computer failures, separate from the agents list."),
        ("/learn/ops/", "X, Cursor, MCP", "How a brief becomes a Cloud Agent."),
        ("/troubleshooting/codebase/", "Codebase", "No repo index inside Grok Bot itself."),
        ("/troubleshooting/usage-limit/", "Usage limit", "Bot chat pool versus Cursor plan usage."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "GitHub header and the X plugin."),
    ]
    sources = [
        ("Source filter hides Grok-launched agents", "https://forum.cursor.com/t/cloud-agents-created-in-grok-bot-not-displayed-in-cursor/169939"),
        ("Source filter and Open in Cursor", "https://forum.cursor.com/t/grok-bot-open-cloud-agent-cards-in-the-browser-and-show-grok-launched-agents-on-agents/169754"),
        ("Fast default ignored", "https://forum.cursor.com/t/cloud-cursor-agents-spawned-by-grok-bot-do-not-fully-respect-the-user-selected-default-model-and-speed-preferences/169746"),
        ("/review-bugbot missing", "https://forum.cursor.com/t/review-bugbot-is-missing-on-cloud-agents-launched-from-grok-bot/170096"),
        ("Agent usage and model default", "https://forum.cursor.com/t/query-about-grok-bot-cursor-agent-usage-and-model-selection/169160"),
    ]
    return _page("Cloud Agent", "Grok Bot cloud agent not showing in Cursor", lede, body, CLOUD_FAQS, related, sources)


# --- Routines ------------------------------------------------------------

ROUTINE_FAQS = [
    ("The card says Next run: Run now, and it is late. Did I break the schedule by editing the bot?",
     "Staff: editing instructions, or which platform created the routine, does not break the schedule. A late slot usually fired and sat in a queue, often 10 to 37 minutes. Some runs finish without posting to chat."),
    ("Should I delete the routine and create it again?",
     "No. Staff said not to recreate it. Message the bot for an on-demand check-in."),
    ("Where is the webhook URL?",
     "On the desktop app only, on the trigger card, with the sender key. iOS does not show it. Keep the desktop app updated."),
    ("A routine that came due while I was out of weekly usage never ran later. Is the schedule broken?",
     "No. Routines due during a usage block are skipped. They do not queue up as a later batch of sends. Messages you already sent reply in a batch when usage returns. That split is the usage page."),
]

def routines():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Schedule notes from staff. How to save a routine in the first place is <a href="/learn/skills-routines/">skills and routines</a>.</p>
<div class="callout">
<p><strong>Grok Bot routines not running are often a queued slot, not a deleted schedule.</strong> Editing the bot does not break it. Do not recreate the routine. A run can finish without a chat message. The webhook URL exists only on desktop.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>A routine tells one bot when to work. The schedule can fire and then wait. Staff described late cards that still say Next run: Run now because the slot sat in a queue, often 10 to 37 minutes. Some of those runs finish and never post to the chat, so the bot looks idle after it already did the job. Editing the bot&#x27;s instructions, or creating the routine on a different platform, is not what breaks the clock.</p>
<p>Two other silences get blamed on the scheduler. If the weekly pool is empty, routines that come due during the block are skipped. They do not come back later as a surprise batch. And the webhook form is easy to miss: the POST URL and the sender key are on the desktop trigger card, not on iOS. A past webhook incident is also in the record. Staff saw POSTs to api2.cursor.sh return an internal error, rolled a change back, and the same request worked. This page does not claim that incident is still open.</p>
<h2>What to do</h2>
<ol>
<li>Read the card before you delete anything. If it is late and still says Run now, wait out the queue window staff described, then message the bot for an on-demand check-in.</li>
<li>Look in the computer or the files for a finished run that never posted. Absence of a chat line is not absence of a run.</li>
<li>Open Usage if several routines went quiet together. A full meter skips slots. Fix that on <a href="/troubleshooting/usage-limit/">usage limit</a>, not by cloning the routine.</li>
<li>For a webhook, use the desktop app. Open the trigger card for the URL and the sender key. Updating the phone app will not reveal them.</li>
<li>Bot-to-bot chatter is not a routine firing. Those messages still burn weekly usage, and telling them to stay quiet is only a hint. Idle specialists can be woken. That trap is the usage page.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not list cron syntax or a new scheduler UI. The product fields are the ones on the skills lesson.</li>
<li>An Approval needed tile that stays after the card timed out, about ten minutes with no answer, is a different stuck badge. Staff say open the agent and send a short message, or restart the app. The tile is supposed to clear when the card expires. There is not enough reviewed detail for a separate page.</li>
<li>A bot that never answers at all, with the computer view open, is <a href="/troubleshooting/not-responding/">not responding</a>.</li>
<li>Do not Reset the computer because a digest was late.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Index if the bot itself is down."),
        ("/learn/skills-routines/", "Skills and routines", "Save a method before you schedule it."),
        ("/troubleshooting/usage-limit/", "Usage limit", "Skipped slots during a full week."),
        ("/troubleshooting/phone-not-connecting/", "Phone", "Webhook URL is desktop-only."),
        ("/troubleshooting/not-responding/", "Not responding", "No replies at all, versus one late routine."),
    ]
    sources = [
        ("Routines sit in a queue", "https://forum.cursor.com/t/grok-bot-routines-dont-auto-run-on-schedule/170358"),
        ("Webhook URL is desktop-only", "https://forum.cursor.com/t/webhook-url-missing-on-ios/169589"),
        ("Webhook internal error was rolled back", "https://forum.cursor.com/t/grok-bot-webhooks-are-failing-with-internal-server-error/169323"),
        ("Bot-to-bot turns and skipped routines", "https://forum.cursor.com/t/grok-bot-weekly-usage-hits-100-after-bot-to-bot-reviews-the-user-asked-to-stop/170271"),
        ("Approval needed tile after a timeout", "https://forum.cursor.com/t/grok-bot-approval-needed-stays-on-agent-view-homepage-when-coder-has-nothing-to-approve/170127"),
    ]
    return _page("Routines", "Grok Bot routines not running", lede, body, ROUTINE_FAQS, related, sources)


# --- X login -------------------------------------------------------------

X_FAQS = [
    ("The cloud computer is locked out of X. Is my account broken?",
     "Not from this symptom alone. Staff and the handbook treat X login risk controls on the cloud computer as a known phenomenon. It is not proof the account is broken."),
    ("Should the bot install a VPN on its computer to get past the lock?",
     "No. A VPN installed inside the Agent Computer can cut the always-on path so every bot fails until Recover restores routing."),
    ("The official X plugin says connected but has zero tools. Same bug?",
     "No. That is plugin auth across desktop, Cloud Agents, and Grok Bot, waiting on X-side app config. There is no reviewed user workaround. Do not paste a token into chat."),
    ("Can I post from the bot while this is broken?",
     "The ops page&#x27;s rule stays: use the official X connector for research, keep drafts in /workspace, and publish yourself. This page does not add a bypass."),
]

def x_login():
    lede = '''
<p class="meta">Unofficial handbook, not xAI, Cursor, or X support. Lock and plugin notes from staff threads. How operators scout X is <a href="/learn/ops/">ops</a>.</p>
<div class="callout warn">
<p><strong>A Grok Bot X login lock means the cloud computer hit site risk controls.</strong> It does not prove the account is dead. Do not install a VPN on that computer. The official X plugin showing connected with zero tools is a separate outage with no user-side fix.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>The shared computer signs into websites with a browser that many bots reuse. X treats that environment like any other automated or unfamiliar client. Locks show up. The handbook&#x27;s failure notes call them a known phenomenon, not a theoretical one, and not a diagnosis that your password is wrong. Because every bot shares the browser, one locked session is the session the rest of the roster sees. A second bot is not a clean browser.</p>
<p>The official X plugin is a different door. Staff said connect and refresh were failing across the Cursor desktop, Cloud Agents, and Grok Bot, including the state connected but tools=0, with no clean workaround while X-side app config was fixed. Retrying Connect inside Grok Bot does not repair that vendor config. Pasting a bearer token into chat is the failure mode the plugin notes tell you to avoid.</p>
<h2>What to do</h2>
<ol>
<li>Stop if you were about to ask the bot to install a VPN, a proxy, or a new DNS resolver on its computer. Recover is how you undo that kind of routing damage, and it removes installed apps. Do not cause the outage you are trying to escape.</li>
<li>For a lock on the computer&#x27;s browser: take over the computer when the bot hands it to you, the same way you would for any site that wants a human. The computer lesson covers takeover for passwords, 2FA, and CAPTCHA. Do not paste passwords or one-time codes into ordinary chat. If the bot never offers takeover, the reviewed nudge is to ask it to hand you the computer, and to skip passkeys with Try another way. That nudge is a staff reply, not a guaranteed bypass of X&#x27;s lock.</li>
<li>For the plugin with zero tools: wait on the vendor fix. Use <a href="/troubleshooting/plugin-oauth/">plugin OAuth</a> for the other connectors, which do have user steps. X does not.</li>
<li>Keep drafts in /workspace and publish them yourself, which is the ops rule whether or not the plugin is healthy.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>This page does not claim a cooldown, a phone-number check, or an X setting that lifts the lock. Those steps are not in the reviewed notes.</li>
<li>Takeover that never appears is one staff thread, not a full login manual. Try another way is specifically the passkey skip they named.</li>
<li>A deleted Cursor account, or Too many computers, is <a href="/troubleshooting/account-unavailable/">account unavailable</a>. It is not an X risk control.</li>
<li>Reset will not unlock X, and it can drop unsynced work. Leave the computer buttons alone unless the computer itself is unreachable for a reason on <a href="/troubleshooting/cant-reach/">can&#x27;t reach</a>.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Non-X failures."),
        ("/learn/ops/", "Ops", "Scout X, draft in /workspace, you publish."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "Gmail, Notion, GitHub, Zoom, Canva, and the X plugin."),
        ("/learn/computer/", "Shared computer", "One browser profile for every bot."),
        ("/troubleshooting/account-unavailable/", "Account unavailable", "Cursor session and device limits."),
    ]
    sources = [
        ("X login lock on the computer", "https://forum.cursor.com/t/grok-bot-x-login-lock-limit-not-lifting/168541"),
        ("X plugin tools=0", "https://forum.cursor.com/t/official-x-plugin-auth-is-broken-on-cursor-cloud-grok-bot-and-desktop-refresh/169592"),
        ("Take over was not offered", "https://forum.cursor.com/t/grok-bot-failed-to-open-its-computer-and-couldnt-recognize-the-issue/169179"),
        ("Do not install a VPN on the computer", "https://forum.cursor.com/t/vpn-sso-passkey-and-yubikey-within-grokbot/170148"),
    ]
    return _page("X", "Grok Bot X login locked", lede, body, X_FAQS, related, sources)


# --- Account unavailable -------------------------------------------------

ACCOUNT_FAQS = [
    ("The Mac app says Grok Bot is not available on this account, but the web still shows my plan. What is that?",
     "Usually an expired desktop session after a password change. Log out from the bottom of that screen, fully quit, and sign in with the new password. Check Access, then download, is a misleading expired-session screen, not a missing entitlement."),
    ("Does signing out delete the computer?",
     "The reviewed password-change note says the cloud computer and the bots are still there. iOS Delete Account is different: that deletes the Cursor account plus agents, chats, and the computer. Desktop sign-out does not."),
    ("What is Too many computers?",
     "Staff: a Grok Bot login counts as its own Cursor device, and the cloud workspace can count as another one toward that limit. This handbook does not have a reviewed list of which device to remove."),
    ("I deleted the Cursor account and the Grok link is stuck. How do I relink it?",
     "The reviewed note says deletion can pin the bot to a dead Cursor identity. There is no recovery click-path in this handbook. Email hi@cursor.com. Do not create a second product account that this site does not document."),
]

def account_unavailable():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Session notes from staff, also summarized on <a href="/learn/login/">login</a>. Plan checks: <a href="/pricing/">pricing</a>.</p>
<div class="callout warn">
<p><strong>Grok Bot account unavailable after a password change is usually a stale desktop session.</strong> Log out, fully quit, and sign in again. The plan and the cloud computer are often still fine. Do not Reset to refresh a login.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>The desktop app keeps its own Cursor session. After a password reset, that session can expire while the website still shows SuperGrok or the Cursor plan, and while the cloud computer and the bots are intact. The app then says the product is not available on this account yet. Staff called Check Access, then download, a misleading screen for that expired session, not a missing entitlement.</p>
<p>Other account sentences are harsher. Delete Account on iOS deletes the Cursor account plus agents, chats, and the computer. The desktop app only signs out. There is no separate Grok Bot account underneath either action. A deleted Cursor account can also leave the Grok link pinned to a dead identity. And a Grok Bot login counts as a Cursor device, with the cloud workspace able to count as a second device, which is how people hit Too many computers without plugging in a laptop.</p>
<h2>What to do</h2>
<ol>
<li>If the screen appeared after a password change: log out from the bottom of that screen, Quit (on a Mac, Cmd+Q, not the window close), reopen, and sign in with the new password.</li>
<li>Do not download a second copy because Check Access offered a download. Finish the sign-in first. A missing seat is a different spinner, on <a href="/troubleshooting/no-seat/">no seat</a>, and an ended trial is <a href="/troubleshooting/trial-ended/">trial ended</a>.</li>
<li>If you wanted to leave, know which button you are pressing. iOS Delete Account is the destructive one. Desktop sign-out is not.</li>
<li>Too many computers: the reviewed fact stops at the device count. This site will not invent a devices page or tell you which session to revoke.</li>
<li>A link orphaned on a deleted Cursor account: email hi@cursor.com. Include the address you used and what you already deleted. No passwords or keys. There is no relink procedure in the reviewed notes.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>Signing out does not refill weekly usage and does not repair DNS.</li>
<li>Privacy Mode left on Legacy looks like Connecting, not like account unavailable. See <a href="/troubleshooting/privacy-mode/">Privacy Mode</a>.</li>
<li>This page does not claim that a stale session deletes chats. The password-change thread says the opposite: computer and bots were fine.</li>
<li>X locks and plugin failures are not this screen. They assume you are already signed in.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "Screens that happen after a good login."),
        ("/learn/login/", "Cursor login", "No second account, SSO, and the popup."),
        ("/pricing/", "Pricing", "If the account truly lacks access."),
        ("/troubleshooting/privacy-mode/", "Privacy Mode", "Connecting forever on a new account."),
        ("/troubleshooting/trial-ended/", "Trial ended", "Access ended, mislabeled as Can&#x27;t reach."),
    ]
    sources = [
        ("Stale session after a password change", "https://forum.cursor.com/t/grok-bot-mac-blocked-after-password-change-app-says-unavailable-spending-shows-supergrok-plus/170389"),
        ("Deleted Cursor account orphans the link", "https://forum.cursor.com/t/deleted-cursor-account-leaves-grok-link-orphaned-and-blocks-relinking/168783"),
        ("Too many computers", "https://forum.cursor.com/t/does-logging-into-grokbot-count-as-a-separate-computer/169289"),
        ("Cursor getting started", "https://cursor.com/help/grok-bot/getting-started"),
    ]
    return _page("Account", "Grok Bot account unavailable", lede, body, ACCOUNT_FAQS, related, sources)


# --- Codebase ------------------------------------------------------------

CODE_FAQS = [
    ("Does Grok Bot index my Cursor repo the way the IDE does?",
     "No. Staff: there is no codebase plugin, and Grok Bot does not index the repo. Coding work is handed to a Cursor Cloud Agent."),
    ("What has to be connected first?",
     "A GitHub-connected account. Staff point at Dashboard, then Integrations. An optional GitHub PAT connector is described for read-only use and for repos the agent creates. Origin is not available yet in that reply."),
    ("The agent ran and I cannot see it in Cursor.",
     "Enable Source, then Grok Bot. That filter page is cloud agent not showing. This page is only the missing index."),
    ("Can I point it at a localhost dev server instead?",
     "A localhost MCP on your PC is unreachable from the cloud computer. Company VPN sites need local execution on a machine already on the VPN, not a VPN client installed on the bot&#x27;s computer."),
]

def codebase():
    lede = '''
<p class="meta">Unofficial handbook, not xAI or Cursor support. Staff reply on repo access. How to brief an agent is <a href="/learn/ops/">ops</a>.</p>
<div class="callout">
<p><strong>Grok Bot cannot access your Cursor codebase by indexing it.</strong> There is no codebase plugin. Hand the coding job to a Cursor Cloud Agent on a GitHub-connected account. You still review the pull request.</p>
</div>
'''
    body = '''
<h2>Why it happens</h2>
<p>Grok Bot&#x27;s computer can use a browser, a terminal, and files under /workspace. That is not the Cursor IDE index of your repository. Staff said there is no codebase plugin and the bot does not index the repo. People who ask it to open the project the IDE already has open are asking for a connection that was never installed. The supported handoff is a Cursor Cloud Agent on an account that has GitHub connected.</p>
<p>The agent then has its own visibility bug. It runs, and cursor.com/agents hides it until you enable the Grok Bot source filter. That is <a href="/troubleshooting/cloud-agent/">cloud agent not showing</a>. Billing is also separate: the agent spends Cursor plan usage, not the Grok Bot weekly chat pool. A GitHub connector that says Connected and then fails with a badly formatted Authorization header is <a href="/troubleshooting/plugin-oauth/">plugin OAuth</a>, which you fix by removing the account and signing in again, not by Reset.</p>
<h2>What to do</h2>
<ol>
<li>Connect GitHub on the Cursor account. The staff path is Dashboard, then Integrations.</li>
<li>Ask the bot for a Cloud Agent on that repo, with a brief in /workspace. The ops lesson is the shape of that brief. Cursor opens the pull request. You merge.</li>
<li>If you need read-only access, or a repo created from scratch, the same staff reply allows an optional GitHub PAT connector for that. Do not paste the token into chat. Use the connector. Origin access was not available in that reply. This page will not pretend it shipped later.</li>
<li>Open the agents list and enable Source, then Grok Bot, or you will think the handoff did nothing. The filter steps are on <a href="/troubleshooting/cloud-agent/">cloud agent not showing</a>.</li>
<li>For /review-bugbot, start the agent from cursor.com/agents on the branch. Agents created by Grok Bot do not get that command attached.</li>
</ol>
<h2>Limits</h2>
<ul>
<li>Local stdio MCP, including a notes tool that only runs on your laptop, cannot be attached. Public HTTPS MCP is the supported add. There is no custom-connector settings form. You ask the bot in chat.</li>
<li>Internal sites that require a corporate VPN are not reachable by installing a VPN on the cloud computer. Use Execution on Local Computer on a machine that already has the VPN. See <a href="/troubleshooting/local-execution/">local computer</a>.</li>
<li>Template share links copy identity, skills, and routines, not your computer and logins. A separate staff bug: template preview lists skills, but import does not apply them, because the export ships an empty skills list. Until that is fixed, copy the skill body from the preview and ask the new bot to recreate it. That is not codebase access, and it is too narrow for its own URL.</li>
<li>This page does not invent a codebase toggle inside Grok Bot settings.</li>
</ul>
<p>Hub: <a href="/troubleshooting/">Grok Bot not working</a>.</p>
'''
    related = [
        ("/troubleshooting/", "Not working", "If the computer itself will not open, start there."),
        ("/learn/ops/", "Ops", "Brief a Cloud Agent and keep the merge."),
        ("/troubleshooting/cloud-agent/", "Cloud agent missing", "Source filter, Fast, and /review-bugbot."),
        ("/troubleshooting/plugin-oauth/", "Plugin OAuth", "GitHub connected with a bad Authorization header."),
        ("/troubleshooting/local-execution/", "Local computer", "VPN-only sites and localhost MCP."),
    ]
    sources = [
        ("No codebase plugin", "https://forum.cursor.com/t/does-grokbot-not-have-access-to-my-cursor-codebase/169684"),
        ("Agents hidden until Source is Grok Bot", "https://forum.cursor.com/t/cloud-agents-created-in-grok-bot-not-displayed-in-cursor/169939"),
        ("/review-bugbot is create-time", "https://forum.cursor.com/t/review-bugbot-is-missing-on-cloud-agents-launched-from-grok-bot/170096"),
        ("Custom MCP is chat, not a settings form", "https://forum.cursor.com/t/grokbot-custom-connectors/169965"),
        ("Template skills are not imported", "https://forum.cursor.com/t/grok-bot-templates-preview-shows-skills-but-the-export-ships-skills-skills-are-never-delivered/169911"),
    ]
    return _page("Codebase", "Grok Bot cannot access your Cursor codebase", lede, body, CODE_FAQS, related, sources)


ERRORS = [
    _spec(
        "/troubleshooting/dns-error/",
        dns_error,
        DNS_FAQS,
        (
            "Fix a Grok Bot DNS error",
            "Quit, compare a phone hotspot, then set public DNS on IPv4 and IPv6.",
            [
                ("Fully quit and Retry", "Menu-bar or tray quit. Reset stays last."),
                ("Compare a phone hotspot", "If the hotspot works, the resolver is the fault."),
                ("Set DNS on IPv4 and IPv6", "Staff point at 1.1.1.1 and 8.8.8.8. Router advertisements can keep the ISP resolver."),
                ("Look up a cursorvm.com subdomain", "Query refused on the subdomain while the apex works is the failure."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/plugin-oauth/",
        plugin_oauth,
        OAUTH_FAQS,
        (
            "Fix a Grok Bot plugin OAuth failure",
            "Use the connector-specific step. Do not paste a bearer token into chat.",
            [
                ("Reopen the auth tab", "Waiting for authorization means the browser tab was lost."),
                ("Re-authenticate Notion", "Connect again replays the stored redirect."),
                ("Authorize Gmail from Cursor", "That connection is shared into Grok Bot."),
                ("Remove and reconnect GitHub", "Press and hold the account, then Remove, when the header is badly formatted."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/usage-limit/",
        usage_limit,
        USAGE_FAQS,
        (
            "Check a Grok Bot usage limit",
            "Read the weekly meter before you enable On-Demand or press Reset.",
            [
                ("Open Usage", "The app often omits the limit banner."),
                ("Wait or set a cap", "A zero On-Demand cap blocks paid spillover and does not block credits."),
                ("Shrink bot-to-bot chatter", "Each bot-to-bot message spends a weekly turn."),
                ("Do not Reset", "Reset does not refill the meter."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/install-failed/",
        install_failed,
        INSTALL_FAQS,
        (
            "Fix a failed Grok Bot install",
            "Match the Mac chip or the Windows architecture, then sign in. A missing seat is not a bad file.",
            [
                ("Download from x.ai/bot", "The top Mac button is Apple silicon. Intel is under More downloads."),
                ("Keep one Windows copy", "Uninstall the older install, then quit the tray."),
                ("Rename local config if the window is white", "Reinstall does not clear that folder."),
                ("Stop if there is no seat", "A free plan never gets a computer."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/update-failed/",
        update_failed,
        UPDATE_FAQS,
        (
            "Finish a Grok Bot update",
            "Tell the app update from the computer update. Keep waiting on a slow computer image.",
            [
                ("Check which control you used", "Check for Updates restarts the app. Update under Grok Bot Computer replaces the image."),
                ("Keep waiting", "Do not start a second update while one is running."),
                ("Sign in again if Recover will not start", "Those buttons need a live session."),
                ("Reinstall packages after", "Synced bots and files stay. Installed apps do not."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/phone-not-connecting/",
        phone_not_connecting,
        PHONE_FAQS,
        (
            "Connect the Grok Bot phone app to the shared computer",
            "Use the same Cursor account. If the phone works, do not Reset the desktop.",
            [
                ("Sign in with the same Cursor account", "A second account is an empty roster."),
                ("Trust a working iPhone", "Desktop-only failure means the bots are still there."),
                ("Hold off when both devices fail on cellular", "Staff treat that as server-side."),
                ("Use desktop for webhooks and Always Allow", "Those controls are not on iOS."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/local-execution/",
        local_execution,
        LOCAL_FAQS,
        (
            "Reconnect Grok Bot local execution",
            "Quit the desktop helper. Do not Reset the cloud computer for an offline laptop.",
            [
                ("Fully quit and reopen", "The helper can register and then drop."),
                ("On Windows, end the leftover daemon", "Tray quit, then Task Manager, then wait about a minute."),
                ("Set Always Allow on that desktop", "iOS can only approve one action at a time."),
                ("Leave the cloud VPN uninstalled", "A VPN on the Agent Computer can take every bot offline."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/linux/",
        linux_not_connecting,
        LINUX_FAQS,
        (
            "Fix Grok Bot on Linux",
            "Use the official package, then the keyring workaround for empty ListMachines.",
            [
                ("Install deb, rpm, or AppImage from x.ai/bot", "Reject the old 0.18 build instead of debugging its network."),
                ("Unlock gnome-keyring or KWallet", "Then fully quit leftover processes and relaunch."),
                ("Do not attach local MCP", "The cloud computer cannot see stdio on the PC."),
                ("Treat community ports as unofficial", "They are not Cursor support."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/trial-ended/",
        trial_ended,
        TRIAL_FAQS,
        (
            "Recover access after a Grok Bot trial ends",
            "Export while the computer view opens. Do not Reset to save a trial.",
            [
                ("Export before Reset", "Trial end does not delete data. Reset can."),
                ("Read the plan, not the DNS error", "Can&#x27;t reach can be a display bug when access has ended."),
                ("Restore access, then quit", "A plan that includes Grok Bot, or a SuperGrok link on the same email."),
                ("Separate a full week from an ended trial", "The weekly meter is a different silence."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/privacy-mode/",
        privacy_mode,
        PRIVACY_FAQS,
        (
            "Unstick Grok Bot on Connecting",
            "Save Privacy Mode on the Cursor dashboard, then fully quit.",
            [
                ("Save Privacy Mode, not Legacy", "The dashboard save is the step that matters."),
                ("Fully quit and reopen", "Retry and Reset do not write that setting."),
                ("Do not create a second Cursor user", "That is a different account."),
                ("Match createAgent to DNS only after the save", "A missing computer is not a resolver bug."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/no-seat/",
        no_seat,
        SEAT_FAQS,
        (
            "Fix Grok Bot stuck on Setting up",
            "Provision a seat. The spinner is not a network test.",
            [
                ("Check for a free plan or a missing team seat", "Admin is not a computer."),
                ("Assign a Standard or Premium seat", "Cursor dashboard, Members, then quit and reopen."),
                ("Do not redownload the app first", "The installer cannot create a seat."),
                ("Do not Reset", "There is no computer to rebuild."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/antivirus/",
        antivirus,
        AV_FAQS,
        (
            "Unblock Grok Bot from HTTPS scanning",
            "Exclude the app or pause SSL inspection, then quit and reopen.",
            [
                ("Quit Grok Bot", "Change the scanner only after the process is gone."),
                ("Turn off HTTPS scanning or exclude the app", "The app trusts public certificate authorities only."),
                ("Pause Zscaler or WARP if they are in the path", "A hotspot that still tunnels is not a clean test."),
                ("Stop if the hotspot works", "Do not Reset a computer the clean path can reach."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/windows-proxy/",
        windows_proxy,
        PROXY_FAQS,
        (
            "Test Grok Bot when Windows proxy mode fails",
            "Use TUN, then the noproxy curl probe, before Reset.",
            [
                ("Quit the tray", "The app connects directly and ignores the system proxy."),
                ("Switch the tunnel to TUN", "System-proxy mode does not capture that direct connection."),
                ("Run the noproxy probe", "A fast 404 from awselb means the path works."),
                ("Do not install the proxy on the Agent Computer", "That can take every bot offline."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/cloud-agent/",
        cloud_agent,
        CLOUD_FAQS,
        (
            "Find a Cloud Agent launched by Grok Bot",
            "Enable the Grok Bot source filter on each Cursor client.",
            [
                ("Open cursor.com/agents", "The agent is hidden, not deleted."),
                ("Enable Source, then Grok Bot", "Repeat in the desktop sidebar. The filter is per client."),
                ("Uncheck Fast if the run ignored your default", "Hover Cursor Grok 4.6, then Edit."),
                ("Start Bugbot from cursor.com/agents", "Grok-created agents do not get /review-bugbot."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/routines/",
        routines,
        ROUTINE_FAQS,
        (
            "Check a Grok Bot routine that did not speak",
            "Wait out a queued slot before you recreate the routine.",
            [
                ("Read Next run", "A late Run now often means the slot is queued."),
                ("Look for a finished run with no chat line", "Some runs never post."),
                ("Check Usage", "A full week skips routines instead of delaying them."),
                ("Open the webhook on desktop", "iOS does not show the URL or the sender key."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/x-login/",
        x_login,
        X_FAQS,
        (
            "Handle a Grok Bot X login lock",
            "Do not install a VPN on the computer. Do not paste a token for the plugin.",
            [
                ("Treat the lock as a risk control", "It is not proof the account is broken."),
                ("Do not install a VPN on the Agent Computer", "Recover is how that damage gets undone."),
                ("Ask for takeover if the bot never offers it", "Skip passkeys with Try another way."),
                ("Leave the X plugin alone if tools equal zero", "There is no reviewed user fix."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/account-unavailable/",
        account_unavailable,
        ACCOUNT_FAQS,
        (
            "Clear Grok Bot account unavailable",
            "Log out of a stale session and sign in. Do not Reset.",
            [
                ("Log out from the unavailable screen", "Then fully quit. On a Mac that is Cmd+Q."),
                ("Sign in with the new password", "The plan on the website can be fine the whole time."),
                ("Do not follow Check Access into a second download", "That screen is a stale session."),
                ("Email support for an orphaned link", "A deleted Cursor account has no reviewed relink steps here."),
            ],
        ),
    ),
    _spec(
        "/troubleshooting/codebase/",
        codebase,
        CODE_FAQS,
        (
            "Reach a repo from Grok Bot",
            "Use a Cursor Cloud Agent on a GitHub-connected account. Grok Bot does not index the codebase.",
            [
                ("Connect GitHub", "Dashboard, then Integrations."),
                ("Brief a Cloud Agent", "The pull request stays yours to merge."),
                ("Enable the Grok Bot source filter", "Otherwise the agents list looks empty."),
                ("Keep tokens out of chat", "Use the PAT connector for the read-only case staff described."),
            ],
        ),
    ),
]

