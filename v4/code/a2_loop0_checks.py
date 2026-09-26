"""A2 (fundamental / IC auditor) - loop 0 baseline: independent re-computation of v3 headline numbers.

Read-only on the legacy bundle (PROJECT/equity_project). Writes nothing except stdout and
C:/Users/user/eqv4/cache/a2/a2_loop0_checks.json.  Run (Git Bash):
    PYTHONPATH='C:\\Users\\user\\eqv4\\pylib' python a2_loop0_checks.py
All logic is written independently of the lead's lead_check_*.py scripts (same inputs, own code).
"""
import json, math, os, pickle, warnings
import numpy as np, pandas as pd

warnings.filterwarnings('ignore')
LEG = r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\equity_project'
OUT = r'C:\Users\user\eqv4\cache\a2\a2_loop0_checks.json'
P14 = ['NVDA', 'CPAY', 'AMP', 'RL', 'AME', 'SNA', 'ABNB', 'NTAP', 'PAYX', 'MSFT', 'IBKR', 'HIG', 'ALLE', 'AIZ']
R = {}

X = pd.read_pickle(os.path.join(LEG, 'conv.pkl')).set_index('t')
C = pd.read_pickle(os.path.join(LEG, 'close10.pkl'))
cp = json.load(open(os.path.join(LEG, 'conv_port.json')))
w_rep = pd.Series(cp['w'])

# ---------------------------------------------------------------- 1. weights & constraints (own re-implementation of conv_port.py rules)
cand = X[(X.stab >= 0.5) & (X.E_cons >= 0.08)].sort_values('cscore', ascending=False)
pick, subs = [], set()
for t, r in cand.iterrows():
    if r['sub'] in subs:
        continue
    pick.append(t); subs.add(r['sub'])
w = X.loc[pick, 'cscore'] * (0.5 + X.loc[pick, 'stab']); w = w / w.sum()
for _ in range(50):
    w = w.clip(0.04, 0.10); w = w / w.sum()
    for s in set(X.loc[pick, 'sector']):
        m = X.loc[pick, 'sector'] == s
        if w[m].sum() > 0.25:
            w[m] *= 0.25 / w[m].sum()
    w = w / w.sum()
sec = w.groupby(X.loc[pick, 'sector']).sum()
R['1_weights'] = dict(pick_matches=pick == list(w_rep.index), max_abs_diff_vs_reported=float((w - w_rep).abs().max()),
                      RL=float(w['RL']), ABNB=float(w['ABNB']), sector_sums=sec.round(6).to_dict(),
                      names_over_10pct=[k for k, v in w.items() if v > 0.10 + 1e-9],
                      sectors_over_25pct=[k for k, v in sec.items() if v > 0.25 + 1e-9],
                      max_feasible_invest=float(sum(min(0.25, 0.10 * n) for n in X.loc[pick].groupby('sector').size())))

# ---------------------------------------------------------------- 2. expected return & method coverage
Y = X.loc[P14]
R['2_E'] = dict(E_port=float((w_rep * Y.E_cons).sum()), n_with_E_scen=int(Y.E_scen.notna().sum()),
                missing_E_scen=list(Y.index[Y.E_scen.isna()]),
                E_bb_capped_40=list(Y.index[Y.E_bb >= 0.3999]), rerate_at_cap=list(Y.index[Y.bb_rerate.abs() >= 0.0999]),
                weighted_net_buyback_yield=float((w_rep * Y.nby).sum()),
                weighted_rerate=float((w_rep * Y.bb_rerate).sum()))
# CAPM-consistent market leg instead of 10% x adj-beta (rf 4.2% + b x 5.8% keeps the market at 10%)
badj = np.clip(0.67 * X.beta3.fillna(1) + 0.33, 0.6, 1.6)
capm = 0.042 + 0.058 * badj
Ebb_nobb = np.clip(X.E_bb - X.nby.fillna(0), -0.3, 0.4)  # remove buyback yield double count (EPS growth is per share)
Efin2 = pd.concat([Ebb_nobb, X.E_fac - 0.10 * badj + capm, X.E_scen], axis=1).mean(axis=1)
X['E_cons_fix'] = 0.5 * Efin2 + 0.5 * capm
cand2 = X[(X.stab >= 0.5) & (X.E_cons_fix >= 0.08)].sort_values('cscore', ascending=False)
pick2, subs2 = [], set()
for t, r in cand2.iterrows():
    if r['sub'] in subs2:
        continue
    pick2.append(t); subs2.add(r['sub'])
