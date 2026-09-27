"""Lead: assemble the v4 dashboard data (D4V) from whatever agent outputs exist, inject the v4 tabs into the
benchmark dashboard (never removing v1/v2/v3 tabs), and write v4/dashboard/equity_audit_v4.html for publishing.
Re-run after every loop; missing pieces render as 'pending'."""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent))
from lead_guard import check_build_fresh
check_build_fresh()  # never assemble a dashboard that mixes a stale build with newer inputs
import json, re, glob, pathlib, math, datetime
import pandas as pd, numpy as np, markdown

V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')
BASE_HTML = V4 / 'dashboard' / 'artifact_v3_published_backup.html'
OUT_HTML = V4 / 'dashboard' / 'equity_audit_v4.html'


def rd(p):
    p = V4 / p
    return p.read_text(encoding='utf-8') if p.exists() else None


def clean(x):
    if isinstance(x, dict): return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [clean(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if (x != x or math.isinf(x)) else round(float(x), 6)
    if isinstance(x, np.integer): return int(x)
    if isinstance(x, np.bool_): return bool(x)
    if isinstance(x, (pd.Timestamp, datetime.date)): return str(x)[:10]
    return x


def md_table(text, header_startswith):
    """Return rows (list of cell lists) of the first markdown table whose header starts with header_startswith."""
    lines = text.splitlines(); rows = []; on = False
    for ln in lines:
        s = ln.strip()
        if not on and s.startswith('|') and s[1:].strip().startswith(header_startswith):
            on = True; continue
        if on:
            if not s.startswith('|'): break
            if re.match(r'^\|\s*-', s): continue
            rows.append([c.strip() for c in s.strip('|').split('|')])
    return rows


def strip_md(s):
    return re.sub(r'\*\*|`', '', s).strip()


D = {'asof': '2026-09-25'}
PARAMS = json.loads(rd('outputs/lead_params.json') or '{}')

# ---------- v3 audit (lead verified findings) ----------
FIX = {
    '1': 'Probabilities shown under three sourced market scenarios (bear 2% / base 6% / bull 9%, R1) plus empirically calibrated odds from the point-in-time backtest.',
    '2': 'All backtests use point-in-time S&P 500 membership (D1) so a stock only counts after it joined the index.',
    '3': 'The v3 filter is re-tested over 2010–2026 on point-in-time data; v4 uses a pre-registered model and reports all variants.',
    '4': 'Drawdowns computed on daily data with missing history excluded or proxied and labelled (B2).',
    '5': 'Solver checks every cap after solving; infeasible caps leave disclosed cash instead of breaking a limit.',
    '6': 'No zero-filling: missing history is excluded or proxied with a labelled synthetic series.',
    '7': 'Every stock valued on calendarised next-twelve-month (NTM) EPS; FY0/FY1 shown alongside.',
    '8': 'Expected returns come from sourced market scenarios plus haircut, backtest-calibrated alpha; no beta-scaled market return, no buyback double count.',
    '9': 'Reverse DCF on FCFF discounted at WACC with SBC treated as a cost; financials valued on ROE vs cost of equity (V1).',
    '10': 'Four evidence-based factor families with measured correlations; stability reported as sensitivity, never as confidence.',
    '11': 'Missing data is marked unknown, never a pass; financials routed to business-model-specific checks in diligence.',
    '12': 'Model frozen in STATE.md before any v4 backtest; 16 years of monthly point-in-time tests; walk-forward by year.',
    '13': 'Benchmark is SPY total return (and ^SP500TR); stocks are total return too.',
    '14': 'Each holding has a primary-source dossier with adverse facts, GAAP vs adjusted reconciliation and kill criteria.',
    '15': 'Vendor metadata is never used as evidence; identities checked against SEC CIKs.'}
t = rd('outputs/lead_v3_audit.md')
if t:
    rows = md_table(t, '#')
    D['v3audit'] = [{'sev': r[1], 'f': strip_md(r[2]), 'ev': strip_md(r[3]), 'fix': FIX.get(r[0], '')} for r in rows if len(r) >= 5]
    D['v3auditLede'] = ('Fifteen findings, every one re-computed from the v3 files. The four critical ones: the 90% figure was an assumption, '
                        'the momentum evidence carried look-ahead bias, the only out-of-sample test pointed the wrong way, and the real '
                        'drawdown was about 10 points worse than reported. Items marked [C] were first raised by an earlier external review '
                        'and verified here; [L] items were found or quantified in this audit.')
    D['v3credit'] = ('Credit where due: v3 correctly rejected per-stock 90% certainty, measured survivorship bias against RSP, read primary-source '
                     'earnings releases (no fabricated headline figures were found), flagged the UAE estate-tax structure, and left reproducible code.')

# ---------- method ----------
st = rd('STATE.md') or ''
m = re.search(r'## Pre-registered primary model.*?\n(.*?)\n## ', st, re.S)
D['method'] = {
    'prereg': re.sub(r'\s+', ' ', m.group(1)).strip() if m else '',
    'steps': [['1 · Universe', 'Every stock that was actually in the S&P 500 on each date since 2000 (not today\'s survivors).'],
              ['2 · Data', 'Total-return prices; as-filed SEC XBRL fundamentals usable only after their filing date.'],
              ['3 · Model', 'Pre-registered quality, value, momentum and earnings-surprise families; sector-neutral; equal weights.'],
              ['4 · Evidence', '16 years of monthly point-in-time backtests with costs, independent replication and stress tests.'],
              ['5 · Diligence', 'Primary-source dossiers on every finalist: statements with variance analysis, guidance, balance sheet, adverse facts, kill criteria.'],
              ['6 · Portfolio', 'Risk-balanced weights with caps verified after solving; daily-data stress tests; scenario odds.'],
              ['7 · Audit', 'Three deep data audits plus three independent scorers per loop until the score stops improving.']],
    'data': [], 'agents': [], 'limits': []}
DATA_ROWS = [('d1', 'Index membership 1996–2026 + CIK/sector map', 'fja05680 GitHub dataset, Wikipedia change log, SEC submissions'),
             ('d2', 'Daily prices & total returns 1995–2026', 'Yahoo Finance (validated vs Stooq)'),
             ('d3', 'As-filed fundamentals (point-in-time)', 'SEC XBRL companyfacts API'),
             ('d4', 'Live snapshot, consensus estimates, NTM valuation', 'Yahoo Finance; SEC frames; Stooq'),
             ('r1', 'Capital-market assumptions & base rates', '12+ institutional CMAs, Shiller/Damodaran data'),
             ('r2', 'UAE implementation & cross-border tax facts', 'IRS, UAE MoF, fund issuers, broker pages'),
             ('r3', 'Factor evidence & base rates', 'Kenneth French library, SPIVA, peer-reviewed papers')]
D['method']['data'] = [
    ['D1 · S&P 500 membership 1996–2026, company IDs, sectors', 'fja05680 historical components + Wikipedia change log + SEC submissions',
     '1,271 membership spells, 1,217 companies; 99.99% of member-months mapped to an SEC CIK', 'Final month = Wikipedia list exactly; 10/10 change-date spot checks; 499–506 members every month'],
    ['D2 · Daily prices & total returns 1995–2026', 'Yahoo Finance (1,172 symbols)',
     'Point-in-time member-days priced: 69% (2010–14), 79% (2015–19), 93% (2020–26)', 'CNBC: 96.7% of closes within 0.5% (99.93% up to constant corporate-action offsets); SPY vs official S&P 500 TR −0.11%/yr'],
    ['D3 · As-filed fundamentals (point in time)', 'SEC XBRL companyfacts (3.56M facts, 659 companies)',
     'Revenue TTM ≥96.7% of members from 2012; earnings-surprise ≥89.6%', 'Net income 100/100 within 1% of statements; 0 facts used before their filing date (114,695 rows); restatements enter only when filed'],
    ['D4 · Live snapshot at the 25 Sep 2026 close', 'Yahoo Finance; SEC frames; Cboe & CNBC',
     '503/503 constituents; calendarised NTM valuation', '503/503 prices within 0.5% of both Cboe and CNBC; SEC revenue 94.9% within 2%'],
    ['DA1 · Deep audit: prices & corporate actions (76/100)', 'SlickCharts, StockAnalysis, Macrotrends, company IR',
     '503 closes, 50 historical spot checks, 25 splits, 6 spin-offs', 'Pass with fixes: some "missing" members are recent delistings (CMA, EA, K) — disclosed'],
    ['DA2 · Deep audit: SEC fundamentals vs filing documents (83/100)', 'EDGAR rendered statements; Shibui Finance',
     '44 filing checks; 149/150 cross-source matches', 'Pass with fixes: BRK-B EPS ×1,500 and filer EPS scale errors (7 tickers) fixed before final scoring'],
    ['DA3 · Deep audit: estimates & valuation inputs (86/100)', 'SEC submissions, 8-K texts, FMP (where the plan allowed)',
     'All 503 NTM calculations; 21 non-December fiscal years', 'Pass: NTM maths 500/500 consistent; fiscal dates 21/21 vs SEC; no missed takeover targets'],
    ['R1–R3 · Market scenarios, UAE facts, factor evidence', '12+ institutional CMAs, IRS/UAE MoF/issuers, French library, SPIVA, peer-reviewed papers',
     'Bear 2% / Base 6% / Bull 9%; 71 cited tax/structure sources; 29 papers', 'Every figure dated and sourced in v4/outputs/r1_, r2_, r3_ reports']]
D['method']['agents'] = [
    ['D1–D4', 'Data builders', 'membership, prices, SEC fundamentals, live snapshot'], ['R1–R3', 'Researchers', 'scenarios, UAE implementation, evidence base'],
    ['B1 / B1X', 'Backtest + independent replication', 'agree within 0.04 pts/yr; rank correlation 0.976'], ['B2', 'Risk engine', 'daily drawdowns, stress, bootstrap (25 unit tests)'],
    ['V1 / V1X', 'Valuation + independent re-derivation', '92 names on one method: own-history multiples, reverse DCF, scenarios; V1X re-derives every holding from SEC filings'],
    ['F1–F15', 'Diligence analysts', 'primary-source dossiers with statements, guidance track, kill criteria, one-line thesis and a reconciliation with V1'],
    ['T2', 'Holding-notes editor', 'faithful one-line theses and verbatim kill criteria; flags any dossier that disagrees with V1'],
    ['DA1–DA4, D2R', 'Deep data auditors', 'prices, SEC fundamentals, estimates, 30+ dossier facts against SEC filings; D2R re-downloads the "no price data" list'],
    ['R3', 'Implementation verifier', 'IBKR entity and protection, broker eligibility, fund facts, estate-tax situs, withholding'],
    ['A1–A3', 'Independent scorers', 'quant & data · investment committee · client & compliance']]
D['method']['limits'] = [
    'No stock-selection edge was found (2012–2026); the stock sleeve is therefore sized as a bounded satellite and assumed to have zero alpha in every probability shown.',
    'Free price data lacks many delisted companies (coverage 69–93% by era); measured bias +1.0 pt/yr vs the real equal-weight ETF, disclosed with every backtest number.',
    'No point-in-time history of analyst estimates exists in free data, so revisions and NTM valuation are live overlays, never backtested drivers.',
    'Probabilities are conditional on the Bear/Base/Bull market scenarios and on history being a fair guide to volatility and crashes; they are not guarantees.',
    'The lead\'s early triage file had a stale-XBRL-tag bug (110 rows); it only ordered the diligence queue — see the error log (v4/outputs/lead_error_log.md).',
    'FMP premium endpoints were plan-gated, so estimate cross-checks used SEC and other free sources; earnings-call transcripts were read where companies publish them.',
    'The "no price data" list is itself imperfect: DA1 found its three most important entries (CMA, EA, K) were download failures, not delistings. D2R re-downloads the whole list; the effect shows up in the measured +1.0 pt/yr residual bias and cannot make the negative result positive.',
    'The backtest starts in 2012 because as-filed XBRL fundamentals begin in 2009–2011, so the model history excludes 2008; the stress tests replay 2007–09 for today\'s sleeve on prices only.',
    'Simulations rebalance to the target mix daily (the B2 method), a simplification against the quarterly rule; the crisis replays use quarterly rebalancing. Results are insensitive to the bootstrap block length (5, 21 or 63 days).']
_ix = rd('outputs/lead_impl_extra.json')
IMPL_EXTRA = json.loads(_ix) if _ix else {}
_fr = rd('FINAL_REPORT.md') or ''
_gl = _fr.split('## 12. Plain-English glossary', 1)[1] if '## 12. Plain-English glossary' in _fr else ''
D['glossary'] = [[m.group(1).strip(), m.group(2).strip()] for m in re.finditer(r'^- \*\*(.+?):\*\*\s*(.+)$', _gl, re.M)]

# ---------- implementation facts (R2) ----------
D['impl'] = {'lede': 'General information for a UAE-resident (non-US) investor, with primary sources. Confirm specifics with a qualified cross-border tax adviser.',
             'facts': [], 'rules': [], 'weekly': [],
             'disclaimer': 'Research and general information, not personalised investment, tax or legal advice. The author is not a licensed adviser; no trades are placed.'}
r2 = rd('outputs/r2_implementation_facts.md')
if r2:
    D['impl']['facts'] = [
        ['US estate tax on US-situs assets', 'Non-US persons get a $13,000 credit ≈ $60,000 exemption (not indexed); rates 18–40%; Form 706-NA above $60k. No US–UAE estate treaty. Illustrative tax: $80k → $5,200; $100k → $10,800.', 'https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns'],
        ['US dividend withholding', '30% for UAE residents (no US–UAE income-tax treaty; W-8BEN does not reduce it). Capital gains generally not US-taxed.', 'https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z'],
        ['UAE taxation', 'No personal income tax; Cabinet Decision 49/2023 keeps personal investment income outside UAE Corporate Tax.', 'https://mof.gov.ae/'],
        ['Irish UCITS S&P 500 funds', 'CSPX / VUAA / SPY5 (physical, 15% withholding inside the fund) and SPXS (swap, ~0% withholding, counterparty risk) are not US-situs. All-in annual tax drag at a 1.11% yield: VOO 0.36%, CSPX/VUAA 0.24%, SPY5 0.20%, SPXS 0.12%.', 'https://www.ishares.com/'],
        ['Brokers', 'IBKR: US stocks ~$0.005/share (min $1); LSE ETFs 0.05% of value; no inactivity fee. Vested: 0.25% per trade (max $35), US stocks/ETFs only, clears via DriveWealth (US-situs), and appears to onboard only Indian-origin (PAN/NRI) clients — check eligibility (R3).', 'https://www.interactivebrokers.com/en/pricing/commissions-stocks.php'],
        ['Which IBKR entity holds a UAE account', 'UAE residents are onboarded by Interactive Brokers (U.K.) Ltd, DIFC Branch (DFSA Category 4, an arranging broker); custody sits with Interactive Brokers LLC in the US, so SIPC protection applies (not FSCS). Verified on IBKR\'s own pages, 26 Sep 2026 (R3).', 'https://www.interactivebrokers.com/'],
        ['Open items only a broker or adviser can settle', 'Marked permanently open, each with a workaround. (1) Estate-tax situs of idle cash at a US broker: keep the reserve in T-bills or a UCITS T-bill fund such as IB01, not as a large broker cash balance. (2) Fractional units of CSPX/VUAA at IBKR: the order ticket shows whether "cash quantity" is offered; otherwise buy whole units (VUAA about $149 a unit at its 24 Sep NAV). (3) IBKR market-data fees: optional; delayed quotes are free.', ''],
        ['UAE regulator name change', 'The Securities and Commodities Authority (SCA) became the Capital Market Authority (CMA) on 1 Jan 2026 (Federal Laws 32 and 33 of 2025). Sarwa is regulated by the ADGM FSRA (R3).', ''],
        ['Implication', 'Individual US stocks cannot be wrapped in UCITS, so a stock-picking sleeve is US-situs; keeping it near or below ~$60k limits estate-tax exposure, while the index core can sit in a UCITS fund.', '']]

D['impl']['rules'] = [
    ['Structure: index core + stock satellite', 'Hold broad US exposure in an Irish-domiciled UCITS S&P 500 fund (not US-situs, 15% fund-level dividend withholding) and the v4 stocks as a satellite. The satellite is where the research can add return; the core is where the 90%-over-10-years confidence actually lives.'],
    ['Entry: three tranches, limit orders', 'Buy in three equal tranches about three weeks apart. Use limit orders near the last close and never buy a stock in the two trading days before its earnings date. In Dubai time the US market is open 17:30–00:00 while US daylight saving applies (early March to early November) and 18:30–01:00 otherwise.'],
    ['Rebalance quarterly, not weekly', 'Re-run the model each quarter. Sell a holding only if it falls out of the top quarter of the ranking or a kill criterion fires. Trim any position above 1.5× its target weight. Most weeks the right action is no trade.'],
    ['Kill criteria are pre-written', 'Each holding has 3–5 measurable exit triggers in its dossier (for example, a guidance cut plus a >10% fall in next-year EPS estimates, leverage above a stated level, or a thesis-breaking event). If one fires, exit at the next review; if none fires, price moves alone are not a reason to sell.'],
    ['Drawdowns trigger reviews, not panic', 'A −10% portfolio fall triggers a review of every thesis; −15% a review of the equity/reserve mix; −20% means the stated tolerance is reached. Stop orders are not used: gaps can fill far below the trigger.'],
    ['Know what would change the view', f'Fold the satellite into the index if it trails the S&P 500 by more than {PARAMS.get("THR", 20)} points over 24 months (about a 1-in-8 outcome if it has no edge, given its {PARAMS.get("TE_R", 12)}% tracking error). Revisit the design if a quarterly re-run replaces more than half the names or a data audit finds a material error.']]
D['impl']['steps'] = [
    'Open the IBKR mobile app or Client Portal and log in yourself (never share credentials). Confirm your W-8BEN is on file: Settings → Account Settings → Tax Forms.',
    'Put US dollars in the account. If you hold AED: Trade → Currency Conversion (FX) → sell AED, buy USD → review the rate → submit.',
    'Index core: tap Search → type CSPX (or VUAA) → choose the London Stock Exchange line quoted in USD (iShares Core S&P 500 UCITS ETF (Acc) / Vanguard S&P 500 UCITS ETF (USD) Accumulating) → check that the fund name and "Ireland" domicile match.',
    'Tap Buy → Order type: Limit → Limit price: the last price or a few cents above → Quantity: units = this line\'s amount ÷ 3 tranches ÷ the current price, rounded down (amounts per $10,000 are in the table above) → Time in force: Day → Preview → check the commission (about 0.05% of value) and total → Submit. LSE hours in Dubai time are roughly 11:00–19:30.',
    'Stock satellite: search each ticker (e.g. HST) → Buy → Limit → use "Cash quantity" if you want a fixed dollar amount (fractional shares) → Day → Preview (commission about $1 minimum) → Submit. US hours in Dubai time: 17:30–00:00 until early November, then 18:30–01:00.',
    'Check Orders → Filled; unfilled limit orders expire at the close — re-enter the next day rather than chasing the price.',
    'Record the fills (date, price, units) in the decision log. Repeat for tranches 2 and 3 about three weeks apart; skip any stock within two trading days of its earnings date.']
D['impl']['weekly'] = [
    'Open the dashboard: note the week\'s moves for the portfolio, the S&P 500 and each holding (2 min).',
    'Check whether any holding reported earnings or issued guidance this week; compare with its kill criteria in the dossier tab (10 min).',
    'Check the news list for holdings for M&A, regulatory action, management changes or accounting issues (5 min).',
    'Check weights against targets: act only if a position exceeds 1.5× target or a kill criterion fired (3 min).',
    'Record the decision, including "no trade", in the decision log with the date and reason (5 min).',
    'Quarter-end weeks only: re-run the model and review the replacement list before trading (extra 30 min).']
D['impl']['dollars'] = IMPL_EXTRA

# ---------- evidence summary (R1, R3) ----------
D['evidence'] = {}
sc = V4 / 'data' / 'r1_scenarios.csv'
if sc.exists():
    s = pd.read_csv(sc)
    D['evidence']['scenarios'] = clean(s[['scenario', 'nominal_geo_return', 'P_gain_1y', 'P_gain_5y', 'P_gain_10y', 'P_loss_worse_than_20pct_5y_endpoint']].to_dict('records'))

# ---------- audits ----------
loops = {}
latest_rows = {}
for f in sorted(glob.glob(str(V4 / 'audit' / 'A[123]_loop*.*'))):
    fn = pathlib.Path(f).name; mm = re.match(r'(A[123])_loop(\d+)\.(md|json)', fn)
    if not mm: continue
    aid, lp, ext = mm.group(1), int(mm.group(2)), mm.group(3)
    score = None
    txt = pathlib.Path(f).read_text(encoding='utf-8', errors='ignore')
    if ext == 'json':
        try: score = float(json.loads(txt).get('total'))
        except Exception: pass
    else:
        m2 = re.search(r'[Tt]otal[^\n0-9]{0,40}?(\d{1,3}(?:\.\d)?)\s*/\s*100', txt) or re.search(r'(\d{1,3}(?:\.\d)?)\s*/\s*100', txt)
        if m2: score = float(m2.group(1))
    # A2 loop-5: the JSON total is authoritative; the .md regex is only a fallback when no JSON total exists
    # (sorted() reads A3_loop2.json before A3_loop2.md, and the .md regex had overwritten 89 with an earlier '80/100' mention).
    if score is not None and (ext == 'json' or aid not in loops.get(lp, {})):
        loops.setdefault(lp, {})[aid] = score
# regression check (A2 loop-7): every score shown must equal the auditor's JSON total when that JSON exists
for _f in glob.glob(str(V4 / 'audit' / 'A[123]_loop*.json')):
    _mm = re.match(r'(A[123])_loop(\d+)\.json', pathlib.Path(_f).name)
    try:
        _tot = float(json.loads(pathlib.Path(_f).read_text(encoding='utf-8')).get('total'))
    except Exception:
        continue
    if loops.get(int(_mm.group(2)), {}).get(_mm.group(1)) != _tot:
        raise SystemExit(f'AUDIT SCORE MISMATCH: {_mm.group(1)} loop {_mm.group(2)} dashboard={loops.get(int(_mm.group(2)), {}).get(_mm.group(1))} json={_tot}')
fixes = json.loads(rd('audit/loop_fixes.json') or '{}')
D['audits'] = {'lede': 'Each loop: three independent auditors (quant & data; investment committee; client & compliance) score the whole deliverable on the same 100-point rubric, and every must-fix item is implemented before the next loop. Loop 0 scores the original v3 deliverable as the baseline.',
               'loops': []}
for lp in sorted(loops):
    sc_ = loops[lp]; vals = [v for v in sc_.values() if v is not None]
    D['audits']['loops'].append({'loop': ('0 (v3 baseline)' if lp == 0 else str(lp)), 'A1': sc_.get('A1'), 'A2': sc_.get('A2'), 'A3': sc_.get('A3'),
                                 'avg': round(sum(vals) / len(vals), 1) if vals else None, 'fixes': fixes.get(str(lp), '')})

# ---------- optional blocks produced by later phases (json files written by lead scripts) ----------
for key, fn in [('hero', 'outputs/lead_hero.json'), ('answer', 'outputs/lead_answer.json'), ('port', 'outputs/lead_portfolio.json'),
                ('bt', 'outputs/lead_bt_view.json'), ('risk', 'outputs/lead_risk_view.json'), ('rank', 'outputs/lead_rank.json'), ('next', 'outputs/lead_next.json'), ('v005', 'outputs/lead_v005_reconciliation.json'), ('appendix', 'outputs/lead_appendix.json')]:
    t_ = rd(fn)
    if t_: D[key] = json.loads(t_)
if 'hero' not in D:
    D['hero'] = {'title': 'v4 rebuild in progress: v3 audited, new evidence being built.',
                 'lede': 'The v3 portfolio failed its own tests: the 90% figure was an assumption, its momentum evidence carried look-ahead bias, and its real drawdown was about 36%, not 26%. The v4 rebuild uses point-in-time data, a pre-registered model, primary-source diligence and independent audit loops. Scores update here after every loop.',
                 'tiles': [['15', 'v3 flaws verified'], ['−36%', 'v3 real worst fall (reported −26%)'], ['18%', 'v3 momentum CAGR without look-ahead (claimed 29%)'], ['6%', 'base-case market return (v3 assumed 10%)']]}

# ---------- dossiers ----------
dos = {}
for f in sorted(glob.glob(str(V4 / 'dossiers' / '*.md'))):
    tk = pathlib.Path(f).stem.upper()
    html = markdown.markdown(pathlib.Path(f).read_text(encoding='utf-8', errors='ignore'), extensions=['tables'])
    dos[tk] = '<div class="dossier">' + html + '</div>'
D['dossiers'] = dos

D = clean(D)
(V4 / 'dashboard' / 'd4v.json').write_text(json.dumps(D, ensure_ascii=False), encoding='utf-8')

# ---------- inject into benchmark HTML ----------
h = BASE_HTML.read_text(encoding='utf-8')
for a, b in [('<!DOCTYPE html>', ''), ('<html lang="en">', ''), ('<head>', ''), ('</head>', ''), ('<body>', ''), ('</body></html>', ''), ('</body>', ''), ('</html>', ''),
             ('<meta charset="utf-8">', ''), ('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">', '')]:
    h = h.replace(a, b, 1)
h = h.replace(':root{--bg:#0a0e1a;', ':root{color-scheme:dark;--bg:#0a0e1a;', 1)
h = h.replace(':root[data-theme="light"]{', ':root[data-theme="light"]{color-scheme:light;', 1)
extra_css = ('<style>.dossier h1{font-size:26px;margin:0 0 8px}.dossier h2{font-size:20px;margin:22px 0 6px}.dossier h3{font-size:16px;margin:16px 0 6px;color:var(--gold2)}'
             '.dossier table{margin:8px 0;display:block;overflow-x:auto}.dossier td,.dossier th{white-space:normal}.dossier p,.dossier li{max-width:90ch}'
             '.flow span{display:block;color:var(--mute)}</style>')
h = h.replace('</style>', '</style>' + extra_css, 1)
js = (V4 / 'dashboard' / 'v4tabs.js').read_text(encoding='utf-8').replace('__DATA4__', json.dumps(D, ensure_ascii=False).replace('</', '<\\/'))
marker = 'tabs();R[cur]();'
assert h.count(marker) == 1, 'injection marker not unique'
h = h.replace(marker, js + '\n' + marker)
OUT_HTML.write_text(h, encoding='utf-8')
print('wrote', OUT_HTML, round(len(h) / 1e6, 2), 'MB; loops', D['audits']['loops'], '; dossiers', len(dos))
