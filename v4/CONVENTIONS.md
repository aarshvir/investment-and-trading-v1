# v4 research program — shared conventions (every agent reads this first)

## Purpose
Rebuild the US large-cap equity research ("v3 conviction portfolio", see ../HANDOFF_v3_US_Equity_Conviction_Research.md)
into an institutional-grade, point-in-time, survivorship-aware, independently audited process.
Market-data cutoff: **US close Friday 2026-09-25**. Today is Saturday 2026-09-26. No trades are ever placed.

## Paths
- PROJECT = `C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments`
- V4 = `PROJECT\v4`  (Git Bash: `/c/Users/user/OneDrive/Documents/Projects/Investing and trading/Long-term and mid-term investments/v4`)
  - `v4\code\`     scripts (prefix every file with your agent id, e.g. `d1_membership.py`)
  - `v4\data\`     processed datasets (parquet preferred; csv for small tables) + sidecar `<name>.meta.json`
  - `v4\outputs\`  your report `<agent_id>_report.md` and result json/csv
  - `v4\dossiers\` per-company diligence dossiers (`<TICKER>.md`)
  - `v4\audit\`    auditor reports only
- CACHE (raw downloads, NOT synced to OneDrive) = `C:\Users\user\eqv4\cache\<agent_id>\`
- Legacy v3 bundle (read-only): `PROJECT\equity_project\` (scripts, pickles, info.json, dash*.json)
- Prior external review by another AI (read-only, treat as claims to verify): `PROJECT\review\`

## Python
- Run: `PYTHONPATH='C:\Users\user\eqv4\pylib' python script.py` (Git Bash) or
  `$env:PYTHONPATH='C:\Users\user\eqv4\pylib'; python script.py` (PowerShell). Python 3.11.
- Libraries available: pandas 3.0.6 (copy-on-write, new string dtype), numpy 2.4, scipy 1.17, statsmodels 0.15,
  pyarrow 25, yfinance 1.7 (+curl_cffi), requests, lxml, bs4, openpyxl. Do NOT pip install into other locations.
  If you truly need another package: `python -m pip install --target C:\Users\user\eqv4\pylib <pkg>`.
- Long scripts: run in the foreground with a timeout, write incremental checkpoints to CACHE so re-runs resume.
- Windows paths contain spaces: always quote.

## Data-source etiquette (shared rate limits — several agents run at once)
- SEC (data.sec.gov / www.sec.gov): header `User-Agent: PersonalEquityResearch research-admin@personal-research.org`,
  `Accept-Encoding: gzip, deflate`. Max **4 requests/second per agent**. Retry with backoff on 429/5xx. Cache raw JSON.
- Yahoo (yfinance): max 6 concurrent threads, exponential backoff on errors/429, cache results. Prefer batched `yf.download`.
- Wikipedia/GitHub/Stooq: polite (≤2 req/s), send a descriptive User-Agent.
- Never send the owner's email or personal data to any service.

## Identifiers & conventions
- Tickers: Yahoo style, uppercase, `.`→`-` (BRK-B, BF-B). Keep a column `ticker_orig` if you changed it.
- Dates: ISO `YYYY-MM-DD`; month-end = last trading day of month unless stated.
- Returns: total-return (dividend-adjusted) closes unless stated. Benchmark: SPY total return (adjusted) and ^SP500TR if available.
- Fundamentals: always carry `period_end`, `filed` (SEC filing date = availability date), `form`, `fy`, `fp`, units.
- Point-in-time rule: a fact is usable at date t only if `filed <= t` (for backtests use filed + 1 trading day).
- Missing is MISSING (NaN + reason), never silently zero/median-filled in stored data.

## Output contract for every agent
1. Write `v4\outputs\<agent_id>_report.md`: answer-first summary; what you did; key numbers; validation checks
   performed (with pass/fail counts); known limitations; list of files you produced (with row counts).
2. Every dataset gets `<name>.meta.json`: source URLs, retrieval UTC time, row/column counts, coverage, caveats.
3. Never fabricate a number. If a source is unavailable, say so and continue with what is available.
4. Never modify files owned by another agent or the legacy folders. Only write your own prefixed files.
5. Cite primary sources (URLs) for every factual claim in research reports.
6. Keep final chat reply to the lead short (≤300 words): status, headline numbers, files, open issues.

## Safety
No trades, no account logins, no credentials, no form submissions, no purchases. Research only.
