# KEYS — Keysight Technologies — Diligence Dossier (Agent F87, Wave 5)

## 1. Verdict
**WATCH.** Real business, real cyclical upswing — but the 25-Sep-2026 close ($362.15) already prices in growth
above my base case. Horizon: 12–24 months (revisit after 1–2 more quarters confirm whether the AI/semiconductor
test-capex cycle is still accelerating or has crested).

## 2. Business in plain English
Keysight designs and sells electronic test-and-measurement instruments and software used to validate chips,
wireless networks (5G/6G), satellites, and defense electronics before they ship. Customers are semiconductor
fabs, network-equipment makers, telecom carriers and defense primes. It makes money selling hardware (spectrum
analyzers, network analyzers) plus a growing high-margin software/subscription tail, and it sits in an oligopoly
with Keysight, Anritsu, Rohde & Schwarz and National Instruments (Emerson) as the main players.

## 3. Why the model likes it — durable or artefact?
b1 factor file (composite decile 5, quintile 3, live_rank 257): momentum (pct_mom_12_1 0.77) and standardized
unexpected earnings (pct_sue 0.84) are both very high; quality (fam_Q pct_gp_a/roe strong) also elevated. This is
**mostly an artefact of a cyclical upswing**: KEYS's semiconductor and communications customers are mid-capex
cycle on AI accelerators and 6G R&D, driving order and revenue growth far above KEYS's historical trend. The
quant score will fade once base effects roll off — this is exactly the kind of "real but temporary" signal the
triage red flag ("cyclical: current growth partly reflects a semiconductor/AI test-capex upswing") flagged.

## 4. Last several quarters (fiscal year ends 31 Oct; source: 10-Qs/10-K, SEC EDGAR, XBRL companyfacts
CIK0001601046, e.g. accession 0001601046-26-000036)
| Quarter (fiscal) | Period end | Revenue | YoY growth | Net income | Diluted EPS |
|---|---|---|---|---|---|
| Q3 FY25 | 2025-07-31 | $1,352M | — | — | $1.10 |
| Q4 FY25 | 2025-10-31 (derived: FY25 total − 9mo) | $1,419M (5,375−3,956) | — | $850M FY total | $1.35 (4.91−3.56) |
| Q1 FY26 | 2026-01-31 | $1,600M | — | $281M | $1.63 |
| Q2 FY26 | 2026-04-30 | $1,717M | +31.5% vs Q2 FY25 $1,306M | $349M | $2.02 |
| Q3 FY26 | 2026-07-31 | **$1,846M** | **+36.5%** vs Q3 FY25 $1,352M | **$397M** | **$2.30** (+109% YoY vs $1.10) |

TTM (Q4'25–Q3'26): revenue ≈ $6,682M, diluted EPS ≈ $7.30 (1.35+1.63+2.02+2.30). This matches the triage's stated
36.5% Q3 revenue growth exactly. GAAP EPS is used throughout (Keysight also reports a non-GAAP EPS that runs
higher; I did not extract the exact adjusted figure this round — data gap noted).

## 5. Guidance track record
Not independently re-verified against the prior-quarter press release ranges this round (I did not pull the
non-XBRL 8-K exhibits for FY26 Q1–Q3 guidance letters — **data gap**). The triage's underlying claim of consistent
beats is consistent with the sequential revenue acceleration in the XBRL data above (Q1→Q3 FY26: $1,600M→
$1,717M→$1,846M), but I have not confirmed "guidance raised" wording directly from primary sources this pass.

## 6. Earnings quality & balance sheet
- 9-month FY26 (Nov'25–Jul'26) operating cash flow: **$1,379M**; capex: **$97M**; FCF ≈ **$1,282M**. FCF/NI
  (9mo NI $1,027M) ≈ 125% — very clean cash conversion, no working-capital games evident.
- Consolidated balance sheet (10-Q, period end 2026-07-31): cash & equivalents **$2,605M**; consolidated
  long-term debt (noncurrent) **$1,817M**. Keysight is **consolidated net-cash positive by roughly $0.8B** — no
  leverage risk.
- SBC not separately extracted this round; historically mid-single-digit % of revenue for KEYS (data gap, not
  re-verified from FY26 filings).
- No pending M&A, no litigation flagged in the sections read.

## 7. Valuation: reverse DCF and reconciliation with V1
**No V1 row exists for KEYS in `v1_valuation_table.csv`** → v1_verdict = null, no systematic model to reconcile
against this cycle.

