"""Lead: independent re-derivation of the sleeve's sample-covariance risk numbers (A1 loop-2 must-fix #3).

Written without lead_risk.py or b2_risk.py: reads the portfolio weights from lead_portfolio_build.json and raw adjusted
closes from v4/data/d2_adjclose.parquet, computes simple daily returns over the same 3-year window, the annualised sample
covariance, portfolio volatility, Euler risk contributions (w_i * (Sigma w)_i / w' Sigma w), tracking error against SPY and
the average pairwise correlation, then compares each figure with lead_risk_results.json['risk_sample_cov'].
Writes v4/outputs/lead_check_risk_contrib.json."""
import json, pathlib
import numpy as np, pandas as pd

V4 = pathlib.Path(__file__).resolve().parents[1]
B = json.loads((V4 / 'outputs' / 'lead_portfolio_build.json').read_text(encoding='utf-8'))
R = json.loads((V4 / 'outputs' / 'lead_risk_results.json').read_text(encoding='utf-8'))['risk_sample_cov']
w = {k: float(v) for k, v in B['weights'].items() if float(v) > 0}
fill = 1.0 - sum(w.values())
if fill > 1e-6:
    w['SPY'] = w.get('SPY', 0.0) + fill
tot = sum(w.values()); w = {k: v / tot for k, v in w.items()}

A = pd.read_parquet(V4 / 'data' / 'd2_adjclose.parquet')
A.index = pd.to_datetime(A.index)
start, end = R['window'].split('..')
cols = list(w)
px = A.loc[:, cols + ([] if 'SPY' in cols else ['SPY'])]
ret = px.pct_change().loc[pd.Timestamp(start):pd.Timestamp(end)]
X = ret[cols].dropna(how='any')                        # same complete-case rule: days where every holding has a return
spy = ret['SPY'].reindex(X.index)
wv = np.array([w[c] for c in X.columns])
S = np.cov(X.values, rowvar=False, ddof=1) * 252       # annualised sample covariance
var_p = float(wv @ S @ wv)
contrib = wv * (S @ wv) / var_p                         # Euler decomposition; sums to 1
te = float(np.std(X.values @ wv - spy.values, ddof=1) * np.sqrt(252))   # sample std (lead_risk aligned to ddof=1 in Loop 3)
C = np.corrcoef(X.values, rowvar=False)
avg_corr = float(C[np.triu_indices(len(wv), 1)].mean())

mine = {'n_days': int(len(X)), 'vol_annual': var_p ** 0.5, 'tracking_error_annual': te, 'avg_pairwise_corr': avg_corr,
        'risk_contribution_pct_by_name': {c: float(v) for c, v in zip(X.columns, contrib)}}
cmp = {k: {'lead_risk': R.get(k), 'independent': mine[k], 'abs_diff': abs((R.get(k) or 0) - mine[k])}
       for k in ('n_days', 'vol_annual', 'tracking_error_annual', 'avg_pairwise_corr')}
rc_diff = {c: abs(R['risk_contribution_pct_by_name'].get(c, float('nan')) - v) for c, v in mine['risk_contribution_pct_by_name'].items()}
out = {'window': R['window'], 'comparison': cmp, 'max_abs_diff_risk_contribution': max(rc_diff.values()),
       'sum_of_contributions': float(contrib.sum()), 'independent': mine,
       'pass': bool(max(rc_diff.values()) < 1e-6 and all(v['abs_diff'] < 1e-6 for v in cmp.values()))}
(V4 / 'outputs' / 'lead_check_risk_contrib.json').write_text(json.dumps(out, indent=1), encoding='utf-8')
print(json.dumps({k: out[k] for k in ('window', 'comparison', 'max_abs_diff_risk_contribution', 'sum_of_contributions', 'pass')}, indent=1))
if not out['pass']:
    import sys
    sys.exit('risk numbers do not reproduce: see v4/outputs/lead_check_risk_contrib.json')
