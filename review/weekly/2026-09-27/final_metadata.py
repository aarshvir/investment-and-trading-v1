from pathlib import Path
import json
P=Path('review/ready');W=Path('review/weekly/2026-09-27')
f=P/'weekly_override.json';d=json.loads(f.read_text());d['stocks']['PAYX']['condition']='Conditional starter BUY only at or below101.80, within2% of total capital after existing holdings. Confirm issuer event calendar and live all-in price. Require demonstrated cumulative cash recovery before any subsequent ADD; owner-cash diagnostic1711.5m is only11.5m above the1700m thesis threshold.'
d['stocks']['NTAP']['condition']='WAIT: price exceeds150. September25 PEAK:AIO acquisition intent has no quantified price/earnings bridge in the observed release. Reconcile consideration, financing, dilution and integration before any entry; assign no unverified synergy value.'
f.write_text(json.dumps(d,indent=2))
f=P/'build_decision_pack.py';s=f.read_text().replace("ws.write(r,6,'30% dividend tax;25bp entry/exit')","ws.write(r,6,'Scenarios tax input;25bp entry/exit')");f.write_text(s)
f=W/'build_weekly_report.py';s=f.read_text()
s=s.replace('The separate market audit reports an AMP29 October issuer announcement; the root re-open failed, so its corroboration scope remains explicit.','AMP29 October results/09:00 ET call are observed in search-indexed issuer syndication; direct source pages remain unavailable. This is not a complete event clearance.')
s=s.replace('stock terminal proceeds plus30%-withheld dividends','stock terminal proceeds plus 30%-withheld dividends')
s=s.replace('The existing model','The existing model')
s=s.replace("with (W/'ACTION_TABLE.csv').open", "for action in actions:\n    if action['ticker']=='AMP': action['next_catalyst']='October29 results08:15ET /call09:00ET: search-indexed issuer release; direct source unavailable. Overall event clearance UNKNOWN.'\n    if action['ticker']=='PAYX': action['next_catalyst']='Q1FY27 reportedSeptember23. Next earnings date not primary-confirmed; next-quarter/cumulative cash recovery is critical.'\n    if action['ticker']=='HIG': action['next_catalyst']='Next Q3 filing and settlement/capital bridge; earnings calendar not independently cleared.'\n    if action['ticker']=='NTAP': action['next_catalyst']='PEAK:AIO definitive terms/funding/closing update; earnings calendar unconfirmed.'\nwith (W/'ACTION_TABLE.csv').open")
# Add an explicit distinction between data currency and all source documents.
s=s.replace('No normalized EPS, terminal multiple or stock dividend path changes', 'No normalized EPS, terminal multiple or stock dividend path changes')
f.write_text(s)
print('Final event and cash-recovery conditions saved.')
