"""Quarter-label check for dossier results tables (A1 loop-10 must-fix; the TJX, PTC and LH errors were rows whose
figures belonged to a different quarter than their label).

For every table row in a dossier whose first cell names a quarter (e.g. "Q2 2026", "2Q'25", "Q3'26") and whose next cell
is a revenue figure, look up the company's SEC XBRL quarterly revenue (duration facts of ~13 weeks) and find which
calendar quarter that revenue value belongs to (the XBRL "frame", e.g. CY2025Q3). Flag the row if the label's quarter
differs from the frame's quarter. Only companies whose fiscal year ends in December are checked, because only for them
does a "Q3 2025" label map one-to-one to calendar Q3; others are listed as not checkable. Usage:
python code/lead_quarter_label_check.py [TICKER ...]   (default: current holdings). Writes outputs/quarter_label_check.json."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import lead_xbrl_crosstie as X
V4 = pathlib.Path(__file__).resolve().parents[1]
REV = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'RevenuesNetOfInterestExpense']
LAB = re.compile(r"^\|\s*\**\s*(?:Q([1-4])\s*[' ]?\s*(?:FY)?\s*'?(\d{2,4})|([1-4])Q\s*'?(\d{2,4}))\b", re.I)
NUM = re.compile(r'\|\s*\$?\s*([\d,]+(?:\.\d+)?)')


def calendar_fy(fj):
    g = fj.get('facts', {}).get('us-gaap', {})
    import datetime as _dt, collections as _c
    ends = []
    for c in REV:
        for u in (g.get(c, {}).get('units', {}).get('USD') or []):
            if 'start' in u and u.get('form') == '10-K':
                d = (_dt.date.fromisoformat(u['end']) - _dt.date.fromisoformat(u['start'])).days
                if 350 <= d <= 380:
                    ends.append(u['end'][5:])
    return bool(ends) and _c.Counter(ends).most_common(1)[0][0] == '12-31'   # annual periods ending 31 Dec


def rev_frames(fj):
    g = fj.get('facts', {}).get('us-gaap', {}); out = []
    for c in REV:
        for u in (g.get(c, {}).get('units', {}).get('USD') or []):
            fr = u.get('frame', '')
            if re.fullmatch(r'CY\d{4}Q[1-4]', fr):
                out.append((float(u['val']) / 1e6, fr))
    return out


def check(t):
    p = V4 / 'dossiers' / f'{t}.md'
    if not p.exists():
        return {'error': 'no dossier'}
    cik = X.cik_of(t)
    if not cik:
        return {'error': 'no CIK'}
    fj = X.facts(cik)
    if not calendar_fy(fj):
        return {'checkable': False, 'reason': 'fiscal year does not end in December; labels are fiscal quarters'}
    frames = rev_frames(fj); flags = []
    for i, line in enumerate(p.read_text(encoding='utf-8').split('\n## Correction')[0].split('\n'), 1):
        if '[Corrected' in line:
            continue
        m = LAB.match(line.strip())
        if not m:
            continue
        q = int(m.group(1) or m.group(3)); y = int(m.group(2) or m.group(4)); y = y + 2000 if y < 100 else y
        n = NUM.search(line[m.end():])
        if not n:
            continue
        v = float(n.group(1).replace(',', ''))
        if v < 50:
            continue
        hits = [fr for val, fr in frames if abs(val - v) / max(abs(val), 1) < 0.002]
        own = [val for val, fr in frames if fr == f'CY{y}Q{q}']   # the SEC figure for the labelled quarter itself
        if hits and own and f'CY{y}Q{q}' not in hits and all(abs(o - v) / max(abs(o), 1) > 0.002 for o in own):   # flag only when the labelled quarter is on file and disagrees (USB test)
            flags.append({'line': i, 'label': f'Q{q} {y}', 'revenue_$m': v, 'xbrl_frame_of_that_value': sorted(set(hits)), 'text': line.strip()[:140]})
    return {'checkable': True, 'flags': flags}


if __name__ == '__main__':
    tick = sys.argv[1:] or [r['t'] for r in json.loads((V4 / 'outputs' / 'lead_portfolio.json').read_text(encoding='utf-8'))['rows']]
    res = {}
    for t in tick:
        try:
            res[t] = check(t)
        except Exception as e:
            res[t] = {'error': str(e)[:120]}
        r = res[t]
        print(t, r.get('error') or ('not checkable (non-December fiscal year)' if not r.get('checkable') else f"{len(r['flags'])} flag(s)"))
    (V4 / 'outputs' / 'quarter_label_check.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
