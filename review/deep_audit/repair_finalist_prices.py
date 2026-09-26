"""Separate externally corroborated Sep22 repair layer, preserved source unchanged."""
import json,pathlib
import numpy as np
import pandas as pd
P=pathlib.Path('source_bundle/equity_project'); O=pathlib.Path('review/deep_audit')
evidence=json.loads((O/'raw/02_sep22_price_observations.json').read_text())
orig=pd.read_pickle(P/'close10.pkl'); corrected=orig.copy(); day=pd.Timestamp(evidence['date'])
patch=[]
for e in evidence['rows']:
    t=e['ticker']
    if pd.notna(orig.loc[day,t]):raise ValueError('Attempted overwrite of existing source price '+t)
    last=float(orig.loc[pd.Timestamp('2026-09-24'),t])
    if abs(last-e['sep24_close'])>.011:raise ValueError('Unreconciled cutoff close basis '+t)
    corrected.loc[day,t]=e['close']
    patch.append(dict(ticker=t,date=evidence['date'],original=None,repaired=e['close'],external_current_adjusted=e['adj_close_current_vintage'],basis='Raw close; provisional adjustment alignment through cutoff. RL later dividend excluded.',source='https://stockanalysis.com/stocks/'+t.lower()+'/history/',status='externally corroborated distributor observation; original source untouched'))
pd.DataFrame(patch).to_csv(O/'03_finalist_price_patch.csv',index=False)
pick=json.loads((P/'conv_port.json').read_text())['pick']; benchmark='^GSPC'
# Benchmark repair may be supplied as independently sourced evidence in a separate file.
bp=O/'raw/02_sep22_sp500_observation.json'; benchmark_repaired=False
if bp.exists():
    be=json.loads(bp.read_text())
    for date,close in [('2026-09-21',7764.70),('2026-09-23',7706.03),('2026-09-24',7704.13)]:
        if abs(float(orig.loc[pd.Timestamp(date),benchmark])-close)>.011:raise ValueError('Benchmark neighboring close mismatch '+date)
    corrected.loc[day,benchmark]=be['close']; benchmark_repaired=True
baseline=orig.ffill(); fixed=corrected.ffill()
fixed[pick+[benchmark]].to_csv(O/'03_finalist_repaired_history_diagnostic.csv',index_label='date')
def measure(c,t):
    s=c[t].dropna();r=s.pct_change(fill_method=None).iloc[-252:]
    bench=c[benchmark].pct_change(fill_method=None).iloc[-252:]
    pair=pd.concat([r,bench],axis=1).dropna()
    return dict(vol252=float(r.std()*np.sqrt(252)),beta252=float(pair.iloc[:,0].cov(pair.iloc[:,1])/pair.iloc[:,1].var()),sma50=float(s.tail(50).mean()),sma200=float(s.tail(200).mean()),ret6=float(s.iloc[-1]/s.iloc[-126]-1),ret12=float(s.iloc[-1]/s.iloc[-252]-1),mdd3y=float((s.tail(753)/s.tail(753).cummax()-1).min()),sep22_return=float(s.pct_change(fill_method=None).loc[day]),sep23_return=float(s.pct_change(fill_method=None).loc[day+pd.Timedelta(days=1)]))
rows=[dict(ticker=t,baseline=measure(baseline,t),repaired=measure(fixed,t)) for t in pick]
w=pd.Series(json.loads((pathlib.Path('review/data/risk_audit.json')).read_text())['weights']).reindex(pick)
def portfolio(c):
    R=c[pick].pct_change(fill_method=None).iloc[-252:];r=R@w
    W=c[pick].resample('W-FRI').last().pct_change(fill_method=None).iloc[-156:]
    return dict(daily_weight_reset_vol252=float(r.std()*np.sqrt(252)),weekly_weight_reset_vol156=float((W@w).std()*np.sqrt(52)))
result=dict(as_of='2026-09-24',patch_rows=len(patch),still_missing_scored_stocks=426,benchmark_repaired=benchmark_repaired,beta_status='Repaired stock and index daily paths' if benchmark_repaired else 'Stock repaired but benchmark Sep22 still forward-filled: beta is partial sensitivity ONLY',source=evidence['source'],basis_warning=evidence['warning'],portfolio_baseline=portfolio(baseline),portfolio_repaired=portfolio(fixed),rows=rows,scope='Sep22 repair only. Prior corporate actions, vintage bias, missing November2025 value, delisting returns and historic universe remain unaudited; this is not a validated strategy backtest.')
result['adjustment_alignment_status']='PROVISIONAL adjusted-return diagnostic: raw Sep22 points corroborated; matching Sep24 endpoints alone does not certify all intervening corporate actions. Complete action alignment through cutoff remains open; RL post-cutoff dividend excluded.'
(O/'03_finalist_repair_impact.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
for r in rows:
    print(r['ticker'],json.dumps(r))
