# D1 — S&P 500 point-in-time membership, identifiers & sectors (report)

**Status: delivered (v1, 2026-09-26).** PIT, survivorship-free S&P 500 membership 1996-01-02 → 2026-09-25 at entity (CIK) level, with CIK-dated intervals, a monthly membership matrix, a CIK map and a SIC→sector map.

## Answer first
- **Membership:** 1,271 intervals and 1,217 entities. The monthly count since 2000 stays between **499 and 506** (median 500). The last month (2026-09-25) has **503 lines**, and they match Wikipedia's current table exactly (503/503 tickers).
- **CIK coverage:** **99.99 %** of the 161,066 member-months since 2000 have a high- or medium-confidence CIK (95.76 % high, 4.23 % medium, 0.01 % none). Two entities are unresolved: `NLV-200001` (removed 2000-01) and `USB-200102` (old U.S. Bancorp, removed 2001).
- **Sectors:** the SIC-derived sector agrees with actual GICS for **87.9 %** of current members after tuning (82.1 % before tuning). Nine SIC codes were overridden. Agreement on current members whose SIC code was *not* tuned is 87.5 %. For historical entities it is 84.0 %, measured against the last GICS sector Wikipedia showed for them.
- **Look-ahead input:** 250 index additions have happened since 2015-01-01 (185 of those entities are still members). **36.8 % of today's 503 lines were added after 2015**, which is the survivorship/look-ahead exposure of a backtest that uses today's constituents.

## Sources and final membership decision
- **Primary source:** fja05680/sp500. For 1996-01-02 → 2019-01-11 we use the **original** file (Clenow/Norgate symbols). For 2019-01-12 → 2026-08-18 we use the **Updated** file. The 2026-09-21 change comes from Wikipedia (fja ends on 2026-08-18).
- **Why the original file for the early period:** the Updated file strips Norgate's `-YYYYMM` delisting suffix and de-duplicates. That silently merges different companies that shared a ticker (for example Tyco `JCI` vs Johnson Controls `JCI-201609`, or NationsBank `BAC` vs BankAmerica `BAC-199809`).
- **Validation sources:** 235 month-end snapshots of Wikipedia's "List of S&P 500 companies" page history (2007-03 → 2026-09); the change table, which has moved to <https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500>; and SEC data (company_tickers, cik-lookup-data, submissions API).

**Fixes applied to fja** (logged in `cache/d1/fja_diag.json`):
1. Ten artifact duplicates in the original file were merged (for example AET and AET-201811 are the same company).
2. Data-seam duplicates were removed: KORS/CPRI in 2016-01 → 2018-09 and CCE/CCEP in 2016.
3. Linde plc (LIN), missing from the original file, was added from 2018-10-31.
4. Wikipedia's 2026-09-21 rebalance was applied: BE, P and ILMN in; TAP, TTD and BLDR out.

## Reconciliation results
- **fja vs Wikipedia current list:** fja's last row (2026-08-18) differs from Wikipedia only by the three 2026-09-21 swaps. After those are applied, the match is 503/503.
- **fja vs Wikipedia month-end snapshots (2007-03 → 2026-09):** 99.62 % of 118,081 fja key-months link to a row in the Wikipedia list at the same month-end.
  - 414 Wikipedia rows are unlinked; they are mostly Wikipedia editing lag of one or two months.
  - 80 at-the-time ticker pairings were accepted by co-occurrence plus name gating (for example PCLN→BKNG, YHOO→AABA, TYC→JCI, WLP→ANTM).
