from pathlib import Path
import json,csv
r=Path('review')
p=r/'deep_audit/01_filing_audit.md'
s=p.read_text(encoding='utf-8')
s=s.replace('A **2.7x** claim was not substantiated by the examined tables and is quarantined; 2.55x remains a management metric, not independently replicated covenant leverage.', 'The original cached vendor net-debt/EBITDA ratio rounds to **2.7x**, while the company reports **2.55x** under its management definition. The latter is not a same-basis correction of the former. Their numerator/denominator bridge remains unresolved; neither is independently replicated covenant leverage.')
s=s.replace('Microsoft corroboration is added to the machine ledger only if its complete response is present and matches the filing calculation.', 'Microsoft’s actual displayed annual response likewise gives FY2026 CFO $182,935m, signed capex −$115,948m and FCF $66,987m. Its retained JSON contains selected fields transcribed from the complete Raw UI display because the download did not complete; it is not a byte-for-byte raw response. The provider access ledger records this distinction. Both corroborations are included in the 33-row field ledger.')
p.write_text(s,encoding='utf-8')
p=r/'deep_audit/build_filing_ledger.py';s=p.read_text(encoding='utf-8')
s=s.replace("notes='Separate provider transformation, common underlying issuer filing. Zero optional fields do not establish actual zero. Does not independently certify TTM or prices.'", "notes=('Full downloaded JSON. ' if ticker=='NVDA' else 'Selected fields transcribed from actual full Raw UI response; not full raw payload. ')+ 'Capture method and access: 00_provider_access_ledger.json. Separate provider transformation, common issuer origin. Zero optional fields are not established actual zeros. Does not certify TTM or prices.'")
p.write_text(s,encoding='utf-8')
p=r/'INVESTMENT_COMMITTEE_REVIEW.md';s=p.read_text(encoding='utf-8')
s=s.replace('## What was reviewed', '''## Deep-data extension: three additional parallel audits

The completed extension adds filing/footnote reconciliation, market/forecast reconciliation, and historical-lineage validation. Nine specialist agents have now contributed in total; the original adversarial reviewer is checking this extension. The detailed findings, source contracts, repaired series and unresolved gates are in **DEEP_DATA_AUDIT.md** and the dashboard’s **Three deep data audits** tab.

- NVIDIA conventional TTM FCF is $127.006bn and company-defined FCF $126.886bn; Microsoft FY2026 conventional FCF is $66.987bn. Saved quarterly totals support these, while the ambiguous headline fields differ materially. They require quarantine, not blind substitution into a valuation.
- Airbnb’s $1.3bn/35% quarterly FCF claim is valid rounding: exact FCF $1.253bn and adjusted EBITDA $1.261bn. This resolves the earlier ambiguity in favor of the filing.
- All 14 September 24 closes now have external corroboration; two also match actual authenticated FMP responses. Forecast accounting basis is clearer, but original estimate vintages remain unverified.
- A September 22 outage affected 438 stocks plus benchmark. Separate-source observations repaired all 12 affected finalists and benchmark; 426 other stock gaps remain. Portfolio daily-volatility diagnostic changes 15.9939% to 15.9239%; weekly endpoint volatility is unchanged.
- The 2023 validation slice had only one observed revenue-growth value and five EPS-growth values among 485 stocks. It cannot establish the intended growth strategy’s historical validity.

These findings supersede conflicting statements in the preserved first six reports. Three genuinely deeper reviews do not make every source complete or independent. The decision remains to withhold new deployment under the original model.

## What was reviewed''')
s=s.replace('exact end-of-day prices have not been certified against a second independently sourced exchange feed; consensus EPS horizons and accounting bases remain unresolved. None is marked independently certified in the ledger.', 'all 14 snapshot closes are externally corroborated, with actual FMP responses for NVDA/MSFT; no complete raw exchange-feed history is certified. Public forecast displays specify adjusted EPS and fiscal years, but original forecast vintages, conflicting snapshots and contributor coverage remain unresolved. Updated per-name statuses are in the deep market ledger.')
s=s.replace('not independently verified forecasts, and neither is automatically next-twelve-month P/E.', 'not historically vintage-certified forecasts, and neither is automatically next-twelve-month P/E. The later public forecast cross-check documents adjusted rather than GAAP EPS.')
p.write_text(s,encoding='utf-8')
p=r/'WEEKLY_INVESTMENT_POLICY.md';s=p.read_text(encoding='utf-8')
s += '''

## Mandatory three-pass data audit, added 26 September 2026

For each new or materially changed decision-critical input use three parallel bounded reviewers: (1) source filings/accounting bridges; (2) instrument, market session, corporate action and estimate definition/vintage; (3) historical availability, transformations and before/after portfolio impact. Preserve disagreement and shared source lineage. Reuse unchanged evidence only after event/freshness checks. Read DEEP_DATA_AUDIT.md and all deep_audit reports before each refresh.

- Archive full responses/documents when available; retain accession, acceptance/publication time, fiscal interval, tag/context/unit, transformation, ingestion time and hash. Label observation extracts and manual transcriptions accurately. A hash proves retained bytes, not source truth.
- Reject error responses, provider bundled samples, wrong symbols, wrong dates and stale last-good data. No access upgrade or paid feed is assumed. Current FMP access verified two names; Financial Datasets documentation alone validates no figures.
- Block affected signals on unexplained session gaps. Keep original and repaired series separately; do not fill daily holes with zeros or splice incompatible dividend-adjustment vintages. Recompute dependent measures and document materiality. The remaining 426-stock September 22 outage is unresolved.
- Use complete numerical GAAP/non-GAAP and cash-flow bridges. Do not confuse company-defined FCF, CFO less cash capex, economic owner earnings and after-finance-lease-principal cash. Keep forecast, management claim and actual separate.
- Require original forecast vintage and accounting definition; FY1 is not NTM. Require contemporaneous membership, genuine prior periods, original filing availability, restatements, delistings and transaction costs for strategy validation.
- Apply the requested Druckenmiller skill only after all five required reports pass strict schema and underlying-observation-date checks. File modification time is insufficient. Do not let absent market-top values imply zero risk or bearish agreement inflate directional conviction. The current two partial inputs cannot produce an allocation score.
- Update source corrections everywhere in the current decision view; retain earlier reports as dated evidence, clearly superseded. The corrected Airbnb quarterly FCF claim is supported. Quarantined vendor headline cash-flow fields are not proof that all saved quarterly statements are wrong.

The Sunday 18:00 Dubai automation was updated to include these requirements. No daily monitoring or brokerage execution was added.
'''
p.write_text(s,encoding='utf-8')
p=r/'data/universe_data_ledger_497.csv'
with p.open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
finals=set('NVDA CPAY AMP RL AME SNA ABNB NTAP PAYX MSFT IBKR HIG ALLE AIZ'.split())
for x in rows:
 if x['ticker'] in finals:
  x['quote_external_status']='Dated public display corroborated'+('; authenticated FMP agrees' if x['ticker'] in ['NVDA','MSFT'] else '; FMP current-plan access blocked')
  x['consensus_external_status']='Public adjusted-EPS display checked; original vintage unresolved'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print('Updated memo, policy, filing caveats, and 14 evidence statuses.')
