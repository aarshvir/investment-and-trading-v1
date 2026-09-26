"""Lead: select and weight the v4 conviction sleeve with rules fixed BEFORE the diligence verdicts were read
(written 2026-09-26 ~03:00, recorded in STATE.md). Writes the dashboard/report JSON blocks.

Rules
1. Eligible = official B1 live score available (live_rank <= 70), not a pending-deal target, 1-yr daily vol <= 45%,
   V1 valuation verdict in {attractive, fair} (or, if V1 missing, the dossier's own valuation not flagged excessive),
   diligence verdict INCLUDE or INCLUDE-SMALL.
   Amendments after Loop 1 (STATE.md; each removes an internal inconsistency found by the auditors, none uses returns):
   (a) missing V1 valuation = ineligible; (b) negative V1 base case = ineligible; (c) no V1 base case = ineligible;
   (d) half conviction also halves the per-name cap, unfilled capacity goes to the index fund;
   (e) the analyst's reconciled valuation view (dossier / T2 notes) must also be cheap or fair.
   (f) REITs: the FFO-based verdict rebuilt from filings (V2R) replaces V1's net-income-plus-D&A proxy verdict.
2. Diversification: <= 2 names per GICS sub-industry; sector <= 25% of the sleeve.
3. Weights: inverse 1-yr vol x (1.0 INCLUDE, 0.5 INCLUDE-SMALL), bounds 3%..10% for INCLUDE and 1.5%..5% for
   INCLUDE-SMALL (Loop-2 amendment: half conviction = half the cap as well as half the target), sector <= 25%,
   sub-industry <= 12%; constrained least-squares to the target; every constraint verified. Sleeve capacity the caps
   cannot absorb is held in the index core (S&P 500 UCITS fund), not in cash and not forced into other stocks.
4. Rank = composite rank among the selected names (the pre-registered ordering).
"""
import json, glob, re, pathlib, math
import numpy as np, pandas as pd
import sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lead_portfolio import build_weights
import lead_commit_rules as _lcr   # pre-registration firewall: rules must be committed before any build reads diligence output
_RC = _lcr.latest()
if _RC is None or _RC['sha256'] != _lcr.current_hash():
    raise SystemExit('RULES NOT COMMITTED: run python code/lead_commit_rules.py "<reason>" before building (see its docstring).')

V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
L = pd.read_csv(V4 / 'data' / 'b1_live_scores.csv').rename(columns={'ticker_yahoo': 't'})
VAL = pd.read_csv(V4 / 'outputs' / 'v1_valuation_table.csv').set_index('ticker')
S = pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet').set_index('ticker')
CAL = pd.read_csv(V4 / 'outputs' / 'b1_calibration_by_decile_vol.csv')

# ---- diligence summaries (formats vary slightly by agent; parse defensively) ----
DIL = {}
paths = glob.glob(str(V4 / 'outputs' / 'f*_summary.json')) + glob.glob(r'C:\Users\user\eqv4\cache\f*\*\summary.json')
import os
paths = sorted(paths, key=os.path.getmtime)   # oldest first: a later re-assessment (e.g. F16) overrides an earlier verdict
for p in paths:
    try:
        d = json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
    except Exception:
        continue
    items = d.items() if isinstance(d, dict) else []
    if isinstance(d, dict) and 'ticker' in d and 'verdict' in d:
        items = [(d['ticker'], d)]
    for key in ('tickers', 'companies', 'results', 'summaries'):
        if isinstance(d, dict) and key in d and isinstance(d[key], dict):
            items = d[key].items()
        elif isinstance(d, dict) and key in d and isinstance(d[key], list):
            items = [(x.get('ticker'), x) for x in d[key] if isinstance(x, dict)]
    if isinstance(d, list):
        items = [(x.get('ticker'), x) for x in d if isinstance(x, dict)]
    for tk, v in items:
        if not isinstance(v, dict) or 'verdict' not in v:
            continue
        verdict = str(v['verdict']).upper().replace('_', '-').strip()
        verdict = 'INCLUDE-SMALL' if 'SMALL' in verdict else ('INCLUDE' if verdict.startswith('INCLUDE') else ('REJECT' if 'REJECT' in verdict else ('WATCH' if 'WATCH' in verdict else verdict)))
        DIL[str(tk).upper()] = {**v, 'verdict': verdict, '_src': p, '_mtime': os.path.getmtime(p)}

