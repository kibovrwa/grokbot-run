# -*- coding: utf-8 -*-
"""/hotel-lobby-ai/ — static landing page for the Hotel Lobby AI meme.

Honesty rules for this page:
- The generator does NOT exist yet. The tool block is a labelled mock of the
  upload screen. Nothing uploads, nothing is generated, no sample output,
  no testimonials, no usage numbers.
- The email form opens the visitor's own mail app (mailto:). Nothing is
  stored by this site.
- Meme facts are limited to what Complex and XXL reported in Sept 2026.
"""
from html import escape

PATH = "/hotel-lobby-ai/"
MAIL = "hello@grokbot.run"

COMPLEX = "https://www.complex.com/music/a/markelibert/quavo-takeoff-hotel-lobby-ai-trend-tiktok"
XXL = "https://www.xxlmag.com/quavo-takeoff-viral-hotel-lobby-ai-trend/"

FAQS = [
    ("What is Hotel Lobby AI?",
     "Hotel Lobby AI is a September 2026 video meme. Two people, characters, or pets are placed into the orange-room "
     "performance of \"Hotel Lobby (Unc & Phew)\", the 2022 A COLORS SHOW clip by Quavo and Takeoff. Press coverage "
     "(Complex, XXL) traces it to TikTok clips of two cats in early September 2026, after which people swapped in "
     "friends, celebrities, and fictional characters."),
    ("Can I generate a Hotel Lobby AI video on this page today?",
     "No. The generator on this page is not live. The upload screen above is a preview of the layout only: it does "
     "not accept files and does not produce a video or an image. You can ask to be told when it launches. There is "
     "no launch date and no price yet."),
    ("What does the email form do?",
     "It opens your own email app with a pre-filled message to " + MAIL + " that says you want a launch note. "
     "Nothing is sent until you press send in your mail app, and this page stores nothing. We will only use the "
     "address to tell you if the generator launches."),
    ("Will the finished video use the real COLORS clip or the original audio?",
     "No. The plan is an original orange-studio template made for this site, not the A COLORS SHOW footage and not "
     "the Migos recording. Some other tools on the web reuse the original clip and audio. That is their choice and "
     "their legal risk, and it is not what this page plans to do. Expect a clip that looks like the trend, not a copy "
     "of the original."),
    ("Is this affiliated with Quavo, Takeoff, Migos, or COLORS?",
     "No. This is an independent fan-trend page. It is not affiliated with, endorsed by, or connected to Quavo, "
     "Takeoff, Migos, COLORS, or any rights holder. Names appear only to describe the meme."),
    ("What will happen to the photos I upload?",
     "Nothing is uploaded today, so nothing is stored today. When a generator exists, this section and the Privacy "
     "page will say exactly how long photos are kept and how to delete them before anyone is asked to upload a file. "
     "Until then, do not send photos to this site by email either."),
    ("Which photos will work best?",
     "One clear, well-lit, full-body or waist-up photo per person, facing the camera, with nothing covering the face "
     "or hands. Two separate photos, one subject each. See the photo tips above. Pets work best when the whole animal "
     "is visible."),
    ("Is it okay to use celebrities or someone else's face?",
     "Use only photos you have the right to use, of adults who agree. Do not use public figures, children, or "
     "anyone who has not agreed, and do not pass a clip off as real. Fans asked for respect because Takeoff died in "
     "2022. Press coverage also raised consent and copyright concerns about the trend. A launched generator would "
     "block misuse, and this page will say how."),
    ("Is it free?",
     "Unknown. There is no product to price yet, so this page lists no price and no free tier. If that changes, the "
     "price and what you get will be written here before you are asked to pay for anything."),
    ("Why is a Hotel Lobby AI page on a Grok Bot guide site?",
     "grokbot.run is an unofficial handbook for xAI and Cursor's Grok Bot. This page is a separate side project on "
     "the same domain. It is not about Grok Bot and not affiliated with xAI or Cursor. The handbook links below are "
     "for readers who came for Grok Bot."),
]

HOWTO = [
    ("Pick two photos",
     "Choose one clear photo per subject: two people, two pets, or one of each. Use photos you own or have permission to use."),
    ("Upload them",
     "When the generator launches, you will add Photo 1 and Photo 2 on this page. The upload screen on this page is a mock today."),
    ("Wait for the render",
     "Video takes minutes, not seconds. When the generator exists, this step will state the real wait time and output format."),
    ("Download and share",
     "Save the clip and post it. Say it is AI-generated. Do not present it as a real performance."),
]

