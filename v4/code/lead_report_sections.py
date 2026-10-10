"""Lead: generate the data-driven sections of FINAL_REPORT.md (verdict, portfolio, risk, operating rules, audit) and the
dashboard hero/answer/risk JSONs from the output files, so every number in the report equals the data. Re-run after any update."""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent))
from lead_guard import check_build_fresh
check_build_fresh()  # stops with StaleBuildError if any input changed after the portfolio build
import json, pathlib, re, math, glob
V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
O = V4 / 'outputs'


def load(n):
    p = O / n
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


def pct(x, d=0):
    return '–' if x is None else f"{100 * x:.{d}f}%"


def spct(x, d=1):
    return '–' if x is None else f"{'+' if x > 0 else '−' if x < 0 else ''}{abs(100 * x):.{d}f}%"


P = load('lead_portfolio.json'); RR = load('lead_risk_results.json'); BT = load('b1_results.json'); BLD = load('lead_portfolio_build.json')
rows = sorted(P['rows'], key=lambda r: r['rank'])
import pandas as _pd
V1T = _pd.read_csv(O / 'v1_valuation_table.csv').set_index('ticker')
_V2R = (load('v2r_reit_valuation.json') or {}).get('tickers', {})
def mult_str(r):
    t = r['t']
    if t in _V2R and (_V2R[t].get('pffo_fy26_guide') or _V2R[t].get('pffo_ttm_now')):
        _g = _V2R[t].get('pffo_fy26_guide')
        return f"{float(_g):.1f}x P/FFO (2026 guidance)" if _g else f"{float(_V2R[t]['pffo_ttm_now']):.1f}x P/FFO (NAREIT, TTM)"
    if t in V1T.index and V1T.loc[t, 'classification'] == 'reit':
        return f"{float(V1T.loc[t, 'metric_value']):.1f}x P/FFO (V1 proxy)"
    return '–' if r.get('pe') in (None, 'None') else f"{float(r['pe']):.1f}x" + (' (trailing)' if r.get('pe_label') == 'trailing P/E' else '')
def kill_from_dossier(t):
    txt = (V4 / 'dossiers' / f'{t}.md').read_text(encoding='utf-8', errors='ignore') if (V4 / 'dossiers' / f'{t}.md').exists() else ''
    m = re.search(r'(?:kill criteria|exit triggers?)[^\n]*\n+((?:\s*(?:[-*]|\d+[.)])\s+.+\n?)+)', txt, re.I)
    if not m: return None
    first = re.split(r'\n\s*(?:[-*]|\d+[.)])\s+', '\n' + m.group(1).strip())
    first = [re.sub(r'\*\*|__', '', x).strip() for x in first if x.strip()]
    return first[0] if first else None
N = len(rows)
cash_sleeve = P.get('cash') or 0.0
FILL = float(BLD.get('index_fill') or 0.0)          # sleeve capacity held in the index fund (Loop-2 rule)
_V1X = load('v1x_verification.json') or {}
def _na_reason(t):
    d = ((_V1X.get('tickers', {}) or {}).get(t) or {}).get('nan_explanations') or []
    if d and isinstance(d[0], dict):
        return (f"{t}'s {d[0].get('scenario', 'bear')} case applies a P/E exit multiple to a loss-making year (its worst historical margin), which implies a negative share price "
                f"and cannot be expressed as an annual return. This is a V1 bug found by the independent re-derivation (V1X); floored at zero the scenario would read −100%, a total loss of that position")
    return f"{t}: see v1_valuation.json for the reason"
SCN = {'Bear': '2%', 'Base': '6%', 'Bull': '9%'}


def sim(mix, sc):
    for s in RR['sims']:
        if s['mix'] == mix and s['scenario'] == sc:
            return s['result']['horizons']
    return None


models = ['Index only (100/0/0)', 'Growth (80/20/0)', 'Moderate (55/15/30)', 'Cautious (35/10/55)', 'Defensive (15/10/75)']
# ---------------------------------------------------------------- allocation table (base case) + scenario ranges
alloc_rows = []
for m in models:
    b = sim(m, 'Base'); lo = sim(m, 'Bear'); hi = sim(m, 'Bull')
    alloc_rows.append(dict(model=m,
                           p5=b['5y']['p_total_return_gt_0'], p10=b['10y']['p_total_return_gt_0'],
                           p5_lo=lo['5y']['p_total_return_gt_0'], p5_hi=hi['5y']['p_total_return_gt_0'],
                           p10_lo=lo['10y']['p_total_return_gt_0'], p10_hi=hi['10y']['p_total_return_gt_0'],
                           dd15_5=b['5y']['p_drawdown_worse_than']['-15%'], dd20_5=b['5y']['p_drawdown_worse_than']['-20%'],
                           dd20_1=b['1y']['p_drawdown_worse_than']['-20%'], med5=b['5y']['annualized_return_pct']['p50'],
                           p5th1=b['1y']['total_return_pct']['p5'], ewd5=b['5y']['expected_worst_drawdown']))
stress = RR['stress']
_g = next((s for s in stress if s['episode'].startswith('Global')), {})
_gfc_mod = _g.get('Moderate (55/15/30) | worst point'); _gfc_cau = _g.get('Cautious (35/10/55) | worst point'); _gfc_def = _g.get('Defensive (15/10/75) | worst point')
_gl = (RR.get('equity_share_limits') or {}).get('Global financial crisis', {})
_lim20 = _gl.get('max_equity_share_within_20pct'); _lim15 = _gl.get('max_equity_share_within_15pct')
sleeve_sim = {sc: sim('Stock sleeve alone', sc) for sc in SCN}
risk = RR.get('risk', {})
_w5 = (risk.get('windows', {}) or {}).get('5y', {}) or {}
TE = (RR.get('risk_sample_cov') or {}).get('tracking_error_annual') or _w5.get('tracking_error_annual') or 0.10   # 3-yr daily, sample
TE_R = int(round(TE * 100))
THR = int(round(1.15 * TE * (2 ** 0.5) * 100 / 5.0)) * 5          # ~1-in-8 one-sided under zero alpha over 24 months, rounded to 5 pts
_Sn = _pd.read_parquet(V4 / 'data' / 'd4_live_snapshot.parquet').set_index('ticker')
_wts = {r['t']: r['w'] for r in rows}
DY = sum(_wts[t] * float(_Sn.loc[t, 'trailingAnnualDividendYield'] or 0) for t in _wts if t in _Sn.index) / max(sum(_wts.values()), 1e-9)

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


# ---------------------------------------------------------------- markdown sections
L = []
L.append('## 1. Verdict\n')
mod = next(a for a in alloc_rows if a['model'].startswith('Moderate'))
cau = next(a for a in alloc_rows if a['model'].startswith('Cautious'))
idx = next(a for a in alloc_rows if a['model'].startswith('Index'))
dfn = next((a for a in alloc_rows if a['model'].startswith('Defensive')), None)
_mixdesc = {'Index only (100/0/0)': 'the index alone', 'Growth (80/20/0)': 'the Growth mix (80% index / 20% stocks)',
            'Moderate (55/15/30)': 'the **Moderate** mix (55% index / 15% stocks / 30% T-bills)', 'Cautious (35/10/55)': 'the **Cautious** mix (35/10/55)',
            'Defensive (15/10/75)': 'the **Defensive** mix (15/10/75, the equity budget Codex release v005 chose)'}
_hz = {'p5': '5 years', 'p10': '10 years'}


def ppct(x):
    """probability formatter: never print a simulated 100% or 0% (a model is not a certainty)"""
    if x is None:
        return '–'
    return 'over 99%' if x >= 0.995 else ('under 1%' if x < 0.005 else f"{100 * x:.0f}%")


_clear_lines = []
_below_parts = []
for a in alloc_rows:
    _hi = [(h, a[h]) for h in ('p5', 'p10') if a[h] >= 0.90]
    _lo = [(h, a[h]) for h in ('p5', 'p10') if a[h] < 0.90]
    if _hi:
        _clear_lines.append(f"  - {_mixdesc[a['model']]}: " + ' and '.join(f"**{ppct(v)}** over {_hz[h]}" for h, v in _hi) + ";\n")
    if _lo:
        _below_parts.append(f"{a['model'].replace(' (', ' ').replace(')', '')}: " + ', '.join(f"{ppct(v)} over {_hz[h]}" for h, v in _lo))
