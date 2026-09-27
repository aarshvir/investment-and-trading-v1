# X1 cross-workstream verification of v005_2026-09-26_codex

Verifier: X1 (cross-workstream verifier, Claude v4 side). Research only; no files under `versions/` or `review/` were modified.
Scope: `INVESTMENT_DECISION_MEMO.md`, `decision_table.csv`, `scenarios.csv`, `financials.md`, `quality_compounders.md`, `WEEKLY_POLICY_V2.md`, `release_validation.json` from `versions/v005_2026-09-26_codex/reports/review/ready/`, cross-checked against v4's `d2_close.parquet`/`d2_adjclose.parquet`, `v1_valuation_table.csv`, and independent primary sources (SEC EDGAR filings, issuer IR pages, Vanguard/iShares product pages, stockanalysis.com) fetched live via WebFetch/WebSearch.

Summary counts: **26 checked** — CONFIRMED 23, MINOR DIFFERENCE 1, NOT CONFIRMED 1, UNVERIFIABLE 1.

## 1. Reference closes vs v4 D2 daily closes

| Ticker | Memo reference | Date | v4 D2 close | Independent 3rd source | Status |
|---|---|---|---|---|---|
| AMP | $485.15 | 24-Sep | $485.1499938964844 | stockanalysis.com: $485.15 | CONFIRMED |
| PAYX | $101.59 | 24-Sep | $101.58999633789062 | — | CONFIRMED |
| MSFT | $516.05 | 25-Sep | $516.1699829101562 | stockanalysis.com (live refetch): $516.17 | **MINOR DIFFERENCE** |
| NVDA | $224.58 | 24-Sep | $224.5800018310547 | — | CONFIRMED |
| ALLE | $152.48 | 24-Sep | $152.47999572753906 | — | CONFIRMED |
| HIG | $125.69 | 24-Sep | $125.69000244140625 | — | CONFIRMED |

MSFT: the memo calls $516.05 the "reconciled September 25 close." Both v4's D2 close (Yahoo-sourced) and a fresh live fetch of the exact stockanalysis.com history page Codex itself cited show **$516.17**, not $516.05 — a $0.12 (0.02%) gap. Unlike NVDA, AMP-25Sep, HIG-25Sep, AIZ-25Sep and IBKR-25Sep, where Codex explicitly disclosed a header/history-row conflict and picked one side, no such disclosed conflict exists for MSFT — it is presented as settled. Immaterial to the decision (both figures sit far above the $500 "buy below" ceiling), but the "reconciled" language is not supported by any source I could locate (see §5).

## 2. Fund facts

| Claim | Source checked | Result | Status |
|---|---|---|---|
| VUAA ISIN IE00BFMXXD54 | vanguard.co.uk product page | Exact match | CONFIRMED |
| IB01 ISIN IE00BGSF1X88 | ishares.com product page | Exact match | CONFIRMED |
| VUAA expense ratio 0.07% | vanguard.co.uk | Exact match | CONFIRMED |
| IB01 expense ratio 0.07% | ishares.com + justetf.com (2 sources) | Exact match | CONFIRMED |
| IB01 YTM 4.16% as of 24 Sep 2026 | ishares.com | Page literally shows "Weighted Average YTM 24/Sept/2026: 4.16%" | CONFIRMED |
| IB01 effective duration 0.31yr | ishares.com, justetf.com, factsheet PDF | Not displayed on any page I could parse (factsheet PDF was binary/unparseable) | **UNVERIFIABLE** |
| Vanguard look-through NVIDIA 8.08% (8.07902%) | vanguard.co.uk holdings | Exact match: "NVIDIA Corp - 8.08%" | CONFIRMED |
| Vanguard look-through Microsoft 5.69% (5.69335%) | vanguard.co.uk holdings | Exact match: "Microsoft Corp - 5.69%" | CONFIRMED |
| Combined look-through math: NVDA total 2.712%, MSFT total 2.854% at full deployment | Recomputed: 1.5%+15%×8.07902%=2.712%; 2%+15%×5.69335%=2.854% | Reproduces exactly | CONFIRMED |

## 3. Arithmetic recomputation

**Correlated-shock table** — recomputed from stated weights (initial: 15% index/4% direct/81% reserve; full: 15%/10%/75%) and stated shock magnitudes:

