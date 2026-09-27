# V2R — REIT Valuation Repair (HST, FRT, UDR, PSA)

**Agent:** V2R | **As of:** 2026-09-25 close | Research only; not investment advice.

## 1. The problem with V1's REIT valuation

V1 (`v4/code/v1_valuation.py` lines ~229-245, ~440-470) computes, for every REIT, a proxy
`ffo_proxy_ttm = ni_ttm + da_ttm` (GAAP net income, trailing twelve months, plus **total**
depreciation & amortization — not real-estate-only) and ranks the resulting P/FFO against the
stock's own **~171-177 month** (14.25-14.75y) history to get an "own-history percentile," which
V1 blends into its verdict. This proxy:
- **Does not exclude gains on sale of real estate**, which are one-off and explicitly excluded
  from NAREIT FFO by definition — so any quarter with a large disposition gain mechanically
  *inflates* the proxy and makes the stock look "cheaper" (lower P/FFO, lower percentile) than
  it really is.
- **Does not add back real-estate impairments** (a smaller effect for these four, but part of
  the standard definition).
- Uses **total** D&A rather than real-estate D&A (immaterial for these four pure-play REITs,
  whose non-real-estate D&A is negligible).

This matters most right now because HST booked a **$242m pre-tax gain on a 3-hotel sale** in Q1
2026 and FRT booked **$20.6-113.3m/quarter of realty gains** in Q1-Q2 2026 — both flow straight
into V1's `ni_ttm` and hence its "FFO," badly overstating trailing FFO and understating P/FFO
for exactly the two REITs the lead flagged.

## 2. Method

1. **NAREIT FFO reconstruction**: `FFO_q = NetIncomeLoss_q + DepreciationAndAmortization_q −
   GainOnSaleOfRealEstate_q + RealEstateImpairment_q(add-back)`, built quarterly from SEC XBRL
   `companyfacts` (data.sec.gov, CIK per ticker; concept fallback chains and per-ticker tag
   choices are in `v2r_reit_ffo.py`). Weighted-average diluted shares are XBRL
   `WeightedAverageNumberOfDilutedSharesOutstanding`; a discrete Q4 (not separately tagged in
   10-Ks) is derived as FY − 9M-YTD for flow items, and as `FY_avg×4 − (Q1+Q2+Q3)` for the share
   count (weighted averages are not additive across sub-periods — using FY−9M for shares produces
   nonsense and was caught and fixed during QC, see §5).
2. **Ground-truth overlay**: for each ticker, the **8 most recent quarters' company-reported
   NAREIT FFO/share** (Q3'24-Q2'26) — sourced from the dossiers' own §4 tables (FRT, UDR, PSA,
   all primary 8-K EX-99.1-sourced) plus two direct SEC EDGAR fetches for HST (Q2'26, Q4/FY25,
   Q3'25 releases, since the HST dossier only tabulated Adjusted FFO, not NAREIT FFO) — **replace**
   the XBRL proxy wherever available. The current TTM figure (the number that matters most for
   the verdict) is therefore built **entirely from company-reported actuals**, not the proxy, for
   all four tickers.
3. **Monthly panel**: quarterly TTM FFO/share is forward-filled from each quarter's XBRL filing
   date (or +35 days after quarter-end for the reported overlay, approximating the 8-K release
   date) and matched to month-end close (`v4/data/d2_close.parquet`, unadjusted — no special
   dividends among these four in the sample window that would distort the *unadjusted* close/FFO
   ratio). An explicit "as of 2026-09-25" observation uses the actual current close.
4. **Own-history percentile** = share of monthly P/FFO observations, trailing 5y (60mo) and 10y
   (120mo) windows, that are ≤ today's value (matches the direction of V1's own language, e.g.
   "5.65th percentile" = cheaper than 94% of history).
5. **FY2026 guidance P/FFO** = current price ÷ company's own FY2026 guidance midpoint, labeled
   with whichever measure (NAREIT FFO / Core FFO / FFO-as-Adjusted) the company itself guides on
   (see per-ticker tables) — this matches the lead's own reference figures for HST (~10.4x) and
   FRT (~14.7x) exactly.