_full = [r for r in rows if r['verdict'] == 'INCLUDE']
_ss5 = sleeve_sim['Base']['5y']
_ep = lambda k: next((x for x in stress if x['episode'].startswith(k)), {})
_gf, _cv, _22 = _ep('Global'), _ep('COVID'), _ep('2022')
_n_dil = sum(1 for c in BLD['candidates'] if c.get('verdict') in ('INCLUDE', 'INCLUDE-SMALL', 'WATCH', 'REJECT'))
_n_queue = sum(1 for c in BLD['candidates'] if str(c['why']).startswith('no diligence') and c.get('lane') is True)
_n_elig = sum(1 for c in BLD['candidates'] if c['eligible'])
from statistics import NormalDist as _ND
_p10_1 = 1 - _ND().cdf(0.10 / TE); _p10_5 = 1 - _ND().cdf(0.10 / (TE / 5 ** 0.5))   # zero-alpha, normal approximation
_nohist = list(_gf.get('no_price_tickers') or [])   # holdings with no price at the episode start (b2 'exclude' renormalises them out)
# ---- Read-first block (Loop-11 A1/A2/A3 must-fix, 6 Oct 2026): turnover vs v011, rule (o) figures, verification coverage, 40% mandate
import glob as _gx
_prev = set(json.loads((O / 'lead_previous_sleeve.json').read_text(encoding='utf-8')).get('names', []))
_cur = [t for t in BLD['selected']]
_kept = [t for t in _cur if t in _prev]; _new = [t for t in _cur if t not in _prev]; _gone = sorted(_prev - set(_cur)); _p17 = set('BR WTW GDDY V CAH ACGL WFC COR FIS INTU ADSK BIIB FSLR BKNG FDX ACN OMC AMCR CVS VZ'.split()); _in17 = [t for t in _cur if t not in _p17]; _out17 = sorted(_p17 - set(_cur))
_Wb = BLD['weights']; _Cb = {c['t']: c for c in BLD['candidates']}
_TS = {'Interactive Media & Services', 'Transaction & Payment Processing Services'}
_w_tech = sum(_Wb[t] for t in _cur if _Cb[t]['s'] == 'Information Technology' or _Cb[t]['sub'] in _TS)
_w_it = sum(_Wb[t] for t in _cur if _Cb[t]['s'] == 'Information Technology')
_vchk = set()
for _f in _gx.glob(str(O / 'da[0-9]*_factcheck.json')) + _gx.glob(str(O / 'dv' / 'DV*_factcheck.json')):
    _vchk |= {x.get('ticker') for x in json.loads(pathlib.Path(_f).read_text(encoding='utf-8')).get('facts', []) if x.get('ticker')}
for _f in _gx.glob(str(O / 'ra*_reassess.json')):
    _vchk |= set(json.loads(pathlib.Path(_f).read_text(encoding='utf-8')).get('tickers', {}))
_fn = _ff = 0
for _f in _gx.glob(str(O / 'dv' / 'DV*_factcheck.json')):
    for x in json.loads(pathlib.Path(_f).read_text(encoding='utf-8')).get('facts', []):
        _fn += 1; _ff += str(x.get('status', '')).upper() == 'FAIL'
_n_ver = len({t for t in _vchk if t in _Cb}); _held_ver = sum(1 for t in _cur if t in _vchk)
L.append("### Read this first: what changed since v011, how much is independently verified, and your 40% tolerance\n")
L.append(f"- **{len(_new)} of the {N} holdings are new since v011** ({', '.join(_new)}); {len(_kept)} are kept ({', '.join(_kept) or 'none'}). {len(_gone)} v011 names left ({', '.join(_gone)}). The cause is not market moves: on 5–6 October every v011 holding was re-tested and the first valuation method was found to have systematic errors (stock-based pay added back as if free, interest income counted twice, earnings used as cash, a discount rate that pre-dated the Fed's 16 September rise and the 5.17% 10-year Treasury yield of 25 September, and a bank-style method not applied to banks and insurers). PTC (Schneider's $205 cash bid) and VEEV went to WATCH, and most full-conviction names moved to half conviction. Every change is listed with its reason in §6. Against the previous published release (v017, 6 October) the list changed by {len(_in17)} in ({', '.join(_in17) or 'none'}) and {len(_out17)} out ({', '.join(_out17) or 'none'}), because the completed independent verification of all 500 files moved more names to WATCH, and a new completeness rule (q) now requires a stated base-case return for every holding. These are research findings, not instructions to trade.\n")
L.append(f"- **Technology share (your 20–30% request, rule (o), committed before the build).** Counting Information Technology plus Interactive Media and Payments companies, technology is **{100 * _w_tech:.1f}%** of the portfolio; Information Technology alone is **{100 * _w_it:.1f}%**. The rule did not need to force any swap in this build. Payments companies such as Visa are classified by GICS as Financials, so whether they count as tech is a judgement; both figures are shown.\n")
L.append(f"- **How much is independently verified.** All 500 companies have a full dossier (research from SEC filings), and **{_n_ver} of them have been independently fact-checked and valuation-tested by a second analyst**, including **{_held_ver} of the {N} holdings** (the release gate requires this for every holding). The second pass is another analyst re-reading the same filings, not a different source of economic truth; in the verification series {_ff} of {_fn} facts ({100 * _ff / max(_fn, 1):.0f}%) failed and were corrected in the dossiers, so the first-pass dossiers should not be trusted without their corrections.\n")
L.append("- **Your 40% drawdown tolerance (Codex release v016, 5 October).** Codex recorded that you now accept a temporary fall of up to 40% while the thesis holds, with the all-stock mandate unchanged. This release adopts that. The worst replayed falls for this kind of all-stock portfolio (§7) are close to or beyond 40%, so 40% is a review trigger, not a guaranteed floor. The risk figures in §7 that use a three-year beta of about 0.6 understate market sensitivity: the Loop-11 quant auditor reported betas of 0.93–0.98 in the windows before the last three years, so plan for market-like risk. Events after the 25 September price date are not all reflected: the Loop-12 auditor reported that ACN has since published quarterly results and that UBER has made a takeover bid for Delivery Hero; both sit in half-conviction slots, and prices, earnings dates and any such news should be refreshed before each purchase.\n")
def _wavg(key):
    num = den = 0.0
    for t in _cur:
        x = _Cb[t].get(key)
        if isinstance(x, (int, float)) and x == x:
            num += _Wb[t] * x; den += _Wb[t]
    return (num / den) if den else None
_sb, _sm, _su = _wavg('bear'), _wavg('base'), _wavg('bull')
if None not in (_sb, _sm, _su):
    _ev = lambda r, amt: amt * (1 + r) ** 3
    L.append(f"- **What the portfolio could be worth in 3 years, bottom-up versus no-edge.** Weighting each holding's own 3-year bear / base / bull return gives {100 * _sb:+.0f}% / {100 * _sm:+.0f}% / {100 * _su:+.0f}% a year. On $50,000 that is about ${_ev(_sb, 50000):,.0f} / ${_ev(_sm, 50000):,.0f} / ${_ev(_su, 50000):,.0f}, and on $100,000 about ${_ev(_sb, 100000):,.0f} / ${_ev(_sm, 100000):,.0f} / ${_ev(_su, 100000):,.0f} (before tax, fees and the 30% US withholding on dividends for a non-treaty holder). These weight each holding's own scenarios (the analyst's re-assessed base case where one exists, otherwise the systematic model's), and no stock-selection method tested here beat the S&P 500 on point-in-time data, so the zero-edge market case of about 6% a year is the figure to plan on; treat the bottom-up base case as an upper reference, not a forecast." + chr(10))
