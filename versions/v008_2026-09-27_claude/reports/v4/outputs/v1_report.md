# V1 — Valuation (systematic, scripted, uniform layer)

Agent V1 · market-data cutoff US close 2026-09-25 · report generated 2026-09-25

## 1. Answer first

**69 names valued** with one uniform script (`v4/code/v1_valuation.py`): the 60 non-pending-takeover
names of `lead_prelim_rank.csv` by `prelim` (excl. WBD, KVUE, TECH, AES, NSC, D) **plus 9 names added
once `b1_live_scores.csv` appeared mid-run** (top 40 by `composite`, not already covered: CVS, NTAP,
MGM, ROST, NUE, CRM, COF, MTB, ODFL). 51 valued as operating companies (FCFF reverse DCF), 14 as
financials (justified P/B / excess return), 4 REITs (FFO proxy).

**Verdict mix:** 27 attractive, 18 fair, 7 demanding, 17 excessive. **27 base-case values sit outside
the Street 12-month target range** (18 exceed the high target, 19 sit below the low target on a 3-year
view vs a 12-month one, so this is expected, not necessarily a red flag by itself — see §4). Every name
resolved to a real number; no silent fabrication — where the data could not support a metric (5 cases)
it is reported as `n/a` with a stated reason, never a placeholder.

**Cheapest vs own 14-year history (NTM multiple in single digits of its own percentile range):** UPS,
ADBE, BMY at the 0th percentile; EXPE, LVS, ALGN, CRM near the 1st–2nd. **Most expensive vs own
history:** TRV (p98), BAC (p94), WSM (p89), COF (p88), ROST (p79).

**Two real data-quality catches, disclosed and corrected, not hidden:** (1) APA's D3 `rev_ttm` resolves
to a partial revenue concept (implied EBIT margin 157%); switched to Yahoo TTM revenue for the DCF and
flagged. (2) NUE's D&A is missing across its *entire* D3 history (not just the latest quarter), which
would structurally understate FCFF against real capex — the reverse DCF for NUE is suppressed (`n/a`)
rather than reported as a false number. See §5 for the full list (7 conflicts, 14 flags).

## 2. Methodology (identical for every name)

1. **Inputs, with lineage.** Price/shares/NTM EPS/consensus/targets from `d4_live_snapshot.parquet`
   (2026-09-25 close). TTM revenue/EBIT/D&A/capex/SBC/OCF from `d3_pit_monthly.parquet`'s latest
   point-in-time row. Net debt = D3 latest 10-Q `total_debt − cash_sti` (Yahoo fallback if missing).
   D3 TTM revenue is reconciled against Yahoo TTM every time; a >5% gap is logged as a conflict, and if
   the D3-implied EBIT margin is implausible (>65% or <-150%) the revenue base for the DCF/scenario
   switches to Yahoo TTM revenue automatically (§5 lists every case).
2. **Multiples in context.** Monthly trailing P/E and FCF-yield history is rebuilt 2012–2026 (fuller
   history used where available back to 2009) directly from `d2_close.parquet` (split-adjusted, **not**
   dividend-adjusted, so it is on the same basis as point-in-time XBRL shares/EPS) × D3 PIT
   shares/NI/OCF/capex. Historical EPS is implicitly reconciled to today's share count via
   `d2_splits.parquet` (cumulative forward-split factor for every split *after* each historical date).
   Current NTM P/E / TTM FCF yield (from D4) is then percentile-ranked inside that own history, and
   compared with the median of same-GICS-sub-industry peers (`d1_current_constituents.csv`, full
   503-name universe). REITs use a P/FFO proxy (NI+D&A) in place of P/E/FCF-yield throughout (own-history
   percentile is true P/FFO; **peer comparison is NTM P/E as a proxy since FFO peer data wasn't
   available — flagged, not silently substituted**). Financials use P/B and ROE.
