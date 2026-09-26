"""Lead: build dashboard view JSONs (evidence, risk, ranking, portfolio) from agent outputs. Re-run after any update."""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent))
from lead_guard import check_build_fresh
check_build_fresh()  # stops with StaleBuildError if any input changed after the portfolio build
import json, pathlib, math
import numpy as np, pandas as pd

V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
O = V4 / 'outputs'


def clean(x):
    if isinstance(x, dict): return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [clean(v) for v in x]
    if isinstance(x, (float, np.floating)): return None if (x != x or math.isinf(x)) else round(float(x), 5)
    if isinstance(x, (np.integer,)): return int(x)
    if isinstance(x, (np.bool_,)): return bool(x)
    return x


def w(name, obj):
    (O / name).write_text(json.dumps(clean(obj), ensure_ascii=False), encoding='utf-8')


# ------------------------------------------------------------------ evidence (B1)
R = json.loads((O / 'b1_results.json').read_text(encoding='utf-8'))
M = pd.read_parquet(V4 / 'data' / 'b1_strategy_returns_monthly.parquet')
cols = [('primary_top30_ew_net', 'Model top 30', 'var(--gold)', 2.4), ('pit_ew_universe_net', 'Equal-weight S&P 500 (point-in-time)', 'var(--blue)', 1.6),
        ('bench_SPY', 'S&P 500 (SPY, total return)', 'var(--ink)', 2.4), ('primary_topquintile_ew_net', 'Model top quintile', 'var(--amber)', 1.4)]
eq = {}
x = [str(d.date()) for d in M.index]
lines = []
for c, name, color, width in cols:
    if c in M.columns:
        v = (1 + M[c].fillna(0)).cumprod()
        lines.append({'name': name, 'v': [round(float(t), 4) for t in v], 'c': color, 'w': width})
S = R['strategies']


def srow(key, label):
    s = S.get(key, {}); net = s.get('net', s); vs = s.get('vs', {}).get('SPY', s.get('vs_SPY', {})); ve = s.get('vs', {}).get('PIT_EW', s.get('vs_PIT_EW', {}))
    r36 = vs.get('rolling_36m', vs.get('roll36_pos'))
    if isinstance(r36, dict): r36 = r36.get('share_positive', r36.get('pos_share', r36.get('p_pos')))
    return {'name': label, 'cagr': net.get('cagr'), 'vol': net.get('vol'), 'sharpe': net.get('sharpe'), 'mdd': net.get('mdd_monthly'),
            'exc_ew': ve.get('excess_cagr'), 'exc_spy': vs.get('excess_cagr'), 't': vs.get('nw_t'), 'hit36': r36}


stats = [srow('primary_top30_ew', 'Model top 30 (monthly, net of costs)'), srow('primary_topquintile_ew', 'Model top quintile'),
         srow('primary_bottomquintile_ew', 'Model bottom quintile'), srow('pit_ew_universe', 'Equal-weight S&P 500 (point-in-time)')]
spy = S.get('bench_SPY', {})
stats.append({'name': 'S&P 500 (SPY total return)', 'cagr': spy.get('net', spy).get('cagr'), 'vol': spy.get('net', spy).get('vol'), 'sharpe': spy.get('net', spy).get('sharpe'), 'mdd': spy.get('net', spy).get('mdd_monthly')})
PB = R.get('phase_b', {})
lead_sleeve = PB.get('lead_sleeve', {})
for k, lab in [('sleeve_top20_invvol_q (as implemented)', 'Sleeve rule as pre-committed (top 20, vol ≤45%, inverse-vol, quarterly)'),
               ('blend_SPY70_sleeve30', '70% S&P 500 + 30% sleeve rule')]:
    s = lead_sleeve.get(k)
    if s:
        vs = s.get('vs_SPY', {}); ve = s.get('vs_PIT_EW', {})
        stats.append({'name': lab, 'cagr': s.get('cagr'), 'vol': s.get('vol'), 'sharpe': s.get('sharpe'), 'mdd': s.get('mdd_monthly'),
                      'exc_ew': ve.get('excess_cagr'), 'exc_spy': vs.get('excess_cagr'), 't': vs.get('nw_t'), 'hit36': vs.get('roll36_pos')})
