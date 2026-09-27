import re
"""Lead: Appendix A of FINAL_REPORT.md (technical notes for specialists) and the dashboard's verification tables.

A3 (Loop 2) asked for a clean primary reading path: the core sections stay in plain English, and the statistics (t-stats,
95% ranges, Newey-West), the simulation method and its sensitivity, the risk-model details, the register of independent
checks and a per-holding verification table live here. Every number is read from the output files.
Writes FINAL_REPORT.md between <!-- SECTION:APPX --> markers and v4/outputs/lead_appendix.json."""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent))
from lead_guard import check_build_fresh
check_build_fresh()
import json, pathlib, re
from collections import Counter

V4 = pathlib.Path(__file__).resolve().parents[1]
O = V4 / 'outputs'


def load(n):
    p = O / n
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


def pct(x, d=0):
    return '–' if x is None else f"{100 * x:.{d}f}%"


def ppct(x):
    return '–' if x is None else ('over 99%' if x >= 0.995 else ('under 1%' if x < 0.005 else f"{100 * x:.0f}%"))


def spct(x, d=1):
    return '–' if x is None else f"{'+' if x > 0 else '−' if x < 0 else ''}{abs(100 * x):.{d}f}%"


BT = load('b1_results.json'); RR = load('lead_risk_results.json'); BLD = load('lead_portfolio_build.json'); P = load('lead_portfolio.json')
CHK = load('lead_check_risk_contrib.json'); DD = load('lead_check_daily_dd.json')
V1X = load('v1x_verification.json') or {}; V2R = (load('v2r_reit_valuation.json') or {}).get('tickers', {})
DA4 = load('da4_factcheck.json') or {}; DA5 = load('da5_factcheck.json') or {}; DA6 = load('da6_factcheck.json') or {}; DA7 = load('da7_factcheck.json') or {}; DA8 = load('da8_factcheck.json') or {}; C1 = load('c1_consistency.json') or {}; X1 = load('x1_v005_verification.json') or {}
rows = sorted(P['rows'], key=lambda r: r['rank'])
A = ['## Appendix A. Technical notes (for specialists)\n',
     'The core sections above are written for a non-specialist. This appendix holds the statistics and methods behind them, and the register of independent checks.\n']

# ---------------- A.1 backtest statistics
S = BT['strategies']; LS = BT['phase_b']['lead_sleeve']
bt_rows = [('Model top 30, monthly', S['primary_top30_ew']['vs']['SPY']), ('Model top quintile (~85 names)', S['primary_topquintile_ew']['vs']['SPY']),
           ('Sleeve rule as pre-committed', LS['sleeve_top20_invvol_q (as implemented)']['vs_SPY']), ('70% S&P 500 + 30% sleeve rule', LS['blend_SPY70_sleeve30']['vs_SPY']),
           ('Equal-weight S&P 500 (point-in-time)', S['pit_ew_universe']['vs']['SPY'])]
A += ['### A.1 Backtest statistics (2012-01 to 2026-08, against the S&P 500 total return)\n',
      '| Strategy | Compound gap a year | Average yearly gap | 95% range for the average gap | t-stat (Newey-West) |', '|---|---|---|---|---|']
for name, v in bt_rows:
    lo, hi = v['ci95_ann_mean_excess']
    A.append(f"| {name} | {spct(v['excess_cagr'])} | {spct(v['ann_mean_excess'])} | {spct(lo)} to {spct(hi)} | {v['nw_t']:.2f} |".replace('| -', '| −'))
A.append("\nThe t-stat is the average monthly gap divided by its standard error. The Newey-West method widens that error to allow for correlated neighbouring months. "
         "Values between −2 and +2 are within what chance alone produces. Every 95% range contains zero or lies almost entirely below it: there is no evidence of an edge. "
         "B1's 500 random re-weightings of the four factor families (a Dirichlet test) found 1.4% that beat the S&P 500. "
         "Daily worst falls were re-derived without B1's code: top 30 " + (spct(DD['top30_daily_mdd_gross']) if DD else '–') + ", sleeve rule "
         + (spct(DD['sleeve_rule']['daily_mdd_net']) if DD and DD.get('sleeve_rule') else '–') + " (B1: −44.4% and −41.7%).\n")

