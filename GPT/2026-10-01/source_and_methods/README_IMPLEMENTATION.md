# GPT methodology implementation and reproducibility

`methodology_v2.py` contains three isolated, read-only primitives: a trailing-only historical share/split repair, corrected covariance shrinkage scaling, and deterministic analyst-verdict precedence from explicit approved records. It does not replace the original B1 or B2 engines and does not issue a recommendation.

The recommended reproducible command on this host is:

```powershell
& 'GPT\2026-10-01\source_and_methods\run_portable_tests.ps1'
```

The launcher uses the workspace's bundled Python 3.12 with pandas/numpy and **no pyarrow requirement**. `fixtures/` holds gzip CSV derivatives of the archived B1 panel, splits and the 20-stock return window. `fixtures/manifest.json` records source and fixture SHA-256 hashes, vintage, row counts and tickers. The tests verify those hashes and also verify the source Parquet bytes when present; they do not need to parse Parquet. On 1 October 2026, all **six tests passed** in **29.618 seconds** with bundled Python, exit code zero. `validate_methodology_v2.py` also passed with that runtime and wrote the exact counts to `methodology_v2_validation.json`.

The original research runtime can also read the full Parquet source directly:

```powershell
$env:PYTHONPATH='C:\Users\user\eqv4\pylib'
& 'C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe' 'GPT\2026-10-01\source_and_methods\make_portable_fixtures.py'
```

That Python 3.11 environment includes the compiled `pyarrow` package used to derive the portable fixtures. The bundled Python is 3.12; setting its `PYTHONPATH` to the 3.11 package directory breaks compiled NumPy imports. The launcher clears any inherited `PYTHONPATH` for its child commands and restores it afterward. The full-Parquet derivation and the portable tests have distinct scopes: the derivation checks and exports the original archive; the portable tests verify the frozen derived rows and numerical behavior without an external package installation.

Validation shows 90 changed split decisions, including 78 within the headline scored period, and separately rejects 16 future-dated share observations. Corrected covariance shrinkage is 0.03758 and yields 13.335% annual volatility on the archived 754-day, 20-stock diagnostic window, near the 13.539% sample estimate. These are primitive-level checks. **No full historical factor reranking, trade simulation or CAGR recalculation was performed.** Historical FRT verdict summaries lack the required approval metadata; the new selector will refuse to infer it from modification times.
