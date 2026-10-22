"""Validate the schema keywords used by papers.schema.json and semantic invariants.

Standard library only. This is not a general JSON Schema implementation or a factual verifier.
"""
from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import json
import re
from render import catalog
R = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate(value, schema, at='$'):
    # Reject unknown keywords so a schema extension cannot silently go unenforced.
    supported = {'$schema', 'title', 'type', 'enum', 'minLength', 'pattern', 'format',
                 'minimum', 'properties', 'required', 'additionalProperties',
                 'items', 'uniqueItems', 'minItems'}
    require(not set(schema) - supported, f'{at}: unsupported schema keywords')
    kinds = {'null': lambda x: x is None, 'string': lambda x: isinstance(x, str),
             'boolean': lambda x: type(x) is bool, 'number': lambda x: type(x) in (int, float),
             'object': lambda x: isinstance(x, dict), 'array': lambda x: isinstance(x, list)}
    if 'type' in schema:
        allowed = schema['type'] if isinstance(schema['type'], list) else [schema['type']]
        require(any(kinds[t](value) for t in allowed), f'{at}: expected {allowed}')
    if 'enum' in schema:
        require(value in schema['enum'], f'{at}: invalid enum value')
    if isinstance(value, str):
        require(len(value) >= schema.get('minLength', 0), f'{at}: empty string')
        if 'pattern' in schema:
            require(re.search(schema['pattern'], value), f'{at}: pattern mismatch')
        if schema.get('format') == 'date':
            date.fromisoformat(value)
        if schema.get('format') == 'uri':
            u = urlparse(value)
            require(u.scheme == 'https' and u.hostname and not u.username and not u.password,
                    f'{at}: expected credential-free HTTPS URL')
    if type(value) in (int, float) and 'minimum' in schema:
        require(value >= schema['minimum'], f'{at}: below minimum')
    if isinstance(value, list):
        require(len(value) >= schema.get('minItems', 0), f'{at}: too few items')
        if schema.get('uniqueItems'):
            require(len({json.dumps(v, sort_keys=True) for v in value}) == len(value), f'{at}: duplicates')
        for i, v in enumerate(value):
            validate(v, schema['items'], f'{at}[{i}]')
    if isinstance(value, dict):
        require(not set(schema.get('required', [])) - value.keys(), f'{at}: missing required fields')
        if schema.get('additionalProperties') is False:
            require(not value.keys() - schema['properties'].keys(), f'{at}: unknown fields')
        for k, v in value.items():
            if k in schema.get('properties', {}):
                validate(v, schema['properties'][k], f'{at}.{k}')

if __name__ == '__main__':
    papers = json.loads((R/'data/papers.yaml').read_text())
    validate(papers, json.loads((R/'data/papers.schema.json').read_text()))
    categories = {c['id'] for c in json.loads((R/'data/taxonomy.json').read_text())}
    seen = set()
    titles = set()
    for p in papers:
        pid = p['id']
        require(pid not in seen, f'duplicate ID: {pid}')
        title = re.sub(r'\W+', '', p['title'].casefold())
        require(title not in titles, f'duplicate normalized title: {pid}')
        seen.add(pid)
        titles.add(title)
        require(p['primary_category'] in categories, f'{pid}: invalid category')
        first = date.fromisoformat(p['first_published'])
        checked = date.fromisoformat(p['verification']['checked_on'])
        require(first <= checked <= date.today(), f'{pid}: invalid date order')
        if p['last_revised']:
            require(first <= date.fromisoformat(p['last_revised']) <= checked, f'{pid}: revision date')
        require(p['source_url'] == f'https://arxiv.org/abs/{pid}', f'{pid}: canonical source mismatch')
        if p['parameters_active_b'] is not None and p['parameters_total_b'] is not None:
            require(p['parameters_active_b'] <= p['parameters_total_b'], f'{pid}: active > total')
        v = p['verification']
        if v['manuscript_sections_reviewed'] or v['full_text_reviewed']:
            require(p['note'] and v['sections_reviewed'], f'{pid}: missing review provenance')
        if p['note']:
            target = (R/p['note']).resolve()
            require(target.is_relative_to(R) and target.is_file(), f'{pid}: missing/outside note')
            require(p.get('note_version_reviewed'), f'{pid}: missing note version')
        if v['human_reviewed']:
            require(v['human_reviewer'], f'{pid}: missing human reviewer')
        if v['reproduced']:
            manifest = p.get('reproduction_manifest')
            require(manifest and (R/manifest).resolve().is_relative_to(R) and (R/manifest).is_file(),
                    f'{pid}: missing reproduction manifest')
        if p['publication']['status'] != 'preprint':
            require(p['publication']['venue'], f'{pid}: missing venue')
    s = (R/'README.md').read_text()
    require(s.count('<!-- CATALOG:START -->') == s.count('<!-- CATALOG:END -->') == 1, 'catalog markers')
    actual = s.split('<!-- CATALOG:START -->')[1].split('<!-- CATALOG:END -->')[0].strip()
    require(actual == catalog(), 'Run python3 scripts/render.py')
    print(f'{len(papers)} records: schema, invariants, and generated catalog consistent. Not scientific validation.')
