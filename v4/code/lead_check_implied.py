"""List diligence summaries whose tickers lack implied_vs_base both in the summary and in the normalization file."""
import json, glob, pathlib
V4 = pathlib.Path(__file__).resolve().parents[1]
N = json.loads((V4 / 'outputs' / 'lead_implied_normalization.json').read_text(encoding='utf-8'))['tickers']
for f in sorted(glob.glob(str(V4 / 'outputs' / 'F[1-9]*_summary.json'))):
    d = json.loads(pathlib.Path(f).read_text(encoding='utf-8')); T = d.get('tickers', d)
    it = T.items() if isinstance(T, dict) else [(x.get('ticker'), x) for x in T]
    for t, x in it:
        if not isinstance(x, dict) or 'verdict' not in x: continue
        iv = ((x.get('valuation_view_vs_v1') or {}).get('implied_vs_base'))
        print(pathlib.Path(f).stem.split('_')[0], t, x['verdict'], iv or ('norm:' + N[t]['implied_vs_base'] if t in N else 'MISSING'))