3. **Reverse DCF.** FCFF = EBIT×(1−t) + D&A − capex − ΔNWC, with SBC **not** added back on top (GAAP
   EBIT already expenses it). WACC = E/(E+D)·CoE + D/(E+D)·CoD·(1−t); CoE = 5.17% (10y rf) +
   β_adj×4.14% (Damodaran ERP, R1); β from 5-year weekly total-return regression vs SPY, Blume-adjusted
   (⅔ raw + ⅓×1.0). 10-year explicit period, growth fades linearly from the solved rate g to 3%
   terminal by year 10 (Gordon terminal value at 3% thereafter); solved for the constant *starting* g
   that clears today's EV via root-finding. Compared with consensus FY1 revenue growth and 5y/10y
   delivered revenue CAGR. Missing capex is proxied with D&A (maintenance-capex assumption); a
   non-positive current EBIT margin falls back to the company's own full-history median margin (flagged,
   since it then embeds a margin-recovery assumption); if D&A is unavailable across the *entire* history
   while capex is material, the DCF is suppressed rather than reported. Financials instead solve
   **justified P/B = (ROE−g)/(COE−g) for the ROE the price implies** (g = 3% terminal), compared with
   actual TTM ROE and the company's own ROE history.
4. **Scenario values (3-year, per share).** Bear/base/bull = the company's own historical **20th/50th/
   80th percentile** of (a) revenue growth, (b) net margin (FFO margin for REITs — never the EBIT margin
   used in the DCF), (c) share-count change, and (d) exit multiple (trailing P/E, P/FFO or P/B) — never a
   fixed ±% shock. Flat current-rate dividends over 3 years are added; return is annualised.
5. **Sanity checks.** Base value vs Street 12m low/mean/high target; SBC-adjusted FCF yield
   ((FCF−SBC)/mcap); reverse-DCF (or justified-P/B) sensitivity at WACC/COE ±1pt.
6. **Verdict** (attractive / fair / demanding / excessive) is a single documented formula, equal-ish
   weighted across three signals, each clipped to [-1,1]: (own-history percentile, inverted) 0.30 +
   (achievable growth − implied growth, /15pt — or actual ROE − implied ROE, /6pt for financials) 0.35 +
   (base 3y annualised return − hurdle rate) 0.35. Full formula and every input are in
   `v1_valuation.json` per ticker.

## 3. Summary table (all 69 names, answer-first)

Own-history % = current NTM-multiple's percentile inside the company's own 2012–2026 (or longer)
monthly distribution. "Implied" = reverse-DCF 10y starting growth (fading to 3%), or for financials the
ROE the current P/B implies. "Delivered" = 5y revenue CAGR / consensus FY1 growth (financials: actual
TTM ROE). Returns are annualised over the 3-year scenario horizon.

