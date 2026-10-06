# INTU (Intuit Inc.) — Diligence Dossier

Agent: F45 · Standard depth · Prepared 2026-09-26 · Price/market data as of 2026-09-25 close ($275.79; mkt cap ≈$76.4B on 277M diluted FY26 shares)

## 1. Verdict

**INCLUDE-SMALL** — 24–36 month horizon, one specific reservation: unresolved risk that AI-native "do-it-for-you"
tax/bookkeeping tools disintermediate TurboTax/Credit Karma faster than Intuit's own "Big Bets" can offset it,
compounded by a management-credibility flag from the May 2026 restructuring (Section 11). No V1 systematic
valuation row exists for INTU (`v4/outputs/v1_valuation_table.csv` / `v1_valuation.json` have no INTU entry) —
`v1_verdict` is null; the valuation view in Section 7 is the analyst's own reverse DCF.

## 2. Business in plain English

Intuit is a financial-software platform: TurboTax (DIY + assisted consumer tax filing), Credit Karma (free
credit monitoring monetized via lending/insurance referrals), QuickBooks + Intuit Enterprise Suite (small/mid-market
accounting, payroll, payments), and Mailchimp (email/marketing for small business). It earns subscription,
transaction and referral-commission fees from ~100M consumer and small-business customers. The moat is
network effects (QuickBooks' accountant ecosystem, Credit Karma's lender marketplace) and high switching costs
once a business's books or years of tax history live on the platform.

## 3. Why the model likes it / durability

`data/b1_live_scores.csv`: live_rank 251, composite driven by Quality (pct_roe 0.96, pct_ocf_a 0.91) and Value
(pct_fcfp 0.84) — high ROE/OCF and a cheap FCF yield together. This is unusual: normally a 24%+ ROE, 24%
OCF/assets grower does not also screen cheap on FCF yield. It reflects a real de-rating (Section 7), not an
accounting artefact — FY26 GAAP operating income growth (+20%) and revenue growth (+14%) are confirmed in the
10-K/8-K, not adjusted-metric puffery. Whether the de-rating is *justified* (AI disruption risk) or an
overreaction is the crux of the thesis; triage (Q11) flagged this explicitly as "monitor, not confirmed."

## 4. Last two fiscal years of results (FYE 31-Jul; GAAP; $M except EPS)

| Quarter (end) | Revenue | YoY | Op. income | Op. margin | Net income | Diluted EPS |
|---|---:|---:|---:|---:|---:|---:|
| Q1 FY25 (31-Oct-24) | 3,283 | — | 271 | 8.3% | 197 | 0.70 |
| Q2 FY25 (31-Jan-25) | 3,963 | — | 593 | 15.0% | 471 | 1.67 |
| Q3 FY25 (30-Apr-25) | 7,754 | — | 3,720 | 48.0% | 2,820 | 10.02 |
| Q4 FY25 (31-Jul-25) | 3,831 | — | 339 | 8.9% | 381 | 1.28¹ |
| Q1 FY26 (31-Oct-25) | 3,885 | +18.3% | 534 | 13.7% | 446 | 1.59 |
| Q2 FY26 (31-Jan-26) | 4,651 | +17.4% | 855 | 18.4% | 693 | 2.48 |
| Q3 FY26 (30-Apr-26) | 8,558 | +10.4% | 4,020 | 47.0% | 3,064 | 11.09 |
| Q4 FY26 (31-Jul-26) | 4,354 | +13.7% | 475 | 10.9%² | 363 | 1.30¹ |
| **FY26 total** | **21,448** | **+13.9%** | **5,884** | **27.4%** | **4,566** | **16.46** |

¹ Derived (FY total minus reported 9-month cumulative); Intuit does not disclose Q4 EPS as a discrete headline
figure separately from the FY total in the press release, so this is a computed residual, flagged as such.
² Q4 FY26 op income is suppressed by ~$300M of the restructuring charge below (excluding it, underlying Q4
margin ≈17.8%) — a GAAP/adjusted gap driver, not organic margin compression.
Big-quarter swings (Q3 >> Q1/Q2/Q4) are Intuit's normal seasonality: US tax season concentrates TurboTax/ProTax
revenue and profit in the fiscal Q3 (Feb–Apr). Full-year (non-seasonal) comparison is the right lens: FY26
revenue +14%, GAAP EPS +20%, non-GAAP EPS +20% to $24.27 (source 3, 4).
Segment FY26: Global Business Solutions $12.9B (+16%); Online Ecosystem $9.9B (+19%); Consumer $8.6B (+11%).

## 5. Guidance track record (last 4 releases, full-year FY26 revenue guide)

