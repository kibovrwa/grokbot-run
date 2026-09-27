# -*- coding: utf-8 -*-
from html import escape


def guides_block(items):
    """Back-links from a tool or lesson page to the guides that hand off to it."""
    lis = []
    for href, label, note in items:
        lis.append(
            "<li><a href=\"%s\">%s</a> — %s</li>"
            % (escape(href, quote=True), escape(label), escape(note))
        )
    return "<h2>Guides</h2><ul>%s</ul>" % "".join(lis)


INSTALL_GUIDES = guides_block([
    ("/troubleshooting/install-failed/", "Install failed on Mac or Windows", "Wrong chip, a second Windows copy, or a computer that was never provisioned."),
    ("/troubleshooting/uninstall/", "How to uninstall Grok Bot", "Removing the app is not deleting the Cursor account."),
])

PLUGINS_GUIDES = guides_block([
    ("/troubleshooting/plugin-oauth/", "Plugin OAuth failed", "Gmail, Notion, GitHub, Zoom 4700, Canva, and X."),
])

COST_GUIDES = guides_block([
    ("/troubleshooting/usage-limit/", "Usage limit and On-Demand", "Silent bots while the computer still opens. No prices on that page."),
])

PRICING_GUIDES = guides_block([
    ("/learn/is-grok-bot-free/", "Is Grok Bot free", "Access and the trial, without a second price table."),
])

COMPUTER_GUIDES = guides_block([
    ("/troubleshooting/local-computer/", "Local computer not connected", "The helper on your machine, not a dead cloud computer."),
    ("/troubleshooting/approval-stuck/", "Approval needed stuck", "A timed-out card, or an Ask first rule."),
    ("/troubleshooting/attachment/", "Attachment cannot be read", "Size, encryption, and the thumbnail."),
    ("/troubleshooting/waiting-for-login/", "Stuck waiting for login", "Take over the computer. Do not paste a password."),
])

SKILLS_GUIDES = guides_block([
    ("/troubleshooting/routine-did-not-run/", "Routine did not run", "Schedule, usage pause, or a run sitting in the queue."),
])

PHONE_GUIDES = guides_block([
    ("/troubleshooting/phone-not-connecting/", "Phone app not connecting", "The phone shares the cloud computer. It does not attach to the laptop."),
])

LOGIN_GUIDES = guides_block([
    ("/troubleshooting/sign-in/", "Sign-in does not complete", "Lost browser popup, Privacy Mode, or an expired Mac session."),
])

REACH_GUIDES = guides_block([
    ("/troubleshooting/dns-error/", "DNS error", "Subdomain lookup under cursorvm.com, IPv4 and IPv6."),
])

RECOVER_GUIDES = guides_block([
    ("/troubleshooting/update-failed/", "Update failed", "App update versus computer update. Backup not ready means wait."),
])

LINUX_GUIDES = guides_block([
    ("/troubleshooting/linux-setup/", "Linux setup failed", "Official deb, rpm, and AppImage before a community port."),
])
