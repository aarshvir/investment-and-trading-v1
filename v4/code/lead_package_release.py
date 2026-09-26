"""Lead: build the complete v4 release package for the shared release tool (tools/publish_research_release.py).

The ZIP contains the whole v4 workstream under the prefix 'v4/' (report, dashboard, code, data, dossiers, outputs, audit
loops, prompts, state, runbook, requirements), minus caches. Convenience copies of FINAL_REPORT.md and HANDOFF_v4.md are
added under v4/outputs/release_copies/ so the publisher extracts them as readable reports. Usage:
    python lead_package_release.py            -> writes v4/release/Claude_v4_Research_Release_<date>.zip and prints its sha256
The publisher itself is run separately (see RESEARCH_VERSIONING.md) so the release notes can be reviewed first."""
import datetime, hashlib, pathlib, sys, zipfile

V4 = pathlib.Path(__file__).resolve().parents[1]
ROOT = V4.parent
OUTDIR = V4 / 'release'
SKIP_DIRS = {'__pycache__', 'release', '.pytest_cache'}
SKIP_SUFFIX = {'.pyc', '.lock', '.tmp'}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    sys.path.insert(0, str(V4 / 'code'))
    from lead_guard import check_build_fresh
    built = check_build_fresh()                     # never package a stale build
    from lead_verify_gate import unverified
    _u = unverified()                               # never package with an unchecked or uncorrected holding
    if _u:
        sys.exit('verification gate OPEN: ' + '; '.join(f'{t}: {w}' for t, w in _u))
    OUTDIR.mkdir(exist_ok=True)
    day = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4))).date().isoformat()
    z = OUTDIR / f'Claude_v4_Research_Release_{day}.zip'
    if z.exists():
        sys.exit(f'{z} already exists; never overwrite a package - rename or remove it deliberately first')
    n = 0
    with zipfile.ZipFile(z, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for p in sorted(V4.rglob('*')):
            rel = p.relative_to(V4)
            if p.is_dir() or any(part in SKIP_DIRS for part in rel.parts) or p.suffix in SKIP_SUFFIX:
                continue
            zf.write(p, arcname=str(pathlib.PurePosixPath('v4', *rel.parts)))
            n += 1
        for name in ('FINAL_REPORT.md', 'HANDOFF_v4.md', 'STATE.md', 'README_RUN.md'):
            zf.write(V4 / name, arcname=f'v4/outputs/release_copies/{name}')
    with zipfile.ZipFile(z) as zf:
        bad = zf.testzip()
    if bad:
        sys.exit(f'integrity check failed at {bad}')
    print({'package': str(z.relative_to(ROOT)), 'files': n, 'bytes': z.stat().st_size, 'sha256': sha(z), 'portfolio_build': built})


if __name__ == '__main__':
    main()
