# -*- coding: utf-8 -*-
"""About, privacy, terms, and contact. Unofficial handbook. No invented operators."""

ABOUT_FAQS = [
    ("Is grokbot.run an xAI or Cursor website?",
     "No. It is an unofficial community handbook. Official packages are on x.ai/bot. Official docs are on docs.x.ai and cursor.com/help."),
    ("Who operates this site?",
     "The site is published as a community handbook at grokbot.run. It does not speak for xAI or Cursor. Product support is hi@cursor.com. Site mail is hello@grokbot.run."),
    ("Where do the failure notes come from?",
     "From official troubleshooting and Cursor Help pages, plus staff replies already reviewed into the handbook snapshots. Forum threads are field evidence, not product promises."),
    ("Do you sell Grok Bot or set its price?",
     "No. This site does not sell access, does not take payment, and does not publish a price list. Eligibility wording lives on the pricing snapshot and links to the originals."),
]

PRIVACY_FAQS = [
    ("Does this site require an account?",
     "No. There is no grokbot.run login. Reading the pages does not create a profile on this site."),
    ("When does analytics run?",
     "Only if the build was given a GA4 measurement ID. With no ID, the generator inserts no Google tag. The tag, when present, records a page view and a click on the main official-store buttons."),
    ("Do you show ads today?",
     "No advertising is placed on the site today. Ads may be shown in the future. If that starts, this page will be updated, and ad partners may set their own cookies."),
    ("What should I not email?",
     "Do not send passwords, one-time codes, API keys, session files, or private customer data to hello@grokbot.run or in a support mail you copy from these pages."),
]

TERMS_FAQS = [
    ("Can I rely on this site as official documentation?",
     "No. Official product behavior is whatever xAI and Cursor publish. This handbook can lag. When a page and an official doc disagree, the official doc wins."),
    ("Are the third-party tools yours?",
     "No. The tools catalog links to other people's repositories. Their licenses, maintenance, and permissions are theirs. Read the upstream README before you install anything."),
    ("Do you guarantee that a fix will work?",
     "No. The steps repeat controls and staff replies that were already public. Networks, plans, and app builds change. If Recover and one retry fail, contact Cursor support instead of repeating Reset."),
]

CONTACT_FAQS = [
    ("Which address is for the website?",
     "hello@grokbot.run. Use it for a broken link, a factual correction, or a privacy question about this handbook."),
    ("Which address is for Grok Bot the product?",
     "hi@cursor.com, as named in Cursor Help and on the troubleshooting pages. Include the version, OS, the exact sentence on screen, the time and time zone, and what you already tried. Do not attach secrets."),
    ("Will emailing this site reset my computer or refund a charge?",
     "No. This site cannot see your Cursor account, change a plan, or operate the cloud computer."),
]


def _faq(faqs):
    from html import escape
    bits = ['<h2>FAQ</h2><div class="faq card">']
    for q, a in faqs:
        bits.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    bits.append("</div>")
    return "".join(bits)