My own reverse DCF: TTM FCF ≈ $1,469M (derived: FY25 OCF $1,409M − 9mo FY25 OCF $1,184M + 9mo FY26 OCF $1,379M,
less trailing capex ≈ $135M) against a $61.65B market cap (b1 file, 25-Sep-2026) → **FCF yield ≈ 2.4%**. Solving
a two-stage DCF (WACC 8.5%, 10-year explicit growth fading to a 3% terminal) for the growth rate that justifies
today's price gives **implied 10-year FCF growth ≈ 13%/year**. My evidence-based base case for a test-and-
measurement equipment maker — high-single-digit through-cycle growth (5–7% organic historically) lifted for 2–3
years by the AI/6G capex upswing, then reverting — averages to roughly **8–9%/year over 10 years**. **Implied
growth (~13%) is above my base case (~8–9%)** — this is a good business priced for a cycle that doesn't mean-
revert, which per the mandate makes it WATCH, not INCLUDE, even though the trend is genuinely strong right now.

## 8. Bull case / Bear case
**Bull:** (1) AI-accelerator and 6G R&D test-capex is a multi-year, not one-year, upswing — backlog/orders could
keep surprising high. (2) Net-cash balance sheet gives room to buy back stock or bolt on software/IP without
dilution. (3) Software/subscription mix shift raises structural margins over time.

**Bear:** (1) Semiconductor capex is famously cyclical — a 2019- or 2023-style capex air pocket would hit orders
before revenue, and the stock is priced at ~50x TTM EPS for a hardware-heavy business. (2) A single-customer or
single-node (e.g., leading-edge AI chip) slowdown could remove a large slice of the current growth. (3) Multiple
compression risk: even flat fundamentals at a normalized ~30–35x multiple implies material downside from $362.

## 9. Kill criteria (measurable)
1. Quarterly revenue growth decelerates below **+15% YoY** for two consecutive quarters (signals the AI/test
   capex cycle has crested).
2. Order backlog or book-to-bill ratio (next earnings release) falls below 1.0x for two consecutive quarters.
3. Diluted EPS growth YoY drops below **+15%** for two consecutive quarters.
4. Net cash position turns negative (i.e., debt-funded buyback/M&A that changes the balance-sheet risk profile).
5. Forward P/E stays above 45x TTM EPS while revenue growth decelerates below 15% — valuation/fundamentals gap
   widening rather than closing.

## 10. Catalysts & calendar
Next earnings: fiscal Q4 FY26, expected ~late November 2026 (pattern: FY25 10-K, accession 0001601046-25-000127,
filed 2025-12-17; FY26 Q4 release likely similar timing — not yet confirmed on IR site this round).

## 11. Red-flag scan
No auditor changes, restatements, going-concern language, or SEC/DOJ investigation disclosures found in the
10-Q sections reviewed. No short-seller report identified in this pass. Insider Form 4 pattern not reviewed this
round (data gap — time-boxed).

## 12. Sources
1. SEC EDGAR submissions, CIK0001601046, https://data.sec.gov/submissions/CIK0001601046.json (accessed 2026-09-27).
2. SEC EDGAR XBRL companyfacts, CIK0001601046, https://data.sec.gov/api/xbrl/companyfacts/CIK0001601046.json
   (accessed 2026-09-27; latest quarter incorporated: 10-Q accession 0001601046-26-000036, filed 2026-09-02,
   period ended 2026-07-31).
3. v4/data/b1_live_scores.csv (KEYS row, as_of 2026-09-25).
4. v4/outputs/Q11_triage.json (KEYS entry).
5. v4/outputs/v1_valuation_table.csv (checked — no KEYS row present).

## Data basis, recency and disclaimer
Most recent period incorporated: fiscal Q3 FY2026 10-Q (accession 0001601046-26-000036), period ended
2026-07-31, filed 2026-09-02. Events
checked to 2026-09-25 via SEC EDGAR submission list (no later 10-Q/10-K/8-K earnings release found). All revenue,
EPS, cash-flow and balance-sheet figures above are **GAAP**, sourced from XBRL company facts tied to the cited
filings; no adjusted/non-GAAP figures were substituted. Several items (exact FY26 guidance letters, SBC %,
AFFO/non-GAAP EPS, Form 4 insider pattern) were **not independently re-verified this round** and are flagged as
data gaps above rather than asserted. Research, not personal investment advice.