| Release (date) | FY26 revenue guide | vs prior range | Non-GAAP EPS guide |
|---|---|---|---|
| Q4 FY25 / initial FY26 (21-Aug-25) | $20.997–21.186B (+12–13%) | new (baseline) | $22.98–23.18 |
| Q1 FY26 (20-Nov-25) | $20.997–21.186B | **reiterated**, unchanged | $22.98–23.18 |
| Q2 FY26 (26-Feb-26) | $20.997–21.186B | **reiterated**, unchanged | $22.98–23.18 |
| Q3 FY26 (20-May-26) | $21.341–21.374B (+13–14%) | **raised** (revenue & non-GAAP); GAAP op-income guide range *lowered* slightly to absorb a new $300–340M restructuring charge | $23.80–23.85 |
| **FY26 actual** (25-Aug-26) | **$21.448B** (+14%) | beat even the raised Q3 guide | **$24.27** (beat) |

Every release beat or reiterated; Intuit raised revenue/profit guidance once (Q3) and beat its own raised number
at year-end. Track record is clean, but note the guide was flat for two full quarters before the raise — i.e.
guidance conservatism, not necessarily acceleration, until Q3. FY27 initial guide (25-Aug-26): revenue
$23.279–23.512B (+9–10%), non-GAAP EPS $22.88–23.12 (+23–24%, reflecting a Mailchimp segment/non-GAAP
reporting-methodology change flagged in the release — treat the FY27 vs FY26 EPS comparison as not
like-for-like without adjustment).

## 6. Earnings quality & balance sheet

- **FCF conversion:** FY26 OCF $8.838B − capex $0.175B = FCF $8.663B vs GAAP NI $4.566B → FCF/NI ≈190%. The gap
  is almost entirely non-cash add-backs (SBC, deferred revenue, amortization), not working-capital games.
