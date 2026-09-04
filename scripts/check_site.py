from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import re, sys

root = Path(__file__).resolve().parents[1]
dist = root / 'dist'

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1 = 0
        self.canon = 0
        self.desc = 0
        self.logo = False
        self.lang = None
        self.og_image = False
        self.in_h1 = False
        self.h1_text = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'html':
            self.lang = d.get('lang')
        if tag == 'a' and d.get('href'):
            self.links.append(d['href'])
        if tag == 'h1':
            self.h1 += 1
            self.in_h1 = True
        if tag == 'link' and d.get('rel') == 'canonical':
            self.canon += 1
        if tag == 'meta' and d.get('name') == 'description':
            self.desc += 1
        if tag == 'meta' and d.get('property') == 'og:image':
            self.og_image = True
        if tag == 'img' and 'grok-bot-face.svg' in (d.get('src') or ''):
            self.logo = True

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1_text.append(data)

files = sorted(dist.rglob('*.html'))
errors = []
titles = set()
h1s = set()
zh_re = re.compile(r'[\u4e00-\u9fff]')

for f in files:
    text = f.read_text(encoding='utf-8')
    p = Parser()
    p.feed(text)
    m = re.search(r'<title>(.*?)</title>', text, re.S)
    title = m.group(1).strip() if m else ''
    if not title or title in titles:
        errors.append(f'{f}: missing/duplicate title: {title}')
    titles.add(title)
    dm = re.search(r'<meta name="description" content="(.*?)"', text, re.S)
    desc = dm.group(1) if dm else ''
    if not (110 <= len(desc) <= 160):
        errors.append(f'{f.relative_to(dist)}: description length {len(desc)} not in 110–160: {desc[:80]}...')
    if (p.h1, p.canon, p.desc) != (1, 1, 1):
        errors.append(f'{f}: H1/canonical/description={(p.h1, p.canon, p.desc)}')
    if not p.logo:
        errors.append(f'{f.relative_to(dist)}: missing site logo /brand/grok-bot-face.svg')
    if 'disclaimer-bar' in text:
        errors.append(f'{f.relative_to(dist)}: leftover disclaimer bar')
    if 'lang-switch' in text or '中文长文' in text:
        errors.append(f'{f.relative_to(dist)}: leftover Chinese language switch')
    if 'hreflang="zh' in text:
        errors.append(f'{f.relative_to(dist)}: leftover zh hreflang')
    if '/learn/zh-guides/' in text:
        errors.append(f'{f.relative_to(dist)}: leftover /learn/zh-guides/ link')
    if re.search(r'href="/zh/', text):
        errors.append(f'{f.relative_to(dist)}: leftover /zh/ href')
    if p.lang != 'en':
        errors.append(f'{f}: html lang={p.lang!r}, expected en')
    if 'inLanguage": "en"' not in text and '"inLanguage":"en"' not in text:
        # WebSite json-ld only on pages via htmlutil — all pages get it
        if 'application/ld+json' in text and 'WebSite' in text:
            errors.append(f'{f}: WebSite json-ld missing inLanguage en')
    if not p.og_image or 'https://grokbot.run/og.png' not in text:
        errors.append(f'{f}: missing og:image https://grokbot.run/og.png')
    # H1 must be English-only; Chinese subtitle lives in sibling <p class="en-sub">
    h1_primary = re.sub(r'<[^>]+>', '', ''.join(
        re.findall(r'<h1[^>]*>(.*?)</h1>', text, re.S)
    )).strip()
    if zh_re.search(h1_primary):
        errors.append(f'{f.relative_to(dist)}: H1 contains Chinese: {h1_primary!r}')
    if re.search(r'<h1[^>]*>[^<]*<span class="en-sub"', text):
        errors.append(f'{f.relative_to(dist)}: H1 still nests en-sub span; use sibling p.en-sub')
    if h1_primary in h1s:
        errors.append(f'{f.relative_to(dist)}: duplicate H1: {h1_primary!r}')
    h1s.add(h1_primary)
    for href in p.links:
        if 'www.grokbot.run' in href or href.startswith('http://grokbot.run'):
            errors.append(f'{f.relative_to(dist)} non-canonical internal href: {href}')
        if href.startswith(('#', 'http://', 'https://', 'mailto:', 'tel:')):
            continue
        u = urlparse(href)
        if u.path not in ('', '/') and not u.path.endswith('/'):
            errors.append(f'{f.relative_to(dist)} missing trailing slash: {href}')
        target = dist / u.path.lstrip('/')
        if u.path.endswith('/'):
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{f.relative_to(dist)} -> {href}')

for asset in ('robots.txt', 'sitemap.xml', 'og.png', '_redirects', '_headers', 'brand/grok-bot-face.svg', 'llms.txt', '7c4e9a2f18b0d6e35a91c8f4b2d07e16.txt'):
    if not (dist / asset).exists():
        errors.append('missing ' + asset)

redirects = (dist / '_redirects').read_text(encoding='utf-8') if (dist / '_redirects').exists() else ''
for needle in (
    'https://www.grokbot.run/* https://grokbot.run/:splat 301',
    'http://www.grokbot.run/* https://grokbot.run/:splat 301',
    'http://grokbot.run/* https://grokbot.run/:splat 301',
):
    if needle not in redirects:
        errors.append(f'_redirects missing {needle}')

if not (root / 'functions' / '_middleware.js').is_file():
    errors.append('missing functions/_middleware.js')

sitemap = (dist / 'sitemap.xml').read_text(encoding='utf-8')
if 'www.grokbot.run' in sitemap or 'http://grokbot.run' in sitemap:
    errors.append('sitemap contains non-canonical host')
if 'pages.dev' in sitemap:
    errors.append('sitemap contains pages.dev host')
for must in (
    'https://grokbot.run/learn/',
    'https://grokbot.run/learn/glossary/',
    'https://grokbot.run/learn/cursor/',
    'https://grokbot.run/learn/operator/',
    'https://grokbot.run/learn/ops/',
    'https://grokbot.run/compare/',
):
    if '<loc>%s</loc>' % must not in sitemap:
        errors.append('sitemap missing %s' % must)

sources_html = (dist / 'sources/index.html').read_text()
# Count official source-notes before the community failure section heading
split_key = 'Community failure sources'
if split_key not in sources_html:
    errors.append('sources page missing English heading for community failure sources')
    official_count = -1
else:
    official_count = sources_html.split(split_key)[0].count('class="source-note"')

counts = {
    'tools': (dist / 'tools/index.html').read_text().count('class="tool-row"'),
    'cases': (dist / 'use-cases/index.html').read_text().count('class="case-card"'),
    'failures': (dist / 'troubleshooting/index.html').read_text().count('class="source-note"'),
    'official': official_count,
}
expected = {'tools': 199, 'cases': 54, 'failures': 89, 'official': 42}
if counts != expected:
    errors.append(f'counts {counts} != {expected}')

print(f'Checked {len(files)} HTML pages; rendered={counts}; errors={len(errors)}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