dec = [(int(r.get('decile', i + 1)), r.get('mean_fwd12') if r.get('mean_fwd12') is not None else r.get('mean_fwd12m_tr')) for i, r in enumerate(R['decile_table']['rows'])]
cal = []
for r in R['calibration_by_decile']:
    cal.append({'d': int(r.get('decile')), 'n': r.get('n'), 'p_pos': r.get('p_fwd12_pos'), 'p_beat': r.get('p_excess_pos'), 'med': r.get('median_fwd12'),
                'p10': r.get('p10_fwd12'), 'p90': r.get('p90_fwd12'), 'p_dd20': r.get('p_maxdd_worse_20')})
legacy = []
vt = {v['strategy']: v for v in PB.get('variants_table', [])}
for key, lab, verdict in [('legacy v1 weights top-30 monthly', 'v1 model (low-volatility tilt)', 'lagged'),
                          ('legacy v2 weights top-30 monthly', 'v2 model (momentum + value)', 'lagged'),
                          ('legacy v3 conviction-filter proxy, annual (late-Sep)', 'v3 conviction filter (annual)', 'lagged'),
                          ('family M alone top-30', 'Momentum alone (for reference)', 'not significant (t 0.6)'),
                          ('low-volatility quintile (1y daily vol)', 'Low-volatility quintile', 'lagged')]:
    v = vt.get(key)
    if v: legacy.append({'name': lab, 'cagr': v['cagr'], 'exc_ew': v['ex_ew'], 'exc_spy': v['ex_spy'], 'verdict': f"{verdict}; t = {v['t_spy']:.2f} vs S&P"})
bias = []
B = PB.get('bias', {})
if B:
    p = B.get('primary_top30', {}); bias.append(['v4 model top 30 (2012–26)', p.get('today_cagr'), p.get('pit_cagr')])
    m = B.get('momentum_top50_gross 2016-10..2026-08 (lead v3-audit window)', {}); bias.append(['Momentum top 50 (v3\'s 10-year test window)', m.get('today_cagr'), m.get('pit_cagr')])
    e = B.get('ew_universe', {}); bias.append(['Equal-weight universe', e.get('today_cagr'), e.get('pit_cagr')])
years = [[r['year'], r.get('top30'), r.get('PIT_EW') if r.get('PIT_EW') is not None else r.get('pit_ew'), r.get('SPY') if r.get('SPY') is not None else r.get('spy')]
         for r in PB.get('walk_forward', {}).get('years', [])]
_t30 = R['strategies']['primary_top30_ew']; _vs30 = _t30['vs']['SPY']; _bp = (PB.get('bias', {}) or {}).get('primary_top30', {}) or {}
lede = ('We froze a model built only from well-replicated research (quality, value, momentum, earnings surprise) before running any test, '
        'then tested it month by month from 2012 to August 2026 on the stocks that were actually in the S&P 500 at each date, '
        'with as-filed SEC data and trading costs. A second agent rebuilt it independently and matched it within 0.04 points a year. '
        f"<b>It did not beat the S&P 500</b>: the top 30 returned {100 * _t30['net']['cagr']:.1f}% a year against {100 * _vs30['cagr_benchmark']:.1f}% for the index "
        f"(t = {_vs30['nw_t']:.2f}), and a higher score did not mean a higher return. "
        'Every variant told the same story, including the v1, v2 and v3 models.'
        + (f" Tested the way v3 was tested (on today's survivors), the same model shows {100 * _bp['today_cagr']:.1f}% a year instead of {100 * _bp['pit_cagr']:.1f}%: "
           f"a {100 * (_bp['today_cagr'] - _bp['pit_cagr']):.1f}-point illusion." if _bp.get('today_cagr') is not None and _bp.get('pit_cagr') is not None else ''))
w('lead_bt_view.json', {'lede': lede, 'x': x, 'lines': lines, 'stats': stats, 'deciles': dec, 'calib': cal, 'legacy': legacy, 'bias': bias, 'years': years,
                       'notes': 'Point-in-time S&P 500 membership (D1/D2), total-return prices (D2), as-filed SEC XBRL fundamentals filed before each month-end (D3); 10 bps per trade; '
                                'Newey–West t-statistics. Residual survivorship (delisted names without free price data) flatters every strategy by about 0.9% a year versus the real equal-weight ETF (RSP); '
                                'it cannot turn the negative result positive. Full detail: v4/outputs/b1_report.md, independent replication v4/outputs/b1x_report.md.'})
print('bt view ok', len(lines), 'lines', len(stats), 'stats')


