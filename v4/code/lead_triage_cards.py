"""Lead: one-line data cards for every S&P 500 member (owner request, 26 Sep 2026: every company gets at least a quick
research pass so that the model-rank gate cannot hide good businesses). Cards come only from the verified project data
(D4 live snapshot 25 Sep 2026, B1 live scores, V1 where it exists) and are split into sector-grouped batches for the
triage agents. Names that already have a full dossier (or are in full diligence) are listed but not re-triaged.
Writes v4/data/triage_cards.csv and v4/data/triage_batches.json."""
import json, pathlib, glob
import numpy as np, pandas as pd

V4 = pathlib.Path(__file__).resolve().parents[1]
S = pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet').set_index('ticker')
L = pd.read_csv(V4 / 'data' / 'b1_live_scores.csv').set_index('ticker_yahoo')
V = pd.read_csv(V4 / 'outputs' / 'v1_valuation_table.csv').set_index('ticker')
DOS = {pathlib.Path(p).stem.upper() for p in glob.glob(str(V4 / 'dossiers' / '*.md'))}
IN_DILIGENCE = {'NVDA', 'MSFT', 'AVGO', 'GOOGL', 'AMZN', 'META', 'AAPL', 'ORCL'}


def f(x):
    try:
        x = float(x)
        return None if (np.isnan(x) or np.isinf(x)) else x
    except Exception:
        return None


rows = []
for t, s in S.iterrows():
    l = L.loc[t] if t in L.index else None
    mc = f(s.get('marketCap')); fcf = f(s.get('freeCashflow')); eb = f(s.get('ebitda'))
    nd = (f(s.get('totalDebt')) or 0) - (f(s.get('totalCash')) or 0)
    fe, te = f(s.get('forwardEps')), f(s.get('trailingEps'))
    px, tgt = f(s.get('price')), f(s.get('y_targetMeanPrice'))
    rows.append({'ticker': t, 'name': s.get('name_wiki') or s.get('y_longName'), 'sector': s.get('gics_sector'), 'sub_industry': s.get('gics_sub_industry'),
                 'price': px, 'mktcap_bn': round(mc / 1e9, 1) if mc else None,
                 'pe_ntm': f(s.get('pe_ntm')), 'pe_trailing': f(s.get('trailingPE')),
                 'eps_growth_fwd_vs_ttm': (fe / te - 1) if (fe and te and te > 0) else None,
                 'revenue_growth_yoy': f(s.get('y_revenueGrowth')), 'profit_margin': f(s.get('y_profitMargins')), 'roe': f(s.get('y_returnOnEquity')),
                 'fcf_yield': (fcf / mc) if (fcf and mc) else None, 'net_debt_to_ebitda': (nd / eb) if (eb and eb > 0) else None,
                 'div_yield': f(s.get('trailingAnnualDividendYield')), 'vol_1y': f(l.vol_1y) if l is not None else None,
                 'mom_12_1': f(l.mom_12_1) if l is not None else None, 'street_target_upside': (tgt / px - 1) if (tgt and px) else None,
                 'n_analysts': f(s.get('y_numberOfAnalystOpinions')), 'model_rank': (int(l.live_rank) if l is not None and l.live_rank == l.live_rank else None),
                 'v1_verdict': V.loc[t, 'verdict'] if t in V.index else None,
                 'status': 'has full dossier' if t in DOS else ('in full diligence (F17/F18)' if t in IN_DILIGENCE else 'to triage')})
C = pd.DataFrame(rows)
for c in ['eps_growth_fwd_vs_ttm', 'revenue_growth_yoy', 'profit_margin', 'roe', 'fcf_yield', 'div_yield', 'vol_1y', 'mom_12_1', 'street_target_upside']:
    C[c] = C[c].round(3)
for c in ['pe_ntm', 'pe_trailing', 'net_debt_to_ebitda']:
    C[c] = C[c].round(1)
C.to_csv(V4 / 'data' / 'triage_cards.csv', index=False)
todo = C[C.status == 'to triage'].sort_values(['sector', 'sub_industry', 'ticker'])
batches, cur = [], []
for _, r in todo.iterrows():
    cur.append(r.ticker)
    if len(cur) >= 31:
        batches.append(cur); cur = []
if cur:
    batches.append(cur)
(V4 / 'data' / 'triage_batches.json').write_text(json.dumps({f"Q{i + 1:02d}": b for i, b in enumerate(batches)}, indent=1), encoding='utf-8')
print('cards', len(C), '| to triage', len(todo), '| batches', len(batches), [len(b) for b in batches])
print(C.status.value_counts().to_dict())