L.append(f"**You asked for an all-stock portfolio of 5–20 US companies, researched across the whole S&P 500, with no index fund or T-bills for now. The answer is the {N} stocks in §6.**\n\n"
         + (f"- **How they were chosen.** Every one of the {_n_dil} S&P 500 companies was researched in full from SEC filings (three second share classes are judged with their sibling), including those the quick first pass had screened out: rule (n) lets any of them qualify on full diligence. "
            "Research is not finished for good: each new quarter of results and each weekly review can change a verdict or the list. " if _n_dil >= 495 else
            f"- **How they were chosen.** Every S&P 500 company got at least a quick research pass. So far {_n_dil} of the strongest, including the eight largest AI and cloud companies, have been researched in full from SEC filings. ")
         + (f"Another {_n_queue} passed the quick pass and are queued for full research, so a later round may still displace some holdings. " if _n_queue else ("" if _n_dil >= 495 else "As of the 25 Sep 2026 data cutoff that completes the queue: every company that passed the quick pass has full research (three second share classes are judged with their sibling). Research is not finished for good: each new quarter of results and each weekly review can change a verdict or the list. "))
         + f""
         + (f"The {N} held are the best of the {_n_elig} that passed every test: {len(_full)} at full conviction, together {pct(sum(r['w'] for r in _full))} of the portfolio ({', '.join(r['t'] for r in sorted(_full, key=lambda r: -r['w']))}), and {N - len(_full)} at half conviction.\n"
            if len(_full) < N else f"The {N} held are the best of the {_n_elig} that passed every test, and all {N} are at full conviction.\n")
         + f""
         f"- **What is excluded, and why.** Great companies whose price already assumes more growth than the evidence supports stay out, including Microsoft, Alphabet, Amazon, Meta, NVIDIA and Apple. §6 lists the first 20 eligible stocks not held (in the order they would be picked) and every top-45 name that failed, with the reason; the complete list of all 500 is in the All-500 register.\n"
         f"- **Honest odds.** In the base-case market (6% a year), with no assumed stock-picking edge: a {ppct(_ss5['p_total_return_gt_0'])} chance of a gain over 5 years, a {ppct(_ss5.get('p_beat_benchmark'))} chance of beating the S&P 500, and a {ppct(_ss5['p_drawdown_worse_than']['-20%'])} chance of a fall worse than 20% at some point along the way.\n"
         f"- **In past crises** (today's holdings on daily prices): {spct(_gf.get('sleeve'), 0)} in 2007–09 (S&P 500 {spct(_gf.get('spy'), 0)}); {spct(_cv.get('sleeve'), 0)} in the 2020 COVID crash ({spct(_cv.get('spy'), 0)}); {spct(_22.get('sleeve'), 0)} in 2022 ({spct(_22.get('spy'), 0)}). {', '.join(_nohist)} had no share price in 2007–09 ({pct(1 - (_gf.get('sleeve_real_data_share') or 1))} of the weight); that replay spreads their weight across the other holdings, so it measures {pct(_gf.get('sleeve_real_data_share'))} of today's portfolio{'. The old General Motors went bankrupt in 2009 (today’s GM listed in 2010), so the real 2007–09 loss for this portfolio would likely have been worse' if 'GM' in _nohist else ''}.\n"
         f"- **Beating the index by 10 points a year cannot be promised.** No rule tested here beat the S&P 500 over 2012–2026, and 86–93% of professional large-cap funds trail it over 10–20 years. The portfolio's own numbers size the gap: it strays from the index by about {TE_R}% a year, so with no real edge a single year 10 points ahead happens about {ppct(_p10_1)} of the time, but averaging 10 points ahead over 5 years has about a {ppct(_p10_5)} chance. "
         f"The edge on offer is depth and discipline: every company screened, prices checked against realistic growth, written exit triggers. That guards against overpaying and unexamined risks; whether it adds return is unproven.\n"
         f"- **Before investing directly:** directly held US shares count toward the ~$60,000 US estate-tax threshold for non-US persons (at $100,000 all in stock you would be above it), and 30% of every US dividend is withheld: on this portfolio's {100 * DY:.1f}% yield (weight-averaged trailing dividend yield of the 20 holdings, a snapshot that moves with prices and payouts at every refresh; 25 Sep 2026 snapshot `data/d4_live_snapshot.parquet`; recorded in `outputs/lead_params.json`) that costs about {0.30 * DY * 100:.2f}% of the portfolio a year (§8, §9).\n\n"
         f"### If you later want less risk: the allocation view\n\n"
         f"The rest of this section keeps the earlier analysis. It holds the same stocks as a bounded satellite next to an S&P 500 index fund (Irish-domiciled UCITS) and a T-bill reserve sized to the loss you can tolerate. "
         f"Measured by certainty rather than return, that allocation choice matters more than the stock picks.\n\n"
         f"- **Where 90% confidence is achievable, and where it is not.** Under the base-case market scenario (6% a year, the median of institutional forecasts), these combinations clear 90% odds of a gain:\n"
         + ''.join(_clear_lines)
         + f"\n  Below 90%: " + '; '.join(_below_parts)
         + ". More T-bills buy certainty with lower returns: the median 5-year return is " + ', '.join(f"{spct(a['med5'])} a year for {a['model'].split(' (')[0]}" for a in alloc_rows)
         + ". These odds depend on the scenario (bear-to-bull ranges in §7). No single stock and no stock basket earns 90% confidence.\n"
         f"- **Why stocks are only a satellite.** Our pre-registered model did not beat the S&P 500 over 2012–2026. Neither did v1, v2 or v3 (§5). Any stock has a 65–70% chance of a gain over a year and a 43–46% chance of beating the index, whatever its score.\n"
         f"- **What the satellite is for.** Owning verified businesses at fair prices, and diversifying away from an index whose ten largest stocks are 40% of its value. It is not a bet that it will outperform. Expect roughly index-like returns, give or take about {TE_R}% a year (its measured tracking error).\n"
         f"- **Your drawdown tolerance decides the reserve, not the stock list:**\n"
         f"  - With no reserve, a fall worse than 20% within 5 years is likely: {pct(idx['dd20_5'])} for the index.\n"
         f"  - With 30% in T-bills the odds fall to {pct(mod['dd20_5'])}; with 55%, to {pct(cau['dd20_5'])}.\n"
         f"  - If 15–20% is a pain threshold you would ride through, the Moderate mix balances return and risk. If it is a hard limit in ordinary bear markets, the Cautious mix fits: it stays above −20% in {pct(1 - cau['dd20_5'])} of simulated 5-year paths.\n"
         + (f"  - **If the limit must hold even in a 2008-style crash, hold about a third or less in equities.** In the 2007–09 replay (quarterly rebalancing) the Moderate mix fell {spct(_gfc_mod)} at its worst point and the Cautious mix {spct(_gfc_cau)}. "
            f"Staying within −20% through that crash would have needed about {pct(_lim20)} or less in equities; within −15%, about {pct(_lim15)}.\n" if _gfc_mod is not None else '')
         + (f"  - **That is the Defensive mix (15% index / 10% stocks / 75% T-bills)**, the equity budget Codex's release v005 reached independently with a hypothetical shock test. In the 2007–09 replay it fell {spct(_gfc_def)}. Its chance of a gain over 5 years is {ppct(dfn['p5'])}, and its chance of a fall worse than 20% within 5 years is {ppct(dfn['dd20_5'])}. The price is return: a median of {spct(dfn['med5'])} a year, against {spct(mod['med5'])} for the Moderate mix. The two workstreams agree on this risk arithmetic; §13 records where they differ.\n" if (dfn and _gfc_def is not None) else ''))
L.append('## 6. The stock satellite, ranked and weighted\n')
NSEC = len({r['s'] for r in rows})
L.append(f"**How these {N} were chosen.** Every S&P 500 company got at least a quick research pass: a triage of the 455 names that then had no dossier (all 500 now have a full dossier) (quality, growth, red flags, and whether the price already assumes more growth than is plausible). The strongest were then researched in full from SEC filings, alongside the 40 earlier dossiers and the eight largest AI and cloud companies. "
         "A stock is eligible when its full diligence verdict is INCLUDE (full conviction) or INCLUDE-SMALL (half conviction, with a named reservation), and the growth its price implies is at or below the analyst's evidence-based base case (for names in the model's top 70, the systematic valuation must also be fair or attractive). "
         f"Of the eligible names, the best {N} are held: full conviction first, then the widest margin of safety, then the higher base-case return, with at most two per industry and five per sector (rule (l), added in the third research wave, before any build used it, so the 25% sector cap cannot squeeze full-conviction names below half-conviction weights).\n\n"
         "Weights are inverse to volatility: steadier stocks get more. Full-conviction names get up to 10% and half-conviction names up to 5%. No sector exceeds 25% and no sub-industry 12%, and every cap is verified after solving. "
         "The rules and every amendment are logged with their reasons in STATE.md. Amendments (a)–(i) were written before the results they govern. "
         "Rule (j), the order used to pick the best 20, was written after the diligence verdicts were known but before the ranked list was produced; it is a judgement call, not a pre-registered test. The last tie-breaker (base-case 3-year return) only orders names within the same conviction and margin-of-safety group. For many names it is the systematic model's scenario, which assumes the valuation multiple drifts back toward its own history; that favours deeply de-rated stocks (CMCSA's +62% a year base case is mostly a re-rating from a 6x P/E), and the analysts often called those scenarios optimistic.\n")