# fallback: verdict stated in the dossier itself (first 'Verdict' section)
for p in glob.glob(str(V4 / 'dossiers' / '*.md')):
    tk = pathlib.Path(p).stem.upper()
    if tk in DIL:
        continue
    txt = pathlib.Path(p).read_text(encoding='utf-8', errors='ignore')
    i = txt.lower().find('verdict')
    m = re.search(r'\b(INCLUDE[-\s]SMALL|INCLUDE|WATCH|REJECT)\b', txt[i:i + 1500] if i >= 0 else '')
    if m:
        vv = m.group(1).upper().replace(' ', '-')
        DIL[tk] = {'verdict': vv, '_src': p + ' (parsed from dossier text)'}

V2R_PATH = V4 / 'outputs' / 'v2r_reit_valuation.json'
V2R = json.loads(V2R_PATH.read_text(encoding='utf-8')).get('tickers', {}) if V2R_PATH.exists() else {}
# analyst's reconciled valuation view per ticker: the most recently written source wins (a diligence summary or the T2
# holding notes), so a later re-assessment (e.g. F16 after the REIT valuation correction) is never masked by older notes
NOTES_PATH = V4 / 'outputs' / 'lead_holding_notes.json'
ANALYST_VIEW, _AV_T = {}, {}
for tk, v in DIL.items():
    vv_ = (v.get('valuation_view_vs_v1') or {}) if isinstance(v.get('valuation_view_vs_v1'), dict) else {}
    if vv_.get('dossier_view'):
        ANALYST_VIEW[tk] = str(vv_['dossier_view']).lower().strip(); _AV_T[tk] = v.get('_mtime', 0)
if NOTES_PATH.exists():
    _nm = os.path.getmtime(NOTES_PATH)
    for tk, v in json.loads(NOTES_PATH.read_text(encoding='utf-8')).get('tickers', {}).items():
        dv_ = ((v.get('valuation_consistency') or {}).get('dossier_view') or '').lower().strip()
        if dv_ and _nm >= _AV_T.get(tk.upper(), 0):
            ANALYST_VIEW[tk.upper()] = dv_

# (g) Quality-growth lane, pre-committed in STATE.md on 2026-09-26 before any verdict was read (owner challenge: the
#     model-rank gate has no proven edge and cannot see growth or moats). The eight largest AI/cloud companies skip only the
#     rank gate. They are eligible if the full diligence verdict is INCLUDE/INCLUDE-SMALL AND the reverse DCF shows the growth
#     priced in at or below the analyst's evidence-based base case. They have no V1 row, so the V1 gates do not apply.
#     Same caps as every other name.
GROWTH_LANE = ['NVDA', 'MSFT', 'AVGO', 'GOOGL', 'AMZN', 'META', 'AAPL', 'ORCL']
# (h) Triage of every S&P 500 member (pre-committed in STATE.md before any triage result): names the Q-agents ADVANCE and
#     that then receive full diligence are judged by the same rule as the quality-growth lane.
TRIAGE_ADV = set()
for _q in sorted(glob.glob(str(V4 / 'outputs' / 'Q[0-9][0-9]_triage.json'))):
    try:
        for _t, _v in json.loads(pathlib.Path(_q).read_text(encoding='utf-8')).get('tickers', {}).items():
            if isinstance(_v, dict) and _v.get('advance') is True:
                TRIAGE_ADV.add(_t.upper())
    except Exception:
        pass
LANE = set(GROWTH_LANE) | TRIAGE_ADV
# (k) V1 input-defect guard (wave-3 finding, F60; committed before the build that uses it): V1's revenue-based models take
#     D3's XBRL "TTM revenue". Where that disagrees with the independent Yahoo TTM revenue by more than a factor of 1.6
#     either way AND V1 actually used the D3 figure, V1's valuation for that name is treated as invalid (FIX: a mis-dated
#     duplicate XBRL context gave TTM revenue $3.96bn vs $11.23bn true, turning a fairly priced stock into "excessive,
#     base case -52%/yr"). Such names are judged by the analyst route (full diligence verdict + the analyst's own
#     valuation) instead; without a dossier they are ineligible. Financials/REITs valued without revenue are unaffected.
V1_DEFECT = set()
try:
    for _t, _x in json.loads((V4 / 'outputs' / 'v1_valuation.json').read_text(encoding='utf-8'))['companies'].items():
        _i = _x.get('inputs') or {}; _a, _b = _i.get('ttm_revenue_d3'), _i.get('ttm_revenue_yahoo')
        _src = str((_x.get('valuation_model') or {}).get('revenue_base_source') or '')
        if _a and _b and _src.startswith('D3') and not (1 / 1.6 <= _a / _b <= 1.6):
            V1_DEFECT.add(_t)
except Exception:
    pass