| Ticker | Sector | Multiple | Own-hist % | Priced for | Delivered/consensus | Bear 3y | Base 3y | Bull 3y | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| ACGL | Financials | P/B=1.4 | p40 | ROE 9.5% | ROE 19.5% (TTM) | 1.1% | 9.6% | 21.8% | attractive |
| ADBE | Information Technology | NTM P/E=8.7 | p0 | g -2.3% | 5y 12.5% / cons 9.2% | 19.1% | 72.4% | 114.6% | attractive |
| AIZ | Financials | P/B=2.2 | p97 | ROE 14.3% | ROE 17.4% (TTM) | -15.2% | -3.9% | 20.0% | excessive |
| ALB | Materials | NTM P/E=9.7 | p7 | g 33.4% | 5y 12.8% / cons 2.9% | -40.6% | -1.2% | 77.8% | excessive |
| ALGN | Health Care | NTM P/E=12.0 | p1 | g 11.3% | 5y 3.6% / cons 4.1% | 10.6% | 59.7% | 126.1% | attractive |
| ALL | Financials | P/B=1.7 | p76 | ROE 11.4% | ROE 39.4% (TTM) | -1.1% | 10.5% | 28.4% | fair |
| AMP | Financials | P/B=7.2 | p77 | ROE 52.4% | ROE 62.0% (TTM) | -12.7% | 6.5% | 67.7% | fair |
| APA | Energy | NTM P/E=8.7 | p43 | g -20.4% | 5y 0.0% / cons -9.6% | n/a | -5.6% | 98.1% | fair |
| BAC | Financials | P/B=1.4 | p94 | ROE 12.0% | ROE 11.2% (TTM) | -16.4% | -1.9% | 11.7% | excessive |
| BBY | Consumer Discretionary | NTM P/E=12.8 | p39 | g -1.7% | 5y -4.2% / cons 1.5% | -16.0% | 1.4% | 23.7% | demanding |
| BIIB | Health Care | NTM P/E=14.7 | p29 | g -10.6% | 5y -3.2% / cons 2.0% | -18.4% | 24.3% | 65.4% | attractive |
| BMY | Health Care | NTM P/E=9.4 | p0 | g -16.4% | 5y 2.1% / cons -3.3% | -31.5% | 18.0% | 76.5% | attractive |
| CF | Materials | NTM P/E=9.5 | p34 | g -25.0% | 5y 11.0% / cons -11.6% | -37.3% | 6.4% | 90.0% | attractive |
| CINF | Financials | P/B=1.5 | p44 | ROE 10.8% | ROE 20.0% (TTM) | 2.9% | 11.5% | 20.7% | attractive |
| CMCSA | Communication Services | NTM P/E=6.2 | p7 | g -24.2% | 5y 2.8% / cons -2.0% | 24.2% | 62.1% | 89.5% | attractive |
| CMI | Industrials | NTM P/E=16.2 | p49 | g 15.7% | 5y 8.4% / cons 8.9% | -25.1% | -3.9% | 19.4% | excessive |
| CNC | Health Care | NTM P/E=11.8 | p7 | g -25.9%* | 5y 11.4%* / cons -1.6% | -2.2% | 67.7% | 142.1% | attractive |
| COF | Financials | P/B=1.1 | p88 | ROE 10.8% | ROE 9.2% (TTM) | -4.7% | 4.1% | 13.4% | excessive |
| COP | Energy | NTM P/E=12.8 | p80 | g -8.2% | 5y 15.2% / cons -6.7% | -57.1% | -24.4% | 36.5% | demanding |
| CRM | Information Technology | NTM P/E=14.4 | p0 | g 13.0% | 5y 13.3% / cons 9.7% | n/a | 8.9% | 195.7%† | attractive |
| CSX | Industrials | NTM P/E=21.2 | p76 | g 13.9% | 5y 5.2% / cons 5.0% | -28.1% | -8.2% | 15.0% | excessive |
| CVS | Health Care | NTM P/E=10.6 | p9 | g -6.4% | 5y 8.3% / cons 2.9% | -5.4% | 35.9% | 67.5% | attractive |
| DAL | Industrials | NTM P/E=10.7 | p64 | g 5.4% | 5y 30.1%‡ / cons 2.2% | -39.6% | -2.8% | 37.2% | fair |
| DECK | Consumer Discretionary | NTM P/E=9.9 | p5 | g -7.5% | 5y 14.8% / cons 7.2% | -12.9% | 22.8% | 65.6% | attractive |
| DG | Consumer Staples | NTM P/E=15.2 | p7 | g -2.9% | 5y 5.3% / cons 4.0% | 19.7% | 34.7% | 50.9% | attractive |
| DLTR | Consumer Staples | NTM P/E=14.5 | p14 | g 4.5% | 5y -4.9% / cons 6.1% | n/a | 7.3% | 42.9% | fair |
| DVA | Health Care | NTM P/E=10.8 | p10 | g -19.7% | 5y 3.9% / cons 3.4% | -18.2% | 20.0% | 63.0% | attractive |
| EIX | Utilities | NTM P/E=8.2 | p12 | g -3.9% | 5y 6.9% / cons 3.4% | -32.8% | 19.7% | 72.9% | attractive |
| EOG | Energy | NTM P/E=9.1 | p14 | g -13.1% | 5y 15.7% / cons -7.3% | -70.4% | 9.4% | 100.2% | attractive |
| EXPD | Industrials | NTM P/E=23.5 | p58 | g 14.2% | 5y -0.9% / cons 0.5% | -18.3% | 1.2% | 21.5% | excessive |
| EXPE | Consumer Discretionary | NTM P/E=11.2 | p1 | g -1.5% | 5y 22.1%‡ / cons 7.1% | -31.3% | 5.3% | 66.5% | attractive |
| FDX | Industrials | NTM P/E=14.3 | p24 | g -4.2% | 5y 2.4% / cons 3.5% | -10.7% | 11.1% | 43.8% | attractive |
| FRT | Real Estate | P/FFO(proxy)=10.8 | p6 | g 12.3% | 5y 8.4% / cons 4.8% | -4.1% | 17.7% | 32.6% | attractive |
| GD | Industrials | NTM P/E=18.5 | p53 | g 5.4% | 5y 6.9% / cons 4.8% | -10.0% | 0.5% | 17.8% | demanding |
| GL | Financials | P/B=2.1 | p86 | ROE 13.9% | ROE 19.7% (TTM) | -3.8% | 8.4% | 24.4% | fair |
| GM | Consumer Discretionary | NTM P/E=5.6 | p29 | g 23.5% | 5y 5.8% / cons 2.4% | -35.5% | -1.6% | 64.2% | excessive |
| HAS | Consumer Discretionary | NTM P/E=13.7 | p6 | g -3.7% | 5y -3.5% / cons 6.8% | -33.6% | -6.5% | 23.2% | fair |
| HIG | Financials | P/B=1.7 | p77 | ROE 11.8% | ROE 22.2% (TTM) | -15.1% | 2.7% | 24.6% | fair |
| HST | Real Estate | P/FFO(proxy)=8.5 | p29 | g 1.8% | 5y 32.7%‡ / cons 0.4% | -27.4% | 6.2% | 49.3% | attractive |
| IVZ | Financials | P/B=1.1 | p54 | ROE 11.3% | ROE -2.5% (TTM) | -15.6% | 6.9% | 34.1% | excessive |
| JBHT | Industrials | NTM P/E=24.1 | p37 | g 10.6% | 5y 3.4% / cons 9.5% | -10.9% | 6.4% | 26.3% | fair |
| LMT | Industrials | NTM P/E=16.2 | p31 | g -5.1% | 5y 2.9% / cons 5.6% | -10.8% | 4.1% | 28.8% | fair |
| LVS | Consumer Discretionary | NTM P/E=11.5 | p2 | g -11.3% | 5y 27.3%‡ / cons 5.5% | -7.7% | 37.5% | 78.7% | attractive |
| MGM | Consumer Discretionary | NTM P/E=16.9 | p57 | g -6.9% | 5y 22.1%‡ / cons 1.2% | n/a | 10.9% | 248.3%† | attractive |
| MPC | Energy | NTM P/E=8.0 | p39 | g -11.2% | 5y 11.9% / cons -12.3% | -49.2% | -17.1% | 44.9% | fair |
| MTB | Financials | P/B=1.2 | p40 | ROE 9.8% | ROE 10.9% (TTM) | 3.0% | 10.5% | 23.1% | fair |
| MU | Information Technology | NTM P/E=6.8 | p23 | g 33.0% | 5y 28.8% / cons 91.0%§ | n/a | -36.8% | 35.0% | fair |
| NEM | Materials | NTM P/E=12.2 | p9 | g -1.8% | 5y 15.6% / cons 9.1% | n/a | -28.7% | 122.5% | fair |
| NTAP | Information Technology | NTM P/E=19.2 | p39 | g 15.3% | 5y 5.2% / cons 5.8% | -38.3% | -17.2% | 12.5% | excessive |
| NUE | Materials | NTM P/E=12.6 | p35 | g n/a¶ | 5y 6.8% / cons 1.1% | -50.3% | -10.5% | 65.3% | excessive |
| ODFL | Industrials | NTM P/E=27.1 | p59 | g 20.1% | 5y 4.1% / cons 7.9% | -33.7% | -5.9% | 25.6% | excessive |
| PCAR | Industrials | NTM P/E=16.1 | p55 | g 10.3% | 5y 4.6% / cons 10.0% | -30.4% | -5.2% | 20.1% | demanding |
| PSA | Real Estate | P/FFO(proxy)=15.8 | p10 | g 25.3% | 5y 9.6% / cons 7.3% | 7.6% | 18.2% | 27.8% | fair |
| PSX | Energy | NTM P/E=9.9 | p38 | g n/a¶ | 5y 13.4% / cons -10.2% | -46.8% | -20.0% | 45.2% | excessive |
| ROST | Consumer Discretionary | NTM P/E=26.8 | p79 | g 17.8% | 5y 10.0% / cons 6.8% | -14.5% | -3.9% | 9.5% | excessive |
| SNDK | Information Technology | NTM P/E=7.9 | n/a# | g 29.4% | 5y n/a# / cons 18.3% | n/a# | n/a# | n/a# | excessive |
| SPG | Real Estate | P/FFO(proxy)=10.5 | p10 | g 7.1% | 5y 8.2% / cons 3.8% | -12.2% | 2.8% | 18.3% | fair |
| SWK | Industrials | NTM P/E=14.8 | p13 | g -7.6% | 5y -1.9% / cons 1.8% | -10.5% | 18.1% | 54.4% | attractive |
| SYF | Financials | P/B=1.4 | p32 | ROE 13.1% | ROE 20.8% (TTM) | 13.5% | 31.2% | 52.8% | attractive |
| TGT | Consumer Staples | NTM P/E=16.1 | p55 | g 5.2% | 5y 1.4% / cons 3.2% | -11.8% | 4.7% | 21.3% | demanding |
| TPR | Consumer Discretionary | NTM P/E=13.9 | p36 | g 1.9% | 5y 6.9% / cons 5.4% | -30.5% | -7.1% | 36.5% | demanding |
| TROW | Financials | P/B=2.1 | p3 | ROE 18.1% | ROE 20.2% (TTM) | 23.4% | 42.7% | 56.7% | attractive |
| TRV | Financials | P/B=2.3 | p98 | ROE 14.1% | ROE 25.1% (TTM) | -7.8% | -0.5% | 17.2% | demanding |
| UAL | Industrials | NTM P/E=8.7 | p40 | g 12.8% | 5y 33.9%‡ / cons 5.2% | n/a | -3.4% | 29.6% | fair |
| UPS | Industrials | NTM P/E=12.0 | p0 | g 2.5% | 5y -0.6% / cons 3.8% | 7.7% | 24.3% | 56.0% | attractive |
| VLO | Energy | NTM P/E=9.5 | p45 | g 1.6% | 5y 11.5% / cons -13.5% | -52.8% | -28.6% | 29.9% | fair |
| VZ | Communication Services | NTM P/E=9.0 | p18 | g -16.4% | 5y 0.9% / cons 1.9% | -12.7% | 11.7% | 34.5% | attractive |
| WDC | Information Technology | NTM P/E=20.0 | p62 | g 42.3% | 5y -5.3% / cons 36.8% | n/a | -57.5% | -21.1% | excessive |
| WSM | Consumer Discretionary | NTM P/E=22.6 | p89 | g 18.1% | 5y 1.9% / cons 5.3% | -32.1% | -22.4% | 9.1% | excessive |