R['2b_E_fix'] = dict(E_port_fix_same_weights=float((w_rep * X.loc[P14, 'E_cons_fix']).sum()),
                     per_name={t: [round(float(X.loc[t, 'E_cons']), 4), round(float(X.loc[t, 'E_cons_fix']), 4)] for t in P14},
                     dropped=[t for t in P14 if t not in pick2], added=[t for t in pick2 if t not in P14])

# ---------------------------------------------------------------- 3. vol, missing history, drawdowns
Cf = C.ffill()
M = Cf[P14].resample('ME').last().pct_change().iloc[-121:]
R['3_hist'] = dict(months=len(M), abnb_missing_months=int(M['ABNB'].isna().sum()),
                   vol_monthly=float((M.fillna(0) @ w_rep[P14]).std() * np.sqrt(12)))
pm = (M.fillna(0) @ w_rep[P14]).values
eq = np.cumprod(1 + pm)
R['3_hist']['mdd_month_end'] = float((eq / np.maximum.accumulate(eq) - 1).min())
# daily wealth path, rebalanced to target weights on the first trading day of each month (pre-IPO ABNB = cash, as v3)
D = Cf[P14].loc['2016-09-01':].pct_change().fillna(0)
val, hold, prev_m, path = 1.0, None, None, []
for dt_, row in D.iterrows():
    if prev_m != (dt_.year, dt_.month):
        hold = w_rep[P14].values * val; prev_m = (dt_.year, dt_.month)
    hold = hold * (1 + row.values); val = hold.sum(); path.append(val)
path = pd.Series(path, index=D.index)
dd = path / path.cummax() - 1
R['3_hist']['mdd_daily'] = float(dd.min()); R['3_hist']['mdd_daily_trough'] = str(dd.idxmin().date())
R['3_hist']['covid_daily_0219_0323'] = float(path.loc['2020-03-23'] / path.loc[:'2020-02-19'].iloc[-1] - 1)
spx = Cf['^GSPC'].loc['2016-09-01':]
R['3_hist']['spx_price_mdd_daily'] = float((spx / spx.cummax() - 1).min())

# ---------------------------------------------------------------- 4. bootstrap odds (own implementation of the v3 re-centred circular block bootstrap)
Ms = Cf['^GSPC'].resample('ME').last().pct_change().iloc[-121:].fillna(0).values