LANE = LANE | V1_DEFECT
_IN = V4 / 'outputs' / 'lead_implied_normalization.json'
IMPLIED_NORM = {t: v['implied_vs_base'] for t, v in json.loads(_IN.read_text(encoding='utf-8')).get('tickers', {}).items()} if _IN.exists() else {}
rows = []
for _, r in L.sort_values('live_rank').iterrows():
    t = r.t
    lane = (t in LANE) and not (r.live_rank == r.live_rank and r.live_rank <= 70 and t not in GROWTH_LANE and t not in V1_DEFECT)   # top-70 names keep their original gates unless V1's inputs are defective (k)
    if not lane and (not (r.live_rank == r.live_rank) or r.live_rank > 70):
        continue
    v = VAL.loc[t] if t in VAL.index else None
    dl = DIL.get(t)
    if lane:
        reasons = []
        _iv = ''
        if bool(r.exclude_pending_deal): reasons.append('pending takeover')
        if dl is None:
            reasons.append('no diligence dossier')
        else:
            if dl['verdict'] not in ('INCLUDE', 'INCLUDE-SMALL'): reasons.append(f"diligence {dl['verdict']}")
            _vv = dl.get('valuation_view_vs_v1') if isinstance(dl.get('valuation_view_vs_v1'), dict) else {}
            _iv = str(_vv.get('implied_vs_base') or IMPLIED_NORM.get(t) or '').lower().strip()
            if _iv not in ('below', 'in_line'):
                reasons.append(f"price implies more growth than the analyst's base case ({_iv or 'not stated'})")
        _sc = (dl or {}).get('scenario_returns_3y') or {}
        rows.append(dict(t=t, n=r['name'], s=r.gics_sector, sub=r.gics_sub_industry, rank=(int(r.live_rank) if r.live_rank == r.live_rank else 999), comp=r.composite,
                         Q=r.fam_Q, V=r.fam_V, M=r.fam_M, S=r.fam_S, dec=r.decile, vol=r.vol_1y, voltercile=r.vol_tercile,
                         val='quality-growth lane', analyst_view=ANALYST_VIEW.get(t), valpct=None,
                         bear=_sc.get('bear'), base=_sc.get('base'), bull=_sc.get('bull'), verdict=(dl['verdict'] if dl else None),
                         lane=True, implied=_iv, eligible=not reasons, why=('; '.join(reasons) if reasons else ('eligible (quality-growth lane)' if t in GROWTH_LANE else 'eligible (advanced by triage)'))))
        continue
    reasons = []
    if bool(r.exclude_pending_deal): reasons.append('pending takeover')
    # (i) volatility gate removed for all names (owner: age 35, all-stock, growth-tolerant). Volatility is handled by the
    #     inverse-volatility weights and the caps. Changed before any affected diligence result existed: no already-
    #     diligenced name had been excluded by volatility alone, and all 20 holdings were under 45%.
    vv = (v.verdict if v is not None else None)
    #  (f) Loop-2 data correction: V1 values REITs on an 'FFO proxy' (net income + total D&A) that counts one-off gains on
    #      property sales as recurring (HST 8.5x proxy vs ~10.4x on company AFFO guidance; FRT 10.8x vs ~14.7x). Where agent
    #      V2R has rebuilt NAREIT FFO from filings, its FFO-based verdict replaces V1's proxy-based one.
    if t in V2R and V2R[t].get('corrected_verdict'):
        vv = str(V2R[t]['corrected_verdict']).lower().strip()
    # Loop-1 amendments (disclosed in STATE.md and the report, motivated by internal consistency, not by returns):
    #  (a) missing valuation = unknown = not eligible (A2 must-fix: a late V1 row was silently treated as absent);
    #  (b) never hold a name whose own V1 base-case 3-yr return is negative.
    if vv is None: reasons.append('valuation missing (not yet valued)')
    elif vv not in ('attractive', 'fair'): reasons.append(f'valuation {vv} vs own history')
    if v is not None and v.base_ann_return_3y == v.base_ann_return_3y and v.base_ann_return_3y < 0:
        reasons.append(f'own valuation base case {v.base_ann_return_3y:+.0%}/yr')
    #  (c) Loop-2: a valuation without a computed base case is incomplete = unknown = not eligible (same logic as (a)).
    if v is not None and vv is not None and not (v.base_ann_return_3y == v.base_ann_return_3y):
        reasons.append('valuation incomplete (no base case)')
    #  (e) Loop-2: the valuation gate needs BOTH views to be fair or better - the systematic model (V1) above AND the
    #      analyst's reconciled view in the dossier (T2 notes / F-summary). Symmetric to the RL case (model "demanding",
    #      dossier "earned"): a name whose own analyst values it well below the price is not a "fair price" holding.
    dv = ANALYST_VIEW.get(t)
    if dv in ('full', 'expensive'):
        reasons.append(f"the analyst's own valuation in dossier section 7 calls it {dv}")
    if dl is None: reasons.append('no diligence dossier')
    elif dl['verdict'] not in ('INCLUDE', 'INCLUDE-SMALL'): reasons.append(f"diligence {dl['verdict']}")
    rows.append(dict(t=t, n=r['name'], s=r.gics_sector, sub=r.gics_sub_industry, rank=(int(r.live_rank) if r.live_rank == r.live_rank else 999), comp=r.composite,
                     Q=r.fam_Q, V=r.fam_V, M=r.fam_M, S=r.fam_S, dec=r.decile, vol=r.vol_1y, voltercile=r.vol_tercile,
                     val=vv, analyst_view=ANALYST_VIEW.get(t), valpct=((V2R[t].get('own_pct_10y') if t in V2R else None) or (v.own_history_percentile if v is not None else None)),
                     bear=(v.bear_ann_return_3y if v is not None else None), base=(v.base_ann_return_3y if v is not None else None),
                     bull=(v.bull_ann_return_3y if v is not None else None), verdict=(dl['verdict'] if dl else None),
                     implied=('below' if vv == 'attractive' else ('in_line' if vv == 'fair' else None)), eligible=not reasons, why=('; '.join(reasons) if reasons else 'eligible')))
