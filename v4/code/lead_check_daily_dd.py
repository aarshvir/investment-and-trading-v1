"""Lead: independent cross-check of B1's DAILY max drawdown for the primary top-30 (A1 loop-1 must-fix #3).
Re-selects each month's top 30 from B1's stored panel (composite, in-universe, priced), holds them equal-weight from month-end t
to month-end t+1 on D2 daily adjusted closes (buy-and-hold within the month, rebalanced monthly), and measures the worst
peak-to-trough fall of the daily wealth path. Written independently of b1_*.py (only the stored panel and D2 prices are used)."""
import pandas as pd, numpy as np, pathlib, json
V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
P = pd.read_parquet(V4 / 'data' / 'b1_panel.parquet')
A = pd.read_parquet(V4 / 'data' / 'd2_adjclose.parquet')
A.index = pd.to_datetime(A.index)
comp = 'composite' if 'composite' in P.columns else [c for c in P.columns if c.startswith('composite')][0]
P = P[(P['in_universe'] == True) & P[comp].notna() & P['series'].notna()]
P['month_end'] = pd.to_datetime(P['month_end'])
months = sorted(P.month_end.unique())
months = [m for m in months if pd.Timestamp('2011-12-31') <= m <= pd.Timestamp('2026-07-31')]
wealth = []; level = 1.0
for i, m in enumerate(months[:-1]):
    nxt = months[i + 1]
    g = P[P.month_end == m].nlargest(30, comp)
    cols = [s for s in g.series if s in A.columns]
    seg = A.loc[(A.index >= m) & (A.index <= nxt), cols]
    if len(seg) < 2: continue
    base = seg.iloc[0]
    ok = base.notna() & (base > 0)
    seg = seg.loc[:, ok].ffill()
    rel = seg.divide(base[ok]).mean(axis=1)         # equal-weight buy-and-hold within the month
    path = level * rel.iloc[1:]
    wealth.append(path); level = float(path.iloc[-1])
W = pd.concat(wealth)
dd = W / W.cummax() - 1
spy = A['SPY'].loc[W.index[0]:W.index[-1]]
sdd = spy / spy.cummax() - 1
res = {'top30_daily_mdd_gross': float(dd.min()), 'date': str(dd.idxmin().date()), 'spy_daily_mdd_same_window': float(sdd.min()),
       'b1_reported': json.loads((V4 / 'outputs' / 'b1_results.json').read_text())['primary_top30_daily'],
       'cagr_gross_daily_path': float(W.iloc[-1] ** (252 / len(W)) - 1), 'start': str(W.index[0].date()), 'end': str(W.index[-1].date())}


# ---- second check (A1 loop-1 must-fix #3, part 2): the pre-committed SLEEVE RULE, re-implemented without b1_sleeve.py
# or lead_portfolio.py. Quarter-ends; composite ranking among in-universe names with 1-yr vol <= 45%; top 20 with <= 2 per
# SIC-4 and <= 5 per sector; weights ~ 1/vol, clipped to 3-8%, sector cap 25%, by simple iterative water-filling (B1 uses a
# constrained least-squares solver, so small weight differences are expected); buy-and-hold within each quarter; 10 bps
# on traded weight at each rebalance.
def sleeve_weights(g, lo=0.03, hi=0.08, sec_cap=0.25):
    w = (1 / g['vol_1y']).astype(float); w = w / w.sum()
    for _ in range(200):
        w = w.clip(lo, hi)
        sec = g['sector'].values
        for s in set(sec):
            m = sec == s
            tot = w[m].sum()
            if tot > sec_cap:
                w[m] = w[m] * sec_cap / tot
        free = (w > lo + 1e-12) & (w < hi - 1e-12)
        gap = 1.0 - w.sum()
        if abs(gap) < 1e-10 or not free.any():
            break
        w[free] = w[free] + gap * w[free] / w[free].sum()
    return w / w.sum() if abs(w.sum() - 1) > 1e-6 and w.sum() > 0 else w


Q = pd.read_parquet(V4 / 'data' / 'b1_panel.parquet')
Q['month_end'] = pd.to_datetime(Q['month_end'])
Q = Q[(Q['in_universe'] == True) & Q['composite'].notna() & Q['series'].notna() & Q['vol_1y'].notna()]
qd = [m for m in sorted(Q.month_end.unique()) if m.month in (3, 6, 9, 12) and pd.Timestamp('2011-12-31') <= m <= pd.Timestamp('2026-06-30')]
qd = qd + [pd.Timestamp('2026-08-31')]
parts, level, prev = [], 1.0, pd.Series(dtype=float)
for i, m in enumerate(qd[:-1]):
    g = Q[(Q.month_end == m) & (Q.vol_1y <= 0.45)].sort_values(['composite', 'entity'], ascending=[False, True])
    picks, s4c, sc = [], {}, {}
    for r in g.itertuples(index=False):
        k4 = int(r.sic) if r.sic == r.sic else -1
        if k4 >= 0 and s4c.get(k4, 0) >= 2: continue
        if sc.get(r.sector, 0) >= 5: continue
        if r.series not in A.columns: continue
        picks.append(r); s4c[k4] = s4c.get(k4, 0) + 1; sc[r.sector] = sc.get(r.sector, 0) + 1
        if len(picks) == 20: break
    sel = pd.DataFrame(picks).set_index('series')
    w = sleeve_weights(sel)
    seg = A.loc[(A.index >= m) & (A.index <= qd[i + 1]), list(sel.index)]
    base = seg.iloc[0]; ok = base.notna() & (base > 0)
    w = w[ok.values]; w = w / w.sum()
    traded = float((w.reindex(w.index.union(prev.index), fill_value=0) - prev.reindex(w.index.union(prev.index), fill_value=0)).abs().sum())
    level *= (1 - 0.0010 * traded)
    rel = seg.loc[:, ok].ffill().divide(base[ok])
    path = level * (rel * w.values).sum(axis=1)
    parts.append(path.iloc[1:]); level = float(path.iloc[-1])
    end_val = w * rel.iloc[-1]; prev = end_val / end_val.sum()
WS = pd.concat(parts); dds = WS / WS.cummax() - 1
b1s = json.loads((V4 / 'outputs' / 'b1_results.json').read_text())['phase_b']['lead_sleeve']['sleeve_top20_invvol_q (as implemented)']
res['sleeve_rule'] = {'daily_mdd_net': float(dds.min()), 'date': str(dds.idxmin().date()), 'cagr_net_daily_path': float(WS.iloc[-1] ** (252 / len(WS)) - 1),
                      'b1_reported_mdd_daily': b1s.get('mdd_daily'), 'b1_reported_date': b1s.get('mdd_daily_date'), 'b1_reported_cagr': b1s.get('cagr'),
                      'note': 'independent re-implementation (water-filling weights, own selection loop); B1 uses a least-squares solver'}
(V4 / 'outputs' / 'lead_check_daily_dd.json').write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))
