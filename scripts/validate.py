"""Offline metadata and generated-content checks; no scientific validation."""
from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import json,re
from render import catalog
R=Path(__file__).resolve().parents[1]
P=json.loads((R/'data/papers.yaml').read_text()); C={c['id'] for c in json.loads((R/'data/taxonomy.json').read_text())}; seen=set()
for p in P:
    assert re.fullmatch(r'\d{4}\.\d{4,5}',p['id']),p['id']
    assert p['id'] not in seen,p['id'];seen.add(p['id'])
    for key in ['title','authors','contribution','evidence','limitation','source_url','model_size_summary']:assert p[key],(p['id'],key)
    assert p['primary_category'] in C
    assert p['tier'] in ['core','supporting','background']
    assert p['publication']['status'] in ['preprint','accepted_author_reported','accepted','published']
    first=date.fromisoformat(p['first_published']); checked=date.fromisoformat(p['verification']['checked_on'])
    assert first<=checked<=date.today()
    if p['last_revised']:assert first<=date.fromisoformat(p['last_revised'])<=checked
    assert urlparse(p['source_url']).scheme=='https'
    assert p['source_url'].endswith(p['id'])
    for k in ['metadata_verified','abstract_reviewed','full_text_reviewed','human_reviewed','reproduced']:assert type(p['verification'][k]) is bool
    if p['verification']['full_text_reviewed']:assert p['note'] and (R/p['note']).is_file()
    if p['verification']['reproduced']:assert p.get('reproduction_manifest')
s=(R/'README.md').read_text(); actual=s.split('<!-- CATALOG:START -->')[1].split('<!-- CATALOG:END -->')[0].strip()
assert actual==catalog(),'Run python3 scripts/render.py'
print(f'{len(P)} records: structure and generated catalog consistent; claims not independently validated.')
