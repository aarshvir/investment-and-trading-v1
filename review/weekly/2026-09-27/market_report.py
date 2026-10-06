import json,pathlib,hashlib,datetime,csv
O=pathlib.Path('review/weekly/2026-09-27');R=O/'raw_market';d=json.loads((O/'market_audit.json').read_text())
events=[{'ticker':'AMP','publication_date':'2026-09-24','event_date':'2026-10-29','event':'Q3 results approximately08:15ET; conference call09:00ET','source_url':'https://www.nasdaq.com/press-release/ameriprise-financial-announces-schedule-third-quarter-2026-investor-conference-call','original_source_url':'https://www.businesswire.com/news/home/20260924689143/en/','source_type':'issuer press release distributed by BusinessWire and hosted byNasdaq','status':'schedule_observed_in_search_indexed_issuer_syndication_direct_page_unavailable_overall_event_clearance_UNKNOWN','retrieved_date':'2026-09-27'},{'ticker':'NTAP','publication_date':'2026-09-25','event':'Intent to acquirePEAK:AIO; customary closing conditions/regulatory approvals remain; consideration not disclosed in the read release','source_url':'https://investors.netapp.com/news/news-details/2026/NetApp-Announces-Intent-to-Acquire-PEAKAIO-to-Advance-Scalable-AI-Infrastructure-Architecture/default.aspx','status':'material_pending_acquisition_newly_read_primary_release; no quantifiedEPSupgrade','retrieved_date':'2026-09-27'}]
(R/'new_event_observations.json').write_text(json.dumps(events,indent=2))
head='''# Weekly market and forecast audit — 27 September 2026

Author: Codex market audit. Status: research inputs for the next release; no trading authorization. Parents: **v011_2026-09-27_claude** and **v005_2026-09-26_codex**. Market cutoff: completed US regular session **25 September 2026**. Newly retrieved Cboe responses carry exact UTC retrieval timestamps in the ledger; underlying session dates remain September 25. Public webpages were viewed September 27. Prices are USD per listed share, not live executable orders.

## Decision-relevant changes

AMP closed **$493.00**, below its existing $500 ceiling. PAYX closed **$101.37**, below $101.80. These satisfy only the price condition; the other thesis, event, account and risk conditions remain necessary. None of the other twelve original candidates crosses its existing v005 entry ceiling. The parent report determines whether the business cases support action.

Correct MSFT's v005 September 25 reference from **$516.05 to $516.17**: new Cboe data, the dated [StockAnalysis history](https://stockanalysis.com/stocks/msft/history/) and archived Yahoo/CNBC agree. This is a correction within the same session, not a one-day return. No limit crossing results.

NTAP has a precision disagreement: newly retrieved Cboe and archived Yahoo show **$201.145**, whereas archived CNBC and the [dated public history](https://stockanalysis.com/stocks/ntap/history/) show **$201.15**. Use $201.15 as the cent-denominated reference; retain both observations and the $0.005 difference. Do not call them exact matches or infer a material economic discrepancy.

## What was actually checked

- **34/34** unique names (original14 plus v011's20, with no overlap) returned new Cboe HTTP200 responses with matching symbol and September25 last-trade dates. Full JSON responses are preserved, not merely copied prices.
- **7/34** also received newly viewed public dated-history checks: AMP, PAYX, MSFT, NVDA, ALLE, HIG and NTAP. Header, historical row, session date and USD denomination agree, apart from the documented NTAP precision difference.
- **503/503** inherited universe rows have September25 prices and USD currency. Recomputing from the immutable release confirms all503 within0.5% of both Cboe and CNBC. This is recalculation of inherited evidence, not503 fresh downloads; **469 names were not newly fetched**.
- **503/503** original Cboe cache payloads were available locally; their identity and close match the archived validation CSV. Copies with original retrieval metadata and hashes are preserved here. CNBC cache batches are also preserved. The immutable v011ZIP contained the derived data but not these raw Cboe files; raw caches are therefore separately identified as inherited local evidence.
- The six inherited market files used here are byte-identical between the v011ZIP and the active v4 folder. Copies were read from the release archive; no v4 or earlier release was edited.

The inherited report's “501 exact” Cboe matches uses relative error below1e-6. Strict equality within $1e-8 produces **495**, while CNBC gives498. Its broad conclusion of all503 within0.5% reproduces. A 0.5% threshold is a diagnostic tolerance, not acceptable hidden execution slippage. All individual raw differences remain available.

Cboe response-generation timestamps can fall on September26 even when last_trade_time belongs to September25. New responses can reset prev_day_close to the latest completed close; do not derive September25 daily returns from that field without checking its date semantics. CNBC's inherited timestamps are sometimes16:10ET, not uniformly16:00ET as prose might suggest. Price agreement alone does not certify the exchange's official closing auction feed or vendor upstream independence.

The specific StockAnalysis **history pages** now explicitly identify **S&P Global Market Intelligence** as their historical-price provider. That endpoint-specific attribution is more precise than the previous audit's general Cboe/UTP site-provenance language. Historical prices are split-adjusted according to the page; the separate adjusted-close column may also reflect dividends. This audit compares the displayed Close column. RL's September25 $1 dividend requires matching adjustment vintages before repairing past returns; a simple raw-price comparison is not total return. No full corporate-action database was newly downloaded.

## Forecast evidence: context, never automatic approval

The 503-row September25 consensus snapshot is reused with its original retrieval timestamps. Its quality counts reproduce:366 “ok”,92 “caution”,45 “unreliable”. Those labels only reflect the original mechanical diagnostics. **Every record has automatic-valuation acceptance set to false.** Original annual time-weighted EPS is labeled an approximation, not independently verified four-quarter NTM or our normalized earnings forecast.

New public display checks cover **AMP, PAYX and PGR only**. [AMP](https://stockanalysis.com/stocks/amp/forecast/) shows FY2026/FY2027 adjusted EPS46.53/51.67; page-updateSeptember22. [PAYX](https://stockanalysis.com/stocks/payx/forecast/) shows FY2027/FY2028 EPS5.96/6.39; page-updateSeptember25. Both broadly corroborate the reused estimates, not their as-of publication vintage or accounting bridge. Analyst submission timestamps, full contributor histories and next-year dispersion were not newly acquired. The other31 forecasts were not newly independently retrieved.

**PGR is a hard rejection for forward EPS/NTM.** The inherited FY2027 EPS is$1,012 with one contributor, producing approximate NTM$747.864. The [newly viewed public page](https://stockanalysis.com/stocks/pgr/forecast/) also displays1.01K: cross-vendor agreement propagates the anomaly instead of validating it. v011's PGR dossier already explicitly quarantines this data and uses trailing/underwriting analysis; credit that safeguard. The original snapshot's “caution” flag is too weak for automatic consumers. Do not repair the figure by guessing a missing decimal point. GDDY also retains a mismatch between info and trend EPS and remains caution.

## Event updates and boundaries

Ameriprise's [issuer announcement hosted by Nasdaq](https://www.nasdaq.com/press-release/ameriprise-financial-announces-schedule-third-quarter-2026-investor-conference-call), published September24, confirms results October29 at approximately08:15ET and a09:00ET call. The issuer-announced schedule is corroborated in search-indexed syndication. Direct opens of Nasdaq and BusinessWire failed on the closure recheck, and the dynamic issuer calendar remains unknown. The exact search-tool capture and failed direct opens are preserved in raw_market/amp_schedule_search_capture.json; it is not a downloaded primary webpage. This confirms what was announced, not a clean overall event clearance.

NetApp's [September25 issuer announcement](https://investors.netapp.com/news/news-details/2026/NetApp-Announces-Intent-to-Acquire-PEAKAIO-to-Advance-Scalable-AI-Infrastructure-Architecture/default.aspx) states its intent to acquire PEAK:AIO. Classify this as a **material pending acquisition**, not an ordinary calendar update. Closing remains subject to conditions/approvals. The read release supplies no consideration or quantified EPS contribution, so no value increase is assigned here.

For all34 names, the ledger retains the inherited next-earnings date and whether the vendor called it estimated. A false estimate flag does not independently prove issuer confirmation. This market subaudit does **not** claim an exhaustive new SEC/IR event sweep or an absence of adverse news for34; the parallel filing audit supplies that coverage. Fund NAV and dealing-price checks are handled by the parent workstream and are not misclassified as equity quotes here.

## Accepted session reference prices

Each name links to the newly retrieved source endpoint. Exact retrieval and provider timestamps, inherited observations, explicit conflicts, forecast vintage and limits are in market_audit.json. All rows refer to September25,2026.

|Ticker|Reference close USD|Prior v005 reference|Existing ceiling|Price condition|
|---|---:|---:|---:|---|
'''
for r in d['rows']:
 prior=r.get('original_v005_reference');lim=r.get('existing_limit');gate=('Below/equal' if r.get('below_existing_limit_price_only') else 'Above') if lim is not None else 'Not set by this audit'
 head+=f"|[{r['ticker']}]({r['new_cboe_url']})|{r['accepted_close']:.2f}|{prior if prior is not None else '—'}|{lim if lim is not None else '—'}|{gate}|\n"
