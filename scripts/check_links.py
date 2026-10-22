"""Bounded, non-destructive HTTPS reachability reports. No catalog edits."""
from pathlib import Path
from datetime import datetime, timezone
import email.utils
import json
import time
import urllib.request
import urllib.error
R = Path(__file__).resolve().parents[1]

def classify(code):
    if code is None:
        return 'network_error_review'
    if 200 <= code < 400:
        return 'reachable'
    if code == 429:
        return 'rate_limited_review'
    if code in (401, 403):
        return 'access_restricted_review'
    if code in (404, 410):
        return 'missing_review'
    return 'server_or_other_error_review'

def delay(retry_after, attempt):
    try:
        seconds = float(retry_after)
    except (ValueError, TypeError):
        try:
            seconds = (email.utils.parsedate_to_datetime(retry_after) - datetime.now(timezone.utc)).total_seconds()
        except (TypeError, ValueError):
            seconds = 3 * 2**attempt
    return min(30, max(1, seconds))

def check(url):
    result = {'url': url, 'checked_at': datetime.now(timezone.utc).isoformat(), 'attempts': []}
    for attempt in range(3):
        code = None
        after = None
        error = None
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'awesome-slm-agents-reachability/0.2'})
            with urllib.request.urlopen(request, timeout=15) as response:
                code = response.status
                response.read(1024)
        except urllib.error.HTTPError as e:
            code = e.code
            after = e.headers.get('Retry-After')
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            error = str(e)
        result['attempts'].append({'status': code, 'error': error})
        if code is not None and code != 429 and code < 500:
            break
        if attempt < 2:
            time.sleep(delay(after, attempt))
    result['classification'] = classify(code)
    return result

if __name__ == '__main__':
    papers = json.loads((R/'data/papers.yaml').read_text())
    urls = set()
    for p in papers:
        urls.update([p['source_url'], p['publication']['status_source']])
        urls.update(v for v in p['resources'].values() if v)
    rows = []
    # Sequential requests limit provider pressure; this reports errors without deleting entries.
    for url in sorted(urls):
        rows.append(check(url))
        time.sleep(3)
    (R/'reports').mkdir(exist_ok=True)
    (R/'reports/link-check.json').write_text(json.dumps(rows, indent=2)+'\n')
    unresolved = sum(r['classification'] != 'reachable' for r in rows)
    print(f'{len(rows)} URLs checked; {unresolved} require review. No entries modified.')
    if unresolved:
        print('::warning::Some URLs require review; see link-reachability artifact. Temporary failures are not deletions.')
