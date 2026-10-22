"""Basic Markdown hygiene and repository-local link/anchor checks; not full Markdown lint."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import unicodedata
R = Path(__file__).resolve().parents[1]

def slug(text):
    text = re.sub(r'[`*_]', '', text).lower()
    return ''.join(c for c in text if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')

def anchors(path):
    found = set(re.findall(r'<a\s+id="([^"]+)"', path.read_text()))
    seen = {}
    for line in path.read_text().splitlines():
        m = re.match(r'^#{1,6}\s+(.+)', line)
        if m:
            base = slug(m.group(1)); n = seen.get(base, 0)
            found.add(base + (f'-{n}' if n else '')); seen[base] = n+1
    return found

if __name__ == '__main__':
    problems = []
    for path in R.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text()
        if not text.endswith('\n'):
            problems.append(f'{path.relative_to(R)}: missing final newline')
        for i, line in enumerate(text.splitlines(), 1):
            if line.endswith((' ', '\t')):
                problems.append(f'{path.relative_to(R)}:{i}: trailing whitespace')
        # Inline links and images used in this repository; reference-style links are not parsed.
        for raw in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            u = urlsplit(raw)
            if u.scheme or u.netloc:
                continue
            dest = (R/u.path.lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path)).resolve() if u.path else path
            if not dest.is_relative_to(R) or not dest.exists():
                problems.append(f'{path.relative_to(R)}: missing local target {raw}')
            elif u.fragment and dest.suffix == '.md' and unquote(u.fragment) not in anchors(dest):
                problems.append(f'{path.relative_to(R)}: missing anchor {raw}')
    if problems:
        raise SystemExit('\n'.join(problems))
    print('Markdown hygiene and inline local links consistent; external links checked separately.')