head+='''
## Primary fund identity cross-check

The parent's newly downloaded primary HTML was independently inspected against its source hashes. VUAA is the USD London listing of accumulating Irish share class **IE00BFMXXD54**; the September 25 USD NAV history row is **149.7632**, rounded to 149.76 in the header. The page's **GBP 112.80** market price belongs to the VUAG London listing, not USD VUAA. IB01 is the USD London listing of accumulating Irish share class **IE00BGSF1X88**, with September 25 NAV **USD 121.89**. Both pages disclose a 0.07% annual fund fee. These are NAVs for sizing illustrations, not exchange quotes. [Vanguard primary product page](https://www.vanguard.co.uk/professional/product/etf/equity/9694/sp-500-ucits-etf-) and [iShares primary product page](https://www.ishares.com/uk/individual/en/products/307243/ishares-treasury-bond-0-1yr-ucits-etf-fund). August 31 portfolio weights remain explicitly dated; they were not refreshed by a September 25 NAV observation.

## Adopted, changed and unresolved

Adopt v011's dated price snapshot after recalculation and raw-response cross-check; adopt its quarantine of contaminated company-name metadata and its warning on PGR. Change v005's MSFT reference, update13 other names to the next completed session, and label approximate NTM explicitly. Preserve the material distinction between source agreement, field validity and investment merit. No allocation, hurdle or issuer earnings assumption is changed by this subaudit.

The web finance batch produced no usable tool response and is recorded as failed. No new FinancialDatasets/FMP request or provider purchase occurred. No failed fetch has been replaced by a fabricated zero or a stale figure labeled fresh. The remaining needs are full point-in-time consensus lineage, primary event closure for each actionable name, and current broker quotes when an authorized trade is actually considered.
'''
(O/'market_audit.md').write_text(head,encoding='utf-8')
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='manifest.json':manifest.append({'path':str(p.relative_to(O)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
for name in ['market_audit.json','market_audit.md','market_fetch.py','market_build.py','market_report.py']:
 p=O/name;manifest.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(R/'manifest.json').write_text(json.dumps({'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':manifest},indent=2))
print('report written; manifest files',len(manifest))