def boot(m, E, months, n=20000, blk=3, seed=5):
    rng = np.random.default_rng(seed)
    m = m - m.mean() + (1 + E) ** (1 / 12) - 1
    T = len(m); out = np.empty(n)
    for i in range(n):
        starts = rng.integers(0, T, months // blk)
        idx = (starts[:, None] + np.arange(blk)[None, :]).ravel() % T
        out[i] = np.prod(1 + m[idx]) - 1
    return out


E14 = R['2_E']['E_port']
R['4_odds'] = dict(p_pos1_stock=float((boot(pm, E14, 12) > 0).mean()), p_pos5_stock=float((boot(pm, E14, 60) > 0).mean()))
blend = 0.5 * pm + 0.5 * Ms
R['4_odds']['blend_by_drift'] = {f'{d:.4f}': float((boot(blend, d, 60) > 0).mean()) for d in [0.04, 0.06, 0.08, 0.10, 0.5 * E14 + 0.05]}
R['4_odds']['blend_5th_pct_1y_at_orig'] = float(np.percentile(boot(blend, 0.5 * E14 + 0.05, 12), 5))

# ---------------------------------------------------------------- 5. valuation horizon: FY1/FY2 vs time-weighted NTM
I = json.load(open(os.path.join(LEG, 'info.json'), encoding='utf-8'))
asof = pd.Timestamp('2026-09-24')
ntm = {}
for t in P14:
    fye = pd.Timestamp(I[t]['nextFiscalYearEnd'], unit='s')  # end of current fiscal year (0y)
    frac0 = min(max((fye - asof).days / 365.25, 0), 1)       # share of NTM window still in FY0
    e0, e1, p = X.loc[t, 'eps0'], X.loc[t, 'eps1'], X.loc[t, 'price']
    e_ntm = frac0 * e0 + (1 - frac0) * e1
    ntm[t] = dict(fy0_end=str(fye.date()), pe_reported=round(float(X.loc[t, 'fpe']), 2), pe_fy0=round(float(p / e0), 2),
                  pe_ntm=round(float(p / e_ntm), 2), ntm_vs_reported=round(float(p / e_ntm / X.loc[t, 'fpe'] - 1), 4))
R['5_ntm'] = ntm

# ---------------------------------------------------------------- 6. lens evidence gaps
nog = X.cuts4.isna()
R['6_lenses'] = dict(no_guidance_record=int(nog.sum()), no_guidance_but_pass_mgmt=int((nog & X['L_Management & red flags']).sum()),
                     fin_names_in_14_pass_BS_on_ROE=[t for t in P14 if X.loc[t, 'sector'] in ('Financials', 'Real Estate')],
                     nd_ebitda_CPAY=float(X.loc['CPAY', 'nd_ebitda']))
L = X[[c for c in X.columns if c.startswith('L_')]].astype(float)
cm = L.corr().values.copy(); np.fill_diagonal(cm, np.nan)
R['6_lenses']['max_lens_corr'] = float(np.nanmax(cm))
R['6_lenses']['vendor_fcf_yield_used'] = {t: round(float(X.loc[t, 'fcfy']), 4) if X.loc[t, 'fcfy'] == X.loc[t, 'fcfy'] else None for t in ['NVDA', 'MSFT', 'HIG', 'AIZ', 'AMP']}

# ---------------------------------------------------------------- 7. risk contributions, correlation, index overlap
W3 = Cf[P14 + ['^GSPC']].resample('W-FRI').last().pct_change().iloc[-156:]
cov = W3[P14].cov() * 52
wv = w_rep[P14].values
pvar = wv @ cov.values @ wv
rc = pd.Series(wv * (cov.values @ wv) / pvar, index=P14)
corr = W3[P14].corr().values; iu = np.triu_indices(14, 1)
beta = {t: float(W3[t].cov(W3['^GSPC']) / W3['^GSPC'].var()) for t in P14}
R['7_risk'] = dict(vol_3y_weekly=float(np.sqrt(pvar)), risk_contrib=rc.round(4).to_dict(),
                   ai_cluster_weight=float(w_rep[['NVDA', 'MSFT', 'NTAP']].sum()), ai_cluster_risk=float(rc[['NVDA', 'MSFT', 'NTAP']].sum()),
                   avg_pairwise_corr=float(corr[iu].mean()), port_beta_3y=float(sum(w_rep[t] * beta[t] for t in P14)),
                   sleeve_corr_with_spx=float(pd.Series(W3[P14].values @ wv, index=W3.index).corr(W3['^GSPC'])))
mc = pd.Series({t: I[t].get('marketCap') for t in X.index}).astype(float)
sp_w = mc / mc.sum()
R['7_risk']['spx_capweight_proxy'] = {t: round(float(sp_w[t]), 4) for t in ['NVDA', 'MSFT']}
R['7_risk']['blend_5050_lookthrough'] = {t: round(float(0.5 * w_rep[t] + 0.5 * sp_w[t]), 4) for t in ['NVDA', 'MSFT']}
secw = sp_w.groupby(X.sector).sum()
R['7_risk']['spx_sector_weight_of_sectors_absent_from_14'] = float(secw.drop(list(sec.index)).sum())
R['7_risk']['sectors_absent'] = sorted(set(secw.index) - set(sec.index))

json.dump(R, open(OUT, 'w'), indent=1, default=float)
print(json.dumps(R, indent=1, default=float))
