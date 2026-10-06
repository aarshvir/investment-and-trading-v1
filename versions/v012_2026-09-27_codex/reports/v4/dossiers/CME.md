# CME Group Inc. (CME) — Diligence Dossier (Agent F99, standard depth)

**1. Verdict: INCLUDE-SMALL (half weight), 24–36 month horizon.** The world's largest regulated derivatives
exchange group, with a self-reinforcing clearing/liquidity moat and minimal balance-sheet risk, priced for
materially less growth than its own multi-year trend — but an active civil antitrust suit plus a live CFTC dispute
over competitor Kalshi's bitcoin perpetual futures are open-ended regulatory tail risks that argue for half
weight, not full, until they resolve.

**2. Business in plain English.** CME Group owns and operates the largest U.S. futures and options exchange
group — interest-rate, equity-index, FX, agricultural, energy and metals derivatives — plus the CME Clearing
central counterparty and a fast-growing market-data business (consolidated, Q2 2026 10-Q, filed 2026-07-24). It
earns transaction/clearing fees per contract traded/cleared plus subscription-style market-data fees; its moat is
liquidity itself (traders go where open interest already sits), reinforced by clearing/margin-efficiency
advantages that are very costly for a competitor to replicate.

**3. Why the model likes it / durability.** b1_live_scores.csv: composite decile 1/10 (bottom decile) — the
lowest composite of the three F99 names, driven by weak value percentiles (pct_ep 0.21, pct_bp 0.21 — the stock is
expensive on both earnings yield and book/price) partly offset by average momentum (pct_mom_12_1 0.48) and modest
earnings-quality (pct_roe 0.55). In plain terms: this is a quality/moat name the *quant score does not like* on
value grounds; the diligence case here rests on durability of the moat and cash generation, not the composite
rank (per program instructions: base the verdict on evidence, not quant rank).

**4. Last several quarters (consolidated income statement, GAAP; source: CME 10-Q filings for the periods shown,
filed 2025-04-30, 2025-07-25, 2025-10-24 (accession 0001156375-25-000206), 2026-04-24 (accession
0001156375-26-000020), 2026-07-24 (accession 0001156375-26-000047)).**

| Quarter (consolidated) | Revenue | YoY | Operating income | Net income | Diluted EPS | YoY EPS |
|---|---|---|---|---|---|---|
| Q1 2025 | $1,487.9m | — | $959.6m | — | $2.35 | — |
| Q2 2025 | $1,532.5m | — | $1,000.6m | — | $2.42 | — |
| Q3 2025 | $1,584.4m | — | $1,024.2m | — | $2.50 | — |
| Q1 2026 | $1,880.1m | **+26.4%** | $1,309.7m | — | $3.18 | **+35.3%** |
| Q2 2026 | $1,706.2m | **+11.3%** | $1,107.1m | $1,041.8m | $2.88 | **+19.0%** |

(Note: Q2'25 net income is not separately captured in the quarterly XBRL cut used this pass — the YoY revenue/EPS
comparisons above are the load-bearing figures.) GAAP throughout; CME's own earnings release also presents an
adjusted (non-GAAP) EPS that excludes items such as the equity stake in **S&P Dow Jones Indices**; this dossier
uses GAAP unless labelled. Per management's own Q2 2026 disclosures (CME press release/earnings commentary,
2026-07-22, and Q2 earnings call): Q2 average daily volume was 29.8m contracts (2nd-highest Q2 ever, within 1% of
the record); open interest ended Q2 up 8% YoY and +16% since 2026-01-01; market-data revenue rose 20% YoY to
$238m, the **33rd consecutive quarter** of YoY market-data growth. Revenue growth clearly decelerated from Q1
(+26.4%) to Q2 (+11.3%) — company attributes this to normalization after an unusually volatile Q1 (metals/energy
volumes driven by Middle East geopolitical tension); management stated **Q3-to-date volumes were tracking +18%
YoY** as of the July call, i.e. the deceleration looks like quarter-to-quarter lumpiness in volatility-driven
volume, not a trend break — but this is management's own characterization, not independently re-verified this
pass.