L.append('| # | Stock | Sector | Weight in sleeve | Diligence | NTM P/E (REITs: P/FFO) | Base rate for similar stocks, 12 months: gain / beat S&P* | 3-yr bear / base / bull, a year† | Exit if (first trigger) |')
L.append('|---|---|---|---|---|---|---|---|---|')
_miss, _disputed = [], []
for r in rows:
    kill = (r.get('kill') or [kill_from_dossier(r['t']) or 'see dossier'])[0]
    kill = re.sub(r'\s+', ' ', str(kill)).replace('|', '/')   # full text (A3 loop-7: a truncated trigger cannot be checked weekly)
    pe = mult_str(r)
    if any(r.get(k) is None for k in ('bear', 'base', 'bull')):
        _miss.append(r['t'])
    _disp = (not r.get('lane')) and _vdir(r.get('val_consistency')) == 'more cautious than V1'   # lane rows show the analyst's own scenarios
    if _disp:
        _disputed.append(r['t'])
    L.append(f"| {r['rank']} | **{r['t']}** {r['n']} | {r['s']} | {pct(r.get('w_disp', r['w']), 1)} | {r['verdict']}{' §' if r.get('lane') is True else ''} | {pe} | {pct(r.get('p_pos'))} / {pct(r.get('p_beat'))} | "
             f"{spct(r.get('bear'), 0).replace('–', 'n/a')} / {spct(r.get('base'), 0)}{'‡' if _disp else ''} / {spct(r.get('bull'), 0)} | {kill} |")
if FILL > 0.001:
    L.append(f"| – | **S&P 500 index fund** (capacity the caps cannot absorb) | – | {pct(FILL, 1)} | – | – | – | – | – |")
L.append(f"\nWeights are rounded to 0.1 point; " + ("including the index-fund row " if FILL > 0.001 else "") + "they sum to 100% of the sleeve.\n\n"
         "\\* How often S&P 500 stocks in the same model-score band and volatility band rose, or beat the index, over the following 12 months in 2011–2025 (B1 calibration). These describe the group a stock belongs to, not a forecast for that stock; they barely differ across the list because the model score did not predict returns.\n\n"
         "† 3-year bear / base / bull returns, annualised. For names marked §, the analyst's own scenarios (dossier section 7); for the others, the base case is the analyst's re-assessed return where one exists and otherwise V1's scripted scenario, with bear and bull valuations drawn from each company's own history. "
         + ("n/a means V1 could not compute that scenario. " + ' '.join(_na_reason(t) + '.' for t in _miss) + " The base case, which decides eligibility, exists for every holding. " if _miss else "")
         + (f"\n\n‡ The analyst's own valuation is more cautious than V1's base case ({', '.join(_disputed)}): treat that base case as optimistic; each dossier's section 7 ends with a written reconciliation.\n" if _disputed else "\n"))
L.append('**What each holding is for** (one line each, from its dossier; full dossiers in `v4/dossiers/`):\n')
for r in rows:
    _th = (r.get('thesis') or '').strip()
    if not _th or 'pending' in _th.lower():   # A2/A3 loop-9: never ship a placeholder thesis for a held name
        raise SystemExit(f"THESIS MISSING for held name {r['t']}: fix the dossier verdict paragraph or the summary thesis_one_line before building")
    L.append(f"- **{r['t']}** ({r['verdict']}): {_th}")
L.append('')
_prev = load('lead_previous_sleeve.json') or {}
if _prev.get('names'):
    _cur = [r['t'] for r in rows]; _whyd = {c['t']: c['why'] for c in BLD['candidates']}
    _out = [t for t in _prev['names'] if t not in _cur]; _in = [t for t in _cur if t not in _prev['names']]
    _conv = [t for t in _prev.get('full_conviction', []) if t in _cur and next((r['verdict'] for r in rows if r['t'] == t), '') == 'INCLUDE-SMALL']
    L.append(f"**What changed since the previous draft** ({_prev.get('label', 'Loop 1')}):\n")
    if _out:
        L.append('- **Removed:** ' + ('; '.join(_out) if all(str(_whyd.get(t, '')).startswith('eligible') for t in _out) else '; '.join(f"{t} ({_whyd.get(t, 'no longer eligible')})" for t in _out)) + '. ' + ('Each still passes every test; it was displaced by a newly researched name ranked ahead of it in the selection order.' if all(str(_whyd.get(t, '')).startswith('eligible') for t in _out) else ''))
    if _in:
        L.append(f"- **Added:** {', '.join(_in)}, from the latest round of full research on names that passed the quick pass (names researched: {_n_dil}; still queued: {_n_queue}).")
    if _conv:
        L.append(f"- **Conviction lowered:** {', '.join(_conv)}, from full to half weight (see each dossier's latest correction).")
    L.append('')
excl = [c for c in BLD['candidates'] if c['rank'] <= 45 and not c['eligible']]
_fin_n = sum(1 for r in rows if r['s'] == 'Financials'); _fin_w = sum(r['w'] for r in rows if r['s'] == 'Financials')
_fin_out = [c['t'] for c in BLD['candidates'] if str(c.get('why', '')).startswith('sixth name in sector (Financials)')]
if _fin_n >= 5 and _fin_w >= 0.2499:
    L.append(f"**Financials binds two limits at once:** it holds the maximum five names and sits at the 25% sector cap ({pct(_fin_w, 1)}). "
             f"Eligible Financials (full or half conviction) left out by the five-name limit: {', '.join(_fin_out[:8]) or 'none'}{' and others' if len(_fin_out) > 8 else ''}. "
             "The cap also trims the weights of the five held, so each sits below what its volatility alone would give it.\n")
_rich = [r for r in rows if isinstance(r.get('pe'), (int, float)) and r['pe'] == r['pe'] and float(r['pe']) > 25]
if _rich:
    L.append("**Holdings priced above 25x earnings:** " + '; '.join(f"{r['t']} ({float(r['pe']):.1f}x)" for r in sorted(_rich, key=lambda r: -float(r['pe'])))
             + ". Each still qualifies only because its analyst's reverse DCF finds the price implies growth at or below the evidence-based base case; a high multiple is not by itself a reason to exclude, but these names have the least room for a disappointment. "
             "Where an independent peer-multiple cross-check exists it is recorded in Appendix A.4 (DA17, DA20).\n")
_lane_n = sum(1 for r in rows if r.get('lane') is True)
L.append(f"§ Entered through the analyst route ({_lane_n} of {N}): outside the model's top 70, so eligibility rests on the full diligence verdict and the analyst's own valuation (price-implied growth at or below the evidence-based base case). The other {N - _lane_n} are in the model's top 70 and also had to pass the systematic valuation (fair or attractive against their own history).\n")
_JS = load('lead_j_sensitivity.json') or {}
if _JS.get('orderings'):
    _o = _JS['orderings']; _alt = [k for k in _o if not k.startswith('actual')]
    _gfcs = [v['episodes']['Global financial crisis'] for v in _o.values()]
    L.append(f"**How much does the selection order matter?** Rule (j) was re-run under {len(_alt)} alternative orderings ({'; '.join(_alt)}). "
             f"Each keeps {min(v['overlap_with_actual'] for v in _o.values())}–{max(v['overlap_with_actual'] for k, v in _o.items() if not k.startswith('actual'))} of the 20 names; "
             f"{_JS['n_in_every_ordering']} are chosen under every ordering ({', '.join(_JS['in_every_ordering'])}). "
             f"The risk barely moves: the 2007–09 replay ranges from {spct(min(_gfcs), 0)} to {spct(max(_gfcs), 0)}. The exact list is a judgement at the margin; the character of the portfolio is not (outputs/lead_j_sensitivity.json).\n")
_VC = (load('lead_verdict_changes.json') or {}).get('changes') or []
if _VC:
    L.append("**Diligence errors that changed a verdict or a holding** (caught by the independent fact-checks before release; each dossier carries a dated correction):\n")
    for _c in _VC:
        L.append(f"- **{_c['ticker']}** ({_c['date']}, {_c['check']}): {_c['finding']} {_c['effect']}")
    L.append('')
_ODH = (load('order_dependence_history.json') or {}).get('history') or []
if _JS.get('orderings') and _ODH:
    _seq = ' → '.join(f"{h['n_in_every_ordering']} ({h['release'].split(' ')[0]})" for h in _ODH) + f" → {_JS['n_in_every_ordering']} (this build)"
    L.append(f"**Order-dependence over time** (names chosen under every ordering tested): {_seq}. The count has fallen as the eligible pool grew; the tie-breaker now decides much of the list, while the 2007–09 replay stays within the range shown above.\n")
_prevN = (_prev or {}).get('n_in_every_ordering')
if _JS.get('orderings') and _prevN is not None and _prevN != _JS.get('n_in_every_ordering') and not _ODH:
    L.append(f"**Order-dependence is {'rising' if _JS['n_in_every_ordering'] < _prevN else 'falling'}:** {_JS['n_in_every_ordering']} names are chosen under every ordering tested, against {_prevN} in {_prev.get('label', 'the previous release')}. "
             "As more companies pass every test, more of them tie on conviction and margin of safety, so the final tie-breaker decides more of the list. The risk profile moves much less than the names (see the range above).\n")
