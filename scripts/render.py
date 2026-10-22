"""Generate a compact README catalog and a separate detailed reading catalog."""
from pathlib import Path
import json
R = Path(__file__).resolve().parents[1]


def groups():
    papers = json.loads((R/'data/papers.yaml').read_text())
    categories = json.loads((R/'data/taxonomy.json').read_text())
    for c in categories:
        subset = sorted((p for p in papers if p['primary_category'] == c['id']),
                        key=lambda p: p['first_published'], reverse=True)
        if subset:
            yield c, subset


def venue_label(p):
    publication = p['publication']
    venue = publication['venue']
    if not venue:
        return 'arXiv'
    if publication['status'] == 'accepted_author_reported':
        venue = venue.split(' (')[0] + '; accepted, author-reported'
    return f"[{venue}]({publication['status_source']})"


def catalog():
    out = []
    for c, papers in groups():
        out += [f"### {c['title']}", '']
        for p in papers:
            out += [f"- **[{p['title']}]({p['source_url']})** ({p['first_published']} · {venue_label(p)}) — {p['contribution']}"]
        out += ['']
    return '\n'.join(out).rstrip()


def detailed_catalog():
    out = ['# Detailed paper catalog', '',
           '[Back to the list](../README.md) · [Structured metadata](../data/papers.yaml)', '',
           'AI-assisted summaries based on primary metadata and abstracts. Evidence below is author-reported; no full-text review or reproduction is claimed. Dates are first-publication dates. `core`, `supporting`, and `background` describe scope, not quality.', '']
    for c, papers in groups():
        out += [f"## {c['title']}", '', c['question'], '']
        for p in papers:
            author = p['authors'][0] + (' et al.' if len(p['authors']) > 1 else '')
            out += [f"### {p['short_name']}", '',
                    f"**[{p['title']}]({p['source_url']})** — {author}; {p['first_published']}. `{p['tier']}`", '',
                    f"- **Models:** {p['model_size_summary']}.",
                    f"- **Contribution:** {p['contribution']}",
                    f"- **Evidence:** {p['evidence']}",
                    f"- **Limitation:** {p['limitation']}",
                    f"- **Status:** {venue_label(p)}.",
                    f"- **Source review:** {p['version_reviewed']}; metadata and abstract, checked {p['verification']['checked_on']}.", '']
    return '\n'.join(out).rstrip() + '\n'


if __name__ == '__main__':
    p = R/'README.md'
    s = p.read_text()
    a, b = '<!-- CATALOG:START -->', '<!-- CATALOG:END -->'
    p.write_text(s.split(a)[0] + a + '\n\n' + catalog() + '\n\n' + b + s.split(b)[1])
    (R/'docs/paper-catalog.md').write_text(detailed_catalog())
