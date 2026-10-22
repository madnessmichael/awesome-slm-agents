"""Non-blocking reachability report; never edits catalog entries."""
from pathlib import Path
import json,time,urllib.request,urllib.error
R=Path(__file__).resolve().parents[1];rows=[]
urls={p['source_url'] for p in json.loads((R/'data/papers.yaml').read_text())}
for url in sorted(urls):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'awesome-slm-agents-link-check/0.1'})
        with urllib.request.urlopen(req,timeout=25) as r:status=r.status
    except Exception as e:status=str(e)
    rows.append({'url':url,'status':status});time.sleep(3)
(R/'reports').mkdir(exist_ok=True);(R/'reports/link-check.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