C = pd.DataFrame(rows)

# ---- diversification: walk down the ranking, max 2 per sub-industry ----
# (j) final size (pre-committed in STATE.md before this build): at most MAX_NAMES, best ideas first:
#     conviction (INCLUDE first), then margin of safety (implied growth below base first), then base-case 3-yr return.
MAX_NAMES = 20
E = C[C.eligible].copy()
E['_conv'] = np.where(E.verdict == 'INCLUDE', 0, 1)
E['_marg'] = E['implied'].map({'below': 0, 'in_line': 1}).fillna(2)
E['_base'] = pd.to_numeric(E['base'], errors='coerce').fillna(-9)
E = E.sort_values(['_conv', '_marg', '_base', 'rank'], ascending=[True, True, False, True])
# (l) at most MAX_PER_SECTOR names per GICS sector (committed 26 Sep 2026 before the wave-3 build). Reason: the 25% sector cap
#     is applied after selection, so a selection with many names in one sector squeezes each of them below the weights
#     that conviction implies (eleven Financials at the cap would average ~2.3%, below a half-conviction name). Five
#     names x 5% average = the 25% cap. Disclosed honestly: written after wave-3 verdicts showed several new
#     full-conviction Financials, before any build or weight was computed with them.
MAX_PER_SECTOR = 5
sel, subcount, seccount = [], {}, {}
for _, r in E.iterrows():
    if subcount.get(r['sub'], 0) >= 2:
        C.loc[C.t == r.t, 'why'] = 'third name in sub-industry'; continue
    if seccount.get(r['s'], 0) >= MAX_PER_SECTOR and len(sel) < MAX_NAMES:
        C.loc[C.t == r.t, 'why'] = f'sixth name in sector ({r["s"]}); rule (l) allows {MAX_PER_SECTOR}'; continue
    if len(sel) >= MAX_NAMES:
        C.loc[C.t == r.t, 'why'] = f'eligible, but outside the best {MAX_NAMES} (conviction, margin of safety, base-case return)'; continue
    sel.append(r.t); subcount[r['sub']] = subcount.get(r['sub'], 0) + 1; seccount[r['s']] = seccount.get(r['s'], 0) + 1
P = C[C.t.isin(sel)].copy().set_index('t')
P['sector'] = P['s']
P['mult'] = np.where(P.verdict == 'INCLUDE-SMALL', 0.5, 1.0)
if len(P) >= 8:
    w, cash, checks, tgt = build_weights(P, hi=0.10, lo=0.03, sector_cap=0.25, sub_cap=0.12, vol_col='vol', mult_col='mult', cap_by_mult=True)
    P['w'] = w; P['target'] = tgt
else:
    cash, checks = None, None