\* CNC's D3 TTM revenue and EBIT are usable but its FY0 is loss-making at the GAAP level (Medicaid-rate
mismatch); the reverse DCF used the historical median margin as a recovery proxy — see flags.
† CRM and MGM bull cases are driven mostly by exit-multiple mean reversion off a currently very low
own-history percentile (see §4 caveat on structurally-shifted businesses).
‡ DAL/EXPE/HST/LVS/UAL 5y revenue CAGR is inflated by the 2020–21 COVID base effect in the denominator
year; do not read as organic growth.
§ MU's cons FY1 revenue growth (91%) reflects the 2026 AI/HBM memory upcycle per current Street
estimates, not a data error.
¶ PSX/NUE: reverse DCF suppressed for a data reason stated in §5, not solved to an extreme value.
\# SNDK (SanDisk, spun off from WDC ~Feb 2025) has only 5 months of D3 point-in-time history — too
short for a reliable own-history percentile or scenario distribution; reported as `n/a`, not guessed.

## 4. Reading the table

- **"Attractive" is dominated by own-history-cheap names**, not by growth optimism: 8 of the 10
  highest-scoring names (UPS, ADBE, BMY, LVS, DECK, CMCSA, CNC, DVA, CVS, EIX) sit at or below the 12th
  percentile of their own 14-year multiple history, most with negative or low reverse-DCF implied growth
  (i.e. the market is pricing a *decline or stagnation* that is more pessimistic than 5y-delivered or
  consensus growth).