**5. Guidance track record.** CME does not issue formal forward EPS or revenue guidance (typical for exchanges);
it guides qualitatively on expense growth and capital-return policy. No "raised/maintained/cut" table applies —
noted per template instruction for no-guidance companies.

**6. Earnings quality & balance sheet (consolidated; source: Q2 2026 10-Q, filed 2026-07-24, accession
0001156375-26-000047).** Consolidated
total debt (Yahoo/company balance-sheet aggregation) **$3,868.5m**, consolidated cash **$2,275.6m** at 2026-06-30
→ net debt ≈ $1.59bn against consolidated stockholders' equity of **$26,520.4m** — trivial leverage (net
debt/equity ~0.06x) for a business with ~65% operating margins. Consolidated assets fell from $201,993.5m
(2026-03-31) to $194,676.6m (2026-06-30), consolidated liabilities from $175,375.3m to $168,156.2m — this swing is
overwhelmingly **clearing-house performance-bond/guaranty-fund cash and securities held for members**, not core
economic assets/liabilities of the exchange itself; the ~$140bn "assets/liabilities" figures should not be read
as CME's own balance-sheet risk (entity-scope flag per wave-6 mandate). ROE 15.8% (TTM); share count essentially
flat to slightly down (modest buybacks, PaymentsForRepurchaseOfCommonStock series present but small relative to
FCF). **Important nuance on the dividend:** the quoted "dividend yield" of ~1.9% (regular quarterly dividend,
$5.10/yr annualized) understates CME's real cash return — CME has historically also paid a large **annual variable
dividend** each January on top of the regular quarterly dividend; that variable component is not captured in the
`y_dividendYield` field used in this pass and should be added back for any total-shareholder-yield calculation
(flagged as a data conflict, not independently re-quantified this pass).

**7. Valuation snapshot & reverse DCF.** Price $264.48 (25-Sep-2026 close). Trailing P/E 22.45x (TTM EPS $11.78),
forward P/E 20.46x (consensus FY2026 EPS $12.93, Yahoo/d4). No V1 row exists for CME → v1_verdict = null. Reverse
DCF (Gordon growth solved for g, forward P/E 20.46x, an assumed total shareholder payout ratio of ~0.85 —
regular + variable dividend + buybacks, appropriate for an asset-light exchange that returns nearly all FCF — and
an 8.0% cost of equity for a moderate-beta (0.95) financial-infrastructure name): **implied perpetual earnings
growth ≈ 3.5–4.0%**. That is well below both CME's own trailing multi-year EPS trend (high-single-digit to
low-double-digit, driven by volume/open-interest growth + 33 straight quarters of market-data growth) and this
dossier's evidence-based base case (~7%), i.e. the market is pricing in materially less growth than the recent
trend implies — the valuation itself is not the risk here; the litigation/regulatory overhang is.

**8. Bull case:** (1) 33 consecutive quarters of market-data revenue growth and record open interest show a
structurally growing, sticky, high-margin (non-transaction) revenue stream layered on top of the core clearing
moat; (2) near-zero net leverage and ~85% cash-return payout give a wide margin of safety per dollar of earnings;
(3) implied growth (~3.5–4%) is well below both trend and base case — the stock is not priced for continuation of
its own recent trajectory. **Bear case:** (1) active civil antitrust litigation alleging CME "abused its dominant
market position to eliminate competition, fix data fees, and manipulate the cost of accessing futures markets,"
reportedly running alongside a CFTC-adjacent inquiry (per Lawfold.com legal-tracker coverage; the underlying
complaint/docket was not independently opened this pass — treat as unverified pending primary confirmation); (2)
CME itself sued the CFTC in 2026 over its approval of Kalshi's bitcoin perpetual futures — a genuine competitive
threat to CME's own product set from a CFTC-regulated prediction-market venue, not just a legal footnote; (3)
Q2 2026 revenue growth decelerated sharply (+11.3% vs +26.4% in Q1) — if the deceleration is not purely
volatility-driven lumpiness as management claims, base-case growth assumptions above are too high.