TIPS = [
    ("Face the camera", "A front-facing photo with both eyes visible gives the model the most to work with. Avoid sunglasses, masks, and hands over the face."),
    ("Show the body", "Full-body or waist-up beats a tight selfie, because the booth scene shows standing figures. Keep the whole subject inside the frame."),
    ("Even light", "Daylight or a plain indoor light. Harsh shadows across the face and strong backlight tend to give worse results."),
    ("One subject per photo", "Do not crop two people into one image. Give each performer their own photo, so they stay distinct."),
    ("Pets: whole animal", "Show the full pet, head to paws, against a plain background. Busy rugs and sofas blur the outline."),
    ("Resolution over filters", "Use the original photo, not a screenshot or a heavily filtered copy. Larger and sharper is better."),
]

IDEAS = [
    ("Pets", "Your cat and your dog, or two cats, which is how the trend began according to press coverage."),
    ("Friends", "Two friends who already do bits together. Both must agree to be in it."),
    ("Couples and family adults", "A duet is the format. Adults who are happy to be in the joke."),
    ("Characters you drew", "Original characters and mascots you made yourself are safer than anyone's real face."),
]

STYLE = """<style>
.hl-tool{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:14px;margin-top:8px}
.hl-slots{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.hl-slot{border:2px dashed var(--hairline-strong);border-radius:var(--radius-n);background:var(--surface);min-height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:14px;color:var(--muted);font-size:15px}
.hl-slot strong{color:var(--text);font-weight:600}
.hl-tag{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;background:#FFF1E6;color:#9A3F0C;border:1px solid rgba(242,107,42,.35);border-radius:9999px;padding:3px 10px;margin-bottom:10px}
.hl-tool .btn[disabled]{opacity:.45;cursor:not-allowed;transform:none;box-shadow:none}
.hl-form label{display:block;font-weight:560;margin:0 0 6px}
.hl-form input[type=email]{width:100%;font:inherit;padding:12px 14px;border-radius:12px;border:1px solid var(--hairline-strong);background:var(--bg-elev);color:var(--text);margin-bottom:12px}
.hl-form input[type=email]:focus{outline:2px solid #111;outline-offset:2px}
.hl-form .btn{width:100%}
.hl-fine{font-size:14px;color:var(--muted);margin:10px 0 0}
.hl-wide{max-width:60rem}
.hl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:14px 0 8px}
.hl-grid .card{padding:20px}
.hl-grid h3{margin-top:0;font-size:17px}
.hl-grid p{color:var(--muted);font-size:15px;margin:0}
@media (max-width:860px){.hl-tool{grid-template-columns:1fr}.hl-grid{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.hl-slots,.hl-grid{grid-template-columns:1fr}}
</style>"""


def _faq_html():
    bits = ['<h2 id="faq">Hotel Lobby AI FAQ</h2><div class="faq card">']
    for q, a in FAQS:
        bits.append("<details><summary>%s</summary><p>%s</p></details>" % (escape(q), escape(a)))
    bits.append("</div>")
    return "".join(bits)