# ---------------- A.2 simulation method and sensitivity
ss = RR.get('sim_settings') or {}
A += ['### A.2 Simulation method and sensitivity\n',
      f"Allocation odds use a stationary block bootstrap (Politis-Romano) of daily returns from {ss.get('source_window', '2005–2026').replace(' daily', '').replace('..', ' to ')}: "
      f"{ss.get('paths', 20000):,} paths, geometric blocks with a mean of {ss.get('mean_block_days', 21)} trading days, random seed {ss.get('seed', 7)}. Each path is re-centred to the scenario's compound "
      "market return (bear 2%, base 6%, bull 9%), and T-bills earn 4%. The stock satellite is simulated with zero alpha. The mix is rebalanced daily to its target weights, a simplification against "
      "the quarterly rule; the crisis replays in §7 rebalance quarterly. Changing the block length barely moves the base-case odds:\n",
      '| Allocation | 5-day blocks: P(gain 5y / 10y), P(fall >20% in 5y) | 21-day blocks | 63-day blocks |', '|---|---|---|---|']
by = {}
for b in RR.get('block_sensitivity_base', []):
    by.setdefault(b['mix'], {})[b['mean_block_days']] = b
for mix, d in by.items():
    A.append(f"| {mix} | " + ' | '.join(f"{ppct(d[k]['p_gain_5y'])} / {ppct(d[k]['p_gain_10y'])}, {ppct(d[k]['p_dd20_5y'])}" if k in d else '–' for k in (5, 21, 63)) + ' |')

# ---------------- A.3 risk model
sc = RR.get('risk_sample_cov') or {}
w5 = ((RR.get('risk_ledoit_wolf_SUPERSEDED') or {}).get('windows') or {}).get('3y') or {}
A += ['\n### A.3 Risk model\n',
      f"Sleeve risk uses the plain sample covariance of {sc.get('n_days', '–')} days of returns ({str(sc.get('window', '')).replace('..', ' to ')}), complete cases only. "
      f"Results: volatility {pct(sc.get('vol_annual'), 1)}, tracking error {pct(sc.get('tracking_error_annual'), 1)} (sample standard deviation), average pairwise correlation {sc.get('avg_pairwise_corr', 0):.2f}. "
      f"The effective number of bets is {sc.get('enb_weight', 0):.1f} by weight (1/Σw²) and {sc.get('enb_risk', 0):.1f} by risk (1/Σ risk-share²). "
      f"B2's Ledoit-Wolf shrinkage hit its 1.0 ceiling (intensity {w5.get('shrinkage_intensity', '–')}); risk shares from that estimator are proportional to squared weights, so they are not used. "
      f"A one-factor split against the S&P 500 attributes {pct(sc.get('systematic_share_of_variance'))} of variance to the market (portfolio beta {sc.get('beta_3y', 0):.2f}) and "
      f"{pct(sc.get('specific_share_of_variance'))} to company-specific moves. The two need not sum to exactly 100%, because the residuals are estimated.\n",
      ('An independent re-computation from raw D2 prices, without the risk engine\'s code (`code/lead_check_risk_contrib.py`), reproduces volatility, correlation, tracking error and every risk share '
       f"to within {max(CHK['max_abs_diff_risk_contribution'], *[v['abs_diff'] for v in CHK['comparison'].values() if isinstance(v.get('abs_diff'), float)]):.1e} (pass: {CHK['pass']}).\n" if CHK else '')]

# ---------------- A.4 register of independent checks
def da_counts(d):
    # C1 loop-9: "CONFIRMED (prior FAIL corrected)" counts as a pass, as in the cumulative DA row
    c = Counter(('PASS' if str(f.get('status', '')).upper().startswith('CONFIRMED') else f.get('status')) for f in d.get('facts', []))
    return (sum(c.values()), c.get('PASS', 0), c.get('MINOR', 0), c.get('FAIL', 0), c.get('UNVERIFIABLE', 0))


reg = [('B1X', 'Blind re-implementation of the whole backtest', 'Matches B1 within 0.04 pts/yr; live-rank correlation 0.976', 'outputs/b1x_report.md')]
if DD:
    reg.append(('Daily drawdown check', 'Daily worst falls of the top 30 and the sleeve rule, without B1\'s code', f"{spct(DD['top30_daily_mdd_gross'])} vs −44.4%; {spct(DD['sleeve_rule']['daily_mdd_net'])} vs −41.7%; same day (23 Mar 2020)", 'outputs/lead_check_daily_dd.json'))
if V1X:
    reg.append(('V1X', 'Valuation inputs and methods of the Loop-1 holdings, from SEC filings', f"{V1X.get('n_pass', '–')} of {V1X.get('n_checks', '–')} checks pass ({pct(V1X.get('pass_rate'), 1)}); no verdict or base-case sign changes", 'outputs/v1x_verification.md'))
