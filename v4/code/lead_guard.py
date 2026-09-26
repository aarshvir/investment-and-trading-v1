"""Freshness guard (Loop-1 A2 must-fix): every downstream step verifies that the portfolio build still matches the exact
inputs it was built from (sha256 of scores, valuation table, snapshot, calibration, verdict JSONs, dossiers). If any input
changed after the build, publishing stops with an explicit message instead of silently shipping stale numbers."""
import hashlib, json, pathlib

V4 = pathlib.Path(r'C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4')


class StaleBuildError(RuntimeError):
    pass


def check_build_fresh(build_path=V4 / 'outputs' / 'lead_portfolio_build.json'):
    b = json.loads(pathlib.Path(build_path).read_text(encoding='utf-8'))
    man = b.get('input_manifest')
    if not man:
        raise StaleBuildError('portfolio build has no input manifest - re-run lead_build_portfolio.py')
    stale = []
    for m in man:
        p = pathlib.Path(m['path']) if pathlib.Path(m['path']).is_absolute() else V4 / m['path']
        if not p.exists():
            stale.append(f"missing: {m['path']}"); continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        if h != m['sha256']:
            stale.append(f"changed since build: {m['path']}")
    # new verdict files or dossiers that did not exist at build time also make the build stale
    known = {m['path'] for m in man}
    for p in list((V4 / 'dossiers').glob('*.md')) + list((V4 / 'outputs').glob('f*_summary.json')):
        rel = str(p.relative_to(V4))
        if rel not in known:
            stale.append(f"new since build: {rel}")
    if stale:
        raise StaleBuildError('STALE PORTFOLIO BUILD - re-run lead_build_portfolio.py:\n  ' + '\n  '.join(stale))
    return b.get('built')


if __name__ == '__main__':
    print('build fresh as of', check_build_fresh())
