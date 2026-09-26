import yfinance as yf, pandas as pd, json, time, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
U=pd.read_csv('universe.csv').t.tolist()
px=yf.download(U+['^GSPC','SPY'],period='3y',auto_adjust=True,progress=False,threads=True)
px['Close'].to_pickle('close.pkl'); px['Volume'].to_pickle('volume.pkl'); px['High'].to_pickle('high.pkl'); px['Low'].to_pickle('low.pkl')
print('prices done',flush=True)
def info(s):
    for k in range(3):
        try: return s,yf.Ticker(s).info
        except Exception: time.sleep(2)
    return s,{}
with ThreadPoolExecutor(16) as ex: infos=dict(ex.map(info,U))
json.dump(infos,open('info.json','w'),default=str)
print('info done',sum(1 for v in infos.values() if v.get('marketCap')),flush=True)
