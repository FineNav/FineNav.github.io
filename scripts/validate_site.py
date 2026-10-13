"""Fail deployment if bilingual entry pages or internal resources are missing."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1] / 'site'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and ((tag in ('a', 'link') and key == 'href') or
                          (tag in ('img', 'script') and key == 'src')):
                self.targets.append(value)

required = ('index.html', 'zh/index.html', 'finenav-engine/index.html',
            'zh/finenav-engine/index.html', 'finenav-engine/guide/quickstart/index.html',
            'zh/finenav-engine/guide/quickstart/index.html')
errors = []
for path in required:
    if not (ROOT / path).is_file():
        errors.append('Missing entry page: ' + path)
for page in ROOT.rglob('*.html'):
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    for target in parser.targets:
        parsed = urlparse(target)
        if not parsed.path or (parsed.scheme and parsed.scheme not in ('http', 'https')):
            continue
        if parsed.netloc and parsed.netloc.lower() != 'finenav.github.io':
            continue
        path = unquote(parsed.path)
        resolved = (ROOT / path.lstrip('/')) if path.startswith('/') else (page.parent / path)
        if resolved.is_dir():
            resolved = resolved / 'index.html'
        if not resolved.is_file():
            errors.append(str(page.relative_to(ROOT)) + ' -> ' + target)
if errors:
    raise SystemExit('\n'.join(errors))
print('Verified bilingual entry pages and links to internal pages/resources.')