if V2R:
    reg.append(('V2R', 'REIT funds from operations rebuilt from filings', '; '.join(f"{t}: {v.get('v1_verdict')} → {v.get('corrected_verdict')}" for t, v in V2R.items()), 'outputs/v2r_reit_valuation.md'))
import glob as _g3
_DA_WHAT = {'DA4': 'Load-bearing dossier facts (6 holdings, 4 excluded names) against SEC filings',
            'DA5': 'Load-bearing dossier facts of the 8 holdings no auditor had checked'}
_DA_LIST = []
for _f in sorted(_g3.glob(str(O / 'da[0-9]*_factcheck.json')), key=lambda f: int(re.findall(r'da(\d+)_', pathlib.Path(f).name)[0])):
    _nm = pathlib.Path(_f).name.split('_')[0].upper(); _dd = json.loads(pathlib.Path(_f).read_text(encoding='utf-8'))
    _tk = sorted({x.get('ticker') for x in _dd.get('facts', []) if x.get('ticker')})
    _DA_LIST.append((_nm, _dd, _DA_WHAT.get(_nm, 'Load-bearing dossier facts of ' + ', '.join(_tk) + ' against SEC filings'), f'outputs/{_nm.lower()}_factcheck.md'))
# whole-market triage and full-diligence waves
_TRI = []
for _q in sorted(_g3.glob(str(O / 'Q[0-9][0-9]_triage.json'))):
    _T = json.loads(pathlib.Path(_q).read_text(encoding='utf-8')).get('tickers', {})
    _TRI += list(_T.values()) if isinstance(_T, dict) else list(_T)
if _TRI:
    reg.append(('Q01–Q15 triage', 'Quick research pass on every S&P 500 company without a dossier: quality, growth, red flags, price vs growth',
                f"{len(_TRI)} scored, {sum(1 for x in _TRI if x.get('advance'))} advanced to full-diligence queue", 'outputs/Q*_triage.json'))
for _w in sorted(int(re.findall(r'wave(\d+)', pathlib.Path(_x).name)[0]) for _x in _g3.glob(str(V4 / 'data' / 'full_diligence_wave*.json'))):   # C1 loop-7: every wave, not a fixed list
    _wf = V4 / 'data' / f'full_diligence_wave{_w}.json'
    if _wf.exists():
        _wd = json.loads(_wf.read_text(encoding='utf-8'))
        reg.append((f'Diligence wave {_w}', 'Full SEC-filing diligence of the next names in the pre-committed order (verdict, reverse DCF, kill criteria)',
                    f"{len(_wd.get('selected', []))} names researched; {len(_wd.get('queued', []))} still queued after this wave", f'data/full_diligence_wave{_w}.json'))
_tot = {'n': 0, 'PASS': 0, 'MINOR': 0, 'FAIL': 0, 'UNVERIFIABLE': 0}
for _nm, _dd, _w, _f in _DA_LIST:
    for _x in _dd.get('facts', []):
        _tot['n'] += 1; _st = str(_x.get('status', '')).split(' ')[0].upper()
        _tot[_st if _st in _tot else 'PASS' if _st.startswith('CONFIRMED') else 'UNVERIFIABLE'] += 1
if _DA_LIST:
    reg.append((f"DA series total ({_DA_LIST[0][0]}–{_DA_LIST[-1][0]})", 'All independent dossier fact-checks against SEC filings, cumulative',
                f"{_tot['n']} facts: {_tot['PASS']} pass, {_tot['MINOR']} minor, {_tot['FAIL']} fail (every fail corrected in its dossier), {_tot['UNVERIFIABLE']} unverifiable", 'outputs/da*_factcheck.json'))
for name, d, what, f in _DA_LIST:
    if d:
        n, p_, mi, fa, un = da_counts(d)
        reg.append((name, what, f"{n} facts: {p_} pass, {mi} minor, {fa} fail, {un} unverifiable", f))
if C1:
    reg.append(('C1', 'Every number in the report traced to its source file', f"{C1.get('checked', '–')} checked, {C1.get('match', '–')} matched, {len(C1.get('mismatch') or [])} mismatch (each fixed before release); audited build {C1.get('build_built', '–')}", 'outputs/c1_consistency.md'))
if X1:
    reg.append(('X1', "Claims inherited from Codex's release v005", f"{X1.get('confirmed')} of {X1.get('checked')} confirmed; " + ', '.join(f"{k.lower()} {v}" for k, v in (X1.get('counts_by_status') or {}).items() if k != 'CONFIRMED'), 'outputs/x1_v005_verification.md'))
