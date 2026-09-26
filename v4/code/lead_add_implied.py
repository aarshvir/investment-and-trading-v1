"""Record a diligence agent's stated 'price-implied growth vs base case' when its summary JSON omitted the field.
Usage: python code/lead_add_implied.py TICKER=below|in_line|above "source text" [TICKER=... "source"] ..."""
import json, sys, pathlib
p = pathlib.Path(__file__).resolve().parents[1] / 'outputs' / 'lead_implied_normalization.json'
d = json.loads(p.read_text(encoding='utf-8'))
a = sys.argv[1:]
for k, src in zip(a[::2], a[1::2]):
    t, v = k.split('=')
    assert v in ('below', 'in_line', 'above'), v
    d['tickers'][t] = {'implied_vs_base': v, 'source': src}
p.write_text(json.dumps(d, indent=1), encoding='utf-8'); print(len(d['tickers']), 'tickers normalised')
