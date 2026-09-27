# DA13 Fact-Check: BR digital-asset gain, BR total debt, GDDY gross vs. net debt

As of: 2026-09-27. Primary sources only (EDGAR 10-K/10-Q/8-K, data.sec.gov companyfacts). No dossier files edited.

## 1. BR — $227m digital-asset gain (PASS)

- Filing: Broadridge Financial Solutions 10-K for FY ended 2026-06-30, filed 2026-08-04, **accession 0001628280-26-052243**. MD&A "Other non-operating income (expense), net" section states GAAP results benefited from "non-cash Gains on Digital Assets of $227.0 million," cross-referencing **Note 8, "Fair Value of Financial Instruments."**
- Corroborated by the same-day 8-K, **accession 0001383312-26-000022**, Exhibit 99.1 earnings release, non-GAAP reconciliation table: row "Gains or Losses on Digital Assets" = Q4-26 **+$11.3m** (loss, added back) / FY26 **-$227.0m** (gain, subtracted out).
- Period/amount: FY2026 full-year pre-tax gain $227.0m; Q4 FY2026 non-cash loss ~$11.3m (dossier's "$11m" is a rounding match).
- Label: GAAP-included (raises reported net income/FCF), **excluded** from Adjusted Operating Income and Adjusted EPS per the release's footnote (iv)/(v).
- **Verdict: dossier's claim is accurate** on amount, period, and treatment (included in GAAP, excluded from adjusted).
- Side note (not scored): the release does show FY2026 diluted EPS and adjusted EPS converging to $9.60 — a real, disclosed coincidence, not a sourcing defect; the dossier's flag of it as "unresolved" is an interpretive judgment outside this check.

## 2. BR — total debt $3,520.5m (FAIL)

- Filing: same 10-K, accession 0001628280-26-052243; cross-tied against data.sec.gov companyfacts CIK 0001383312.
- At FYE **2026-06-30**: LongTermDebt (carrying value, all non-current, current portion = $0) = **$3,254.6m**; DebtInstrumentFaceAmount (gross principal) = **$3,274.7m**; cash = $402.9m (matches dossier exactly).
- At FYE 2025-06-30 (prior year): $3,252.3m carrying ($499.3m current + $2,753.0m non-current); face $3,263.5m.
- Intervening quarters (FY26 Q1–Q3): $3,281.3m / $3,173.1m / $3,227.0m carrying — none match $3,520.5m either.
- A full-text search of the 10-K for "3,520.5" returns **zero hits**. Nearby-looking numbers in the filing (Other direct expenses $3,514.5m/$3,633.2m, Goodwill $3,609.6m) are unrelated line items, not debt.
- **Verdict: the $3,520.5m figure is not traceable to the primary filing under any basis** — it is roughly $266–270m above the correct carrying value. Corrected figures: total debt (carrying) $3,254.6m, net debt = $3,254.6m - $402.9m = **$2,851.7m**; at TTM EBITDA $1,809m (dossier's own figure), net debt/EBITDA ≈ **1.58x**, not 1.7x.
- Kill criterion (net debt/EBITDA > 3.0x): **unaffected** — the corrected ratio is even lower than stated, so this does not change the investment conclusion, but the $3,520.5m and 1.7x figures should be corrected.

## 3. GDDY — gross debt $3,816.9m vs. net carrying value $3,774.4m (MINOR)

- Filing: GoDaddy 10-Q for quarter ended 2026-06-30, filed 2026-07-31, **accession 0001609711-26-000088**, Long-term Debt note.
- Debt-instrument table (2026-06-30 / 2025-12-31):
  - 2029 Term Loans: $1,436.9m / $1,444.2m
  - 2031 Term Loans: $980.0m / $985.0m
  - 2027 Senior Notes: $600.0m / $600.0m
  - 2029 Senior Notes: $800.0m / $800.0m
  - Revolver: $0 / $0
  - **Total (gross principal): $3,816.9m / $3,829.2m**
  - Less: unamortized original issue discount and debt issuance costs: $(42.5)m / $(48.9)m
  - **Total debt, net: $3,774.4m / $3,780.3m**
  - Less: current portion of long-term debt: $(15.0)m / $(15.1)m
  - **Long-term debt (non-current, net): $3,759.4m / $3,765.2m**
- Both dossier figures ($3,816.9m gross, $3,759.4m non-current net) are correct and pulled straight from this table; they are internally consistent ($3,816.9m − $42.5m − $15.0m = $3,759.4m). The auditor's read of **$3,774.4m** is the net carrying value of total debt ($3,816.9m − $42.5m) and is exactly right.
- The dossier's tag label "DebtInstrumentCarryingAmount" is a misnomer for the $3,816.9m gross-principal figure; that XBRL tag properly refers to the net carrying value.
- **Which figure should feed leverage:** the net carrying value, **$3,774.4m**, is the conventionally correct "total debt" input for net-debt/EBITDA (matches how the balance sheet and most credit analyses define debt).
- Recomputed: net debt = $3,774.4m − $1,155.5m cash = **$2,618.9m** (vs. dossier's $2,661.4m using gross). At the dossier's TTM EBITDA proxy of $1,379m: net debt/EBITDA ≈ **1.90x** vs. the dossier's stated **1.93x** — a ~0.03x difference.
- Kill criterion (net debt/EBITDA > 3.0x): **unaffected**; leverage stays comfortably in the ~1.9x range under either basis.
- Recommend: use $3,774.4m as "total debt (net)" for the leverage ratio and relabel $3,816.9m as "gross principal," not carrying value.

## Summary table

| Ticker | Claim | Status | Kill criterion impact |
|---|---|---|---|
| BR | $227m FY2026 digital-asset gain, $11m Q4 loss, GAAP-in/adjusted-out | PASS | None |
| BR | Total debt $3,520.5m / net debt/EBITDA 1.7x | FAIL | None (corrected ratio ~1.58x, still well under 3.0x) |
| GDDY | Total debt $3,816.9m (gross) vs. $3,774.4m (net carrying value) | MINOR | None (corrected ratio ~1.90x vs. stated 1.93x, still well under 3.0x) |