_bench = [c for c in BLD['candidates'] if c['eligible'] and c['t'] not in {r['t'] for r in rows}]
_bench.sort(key=lambda c: (c.get('verdict') != 'INCLUDE', {'below': 0, 'in_line': 1}.get(c.get('implied'), 2), -(c['base'] if isinstance(c.get('base'), (int, float)) and c['base'] == c['base'] else -9), c['rank']))   # mirrors the build's (j) order
if _bench:
    _why_short = lambda w: ('five-per-sector limit' if str(w).startswith('sixth name in sector') else 'two-per-industry limit' if 'sub-industry' in str(w) else 'outranked in the selection order')
    L.append(f"**Eligible but not held: {len(_bench)} names.** Each passed every test and is a candidate replacement if a holding's exit trigger fires. The first 20, in the order they would be picked:\n")
    L.append('| Next in line | Stock | Sector | Conviction | Price implies growth … the base case | Base-case return a year | Why not held |')
    L.append('|---|---|---|---|---|---|---|')
    for _k, c in enumerate(_bench[:20], 1):
        _b = c.get('base') if isinstance(c.get('base'), (int, float)) and c.get('base') == c.get('base') else None
        L.append(f"| {_k} | **{c['t']}** {c.get('n', '')} | {c.get('s', '')} | {'full' if c.get('verdict') == 'INCLUDE' else 'half'} | {'below' if c.get('implied') == 'below' else 'in line with'} | {spct(_b, 0) if _b is not None else 'n/a'} | {_why_short(c.get('why'))} |")
    L.append(f"\nThe other {max(len(_bench) - 20, 0)} are listed, with their position in the selection order and the reason they missed, in `outputs/lead_j_sensitivity.json` (bench_near_misses) and in the dashboard's ranking tab.\n")
L.append('**Every name ranked in the top 45 by the model that the process excluded, with the reason:** ' + '; '.join(f"{c['t']} (rank {c['rank']}: {c['why']})" for c in excl) + '.\n')
L.append('## 7. Risk\n')
L.append('**Historical stress replays** (daily data; the sleeve at today\'s weights, buy-and-hold through each episode; the mixes combine the S&P 500, the sleeve and 4% T-bills, rebalanced quarterly as the operating rules say):\n')
L.append('| Episode | Dates (S&P peak → trough) | Stock sleeve | S&P 500 | Moderate 55/15/30 | Cautious 35/10/55 | Defensive 15/10/75 | Max equity share to stay within −20% / −15% |')
L.append('|---|---|---|---|---|---|---|---|')
_EL = RR.get('equity_share_limits') or {}
for s in stress:
    _e = _EL.get(s['episode'], {})
    L.append(f"| {s['episode']} | {s['dates']} | {spct(s['sleeve'])} | {spct(s['spy'])} | {spct(s['Moderate (55/15/30)'])} | {spct(s['Cautious (35/10/55)'])} | {spct(s.get('Defensive (15/10/75)'))} | "
             f"{pct(_e.get('max_equity_share_within_20pct'))} / {pct(_e.get('max_equity_share_within_15pct'))} |")
L.append('\nThe last column is the largest share of the portfolio in equities (index and stocks in the Moderate mix\'s 55:15 proportions, the rest in T-bills) that would have kept that episode\'s worst point within the loss limit.\n')
WF = RR.get('worst_fall') or {}
if WF:
    _s, _m = WF['sleeve'], WF['spy_same_days']
    _gfc = next((s for s in stress if s['episode'].startswith('Global')), None)
    L.append(f"\n**The worst fall to plan around.** Over the full daily history ({WF['window'].replace('..', ' to ')}) at today's weights, the stock sleeve's worst fall was **{spct(_s['max_drawdown'])}** "
             f"(peak {_s['peak']}, trough {_s['trough']}, {'recovered ' + _s['recovered'] if _s.get('recovered') else 'not yet recovered'}). The S&P 500's worst fall over the same days was {spct(_m['max_drawdown'])} "
             f"({_m['peak']} to {_m['trough']}). The crisis replays above use the S&P 500's own peak and trough dates, so they can show a smaller figure for the sleeve"
             + (f" (GFC: {spct(_gfc['sleeve'])})" if _gfc else '') + f". Treat {spct(_s['max_drawdown'], 0)} as the sleeve's tail-risk anchor. "
             + (f"In the Moderate mix the 2007–09 replay cost {spct(_gfc['Moderate (55/15/30)'])} and in the Cautious mix {spct(_gfc['Cautious (35/10/55)'])}; set those against your 15–20% tolerance." if _gfc else '') + "\n")
_ss = RR.get('sim_settings') or {}
L.append("\n**Simulated outcomes by allocation.** 20,000 possible 5- and 10-year futures, each built by stitching together blocks of real market days from 2005–2026 and re-centred on the bear, base or bull market return. The stock satellite is assumed to have no edge. The method and its settings are in Appendix A.\n")
L.append('| Allocation (index / stocks / T-bills) | P(gain) 5 yrs: base (bear–bull) | P(gain) 10 yrs: base (bear–bull) | P(fall > 15% within 5 yrs) | P(fall > 20% within 5 yrs) | Median 5-yr return a.r. | Bad year (5th pct, 1 yr) |')
L.append('|---|---|---|---|---|---|---|')
for a in alloc_rows:
    L.append(f"| {a['model']} | {ppct(a['p5'])} ({ppct(a['p5_lo'])}–{ppct(a['p5_hi'])}) | {ppct(a['p10'])} ({ppct(a['p10_lo'])}–{ppct(a['p10_hi'])}) | {ppct(a['dd15_5'])} | {ppct(a['dd20_5'])} | {spct(a['med5'])} | {spct(a['p5th1'])} |")
ss = sleeve_sim['Base']
L.append(f"\n**The stock satellite on its own** (base case, zero assumed alpha): P(gain) {pct(ss['1y']['p_total_return_gt_0'])} over 1 year and {pct(ss['5y']['p_total_return_gt_0'])} over 5. P(beating the S&P 500) is {pct(ss['1y'].get('p_beat_benchmark'))} over 1 year and {pct(ss['5y'].get('p_beat_benchmark'))} over 5, a coin flip by construction. P(a fall worse than 20% within 5 years) is {pct(ss['5y']['p_drawdown_worse_than']['-20%'])}.\n")
_sc = RR.get('risk_sample_cov') or {}
if _sc:
    _nm = lambda k: 'the index-fund share' if k == 'SPY' else k
    _spec = sorted((_sc.get('specific_contribution_pct_by_name') or {}).items(), key=lambda x: -x[1])
    _rtw = sorted((_sc.get('risk_to_weight_ratio') or {}).items(), key=lambda x: -x[1])
    L.append(f"**Diversification.** The {N} stocks behave like about **{_sc.get('enb_risk', 0):.0f} independent positions** once their tendency to move together is counted "
             f"({_sc.get('enb_weight', 0):.0f} if only the weights are counted). About **{pct(_sc.get('systematic_share_of_variance'))}** of the sleeve's day-to-day risk comes from the market as a whole "
             f"(its sensitivity to the S&P 500, beta, is {_sc.get('beta_3y', 0):.2f}); the rest is specific to the companies. The largest company-specific risks are "
             + ', '.join(f"{_nm(k)} ({pct(v)})" for k, v in _spec[:3]) + ". Per dollar invested, the riskiest holdings are "
             + ', '.join(_nm(k) for k, v in _rtw[:2]) + f" and {_nm(_rtw[2][0])}" + f": each adds {_rtw[2][1]:.1f}–{_rtw[0][1]:.1f} times as much of the sleeve's risk as its weight alone would suggest"
             + ". Measured over the last three years of daily prices, the sleeve's volatility is " + pct(_sc.get('vol_annual'), 1) + " and it strays from the S&P 500 by about "
             + pct(_sc.get('tracking_error_annual'), 1) + " a year. An independent re-computation and the method are in Appendix A.\n")
