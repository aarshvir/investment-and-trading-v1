"""Numeric cross-tie of dossier balance-sheet figures against SEC XBRL (A1 loop-7 must-fix; the PPG long-term-debt
error, GM net cash and RJF parent debt all survived to the adversarial DA check).

For each ticker, pulls the latest quarter-end values of a few load-bearing XBRL concepts from data.sec.gov companyfacts
(cached) and looks in the dossier (author text before any Correction section) for dollar figures on lines naming the same
item. A figure more than 5% away from EVERY XBRL value of that concept in the last 2 years is flagged. It cannot prove a
number wrong (dossiers legitimately use other bases: gross vs net, segment, pro forma); it tells the author and the DA
checker exactly which lines to look at. Usage: python code/lead_xbrl_crosstie.py [TICKER ...] (default: current holdings).
Writes outputs/xbrl_crosstie.json."""
import json, pathlib, re, sys, time, urllib.request
import pandas as pd
V4 = pathlib.Path(__file__).resolve().parents[1]
CACHE = pathlib.Path(r'C:\Users\user\eqv4\cache\crosstie'); CACHE.mkdir(parents=True, exist_ok=True)
UA = 'PersonalEquityResearch research-admin@personal-research.org'
ITEMS = {  # dossier wording -> XBRL concepts
    'long-term debt': ['LongTermDebtNoncurrent', 'LongTermDebtAndCapitalLeaseObligationsNoncurrent'],   # non-current only: 'LongTermDebt' includes the current portion (PPG test)
    'total debt': ['LongTermDebt', 'DebtInstrumentCarryingAmount', 'LongTermDebtAndCapitalLeaseObligations', 'DebtAndCapitalLeaseObligations'],
    'cash and cash equivalents': ['CashAndCashEquivalentsAtCarryingValue', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],
    "stockholders' equity": ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
}
QUARTERLY = {'net income': ['NetIncomeLoss', 'ProfitLoss']}   # duration facts, latest two ~13-week quarters only (TJX test: a prior-year column mislabelled as the latest quarter)


def q_values(fj, concepts):
    import datetime as _dt
    g = fj.get('facts', {}).get('us-gaap', {}); pts = []
    for c in concepts:
        for u in (g.get(c, {}).get('units', {}).get('USD') or []):
            if 'start' in u and u.get('end', '') >= '2025-06-30':
                d = (_dt.date.fromisoformat(u['end']) - _dt.date.fromisoformat(u['start'])).days
                if 80 <= d <= 100:
                    pts.append((u['end'], float(u['val']) / 1e6))
    ends = sorted({e for e, _ in pts})[-1:]
    return [v for e, v in pts if e in ends]


ITEMS.update(QUARTERLY)
PAT = {k: re.compile(k.replace("'", "'?"), re.I) for k in ITEMS}
MONEY = re.compile(r'\$\s?([\d,]+(?:\.\d+)?)\s*(bn|billion|b\b|m\b|mm|million)', re.I)


def cik_of(t):
    m = pd.read_csv(V4 / 'data' / 'd1_cik_map.csv')
    r = m[(m.ticker_current_yahoo == t) & m.cik_valid_to.isna()]
    return int(r.cik.iloc[0]) if len(r) else None


def facts(cik):
    f = CACHE / f'CIK{cik:010d}.json'
    if not f.exists() or time.time() - f.stat().st_mtime > 7 * 86400:
        req = urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json', headers={'User-Agent': UA})
        f.write_bytes(urllib.request.urlopen(req, timeout=60).read()); time.sleep(0.6)
    return json.loads(f.read_text(encoding='utf-8'))


def values(fj, concepts):
    # only the two most recent balance-sheet dates (latest quarter and prior year-end or quarter): an older period's value
    # can coincide with a wrong figure (PPG test: an earlier quarter's debt sat within 5% of the erroneous $6,876m)
    g = fj.get('facts', {}).get('us-gaap', {}); pts = []
    for c in concepts:
        for u in (g.get(c, {}).get('units', {}).get('USD') or []):
            if 'start' not in u and u.get('end', '') >= '2025-06-30':
                pts.append((u['end'], float(u['val']) / 1e6))
    ends = sorted({e for e, _ in pts})[-2:]
    return [v for e, v in pts if e in ends]


def check(t):
    p = V4 / 'dossiers' / f'{t}.md'
    if not p.exists():
        return {'error': 'no dossier'}
    body = p.read_text(encoding='utf-8').split('\n## Correction')[0]
    cik = cik_of(t)
    if not cik:
        return {'error': 'no CIK'}
    fj = facts(cik); flags = []
    for item, concepts in ITEMS.items():
        xv = q_values(fj, concepts) if item in QUARTERLY else values(fj, concepts)
        if not xv:
            continue
        for i, line in enumerate(body.split('\n'), 1):
            if not PAT[item].search(line) or '[Corrected' in line:
                continue
            for m in MONEY.finditer(line):
                _pre = line[max(0, m.start() - 45):m.start()]
                if not PAT[item].search(_pre) or re.search(r'flow|return|dividend|buyback|repurchas|FCF|OCF|free|interest|issu|paid|raised|repaid|redeem|change|increase|decrease|grew|fell|rose', _pre, re.I):
                    continue    # the item must name this figure directly; flows and changes are not balances
                v = float(m.group(1).replace(',', '')); v = v * 1000 if m.group(2).lower() in ('bn', 'billion', 'b') else v
                if v < 50:      # ratios or per-share figures caught by the pattern
                    continue
                best = min(xv, key=lambda x: abs(x - v))
                if abs(best - v) / max(abs(best), 1) > 0.05:
                    flags.append({'item': item, 'line': i, 'dossier_$m': round(v, 1), 'nearest_xbrl_$m': round(best, 1),
                                  'gap_pct': round(100 * (v - best) / max(abs(best), 1), 1), 'text': line.strip()[:150]})
    return {'cik': cik, 'flags': flags}


if __name__ == '__main__':
    tick = sys.argv[1:] or [r['t'] for r in json.loads((V4 / 'outputs' / 'lead_portfolio.json').read_text(encoding='utf-8'))['rows']]
    res = {}
    for t in tick:
        try:
            res[t] = check(t)
        except Exception as e:
            res[t] = {'error': str(e)[:120]}
        print(t, res[t].get('error') or f"{len(res[t]['flags'])} flag(s)")
    (V4 / 'outputs' / 'xbrl_crosstie.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