6. **Peers**: latest FY2026 guidance (or latest-quarter annualized where guidance was unavailable/
   suspended) FFO per share, current price, both cited (see §7, sources in JSON).

## 3. Per-REIT results

### HST — Host Hotels & Resorts
| Metric | Value |
|---|---|
| FFO measure (TTM) | NAREIT FFO/sh (company-reported for the full trailing 4 quarters: Q3'25 $0.34 + Q4'25 $0.49 + Q1'26 $0.66 + Q2'26 $0.62 = **$2.11**) |
| P/FFO (TTM NAREIT FFO) | **10.63x** at $22.42 |
| P/FFO (FY26 Adjusted FFO guide, mid $2.165) | **10.36x** — matches the lead's reference figure |
| Adjusted FFO/sh (TTM, company-reported) | $2.16 — essentially equals the FY26 guide midpoint |
| Own-history percentile | **57.4 (5y, n=61mo) / 48.8 (10y, n=121mo)** — roughly the **median** of its own range |
| Peers (FY26 guide P/FFO) | PK 7.57x (AFFO guide mid $1.95); RHP 13.29x (AFFO guide mid $9.08, post Grande Lakes Orlando deal); APLE 10.95x (FY25 actual FFO, guide not located) → **median 10.95x** |
| V1 → corrected | P/FFO(proxy) 8.49x, 29.2 pctile, "attractive" → **P/FFO 10.6x, ~49-57 pctile, "FAIR"** |

**Thesis-claim check**: HST's "attractive" framing does **not** fully survive. In line with
peers, roughly at the median of its own history — no longer statistically cheap.

### FRT — Federal Realty
| Metric | Value |
|---|---|
| FFO measure (TTM) | NAREIT FFO/sh, all 4 trailing quarters company-reported: Q3'25 $1.77+Q4'25 $1.84+Q1'26 $1.88+Q2'26 $1.88 = **$7.37** |
| P/FFO (TTM NAREIT FFO) | **14.94x** at $110.52 |
| P/FFO (FY26 Core FFO guide, mid $7.52) | **14.70x** — matches the lead's reference figure |
| Core FFO/sh | Only reported since Q4 2025 (definitional break, flagged by the dossier); TTM not computable on a like-for-like basis |
| Own-history percentile | **55.7 (5y, n=61mo) / 37.2 (10y, n=121mo)** — **median-ish**, modestly below its 10y median, nowhere near an extreme |
| Peers (FY26 guide P/FFO) | REG 15.07x (Nareit FFO guide mid $4.86); KIM 12.23x (FFO guide mid $1.835); SPG 15.46x (Real Estate FFO guide mid $13.25) → **median 15.07x** |
| V1 → corrected | P/FFO(proxy) 10.80x, **5.65 pctile**, "attractive" → **P/FFO 14.9x, ~37-56 pctile, "FAIR"** |

**Thesis-claim check**: FRT's **"near the cheapest ever" claim does NOT survive.** V1's 5.65th
percentile was an artefact of not excluding FRT's realty gains-on-sale ($20.6-113.3m/quarter in
Q1-Q2 2026); on a corrected basis FRT trades at essentially the same P/FFO as its own 10-37y
median and in line with REG/KIM/SPG peers.