- **Walking the Wikipedia change table backwards from the current list:** implemented in `d1_wiki_reconstruct.py`. It gives 506 names at 2020-01, 504 at 2015-01, 508 at 2010-01 and 513 at 2000-01, which drifts upward because the table only lists *selected* changes. It also produced 26 anomalies: renames and ticker reuse such as FB, FLT, IR, AGN and T.
- **Still open:** the entity-space agreement rate at every change date since 2000 was **not computed** (deprioritised at the lead's request). The month-end snapshot comparison above is the validation that was run.

## Identity rules
- **entity_id:** `CIK##########` using the company's latest CIK. A secondary share-class line gets `<id>.<TICKER>`, for example `CIK0001652044.GOOG`. An entity with no CIK gets `NG:<Norgate key>`.
- **CIK candidates** came from the Wikipedia CIK column (2014+), the current Wikipedia table, the SEC ticker table, and exact or fuzzy name matches in cik-lookup-data.
- **CIK verification:** a candidate needs at least one 10-K, 10-Q, 20-F or 40-F filed inside the membership window, and the name must agree.
- **Analyst name hypotheses** (`d1_manual.py`, 170 keys removed before 2007) were used only as search keys. Their confidence is capped at medium.
- **R1 — ticker reuse across keys.** Example: IR → TT on 2020-03-03, after which the IR symbol belongs to the new Ingersoll Rand Inc.
- **R2 — same ticker added and removed in the Wikipedia table.** Treated as a new company. Example: FOXA/FOX on 2019-03-19 (21st Century Fox → Fox Corp).
- **R3 — other CIK changes.** Treated as a reorganisation of the same entity, with a new interval row. The boundary is the successor's first 10-K/10-Q. There are 15 cases (Google→Alphabet 2015-10-29, Medtronic plc, Disney 2019, Cigna 2019, Mylan N.V., and others).
- **Interval semantics:** `start_date` is inclusive (the effective date). `end_date` is exclusive (the first day *not* in the index). A blank `end_date` means the entity is still a member.
- **Monthly matrix:** indexed on the last NYSE trading day of each month (a rule-based calendar that removes Good Friday and Memorial Day). September 2026 uses 2026-09-25.

## Sanity checks
**Spot checks: 10/10 pass**, all agreeing with Wikipedia change dates:

| Company | Result |
|---|---|
| TSLA | Added 2020-12-21 |
| SIVB | Removed 2023-03-15 (reason: FDIC receivership) |
| PLTR | Added 2024-09-23 |
| AAPL | Continuous since 1996 |
| FB → META | One entity since 2013-12-23 (renamed 2022-06-09) |
| SMCI | Added 2024-03-18 and still a member |
| DELL | Old Dell 1996–2013-10-29; Dell Technologies from 2024-09-23 |
| ABNB | Added 2023-09-18 |
| APP / HOOD | Added 2025-09-22 |
| COIN / DASH | Added 2025-05-19 / 2025-03-24 |

**Additions / removals per year:**

| Year | Adds | Removals |
|---|---|---|
| 2000 | 54 | 55 |
| 2001 | 30 | 30 |
| 2002 | 22 | 23 |
| 2003 | 9 | 9 |
| 2004 | 19 | 18 |
| 2005 | 16 | 16 |
| 2006 | 32 | 32 |
| 2007 | 38 | 38 |
| 2008 | 35 | 35 |
| 2009 | 29 | 29 |
| 2010 | 16 | 16 |
| 2011 | 20 | 20 |
| 2012 | 18 | 18 |
| 2013 | 19 | 19 |
| 2014 | 16 | 14 |
| 2015 | 30 | 28 |
| 2016 | 29 | 28 |
| 2017 | 28 | 29 |
| 2018 | 24 | 23 |
| 2019 | 21 | 21 |
| 2020 | 16 | 17 |
| 2021 | 19 | 19 |
| 2022 | 15 | 17 |
| 2023 | 15 | 15 |
| 2024 | 17 | 17 |
| 2025 | 20 | 20 |
| 2026 | 16 | 16 |

The 1996 count includes the initial load. Pure ticker or CIK changes are excluded.

## Limitations
1. **Early-period counts:** 1996–2000 lists hold 499–501 names, and fja itself warns that a few names may be missing in the early years.
2. **Tickers before 2007-03:** `ticker_at_time` is back-filled from the first Wikipedia observation or taken from the Norgate symbol. For bankrupt names that is the last "Q" ticker; see `ticker_at_time_basis`.
3. **Predecessor CIKs before 2014:** for some pre-2014 plain keys the mapped CIK's filings start after the membership start (for example Ingersoll-Rand 1996–2009 is mapped to CIK 1466258). Fundamentals for those early periods will be **missing, not wrong**. Such rows are flagged in `d1_cik_map.notes` and the `cik_first_report` column.
4. **SIC is not point-in-time:** SIC comes from each entity's latest SEC record.
5. **Tuned sector overrides can hurt historical names:** codes 7370→Communication Services and 7320→Financials are driven by current members and may misclassify older software or credit names. `gics_sector_wiki_last` is provided as an alternative for historical names.
6. **Two entities have no CIK:** see the answer-first section.

## Open items (not done)
- The entity-space agreement rate between fja and the Wikipedia backward walk at every change date since 2000.
- A name-based predecessor search for plain keys whose CIK filings begin after the start of membership.
- More sector tuning (payments companies under SIC 7374/7389, internet companies).
- An EDGAR full-text-search cross-check of the analyst hypotheses.

## Files
**Data** (`v4\data`, each with a `.meta.json` sidecar):

| File | Rows / shape |
|---|---|
| `d1_current_constituents.csv` | 503 |
| `d1_membership_intervals.csv` | 1,271 |
| `d1_membership_monthly.parquet` | 369 months × 1,215 entities |
| `d1_cik_map.csv` | 1,232 |
| `d1_sector_map.csv` | 1,217 |
| `d1_sic_to_sector.csv` | 371 (observed SIC codes plus the range rules) |
| `d1_additions_since_2015.csv` | 250 |

**Code** (`v4\code`): `d1_common.py`, `d1_fetch_sources.py`, `d1_wiki_snapshots.py`, `d1_wiki.py`, `d1_fja.py`, `d1_snaplink.py`, `d1_sec_ref.py`, `d1_sec_fetch.py`, `d1_manual.py`, `d1_identity.py`, `d1_membership.py`, `d1_sic_sector_rules.py`, `d1_cik_sector.py`, `d1_out_current.py`, `d1_wiki_reconstruct.py`.

Run order: fetch_sources → wiki_snapshots → wiki → fja → snaplink → sec_fetch → identity → membership → cik_sector → out_current.

**Raw cache:** `C:\Users\user\eqv4\cache\d1\`.