def hotel_lobby():
    steps = "".join(
        '<div class="step"><span class="num">%d</span><div><h3>%s</h3><p>%s</p></div></div>'
        % (i, escape(n), escape(t))
        for i, (n, t) in enumerate(HOWTO, 1)
    )
    tips = "".join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (escape(n), escape(t)) for n, t in TIPS
    )
    ideas = "".join(
        "<li><strong>%s.</strong> %s</li>" % (escape(n), escape(t)) for n, t in IDEAS
    )
    return STYLE + '''
<section class="hero"><div class="wrap hl-wide">
<p class="kicker">Orange booth duet meme</p>
<h1>Hotel Lobby AI</h1>
<p class="lede">Put two photos, two friends, or two pets into the orange-room duet from the viral \"Hotel Lobby\" meme. The generator is <strong>not live yet</strong>. This page explains the trend, shows what the tool screen will look like, and lets you ask for a launch note.</p>

<div class="hl-tool" id="tool">
<div class="card" aria-labelledby="hl-tool-h">
<span class="hl-tag">Preview only, generator launching soon</span>
<h2 id="hl-tool-h" style="font-size:24px">Upload two photos</h2>
<div class="hl-slots" aria-hidden="true">
<div class="hl-slot"><strong>Photo 1</strong><span>Person or pet</span></div>
<div class="hl-slot"><strong>Photo 2</strong><span>Person or pet</span></div>
</div>
<button class="btn btn-primary" type="button" disabled aria-disabled="true">Generate video: launching soon</button>
<p class="hl-fine">This is a mock of the upload screen. It does not accept files, it uploads nothing, and it makes no video or image. No samples are shown because none exist yet.</p>
</div>

<div class="card">
<h2 style="font-size:24px">Get notified when it launches</h2>
<form class="hl-form" action="mailto:%(mail)s" method="get">
<input type="hidden" name="subject" value="Hotel Lobby AI: tell me when the generator launches">
<label for="hl-email">Your email</label>
<input id="hl-email" type="email" name="body" placeholder="you@example.com" autocomplete="email" required>
<button class="btn btn-primary" type="submit">Get notified</button>
</form>
<p class="hl-fine">This opens your own email app with a message to %(mail)s. Nothing is sent until you press send there, and this page stores nothing. We will use the address only to tell you if the generator launches. No launch date, no price, no free tier yet.</p>
</div>
</div>
</div></section>

<section class="band"><div class="wrap prose hl-wide">
<h2 id="what-it-is">What is Hotel Lobby AI?</h2>
<p>Hotel Lobby AI is a September 2026 video meme. The source is \"Hotel Lobby (Unc &amp; Phew)\", a 2022 performance by Quavo and Takeoff on A COLORS SHOW: two rappers in front of a flat orange wall with one microphone hanging between them. In the AI version, two other performers take their places. <a href="%(xxl)s">XXL</a> traces the current wave to a TikTok clip of two cats in early September 2026. <a href="%(cx)s">Complex</a> reports that people then swapped in friends, celebrities, and fictional characters using AI video tools and templates, and that Quavo reposted the original performance in September.</p>
<p>The trend is also controversial. Complex notes that fans criticised the swaps because Takeoff died in 2022, and that the trend raises questions about consent, copyright, and how AI sites use uploaded photos. This page takes those concerns seriously: see the rights notes in the FAQ.</p>

<div class="callout warn"><p><strong>Original template, not the real clip.</strong> The planned generator uses an original orange-studio template made for this site. It will not use the A COLORS SHOW footage or the original audio. That keeps it a fan-style tribute to the look of the trend and not a copy of someone else's recording. Because the generator does not exist yet, no example video is shown here.</p></div>

<h2 id="how-to">How to make a Hotel Lobby AI video: 4 steps</h2>
<p>This is the flow the tool will follow. Steps 2 to 4 are not available yet.</p>
</div></section>

<section class="band"><div class="wrap hl-wide"><div class="roadmap">%(steps)s</div></div></section>

<section class="band"><div class="wrap hl-wide">
<h2 id="photo-tips">Photo tips for Hotel Lobby AI</h2>
<p class="muted">General advice for any two-photo video tool. These tips do not promise a particular result.</p>
<div class="hl-grid">%(tips)s</div>
</div></section>

<section class="band"><div class="wrap prose hl-wide">
<h2 id="ideas">Who goes in the booth?</h2>
<ul>%(ideas)s</ul>
<div class="callout"><p><strong>Rights and safety.</strong> Use only photos you have the right to use. Adults who agree only: no children, no public figures, no one who has not said yes. Label the result as AI-generated and never pass it off as a real recording.</p></div>
</div></section>

<section class="band"><div class="wrap prose hl-wide">
%(faq)s

<h2 id="handbook">Came here for Grok Bot?</h2>
<p>This site is an unofficial Grok Bot handbook. The Hotel Lobby AI page is a separate side page and is not about Grok Bot. If you want the handbook, start with one of these:</p>
<ul>
<li><a href="/learn/">The Grok Bot handbook</a>: lessons in reading order.</li>
<li><a href="/learn/what-is-grok-bot/">What Grok Bot is</a>: a named teammate plus one cloud computer.</li>
<li><a href="/learn/first-bot/">Create your first Bot</a>: one job, one brief.</li>
<li><a href="/learn/install/">Download and sign in</a>: official packages and Cursor login.</li>
<li><a href="/about/">About this site</a>, <a href="/privacy/">Privacy</a>, <a href="/terms/">Terms</a>, and <a href="/contact/">Contact</a>.</li>
</ul>

<h2 id="disclaimer">Disclaimer</h2>
<p>Independent fan-trend page. Not affiliated with, endorsed by, or connected to Quavo, Takeoff, Migos, COLORS, or any rights holder. \"Hotel Lobby\" and A COLORS SHOW belong to their owners and are named only to describe the meme. Not affiliated with xAI or Cursor. AI-generated content, when a generator exists, will be labelled as such.</p>
<h2>Sources</h2>
<ul>
<li><a href="%(cx)s">Complex: Quavo and Takeoff's \"Hotel Lobby\" performance has become a viral AI meme</a></li>
<li><a href="%(xxl)s">XXL: Viral AI trend puts celebrities, animals and more inside the \"Hotel Lobby\" Colors performance</a></li>
</ul>
</div></section>
''' % {"mail": MAIL, "xxl": XXL, "cx": COMPLEX, "steps": steps, "tips": tips, "ideas": ideas, "faq": _faq_html()}