L.append('## 9. Operating rules and the weekly 30-minute review\n')
L.append('- **Entry:** three equal tranches about three weeks apart, using limit orders near the last close. Never buy a stock in the two trading days before its earnings date.\n'
         '- **Rebalance quarterly, not weekly.** A holding is sold only if it its independently re-assessed verdict falls to WATCH or REJECT, the price comes to imply more growth than the analyst\'s base case, or a pre-written kill criterion fires. A position is trimmed if it exceeds 1.5× its target weight. Most weeks the right action is no trade.\n'
         '- **Drawdowns trigger reviews, not panic.** At −10% for the portfolio, review every thesis; at −15%, review the equity/reserve mix; at −20%, the stated tolerance is reached. Stop orders are not used, because gaps fill below the trigger.\n'
         '- **Evaluate the satellite honestly.** After 12 and 24 months, compare it with the S&P 500 on the same dates. If it trails by more than ' + str(THR) + ' points over 24 months (about a 1-in-8 outcome if it has no edge, given its ' + str(TE_R) + '% tracking error), fold it into the index.\n'
         '- **Weekly checklist (about 30 minutes):**\n'
         '  1. Check the moves.\n'
         '  2. Check any earnings or guidance changes against each dossier\'s kill criteria.\n'
         '  3. Scan the news for M&A, regulation, management or accounting issues.\n'
         '  4. Check weight drift.\n'
         '  5. Log the decision, including "no trade".\n'
         '  6. At quarter-end, re-run the model and review the replacement list.\n')
L.append('\n**Turning percentages into amounts** (arithmetic only; which mix to use and how much to invest are your decisions):\n')
L.append('- Amount in a layer = your total × that layer\'s share. Amount in one stock = your total × the stock layer\'s share × the stock\'s weight in the sleeve.\n'
         '- Units to buy in one tranche = that stock\'s amount ÷ 3 ÷ today\'s price, rounded down. Alternatively, use IBKR\'s "cash quantity" to buy a dollar amount in fractional shares.\n'
         '- **Minimum-commission rule:** IBKR charges at least about $1 per US stock order. If a stock\'s amount is under about $300, buy it in one order instead of three: a $1 charge on a $100 order costs 1%.\n')
L.append('| Per $10,000 invested | Index fund (core + unfilled sleeve) | Individual stocks | T-bill reserve | A 10% sleeve position (full conviction) | A 5% sleeve position (half conviction) |')
L.append('|---|---|---|---|---|---|')
for _m, (_c, _sl, _rv) in [('**All stock (0/100/0): your portfolio**', (0.0, 1.0, 0.0)), ('Index only (100/0/0)', (1.0, 0.0, 0.0)), ('Growth (80/20/0)', (0.8, 0.2, 0.0)), ('Moderate (55/15/30)', (0.55, 0.15, 0.30)), ('Cautious (35/10/55)', (0.35, 0.10, 0.55)), ('Defensive (15/10/75)', (0.15, 0.10, 0.75))]:
    L.append(f"| {_m} | ${10000 * (_c + _sl * FILL):,.0f} | ${10000 * _sl * (1 - FILL):,.0f} | ${10000 * _rv:,.0f} | " + (f"${10000 * _sl * 0.10:,.0f}" if _sl else '–') + ' | ' + (f"${10000 * _sl * 0.05:,.0f}" if _sl else '–') + ' |')
L.append('\nScale every figure by your total ÷ 10,000. Worked example of the arithmetic (an illustrative total, not a suggestion): at $80,000 all in stock, a holding with a 7.0% weight is $80,000 × 7.0% = $5,600, bought as three tranches of about $1,870; a 1.5% holding is $1,200, three tranches of $400. In the Moderate mix the same 7.0% holding would be $80,000 × 15% × 7.0% = $840.\n')
L.append('\n**Estate tax and withholding at your size** (general information; confirm with a cross-border tax adviser; assumes you are not a US citizen or green-card holder):\n')
L.append('| Allocation | Individual US stocks at $50k / $100k (US-situs) | Below the ~$60k US estate-tax threshold? | Dividend withholding drag on those stocks (30% × ' + f"{100 * DY:.1f}" + '% yield) |')
L.append('|---|---|---|---|')
_us = 1 - FILL
L.append(f"| **All stock (0/100/0): your portfolio** | ${50000 * _us:,.0f} / ${100000 * _us:,.0f} | **At $50k yes; at $100k no.** Above about $60,000 of US shares, a non-US person's estate can owe US estate tax (up to 40% on the excess) | {0.30 * DY * _us * 100:.2f}% of the total portfolio a year (30% of a {100 * DY:.1f}% dividend yield) |")
for _m, _sl in [('Growth (80/20/0)', 0.20), ('Moderate (55/15/30)', 0.15), ('Cautious (35/10/55)', 0.10), ('Defensive (15/10/75)', 0.10)]:
    _us = _sl * (1 - FILL)
    L.append(f"| {_m} | ${50000 * _us:,.0f} / ${100000 * _us:,.0f} | Yes, provided the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund | {0.30 * DY * _us * 100:.2f}% of the total portfolio a year |")
L.append('\nA US-domiciled ETF (VOO, SPY) or a US T-bill ETF would count toward the $60k threshold; the UCITS versions do not (R2).\n')
(O / 'lead_report_sections.md').write_text('\n'.join(L), encoding='utf-8')

# ---------------------------------------------------------------- splice into FINAL_REPORT.md between markers
fr = (V4 / 'FINAL_REPORT.md').read_text(encoding='utf-8')
txt = '\n'.join(L)
parts = {'VERDICT': txt.split('## 6. ')[0].strip(), 'PORTFOLIO': '## 6. ' + txt.split('## 6. ')[1].split('## 7. ')[0].strip(),
         'RISK': '## 7. ' + txt.split('## 7. ')[1].split('## 9. ')[0].strip(), 'OPERATING': '## 9. ' + txt.split('## 9. ')[1].strip()}
for k, v in parts.items():
    _rep = f'<!-- SECTION:{k} -->\n{v}\n<!-- /SECTION:{k} -->'
    fr = re.sub(rf'<!-- SECTION:{k} -->.*?<!-- /SECTION:{k} -->', lambda _m, _r=_rep: _r, fr, flags=re.S)
(V4 / 'FINAL_REPORT.md').write_text(fr, encoding='utf-8')

# ---------------------------------------------------------------- dashboard JSONs: hero, answer, risk view, next
hero = {'title': f"Your all-stock portfolio: {N} researched companies chosen from the whole S&P 500.",
        'lede': (f"You asked for an all-stock portfolio chosen from the whole S&P 500. Every company got a quick research pass; {_n_dil} got full SEC-filing research so far. "
                 f"The <b>{N} stocks</b> held are the best of {_n_elig} that passed every test: good businesses whose price does not assume more growth than the evidence supports. "
                 f"That rule keeps out Microsoft, NVIDIA, Alphabet, Amazon, Meta and Apple at today's prices. "
                 f"<b>Honest odds:</b> no rule tested here beat the S&P 500 over 2012–2026, so treat beating it as a coin flip, not a promise. "
                 f"The price of going all-stock is risk: the {N} fell {spct(_gf.get('sleeve'), 0)} in the 2007–09 replay."),
        'tiles': [[str(N), f"stocks held ({len(_full)} full conviction, {N - len(_full)} half)"], [ppct(_ss5['p_total_return_gt_0']), 'chance of a gain over 5 years (base case)'],
                  [ppct(_ss5.get('p_beat_benchmark')), 'chance of beating the S&P 500 over 5 years (no assumed edge)'], [spct(_gf.get('sleeve'), 0), 'fall in the 2007–09 replay (S&P 500 ' + spct(_gf.get('spy'), 0) + ')'],
                  [f"{(RR.get('risk_sample_cov') or {}).get('enb_risk', 0):.0f}", 'independent bets, once co-movement is counted']]}
