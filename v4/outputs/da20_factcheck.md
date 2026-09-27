# DA20 — Independent Second Valuation Leg: RSG and LH (Peer EV/EBITDA, EV/FCF, P/E)

**As of:** 2026-09-27 | **Auditor:** DA20 | **Scope:** RSG (Republic Services) and LH (Labcorp) each currently rest
on a single reverse-DCF valuation in their dossier. This builds an independent peer-multiple leg, per the DA17/GDDY
precedent (`v4/outputs/da17_factcheck.md`), and states whether it corroborates each dossier's valuation view.
**Read-only: no dossier or other file was edited.**

## Data sources and vintage

- RSG, LH, WM, DGX, IQV, CRL: `v4/data/d4_live_snapshot.parquet`, 25 Sep 2026 close (Yahoo-sourced fields: price,
  enterprise value, trailing EBITDA, free cash flow, net debt, NTM/forward P/E).
- WCN, CWST, GFL (not S&P 500 constituents, so absent from the parquet universe): stockanalysis.com
  (S&P Global Market Intelligence data), retrieved 2026-09-27, priced at the 25–26 Sep 2026 close; EBITDA/net-debt
  inputs behind the ratio as of each company's most recently reported quarter (site's own "last updated" stamp:
  23–31 Jul 2026). **Caveat:** this mixes a current price with a slightly older EBITDA/debt denominator (standard
  trailing-multiple practice, but a different vintage/source than the parquet names) — directional, not
  precision-grade, exactly as flagged for the GDDY peer leg in DA17.
- All EV/EBITDA and EV/FCF figures below are trailing (TTM-basis) unless marked forward/NTM.

## RSG (Republic Services) — peer table

| Ticker | EV ($bn) | EV/EBITDA | EV/FCF | Net debt/EBITDA | NTM or fwd P/E |
|---|---|---|---|---|---|
| **RSG** | 79.33 | **15.09x** | **40.85x** | **2.70x** | **27.02x (NTM)** |
| WM | 105.92 | 13.63x | 45.07x | 2.93x | 23.36x (NTM) |
| WCN | 48.75 | 15.60x | 40.03x | 3.05x | 26.62x (fwd) |
| CWST | 6.65 | 15.88x | 62.96x | 3.39x | 66.09x (fwd)* |
| GFL | 22.41 | 19.00x | 151.0x | 5.94x | 46.34x (fwd)† |

\* CWST's TTM P/E (917.6x) and even its forward P/E are distorted by depressed near-term GAAP earnings (TTM net
income only $5.7m); not a clean like-for-like comparator on P/E.
† GFL was TTM-unprofitable (TTM net income −$173.4m); trailing P/E not meaningful, forward P/E shown only.

**Read:** RSG's EV/EBITDA (15.09x) sits *below* WCN (15.60x) and CWST (15.88x), *above* only WM (13.63x), and well
below GFL (19.00x). Its EV/FCF (40.85x) is essentially tied with WCN (40.03x), cheaper than WM (45.07x), and far
cheaper than CWST (62.96x) and GFL (151.0x). RSG also carries the lowest leverage in the set (2.70x net
debt/EBITDA vs. 2.93x–5.94x for peers) — the recomputed 2.70x independently matches the dossier's own §6
recalculation (~2.5–2.7x), corroborating that figure. On NTM/forward P/E, RSG (27.02x) is essentially equal to WCN
(26.62x) and above WM (23.36x), but below CWST/GFL's earnings-distorted multiples.

**Verdict on the "27x — highest multiple outside VEEV" framing:** true as a statement about this portfolio, but
the EV/EBITDA and EV/FCF peer leg shows RSG is *not* an outlier versus its closest same-industry peers — 15–20x
EV/EBITDA is the going sector rate, and RSG sits mid-pack while running the lowest leverage and (per the dossier's
§3) the highest margin discipline (32%+ adjusted EBITDA margin, price-led growth) of the group. **The premium
RSG does carry is small (mainly vs. WM) and is explained by margin/returns quality, not an unexplained anomaly.**
This corroborates, rather than contradicts, the dossier's reverse-DCF "price implies growth below base case" view:
a name priced in-line-with-or-below higher-levered, lower-quality peers is not being priced for aggressive growth.

## LH (Labcorp) — peer table

| Ticker | EV ($bn) | EV/EBITDA | EV/FCF | NTM or fwd P/E |
|---|---|---|---|---|
| **LH** | 31.75 | **13.69x** | **35.60x** | **15.92x (NTM) / 15.61x (fwd)** |
| DGX (duopoly peer) | 32.27 | 14.25x | 35.48x | 19.98x (NTM) / 19.60x (fwd) |
| IQV (CRO/biopharma-services) | 59.57 | 19.55x | 27.71x | 19.23x (NTM) / 18.70x (fwd) |
| CRL (CRO/biopharma-services) | 16.95 | 19.96x | 36.16x | 23.75x (NTM) / 23.07x (fwd) |

**Read:** LH is the cheapest of the four names on every multiple except EV/FCF, where it is essentially tied with
DGX and IQV's superior FCF conversion (27.71x) makes IQV look better only on that one metric. On EV/EBITDA, LH
(13.69x) is ~4% below its direct clinical-lab duopoly peer DGX (14.25x) and ~30% below CRO-adjacent comparators IQV
and CRL (19.6–20.0x). On forward P/E, LH (15.61x) is 20% cheaper than DGX (19.60x) and 16–34% cheaper than
IQV/CRL. The dossier's own reverse-DCF price ($304, "~2026-09-23, not independently confirmed") is close to but
not identical to the confirmed 25-Sep-2026 close used here ($309.64, ~1.9% higher) — immaterial to the conclusion,
but the parquet close should now be treated as the confirmed figure.

**Verdict:** the peer leg strongly **corroborates** the dossier's reverse-DCF finding that LH's price implies
low (~3%) perpetual FCF growth versus a ~7–8% base case: LH is priced at a discount to both its direct duopoly
peer and to CRO-adjacent comparators on essentially every multiple checked, despite two consecutive quarters of
raised guidance and margin expansion (dossier §3/§5). This is independent, cross-methodology support for the
INCLUDE / below-base-case thesis, not a mere restatement of the single reverse-DCF already in the dossier.

## Summary by status (facts in `v4/outputs/da20_factcheck.json`)

| Status | Count |
|---|---|
| PASS | 5 |
| MINOR | 2 |
| FAIL | 2 |
| **Total facts** | **9** |

Note on the two FAIL-status facts: both concern RSG's narrow "27x is the highest multiple outside VEEV" framing
taken as a claim of general overvaluation versus its closest EV/EBITDA/EV/FCF-comparable peers (WCN, CWST, GFL) —
on those two specific multiples RSG is not more expensive than those peers, so the framing is contradicted at the
multiple-by-multiple level even though the *bottom-line* reverse-DCF conclusion ("implied growth below base
case") is corroborated at the synthesis level (see the final RSG fact, PASS). Nothing here implies the dossier's
verdict is wrong; it flags that the specific "highest multiple" language should not be read as "priced for growth
in excess of peers," which the peer data does not support.