- **SBC:** $2.056B in FY26, **9.6% of revenue** — the single largest GAAP-vs-non-GAAP reconciling item (non-GAAP
  EPS $24.27 vs GAAP $16.46; SBC alone accounts for ~$5.81/share of the FY27 guide's non-GAAP add-back). This is
  a real economic cost to existing holders even though it doesn't touch OCF; diluted share count has still
  *fallen* FY24→FY26 (284M→277M) because buybacks ($5.4B in FY26) more than offset SBC dilution.
- **Balance sheet:** cash $4.705B, total debt $7.669B (net debt ≈$2.96B), stockholders' equity $18.99B. Net
  debt/EBITDA ≈0.4x (EBITDA ≈$6.9B, GAAP op income $5.884B + D&A/amortization of acquired intangibles/technology
  ≈$1.0B) — low leverage, ample flexibility for further buybacks or bolt-on M&A.
- **Capital return:** $5.4B buybacks + $1.35B dividends in FY26; quarterly dividend raised 15% to $1.20/share
  (Feb-26 board approval).
- **Goodwill** $13.98B (Credit Karma, Mailchimp, TurboTax acquisitions) — no impairment flagged in FY26 10-K.

## 7. Valuation snapshot and reverse DCF

No V1 row exists for INTU, so this section is the analyst's own work (methodology disclosed for reproducibility).
NTM P/E (GAAP, on FY27 guide midpoint EPS $20.24): **13.6x**. NTM P/E (non-GAAP, FY27 guide midpoint $23.00):
**12.0x**. Both are a steep de-rating from Intuit's own 25x+ historical NTM P/E range (triage note, Q11) and from
peer "Rule of 40" software multiples generally.

**Simplified single-stage reverse DCF (disclosed simplification — standard-depth time box did not allow a full
10-year fade model as V1 uses for other names):** EV ≈ market cap $76.4B + net debt $2.96B ≈ **$79.4B**. TTM FCF
$8.663B (FCF yield 10.9% on EV — high for a "growth" stock). Estimated WACC ≈9.5% (rf 5.17%, ERP 4.14%, assumed
beta ≈1.05–1.1, consistent with software peers; INTU has no V1-derived beta to draw on). Solving
EV = FCF×(1+g)/(WACC−g) for g: **implied perpetual FCF growth ≈ −1.3%** (i.e., the market is pricing INTU as if
free cash flow never grows again). Re-running with SBC treated as a real economic cost (FCF − SBC = $6.607B,
i.e. an "owner earnings" haircut) still gives only **≈+1.1%** implied perpetual growth. Either way, the price
implies materially less growth than the FY27 guide (revenue +9–10%, non-GAAP EPS +23–24% off the new base) or
Intuit's own 5-year (historical delivered growth well above high-single digits) — **implied growth is below my
base case (see scenarios)**, which is why this qualifies for INCLUDE-SMALL rather than WATCH despite the
adverse facts in Section 11.

**3-year scenario returns (annualised, price+dividends, exit-multiple method):** bear −9.0% (EPS flat, multiple
to 8x) · base +18.3% (EPS +15%/yr, multiple holds ~12x) · bull +40.5% (EPS +22%/yr, multiple re-rates to 17x).

## 8. Bull case / bear case

**Bull:** (1) Big Bets (AI-driven "done-for-you" tax, bookkeeping, Mailchimp-Intuit-Assist) grew 34%/yr and are
now 30% of FY26 revenue — a second growth engine scaling from a larger base each year. (2) FY27 guide (+9–10%
revenue, +23–24% non-GAAP EPS) at a 12x non-GAAP forward multiple leaves room for material re-rating if executed.
(3) Buybacks have shrunk the share count every year since FY24 while still funding double-digit dividend growth.

**Bear:** (1) Consumer-facing generative-AI tax/bookkeeping tools (ChatGPT-style "just do my taxes/books")
are a structural threat to TurboTax/QuickBooks pricing power that has not yet shown up in the numbers but could
arrive discontinuously. (2) Two workforce restructurings in 24 months (Jul-2024 ~1,800; May-2026 ~3,000, 17% of
staff) signal either aggressive AI-driven cost-cutting or execution/cost-structure problems — the CEO gave
contradicting public explanations for the second one (Section 11). (3) SBC at 9.6% of revenue means reported
non-GAAP EPS growth overstates the cash return actually available to shareholders before buybacks.

## 9. Key risks & kill criteria (measurable)

1. TurboTax **or** Credit Karma segment revenue growth turns negative for 2 consecutive quarters (direct
   evidence of AI-driven disintermediation, not just deceleration).
2. Non-GAAP operating margin compresses >300bps YoY for 2 consecutive quarters.
3. A third major workforce restructuring (>5% of headcount) announced within 24 months of the May-2026 cut.
4. Full-year revenue or non-GAAP EPS guidance is **cut** (vs. the prior range) at any of the next 4 quarterly
   releases (it has never happened in the last 4 — this would be a first).
5. Net debt/EBITDA rises above 1.5x via debt-funded M&A (currently ≈0.4x).

## 10. Catalysts & calendar

Next scheduled release: **Q1 FY27 earnings, estimated ~19-Nov-2026** (Q1 FY26 was reported 20-Nov-2025; date not
yet confirmed by the company — flagged as an estimate). FY27 guidance (already issued 25-Aug-26) will be
updated/reiterated at that release — first read on whether the AI-disruption risk is showing up in TurboTax/
Credit Karma growth. Quarterly dividend record dates follow the normal Nov/Feb/May/Aug cadence.

## 11. Red-flag scan

- **Workforce restructuring, May 2026:** Intuit announced ~3,000 job cuts (17% of ~18,200 employees) alongside
  Q3 FY26 earnings, with $300–340M of restructuring charges (largely in Q4 FY26). This is the **second** major
  cut in two years (July 2024: ~1,800, ~10%). CEO Sasan Goodarzi told employees the goal was a "leaner, more
  focused" organization but told CNBC's Jim Cramer "none of it had to do with AI" — an inconsistency with the
  company's own AI-platform narrative to investors, worth discounting management commentary on execution going
  forward (source 5, 6).
- **FTC consent order (since Jan-2024, ongoing):** Intuit is permanently barred from advertising TurboTax as
  "free" unless it discloses the ~1/3 qualification rate; company also chose **not** to renew participation in
  the IRS Free File Program for the 2026 season, a reputational/political exposure given renewed public
  attention on free-filing access (source 7, 8). No new fine in FY26; compliance risk is ongoing, not escalating.
- No auditor change, restatement, going-concern language, or SEC/DOJ investigation found in the FY26 10-K or
  recent 8-Ks reviewed.
- No unusual insider-selling pattern identified within the standard-depth time box (not exhaustively checked —
  disclosed limitation).

## 12. Data basis, recency and disclaimer

Most recent period incorporated: FY2026 10-K (period end 2026-07-31, filed 2026-09-09) and the FY26 Q4/full-year
earnings release (8-K filed 2026-08-25). Checked for events to 2026-09-25. GAAP figures are labelled GAAP;
non-GAAP figures (Section 4/6/7) are labelled non-GAAP and sourced from Intuit's own press-release
reconciliations, never blended into GAAP totals. Research, not personal investment advice.

## 13. Sources

1. Intuit FY2026 Form 10-K, filed 2026-09-09, SEC EDGAR CIK 0000896878, accession 0000896878-26-000037.
2. Intuit Q1–Q3 FY2026 Forms 10-Q (filed 2025-11-20, 2026-02-26, 2026-05-20), same CIK.
3. Intuit Q4/FY2026 earnings release, 8-K exhibit 99.01, filed 2026-08-25 (accession 0000896878-26-000029).
4. Intuit Q1/Q2/Q3 FY2026 earnings releases, 8-K exhibits, filed 2025-11-20 / 2026-02-26 / 2026-05-20.
5. TechCrunch, "Intuit to lay off over 3,000 employees to refocus on AI," 2026-05-20.
6. CNBC, "Intuit CEO says company's 17% workforce cut had 'nothing to do with AI'," 2026-05-20.
7. FTC consumer alert / Thomson Reuters Tax, "FTC Bars Intuit From Distorting Eligibility for TurboTax Free
   Edition" (order in effect since Jan-2024).
8. Kiplinger / Fortune, "IRS Free File Program delivered by TurboTax is no longer available," 2026.
9. `v4/data/b1_live_scores.csv`, `v4/data/triage_cards.csv`, `v4/outputs/Q11_triage.json` (2026-09-26 program data).