answer = [{'k': 'If you want less risk later: what to own', 'v': 'An S&P 500 UCITS fund (e.g. CSPX or VUAA, Irish-domiciled: no US estate tax, 15% dividend withholding) as the core; T-bills or a UCITS T-bill fund as the reserve; the stock satellite at no more than 15–20% of the total (any part of the satellite the caps cannot fill also goes into the index fund).'},
          {'k': 'If you want less risk later: how much in each', 'v': f"This depends on your drawdown limit. <b>Moderate 55/15/30</b>: {ppct(mod['p5'])} chance of a gain over 5 years, {ppct(mod['dd20_5'])} chance of a fall worse than 20% at some point. <b>Cautious 35/10/55</b>: {ppct(cau['p5'])} and {ppct(cau['dd20_5'])}. Index only: {ppct(idx['p5'])} and {ppct(idx['dd20_5'])}. In a 2008-style crash even the Cautious mix fell {spct(_gfc_cau, 0) if _gfc_cau is not None else 'about 27%'}; a limit that must hold then needs about {pct(_lim20) if _lim20 is not None else 'a third'} or less in equities." + (f" <b>Defensive 15/10/75</b> (the equity budget of Codex's release v005): {ppct(dfn['p5'])} and {ppct(dfn['dd20_5'])}; it fell {spct(_gfc_def, 0)} in the 2008 replay." if (dfn and _gfc_def is not None) else '') + " Your call; this is scenario analysis, not advice."},
          {'k': 'What to expect from the stocks', 'v': f'Roughly index-like returns, give or take about {TE_R}% a year. The honest odds for each name: 65–70% chance of a gain over a year, 43–46% chance of beating the index. Every holding has written exit triggers.'},
          {'k': 'What would change the view', 'v': f'A satellite that trails the S&P 500 by more than {THR} points over 24 months (fold it into the index); a kill criterion firing on a holding; a new quarter\'s model re-run replacing more than half the names.'},
          {'k': 'Your portfolio: all stock', 'v': (f"Hold the {N} stocks at the weights in the table, with no index fund or T-bills. In past crises they fell "
                + (f"{spct(_g.get('sleeve'), 0)} in the 2007–09 replay (S&P 500 {spct(_g.get('spy'), 0)}), " if _g else '')
                + (f"{spct(next((s['sleeve'] for s in stress if s['episode'].startswith('COVID')), None), 0)} in the COVID crash and {spct(next((s['sleeve'] for s in stress if s['episode'].startswith('2022')), None), 0)} in 2022. " if stress else '')
                + f"Base case: {ppct(sleeve_sim['Base']['5y']['p_total_return_gt_0'])} chance of a gain over 5 years, a coin flip to beat the S&P 500, and {ppct(sleeve_sim['Base']['5y']['p_drawdown_worse_than']['-20%'])} chance of a fall worse than 20% at some point. "
                "Fewer than 12–15 names adds single-company risk. Direct US shares count toward the ~$60k US estate-tax threshold for non-US persons. "
                + f"30% of US dividends is withheld: about {0.30 * DY * 100:.2f}% of the portfolio a year on its {100 * DY:.1f}% yield. Research, not advice.")}]
answer = [answer[-1]] + answer[:-1]   # loop-3 (A3): the all-stock answer the owner asked for comes first
risk_view = {'lede': (f"All stock, the {N} holdings have a {ppct(_ss5['p_drawdown_worse_than']['-20%'])} chance of a fall worse than 20% at some point within 5 years (base case). If you later want less risk, allocation is the lever. The index alone has a {pct(idx['dd20_5'])} chance of a fall worse than 20% at some point within 5 years; "
                      f"adding a 30% T-bill reserve cuts it to {pct(mod['dd20_5'])}, and 55% cuts it to {pct(cau['dd20_5'])}. "
                      f"The {N} stocks fell harder than the index in the COVID crash and held up far better in 2022."),
             'stress': [[s['episode'], s['dates'], s['sleeve'], s['spy'], s.get('Moderate (55/15/30)'), s.get('Cautious (35/10/55)'), s.get('Defensive (15/10/75)'),   # C1 re-run: same S&P-dated figures as the report table
                         (_EL.get(s['episode']) or {}).get('max_equity_share_within_20pct'), (_EL.get(s['episode']) or {}).get('max_equity_share_within_15pct'),
                         s.get('sleeve_real_data_share')] for s in stress],
             'worst': next((x for x in L if x.startswith('\n**The worst fall to plan around.**')), '').strip().replace('**', ''),
             'sens': next((x for x in L if x.startswith('**How sensitive are these odds')), '').strip().replace('**', ''),
             'sleeveRisk': next((x for x in L if x.startswith('**Sleeve risk today**')), '').strip().replace('**', ''),
             'divers': next((x for x in L if x.startswith('**Diversification.**')), '').strip().replace('**', ''),
             'sims': [], 'contrib': [],
             'allocHead': ['Allocation (index / stocks / T-bills)', 'P(gain) 5 yrs (bear–bull)', 'P(gain) 10 yrs (bear–bull)', 'P(fall >15%) 5 yrs', 'P(fall >20%) 5 yrs', 'Median 5-yr a.r.', 'Bad year (5th pct)'],
             'alloc': [[a['model'], f"{ppct(a['p5'])} ({ppct(a['p5_lo'])}–{ppct(a['p5_hi'])})", f"{ppct(a['p10'])} ({ppct(a['p10_lo'])}–{ppct(a['p10_hi'])})", ppct(a['dd15_5']), ppct(a['dd20_5']), spct(a['med5']), spct(a['p5th1'])] for a in alloc_rows],
             'allocNum': [1, 2, 3, 4, 5, 6],
             'notes': 'Scenarios: Bear 2% / Base 6% / Bull 9% a year (R1, sourced from 12 institutional forecasts); T-bills 4%. 20,000 stationary-bootstrap paths of 2005–2026 daily returns (B2 module). Sleeve alpha assumed zero. Scenario analysis, not advice.'}
for sc in SCN:
    for m in ['Stock sleeve alone'] + models:
        h = sim(m, sc)
        if not h: continue
        for hz in ['1y', '5y', '10y']:
            risk_view['sims'].append({'mix': m, 'sc': sc, 'h': int(hz[:-1]), 'p_profit': h[hz]['p_total_return_gt_0'], 'p_beat': h[hz].get('p_beat_benchmark'),
                                      'med': h[hz]['annualized_return_pct']['p50'], 'dd15': h[hz]['p_drawdown_worse_than']['-15%'], 'dd20': h[hz]['p_drawdown_worse_than']['-20%']})
_short = {'Index only (100/0/0)': 'Index only', 'Growth (80/20/0)': 'Growth 80/20/0', 'Moderate (55/15/30)': 'Moderate 55/15/30', 'Cautious (35/10/55)': 'Cautious 35/10/55', 'Defensive (15/10/75)': 'Defensive 15/10/75'}
risk_view['allocBars'] = [['Chance of a gain over 5 years', [[_short[a['model']], a['p5']] for a in alloc_rows]],
                          ['Chance of a gain over 10 years', [[_short[a['model']], a['p10']] for a in alloc_rows]],
                          ['Chance of a fall worse than 20% within 5 years', [[_short[a['model']], a['dd20_5']] for a in alloc_rows]]]
rc = (RR.get('risk_sample_cov') or {}).get('risk_contribution_pct_by_name') or {}   # sample covariance (A1 loop-1 fix)
risk_view['contrib'] = sorted([[k, v] for k, v in rc.items()], key=lambda x: -x[1])
nxt = ('Spend 10 minutes on two choices: hold all ' + str(N) + ' stocks or only the ' + str(len(_full)) + ' full-conviction names (a more concentrated bet), and read the estate-tax note in §8 before investing more than about $60,000 directly in US shares. '
       'The order steps are in the Implementation tab.')
(O / 'lead_params.json').write_text(json.dumps({'TE': TE, 'TE_R': TE_R, 'THR': THR, 'DY': DY}), encoding='utf-8')
_mixes = [('All stock (0/100/0): your portfolio', (0.0, 1.0, 0.0)), ('Index only (100/0/0)', (1.0, 0.0, 0.0)), ('Growth (80/20/0)', (0.8, 0.2, 0.0)), ('Moderate (55/15/30)', (0.55, 0.15, 0.30)), ('Cautious (35/10/55)', (0.35, 0.10, 0.55)), ('Defensive (15/10/75)', (0.15, 0.10, 0.75))]
(O / 'lead_impl_extra.json').write_text(json.dumps({
    'formula': ["Amount in a layer = your total × that layer's share. Amount in one stock = your total × the stock layer's share × the stock's weight in the sleeve.",
                "Units to buy in one tranche = that stock's amount ÷ 3 ÷ today's price, rounded down (or use IBKR's \"cash quantity\" for a dollar amount in fractional shares).",
                "IBKR charges at least about $1 per US stock order: if a stock's amount is under about $300, buy it in one order instead of three.",
                f"{pct(FILL, 0)} of the stock sleeve is held in the S&P 500 index fund because the caps cannot absorb more with {N} names; it is included in the index column below."],
    'head': ['Per $10,000 invested', 'Index fund (core + unfilled sleeve)', 'Individual stocks', 'T-bill reserve', 'A 10% sleeve position', 'A 5% sleeve position'],
    'estate': {'note': 'General information; confirm with a cross-border tax adviser. Assumes you are not a US citizen or green-card holder.',
               'head': ['Allocation', 'US shares held directly at $50k / $100k', 'Below the ~$60k US estate-tax threshold?', 'Dividend withholding cost (30% of the dividends)'],
               'rows': [['All stock (0/100/0): your portfolio', f"${50000 * (1 - FILL):,.0f} / ${100000 * (1 - FILL):,.0f}", "At $50k yes; at $100k no. Above about $60,000 of US shares, a non-US person’s estate can owe US estate tax (up to 40% on the excess).", f"{0.30 * DY * (1 - FILL) * 100:.2f}% of the portfolio a year"]]
                       + [[m, f"${50000 * sl * (1 - FILL):,.0f} / ${100000 * sl * (1 - FILL):,.0f}", 'Yes, if the index core is an Irish UCITS fund and the reserve is directly held T-bills or a UCITS T-bill fund', f"{0.30 * DY * sl * (1 - FILL) * 100:.2f}% of the portfolio a year"] for m, (c, sl, rv) in _mixes if 0 < sl < 1],
               'foot': 'A US-domiciled ETF (VOO, SPY) or a US T-bill ETF would count toward the $60k threshold; the Irish UCITS versions do not.'},
    'rows': [[m, f"${10000 * (c + sl * FILL):,.0f}", f"${10000 * sl * (1 - FILL):,.0f}", f"${10000 * rv:,.0f}", (f"${10000 * sl * 0.10:,.0f}" if sl else '–'), (f"${10000 * sl * 0.05:,.0f}" if sl else '–')] for m, (c, sl, rv) in _mixes]},
    ensure_ascii=False), encoding='utf-8')
