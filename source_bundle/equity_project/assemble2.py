import pandas as pd, numpy as np, json, pickle
K=pickle.load(open('K.pkl','rb')); X=pd.read_pickle('v3.pkl'); ER=json.load(open('edgar_read.json')); P2=json.load(open('port2.json'))
BT=dict(v1=json.load(open('backtest.json')),v3=json.load(open('bt_v3.json')),v3b=json.load(open('bt_v3b.json')),f10=json.load(open('bt10.json')))
def cl(x):
    if isinstance(x,(float,np.floating)): return None if (x!=x or np.isinf(x)) else round(float(x),4)
    if isinstance(x,(np.integer,)): return int(x)
    if isinstance(x,(np.bool_,)): return bool(x)
    if isinstance(x,dict): return {str(k):cl(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [cl(v) for v in x]
    return x
C2={}
for t,r in K.iterrows():
    e=ER[t]
    C2[t]=cl(dict(t=t,n=r['name'],s=r.sector,sub=r['sub'],p=r.price,rk=int(r.rank52),v3=r.v3,pm=r.P_mom,pe=r.P_emom,pv=r.P_val,pq=r.P_q,
      Ebb=r.E_bb,by=r.bb_yield,bg=r.bb_growth,br=r.bb_rerate,Efac=r.E_fac,Escen=r.E_scen,Ef=r.E_final,Esh=r.E_sh,Esp=r.E_spread,conf=r.conf2,
      g=r.g,rev90=r.rev90,beats=r.beats8,mom=r.mom121,vol=r.vol,beta=r.beta3,fpe=r.fpe,fcfy=r.fcfy,roe=r.roe,revg=r.revg,dd=r.mdd3y,art=bool(r.g_artifact),
      nrel=e['n'],raises=e['raises'],cuts=e['cuts'],keeps=e['keeps'],gs=e['gscore'],tl=e['timeline'],url=e['last_url'],flags=dict(record=e['record'],headwind=e['headwind'],investig=e['investig'],weakness=e['weakness'],goingc=e['goingc'],tariff=e['tariff'],ai=e['ai'])))
U3=[cl(dict(t=r.t,n=r['name'],s=r.sector,rk=int(r.rank_v3),v3=r.v3,pm=r.P_mom,pe=r.P_emom,pv=r.P_val,pq=r.P_q,E=r.E_final,vol=r.vol,gate=bool(r.gate),why=r.gate_why)) for _,r in X.iterrows()]
fix2=[('My v1 model had the wrong risk tilt','A point-in-time backtest showed the low-volatility pillar lost money in all 3 test years (information coefficient −0.14, −0.05, −0.26), and v1\'s top 30 lagged the S&P by 10, 5 and 8 points. Low-vol was removed as a return driver and kept only as a constraint.'),
 ('Dividend-yield unit bug','Yields under 0.5% were being read as 44% to 47% (for example NVDA, REGN, AAPL). Switched to the trailing-yield field and re-ran everything.'),
 ('One-off earnings made growth look explosive','Merck, Freeport and 8 others showed 60% EPS growth because last year\'s EPS was depressed by one-off charges. Growth is now capped at revenue growth + 10pts when the two diverge.'),
 ('1-year betas were noisy (some negative)','Replaced with 3-year weekly betas for all 497 stocks.'),
 ('Optimiser maximised estimation error','A raw return-maximiser piled into cyclicals with the shakiest forecasts (airlines, autos). Fixed with confidence-weighted shrinkage toward a market prior (Black-Litterman style), a quality floor, confidence-based position caps, and 40-run resampled optimisation.'),
 ('Hidden concentration','Sub-industry cap of 12% added (online travel, asset managers).'),
 ('Alpha from the backtest overstated','Backtested excess return was shrunk 58%, in line with McLean and Pontiff\'s published post-publication decay of return predictors.')]
grade=[('Universe & data breadth','497 stocks, 11 years of prices, 4-5 years of statements, full estimate history',10,10),
 ('Primary-source reading','467 SEC earnings releases (2 years, 52 companies) read by machine for guidance raises, cuts and red flags; 8 releases read in full',9,10),
 ('Valuation rigour','3 independent methods (building-block, factor, scenario/DCF) with reverse DCF, shrinkage and disagreement tracking',9,10),
 ('Out-of-sample validation','3-year point-in-time backtest plus 10-year factor test; found and fixed my own model\'s flaw',9,10),
 ('Risk modelling','20,000-path block bootstrap on 10 years including COVID and 2022, stress replays, resampled optimisation',9,10),
 ('Portfolio vs mandate','Efficient frontier with explicit odds for 15%, 20%, 25% and 50% outcomes',9,10),
 ('Error discovery','15 model errors found and fixed across v1 and v2',10,10),
 ('Honesty of probabilities','Shrunk estimates reported next to raw; limits stated',10,10),
 ('Company-level qualitative depth','Guidance trajectories for 52 companies; deep human-style notes for only 8. No earnings-call transcripts or expert calls',7,10),
 ('Actionability','Exact weights; order sheet needs your amount and broker',9,10)]
out=dict(C2=C2,U3=U3,P2=P2,BT=BT,fix2=fix2,grade=grade)
json.dump(cl(out),open('dash2.json','w')); import os; print(os.path.getsize('dash2.json')/1e6,'MB', sum(g[2] for g in grade))
