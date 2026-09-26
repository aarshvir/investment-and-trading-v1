"""Lead: risk view for the final v4 sleeve and the model allocations (index core + sleeve + T-bill reserve),
using B2's tested module. Scenario drifts from R1 (Bear 2% / Base 6% / Bull 9% geometric, cash 4%).
Sleeve alpha is set to ZERO in every scenario (B1 found no evidence of edge), so the sleeve contributes
tracking error and diversification, not assumed excess return.
Usage: python lead_risk.py [weights_json]   (default: v4/outputs/lead_portfolio_build.json 'weights')"""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent))
from lead_guard import check_build_fresh
check_build_fresh()  # stops with StaleBuildError if any input changed after the portfolio build
import sys, json, pathlib, math
import numpy as np, pandas as pd
CODE = pathlib.Path(__file__).parent
sys.path.insert(0, str(CODE))
import b2_risk as b2

V4 = CODE.parent
SCEN = {'Bear': 0.02, 'Base': 0.06, 'Bull': 0.09}
CASH = 0.04
MODELS = {  # name: (core SPY, sleeve, reserve)
    'Index only (100/0/0)': (1.00, 0.00, 0.00),
    'Growth (80/20/0)': (0.80, 0.20, 0.00),
    'Moderate (55/15/30)': (0.55, 0.15, 0.30),
    'Cautious (35/10/55)': (0.35, 0.10, 0.55),
    'Defensive (15/10/75)': (0.15, 0.10, 0.75),   # the full-deployment equity budget of Codex release v005 (15% index, 10% direct, 75% reserve)
}
EPISODES = [('Global financial crisis', '2007-10-09', '2009-03-09'), ('US downgrade / euro crisis', '2011-07-07', '2011-10-03'),
            ('China devaluation sell-off', '2015-07-20', '2016-02-11'), ('Q4 2018 rate scare', '2018-09-20', '2018-12-24'),
            ('COVID crash', '2020-02-19', '2020-03-23'), ('2022 inflation bear market', '2022-01-03', '2022-10-12')]


def clean(x):
    if isinstance(x, dict): return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [clean(v) for v in x]
    if isinstance(x, (float, np.floating)): return None if (x != x or math.isinf(x)) else round(float(x), 6)
    if isinstance(x, (np.integer,)): return int(x)
    return x


