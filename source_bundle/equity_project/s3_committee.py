# STAGE 3: Investment Committee (100 -> 30) + confidence + final ranking
import pandas as pd, numpy as np, pickle
df=pd.read_pickle('s1.pkl'); O=pickle.load(open('s2.pkl','rb'))
X=pd.DataFrame(O).T.reset_index(drop=True)
S=df[df.short100].merge(X,on='t'); 
num=lambda c: pd.to_numeric(S[c],errors='coerce')
def pr(s,asc=True): s=pd.to_numeric(s,errors='coerce'); return s.fillna(s.median()).rank(pct=True,ascending=asc)
S['C_forensic']=(pr(num('fscore'))+pr(num('Z').clip(upper=10))+pr(num('accr'),False))/3
S['C_capital']=(pr(num('roic').clip(upper=1.5))+pr(num('sh_chg'),False))/2
S['C_earn']=(pr(num('beats'))+pr(num('avg_surp').clip(-20,20))+pr(num('rev90').clip(-.3,.5))+pr(num('up30')-num('dn30'))+pr(num('ups')-num('downs')))/5
S['C_value']=(pr(num('exp_ret'))+pr(num('base_ret')))/2
S['C_buffett']=num('bscore')/8
S['C_screen']=pr(S.s1)
W={'C_screen':.25,'C_forensic':.10,'C_capital':.10,'C_earn':.15,'C_value':.25,'C_buffett':.15}
S['s3']=100*sum(W[k]*S[k] for k in W)
# Devil's-advocate vetoes (logged)
V=[];OVR=[]
for _,r in S.iterrows():
    v=[]
    if not r.fin and r.sector!='Utilities' and r.Z==r.Z and r.Z<1.8:
        weak=(r.cover==r.cover and r.cover<4) or (r.nd_ebitda==r.nd_ebitda and r.nd_ebitda>3.5)
        if weak: v.append('Distress-zone balance sheet (Altman Z < 1.8 and weak debt cover)')
        else: OVR.append((r.t,'Altman Z %.1f is below 1.8, but interest cover and net debt are healthy. Z-score misreads asset-light models. Veto overturned.'%r.Z))
    if 'Possible cyclical peak earnings' in r['flags'] and r.vol>0.5: v.append('Peak-cycle trap: earnings boom in a highly volatile cyclical')
    if r.beats==r.beats and r.beats<=3: v.append('Missed estimates in 5+ of last 8 quarters')
    if r.rev90==r.rev90 and r.rev90<-0.10: v.append('Analysts cut next-year EPS >10% in 90 days')
    if r.vol>0.55: v.append('Mandate breach: volatility %.0f%% conflicts with your low-risk brief'%(100*r.vol))
    if r.exp_ret<-0.05: v.append('Own valuation models say it is overpriced (probability-weighted return < -5%)')
    V.append(v)
S['veto3']=V
# Confidence agent (0-100)
agent_cols=['A_Quality','A_Growth','A_Valuation','A_Momentum','A_Risk','A_Street']
agree=1-S[agent_cols].std(axis=1)/0.35
comp=S[['fpe','evebitda','roe','om','revg','tgt','nan','fscore','Z','roic','beats','rev90']].notna().mean(axis=1)
S['conf']=100*(0.15*comp+0.20*agree.clip(0,1)+0.15*pr(S.tgt_disp,False)+0.15*(num('beats')/8)+0.20*pr(num('disp'),False)+0.15*(0.5*pr(num('Z').clip(upper=10))+0.5*pr(num('cover').clip(upper=50))))
S['conf']=S.conf.round(0)
S=S.sort_values('s3',ascending=False).reset_index(drop=True); S['rank100']=S.index+1
pick=[];cnt={}
for _,r in S[S.veto3.map(len)==0].iterrows():
    if cnt.get(r.sector,0)>=6: continue
    pick.append(r.t); cnt[r.sector]=cnt.get(r.sector,0)+1
    if len(pick)==30: break
S['top30']=S.t.isin(pick)
T=S[S.top30].copy()
T['rr']=num('exp_ret')[T.index]/num('down')[T.index].abs()
def p2(s,asc=True): s=pd.to_numeric(s,errors='coerce'); return s.rank(pct=True,ascending=asc)
T['final']=100*(0.35*p2(T.rr)+0.25*T.conf/100+0.20*(0.5*T.C_buffett+0.5*T.C_capital)+0.20*T.C_earn)
T=T.sort_values('final',ascending=False).reset_index(drop=True); T['rank30']=T.index+1
T['tier']=np.where((T.rank30<=10)&(T.exp_ret>0.08),'A: Buy now',np.where(T.exp_ret>0.03,'B: Accumulate on dips','C: Watchlist'))
pickle.dump(OVR,open('overrides.pkl','wb')); S.to_pickle('s3_100.pkl'); T.to_pickle('s3_30.pkl')
print('vetoed in 100:',(S.veto3.map(len)>0).sum()); print(pd.Series(cnt).to_string())
print(T[['rank30','t','sector','final','conf','exp_ret','up','down','rr','bscore','beats','tier']].round(2).to_string())
print('Dropped with veto (top by s3):'); print(S[S.veto3.map(len)>0][['rank100','t','s3','veto3']].head(12).to_string())