# ------------------------------------------------------------------ portfolio, risk, ranking (after lead_build_portfolio.py + lead_risk.py)
def load(name):
    p = O / name
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


B = load('lead_portfolio_build.json')
DOS = {}
for p in (V4 / 'dossiers').glob('*.md'):
    DOS[p.stem.upper()] = p.read_text(encoding='utf-8', errors='ignore')


def dossier_bits(t):
    """thesis line + kill criteria from the diligence JSON summaries (or dossier text as fallback)."""
    import glob, os, re as _re
    files = glob.glob(str(O / 'f*_summary.json')) + glob.glob(r'C:\Users\user\eqv4\cache\f*\*\summary.json')
    for f in sorted(files, key=os.path.getmtime, reverse=True):     # newest first: a later re-assessment wins
        try:
            d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
        except Exception:
            continue
        cands = []
        if isinstance(d, dict):
            for key in ('tickers', 'companies', 'results', 'summaries'):
                if isinstance(d.get(key), dict): cands += list(d[key].items())
            if 'ticker' in d: cands.append((d['ticker'], d))
            cands += [(k, v) for k, v in d.items() if isinstance(v, dict) and 'verdict' in v]
        for k, v in cands:
            if str(k).upper() == t and isinstance(v, dict):
                return {**v, '_mtime': os.path.getmtime(f)}
    return {}


_V1T = pd.read_csv(V4 / 'outputs' / 'v1_valuation_table.csv').set_index('ticker')
_V2R = (load('v2r_reit_valuation.json') or {}).get('tickers', {})
NOTES = (load('lead_holding_notes.json') or {}).get('tickers', {})   # T2 (Loop 2): faithful one-line theses + verbatim kill criteria
import os as _os
NOTES_MTIME = _os.path.getmtime(O / 'lead_holding_notes.json') if (O / 'lead_holding_notes.json').exists() else 0


def kill_from_text(txt):
    import re as _re
    m = _re.search(r'(?:kill criteria|exit triggers?)[^\n]*\n+((?:\s*(?:[-*]|\d+[.)])\s+.+\n?)+)', txt, _re.I)
    if not m:
        return []
    items = _re.split(r'\n\s*(?:[-*]|\d+[.)])\s+', '\n' + m.group(1).strip())
    return [_re.sub(r'\*\*|__', '', x).strip() for x in items if x.strip()]


