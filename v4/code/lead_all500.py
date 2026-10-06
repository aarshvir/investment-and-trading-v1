"""All-500 register (owner request, 5 Oct 2026: a deep assessment of every S&P 500 company, visible, not just the holdings).

One row per company from the build candidates and each company's full-diligence summary: verdict, price-implied growth vs
the analyst's base case, base-case 3-year return, one-line thesis, first kill criterion, eligibility and the reason a
name is or is not held, plus the independent-verification status (DA/DV fact-checks, mechanical checks). Writes
outputs/all500_register.json (dashboard tab "All 500") and outputs/all500_register.md (readable table, linked from §6)."""
import json, glob, pathlib, re
V4 = pathlib.Path(__file__).resolve().parents[1]; O = V4 / 'outputs'
B = json.loads((O / 'lead_portfolio_build.json').read_text(encoding='utf-8'))
held = set(B['selected']); W = B.get('weights') or {}

summ = {}
for f in glob.glob(str(O / '[Ff]*_summary.json')):
    try:
        d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    except Exception:
        continue
    T = d.get('tickers', d); it = T.items() if isinstance(T, dict) else [(x.get('ticker'), x) for x in T]
    for t, x in it:
        if isinstance(x, dict) and 'verdict' in x:
            prev = summ.get(t)
            if prev is None or pathlib.Path(f).stat().st_mtime >= prev[0]:
                summ[t] = (pathlib.Path(f).stat().st_mtime, x)
norm = json.loads((O / 'lead_implied_normalization.json').read_text(encoding='utf-8')).get('tickers', {})

checked = {}
for f in glob.glob(str(O / 'd[av][0-9]*_factcheck.json')) + glob.glob(str(O / 'dv' / 'dv*_factcheck.json')):
    src = pathlib.Path(f).name.split('_')[0].upper()
    for x in json.loads(pathlib.Path(f).read_text(encoding='utf-8')).get('facts', []):
        e = checked.setdefault(x.get('ticker'), {}).setdefault(src, [0, 0]); e[0] += 1; e[1] += str(x.get('status', '')).upper() == 'FAIL'

rows = []
for c in B['candidates']:
    t = c['t']; x = (summ.get(t) or (0, {}))[1]
    vv = x.get('valuation_view_vs_v1') or {}
    imp = vv.get('implied_vs_base') or (norm.get(t) or {}).get('implied_vs_base') or c.get('implied') or ''
    sc = x.get('scenario_returns_3y') or {}
    base = sc.get('base') if isinstance(sc.get('base'), (int, float)) else (c.get('base') if isinstance(c.get('base'), (int, float)) and c.get('base') == c.get('base') else None)
    kc = x.get('kill_criteria') or []
    dossier = (V4 / 'dossiers' / f'{t}.md').exists()
    status = 'HELD' if t in held else ('eligible, not held' if c.get('eligible') else 'not eligible')
    rows.append({'t': t, 'name': c.get('n'), 'sector': c.get('s'), 'verdict': x.get('verdict') or c.get('verdict') or '–',
                 'implied_vs_base': imp, 'base_3y': base, 'thesis': (x.get('thesis_one_line') or '').strip(),
                 'first_kill': (kc[0] if kc else ''), 'status': status, 'weight': W.get(t), 'why': c.get('why'),
                 'dossier': dossier, 'checks': {k: {'facts': v[0], 'fails': v[1]} for k, v in (checked.get(t) or {}).items()}})
order = {'HELD': 0, 'eligible, not held': 1, 'not eligible': 2}
rows.sort(key=lambda r: (order[r['status']], -(r['weight'] or 0), r['t']))
(O / 'all500_register.json').write_text(json.dumps({'n': len(rows), 'n_dossier': sum(r['dossier'] for r in rows), 'rows': rows}, indent=1, default=str), encoding='utf-8')

md = ['# All S&P 500 companies: verdicts from full diligence', '',
      f"{len(rows)} index lines ({sum(r['dossier'] for r in rows)} with a full dossier; second share classes are judged with their sibling). "
      "Verdict: INCLUDE (full conviction), INCLUDE-SMALL (half conviction), WATCH (good or fair business, price assumes too much or a named risk), REJECT. "
      "Implied vs base: the growth today's price implies against the analyst's evidence-based base case. Research, not advice.", '',
      '| Stock | Sector | Verdict | Implied vs base | Base-case 3-yr return a year | Status | Thesis | First exit trigger |', '|---|---|---|---|---|---|---|---|']
for r in rows:
    b = f"{100 * r['base_3y']:+.0f}%" if isinstance(r['base_3y'], (int, float)) else '–'
    st = r['status'] + (f" ({100 * r['weight']:.1f}%)" if r['weight'] else '')
    clean = lambda s: re.sub(r'\s+', ' ', str(s or '')).replace('|', '/')
    md.append(f"| **{r['t']}** {clean(r['name'])} | {clean(r['sector'])} | {r['verdict']} | {str(r['implied_vs_base']).replace('_', ' ')} | {b} | {st} | {clean(r['thesis'])} | {clean(r['first_kill'])} |")
(O / 'all500_register.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print('all500 register:', len(rows), 'rows;', sum(r['dossier'] for r in rows), 'dossiers')
