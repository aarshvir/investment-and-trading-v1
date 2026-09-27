# Honeywell International Inc. (Nasdaq: HON, "Honeywell Technologies") — Diligence Dossier
Agent F102 · Standard depth · As-of close 2026-09-25 (~$226, per closest available quote; company market cap ≈$146bn)

## 1. Verdict
**WATCH.** Thesis horizon 12–36 months. One-sentence reason: the three-way breakup (Solstice spun Oct 2025, Aerospace spun 29 Jun 2026) has left a cleaner, higher-margin Building/Industrial/Process-Automation pure-play, but the post-spin financials are still noisy (separation costs, restated share count, one negative-EPS quarter), leverage is elevated at ~3x, and the market has already priced in a meaningful re-rating — there isn't yet enough post-spin data to confirm the "market hasn't re-rated it" thesis from triage.

## 2. Business in plain English
"Honeywell Technologies" (the entity that kept the HON ticker after the Aerospace spinoff) is now a pure-play automation and autonomy company organized around Building Automation, Industrial Automation and Process/Energy Automation — think building controls, warehouse/industrial automation, process-control instrumentation for refiners and chemical plants, and connected-building software. It sells mainly to industrial, commercial-real-estate and energy customers through long-cycle equipment sales plus recurring service/software contracts, competing with Siemens, Schneider Electric, Emerson and Rockwell.

## 3. Why the model likes it / is it durable
Triage flagged 12-month momentum from the freshly completed breakup (Solstice Sep/Oct 2025, Aerospace Jun 2026) as the market not yet having re-rated a more focused, higher-margin automation franchise. This is a real structural change (durable), but "the market hasn't re-rated it" is an assertion that needs the multiple evidence in §7 — which shows the multiple has in fact already moved up meaningfully since the spin announcements, weakening the pure re-rating argument.

## 4. Last quarters — results (GAAP, consolidated continuing-operations basis where available; source: 10-Q/10-K XBRL)
| Period end | Revenue | Net income | Diluted EPS | OCF (period) | Capex (period) |
|---|---|---|---|---|---|
| Q2 2025 | $9,435 (Q) | — | $4.90 (6mo) / $2.45 restated-Q | $1,916 (6mo cum.) | $416 (6mo cum.) |
| Q3 2025 | $9,437 | $1,825 (9mo cum.) | $2.86 (Q) | $5,204 (9mo cum.) | $928 (9mo cum.) |
| FY2025 | $37,442 | $4,729 (or -$115 in one alternate FY2025 tag — see note) | $7.36 (or -$0.18 alt tag) | $6,408 | $986 |
| Q1 2026 | $9,143 | $821 | $1.29 | -$650 (negative OCF quarter) | $223 |
| Q2 2026 | $9,719 (Q) / $18,862 (6mo) | $5,682 (Q, includes spin gain) / $6,503 (6mo) | $17.83 (Q) / $20.39 (6mo) | $626 (6mo cum.) | $538 (6mo cum.) |

**Data conflict flagged, not smoothed over:** the XBRL companyfacts feed carries two inconsistent FY2025 NetIncomeLoss/EPS tags ($4,729mn / $7.36 vs. -$115mn / -$0.18) and the diluted share count roughly halves between Q1 2026 (638mn) and Q2 2026 (319mn) in the same tag family. This is consistent with (a) the Aerospace spin-off being accounted for as discontinued operations with restated comparatives, and (b) a share count/EPS discontinuity from deconsolidating Aerospace mid-2026, but I could not fully reconcile the two tag sets from the XBRL facts API alone inside the time box — **flag this as a data_conflict requiring a read of the actual Q2 2026 10-Q financial statements (not just XBRL) before sizing a position.** Q2 2026 net income of $5.68bn on $9.72bn revenue is not organic — it includes a large one-time separation/deconsolidation gain and should not be treated as a run-rate margin.

## 5. Guidance track record (versus prior range)
- **Solstice Advanced Materials** (spun-off entity, now separately listed, ticker SOLS): raised FY26 revenue view to $4.13–4.19bn from $3.9–4.1bn and FY26 adjusted EBITDA to $1.04–1.06bn from $975mn–1.03bn at its Q2 2026 release (30 Jul 2026) — **this is SOLS's guidance, not HON's; cited only as context on how the broken-up pieces are performing, and to flag that some "Honeywell" headlines in the wild conflate the three entities.**
- I could not source a clean, filing-quoted HON-standalone (post-Aerospace) full-year guidance reset with a "prior range" comparison inside the time box — the Q2 2026 8-K (filed ~Jul 2026) is the right primary source for this and should be the first read in a follow-up pass.

## 6. Earnings quality & balance sheet
- **Entity scope:** figures above are HON (Honeywell International Inc., the entity that retained the ticker; "Honeywell Technologies" post-spin) as filed. The **September 2026 DOJ $2.04mn cybersecurity False Claims Act settlement is against "Honeywell Aerospace Inc.,"** which is now the **separately listed HONA**, not this HON entity — this distinction matters and an earlier draft of this note nearly attributed it to the wrong company; the wave-3 entity-scope mandate specifically warns against this kind of cross-entity mixing post-breakup.
- Long-term debt (consolidated, carrying value): $31.51bn at 2026-06-30 (10-Q), up from $28.69bn at 2025-12-31 — leverage rose through the separation, consistent with triage's flagged "elevated net debt/EBITDA (3.0x) from separation-related debt allocation."
- Stockholders' equity jumped from $13.59bn (Q1 2026) to $18.54bn (Q2 2026), consistent with a large one-time gain/reclassification from the Aerospace deconsolidation — another reason the Q2 2026 income statement should not be read as run-rate.
- Buybacks continued through the separation ($1.0bn in both Q1 and Q2 2026) even as OCF went negative in Q1 2026 — a capital-allocation choice worth watching given the leverage level.

