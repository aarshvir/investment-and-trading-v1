import pandas as pd, numpy as np, pickle, json
df=pd.read_pickle('s1.pkl'); S=pd.read_pickle('s3_100.pkl'); T=pd.read_pickle('s3_30.pkl')
A=json.load(open('audit.json')); P=json.load(open('port.json')); O=pickle.load(open('s2.pkl','rb'))
sec_fpe=df[df.fpe>0].groupby('sector').fpe.median().to_dict()
def cl(x):
    if isinstance(x,(float,np.floating)): return None if (x!=x or np.isinf(x)) else round(float(x),4)
    if isinstance(x,(np.integer,)): return int(x)
    if isinstance(x,(np.bool_,)): return bool(x)
    if isinstance(x,dict): return {k:cl(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [cl(v) for v in x]
    return x
U=[cl(dict(t=r.t,n=r['name'],s=r.sector,p=r.price,mc=r.mcap,rk=r.rank500,sc=r.s1,q=r.A_Quality,g=r.A_Growth,v=r.A_Valuation,m=r.A_Momentum,rk_=r.A_Risk,st=r.A_Street,
   fpe=r.fpe,rg=r.revg,vol=r.vol,dd=r.mdd3y,up=r.upside,sl=bool(r.short100),vt=list(r.veto),fl=list(r['flags']))) for _,r in df.iterrows()]
DIL={
'AIZ':dict(src='https://www.sec.gov/Archives/edgar/data/0001267238/000126723826000039/aiz-20260630exx991pressrel.htm',notes=['Record Q2 2026: adjusted EPS ex-catastrophes rose 19% to $6.60; GAAP net income up 27%.','Global Lifestyle (device protection, auto service contracts) is the engine: adjusted EBITDA +21%, with Connected Living up 29%.','Full-year 2026 outlook raised; Lifestyle now guided to low-double-digit EBITDA growth.','Capital return continues: $123M returned in Q2 (buybacks plus dividends).','Watch: Global Housing benefited from unusually low claims frequency and catastrophe losses. Hurricane season (Aug to Oct) is the main near-term risk.']),
'CAH':dict(src='https://www.sec.gov/Archives/edgar/data/0000721371/000072137126000037/a26q4_x063026xex991xnewsre.htm',notes=['FY2026 revenue $254B (+14%); non-GAAP EPS $10.95 ex a one-off tariff refund (+33%).','Specialty pharma is the growth engine: segment profit +21%, specialty revenue growth above 25%.','FY2027 guide: EPS $12.40 to $12.60, 13% to 15% growth, above the long-term target.','$1.4B of buybacks in FY26 and a new $5B authorisation; adjusted FCF $5.0B.','Watch: thin-margin distribution model, drug-pricing policy and opioid-litigation overhang.']),
'HIG':dict(src='https://insurancenewsnet.com/oarticle/the-hartford-reports-strong-second-quarter-2026-financial-results',notes=['Q2 2026 core EPS $3.42; trailing core ROE 18.7%.','Business Insurance premiums +5% at an 89.3 underlying combined ratio (profitable underwriting).','New $4.2B buyback through 2028, part-funded by selling Hartford Funds to Wellington.','Net investment income +22% to $800M, helped by higher yields.','Watch: reserve strengthening in general liability and commercial auto; personal-lines premiums fell 7%.']),
'BKNG':dict(src='https://www.sec.gov/Archives/edgar/data/0001075531/000107553126000036/q2-26bkngearningsrelease.htm',notes=['Q2 2026 beat on every line: room nights +5%, gross bookings +9% to $51B, adjusted EPS +15%.','Free cash flow $3.6B in the quarter (+16%); share count down about 6% from buybacks.','Cost programme savings target raised to about $650M run-rate by end-2027.','FY26 guide: high-single-digit revenue growth, low-to-mid-teens adjusted EPS growth.','Watch: Middle East conflict hitting long-haul travel (about 7% of room nights touch the region); EU regulatory probes of its commission model.']),
'BMY':dict(src='https://www.marketbeat.com/instant-alerts/bristol-myers-squibb-q2-earnings-call-highlights-2026-07-30/',notes=['Q2 2026 revenue about $13B (+5%); growth portfolio +14% to $7.6B, now about 60% of sales.','Full-year revenue and EPS guidance raised; Eliquis +21%, Camzyos +59%, Breyanzi +41%.','Pipeline readouts (milvexian, Cobenfy in Alzheimer\'s psychosis) slipped to early 2027.','BEAR CASE IS REAL: Eliquis loses exclusivity in Europe in 2027 and in the US in April 2028, a $1.5B to $2B revenue step-down starting 2027.','Low multiple prices in the patent cliff; upside depends on pipeline hits.']),
'MDT':dict(src='https://www.sec.gov/Archives/edgar/data/0001613103/000162828026059697/exhibit991-fy27q1earningsr.htm',notes=['Q1 FY27 (to July 2026): revenue $9.8B, +13.7% organic, about 2 points above guidance; FY27 guidance raised.','Cardiac ablation surging (+88% globally) on Sphere-9 and Affera; heart-rhythm business +15%.','Hugo surgical robot scaling; diabetes business separation planned before fiscal year-end.','48-year record of annual dividend increases.','Watch: part of Q1 growth came from an extra selling week; robot competition from Intuitive.']),
'CL':dict(src='https://www.sec.gov/Archives/edgar/data/0000021665/000002166526000041/q22026pressreleasetables.htm',notes=['Q2 2026: net sales +4.9%, organic +2.4%; base-business EPS +8%.','Gross margin up 140bps to 61.5%; full-year base EPS guidance raised to mid-single-digit growth.','Global toothpaste share 41.3% (up 0.2pts); manual toothbrush share 32.7%.','Advertising up 15% to defend brands; first-half operating cash flow +17%.','Watch: slow organic growth (1% to 4% guide) caps upside; this is a ballast holding, not a growth engine.']),
'NVDA':dict(src='https://finance.yahoo.com/quote/NVDA/',notes=['Fiscal Q2 2027 revenue grew 106% year on year to $96.2B.','Forward P/E about 14x on consensus, cheaper than the S&P 500 despite leading growth.','Next-year EPS estimates rose about 24% in 90 days (42 upward revisions, 0 down in 30 days).','Customers (Meta, Google) building their own chips with Broadcom: a long-run share risk.','Weighted at only about 5% because it is the most volatile name in the portfolio.'])}
def bullbear(r,o):
    b=[];x=[]
    if r.revg==r.revg and r.revg>0.10: b.append(f'Revenue growing {r.revg*100:.0f}% a year')
    if o['roic']==o['roic'] and o['roic']>0.20: b.append(f'High return on capital ({o["roic"]*100:.0f}%)')
    if o['beats']==o['beats'] and o['beats']>=7: b.append(f'Beat earnings estimates in {o["beats"]} of last {o["nq"]} quarters')
    if o['rev90']==o['rev90'] and o['rev90']>0.03: b.append(f'Analysts raised next-year EPS by {o["rev90"]*100:.0f}% in 90 days')
    if o['sh_chg']==o['sh_chg'] and o['sh_chg']<-0.02: b.append(f'Share count down {abs(o["sh_chg"])*100:.0f}% (buybacks)')
    if r.fpe==r.fpe and r.fpe>0 and r.fpe<sec_fpe.get(r.sector,20)*0.85: b.append(f'Cheaper than its sector ({r.fpe:.1f}x vs {sec_fpe.get(r.sector,20):.1f}x forward P/E)')
    if r.fcfy==r.fcfy and r.fcfy>0.05: b.append(f'Free-cash-flow yield {r.fcfy*100:.1f}%')
    if o['bscore']>=6: b.append(f'Passes {o["bscore"]}/8 Buffett tests')
    if r.tt>=6: b.append('Price in a healthy uptrend (trend template 6+/7)')
    if r.vol>0.35: x.append(f'Volatile: price swings about {r.vol*100:.0f}% a year')
    if o['down']<-0.25: x.append(f'Bear case is a {o["down"]*100:.0f}% fall')
    if o['rev90']==o['rev90'] and o['rev90']<-0.02: x.append(f'Analysts cut next-year EPS {o["rev90"]*100:.0f}% in 90 days')
    if r.fpe==r.fpe and r.fpe>sec_fpe.get(r.sector,20)*1.3: x.append(f'Expensive vs sector ({r.fpe:.1f}x vs {sec_fpe.get(r.sector,20):.1f}x)')
    if r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>3: x.append(f'Leveraged: net debt {r.nd_ebitda:.1f}x EBITDA')
    if r.revg==r.revg and r.revg<0.03: x.append(f'Slow growth ({r.revg*100:.1f}%)')
    if o['ins_net']==o['ins_net'] and o['ins_net']<0: x.append('Insiders net sellers over 6 months')
    om=[v for v in o['om_a'] if v is not None]
    if len(om)>=3 and om[0]<om[-1]-0.03: x.append('Operating margin lower than 3 years ago')
    if o['disp']>0.35: x.append('Valuation methods disagree widely (lower certainty)')
    for f in r['flags']: x.append(f)
    return b[:7],x[:7]
def company(t):
    r=S[S.t==t].iloc[0]; o=O[t]; b,x=bullbear(r,o); tt=T[T.t==t]
    d=dict(t=t,n=r['name'],s=r.sector,sub=r['sub'],p=r.price,mc=r.mcap,sum=r.summary,web=r.website,emp=r.employees,rk500=r.rank500,rk100=r.rank100,s1=r.s1,s3=r.s3,
      ag=dict(Quality=r.A_Quality,Growth=r.A_Growth,Valuation=r.A_Valuation,Momentum=r.A_Momentum,Risk=r.A_Risk,Street=r.A_Street),
      cm=dict(Screen=r.C_screen,Forensic=r.C_forensic,Capital=r.C_capital,Earnings=r.C_earn,Value=r.C_value,Buffett=r.C_buffett),
      k=dict(fpe=r.fpe,tpe=r.tpe,eve=r.evebitda,pb=r.pb,fcfy=r.fcfy,divy=r.divy,roe=r.roe,om=r.om,gm=r.gm,revg=r.revg,epsg=r.epsg,de=r.de,nde=r.nd_ebitda,vol=r.vol,beta=r.beta,dd=r.mdd3y,r12=r.ret12,r6=r.ret6,offhi=r.off_hi,tt=r.tt,short=r.short,ins=r.insider,rec=r.rec,nan=r.nan,tgt=r.tgt,tlo=r.tgt_lo,thi=r.tgt_hi),
      debate=[list(z) for z in r.debate],veto3=list(r.veto3),top30=bool(r.top30),conf=r.conf,
      bull_pts=b,bear_pts=x,**{kk:o[kk] for kk in ['yrs','rev_a','ni_a','fcf_a','om_a','roe_a','eps_a','cagr','roic','sh_chg','cover','fscore','Z','accr','buyback','div','beats','nq','avg_surp','eq_hist','next_date','eps0y','eps1y','rev90','up30','dn30','ups','downs','ins_net','news','qs','q_yoy','wacc','impl_g','g1','methods','fair','disp','base','bull','bear','exp','exp_ret','up','down','base_ret','buffett','bscore','capex_adj','oneoff']})
    if len(tt): tt=tt.iloc[0]; d.update(rk30=int(tt.rank30),final=tt.final,tier=tt.tier,stab=tt.stability,rr=tt.rr)
    if t in DIL: d['dil']=DIL[t]
    return cl(d)
C100={t:company(t) for t in S.t}
agents=[
 ('Stage 1: Screening committee (497 stocks)',[('A1 Quality & Moat (Buffett lens)','Return on equity, margins, cash conversion, leverage, ranked within each sector.'),('A2 Growth','Revenue, earnings and forward EPS growth.'),('A3 Valuation','Forward P/E and EV/EBITDA vs sector, FCF yield, analyst upside.'),('A4 Momentum & Trend','Minervini 7-point trend template, 6-month relative strength vs S&P, 12-month return.'),('A5 Risk','Volatility, downside volatility, 3-year max drawdown, worst 12-month loss, beta.'),('A6 Street Sentiment','Analyst ratings, target upside, coverage breadth, short interest.'),('A7 Red Team','Hard vetoes (no profit, cash burn, fell >60%) and soft flags (leverage, weak cash conversion, shrinking revenue, peak-cycle earnings).')]),
 ('Stage 2: Diligence team (100 stocks)',[('A8 Forensic Accountant','Piotroski F-score, Altman Z, accruals, interest cover from 4 years of statements.'),('A9 Capital Allocation','Return on invested capital, buybacks vs dilution, dividends, growth-capex adjustment.'),('A10 Earnings Record','Last 8 quarterly reports (2 years): beats/misses, surprise size, 90-day estimate revisions, upgrades vs downgrades.'),('A11 Intrinsic Value','Up to 4 methods: forward multiple, 10-year DCF with reverse-DCF implied growth, justified P/B for banks and insurers, Street target. Bear, base and bull prices.')]),
 ('Stage 3: Investment committee (100 to 30 to ranked)',[('A12 Bull Advocate','Builds the strongest data-backed case for each stock.'),('A13 Bear Advocate / Devil\'s Advocate','Vetoes: distress balance sheet, serial misses, falling estimates, overvaluation, low-risk mandate breach.'),('A14 Confidence Officer','Scores 0 to 100 from data completeness, agent agreement, analyst dispersion, earnings reliability, valuation-method agreement and balance-sheet strength.'),('A15 Portfolio Construction (CIO)','Picks the final 10 with sector, sub-industry and insurance caps; weights by confidence x return / volatility.')]),
 ('Audit layer',[('X1 Data Integrity Auditor','Coverage, stale prices, price reconciliation, outliers.'),('X2 Methodology & Robustness Auditor','500-run weight-sensitivity test, veto consistency, sector tilt, overturned vetoes.'),('X3 Output Reconciliation Auditor','Scenario ordering, reconciliation with prior answers, calibration haircut on returns.')])]
dstats={}
for d in df.debate:
    for z in d: dstats[z[0]]=dstats.get(z[0],0)+1
self_fix=[('Cash-conversion flag misfired on AI spenders','Red team flagged GOOGL, MSFT, META, AMZN, LLY for weak cash conversion. The capital-allocation agent showed operating cash covers profit and the gap is growth capex. Flag withdrawn for these names.'),
 ('DCF used one-off profits as the growth base','GOOGL\'s trailing EPS includes one-off investment gains, so forecast growth looked negative (DCF of $73). The auditor added a one-off detector. 8 companies were corrected.'),
 ('Payment networks were valued like banks','Visa and Mastercard were run through a bank P/B model (Visa at $120). They were re-routed to DCF, alongside exchanges, data firms and asset managers.'),
 ('Growth-capex companies had understated DCFs','LLY, MSFT and others building capacity had depressed FCF. Normalised owner earnings (70% of profit) were applied when capex exceeds 1.5x depreciation. 11 companies adjusted.'),
 ('Bear cases were too gentle for stocks that only went up','SNDK showed a 3% bear case because its short history had no down year. A volatility-based floor was added; its bear case is now -58%.'),
 ('Altman Z-score wrongly vetoed asset-light firms','EXPE, BLK, CPAY and FANG failed Z but have healthy interest cover. Veto now requires weak debt metrics as well. 4 vetoes overturned.'),
 ('Low-risk mandate was not enforced','A 75%-volatility memory stock reached the top 30. The mandate agent now vetoes volatility above 55%.'),
 ('Portfolio had 3 correlated insurers','CIO rules tightened to one stock per sub-industry and at most two insurers.')]
out=dict(asof=A['X1']['asof'],U=U,C=C100,top30=[c for c in T.t],P=P,A=A,agents=agents,dstats=dstats,self_fix=self_fix,sec_fpe=sec_fpe,
  funnel=dict(u=len(df),veto1=int(df.vetoed.sum()),s100=100,veto3=int((S.veto3.map(len)>0).sum()),s30=30,final=10))
json.dump(cl(out),open('dash.json','w'))
import os; print(os.path.getsize('dash.json')/1e6,'MB')