| Shock | Computed initial loss | Memo | Computed full loss | Memo | $50k / $100k full loss |
|---|---|---|---|---|---|
| Equity selloff (-30/-40/0) | -6.10% | -6.1% | -8.50% | -8.5% | matches $-4,250 / $-8,500 |
| Severe (-50/-60/-1) | -10.71% | -10.7% | -14.25% | -14.3%* | matches $-7,125 / $-14,250 |
| Tail (-60/-75/-2) | -13.62% | -13.6% | -18.00% | -18.0% | matches $-9,000 / $-18,000 |

*Memo rounds -14.25% to -14.3%; dollar figures use the unrounded -14.25%. All values reconcile exactly. **CONFIRMED.**

**Return-tradeoff CAGR table** — reverse-engineered methodology: geometric (terminal-wealth) blend of index/reserve annual assumptions with each direct stock's own IRR-at-limit-price-after-30%-withholding, weighted by slot sizes (initial: AMP 2%+PAYX 2%; full: +MSFT 2%/NVDA 1.5%/ALLE 1.5%/HIG 1%):

| Case | Memo initial CAGR | Recomputed | Memo full CAGR | Recomputed |
|---|---|---|---|---|
| Bear | 0.6% | 0.62% | -0.2% | -0.19% |
| Base | 4.3% | 4.27% | 4.9% | 4.95% |
| Bull | 6.5% | 6.55% | 8.3% | 8.34% |

All six values reproduce to within 0.05 percentage points (rounding). **CONFIRMED.** (A naive linear/weighted-average blend of the same inputs does *not* reproduce these figures as closely — confirming Codex used proper compounding, not a simple weighted average.)

**AMP/PAYX scenario mechanics** — independently re-solved via Newton's-method IRR and explicit PV discounting:
- AMP base IRR @ $485.15 ref = 14.343% (scenarios.csv: 14.343%) — CONFIRMED
- AMP base IRR @ $500 limit = 13.186% (scenarios.csv: 13.186%) — CONFIRMED
- AMP terminal EPS: 44×1.07³ = 53.9019 (memo: 53.901892) — CONFIRMED
- AMP terminal price: 53.9019×13 = 700.7246 (memo: 700.724596) — CONFIRMED
- AMP max entry @12%: recomputed 515.86 (memo 515.8615) — CONFIRMED
- PAYX base IRR @ $101.59 ref = 13.637% (scenarios.csv: 13.637%) — CONFIRMED
- PAYX base IRR @ $101.80 limit = 13.556% (scenarios.csv: 13.556%) — CONFIRMED
- PAYX bottom-up terminal EPS: ($7.6bn×43.8% − $265m + $30m)×(1−24%)/356m = $6.6047 (memo: $6.60) — CONFIRMED
- PAYX max entry @12%: recomputed 105.928 (memo 105.9278) — CONFIRMED

## 4. AMP / PAYX base-case load-bearing inputs vs SEC filings

**AMP** (SEC EDGAR q1/q2 2026 earnings releases, fetched directly):
- Q1 2026 adjusted diluted EPS $11.26 + Q2 2026 adjusted diluted EPS $11.07 = **$22.33** H1 — exact match to financials.md's "$22.33". CONFIRMED.
- Comerica termination "**$25 million** benefit" to pretax earnings — exact match. CONFIRMED.
- Quarterly dividend "**$1.70** per common share" — exact match ($6.80 annualized). CONFIRMED.
- Q2 diluted share count 92.9m — exact match to the sum-of-parts crosscheck's "92.9m diluted shares". CONFIRMED.
- Normalized $44 base EPS and 7%/yr growth to $53.90 terminal EPS is a traceable, disclosed extension of the confirmed $22.33 H1 (×2, minus the Comerica benefit) — a reasonable, documented normalization, not an unsupported jump.
- **13.0x terminal P/E vs AMP's own 10-year history**: secondary aggregators (fullratio.com, macrotrends) put AMP's 10-year average P/E at ~12.76x, with a 10-year range of roughly 3.7x (2020 COVID-distorted low) to ~27x (2021 high). 13.0x sits almost exactly on the 10-year average and well inside the range. CONFIRMED (reasonable).

