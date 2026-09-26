"""Mechanical pre-check of diligence output, run BEFORE the independent DA-series fact-check (A1 loop-5/6 must-fix).

It cannot tell whether a number is true; it flags the patterns behind most errors the DA checks have found:
  1. summary JSON missing verdict / implied_vs_base / scenario_returns_3y (the build silently drops such names);
  2. balance-sheet, debt, cash or capital-ratio statements with no entity scope (consolidated / segment / subsidiary /
     bank / parent) on the same line (GM automotive-vs-consolidated cash; RJF bank-vs-consolidated ratios);
  3. "a year ago" / "YoY" comparisons whose two quarter labels are not four quarters apart (MSCI Q2 2026 vs Q4 2025);
  4. citations of filings by form type with no accession number (the LVS "July 2026 13D/A" that does not exist).
Usage: python code/lead_dossier_precheck.py TICKER [TICKER ...]   (no arguments: every current holding)
Writes outputs/dossier_precheck.json and prints a per-ticker count. Findings are prompts for the fact-checker and the
author, not verdicts."""
import json, glob, pathlib, re, sys
V4 = pathlib.Path(__file__).resolve().parents[1]
SCOPE = re.compile(r'consolidat|segment|subsidiar|standalone|stand-alone|parent|holding compan|bank\b|legal entity|automotive-only|pro rata|share of', re.I)
BS = re.compile(r'\b(net debt|total debt|long-term debt|cash (and|&) (cash equivalents|marketable)|CET1|Tier 1|total capital ratio|leverage ratio|stockholders\'? equity)\b', re.I)
QTR = re.compile(r'\bQ([1-4])[\s\'’-]*(?:FY)?\s*(20\d\d|\d\d)\b')
FORM = re.compile(r'\b(10-K|10-Q|8-K|13D/A|13D|13G|DEF 14A|S-4|20-F|6-K)\b')
ACC = re.compile(r'\b\d{10}-\d{2}-\d{6}\b|accession', re.I)


def qidx(q, y):
    y = int(y); y = y + 2000 if y < 100 else y
    return y * 4 + int(q)


def summary_fields():
    out = {}
    for f in glob.glob(str(V4 / 'outputs' / 'F*_summary.json')):
        try:
            d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
        except Exception:
            continue
        T = d.get('tickers', d); it = T.items() if isinstance(T, dict) else [(x.get('ticker'), x) for x in T]
        for t, x in it:
            if isinstance(x, dict) and 'verdict' in x:
                out[t] = x
    return out


def check(t, S):
    p = V4 / 'dossiers' / f'{t}.md'
    txt = p.read_text(encoding='utf-8') if p.exists() else ''
    body = txt.split('\n## Correction')[0]           # judge the author's text, not later corrections
    f = []
    x = S.get(t)
    _lane = {c['t'] for c in json.loads((V4 / 'outputs' / 'lead_portfolio_build.json').read_text(encoding='utf-8'))['candidates'] if c.get('lane') is True}
    if t not in _lane:
        pass   # model-gated names use V1's valuation and scenarios, so the analyst fields are optional
    elif x is None:
        f.append({'type': 'summary', 'msg': 'no summary JSON entry'})
    else:
        _norm = json.loads((V4 / 'outputs' / 'lead_implied_normalization.json').read_text(encoding='utf-8')).get('tickers', {}) if (V4 / 'outputs' / 'lead_implied_normalization.json').exists() else {}
        if not (x.get('valuation_view_vs_v1') or {}).get('implied_vs_base') and t not in _norm:
            f.append({'type': 'summary', 'msg': 'implied_vs_base missing'})
        if not (x.get('scenario_returns_3y') or {}).get('base') and (x.get('scenario_returns_3y') or {}).get('base') != 0:
            f.append({'type': 'summary', 'msg': 'scenario_returns_3y missing'})
    for i, line in enumerate(body.split('\n'), 1):
        if BS.search(line) and re.search(r'\d', line) and not SCOPE.search(line):
            f.append({'type': 'entity_scope', 'line': i, 'text': line.strip()[:160]})
        if re.search(r'a year ago|year-ago|YoY|year over year', line, re.I):
            qs = [qidx(a, b) for a, b in QTR.findall(line)]
            if len(qs) == 2 and abs(qs[0] - qs[1]) != 4:
                f.append({'type': 'period_label', 'line': i, 'text': line.strip()[:160]})
        if FORM.search(line) and re.search(r'filed|per |source|cited|according', line, re.I) and not ACC.search(line):
            f.append({'type': 'citation', 'line': i, 'text': line.strip()[:160]})
    return f


if __name__ == '__main__':
    tick = sys.argv[1:] or [r['t'] for r in json.loads((V4 / 'outputs' / 'lead_portfolio.json').read_text(encoding='utf-8'))['rows']]
    S = summary_fields(); res = {t: check(t, S) for t in tick}
    (V4 / 'outputs' / 'dossier_precheck.json').write_text(json.dumps(res, indent=1), encoding='utf-8')
    for t, f in res.items():
        c = {}
        for x in f:
            c[x['type']] = c.get(x['type'], 0) + 1
        print(t, c or 'clean')