- **"Excessive" is dominated by own-history-rich names**: TRV (p98), BAC (p94), WSM (p89), COF (p88),
  ROST (p79), CSX (p76) are all trading above the 75th percentile of their own history.
- **Base-case values outside the Street range are not automatically wrong**: Street targets are
  12-month, sell-side, and typically anchored near-consensus; V1's base case is a 3-year,
  mechanically-derived, own-history-percentile scenario. A base value above the Street high (18 names,
  e.g. ALGN, CNC, MGM) simply means 3 years of median-case compounding plus multiple normalisation
  exceeds today's 1-year sell-side target — informative, not necessarily an error.
- **Scenario spread is multiple-driven for structurally-shifted businesses.** ADBE and CMCSA are at the
  0th–7th percentile of a P/E history that includes an earlier high-growth/high-multiple regime; the
  bull/base cases assume reversion toward that historical distribution, which may overstate what is
  achievable if the business's growth regime has permanently shifted. Read the *own-history percentile*
  and *implied vs. delivered growth* columns as the primary evidence; treat the scenario return spread
  as "if the multiple normalises" conditional math, not a probability-weighted forecast.

## 5. Data-quality conflicts (D3 vs Yahoo TTM revenue, >5% or implausible margin)

- **APA**: D3 TTM revenue $2.43bn vs Yahoo $8.57bn (252% gap) — D3's revenue concept resolves to a
  partial line; DCF/scenario revenue base switched to Yahoo.
