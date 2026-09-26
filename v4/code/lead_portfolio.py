"""Lead: constrained portfolio construction with post-solve verification (fixes v3 bug: caps broken by renormalisation).

Target weights: inverse-volatility (risk-balanced) x diligence multiplier (INCLUDE=1, INCLUDE-SMALL=0.5).
Solve  min sum((w - target)^2)  s.t.  sum(w)=1-cash,  lo<=w<=hi,  sector sums<=sector_cap,  sub-industry sums<=sub_cap.
If infeasible, the residual is reported as cash rather than silently breaking a cap.
"""
import numpy as np, pandas as pd
from scipy.optimize import minimize


def feasible_max_investment(df, hi, sector_cap, sub_cap, hi_col=None):
    """Upper bound on total investable weight given caps (per sector: min(cap, sum of per-name caps within sub-industry caps)).
    hi_col (optional) names a column of per-name caps; otherwise every name has the scalar cap hi."""
    tot = 0.0
    for s, g in df.groupby('sector'):
        cap_s = 0.0
        for sub, h in g.groupby('sub'):
            cap_s += min(sub_cap, float(h[hi_col].sum()) if hi_col else hi * len(h))
        tot += min(sector_cap, cap_s)
    return tot


def build_weights(df, hi=0.08, lo=0.03, sector_cap=0.25, sub_cap=0.10, vol_col='vol', mult_col='mult', cap_by_mult=False):
    """cap_by_mult=True scales each name's cap (and floor) by its diligence multiplier, so a half-conviction name
    (mult 0.5) is held between lo/2 and hi/2 (Loop-2 amendment; see STATE.md). The un-investable remainder is returned
    as the second value; the caller decides where it goes (the v4 sleeve sends it to the index core, not to cash)."""
    df = df.copy()
    mult = df[mult_col].astype(float) if mult_col in df.columns else pd.Series(1.0, index=df.index)
    tgt = (1.0 / df[vol_col]) * mult
    tgt = tgt / tgt.sum()
    df['_hi'] = hi * mult if cap_by_mult else hi
    maxinv = feasible_max_investment(df, hi, sector_cap, sub_cap, hi_col='_hi')
    invest = min(1.0, maxinv)
    n = len(df)
    secs = df['sector'].values
    subs = df['sub'].values
    cons = [{'type': 'eq', 'fun': lambda w: w.sum() - invest}]
    for s in set(secs):
        m = secs == s
        cons.append({'type': 'ineq', 'fun': lambda w, m=m: sector_cap - w[m].sum()})
    for s in set(subs):
        m = subs == s
        cons.append({'type': 'ineq', 'fun': lambda w, m=m: sub_cap - w[m].sum()})
    hi_eff = df['_hi'].values.astype(float)
    lo_eff = np.minimum(lo * mult.values, hi_eff)
    bounds = list(zip(lo_eff, hi_eff))
    x0 = np.clip(tgt.values * invest, lo_eff, hi_eff)
    r = minimize(lambda w: ((w - tgt.values * invest) ** 2).sum(), x0, bounds=bounds, constraints=cons,
                 method='SLSQP', options={'maxiter': 1000, 'ftol': 1e-12})
    if not r.success:
        raise RuntimeError('solver failed: ' + r.message)
    w = pd.Series(r.x, index=df.index)
    checks = verify(df.assign(w=w), hi_eff, lo_eff, sector_cap, sub_cap, invest)
    return w, 1 - invest, checks, tgt


def verify(df, hi, lo_eff, sector_cap, sub_cap, invest, tol=1e-6):
    hi_arr = np.broadcast_to(np.asarray(hi, dtype=float), (len(df),))
    rows = []
    rows.append(('Weights sum to invested share', invest, df.w.sum(), abs(df.w.sum() - invest) < tol))
    rows.append(('Max single name', float(hi_arr.max()), df.w.max(), bool((df.w.values <= hi_arr + tol).all())))
    if hi_arr.min() < hi_arr.max() - tol:
        m = hi_arr < hi_arr.max() - tol
        rows.append(('Max half-conviction name', float(hi_arr[m].max()), float(df.w.values[m].max()), bool((df.w.values[m] <= hi_arr[m] + tol).all())))
    rows.append(('Min single name (per-name floor)', float(np.min(lo_eff)), df.w.min(), bool((df.w.values >= lo_eff - tol).all())))
    ss = df.groupby('sector').w.sum()
    rows.append(('Max sector', sector_cap, ss.max(), ss.max() <= sector_cap + tol))
    su = df.groupby('sub').w.sum()
    rows.append(('Max sub-industry', sub_cap, su.max(), su.max() <= sub_cap + tol))
    out = pd.DataFrame(rows, columns=['constraint', 'limit', 'actual', 'pass'])
    if not out['pass'].all():
        raise AssertionError('constraint violated:\n' + out.to_string())
    return out


if __name__ == '__main__':
    # self-test on the v3 portfolio universe: 4 sectors -> must report cash rather than breach caps
    demo = pd.DataFrame({'sector': ['IT'] * 3 + ['Fin'] * 5 + ['Ind'] * 4 + ['CD'] * 2,
                         'sub': list('abcdefghijklmn'), 'vol': np.linspace(.2, .4, 14), 'mult': 1.0},
                        index=['NVDA', 'NTAP', 'MSFT', 'CPAY', 'AMP', 'IBKR', 'HIG', 'AIZ', 'AME', 'SNA', 'PAYX', 'ALLE', 'RL', 'ABNB'])
    w, cash, checks, _ = build_weights(demo, hi=0.10, lo=0.04, sector_cap=0.25, sub_cap=0.10)
    print(checks.to_string()); print('cash', round(cash, 4)); print(w.round(4).to_string())
    assert abs(cash - 0.05) < 1e-6, 'v3 universe under v3 caps should leave exactly 5% cash'
    print('self-test passed: v3 caps are infeasible at 100% invested; max investable = 95%')
