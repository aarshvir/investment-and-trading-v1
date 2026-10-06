"""One-command runner for the v4 pipeline: the canonical run order (the table in README_RUN.md, as code).

Usage (from the v4 folder, Python 3.11.9, libraries pinned in requirements.txt):
    python run_all.py                     # offline re-derivation of every published number: checks + lead stages
    python run_all.py --stages all        # everything from the D1 downloads onward (network; data after 2026-09-25 will differ)
    python run_all.py --stages B1,B1X,B2,V1,lead,checks
    python run_all.py --list              # print the plan without running it

Each script runs from v4/code with PYTHONPATH pointing at the pinned library folder and PYTHONIOENCODING=utf-8.
The run stops at the first failure. The lead stage ends with lead_assemble.py; every downstream lead script calls
lead_guard.check_build_fresh(), so publication stops if any input changed after the portfolio build.
"""
import argparse, os, pathlib, subprocess, sys, time

V4 = pathlib.Path(__file__).resolve().parent
CODE = V4 / 'code'
PYLIB = os.environ.get('EQV4_PYLIB', r'C:\Users\user\eqv4\pylib')
# 5 Oct 2026: Windows Application Control blocks pyarrow's _fs DLL on this machine. A fastparquet folder (whose
# sitecustomize makes it pandas' parquet engine) goes first when present; verified to reproduce v011's risk figures exactly.
if 'EQV4_PYLIB' not in os.environ and os.path.isdir(r'C:\Users\user\eqv4\pylib_fp'):
    PYLIB = r'C:\Users\user\eqv4\pylib_fp' + os.pathsep + PYLIB

STAGES = [   # (stage, scripts in order) - network stages first, offline stages last
    ('D1', ['d1_fetch_sources.py', 'd1_fja.py', 'd1_wiki.py', 'd1_wiki_snapshots.py', 'd1_wiki_reconstruct.py', 'd1_membership.py',
            'd1_sec_fetch.py', 'd1_identity.py', 'd1_cik_sector.py', 'd1_out_current.py']),
    ('D2', ['d2_universe.py', 'd2_download.py', 'd2_build.py', 'd2_validate.py', 'd2_report.py']),
    ('D3', ['d3_universe.py', 'd3_pull.py', 'd3_extract.py', 'd3_lineage.py', 'd3_build_pit.py', 'd3_validate.py']),
    ('D4', ['d4_universe.py', 'd4_fetch_yahoo.py', 'd4_fetch_indep_prices.py', 'd4_fetch_sec.py', 'd4_build_snapshot.py', 'd4_validate.py',
            'd4_events.py', 'd4_changelog.py', 'd4_report.py']),
    ('R', ['r1_base_rates.py', 'r1_cma_scenarios.py', 'r2_implementation_calcs.py', 'r3_ff_factors.py', 'r3_largecap_longonly.py',
           'r3_pit_beat_rates.py', 'r3_stock_base_rates.py', 'r3_confidence_calibration.py', 'r3_build_report.py']),
    ('B1', ['b1_panel.py', 'b1_backtest.py', 'b1_phaseb.py', 'b1_tests.py', 'b1_report.py']),   # b1_sleeve.py is called by b1_phaseb.py
    ('B1X', ['b1x_build.py', 'b1x_backtest.py', 'b1x_live.py', 'b1x_compare.py']),
    ('B2', ['b2_run.py']),
    ('V1', ['v1_valuation.py']),
    ('checks', ['b2_tests.py', 'b1_tests.py', 'lead_check_daily_dd.py']),   # lead_check_risk_contrib.py runs after lead_risk (below)
    ('lead', ['lead_build_portfolio.py', 'lead_risk.py', 'lead_check_risk_contrib.py', 'lead_j_sensitivity.py', 'lead_reconcile_v005.py', 'lead_views.py', 'lead_report_sections.py', 'lead_report_appendix.py', 'lead_all500.py', 'lead_assemble.py']),
]
DEFAULT = ['checks', 'lead']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--stages', default=','.join(DEFAULT), help="comma list of stages, or 'all'")
    ap.add_argument('--list', action='store_true', help='print the plan and exit')
    a = ap.parse_args()
    names = [s for s, _ in STAGES]
    want = names if a.stages == 'all' else [s.strip() for s in a.stages.split(',') if s.strip()]
    bad = [s for s in want if s not in names]
    if bad:
        sys.exit(f'unknown stage(s): {bad}; choose from {names}')
    plan = [(s, f) for s, fs in STAGES if s in want for f in fs]
    for i, (s, f) in enumerate(plan, 1):
        print(f'{i:>2}. [{s}] {f}')
    if a.list:
        return
    env = dict(os.environ, PYTHONPATH=PYLIB, PYTHONIOENCODING='utf-8')
    t0 = time.time()
    for i, (s, f) in enumerate(plan, 1):
        t = time.time()
        print(f'\n=== {i}/{len(plan)} [{s}] {f} ===', flush=True)
        r = subprocess.run([sys.executable, f], cwd=CODE, env=env)
        if r.returncode != 0:
            sys.exit(f'FAILED at [{s}] {f} (exit {r.returncode}); fix and re-run with --stages {s}' + (',' + ','.join(want[want.index(s) + 1:]) if s != want[-1] else ''))
        print(f'--- ok in {time.time() - t:.0f}s', flush=True)
    print(f'\nAll {len(plan)} steps passed in {time.time() - t0:.0f}s. Published files: FINAL_REPORT.md, dashboard/equity_audit_v4.html')


if __name__ == '__main__':
    main()