**PAYX** (SEC EDGAR FY2026 press release + recent dividend 8-Ks, fetched directly):
- FY2026 adjusted diluted EPS **$5.51** vs GAAP **$4.89** — exact match. CONFIRMED.
- FY2027 guidance **7–9%** adjusted EPS growth — exact match; midpoint recomputes to $5.951 exactly as stated. CONFIRMED.
- Year-1 dividend **$4.76** — matches 4×$1.19, the current quarterly rate declared May/July 2026 (up from $1.08). CONFIRMED.
- FY2029 terminal EPS $6.60 bottom-up build (revenue/margin/interest/tax/shares) reproduces to the cent from disclosed drivers. CONFIRMED.
- **20.0x terminal P/E vs PAYX's own 10-year history**: secondary aggregators show PAYX's 10-year average P/E at ~28–29x with a range of roughly 23.6x (2020 low) to 34.3x (2025 high). A 20.0x terminal multiple sits **below the entire cited 10-year range**, not inside it. **NOT CONFIRMED** as "inside the historical range" — though this makes the model *more* conservative than history, not less, so it does not overstate the valuation; it is a defensible conservatism the memo doesn't flag as being below-range.

**Cross-check with v4's V1 row (AMP only, as instructed):** v4's `v1_valuation_table.csv` shows AMP verdict = "fair", base_ann_return_3y = 0.064809 (**+6.5%/yr**), using a P/B-relative/peer-median methodology (metric P/B 7.19x, peer median 2.75x, wacc/coe 9.87%). This is confirmed as an accurate read of the V1 output. It is a materially more conservative estimate than Codex's DDM/EPS-multiple base case (14.3% at reference, 12.8% at the $500 limit after withholding). Recorded as a cross-workstream methodological disagreement, not resolved here (see disagreements below) — the two models answer related but different questions (relative P/B versus peers vs. absolute three-scenario cash-flow IRR).

## 5. Claims found wrong or overstated

1. **MSFT "$516.05, reconciled September 25 close"** — not reproducible from any source found (v4 D2/Yahoo and a live stockanalysis.com refetch both show $516.17). Calling it "reconciled" implies a resolved conflict; no conflict is disclosed for MSFT the way it is for NVDA/AMP/HIG/AIZ/IBKR on 25-Sep. Immaterial to the buy-below decision. Recommend Codex either show its MSFT source/timestamp or restate as $516.17.
2. **PAYX 20x terminal multiple** is described only as "a 5% earnings yield on modestly growing, recurring revenue" without noting it sits below PAYX's own 10-year trading range (~23.6x–34.3x per secondary aggregators). Not wrong (conservative bias is disclosed generally and is defensible given deceleration/integration risk), but the memo doesn't state that the multiple is below-range, which a reader might wrongly read as a mid-range historical assumption.
3. **Minor observational note (not a primary finding):** financials.md's disclosed AMP 25-Sep conflict ("$497.19/$492.96") does not match either v4's D2 25-Sep close ($493.00) or a live stockanalysis.com refetch ($493.00) today. This does not affect any decision (AMP's reference price is the 24-Sep close, which is solidly confirmed), but suggests the specific 25-Sep figures cited for AMP in financials.md may themselves be stale or mis-transcribed.

No other numerical, sourcing, or arithmetic errors were found. The scenario mechanics, shock-table math, return-tradeoff CAGRs, dividend paths, and normalized EPS builds for AMP and PAYX all reproduce independently from primary SEC filings and from the stated model assumptions.

## Disagreements (recorded, not adjudicated)

- **AMP valuation methodology**: v4/V1 (P/B-relative, peer-median approach) lands on "fair"/+6.5%/yr base; Codex v005 (three-scenario DDM/EPS-multiple IRR) lands on 13–14% base IRR and a BUY NOW call. Both are internally consistent with their own stated methodology and inputs (verified above); the gap is a methodology choice (relative multiple vs. absolute cash-flow scenario), not an arithmetic or sourcing error in either. Flagged for the next release to reconcile explicitly (e.g., state why the absolute DDM basis is preferred over the peer-relative basis, or show both).

## Environment notes

Python 3.11 with pandas/pyarrow (via `PYTHONPATH=C:\Users\user\eqv4\pylib`) was used to read v4's parquet price data; no pandas was available on the bare system path, so PYTHONPATH was required for every invocation. All web verification used WebFetch/WebSearch (loaded via ToolSearch) against the fictional-2026 dataset the workspace already treats as canonical (SEC EDGAR, issuer IR pages, Vanguard/iShares product pages, stockanalysis.com) — these returned live, internally consistent content, so verification was possible using the same source classes Codex itself cited (SEC filings for company numbers, issuer pages for funds, exchange/close data for prices).