### UDR — apartment REIT (candidate, INCLUDE-SMALL)
| Metric | Value |
|---|---|
| FFO measure (TTM) | FFO/sh (NAREIT), all 4 trailing quarters company-reported: Q3'25 $0.62+Q4'25 $0.62+Q1'26 $0.63+Q2'26 $0.60 = **$2.47** |
| P/FFO (TTM FFO) | **13.65x** at $33.84 |
| P/FFO (FY26 FFO guide, mid $2.51) | **13.48x**; on FFOA guide (mid $2.53): 13.38x |
| FFO-as-Adjusted/sh (TTM, reported) | $2.55 |
| Own-history percentile | **7.1 (both windows quoted) — LOW CONFIDENCE, n=14 months only** (2025-08 to present); UDR's XBRL `DepreciationAndAmortization` tag is mis-scoped (~20-25x too small) for most quarters before Sep-2025, so 37 of 53 reconstructed quarters had to be dropped as implausible rather than trusted — a genuine data-quality limitation, not a judgment call. V1's own (uncorrected) percentile was 10.2 over ~15y; direction is consistent (cheap) but the exact number above should not be over-read |
| Peers (P/FFO) | EQR 15.76x (FY26 FFO guide mid $4.04, price ~6wk stale, merger pending w/ AVB); AVB 16.09x (Q2'26 Core FFO ×4, guidance suspended); CPT 14.60x (Q2'26 Core FFO ×4, no FY26 guide found); MAA/ESS not available this pass → **median 15.76x** |
| V1 → corrected | P/FFO(proxy) 13.34x, 10.2 pctile, "attractive" → **P/FFO 13.5-13.7x, directionally still cheap vs peers, "ATTRACTIVE" (unchanged), but conviction lower than V1's 0.874 score implies** |

**Thesis-claim check**: partially survives — still cheap vs. peers even after removing UDR's own
$193m (1H26) of realty gains, but the precise historical percentile could not be independently
verified this pass; treat with the same caution the UDR dossier itself applied (INCLUDE-SMALL).

### PSA — Public Storage (WATCH)
| Metric | Value |
|---|---|
| FFO measure (TTM) | Two measures, reported separately (PSA's plain FFO is noisy — FX swings on Euro debt, dossier §6): NAREIT FFO/sh TTM (Q3'25 $4.33+Q4'25 $4.33+Q1'26 $4.39+Q2'26 $4.21) = **$16.68/sh → 16.68x**; **Core FFO/sh TTM** (4.31+4.26+4.22+4.17) = **$16.96/sh → 16.98x** (preferred, cleaner) |
| P/FFO (FY26 Core FFO guide, mid $16.90) | **17.04x** |
| Own-history percentile (NAREIT FFO basis) | **27.9 (5y, n=61mo) / 17.4 (10y, n=121mo)** — moderately cheap vs. its own past, not extreme |
| Peers (FY26 guide P/FFO) | EXR 16.02x (Core FFO guide mid $8.325); CUBE 16.20x (FFO-as-adjusted guide mid $2.56) → **median 16.11x** |
| V1 → corrected | P/FFO(proxy) 15.84x, 9.6 pctile, "fair" → **P/FFO ~17.0x, ~17-28 pctile, "FAIR" (unchanged)** |

**Thesis-claim check**: PSA's "fair" verdict survives; roughly in line with EXR/CUBE and only
moderately (not extremely) cheap vs. its own history — consistent with the dossier's separate,
business-quality-driven WATCH stance (shrinking same-store NOI, unproven NSA merger integration).

## 4. Verdict summary

| Ticker | V1 P/FFO(proxy) | V1 own-pctile | V1 verdict | Corrected P/FFO (TTM) | Corrected pctile (5y/10y) | Corrected verdict | Changed? |
|---|---|---|---|---|---|---|---|
| HST | 8.49x | 29.2 | attractive | 10.63x | 57.4 / 48.8 | **fair** | **YES** |
| FRT | 10.80x | 5.65 | attractive | 14.94x | 55.7 / 37.2 | **fair** | **YES** |
| UDR | 13.34x | 10.2 | attractive | 13.65x | 7.1* / 7.1* (low-confidence) | attractive | no |
| PSA | 15.84x | 9.6 | fair | 16.68x (Core FFO: 16.98x) | 27.9 / 17.4 | fair | no |

\* UDR's percentile is built on only 14 clean months, not a true 5y/10y sample — see §3 data-quality note.

## 5. Validation performed

- **HST**: computed proxy vs. company-reported NAREIT FFO$ (not per-share) for Q1'26 ($442m proxy
  vs. ~$455m actual, ~3% off), Q2'26 ($431m vs. $426m, ~1% off), Q3'25 ($235m vs. $234m, ~0.4%
  off) — all three checks within 3%, confirming the `OtherNonoperatingGainsLosses` tag correctly
  captures HST's disclosed disposition gains ($242m Q1'26, $122m Q3'25 — both match the tag
  exactly). 6 quarters of actual reported NAREIT FFO/share obtained directly from primary SEC
  filings (Q2'26, Q2'25, Q4'25, Q4'24, FY25, FY24) plus 2 more (Q3'25, Q3'24) = 8 validation
  points, exceeding the 4-point minimum.