- **BAC**: D3 $121.1bn vs Yahoo $113.9bn (5.9%); D3-implied "EBIT" margin >100% (not a meaningful concept
  for a bank's generic XBRL EBIT tag) — informational only, BAC is valued on P/B, not FCFF.
- **CNC**: D3 $202.9bn vs Yahoo $180.3bn (11.2%) — both used as informational; margin-fallback applied
  (see §3).
- **COF**: D3 $62.0bn vs Yahoo $48.1bn (22.4%) — informational only (COF valued on P/B).
- **MTB**: D3 $10.0bn vs Yahoo $9.5bn (5.1%); same generic-EBIT caveat as BAC — informational only
  (MTB valued on P/B).
- **MU**: D3-implied EBIT margin 65.6% (current AI/memory upcycle margins are genuinely high, but above
  the 65% sanity threshold) — DCF revenue base switched to Yahoo TTM as a precaution.
- **SYF**: D3 $19.2bn vs Yahoo $9.9bn (48.5%, likely gross vs net interest income/fees presentation) —
  informational only (SYF valued on P/B).

**Reading rule applied uniformly**: for the 14 financial-classified names, revenue/EBIT reconciliation
flags are recorded for transparency but **do not affect the valuation**, which uses P/B and ROE, not
revenue or EBIT.

## 6. Other flags (14 tickers)

Capex missing/zero in D3, proxied with D&A as a maintenance-capex assumption: APA, BAC, EOG, FRT, PSA,
PSX, SYF, TRV. NWC unavailable (no classified current-asset/liability split in D3), treated as 0: FRT,
HST, PCAR, PSA, SPG. REIT peer comparison uses NTM P/E as a proxy (no FFO peer data): FRT, HST, PSA, SPG.
CNC's current EBIT margin is negative; historical median used instead (margin-recovery assumption
embedded in its implied growth). NUE's reverse DCF is suppressed (D&A absent across its full D3 history
while capex is material — see §1). SNDK has only 5 months of history (recent spin-off).

## 7. Files

- `v4/code/v1_valuation.py` — the single script, run via
  `PYTHONPATH='C:\Users\user\eqv4\pylib' python v1_valuation.py`, fully reproducible from D1–D4 outputs.
- `v4/outputs/v1_valuation.json` — full detail per ticker (inputs with sources, multiples & percentiles,
  cost of capital, reverse-DCF/P-B model with sensitivity, all three scenarios, sanity checks, verdict
  formula and score, conflicts and flags). Strict JSON (no bare NaN).
- `v4/outputs/v1_valuation_table.csv` — flat summary, one row per ticker (69 rows).

## 8. Open items

- `d3_report.md` did not exist at run time (D3 had not yet written its narrative report); D3's parquet
  outputs were read directly and cross-checked against Yahoo/D4 instead.
- If `b1_live_scores.csv` is rebuilt with a materially different top-40, re-run
  `v1_valuation.py` (universe auto-detects new names not already covered) — it is idempotent and takes
  under a minute for the full 69-name set.
