# -*- coding: utf-8 -*-
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://grokbot.run"
LOGO = "/brand/grok-bot-face.svg"
LOGO_ABS = SITE + LOGO

# Top nav is jobs, not every lesson. Lessons live in the footer.
NAV = [
    ("/", "Guide"),
    ("/learn/install/", "Install"),
    ("/pricing/", "Pricing"),
    ("/tools/", "Tools"),
    ("/use-cases/", "Cases"),
    ("/troubleshooting/", "Help"),
]

LESSONS = [
    ("/learn/what-is-grok-bot/", "What Grok Bot is"),
    ("/learn/install/", "Install and sign in"),
    ("/learn/first-bot/", "First Bot"),
    ("/learn/computer/", "Shared computer"),
    ("/learn/skills-routines/", "Skills and routines"),
    ("/learn/plugins/", "Plugins and MCP"),
    ("/learn/cost-and-pitfalls/", "Cost and pitfalls"),
]

LESSONS_EN = LESSONS
NAV_EN = NAV


def canonical(path):
    if path == "/":
        return SITE + "/"
    return SITE + path.rstrip("/") + "/"


def pager(path, lang="en"):
    urls = [u for u, _ in LESSONS]
    if path not in urls:
        return ""
    i = urls.index(path)
    bits = []
    if i > 0:
        pu, pt = LESSONS[i - 1]
        bits.append('<a href="%s">Previous: %s</a>' % (pu, escape(pt)))
    else:
        bits.append("<span></span>")
    if i < len(urls) - 1:
        nu, nt = LESSONS[i + 1]
        bits.append('<a href="%s">Next: %s</a>' % (nu, escape(nt)))
    else:
        bits.append('<a href="/use-cases/">Next: Field cases</a>')
    return '<nav class="pager">%s</nav>' % "".join(bits)


def _nav_current(href, path):
    if href == "/":
        return path == "/"
    return path == href or path.startswith(href)


def nav_html(path):
    bits = []
    for href, label in NAV:
        cur = ' aria-current="page"' if _nav_current(href, path) else ""
        bits.append('<a href="%s"%s>%s</a>' % (href, cur, escape(label)))
    return "".join(bits)


FIND_JS = r"""
(function(){
  const box=document.querySelector('[data-find]');
  const input=document.querySelector('[data-find-input]');
  const list=document.querySelector('[data-find-list]');
  if(!box||!input||!list) return;
  let rows=[], hits=[], active=-1, loaded=false;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function hide(){ list.hidden=true; list.innerHTML=''; hits=[]; active=-1; }
  function score(row,q){
    const t=row.t.toLowerCase(), hay=row.q||'';
    if(t===q) return 100;
    if(t.startsWith(q)) return 80;
    if(t.includes(q)) return 60;
    if(hay.includes(q)) return 40;
    return 0;
  }
  function render(){
    if(!hits.length){ hide(); return; }
    list.innerHTML=hits.map((r,i)=>'<a role="option" class="'+(i===active?'is-active':'')+'" href="'+esc(r.h)+'"><span>'+esc(r.t)+'</span><em>'+esc(r.k)+'</em></a>').join('');
    list.hidden=false;
  }
  function run(){
    const q=(input.value||'').trim().toLowerCase();
    if(q.length<2){ hide(); return; }
    hits=rows.map(r=>({r,s:score(r,q)})).filter(x=>x.s).sort((a,b)=>b.s-a.s).slice(0,8).map(x=>x.r);
    active=hits.length?0:-1;
    render();
  }
  function load(){
    if(loaded) return Promise.resolve();
    return fetch('/search.json').then(r=>r.json()).then(data=>{ rows=data; loaded=true; });
  }
  input.addEventListener('focus', ()=>load().then(run));
  input.addEventListener('input', ()=>load().then(run));
  input.addEventListener('keydown', e=>{
    if(e.key==='Escape'){ hide(); input.blur(); return; }
    if(!hits.length) return;
    if(e.key==='ArrowDown'){ e.preventDefault(); active=Math.min(hits.length-1,active+1); render(); }
    if(e.key==='ArrowUp'){ e.preventDefault(); active=Math.max(0,active-1); render(); }
    if(e.key==='Enter' && active>=0 && hits[active]){ e.preventDefault(); location.href=hits[active].h; }
  });
  document.addEventListener('click', e=>{ if(!box.contains(e.target)) hide(); });
  const pre=new URLSearchParams(location.search).get('q');
  if(pre){ input.value=pre; load().then(run); }
})();
"""