## 7. Valuation — reverse DCF and reconciliation with V1
No row for HON exists in `v4\outputs\v1_valuation_table.csv` — **v1_verdict = null**.
- Price ≈$226; FY2027 consensus EPS ≈$10.20 (range $9.21–12.02) → forward P/E ≈22x, versus a headline trailing P/E of ~31x distorted by the separation-cost-heavy 2025/early-2026 quarters (see §4 caveat).
- **Reverse DCF:** using FY2027 consensus EPS $10.20 and an industrial FCF-conversion haircut of ~85% (≈$8.67 FCF/share, in line with HON's historical capex-light industrial-automation mix), r = 8.5% (reflecting 3x leverage and integration/carve-out execution risk), P=$226 implies **g ≈ 4.3–4.6%** perpetual FCF growth — a moderate, not aggressive, bar.
- **implied_vs_base: in_line.** My base case for the automation-only pure-play (mid-single-digit organic growth, further margin expansion from mix shift toward higher-margin automation/software, offset by dis-synergy costs from the breakup) lands at ~4–5% FCF growth too. The re-rating thesis from triage is therefore **already mostly reflected in the price** rather than still ahead of it — this is the main reason I am not calling this INCLUDE outright.

## 8. Bull case
1. Focused automation pure-play removes the aerospace-cycle and advanced-materials-cycle noise that previously obscured segment economics; management can now be judged on one set of KPIs.
2. Software/recurring-revenue mix (building management, process control analytics) should support margin expansion as the standalone cost structure is right-sized.
3. Consensus 2027 EPS of ~$10.20 has not been walked back despite the messy separation quarter, suggesting sell-side confidence in the standalone base.

## 9. Bear case
1. Net debt/EBITDA ~3x plus continued buybacks during a negative-OCF quarter (Q1 2026) is an aggressive capital-allocation combination for a company mid-separation.
2. The FY2025/2026 income statement is genuinely hard to read cleanly (conflicting XBRL tags, large one-time gains) — a real earnings-quality flag, not just a modeling inconvenience, until the Q2 2026 10-K/10-Q is read line-by-line.
3. Standalone dis-synergy costs (shared services, IT, real estate previously spread across three businesses) are a known post-spin risk that has sunk other three-way breakups' first 12–18 months of margin guidance.

## 10. Key risks & kill criteria (measurable)
1. Net debt/EBITDA (consolidated, per 10-Q) stays above 3.25x for two consecutive quarters post-separation.
2. Standalone FY2026 or FY2027 EPS guidance (ex. separation/one-time items) is cut versus the first post-spin baseline set at or after the Q2 2026 release.
3. Organic (like-for-like) revenue growth in Building or Industrial Automation segments falls below 2% for two consecutive quarters.
4. Any material weakness or restatement disclosed in the Q3 2026 or FY2026 10-K tied to the carve-out accounting (a real risk given the XBRL inconsistencies already observed).
5. Standalone free cash flow conversion (OCF−capex)/NI falls below 70% for two consecutive quarters, signaling separation cash costs are structural rather than transitory.

## 11. Catalysts & calendar
- Next earnings: **Q3 2026, Thursday 2026-10-22** (before market open; confirmed via investor.honeywell.com press release).
- First full standalone-guidance reset (if not already given at Q2 2026) is the key near-term catalyst to resolve the data conflicts in §4/§5.

## 12. Red-flag scan
- **DOJ settlement, 1 Sep 2026:** Honeywell Aerospace Inc. (now HONA, not this HON entity) paid ~$2.04mn to resolve a False Claims Act cybersecurity-compliance matter (DoD contract, conduct 2020–2023) — entity-scoped correctly here per the wave-3 mandate; not a HON (Technologies) liability going forward, though legacy indemnification terms in the Separation Agreement were not verified in this pass and should be checked before fully dismissing it.
- **Resolved:** DOJ/SEC investigation into a foreign subsidiary's dealings with Unaoil S.A.M. — deferred-prosecution agreement terminated early and charges dismissed with prejudice (Jul 2025), per company disclosure.
- General "other lawsuits" boilerplate (commercial, product liability, environmental) disclosed per usual 10-K risk factors; nothing else materially adverse surfaced in this pass.
- No auditor change or going-concern language found.

## Data basis, recency and disclaimer
Most recent period incorporated: Q2 2026 10-Q (period end 2026-06-30, filed ~Jul/Aug 2026) via XBRL companyfacts; cross-checked against the confirmed Q3 2026 earnings-date press release. Checked for events to 2026-09-25. **This dossier carries an explicit, unresolved data-quality flag on FY2025–Q2 2026 GAAP figures (see §4/§6) that a follow-up pass should resolve by reading the Q2 2026 10-Q financial statements directly** rather than relying on the XBRL facts API. GAAP vs. adjusted labelling: all figures above are GAAP as tagged; no adjusted/non-GAAP reconciliation was sourced in this pass. Research, not personal investment advice.