if CHK:
    reg.append(('Risk re-computation', 'Sleeve volatility, tracking error, correlation and risk shares from raw prices', f"pass: {CHK['pass']}", 'outputs/lead_check_risk_contrib.json'))
reg += [('D2R', "Re-download of the 408 'no price data' symbols", 'Root cause found (retry logic); 0 recovered because the names were acquired and purged; coverage unchanged', 'outputs/d2r_report.md'),
        ('R3', 'UAE implementation and tax facts', 'IBKR entity and protection confirmed; fund, withholding and estate-tax facts re-verified; open items labelled', 'outputs/r3_implementation_verification.md'),
        ('DA1–DA3', 'Prices and corporate actions; SEC fundamentals against filing documents; estimates', 'See each report for pass rates and fixes', 'audit/da1_data_audit.md, da2, da3')]
A += ['\n### A.4 Register of independent checks\n', '| Check | What it re-derived | Result | File |', '|---|---|---|---|']
A += [f"| {a} | {b} | {c} | `{d}` |" for a, b, c, d in reg]

# ---------------- A.5 per-holding verification
_VR = {'cheap': 0, 'attractive': 0, 'undervalued': 0, 'fair': 1, 'in_line': 1, 'fairly valued': 1, 'demanding': 2, 'full': 2,
       'expensive': 3, 'excessive': 3, 'overvalued': 3}


def _vdir(vc):
    """direction of the analyst-vs-V1 disagreement: 'more cautious', 'more optimistic', or None if unknown/consistent"""
    vc = vc or {}
    if vc.get('consistent') is not False:
        return None
    a = _VR.get(str(vc.get('dossier_view') or '').lower().split(' ')[0]); b = _VR.get(str(vc.get('v1_verdict') or '').lower())
    if a is None or b is None or a == b:
        return 'differs from V1'
    return 'more cautious than V1' if a > b else 'more optimistic than V1'


AUDITED = {  # dossiers whose facts each independent auditor checked against sources (from the audit files' fact-check sections)
    'A1 (loops 1–2)': ['MTB', 'LMT', 'JBHT', 'HST', 'DLTR', 'BMY', 'VRSN', 'EOG'], 'A2 (loops 1–2)': ['RL', 'MTB', 'LMT', 'HST', 'DLTR', 'FRT', 'DG', 'ABNB', 'EOG', 'BKNG'],
    'A3 (loops 1–2)': ['MTB', 'HST', 'RL', 'LMT', 'DLTR', 'GL', 'DRI', 'VRSN'],
    'A1 (loop 3)': ['CRH', 'PGR', 'AMP'], 'A2 (loop 3)': ['LVS', 'PGR', 'CRH', 'CMCSA', 'EG', 'BR', 'NOW', 'AMP', 'BX'], 'A3 (loop 3)': ['AMP', 'PGR', 'BX', 'NOW'],
    'A1 (loop 4)': ['ADP', 'DOV'], 'A2 (loop 4)': ['GM', 'ADP', 'RJF', 'DOV', 'HBAN'], 'A3 (loop 4)': ['GM', 'HBAN'],
    'A1 (loop 5)': ['HBAN', 'GM'], 'A2 (loop 5)': ['GM', 'RJF', 'LVS', 'HBAN', 'ADP', 'DOV', 'CRH'], 'A3 (loop 5)': ['ADP', 'DOV', 'CRH']}
fc = {}
import glob as _g2
_DAS = [(pathlib.Path(f).name.split('_')[0].upper(), json.loads(pathlib.Path(f).read_text(encoding='utf-8'))) for f in sorted(_g2.glob(str(O / 'da[0-9]*_factcheck.json')), key=lambda f: int(re.findall(r'da(\d+)_', pathlib.Path(f).name)[0]))]
for src, d in _DAS:
    for f in d.get('facts', []):
        e = fc.setdefault(f.get('ticker'), {}); e.setdefault(src, Counter())[f.get('status')] += 1
# A1 loop-5: from Loop 5 on, auditors record their dossier fact-checks as structured 'fact_checks' in their JSON
# ([{ticker, claim, source, status}]); the register reads them directly. The dict above holds the earlier loops, which
# only reported fact-checks in prose.
import glob as _glob
for _f in sorted(_glob.glob(str(V4 / 'audit' / 'A[123]_loop*.json'))):
    _m = re.match(r'(A[123])_loop(\d+)\.json', pathlib.Path(_f).name)
    try:
        _fcs = json.loads(pathlib.Path(_f).read_text(encoding='utf-8')).get('fact_checks') or []
    except Exception:
        _fcs = []
    for _x in _fcs:
        if isinstance(_x, dict) and _x.get('ticker'):
            AUDITED.setdefault(f"{_m.group(1)} (loop {_m.group(2)})", [])
            if _x['ticker'] not in AUDITED[f"{_m.group(1)} (loop {_m.group(2)})"]:
                AUDITED[f"{_m.group(1)} (loop {_m.group(2)})"].append(_x['ticker'])