def find_html():
    return (
        '<div class="find" data-find>'
        '<label class="visually-hidden" for="site-find">Find a page or symptom</label>'
        '<input id="site-find" class="find-input" type="search" placeholder="Find a page or symptom" autocomplete="off" data-find-input>'
        '<div class="find-list" hidden data-find-list role="listbox"></div>'
        "</div>"
    )


def header_html(path):
    return (
        '<header class="site"><div class="wrap nav">'
        '<a class="brand" href="/"><img class="logo" src="%s" alt="Grok Bot Guide"><span class="name">Grok Bot</span><span class="tag">Guide</span></a>'
        '<span class="nav-rule" aria-hidden="true"></span>'
        '%s'
        '<button class="menu-btn" type="button" data-menu>Menu</button>'
        '<nav class="links" data-links>%s</nav></div></header>'
        % (LOGO, find_html(), nav_html(path))
    )


def footer_html():
    return (
        '<footer class="site"><div class="wrap"><div class="foot-grid">'
        "<div><h4>Learn</h4>"
        '<a href="/learn/">Handbook</a>'
        '<a href="/learn/what-is-grok-bot/">What Grok Bot is</a>'
        '<a href="/learn/install/">Install and sign in</a>'
        '<a href="/learn/mac-download/">Mac download</a>'
        '<a href="/learn/windows-download/">Windows download</a>'
        '<a href="/learn/phone-download/">iPhone and Android</a>'
        '<a href="/learn/login/">Cursor login</a>'
        '<a href="/learn/first-bot/">First Bot</a>'
        '<a href="/learn/computer/">Shared computer</a>'
        '<a href="/learn/skills-routines/">Skills and routines</a>'
        '<a href="/learn/plugins/">Plugins and MCP</a>'
        '<a href="/learn/cost-and-pitfalls/">Cost and pitfalls</a>'
        '<a href="/learn/operator/">After week one</a>'
        '<a href="/learn/ops/">X, Cursor, MCP</a>'
        '<a href="/learn/glossary/">Glossary</a>'
        '<a href="/learn/cursor/">Cursor and Grok Bot</a></div>'
        "<div><h4>Look up</h4>"
        '<a href="/pricing/">Pricing</a>'
        '<a href="/compare/">Alternatives</a>'
        '<a href="/tools/">Tools catalog</a>'
        '<a href="/use-cases/">Field cases</a>'
        '<a href="/troubleshooting/">Help</a>'
        '<a href="/troubleshooting/not-responding/">Not responding</a>'
        '<a href="/troubleshooting/stuck/">Stuck</a>'
        '<a href="/troubleshooting/cant-reach/">Can\'t reach</a>'
        '<a href="/troubleshooting/white-screen/">White or black screen</a>'
        '<a href="/troubleshooting/recover-vs-reset/">Recover vs Reset</a>'
        '<a href="/sources/">Sources</a></div>'
        "<div><h4>Official</h4>"
        '<a href="https://x.ai/bot">x.ai/bot</a>'
        '<a href="https://docs.x.ai/grok-bot/overview">xAI docs</a>'
        '<a href="https://cursor.com/help/grok-bot/getting-started">Cursor Help</a>'
        '<a href="https://github.com/RongleCat/awesome-grok-bot">awesome-grok-bot</a></div>'
        "</div></div></footer>"
    )


def _hreflang_tags(path):
    loc = canonical(path)
    return (
        '<link rel="alternate" hreflang="en" href="%s">\n'
        '<link rel="alternate" hreflang="x-default" href="%s">'
        % (loc, loc)
    )


CRUMB_SHORT = {
    "/learn/": "Handbook",
    "/learn/what-is-grok-bot/": "What it is",
    "/learn/install/": "Install",
    "/learn/mac-download/": "Mac",
    "/learn/windows-download/": "Windows",
    "/learn/phone-download/": "Phone",
    "/learn/login/": "Login",
    "/learn/first-bot/": "First Bot",
    "/learn/computer/": "Computer",
    "/learn/skills-routines/": "Skills",
    "/learn/plugins/": "Plugins",
    "/learn/cost-and-pitfalls/": "Cost",
    "/learn/operator/": "After week one",
    "/learn/ops/": "X, Cursor, MCP",
    "/learn/glossary/": "Glossary",
    "/learn/cursor/": "Cursor",
    "/compare/": "Alternatives",
    "/use-cases/": "Cases",
    "/tools/": "Tools",
    "/pricing/": "Pricing",
    "/troubleshooting/": "Help",
    "/troubleshooting/not-responding/": "Not responding",
    "/troubleshooting/stuck/": "Stuck",
    "/troubleshooting/cant-reach/": "Can't reach",
    "/troubleshooting/white-screen/": "Blank screen",
    "/troubleshooting/recover-vs-reset/": "Recover or Reset",
    "/sources/": "Sources",
}