def about():
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">About</p>
<h1>About this Grok Bot guide</h1>
<p>grokbot.run is an unofficial community handbook for Grok Bot, the xAI and Cursor product that pairs named teammates with one shared cloud computer. It is not grok.com chat, not Grok Build, and not an official xAI or Cursor site. Brand marks on these pages are for identification so you can tell this product from the others. They are not a claim of partnership.</p>
<p>The handbook exists because the official docs, Cursor Help, and the Cursor forum answer different questions in different places. This site puts them in reading order: what the product is, how to install it from the real storefront, how to run one job, what the shared computer does and does not isolate, and what to try when a screen says the computer cannot be reached. The long error pages are split by the sentence on the screen, so a DNS failure is not filed under a usage limit.</p>
<h2>What we will and will not write</h2>
<p>A page is added only when the behavior is already described on this site, in the reviewed JSON snapshots, or on an official xAI or Cursor page we have opened. We do not invent menu paths, error strings, plan prices, or features to fill a keyword. If a search query cannot be supported that way, it stays off the site. Prices stay on the pricing snapshot, which quotes official wording and links out instead of filling blanks.</p>
<p>Forum threads are labeled as field evidence. A staff reply in a thread is not a permanent contract. App builds move. When a walkthrough names a control, it names the control from official troubleshooting or from a staff post already in the failure notes, and it links the source.</p>
<h2>What this site is not</h2>
<ul>
<li>Not the download store. Desktop packages are on x.ai/bot. iPhone and iPad are on the App Store. Android is on Google Play.</li>
<li>Not product support. Cursor asks for product mail at hi@cursor.com. This site cannot see your account.</li>
<li>Not a client, a skill pack, or a reconstructed prompt library. Third-party tools in the catalog are other people's repositories.</li>
<li>Not a place that ranks itself as the best Grok Bot, and not a place that invents testimonials.</li>
</ul>
<h2>How the pages are maintained</h2>
<p>The HTML is generated from Python in this repository. Reviewed snapshots under src/data record official links, failure threads, and the tools catalog. The checker refuses a build that drops internal links, duplicates a title, or changes the rendered counts of those snapshots without an intentional edit. The catalog counts you see on the homepage are those rendered counts, not a traffic claim.</p>
<p>Corrections are welcome at hello@grokbot.run. A useful note names the page, the sentence, and the official URL that disagrees. We do not need your Cursor login, a screenshot of a secret, or a token.</p>
''' + _faq(ABOUT_FAQS) + '''
</div></section>
'''


def privacy():
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">Privacy</p>
<h1>Privacy policy</h1>
<p>This policy covers grokbot.run, the unofficial Grok Bot handbook. It does not cover x.ai, cursor.com, the Grok Bot apps, or the cloud computer. Those services have their own policies. If you sign in to Grok Bot, you are dealing with Cursor and xAI, not with this website.</p>
<h2>What the site collects</h2>
<p>The pages are static files. There is no account, no comment box, and no form that stores a profile. The only way to send us a message is email to hello@grokbot.run. We receive whatever you put in that message: the address you send from, the subject, and the body. Do not include passwords, one-time codes, API keys, session cookies, or customer data. We use site mail to answer the note and to correct a page. We do not sell that mail.</p>
<h2>Cookies and analytics</h2>
<p>Analytics is optional and decided at build time. If the environment variable PUBLIC_GA_MEASUREMENT_ID is set to a GA4 measurement ID, the generator adds Google's gtag snippet to each page. That tag records a page view on a full page load. A click on a button that goes to x.ai/bot, the App Store Grok Bot listing, or the Google Play package ai.x.grok.bot also sends a cta_click event with the link URL and the link text. Google Analytics may set cookies to distinguish a browser and to measure those loads. Google's own policy describes what they store.</p>
<p>If that variable is unset, empty, or not a GA4 ID, the build inserts no Google tag and this site sets no analytics cookie. The Find box in the header loads /search.json in your browser and filters it locally. That request is a static file fetch, not an account lookup.</p>
<h2>Advertising</h2>
<p>The site does not show ads today. Ads may be shown in the future. If advertising is added, ad partners may use cookies or similar storage to measure or personalize those ads, and this page will be updated before that change. Until then, do not expect an ad cookie from grokbot.run itself.</p>
<h2>Logs and third parties</h2>
<p>The site is hosted as static files. The host can keep ordinary request logs, such as IP address, user agent, and the URL requested, under the host's own policy. Outbound links to xAI, Cursor, GitHub, the app stores, and forum threads are other sites. What they collect starts when you follow the link.</p>
<p>We do not knowingly ask children to send personal information to this site. The handbook is written for people operating a work tool.</p>
<h2>Retention and contact</h2>
<p>Email you send to hello@grokbot.run is kept long enough to handle the correction or the question, then deleted when it is no longer needed for that purpose. To ask what a specific message contained, or to ask us to delete a message you sent, write to the same address from the same mailbox and name the date. We cannot delete data held by Cursor, xAI, Google Analytics, or an ad partner that is not on this site yet.</p>
<p>This page was updated on 2026-09-27.</p>
''' + _faq(PRIVACY_FAQS) + '''
</div></section>
'''


