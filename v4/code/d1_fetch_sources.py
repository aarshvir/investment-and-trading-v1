"""d1_fetch_sources.py - download raw sources for D1 into C:\\Users\\user\\eqv4\\cache\\d1 (idempotent).

Sources:
  * GitHub fja05680/sp500 (README + historical component CSVs + ticker start/end + changes since 2019)
  * Wikipedia 'List of S&P 500 companies' HTML (current constituents)
  * Wikipedia 'Historical components of the S&P 500' HTML (changes table; moved out of the main list article)
  * SEC company_tickers.json, company_tickers_exchange.json, cik-lookup-data.txt
Writes CACHE/fetch_log.json with retrieval UTC times.
"""
import json
import sys

from d1_common import (CACHE, FJA_BASE, FJA_FILES, WIKI_URL, WIKI_HIST_URL, SEC_TICKERS_URL, SEC_TICKERS_EXCH_URL,
                       SEC_CIK_LOOKUP_URL, fetch_to_cache, utcnow_iso)


def main(refresh: bool = False):
    log_path = CACHE / "fetch_log.json"
    log = json.loads(log_path.read_text()) if log_path.exists() else {}
    items = []
    for name, enc in FJA_FILES.items():
        items.append((FJA_BASE + enc, CACHE / "fja" / name, False))
    items.append((WIKI_URL, CACHE / "wiki_sp500.html", False))
    items.append((WIKI_HIST_URL, CACHE / "wiki_sp500_historical.html", False))
    items.append((SEC_TICKERS_URL, CACHE / "company_tickers.json", True))
    items.append((SEC_TICKERS_EXCH_URL, CACHE / "company_tickers_exchange.json", True))
    items.append((SEC_CIK_LOOKUP_URL, CACHE / "cik-lookup-data.txt", True))
    for url, dest, sec in items:
        existed = dest.exists()
        try:
            fetch_to_cache(url, dest, sec=sec, refresh=refresh)
            if not existed or refresh:
                log[str(dest.name)] = {"url": url, "retrieved_utc": utcnow_iso(), "bytes": dest.stat().st_size}
            print(f"OK {dest.name} {dest.stat().st_size:,} bytes")
        except Exception as e:  # keep going, record failure
            print(f"FAIL {url}: {e}", file=sys.stderr)
            log[str(dest.name)] = {"url": url, "error": str(e), "attempt_utc": utcnow_iso()}
    log_path.write_text(json.dumps(log, indent=2))


if __name__ == "__main__":
    main(refresh="--refresh" in sys.argv)
