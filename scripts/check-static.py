#!/usr/bin/env python3
"""Check the release files without downloading papers or contacting production."""
import base64
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.main_count = 0
        self.h1_count = 0
        self.text = []
        self.assets = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        self.main_count += tag == 'main'
        self.h1_count += tag == 'h1'
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'icon':
            self.assets.append(attrs.get('href', ''))

    def handle_data(self, data):
        self.text.append(data)


def check():
    page = Page()
    page.feed((ROOT / 'index.html').read_text())
    assert page.main_count == 1 and page.h1_count == 1, 'Expected one article landmark and title'
    assert len(page.ids) == len(set(page.ids)), 'Duplicate document IDs'
    assert page.images, 'The release has lost its embedded equations'
    for link in page.links:
        assert link, 'Empty link destination'
        if link.startswith('#'):
            assert unquote(link[1:]) in page.ids, 'Broken article anchor: ' + link
        else:
            assert urlsplit(link).scheme == 'https', 'Unexpected link scheme: ' + link
    for image in page.images:
        assert image.get('alt', '').strip() and image['alt'].strip().lower() not in {'equation', 'formula', 'image'}, 'An equation lacks meaningful alternative notation'
        prefix = 'data:image/svg+xml;base64,'
        assert image.get('src', '').startswith(prefix), 'Unexpected external equation dependency'
        decoded = base64.b64decode(image['src'][len(prefix):], validate=True)
        assert ElementTree.fromstring(decoded).tag == '{http://www.w3.org/2000/svg}svg', 'Invalid equation SVG'
    assert not re.search(r'\$[^$\n]+\$', '\n'.join(page.text)), 'Unrendered TeX in visible text'
    assert page.assets, 'Missing site icon'
    for asset in page.assets:
        path = (ROOT / asset.lstrip('/')).resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), 'Missing local asset: ' + asset
    assert 'User-agent:' in (ROOT / 'robots.txt').read_text(), 'Missing crawler rules'
    print(f'Static release checks passed: {len(page.images)} equations, {len(page.links)} links')


if __name__ == '__main__':
    check()