def main(wfile=None):
    if wfile:
        w = json.loads(pathlib.Path(wfile).read_text())
    else:
        w = json.loads((V4 / 'outputs' / 'lead_portfolio_build.json').read_text(encoding='utf-8'))['weights']
    w = {k: float(v) for k, v in w.items() if float(v) > 0}
    fill = 1.0 - sum(w.values())
    if fill > 1e-6:   # sleeve capacity the caps cannot absorb is held in the index core: model it as SPY, not cash
        w['SPY'] = w.get('SPY', 0.0) + fill
    tot = sum(w.values()); w = {k: v / tot for k, v in w.items()}
    prices = b2.load_prices()
    spy = prices['SPY'].pct_change()
    path = b2.portfolio_daily_path(w, start='2005-01-03', end='2026-09-25', rebalance='Q', missing='exclude', prices=prices)
    sr = path.daily_return.reindex(spy.index)
    ps = path.summary()
    out = {'weights_sleeve_normalised': w, 'sleeve_history': ps, 'index_fill_in_sleeve': max(0.0, fill)}

    # A3 loop-1 must-fix: one unambiguous "worst fall" for the sleeve (full daily history at today's weights), with dates,
    # next to the S&P 500's worst fall over the same days. Episode replays below use each episode's S&P dates instead.
    def worst_fall(r):
        wlt = (1 + r.fillna(0)).cumprod()
        dd = wlt / wlt.cummax() - 1
        tr = dd.idxmin(); pk = wlt.loc[:tr].idxmax()
        after = wlt.loc[tr:]; rec = after[after >= wlt.loc[pk]].index
        return {'max_drawdown': float(dd.min()), 'peak': str(pk.date()), 'trough': str(tr.date()),
                'recovered': (str(rec[0].date()) if len(rec) else None)}
    _dr = path.daily_return.dropna()
    out['worst_fall'] = {'sleeve': worst_fall(_dr), 'spy_same_days': worst_fall(spy.reindex(_dr.index)),
                         'window': f"{_dr.index[0].date()}..{_dr.index[-1].date()}"}
    # A1 loop-4: the B2 Ledoit-Wolf summary is kept only as a documented diagnostic (its shrinkage pins at 1.0, so its
    # vol and effective-bets figures are degenerate). The published risk numbers come from 'risk_sample_cov' below.
    out['risk_ledoit_wolf_SUPERSEDED'] = dict(b2.risk_summary(w, prices=prices), _status='SUPERSEDED diagnostic: shrinkage hits 1.0; not used anywhere in the report. Use risk_sample_cov.')
    # A1 loop-1 must-fix: B2's Ledoit-Wolf shrinkage pins at 1.0 for these portfolios (fat-tailed days), which makes risk
    # contributions proportional to weight^2. Recompute with the plain sample covariance of 3 years of daily returns
    # (~750 observations for ≤20 names: well-conditioned) and report both, flagging the degenerate one.
    rets = prices[list(w)].pct_change().loc['2023-09-25':'2026-09-25'].dropna(how='any')
    cov = rets.cov().values * 252
    wv = np.array([w[k] for k in rets.columns])
    port_var = float(wv @ cov @ wv)
    rc = wv * (cov @ wv) / port_var
    spy3 = spy.loc[rets.index]
    te = float(((rets.values @ wv) - spy3.values).std(ddof=1) * np.sqrt(252))     # sample std, same convention as the covariance
    # Loop-2 (A2): a risk read that is not just a restatement of the weights. One-factor (S&P 500) decomposition: each holding's
    # beta and residual; the sleeve's variance splits into market-driven and stock-specific parts, and the stock-specific part
    # is attributed by name from the residual covariance. Also: effective number of bets by weight and by (sample-cov) risk.
    m = spy3.values; mv = float(np.var(m, ddof=1))
    betas = np.array([float(np.cov(rets[c].values, m, ddof=1)[0, 1] / mv) for c in rets.columns])
    resid = rets.values - np.outer(m, betas) - (rets.values.mean(axis=0) - betas * m.mean())
    E = np.cov(resid, rowvar=False, ddof=1) * 252
    beta_p = float(wv @ betas)
    sys_var = beta_p ** 2 * mv * 252
    spec_var = float(wv @ E @ wv)
    spec_rc = wv * (E @ wv) / spec_var
    out['risk_sample_cov'] = {'window': f"{rets.index[0].date()}..{rets.index[-1].date()}", 'n_days': int(len(rets)), 'vol_annual': port_var ** 0.5,
                              'tracking_error_annual': te, 'avg_pairwise_corr': float(np.nanmean(np.corrcoef(rets.values.T)[np.triu_indices(len(wv), 1)])),
                              'risk_contribution_pct_by_name': {k: float(v) for k, v in zip(rets.columns, rc)},
                              'risk_to_weight_ratio': {k: float(v / wt) for k, v, wt in zip(rets.columns, rc, wv)},
                              'enb_weight': float(1 / np.sum(wv ** 2)), 'enb_risk': float(1 / np.sum(rc ** 2)),
                              'beta_3y': beta_p, 'beta_by_name': {k: float(b) for k, b in zip(rets.columns, betas)},
                              'systematic_share_of_variance': float(sys_var / port_var), 'specific_share_of_variance': float(spec_var / port_var),
                              'specific_contribution_pct_by_name': {k: float(v) for k, v in zip(rets.columns, spec_rc)},
                              'note': 'Sample covariance (no shrinkage). B2 Ledoit-Wolf version degenerates to weight-squared shares when shrinkage hits 1.0. '
                                      'One-factor split: market part = (portfolio beta)^2 x S&P variance; stock-specific part from the residual covariance '
                                      '(the two need not sum exactly to 1 because residuals are estimated, not orthogonalised by construction).'}
    # ---- stress replays: sleeve, SPY, and each model allocation (daily, buy-and-hold from window start) ----
    cash_d = (1 + CASH) ** (1 / 252) - 1

    def mix_replay(parts, weights):
        """Quarterly-rebalanced mix, matching the stated operating rule: buy-and-hold within each calendar quarter,
        reset to the target weights at each quarter end. Returns (end-to-end return, worst point inside the window).
        (Loop-2 fix: the Loop-1 replay rebalanced daily, which overstates losses in a long, trending crash.)"""
        idx = parts[0].index
        qs = pd.Series(idx.to_period('Q'), index=idx)
        level, segs = 1.0, []
        for _, g in qs.groupby(qs):
            comp = [(1 + p.loc[g.index]).cumprod() for p in parts]
            val = sum(wt * cp for wt, cp in zip(weights, comp))
            segs.append(level * val); level = level * float(val.iloc[-1])
        pth = pd.concat(segs).values
        peak = np.maximum.accumulate(np.r_[1.0, pth])[1:]
        return float(pth[-1] - 1), float((pth / peak - 1).min())

    rows = []
    for name, a, b in EPISODES:
        s = sr.loc[a:b].iloc[1:]; m = spy.loc[a:b].iloc[1:]
        miss = float(path.missing_share.loc[a:b].mean()) if len(path.missing_share.loc[a:b]) else None
        row = {'episode': name, 'dates': f'{a} → {b}', 'sleeve': float((1 + s.fillna(0)).prod() - 1), 'spy': float((1 + m).prod() - 1),
               'sleeve_real_data_share': (1 - miss) if miss is not None else None,
               'no_price_tickers': [t for t in w if t in prices.columns and (prices[t].first_valid_index() is None or prices[t].first_valid_index() > pd.Timestamp(a))]}
        cash_s = pd.Series(cash_d, index=m.index)
        for mn, (c, sl, rv) in MODELS.items():
            end, worst = mix_replay([m, s.fillna(m), cash_s], [c, sl, rv])   # names without history in the window: SPY stand-in, disclosed
            row[mn] = end; row[mn + ' | worst point'] = worst
        rows.append(row)
    out['stress'] = rows
    # ---- how much equity (index:stocks held at the Moderate mix's 55:15 proportions) keeps each crisis inside a loss limit?
    lim = {}
    for name, a, b in EPISODES:
        s = sr.loc[a:b].iloc[1:].fillna(spy.loc[a:b].iloc[1:]); m = spy.loc[a:b].iloc[1:]; cash_s = pd.Series(cash_d, index=m.index)
        best = {}
        for limit in (0.15, 0.20):
            ok = [e / 100 for e in range(0, 101) if mix_replay([m, s, cash_s], [e / 100 * 55 / 70, e / 100 * 15 / 70, 1 - e / 100])[1] >= -limit]
            best[f'max_equity_share_within_{int(limit * 100)}pct'] = max(ok) if ok else 0.0
        lim[name] = best
    out['equity_share_limits'] = lim
    # ---- scenario simulations: sleeve vs SPY (alpha = 0) and model allocations ----
    sims = []
    for sc, g in SCEN.items():
        so = b2.simulate_outcomes(w, drift_annual=g, horizons=[1, 3, 5, 10], benchmark_returns=spy, benchmark_drift_annual=g,
                                  missing='exclude', prices=prices, n=20000, seed=7)
        sims.append({'mix': 'Stock sleeve alone', 'scenario': sc, 'result': so})
        hist = pd.concat([spy.rename('spy'), sr.rename('sl')], axis=1).dropna()
        for mn, (c, sl, rv) in MODELS.items():
            eq_share = c + sl
            eq_r = (c * hist.spy + sl * hist.sl) / eq_share
            eq_r = b2.recentre_to_geometric_drift(eq_r, g)
            res = b2.allocation_scenarios(eq_r, reserve_yield=CASH, mixes=[eq_share], horizons=[1, 3, 5, 10], n=20000, seed=7)
            sims.append({'mix': mn, 'scenario': sc, 'result': list(res.values())[0]})
    out['sims'] = sims
    # ---- calibration check: how sensitive are the allocation odds to the bootstrap's mean block length? (base case)
    sens = []
    hist = pd.concat([spy.rename('spy'), sr.rename('sl')], axis=1).dropna()
    for mn, (c, sl, rv) in MODELS.items():
        eq_share = c + sl
        eq_r = b2.recentre_to_geometric_drift((c * hist.spy + sl * hist.sl) / eq_share, SCEN['Base'])
        for mb in (5, 21, 63):
            res = list(b2.allocation_scenarios(eq_r, reserve_yield=CASH, mixes=[eq_share], horizons=[5, 10], n=20000,
                                               mean_block=mb, seed=7).values())[0]['horizons']
            sens.append({'mix': mn, 'mean_block_days': mb, 'p_gain_5y': res['5y']['p_total_return_gt_0'],
                         'p_gain_10y': res['10y']['p_total_return_gt_0'], 'p_dd20_5y': res['5y']['p_drawdown_worse_than']['-20%']})
    out['block_sensitivity_base'] = sens
    out['sim_settings'] = {'method': 'stationary bootstrap (Politis-Romano), geometric blocks', 'mean_block_days': 21, 'paths': 20000,
                           'seed': 7, 'source_window': '2005-01-03..2026-09-25 daily', 'scenario_drifts': SCEN, 'tbill_yield': CASH}
    (V4 / 'outputs' / 'lead_risk_results.json').write_text(json.dumps(clean(out)), encoding='utf-8')
    # compact console summary
    print('sleeve history', {k: ps[k] for k in ('start', 'end', 'cagr', 'max_drawdown', 'missing_weight_share_mean')})
    for r in rows: print(r['episode'], 'sleeve %.1f%% SPY %.1f%% moderate %.1f%%' % (100 * r['sleeve'], 100 * r['spy'], 100 * r['Moderate (55/15/30)']))
    for s in sims:
        if s['scenario'] != 'Base': continue
        h = s['result']['horizons']
        print(s['mix'], {hz: (round(h[hz]['p_total_return_gt_0'], 3), round(h[hz]['p_drawdown_worse_than']['-20%'], 3),
                              round(h[hz].get('p_beat_benchmark', float('nan')) if isinstance(h[hz].get('p_beat_benchmark'), float) else -1, 3)) for hz in h})


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
