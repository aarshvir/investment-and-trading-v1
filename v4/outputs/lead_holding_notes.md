# Lead Holding Notes — T2 (holding-notes editor and consistency checker)

**As of:** 2026-09-26 · **Scope:** 12 current holdings (DLTR, HST, JBHT, ALL, GL, SWK, HIG, BMY, MTB, LMT, FRT, SYF)
**Source:** `v4\outputs\lead_holding_notes.json` (full detail: kill criteria, valuation reconciliation, jargon translated)

## Summary table

| Ticker | One-line thesis (plain English) | # kill criteria | Valuation consistent (dossier vs V1)? | Dossier edited? |
|---|---|---|---|---|
| DLTR | Dollar Tree's stores are healthy and fairly priced, but its eye-catching profitability is inflated by a shrunken balance sheet after the costly Family Dollar sale. | 5 | Yes (both "fair") | No |
| HST | Host owns top hotels with beating forecasts, an improved credit rating, and fair pricing, but next year's comparisons will be tougher. | 5 | Yes (dossier "fair" / V1 "attractive" — not a real conflict) | No |
| JBHT | J.B. Hunt is a strong, low-debt trucking company, but its stock price assumes a brief freight rebound continues, while two of five business lines struggle. | 5 | **No** (dossier "expensive," ~31% downside case; V1 "fair," +6.4%/yr) | **Yes** |
| ALL | Allstate's car and home insurance profits have surged, but the boom is temporary, and Wall Street already expects a big profit drop next year. | 5 | Yes (both "fair") | No |
| GL | Globe Life sells simple life and health insurance through career agents, keeps beating its own raised forecasts, but faces an unresolved lawsuit over sales conduct. | 5 | Yes (dossier "cheap" / V1 "fair" — minor variance) | No |
| SWK | Stanley Black & Decker looks historically cheap after a cost-cutting program, but last quarter's gain leaned heavily on a one-time tariff refund and asset sale. | 5 | Yes (both "cheap"/"attractive"; dossier already self-reconciles the gap in its own §13) | No |
| HIG | Hartford's underwriting is strong, but recent profit gains came mostly from one-time tax and settlement items, and pricing power in its core business is fading. | 5 | Yes (dossier quotes V1's own "fair" verdict verbatim) | No |
| BMY | Bristol Myers has strong new drugs replacing declining older ones, but a government price cut on its top drug is now hurting cash flow. | 5 | **No** (dossier "fair-value, not a bargain"; V1 "attractive," score 1.0, needs a 9.4x→24.9x re-rating) | **Yes** |
| MTB | M&T Bank's lending profits keep improving as deposit costs fall and loan quality improves, with analysts raising forecasts, not cutting them. | 5 | Yes (dossier quotes V1's own "fair" verdict verbatim) | No |
| LMT | Lockheed's missile business is booming with record orders, but the company keeps taking big write-offs on troubled programs, including one still-unresolved classified contract. | 5 | Yes (dossier quotes V1's own "fair" verdict verbatim) | No |
| FRT | Federal Realty's shopping centers keep raising rents, with guidance raised or held every quarter for two years, and shares are near their cheapest ever. | 5 | Yes (dossier adopts V1's "attractive" verdict directly) | No |
| SYF | Synchrony lends through store credit cards for Amazon, Lowe's and others; profit growth has come mostly from fewer bad-loan charges, now leveling off. | 5 | **No** (dossier "fair," already pricing in credit-normalization risk; V1 "attractive," +31.2%/yr, exceeds Street's high target) | **Yes** |

## Notes

- **Kill criteria:** all 12 holdings now have 5 measurable, dossier-verbatim exit triggers in the structured JSON (`kill_insufficient: false` for all). SWK and SYF specifically — flagged by the loop-1 audit as having kill criteria in the dossier but not in structured data — are now captured; SYF also had no `f2/SYF/summary.json` in `outputs/` or cache (only intake/ratios/valuation work files), so its structured data was sourced directly from the dossier.
- **Valuation reconciliation (3 real conflicts found and fixed):** JBHT, BMY and SYF each had a dossier valuation read materially at odds with V1's systematic verdict (the same failure pattern flagged for RL in loop-1, though RL itself is no longer a current holding). For each, a **"Valuation reconciliation with V1 (added 2026-09-26)"** paragraph was appended to the end of the dossier's existing valuation section (Section 7), stating V1's verdict/base case, the dossier's own view, and which is better supported and why — using only numbers already present in the dossier or in V1. No other dossier text was changed.
- **Nine holdings were already consistent** (DLTR, HST, ALL, GL, SWK, HIG, MTB, LMT, FRT). Several of the most recently written dossiers (HIG, MTB, LMT, FRT, SWK) already quote V1's own verdict/score directly in their own §7, so they were self-consistent by construction; no dossier edits were needed for these.
