import pickle, re, json, pandas as pd, numpy as np
E=pickle.load(open('edgar.pkl','rb'))
RAISE=re.compile(r'\b(rais(e|es|ed|ing)|increas(e|es|ed|ing)|lift(s|ed)?|boost(s|ed)?|upgrad(e|ed)|above the high end|improv(e|es|ed))\b[^.]{0,120}\b(guidance|outlook|forecast|expectations?)\b|\b(guidance|outlook|forecast)\b[^.]{0,60}\b(rais(e|ed)|increas(e|ed))\b',re.I)
CUT=re.compile(r'\b(lower(s|ed|ing)?|reduc(e|es|ed|ing)|cut(s)?|withdr(aw|ew)|below)\b[^.]{0,120}\b(guidance|outlook|forecast)\b|\b(guidance|outlook)\b[^.]{0,60}\b(lowered|reduced|cut)\b',re.I)
KEEP=re.compile(r'\b(reaffirm(s|ed)?|maintain(s|ed)?|reiterat(e|es|ed)|confirm(s|ed)?)\b[^.]{0,120}\b(guidance|outlook)\b',re.I)
FLAG=dict(record=r'\brecord\b',headwind=r'\bheadwinds?\b',impair=r'\bimpairment',restruct=r'\brestructuring\b',investig=r'\b(investigation|subpoena)\b',weakness=r'\bmaterial weakness\b',goingc=r'\bgoing concern\b',buyback=r'\b(share repurchase|buyback|repurchased)\b',ai=r'\b(artificial intelligence|\bAI\b|generative)\b',tariff=r'\btariffs?\b')
res={}
for t,docs in E.items():
    if not docs: continue
    rows=[]
    for d in docs:
        tx=d['text'][:40000]
        sents=re.split(r'(?<=[.!?])\s+',tx)
        gs=[s for s in sents if re.search(r'\b(guidance|outlook)\b',s,re.I) and 30<len(s)<420]
        rows.append(dict(date=d['date'],url=d['url'],raise_=bool(RAISE.search(tx[:15000])),cut=bool(CUT.search(tx[:15000])),keep=bool(KEEP.search(tx[:15000])),
             **{k:len(re.findall(p,tx,re.I)) for k,p in FLAG.items()},gsent=gs[:3],head=tx[:500]))
    df=pd.DataFrame(rows).sort_values('date')
    n=len(df); r_=int(df.raise_.sum()); c_=int(df.cut.sum()); k_=int(df.keep.sum())
    last=df.iloc[-1]
    res[t]=dict(n=n,raises=r_,cuts=c_,keeps=k_,gscore=(r_-c_)/n,last_date=last.date,last_url=last.url,last_raise=bool(last.raise_),last_cut=bool(last.cut),
       record=int(df.record.sum()),headwind=int(df.headwind.sum()),impair=int(df.impair.sum()),restruct=int(df.restruct.sum()),investig=int(df.investig.sum()),
       weakness=int(df.weakness.sum()),goingc=int(df.goingc.sum()),ai=int(df.ai.sum()),tariff=int(df.tariff.sum()),
       timeline=[dict(d=x.date,r=bool(x.raise_),c=bool(x.cut),k=bool(x.keep),rec=int(x.record),hw=int(x.headwind)) for x in df.itertuples()],
       latest_guidance=list(dict.fromkeys(sum([x for x in df.gsent.iloc[-2:]],[])))[:4])
json.dump(res,open('edgar_read.json','w'))
T=pd.DataFrame(res).T[['n','raises','cuts','keeps','gscore','last_date','last_raise','last_cut','record','headwind','impair','investig','weakness']]
print(T.sort_values('gscore',ascending=False).to_string())
