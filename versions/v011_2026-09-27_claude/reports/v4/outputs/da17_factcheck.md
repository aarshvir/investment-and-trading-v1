# DA17 — Targeted Fact-Check Sweep (loop-8 must-fix)

**As of:** 2026-09-27
**Scope:** For CRH, COR, LVS, VEEV, GDDY, TJX — verify each dossier's most-recent-reported-quarter revenue, GAAP
net income, diluted EPS (GAAP and adjusted where stated), period label/end date, and prior-year comparative
against primary SEC sources (8-K Ex-99.1 earnings releases, 10-Q/10-K XBRL company-concept data). This sweep
targets the specific bug pattern found by an earlier check: a dossier whose "latest quarter" net income was
actually the prior-year column. Additionally, for GDDY, an independent peer EV/FCF and EV/EBITDA cross-check
against the dossier's reverse-DCF "below base case" valuation view.

Do not edit dossiers or any other file — this is a read-only audit output.

## Summary by status

| Status | Count |
|---|---|
| PASS | 27 |
| MINOR | 0 |
| FAIL | 0 |
| UNVERIFIABLE | 1 |
| **Total facts** | **28** |

No FAILs found. The one bug this sweep was specifically targeting — TJX's "latest quarter" net income actually
being the prior-year column ($1,243M shown as current when it was the Q2 FY2026 comparative; true Q2 FY2027 net
income is $1,520M) — was **already caught and corrected** in TJX.md's Correction section (dated 27 Sep 2026, from
fact-check DA14) before this sweep ran. Independent re-verification against SEC XBRL (`NetIncomeLoss` tag,
accession 0000109198-26-000048) and the 8-K Ex-99.1 earnings release confirms the correction is accurate: $1,520M
is the correct current-quarter figure, and $1,243M is confirmed to be the true prior-year (Q2 FY2026) comparative.
No other dossier in this batch (CRH, COR, LVS, VEEV, GDDY) exhibits this or any other net-income/EPS/revenue
figure error for its latest reported quarter — all core quarterly figures matched primary sources exactly.

## GDDY valuation cross-check

Independent peer comparison (Wix.com/WIX, Tucows/TCX, VeriSign/VRSN, Shopify/SHOP; live multiples via
stockanalysis.com, retrieved 2026-09-27) shows **GDDY trading at EV/EBITDA 10.83x and EV/FCF 8.77x**, materially
below all four named peers on every available multiple (WIX EV/FCF 10.1x; VRSN EV/EBITDA 23.0x / EV/FCF 25.6x;
TCX EV/EBITDA 32.6x; SHOP EV/EBITDA 74.2x / EV/FCF 75.6x). This **corroborates** the dossier's reverse-DCF finding
that GDDY's price implies a decline in FCF that is not supported by fundamentals — i.e., the "below base case"
(cheap) view holds up on an independent, peer-multiple basis, not just the reverse-DCF. Caveat: the peer data
reflects the retrieval-date snapshot from a third-party site rather than the dossier's own 2026-09-25 valuation
date, and the peer set differs in growth/margin profile (SHOP is high-growth, TCX is small-cap with negative FCF,
WIX is mid-turnaround) — this is a directional corroboration, not a precise fair-value cross-check.

## Notes

- One fact (CRH's FY2025 full-year net income/EPS, cited only in dossier narrative prose, not the quarterly table)
  is marked UNVERIFIABLE because it was out of scope for this quarter-focused sweep and was not independently
  re-pulled from XBRL in this pass; it does not affect any of the verified latest-quarter figures, which all
  passed.
- Full detail (claim, dossier location, source document + accession, source value, status, note) for all 28 facts
  is in `v4/outputs/da17_factcheck.json`.
- No dossier or other file was edited. This is a standalone audit output per the assignment.