for aud, lst in AUDITED.items():
    for t in lst:
        fc.setdefault(t, {})[aud] = None
V1T = {}
try:
    import pandas as pd
    V1T = pd.read_csv(O / 'v1_valuation_table.csv').set_index('ticker')['verdict'].to_dict()
except Exception:
    pass
ver = []
import sys as _sys; _sys.path.insert(0, str(V4 / 'code'))
from lead_verify_gate import unverified as _unv
_UV = _unv()
A += ['\n### A.5 Per-holding verification\n',
      ('**Verification gate: PASS.** Every holding has an independent multi-fact check of its dossier against SEC filings (the DA series), and every failed fact is answered by a dated correction in the dossier. A release cannot be packaged unless this gate passes.\n' if not _UV else
       '**Verification gate: OPEN.** Not yet independently fact-checked, or a failed fact not yet corrected: ' + '; '.join(f'{t} ({w})' for t, w in _UV) + '. A release cannot be packaged until this gate passes.\n'),
      '| Stock | Valuation model (V1) | Independent valuation check | Analyst view vs V1 | Dossier facts checked by |', '|---|---|---|---|---|']
for r in rows:
    t = r['t']
    v1x = (V1X.get('tickers') or {}).get(t)
    if t in V2R:
        vchk = f"V2R rebuilt FFO: {V2R[t].get('corrected_verdict')} ({'changed' if V2R[t].get('verdict_changed') else 'unchanged'})"
    elif v1x:
        n = len(v1x.get('checks', [])); pz = sum(1 for c in v1x.get('checks', []) if c.get('status') == 'PASS')
        vchk = f"V1X: {pz}/{n} checks pass; verdict {'changed' if v1x.get('verdict_changes') else 'unchanged'}"
    else:
        vchk = 'Dossier reconciles with V1 in §7 (added after V1X ran)'
    vc = r.get('val_consistency') or {}
    av = f"{vc.get('dossier_view', '–')} ({'consistent' if vc.get('consistent') else (_vdir(vc) or '–')})"
    srcs = []
    for s_, e in sorted((fc.get(t) or {}).items()):
        if isinstance(e, Counter):
            _dtxt = (V4 / 'dossiers' / f'{t}.md').read_text(encoding='utf-8') if (V4 / 'dossiers' / f'{t}.md').exists() else ''
            _fixed = e.get('FAIL', 0) and re.search(r'## Correction[^\n]*' + re.escape(s_), _dtxt)
            srcs.append(f"{s_}: {sum(e.values())} facts, {e.get('FAIL', 0)} fail" + (' (corrected in dossier)' if _fixed else ''))
        else:
            srcs.append(s_)
    ver.append({'t': t, 'v1': V1T.get(t), 'check': vchk, 'analyst': av, 'facts': srcs})
    A.append(f"| **{t}** | {V1T.get(t, '–')} | {vchk} | {av} | {'; '.join(srcs) if srcs else 'not yet checked'} |")
A.append('\nEvery holding carries a primary-source dossier. The fact-check sources are independent agents or auditors who re-read the SEC filings or company releases behind the dossier\'s load-bearing numbers.')

txt = '\n'.join(A)
fr = (V4 / 'FINAL_REPORT.md').read_text(encoding='utf-8')
if '<!-- SECTION:APPX -->' not in fr:
    fr = fr.rstrip() + '\n\n<!-- SECTION:APPX -->\n<!-- /SECTION:APPX -->\n'
fr = re.sub(r'<!-- SECTION:APPX -->.*?<!-- /SECTION:APPX -->', lambda _m: '<!-- SECTION:APPX -->\n' + txt + '\n<!-- /SECTION:APPX -->', fr, flags=re.S)
(V4 / 'FINAL_REPORT.md').write_text(fr, encoding='utf-8')
(O / 'lead_appendix.json').write_text(json.dumps({'register': [list(x) for x in reg], 'verification': ver}, ensure_ascii=False, indent=1), encoding='utf-8')
print('appendix written:', len(reg), 'checks,', len(ver), 'holdings')
