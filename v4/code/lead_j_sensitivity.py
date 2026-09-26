"""Rule (j) sensitivity (A1/A2 loop-3 and loop-4 must-fix).

Rule (j) picks the final 20 from the eligible pool by (1) conviction, (2) margin of safety, (3) base-case 3-yr return,
then model rank, with at most two names per GICS sub-industry. It was written after the wave-1 diligence verdicts were
known, so this script re-runs the selection under alternative, equally defensible orderings and reports how much of the
20-name list, and its risk, depends on the ordering chosen. Weights use the same inverse-volatility x conviction rule and
caps as the build. Reads only lead_portfolio_build.json and the price panel; writes outputs/lead_j_sensitivity.json.
"""
import json, pathlib, sys
import numpy as np, pandas as pd
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lead_portfolio import build_weights
import b2_risk as b2

V4 = pathlib.Path(__file__).resolve().parents[1]
O = V4 / 'outputs'
B = json.loads((O / 'lead_portfolio_build.json').read_text(encoding='utf-8'))
E = pd.DataFrame([c for c in B['candidates'] if c['eligible']])
E['_conv'] = np.where(E.verdict == 'INCLUDE', 0, 1)
E['_marg'] = E['implied'].map({'below': 0, 'in_line': 1}).fillna(2)
E['_base'] = pd.to_numeric(E['base'], errors='coerce').fillna(-9)
E['_rank'] = pd.to_numeric(E['rank'], errors='coerce').fillna(999)

ORDERS = {
    'actual (j): conviction, margin, base return, rank': (['_conv', '_marg', '_base', '_rank'], [True, True, False, True]),
    'base return before margin of safety': (['_conv', '_base', '_marg', '_rank'], [True, False, True, True]),
    'margin of safety before conviction': (['_marg', '_conv', '_base', '_rank'], [True, True, False, True]),
    'model rank instead of base return': (['_conv', '_marg', '_rank'], [True, True, True]),
    'conviction then model rank only': (['_conv', '_rank'], [True, True]),
}
prices = b2.load_prices()
EP = [('Global financial crisis', '2007-10-09', '2009-03-09'), ('COVID crash', '2020-02-19', '2020-03-23'), ('2022 inflation bear market', '2022-01-03', '2022-10-12')]


def select(cols, asc):
    sel, sub, sec = [], {}, {}
    for _, r in E.sort_values(cols, ascending=asc).iterrows():
        if sub.get(r['sub'], 0) >= 2 or sec.get(r['s'], 0) >= 5:   # same sub-industry (2) and sector (5, rule l) limits as the build
            continue
        if len(sel) >= 20:
            break
        sel.append(r['t']); sub[r['sub']] = sub.get(r['sub'], 0) + 1; sec[r['s']] = sec.get(r['s'], 0) + 1
    return sel


out, base_set = {}, None
for name, (cols, asc) in ORDERS.items():
    sel = select(cols, asc)
    P = E.set_index('t').loc[sel].copy()
    P['sector'] = P['s']; P['mult'] = np.where(P.verdict == 'INCLUDE-SMALL', 0.5, 1.0)
    w, cash, checks, _ = build_weights(P, hi=0.10, lo=0.03, sector_cap=0.25, sub_cap=0.12, vol_col='vol', mult_col='mult', cap_by_mult=True)
    wd = {t: float(v) for t, v in w.items() if v > 0}
    if cash and cash > 1e-9:
        wd['SPY'] = wd.get('SPY', 0) + float(cash)
    s = sum(wd.values()); wd = {k: v / s for k, v in wd.items()}
    path = b2.portfolio_daily_path(wd, start='2005-01-03', end='2026-09-25', rebalance='Q', missing='exclude', prices=prices)
    ep = {}
    for en, a, b in EP:
        r = path.daily_return.loc[a:b].iloc[1:]
        ep[en] = float((1 + r.fillna(0)).prod() - 1)
    r3 = path.daily_return.loc['2023-09-25':'2026-09-25'].dropna()
    spy = prices['SPY'].pct_change().reindex(r3.index)
    base_set = base_set or set(sel)
    out[name] = {'names': sel, 'overlap_with_actual': len(set(sel) & base_set), 'full_conviction': int((P.verdict == 'INCLUDE').sum()),
                 'weighted_base_return': float(sum(wd.get(t, 0) * (P.loc[t, '_base'] if P.loc[t, '_base'] > -9 else 0) for t in sel)),
                 'vol_3y': float(r3.std() * np.sqrt(252)), 'te_3y': float((r3 - spy).std() * np.sqrt(252)), 'episodes': ep,
                 'index_fill': float(cash or 0)}
    print(f"{name:55s} overlap {out[name]['overlap_with_actual']:2d}/20  full {out[name]['full_conviction']:2d}  "
          f"GFC {ep['Global financial crisis']:+.1%}  COVID {ep['COVID crash']:+.1%}  2022 {ep['2022 inflation bear market']:+.1%}  vol {out[name]['vol_3y']:.1%}")
core = set.intersection(*[set(v['names']) for v in out.values()])
_ord = E.sort_values(['_conv', '_marg', '_base', '_rank'], ascending=[True, True, False, True]).reset_index(drop=True)
_held = set(B['selected'])
_why = {c['t']: c.get('why') for c in B['candidates']}
bench = [{'t': r['t'], 'position_in_j_order': int(i) + 1, 'conviction': 'full' if r['verdict'] == 'INCLUDE' else 'half',
          'implied_vs_base': r['implied'], 'base_return': (None if r['_base'] == -9 else round(float(r['_base']), 4)), 'why_not_held': _why.get(r['t'])}
         for i, r in _ord.iterrows() if r['t'] not in _held]
res = {'bench_near_misses': bench, 'orderings': out, 'in_every_ordering': sorted(core), 'n_in_every_ordering': len(core),
       'note': 'Same eligible pool, caps and weights as the build; only the selection order differs. Stress figures are buy-and-hold over each S&P 500 peak-to-trough window, missing prices renormalised out (as in lead_risk.py).'}
(O / 'lead_j_sensitivity.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
print('in every ordering:', len(core), sorted(core))