**9. Key risks & kill criteria:** (i) Consolidated revenue growth (YoY) below 5% for two consecutive quarters;
(ii) average daily volume down YoY for two consecutive quarters outside a clearly identified low-volatility
regime; (iii) an adverse antitrust judgment, CFTC enforcement action, or settlement against CME exceeding $500m or
requiring a structural remedy (e.g., forced open access to clearing); (iv) loss of exclusivity/competitive
displacement in a top-3 product line (rates, equity index, or FX futures) to a rival venue (including a
CFTC-approved prediction-market competitor such as Kalshi); (v) market-data revenue growth turns negative for one
quarter (breaking the 33-quarter streak) without a clearly identified one-off cause.

**10. Catalysts & calendar.** Next earnings ~2026-10-21 (Yahoo calendar). CFTC/Kalshi litigation and the civil
antitrust suit are both pending with no confirmed near-term ruling date (not independently verified this pass).

**11. Red-flag scan.** Two live legal/regulatory items, both **not independently opened at the primary-document
level this pass** and flagged as such: (a) ongoing civil antitrust litigation alleging anti-competitive conduct on
data fees and market access (secondary source: Lawfold.com); (b) CME's own 2026 suit against the CFTC (D.C.
district court) challenging the regulator's approval of Kalshi's bitcoin perpetual futures contract (Dechert/
Lowenstein Sandler client-alert coverage) — this is CME as plaintiff, not defendant, but signals a genuine
competitive/regulatory flashpoint over who can list perpetual-style contracts. No auditor change, restatement, or
going-concern language found in the 10-Q text reviewed. Not checked this pass: Form 4 insider-selling pattern,
short-seller reports.

**12. Sources.** (1) CME Q2 2026 10-Q, filed 2026-07-24, accession 0001156375-26-000047,
https://www.sec.gov/Archives/edgar/data/0001156375/000115637526000047/cme-20260630.htm. (2) CME Q1 2026 10-Q,
filed 2026-04-24, accession 0001156375-26-000020. (3) CME Q3 2025 10-Q, filed 2025-10-24, accession
0001156375-25-000206. (4) SEC XBRL companyfacts, CIK0001156375, retrieved 2026-09-27. (5) CME Group press
release, "CME Group Inc. Reports Strong Financial Results for Q2 2026," cmegroup.com, 2026-07-22. (6) Investing.com
earnings-call transcript, "CME Group posts record Q2 2026 revenue," 2026-07. (7) Dechert LLP, "Addendum to
Perpetual Contracts Update: CME Takes CFTC to Court," 2026-06. (8) Lowenstein Sandler, "CME Sues CFTC Over
Approval of Bitcoin Perpetual Futures Contract," 2026. (9) Lawfold.com, "CME Lawsuit 2026: What Traders Need to
Know Now," 2026 (secondary legal-tracker; primary docket not opened). (10) d4_live_snapshot.parquet and
b1_live_scores.csv (v4/data), retrieved 2026-09-25/26. (11) v4/outputs/Q05_triage.json.

**Data basis, recency and disclaimer.** Most recent period incorporated: Q2 2026 (quarter ended 2026-06-30), 10-Q
filed 2026-07-24. Events checked to 2026-09-25 close via web search (litigation, Q3-to-date volume commentary).
Figures above are GAAP and consolidated unless labelled otherwise; the antitrust/CFTC litigation items are sourced
from secondary legal-news coverage, not the underlying court dockets — flagged explicitly as a limitation.
Research only — not personal investment advice.