for n_, obj in [('lead_hero.json', hero), ('lead_answer.json', answer), ('lead_risk_view.json', risk_view), ('lead_next.json', nxt)]:
    (O / n_).write_text(json.dumps(obj, ensure_ascii=False), encoding='utf-8')
print('sections written; N =', N, '; moderate p10', mod['p10'], '; cautious p5', cau['p5'])

# ---------------------------------------------------------------- audit loops section (from v4/audit/A*_loop*.json)
_loops = {}
for _f in sorted((V4 / 'audit').glob('A[123]_loop*.json')):
    _m = re.match(r'(A[123])_loop(\d+)\.json', _f.name)
    try:
        _d = json.loads(_f.read_text(encoding='utf-8'))
        _loops.setdefault(int(_m.group(2)), {})[_m.group(1)] = float(_d.get('total'))
    except Exception:
        pass
_fx = json.loads((V4 / 'audit' / 'loop_fixes.json').read_text(encoding='utf-8')) if (V4 / 'audit' / 'loop_fixes.json').exists() else {}
AUD = ['## 10. Independent audit loops\n',
       'Three independent auditors score the whole deliverable on the same 100-point rubric each loop (v4/audit/RUBRIC.md): **A1** quant & data (ex-head of quant research), **A2** investment committee (ex-PM, top-tier long-only fund), **A3** client & compliance (ex-private-bank CIO, UAE clients). Loop 0 scored the original v3 deliverable. Every must-fix item is implemented before the next loop; reports are in v4/audit/.\n',
       '| Loop | A1 quant & data | A2 investment committee | A3 client & compliance | Average | What changed after this loop |', '|---|---|---|---|---|---|']
for _lp in sorted(_loops):
    _v = _loops[_lp]; _avg = sum(_v.values()) / len(_v)
    AUD.append(f"| {'0 (v3 baseline)' if _lp == 0 else _lp} | {_v.get('A1', '–')} | {_v.get('A2', '–')} | {_v.get('A3', '–')} | **{_avg:.1f}** | {_fx.get(str(_lp), '')} |")
fr2 = (V4 / 'FINAL_REPORT.md').read_text(encoding='utf-8')
_aud_txt = '<!-- SECTION:AUDIT -->\n' + '\n'.join(AUD) + '\n<!-- /SECTION:AUDIT -->'
fr2 = re.sub(r'<!-- SECTION:AUDIT -->.*?<!-- /SECTION:AUDIT -->', lambda _m: _aud_txt, fr2, flags=re.S)
(V4 / 'FINAL_REPORT.md').write_text(fr2, encoding='utf-8')

# ---------------------------------------------------------------- §13 relationship to Codex release v005 (shared-workspace rule)
_X = load('lead_v005_reconciliation.json')
if _X:
    _cell = lambda t: re.sub(r'\s+', ' ', str(t or '')).replace('|', '/')
    V5 = ['## 13. Relationship to Codex release v005\n',
          f"A second AI workstream (Codex) published a completed decision pack, **{_X['v005_release']}** (prepared {_X.get('v005_prepared_utc', '')[:16].replace('T', ' ')} UTC; data {_X.get('v005_data_cutoff', '')}). "
          "The shared workspace rules require each new release to check the previous one and record what it adopts, confirms, changes, rejects or leaves open, with evidence. "
          "This v4 release neither silently replaces v005 nor inherits its conclusions unchecked. Where the two differ, the evidence is below and the owner decides.\n",
          '| Topic | Status | Codex v005 | Claude v4 (evidence) | Effect on this release |', '|---|---|---|---|---|']
    for f in _X['findings']:
        V5.append(f"| **{_cell(f['topic'])}** | {_cell(f['status'])} | {_cell(f['v005'])} | {_cell(f['v4'])} | {_cell(f['effect'])} |")
    V5 += ['', "**v005's fourteen candidates, seen through v4's gates** (prices at the 25 September close):\n",
           '| v005 rank | Stock | v005 decision | v005 max entry | Price 25 Sep | vs limit | v4 model rank | v4 valuation (base 3-yr, a year) | v4 status |', '|---|---|---|---|---|---|---|---|---|']
    for c in _X['candidates']:
        V5.append(f"| {c['v005_rank']} | **{c['t']}** | {c['v005_decision']} | " + ('–' if c['v005_limit'] is None else f"${c['v005_limit']:,.2f}") + ' | '
                  + ('–' if c['v4_price_2026_09_25'] is None else f"${c['v4_price_2026_09_25']:,.2f}") + f" | {spct(c['price_vs_limit'])} | {c['v4_rank'] if c['v4_rank'] is not None else '–'} | "
                  + (c['v4_V1'] or '–') + ('' if c['v4_V1_base_3y'] is None else f" ({spct(c['v4_V1_base_3y'], 0)})") + f" | {_cell(c['v4_status'])} |")
    _x1 = _X.get('x1')
    V5.append('\n' + (f"**Verification of v005's inherited claims** (agent X1, `v4/outputs/x1_v005_verification.md`): {_x1['confirmed']} of {_x1['checked']} checked claims confirmed against v4's price data, issuer pages and SEC filings."
                      + (' Exceptions: ' + '; '.join(_cell(x) for x in (_x1.get('exceptions') or [])) + '.' if _x1.get('exceptions') else '')
                      + (' Method disagreement: ' + '; '.join(_cell(d) for d in (_x1.get('disagreements') or [])) if _x1.get('disagreements') else '')
                      if _x1 else "**Verification of v005's inherited claims** is in progress (agent X1)."))
    V5.append("\nParents recorded for this release (explicit, per RESEARCH_VERSIONING.md): v017_2026-10-06_claude, v016_2026-10-05_codex, v015_2026-10-04_codex, v014_2026-10-01_codex, v013_2026-10-01_codex, v012_2026-09-27_codex, v011_2026-09-27_claude, v010_2026-09-27_claude, v005_2026-09-26_codex, claude-v3, codex-initial-audit, codex-deep-data-audit.")
    V5 += ['', "### Codex releases v012–v016 (27 Sep – 5 Oct 2026): adopted, changed, rejected, unresolved\n",
           "- **Adopted:** v016's mandate recast: you accept a temporary fall of up to 40% while the thesis holds, and the mandate stays 100% individual US stocks with no bond ETF or cash sleeve. v015's dated two-feed price checks and bounded event audit, and v013/v012's method repairs, are accepted as historical evidence and as methods.",
           "- **Changed:** this release is the all-stock redesign that v016's brief asked the next allocator to build. It re-underwrites candidates on filings (all 500 dossiers) instead of carrying over v014/v015 weights, and it does not carry over their PG/PEP/PEG defensive substitutions, which were motivated by the old 15–20% tolerance.",
           "- **Rejected:** applying v015's old-basket return bands (4–8% a year) to this different portfolio; treating 40% as a guaranteed loss floor; treating several agent reviews as independent economic sources (the same applies to this report's own audits).",
           "- **Unresolved:** v012–v015's individual price and event claims were not re-verified here; actual positions and tax/account facts; prices and filings after 25 September were checked only for the names re-assessed on 5–6 October; Codex's entry limits are not reconciled against this release's valuations for names that differ."]
    fr3 = (V4 / 'FINAL_REPORT.md').read_text(encoding='utf-8')
    _v5_txt = '<!-- SECTION:V005 -->\n' + '\n'.join(V5) + '\n<!-- /SECTION:V005 -->'
    fr3 = re.sub(r'<!-- SECTION:V005 -->.*?<!-- /SECTION:V005 -->', lambda _m: _v5_txt, fr3, flags=re.S)
    (V4 / 'FINAL_REPORT.md').write_text(fr3, encoding='utf-8')
    print('section 13 (v005 reconciliation) written')