- **FRT, UDR, PSA**: 8 quarters each of company-reported FFO/share (and Core/Adjusted FFO where
  disclosed) taken directly from the dossiers' primary-sourced §4 tables — used as ground truth,
  not just validation.
- **QC catch**: an initial Q4-derivation bug (deriving discrete Q4 shares as FY−9M, which is
  invalid for a weighted-average/level series, not a flow) produced a nonsensical negative FFO/
  share for one HST quarter (2023 Q4) and, more seriously, corrupted ~40 of UDR's ~53
  reconstructed quarters once combined with a separate UDR-specific issue (its main
  `DepreciationAndAmortization` XBRL tag resolves to a small, evidently non-consolidated figure
  for most periods outside 2025Q3-2026Q2). Both were caught by describing the resulting monthly
  P/FFO series (expecting single-digit-to-30s multiples; found >100x outliers) before the
  percentiles were finalized. The share-count formula was fixed for all four tickers; the D&A
  issue could not be fully resolved for UDR within the time-box and is disclosed as a limitation
  rather than papered over (own_pct_5y/10y for UDR marked low-confidence, n=14 months).
- **Peer data**: current prices for PK, RHP, APLE, CUBE are not in `d2_close.parquet` (not part
  of the tracked universe) and were sourced from web search (secondary, dated as noted per-peer);
  EQR/AVB prices are the last available in `d2_close.parquet` before a gap (merger-related).
  These are flagged, not treated as point-in-time-clean.

## 6. Limitations (disclosed, not silently patched)

1. Net income used throughout is total `NetIncomeLoss` (pre-NCI/OP-unit split), not strictly
   "attributable to common"; validated to within ~1-3% against actuals for HST but not
   independently re-verified for FRT/UDR/PSA's older history.
2. FRT stops isolating a "gain on sale" XBRL tag after 2020-Q3 (a real data-quality gap, not an
   error in this script) — its 2021-2024 reconstructed quarters (before the reported-actuals
   overlay begins in Q3 2024) use NI+D&A without a gain deduction and may be modestly overstated
   in quarters with disclosed realty gains.
3. UDR's 5y/10y own-history percentile is low-confidence (see §3, §5) — a genuine gap, not
   estimated.
4. Several peer prices are secondary-sourced and dated (not exactly 2026-09-25); flagged per-peer
   in the JSON.
5. Real-estate-specific D&A vs. total D&A is not separately isolated (immaterial for these four
   pure-play REITs, per the task's own allowance).

## 7. Files produced
- `v4/outputs/v2r_reit_valuation.json` — machine-readable results (schema per spec)
- `v4/outputs/v2r_reit_valuation.md` — this report
- `v4/code/v2r_reit_ffo.py` — computation code (reads XBRL cache + d2_close.parquet, writes both
  outputs above plus `v4/data/v2r_<ticker>_monthly_pffo.csv` per ticker)
- `v4/data/v2r_hst_monthly_pffo.csv`, `v2r_frt_...`, `v2r_udr_...`, `v2r_psa_...` — monthly P/FFO
  panels underlying the percentiles
- Cache: `C:\Users\user\eqv4\cache\V2R\companyfacts_<TICKER>.json` (raw SEC XBRL, 4 files)

No V1 files or dossiers were modified.
