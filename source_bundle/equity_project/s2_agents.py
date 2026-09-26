# STAGE 2/3: Forensic, Capital-Allocation, Earnings-Momentum, Intrinsic-Value, Bull & Bear agents on the 100
import pandas as pd, numpy as np, pickle, json, warnings
warnings.filterwarnings('ignore')
df=pd.read_pickle('s1.pkl'); D=pickle.load(open('deep.pkl','rb')); I=json.load(open('info.json'))
C=pd.read_pickle('close.pkl').ffill()
RF=0.049; ERP=0.05; TG=0.03
sec_fpe=df[df.fpe>0].groupby('sector').fpe.median()
def row(t,names):
    if t is None: return None
    for n in names:
        if n in t.index: return t.loc[n].astype(float)
    return None
def v(s,k=0):
    try:
        x=s.iloc[k]; return float(x) if x==x else np.nan
    except Exception: return np.nan
out={}
for t in df[df.short100].t:
    o=D[t]; i=I[t]; r=df[df.t==t].iloc[0]; A,Q,CF,BS=o['a_inc'],o['q_inc'],o['a_cf'],o['a_bs']
    NONBANK=['Transaction & Payment Processing Services','Financial Exchanges & Data','Insurance Brokers','Asset Management & Custody Banks']
    fin=(r.sector=='Real Estate') or (r.sector=='Financials' and r['sub'] not in NONBANK)
    rev=row(A,['Total Revenue','Operating Revenue']); ni=row(A,['Net Income Common Stockholders','Net Income'])
    gp=row(A,['Gross Profit']); ebit=row(A,['EBIT','Operating Income']); opi=row(A,['Operating Income','EBIT'])
    intexp=row(A,['Interest Expense','Interest Expense Non Operating']); sh=row(A,['Diluted Average Shares','Basic Average Shares'])
    eps=row(A,['Diluted EPS','Basic EPS']); taxr=row(A,['Tax Rate For Calcs'])
    ocf=row(CF,['Operating Cash Flow','Cash Flow From Continuing Operating Activities']); capex=row(CF,['Capital Expenditure'])
    buyb=row(CF,['Repurchase Of Capital Stock','Common Stock Payments']); divp=row(CF,['Cash Dividends Paid','Common Stock Dividend Paid'])
    nin=row(A,['Normalized Income']); dep=row(CF,['Depreciation And Amortization','Depreciation Amortization Depletion'])
    ta=row(BS,['Total Assets']); tl=row(BS,['Total Liabilities Net Minority Interest']); eq=row(BS,['Stockholders Equity','Common Stock Equity'])
    debt=row(BS,['Total Debt']); cash=row(BS,['Cash Cash Equivalents And Short Term Investments','Cash And Cash Equivalents'])
    ca=row(BS,['Current Assets']); cl=row(BS,['Current Liabilities']); re_=row(BS,['Retained Earnings']); ltd=row(BS,['Long Term Debt'])
    yrs=[str(c.year) for c in A.columns][:4] if A is not None else []
    def ser(s,n=4): return [None if s is None or k>=len(s) or s.iloc[k]!=s.iloc[k] else float(s.iloc[k]) for k in range(n)]
    fcf=(ocf+capex) if (ocf is not None and capex is not None) else ocf
    n_y=min(4,len(rev.dropna())) if rev is not None else 0
    cagr=(v(rev,0)/v(rev,n_y-1))**(1/(n_y-1))-1 if n_y>=2 and v(rev,n_y-1)>0 else np.nan
    om_s=(opi/rev) if (opi is not None and rev is not None) else None
    roe_s=(ni/eq) if (ni is not None and eq is not None) else None
    tax=np.clip(v(taxr,0) if taxr is not None and v(taxr,0)==v(taxr,0) else 0.21,0,0.35)
    ic=(v(debt,0) if debt is not None else 0)+v(eq,0)-(v(cash,0) if cash is not None else 0)
    roic=v(ebit,0)*(1-tax)/ic if (ebit is not None and ic and ic>0) else np.nan
    sh_chg=(v(sh,0)/v(sh,min(3,len(sh.dropna())-1))-1) if sh is not None and len(sh.dropna())>=2 else np.nan
    cover=v(ebit,0)/abs(v(intexp,0)) if (intexp is not None and v(intexp,0) and v(intexp,0)==v(intexp,0) and v(intexp,0)!=0) else np.nan
    # Piotroski F-score
    F=[];
    try:
        roa0,roa1=v(ni,0)/v(ta,0),v(ni,1)/v(ta,1)
        F+=[roa0>0, v(ocf,0)>0, roa0>roa1, v(ocf,0)>v(ni,0)]
        lev0=(v(ltd,0) if ltd is not None else 0)/v(ta,0); lev1=(v(ltd,1) if ltd is not None else 0)/v(ta,1); F.append(lev0<=lev1)
        F.append((v(ca,0)/v(cl,0))>=(v(ca,1)/v(cl,1)) if ca is not None and cl is not None else False)
        F.append(v(sh,0)<=v(sh,1)*1.005 if sh is not None else False)
        F.append((v(gp,0)/v(rev,0))>=(v(gp,1)/v(rev,1)) if gp is not None else False)
        F.append(v(rev,0)/v(ta,0)>=v(rev,1)/v(ta,1))
    except Exception: pass
    fscore=int(sum(bool(x) for x in F)) if (F and not fin) else np.nan
    Z=np.nan
    if not fin:
        try: Z=1.2*(v(ca,0)-v(cl,0))/v(ta,0)+1.4*v(re_,0)/v(ta,0)+3.3*v(ebit,0)/v(ta,0)+0.6*(r.mcap*1e9)/v(tl,0)+1.0*v(rev,0)/v(ta,0)
        except Exception: pass
    accr=(v(ni,0)-v(ocf,0))/v(ta,0) if ocf is not None else np.nan
    # Earnings record (last 8 reported quarters ~ 2 years of reports)
    ed=o['ed']; beats=avgs=np.nan; eq_hist=[]
    if ed is not None and len(ed):
        e=ed.dropna(subset=['Reported EPS']).head(8)
        if len(e): beats=int((e['Surprise(%)']>0).sum()); avgs=float(e['Surprise(%)'].clip(-50,50).mean())
        eq_hist=[dict(d=str(ix.date()),est=None if x['EPS Estimate']!=x['EPS Estimate'] else float(x['EPS Estimate']),act=float(x['Reported EPS']),s=float(x['Surprise(%)']) if x['Surprise(%)']==x['Surprise(%)'] else None) for ix,x in e.iterrows()][::-1]
        nxt=ed[ed['Reported EPS'].isna()]; next_date=str(nxt.index[-1].date()) if len(nxt) else None
    else: next_date=None
    nq=len(eq_hist)
    tr=o['trend']; rv=o['rev']
    eps1y=float(tr.loc['+1y','current']) if tr is not None and '+1y' in tr.index and tr.loc['+1y','current']==tr.loc['+1y','current'] else (i.get('forwardEps') or np.nan)
    eps0y=float(tr.loc['0y','current']) if tr is not None and '0y' in tr.index else np.nan
    rev90=(tr.loc['+1y','current']/tr.loc['+1y','90daysAgo']-1) if tr is not None and '+1y' in tr.index and tr.loc['+1y','90daysAgo'] else np.nan
    up30=int(rv.loc['+1y','upLast30days']) if rv is not None and '+1y' in rv.index and rv.loc['+1y','upLast30days']==rv.loc['+1y','upLast30days'] else 0
    dn30=int(rv.loc['+1y','downLast30days']) if rv is not None and '+1y' in rv.index and rv.loc['+1y','downLast30days']==rv.loc['+1y','downLast30days'] else 0
    ud=o['ud']; ups=downs=0
    if ud is not None and len(ud):
        u=ud[ud.index>=pd.Timestamp.now(tz=ud.index.tz)-pd.Timedelta(days=90)] if ud.index.tz else ud[ud.index>=pd.Timestamp.now()-pd.Timedelta(days=90)]
        ups=int((u.Action=='up').sum()); downs=int((u.Action=='down').sum())
    ins=o['ins']; ins_net=np.nan
    try:
        x=ins.set_index(ins.columns[0]); ins_net=float(x.loc['Net Shares Purchased (Sold)'].iloc[0])
    except Exception: pass
    news=[]
    for n_ in (o['news'] or [])[:5]:
        c_=n_.get('content',{}); news.append(dict(title=c_.get('title'),date=(c_.get('pubDate') or '')[:10],src=(c_.get('provider') or {}).get('displayName'),url=((c_.get('canonicalUrl') or {}).get('url'))))
    # quarterly series
    qrev=row(Q,['Total Revenue','Operating Revenue']); qeps=row(Q,['Diluted EPS','Basic EPS']); qopi=row(Q,['Operating Income'])
    qs=[dict(q=str(c.date()),rev=None if qrev is None or qrev.iloc[k]!=qrev.iloc[k] else float(qrev.iloc[k]),eps=None if qeps is None or qeps.iloc[k]!=qeps.iloc[k] else float(qeps.iloc[k]),
             om=None if (qopi is None or qrev is None or qrev.iloc[k]!=qrev.iloc[k] or qopi.iloc[k]!=qopi.iloc[k]) else float(qopi.iloc[k]/qrev.iloc[k])) for k,c in enumerate(Q.columns)][::-1] if Q is not None else []
    q_yoy=(qs[-1]['rev']/qs[0]['rev']-1) if len(qs)>=5 and qs[0]['rev'] and qs[-1]['rev'] else np.nan
    # ---------- Intrinsic value agent ----------
    p=r.price; badj=float(np.clip(0.67*r.beta+0.33,0.7,1.4)); coe=RF+0.045*badj
    E_=r.mcap*1e9; D_=(v(debt,0) if debt is not None else 0) or 0
    wacc=(E_*coe+D_*(RF+0.015)*(1-tax))/(E_+D_) if not fin else coe
    wacc=max(wacc,0.075)
    methods={}
    fpe_now=p/eps1y if eps1y and eps1y>0 else np.nan
    if eps1y==eps1y and eps1y>0:
        tgt_mult=0.7*fpe_now+0.3*sec_fpe.get(r.sector,20)
        methods['Multiples (fwd EPS x blended P/E)']=eps1y*tgt_mult
    g_cons=(eps1y/eps0y-1) if (eps0y==eps0y and eps0y>0 and eps1y==eps1y) else np.nan
    oneoff=(g_cons==g_cons and g_cons<0 and cagr==cagr and cagr>0.05)
    cands=[x for x in [cagr, (np.nan if oneoff else g_cons), r.revg] if x==x]
    g1=float(np.clip(np.median(cands),-0.05,0.30)) if cands else 0.05
    f0=v(fcf,0) if fcf is not None else np.nan
    ocfc=(v(ocf,0)/v(ni,0)) if (ocf is not None and ni is not None and v(ni,0)>0) else np.nan
    capex_adj=False
    nn=v(nin,0) if (nin is not None and v(nin,0)==v(nin,0) and v(nin,0)>0) else v(ni,0)
    growth_capex=(capex is not None and dep is not None and v(dep,0)>0 and abs(v(capex,0))>1.5*v(dep,0))
    if not fin and nn==nn and nn>0 and (f0!=f0 or f0<0.7*nn) and ((ocfc==ocfc and ocfc>=0.9) or (growth_capex and ocfc==ocfc and ocfc>=0.6)):
        f0=0.7*nn; capex_adj=True
    sh_now=(r.mcap*1e9)/p
    netdebt=(v(debt,0) if debt is not None else 0)-(v(cash,0) if cash is not None else 0)
    def dcf(g0):
        pv=0; f=f0
        for y in range(1,11):
            g=g0 if y<=5 else g0+(TG-g0)*(y-5)/5
            f*=1+g; pv+=f/(1+wacc)**y
        return (pv+f*(1+TG)/(wacc-TG)/(1+wacc)**10-netdebt)/sh_now
    impl_g=np.nan
    if not fin and f0==f0 and f0>0:
        methods['DCF (5-yr growth, 5-yr fade)']=dcf(g1)
        lo,hi=-0.3,0.8
        for _ in range(60):
            mid=(lo+hi)/2; lo,hi=(mid,hi) if dcf(mid)<p else (lo,mid)
        impl_g=mid
    if fin and r.pb and r.pb>0 and r.roe==r.roe and r.sector=='Financials':
        bvps=p/r.pb; roe_=float(np.clip(r.roe,0,0.35)); jpb=(roe_-TG)/(coe-TG)
        methods['Justified P/B (ROE vs cost of equity)']=bvps*jpb
    if r.tgt==r.tgt: methods['Street mean target (12m)']=float(r.tgt)
    mv={k:float(x) for k,x in methods.items() if x==x and x>0}
    # clip each method to +/-60% band to limit model blow-ups
    mv_c={k:float(np.clip(x,p*0.3,p*2.5)) for k,x in mv.items()}
    fair=float(np.median(list(mv_c.values()))) if mv_c else p
    disp=float(np.std(list(mv_c.values()))/p) if len(mv_c)>1 else 0.5
    base=float(np.clip(fair,p*0.7,p*1.45))
    bull_f=eps1y*1.10*fpe_now*1.10 if eps1y==eps1y and eps1y>0 else p*1.3
    bull=float(np.nanmean([bull_f, r.tgt_hi if r.tgt_hi==r.tgt_hi else np.nan, base*1.15]))
    bear_f=eps1y*0.85*fpe_now*0.80 if eps1y==eps1y and eps1y>0 else p*0.7
    emp=p*(1+max(r.worst12m,-0.6)) if r.worst12m<0 else np.nan
    bear=float(np.nanmean([bear_f, p*np.exp(-r.vol), emp, r.tgt_lo if r.tgt_lo==r.tgt_lo else np.nan]))
    bear=min(bear,p*(1-0.5*r.vol))
    bull=max(bull,base*1.05,p*1.05); bear=min(bear,base*0.95,p*0.97)
    exp=0.25*bull+0.5*base+0.25*bear
    # Buffett checklist
    roe_list=[x for x in ser(roe_s) if x is not None]; om_list=[x for x in ser(om_s) if x is not None]
    fcf_list=[x for x in ser(fcf) if x is not None]; eps_list=[x for x in ser(eps) if x is not None]
    B={'ROE above 15% in 3 of last 4 years':sum(x>0.15 for x in roe_list)>=3 if len(roe_list)>=3 else False,
       'Conservative debt (interest cover >8x or net cash)':(cover==cover and cover>8) or ((v(cash,0) if cash is not None else 0)>(v(debt,0) if debt is not None else 0)),
       'Operating margin stable or rising':(om_list[0]>=np.mean(om_list)-0.02) if len(om_list)>=3 else False,
       'Positive free cash flow every year':(len(fcf_list)>=3 and all(x>0 for x in fcf_list)) if not fin else (len(roe_list)>=3 and all(x>0 for x in roe_list)),
       'Share count flat or shrinking':sh_chg==sh_chg and sh_chg<=0.01,
       'Return on capital above 12%':(roic==roic and roic>0.12) if not fin else (r.roe==r.roe and r.roe>0.12),
       'EPS grew in most years':sum(eps_list[k]>eps_list[k+1] for k in range(len(eps_list)-1))>=max(1,len(eps_list)-2) if len(eps_list)>=3 else False,
       'Sensible price (forward P/E under 22)':fpe_now==fpe_now and fpe_now<22}
    out[t]=dict(t=t,fin=fin,yrs=yrs,rev_a=ser(rev),ni_a=ser(ni),fcf_a=ser(fcf),om_a=ser(om_s),roe_a=ser(roe_s),eps_a=ser(eps),
        cagr=cagr,roic=roic,sh_chg=sh_chg,cover=cover,fscore=fscore,Z=Z,accr=accr,buyback=-v(buyb,0) if buyb is not None else np.nan,div=-v(divp,0) if divp is not None else np.nan,
        beats=beats,nq=nq,avg_surp=avgs,eq_hist=eq_hist,next_date=next_date,eps0y=eps0y,eps1y=eps1y,rev90=rev90,up30=up30,dn30=dn30,ups=ups,downs=downs,ins_net=ins_net,news=news,
        qs=qs,q_yoy=q_yoy,wacc=wacc,impl_g=impl_g,g1=g1,methods=mv,fair=fair,disp=disp,base=base,bull=bull,bear=bear,exp=exp,
        exp_ret=exp/p-1,up=bull/p-1,down=bear/p-1,base_ret=base/p-1,capex_adj=capex_adj,g_cons=g_cons,oneoff=oneoff,buffett=B,bscore=int(sum(B.values())),fpe_now=fpe_now)
pickle.dump(out,open('s2.pkl','wb'))
x=pd.DataFrame(out).T
print(x[['fscore','Z','roic','beats','nq','rev90','bscore','exp_ret','up','down','disp']].astype(float).describe().round(2).to_string())
print(x.loc[['NVDA','GOOGL','LLY','V','JPM','MSFT','AAPL'],['cagr','roic','fscore','beats','rev90','bscore','base_ret','up','down','exp_ret']].to_string())
