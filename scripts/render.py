"""Render only the catalog block from the structured source of truth."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def catalog():
    papers=json.loads((R/'data/papers.yaml').read_text())
    categories=json.loads((R/'data/taxonomy.json').read_text())
    out=[]
    for c in categories:
        out += [f"### {c['title']}", '', c['question'], '']
        subset=sorted((p for p in papers if p['primary_category']==c['id']),key=lambda p:p['first_published'],reverse=True)
        if not subset: out += ['No entries selected yet; contributions with primary evidence are welcome.', '']
        for p in subset:
            author=p['authors'][0]+(' et al.' if len(p['authors'])>1 else '')
            out += [f"- **[{p['title']}]({p['source_url']})** — {author}; first published {p['first_published']}. `{p['tier']}`", f"  - Models: {p['model_size_summary']}. Reviewed source: {p['version_reviewed']}; {('selected manuscript sections' if p['verification'].get('manuscript_sections_reviewed') else 'metadata + abstract only')}.", f"  - Contribution: {p['contribution']}", f"  - Evidence: {p['evidence']}", f"  - Limitation: {p['limitation']}", f"  - Status: [{p['publication']['venue'] or p['publication']['status']}]({p['publication']['status_source']}). Checked {p['verification']['checked_on']}.", *(([f"  - [Focused note]({p['note']}) (manuscript {p.get('note_version_reviewed', p['version_reviewed'])}; selected sections, not exhaustive audit)."]) if p['note'] else []), *(([f"  - [Code]({p['resources']['code']}) (availability checked; not reproduced)."]) if p['resources']['code'] else []), '']
    return '\n'.join(out).rstrip()
if __name__=='__main__':
    p=R/'README.md';s=p.read_text();a='<!-- CATALOG:START -->';b='<!-- CATALOG:END -->'
    p.write_text(s.split(a)[0]+a+'\n\n'+catalog()+'\n\n'+b+s.split(b)[1])