if B and B.get('weights'):
    tab = B['table']
    rk = sorted(tab, key=lambda r: float(r['rank']))
    rows = []
    for i, r in enumerate(rk):
        t = r['t']; d = dossier_bits(t)
        thesis = ''
        txt = DOS.get(t, '')
        if txt:
            import re as _re
            m = _re.search(r'Verdict[^\n]*\n+(.{40,400}?)(?:\n\n|\n#)', txt, _re.S)
            thesis = _re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''
            thesis = _re.sub(r'\*\*|__', '', thesis)[:260]
        _pe, _pel = r.get('pe'), ('trailing P/E' if r.get('pe_basis') == 'trailing' else None)
        if t in _V2R and (_V2R[t].get('pffo_fy26_guide') or _V2R[t].get('pffo_ttm_now')):   # REITs: FFO rebuilt from filings (V2R)
            _pe = float(_V2R[t].get('pffo_fy26_guide') or _V2R[t]['pffo_ttm_now'])
            _pel = 'P/FFO (2026 guidance)' if _V2R[t].get('pffo_fy26_guide') else 'P/FFO (NAREIT, TTM)'
        elif t in _V1T.index and _V1T.loc[t, 'classification'] == 'reit':          # fallback: V1's proxy, labelled as such
            _pe, _pel = float(_V1T.loc[t, 'metric_value']), 'P/FFO (V1 proxy)'
        nt = NOTES.get(t, {})
        if nt and d and d.get('_mtime', 0) > NOTES_MTIME:     # a diligence re-assessment written after the T2 notes wins
            nt = {}
        thesis = nt.get('thesis_one_line') or d.get('thesis_one_line') or thesis
        kill = nt.get('kill_criteria') or d.get('kill_criteria') or kill_from_text(txt)
        rows.append({'rank': i + 1, 't': t, 'n': r['n'], 's': r['s'], 'sub': r['sub'], 'w': float(r['w']), 'verdict': r['verdict'], 'lane': bool(r.get('lane') == True), 'model_rank': r.get('rank'),
                     'comp': float(r['comp']), 'fam': {'Q': r['Q'], 'V': r['V'], 'M': r['M'], 'S': r['S']}, 'pe': _pe, 'pe_label': _pel,
                     'vol': float(r['vol']), 'p_pos': r.get('p_pos'), 'p_beat': r.get('p_beat'),
                     'bear': r.get('bear'), 'base': r.get('base'), 'bull': r.get('bull'), 'next_er': (d.get('next_earnings_date') or r.get('next_er')),
                     'kill': list(kill)[:5], 'adverse': (d.get('key_adverse_facts') or [])[:3], 'horizon': d.get('horizon'), 'thesis': thesis,
                     'val_consistency': nt.get('valuation_consistency') or d.get('valuation_view_vs_v1')})
    _raw = [x['w'] * 1000 for x in rows]; _fl = [int(v) for v in _raw]; _left = int(round(1000 * sum(x['w'] for x in rows))) - sum(_fl)
    for _k in sorted(range(len(rows)), key=lambda k: -(_raw[k] - _fl[k]))[:max(_left, 0)]:
        _fl[_k] += 1
    for _k, x in enumerate(rows):
        x['w_disp'] = _fl[_k] / 1000   # display weight: rounded to 0.1 point, sums exactly to the invested total
    cons = [[c[0], c[1], c[2], bool(c[3])] for c in B['checks']]
    secw = B.get('sectors', {})
    bench = {'Information Technology': 0.34, 'Financials': 0.13, 'Communication Services': 0.10, 'Consumer Discretionary': 0.10, 'Health Care': 0.09,
             'Industrials': 0.08, 'Consumer Staples': 0.05, 'Energy': 0.03, 'Utilities': 0.025, 'Real Estate': 0.02, 'Materials': 0.02}
    sectors = sorted([[s, float(secw.get(s, 0)), bench.get(s)] for s in set(list(secw) + list(bench))], key=lambda x: -x[1])
    RR = load('lead_risk_results.json') or {}
    risk = RR.get('risk', {})
    w('lead_portfolio.json', {'rows': rows, 'cash': B.get('cash'), 'index_fill': B.get('index_fill'), 'constraints': cons, 'sectors': sectors,
                              'note': 'Weights are shares of the stock sleeve. Sleeve rules were fixed before the diligence verdicts were read: official point-in-time score in the top 70, 1-year volatility ≤ 45%, no pending takeover, valuation attractive or fair versus the company\'s own history, diligence INCLUDE (full) or INCLUDE-SMALL (half), ≤ 2 names per sub-industry, inverse-volatility weights of 3–10% (full conviction) or 1.5–5% (half conviction), sectors ≤ 25%; sleeve capacity the caps cannot absorb is held in the S&P 500 index fund. * Calibrated odds are empirical frequencies for S&P 500 stocks in the same score decile and volatility band, 2011–2025.'})
print('portfolio view', 'yes' if (B and B.get('weights')) else 'pending')


# ------------------------------------------------------------------ ranking of all constituents
Lv = pd.read_csv(V4 / 'data' / 'b1_live_scores.csv')
Sn = pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet').set_index('ticker')
held = set((B or {}).get('weights', {}).keys()) if B else set()
why = {c['t']: c['why'] for c in (B or {}).get('candidates', [])}
rank_rows = []
for _, r in Lv.sort_values('live_rank', na_position='last').iterrows():
    t = r.ticker_yahoo
    status = 'held' if t in held else (why.get(t) or ('pending takeover' if r.exclude_pending_deal else ('outside top 70' if (r.live_rank == r.live_rank and r.live_rank > 70) else ('no composite' if r.composite != r.composite else ''))))
    rank_rows.append({'rk': (int(r.live_rank) if r.live_rank == r.live_rank else None), 't': t, 'n': r['name'], 's': r.gics_sector, 'comp': r.composite,
                      'Q': r.fam_Q, 'V': r.fam_V, 'M': r.fam_M, 'S': r.fam_S, 'pe': (float(Sn.loc[t, 'pe_ntm']) if t in Sn.index and Sn.loc[t, 'pe_ntm'] == Sn.loc[t, 'pe_ntm'] else None),
                      'vol': r.vol_1y, 'gate': status, 'inport': t in held})
w('lead_rank.json', rank_rows)
print('rank rows', len(rank_rows))