def _crumb_name(path, title):
    return CRUMB_SHORT.get(path) or title.split("—")[0].split("|")[0].split(":")[0].strip()


def _crumb_trail(path, title):
    trail = [("/", "Guide")]
    if path.startswith("/learn/") and path != "/learn/":
        trail.append(("/learn/", "Handbook"))
    elif path.startswith("/tools/") and path != "/tools/":
        trail.append(("/tools/", "Tools"))
    elif path.startswith("/troubleshooting/") and path != "/troubleshooting/":
        trail.append(("/troubleshooting/", "Help"))
    if path != "/":
        trail.append((path, _crumb_name(path, title)))
    return trail


def crumbs_html(path, title):
    if path == "/":
        return ""
    bits = []
    trail = _crumb_trail(path, title)
    for i, (href, label) in enumerate(trail):
        if i == len(trail) - 1:
            bits.append("<span>%s</span>" % escape(label))
        else:
            bits.append('<a href="%s">%s</a>' % (href, escape(label)))
    return '<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap">%s</div></nav>' % '<span class="sep" aria-hidden="true">/</span>'.join(bits)


def faq_jsonld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def howto_jsonld(name, description, steps):
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": [
            {"@type": "HowToStep", "position": i, "name": n, "text": t}
            for i, (n, t) in enumerate(steps, 1)
        ],
    }


def itemlist_jsonld(name, rows):
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": name,
        "numberOfItems": len(rows),
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "url": u}
            for i, (n, u) in enumerate(rows, 1)
        ],
    }


def _crumbs(path, title):
    items = []
    for i, (href, label) in enumerate(_crumb_trail(path, title), 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": canonical(href),
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def page(path, title, description, body, jsonld=None, lang="en"):
    canon = canonical(path)
    site_name = "Grok Bot Guide"
    site_desc = "Grok Bot guide: how to start, Cursor login, first job, shared computer, plan conflicts, and Recover before Reset."
    blobs = list(jsonld or [])
    blobs.insert(0, {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": site_name,
        "url": SITE + "/",
        "inLanguage": "en",
        "description": site_desc,
        "publisher": {
            "@type": "Organization",
            "name": site_name,
            "logo": {"@type": "ImageObject", "url": LOGO_ABS},
        },
        "potentialAction": {
            "@type": "SearchAction",
            "target": SITE + "/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    })
    blobs.append({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": canon,
        "inLanguage": "en",
        "datePublished": "2026-09-04",
        "dateModified": "2026-09-20",
        "isPartOf": {"@type": "WebSite", "name": site_name, "url": SITE + "/"},
    })
    blobs.append(_crumbs(path, title))
    jsonld_html = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(b, ensure_ascii=False)
        for b in blobs
    )
    return _page_join(path, title, description, body, canon, site_name, jsonld_html)


def _page_join(path, title, description, body, canon, site_name, jsonld_html):
    html = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>%s</title>" % escape(title),
        '<meta name="description" content="%s">' % escape(description),
        '<meta name="robots" content="index, follow">',
        '<link rel="canonical" href="%s">' % canon,
        _hreflang_tags(path),
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="%s">' % escape(site_name),
        '<meta property="og:title" content="%s">' % escape(title),
        '<meta property="og:description" content="%s">' % escape(description),
        '<meta property="og:url" content="%s">' % canon,
        '<meta property="og:image" content="%s/og.png">' % SITE,
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:locale" content="en_US">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % escape(title),
        '<meta name="twitter:description" content="%s">' % escape(description),
        '<meta name="twitter:image" content="%s/og.png">' % SITE,
        '<link rel="icon" href="%s" type="image/svg+xml">' % LOGO,
        '<link rel="apple-touch-icon" href="%s">' % LOGO,
        "<style>%s</style>" % (ROOT / "src/css/site.css").read_text(encoding="utf-8"),
        jsonld_html,
        "</head><body>",
        header_html(path),
        "<main>%s%s</main>" % (crumbs_html(path, title), body),
        footer_html(),
        "<script>const btn=document.querySelector('[data-menu]');const links=document.querySelector('[data-links]');if(btn) btn.addEventListener('click',()=>links.classList.toggle('open'));</script>",
        '<script data-find-js>%s</script>' % FIND_JS,
        "</body></html>",
    ]
    return "\n".join(html)


def write(path, html):
    if path == "/":
        dest = ROOT / "dist" / "index.html"
    else:
        dest = ROOT / "dist" / path.strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    return dest