# ---- calibrated per-stock odds from B1 (decile x vol tercile) ----
def cal_lookup(dec, vt):
    c = CAL
    dcol = [x for x in c.columns if 'decile' in x.lower()][0]
    vcol = [x for x in c.columns if 'vol' in x.lower() and 'terc' in x.lower()][0]
    m = c[(c[dcol] == dec) & (c[vcol].astype(str) == str(vt))]
    if m.empty: return None, None
    m = m.iloc[0]
    pp = [x for x in c.columns if re.search(r'p_?fwd12_?pos|p_pos|fwd12>0', x.lower())]
    pb = [x for x in c.columns if re.search(r'excess|beat', x.lower()) and x.lower().startswith('p')]
    return (float(m[pp[0]]) if pp else None), (float(m[pb[0]]) if pb else None)

import hashlib, datetime


def _fp(p):
    p = pathlib.Path(p)
    return {'path': str(p.relative_to(V4)) if str(p).startswith(str(V4)) else str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()[:16],
            'mtime': datetime.datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec='seconds'), 'bytes': p.stat().st_size}


MANIFEST = [_fp(V4 / 'data' / 'b1_live_scores.csv'), _fp(V4 / 'outputs' / 'v1_valuation_table.csv'), _fp(V4 / 'data' / 'd4_live_snapshot.parquet'),
            _fp(V4 / 'outputs' / 'b1_calibration_by_decile_vol.csv')] + ([_fp(NOTES_PATH)] if NOTES_PATH.exists() else []) + ([_fp(V2R_PATH)] if V2R_PATH.exists() else []) + [_fp(p) for p in sorted(paths)] + [_fp(p) for p in sorted(glob.glob(str(V4 / 'dossiers' / '*.md')))]
out = {'candidates': C.to_dict('records'), 'selected': sel, 'built': datetime.datetime.now().isoformat(timespec='seconds'), 'input_manifest': MANIFEST, 'rule_commitment': _RC}
if len(P) >= 8:
    P['p_pos'], P['p_beat'] = zip(*[cal_lookup(r.dec, r.voltercile) for _, r in P.iterrows()])
    def _pe_sane(t):   # A2 loop-3: a corrupted vendor field (PGR NTM P/E 0.27x) must never be shown; fall back to trailing, labelled
        if t not in S.index: return None, None
        for col, basis in (('pe_ntm', 'NTM'), ('trailingPE', 'trailing')):
            try:
                v = float(S.loc[t, col])
            except Exception:
                continue
            if v == v and 3.0 <= v <= 150.0:
                return v, basis
        return None, None
    _pp = [_pe_sane(t) for t in P.index]
    P['pe'] = [a for a, b in _pp]; P['pe_basis'] = [b for a, b in _pp]
    P['next_er'] = [str(S.loc[t, 'next_earnings_date'])[:10] if t in S.index else None for t in P.index]
    _w6 = P.w.round(6)
    _gap = round(round(1.0 - float(cash), 6) - float(_w6.sum()), 6)   # A1 loop-6: stored weights sum exactly to the invested share
    if _gap: _w6.loc[_w6.idxmax()] = round(float(_w6.max()) + _gap, 6)
    out['weights'] = _w6.to_dict(); out['cash'] = 0.0; out['index_fill'] = float(cash)   # remainder held in the index core
    out['checks'] = checks.values.tolist()
    out['sectors'] = P.groupby('s').w.sum().round(4).to_dict()
    out['table'] = P.reset_index().to_dict('records')
# A1/A3 loop-5: content fingerprint of the result (holdings and weights), so a check made against an earlier build can be
# shown to apply to a later, content-identical one. Appended to an append-only history.
out['content_sha256'] = hashlib.sha256(json.dumps(sorted((k, round(float(v), 6)) for k, v in (out.get('weights') or {}).items())).encode()).hexdigest()
with (V4 / 'outputs' / 'build_history.jsonl').open('a', encoding='utf-8') as _bh:
    _bh.write(json.dumps({'built': out['built'], 'content_sha256': out['content_sha256'], 'n': len(out.get('weights') or {}), 'rule_sha256': (_RC or {}).get('sha256')}) + '\n')
(V4 / 'outputs' / 'lead_portfolio_build.json').write_text(json.dumps(out, default=lambda x: None if (isinstance(x, float) and math.isnan(x)) else str(x), indent=1), encoding='utf-8')
print('diligence verdicts parsed:', {k: v['verdict'] for k, v in DIL.items()})
print('eligible:', int(C.eligible.sum()), 'selected:', sel)
if len(P) >= 8:
    print(checks.to_string()); print(P[['s', 'sub', 'rank', 'vol', 'verdict', 'w']].sort_values('w', ascending=False).round(4).to_string())
else:
    print('fewer than 8 eligible names so far; reasons:'); print(C[['t', 'rank', 'why']].head(40).to_string())
