# V1X agent -- SEC XBRL companyfacts fetcher (independent re-pull, cache only, no edits to other agents' files)
# Written independently of code/v1_valuation.py per the V1X independence rule.
import json, os, re, time, sys
import urllib.request as urlreq
import urllib.error as urlerr
import gzip

CACHE = r"C:\Users\user\eqv4\cache\V1X"
os.makedirs(CACHE, exist_ok=True)
UA = "PersonalEquityResearch research-admin@personal-research.org"

CIK = {
    "DLTR": 935703, "HST": 1070750, "JBHT": 728535, "ALL": 899051, "GL": 320335,
    "SWK": 93556, "HIG": 874766, "BMY": 14272, "MTB": 36270, "LMT": 936468,
    "FRT": 34903, "SYF": 1601712,
}

def fetch_companyfacts(ticker, cik):
    path = os.path.join(CACHE, f"{ticker}_CIK{cik:010d}_companyfacts.json")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return path
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    req = urlreq.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    for attempt in range(6):
        try:
            with urlreq.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                enc = resp.headers.get("Content-Encoding", "")
                if enc == "gzip":
                    raw = gzip.decompress(raw)
            data = json.loads(raw.decode("utf-8"))
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f)
            print(f"OK {ticker} CIK{cik} -> {path} ({os.path.getsize(path)} bytes)")
            return path
        except urlerr.HTTPError as e:
            print(f"HTTPError {ticker}: {e.code}, attempt {attempt}")
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            raise
        except Exception as e:
            print(f"Error {ticker}: {e}, attempt {attempt}")
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {ticker}")

if __name__ == "__main__":
    for t, c in CIK.items():
        fetch_companyfacts(t, c)
        time.sleep(0.6)  # <= ~1.6 req/s, under the 2 req/s cap given in the task
    print("done")
