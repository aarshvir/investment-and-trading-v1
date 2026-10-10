# DV43 fact-check (2026-10-09)

Scope: VTRS, VZ, WAB, WAT, WBD, WDAY, WDC, WELL, WFC, WM. Primary sources: SEC EDGAR companyfacts, 10-Q/10-K, 8-K Ex-99.1. Full detail in `DV43_factcheck.json`.

Counts (83 facts): PASS 60, MINOR 9, FAIL 13, UNVERIFIABLE 1. Corrections appended to 7 dossiers (WAB, WAT, WBD, WDC, WELL, WFC, WM). VTRS, VZ (already corrected by DVH6) and WDAY needed none.

## Verdict changes
None. All ten verdicts and all implied_vs_base calls stand. WFC scenario returns were restated (see below).

## FAILs and notable findings
- **WFC:** scenario returns in F49_summary.json were built on $8.00 of run-rate EPS (best quarter x 4); on $7.20 (H1 annualised) they are -11.1% / +5.0% / +13.7% instead of -8.0% / +8.7% / +17.8%. Base case now below the 9.1% cost of equity; INCLUDE rests on the P/TBV-ROTCE test (price implies ROTCE about 13.9% vs 15-16% delivered). Kill criterion 4 wrongly said Q1 EPS growth was +21%; it was +15.1%. F49 summary updated.
- **WAB:** reverse DCF used adjusted EPS as cash flow; on FCF after SBC (TTM $1,620M) implied growth is 9.5-10.5% vs about 10% base, still in line. Net debt/EBITDA is about 2.35x (TTM D&A $546M), not 2.6x. Dividend is $0.31 a quarter, not about $0.25. F94 summary kill-criterion text updated.
- **WAT:** reverse-DCF start of $1.35bn assumed 95% conversion of adjusted net income (FY2025 was 69%, SBC not deducted); on about $1.0bn implied growth is 13.6-17% vs 8% base, so the stock is further above base; the $380 "upgrade price" is about $222-281. Kill criterion 4 (net debt above $4.5bn) was already breached at $4.55bn. F166 summary text updated.
- **WELL:** net debt taken from a Q1 estimate ($14.5bn) although the Q2 10-Q gives $15.6bn; reverse DCF capitalised post-interest FFO against enterprise value with a 4.2% risk-free rate; equity-basis restatement gives 11.5-13.4% implied vs 9% base (still above).
- **WM:** levered FCF capitalised against EV; on equity value and FCF after SBC the price implies 3.6% (not 4.0%) vs 6-7% base; still below.
- **WDC:** Q3 FY25 table row duplicates Q4 FY25 EPS; FY26 buybacks of $2,592M were described as nine-month figures under a $2.0bn programme (it is $6.0bn authorised, $1.92bn in nine months); SBC overstated (FY26 $204M, 1.6% of revenue). Valuation on FCF after SBC: 24-27% implied vs 8-10% base (above).
- **WBD:** the merger closed on 6 Oct 2026 (8-K Items 2.01/3.01, $31.0167 cash per share, delisted); the dossier had marked the closing unverified. REJECT stands and the ticker is no longer investable.
- **VTRS:** all facts verified; on programme Ke 8.99% the "in_line" call is discount-rate sensitive (implied +0.5% vs base +3.3%), but WATCH rests on the 3-year return (+7.4%) and is unchanged.
- **VZ:** all load-bearing facts verified; DVH6 corrections confirmed.
- **WDAY:** all facts verified; method (FCF after SBC) correct.