def terms():
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">Terms</p>
<h1>Terms of use</h1>
<p>These terms cover your use of grokbot.run. They are not a license from xAI or Cursor, and they are not the terms of the Grok Bot product. If you install the app, the product terms on those companies' sites apply to the app. If these handbook terms and an official product term both seem to speak, the official product term governs the product, and these terms govern only this website.</p>
<h2>Unofficial handbook</h2>
<p>The text is a community explanation. It is not official documentation, not support, and not a statement by xAI or Cursor. Names and logos are used to identify the product you already meant to find. Pages can be wrong, incomplete, or behind the current app. When a walkthrough and an official help page disagree, follow the official page and send us the URL.</p>
<p>We do not promise that a step will recover a computer, restore a bot, stop a charge, or make a plugin connect. The steps repeat controls that official troubleshooting and reviewed staff replies already describe. Your network, plan, and build can still differ.</p>
<h2>No professional advice and no prices</h2>
<p>Nothing here is legal, security, or billing advice. The pricing snapshot compares official sentences and refuses to invent dollar amounts. Do not treat a sentence on this site as a quote, an invoice, or a promise that a plan includes Grok Bot tomorrow. Open the linked official page before you buy, cancel, or link SuperGrok. Linking SuperGrok is described by Cursor as permanent; that consequence is theirs, and you should read their page before you click it.</p>
<h2>Acceptable use</h2>
<p>Do not use the handbook as a script to break into an account, bypass an approval, steal a credential, or hide a charge. Do not paste secrets into a bot because a page mentioned a connector. The computer is shared by every bot on the account; that is a product fact, not an invitation to store passwords in chat. Third-party repositories linked from the tools catalog are not supplied by us. Review their license and what they do with a local session before you run them.</p>
<h2>Content and liability</h2>
<p>You may link to these pages. You may not copy the site and present it as an official xAI or Cursor property. The pages are provided as-is, without a warranty of accuracy, fitness, or uptime. To the extent the law allows, the operators of this handbook are not liable for lost bots, lost files, usage charges, store fees, or time spent on a step that did not match your build. Some places do not allow that limit; in those places the limit applies as far as the law actually allows.</p>
<p>If you send a correction, you give us permission to use the factual point on the site. Do not send material you do not have the right to share. We may refuse a change, remove a page, or update a date when a source changes.</p>
<p>These terms were updated on 2026-09-27. The contact page names the mailbox for a question about them.</p>
''' + _faq(TERMS_FAQS) + '''
</div></section>
'''


def contact():
    return '''
<section class="band"><div class="wrap prose">
<p class="kicker">Contact</p>
<h1>Contact this guide</h1>
<p>Site mail is <a href="mailto:hello@grokbot.run">hello@grokbot.run</a>. That mailbox is for this unofficial handbook: a broken link, a page that contradicts an official URL, or a question about the privacy policy. It is not xAI support and not Cursor support. Writing to it does not open a ticket on your Grok Bot account, because this site cannot see that account.</p>
<p>Product support, as Cursor Help and the troubleshooting pages already say, is <a href="mailto:hi@cursor.com">hi@cursor.com</a>. Use that address when the app itself is stuck. Include the Grok Bot version, the operating system, the exact error sentence, the bot or routine name, the time and time zone, the request or conversation id if the app shows one, and what you already tried. Say whether the phone on cellular matches the desktop. Do not attach passwords, one-time codes, private keys, or session files.</p>
<h2>What a useful site note looks like</h2>
<p>Name the page URL on grokbot.run, quote the sentence you think is wrong, and paste the official URL that disagrees. If a control moved, say the build you are on and the label you see now. We would rather delete a step than keep a menu path we cannot source. We do not need a screen recording of your inbox, a customer list, or a token that would let someone act as you.</p>
<h2>What we cannot do</h2>
<ul>
<li>Reset, Recover, or Update your cloud computer.</li>
<li>See your weekly usage, reverse an On-Demand charge, or change a plan.</li>
<li>Unlink SuperGrok, delete a Cursor account, or restore a bot.</li>
<li>Provide a Linux package, a Mac build, or a phone build. Those stay on x.ai/bot and the official stores.</li>
<li>Speak for xAI or Cursor, or escalate inside their support queue.</li>
</ul>
<h2>Security reports</h2>
<p>If you believe a page on this site is being used to phish, or a link points somewhere it should not, write to hello@grokbot.run with the URL. Do not send a proof-of-concept that collects credentials. For a vulnerability in Grok Bot itself, use the channel Cursor or xAI publish. This handbook is a static site and does not run the product.</p>
<p>There is no web form. The working contact is the mailbox above. If your mail client does not open from the link, type hello@grokbot.run yourself and put the page URL in the subject. A short note is enough. We read site mail for corrections to this handbook, not as a queue for the Grok Bot product.</p>
''' + _faq(CONTACT_FAQS) + '''
</div></section>
'''


LEGAL = [
    ("/about/", "About this unofficial Grok Bot guide", "What grokbot.run is: an unofficial handbook for Grok Bot, how facts are chosen, and what the site will not invent. Not an xAI or Cursor site.", about, ABOUT_FAQS),
    ("/privacy/", "Privacy policy for the Grok Bot guide", "Privacy for grokbot.run: no site account, optional GA4 cookies only when a measurement ID is set, and ads may be shown in the future.", privacy, PRIVACY_FAQS),
    ("/terms/", "Terms of use for the Grok Bot guide", "Terms for using this unofficial Grok Bot handbook. Not a product warranty, not official docs, and not a price quote. Official pages win on conflict.", terms, TERMS_FAQS),
    ("/contact/", "Contact the Grok Bot guide", "Contact this handbook at hello@grokbot.run. Product problems go to hi@cursor.com. This site cannot see your Cursor account or reset a computer.", contact, CONTACT_FAQS),
]
