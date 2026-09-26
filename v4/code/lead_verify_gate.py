"""Verification gate (A2 loop-4/5 must-fix): every holding must have an independent, multi-fact dossier check
(a DA-series fact-check file: outputs/da*_factcheck.json) with every FAIL answered by a dated "Correction" section
in its dossier naming that check, before a release is packaged. `unverified()` returns the holdings that fail the gate;
lead_package_release.py refuses to package while it is non-empty, and Appendix A.5 prints it."""
import json, glob, pathlib, re
V4 = pathlib.Path(__file__).resolve().parents[1]


def coverage():
    cov = {}
    for f in sorted(glob.glob(str(V4 / 'outputs' / 'da[0-9]*_factcheck.json'))):
        src = pathlib.Path(f).name.split('_')[0].upper()
        for x in json.loads(pathlib.Path(f).read_text(encoding='utf-8')).get('facts', []):
            e = cov.setdefault(x.get('ticker'), {}).setdefault(src, {'n': 0, 'fail': 0})
            e['n'] += 1; e['fail'] += x.get('status') == 'FAIL'
    return cov


def unverified():
    rows = json.loads((V4 / 'outputs' / 'lead_portfolio.json').read_text(encoding='utf-8'))['rows']
    cov, out = coverage(), []
    for r in rows:
        t = r['t']; c = cov.get(t)
        if not c:
            out.append((t, 'no independent fact-check')); continue
        d = (V4 / 'dossiers' / f'{t}.md').read_text(encoding='utf-8') if (V4 / 'dossiers' / f'{t}.md').exists() else ''
        for src, e in c.items():
            if e['fail'] and not re.search(r'## Correction[^\n]*' + src, d):
                out.append((t, f'{src} found {e["fail"]} FAIL(s) with no correction in the dossier'))
    # C1 freshness (A1/A3 loop-5): the number-tracing audit must name the content fingerprint of the current build
    b = json.loads((V4 / 'outputs' / 'lead_portfolio_build.json').read_text(encoding='utf-8'))
    c1p = V4 / 'outputs' / 'c1_consistency.json'
    c1 = json.loads(c1p.read_text(encoding='utf-8')) if c1p.exists() else {}
    if c1.get('content_sha256') != b.get('content_sha256'):
        out.append(('C1', 'number-tracing audit does not name the current build content (content_sha256 '
                    + str(b.get('content_sha256'))[:12] + '); re-run C1 last, after the final build'))
    return out


if __name__ == '__main__':
    u = unverified()
    print('verification gate:', 'PASS' if not u else 'OPEN'); [print(' -', t, why) for t, why in u]
