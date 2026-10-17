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
                          (tag in ('img', 'script', 'video', 'source') and key == 'src') or
                          (tag == 'video' and key == 'poster')):
                self.targets.append(value)

module_pages = (
    'index.html',
    'guide/why-finenav/index.html',
    'guide/installation/index.html',
    'guide/quickstart/index.html',
    'guide/choose-algorithms/index.html',
    'guide/worldview/index.html',
    'guide/cpp-application/index.html',
    'guide/behavior-tree/index.html',
    'guide/plugins/planners/index.html',
    'guide/plugins/maps/index.html',
    'guide/custom-planner/index.html',
    'guide/custom-map/index.html',
)
required = [prefix + page
            for prefix in ('', 'zh/')
            for page in ('index.html', 'slambox/index.html', 'icra/index.html')]
required += [prefix + 'finenav-engine/' + page
             for prefix in ('', 'zh/') for page in module_pages]
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
