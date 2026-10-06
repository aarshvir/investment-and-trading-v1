"""Build the immutable-input stocks-only correction artifacts; never edit parent releases."""
from __future__ import annotations

import csv
import hashlib
import html
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "GPT" / "2026-10-01"
PARENTS = ["v013_2026-10-01_codex", "v012_2026-09-27_codex", "v011_2026-09-27_claude"]
WEIGHTS = {"MSFT":8,"ADP":6,"TJX":6,"MCK":6,"PEP":6,"RSG":5,"MA":5,"STE":5,"DOV":5,"AXP":5,"CRH":5,"PG":5,"ALLE":5,"NVDA":4,"BALL":4,"BR":4,"PTC":4,"VEEV":4,"GDDY":4,"PEG":4}
REPLACEMENTS = {"PG":"Consumer Staples","PEP":"Consumer Staples","PEG":"Utilities"}
GATES = {
    "MSFT":"FY2027 cloud/AI cash conversion and capex; old $500 level was review only",
    "ADP":"Next payroll/client-fund-interest filing; include capitalized software and SBC",
    "TJX":"Tariffs, comparable sales and cash after capex/dividends",
    "MCK":"Current earnings/event check, customer concentration and working capital",
    "PEP":"H2 CFO less capex must support dividends; demand and debt",
    "RSG":"No equity-FCF/enterprise-WACC mix; debt-funded acquisitions",
    "MA":"Volume/regulation and premium valuation versus cash return",
    "STE":"Procedure volume, debt and sterilization cash conversion",
    "DOV":"Industrial order cycle and acquisition returns",
    "AXP":"Card loss rate, premium-spend trends and funding",
    "CRH":"Infrastructure volume and acquisition/capex cash use",
    "PG":"FY2027 0–3% core-EPS guidance, dividend coverage and 21x entry",
    "ALLE":"Owner cash and next results; old $145 level was review only",
    "NVDA":"AI customer/supply commitments and normalized FY horizon; old $215 review",
    "BALL":"Packaging volumes, raw input costs and capex",
    "BR":"Retention, cash conversion and capital allocation",
    "PTC":"Verify cause of Oct1 >4% delayed move; subscription and valuation",
    "VEEV":"Life-sciences customer retention and cash earnings",
    "GDDY":"Debt, buyback funding and share-count bridge",
    "PEG":"H2 cash after capex versus dividends; financing and rate-base return",
}
FRESH = {"MSFT","NVDA","ADP","TJX","RSG","PG","PEP","PEG"}
THREE_YEAR_FLAT_IRR = {"PG":3.84,"PEP":7.94,"PEG":9.43,"ADP":10.51,"TJX":9.75,"RSG":8.65}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def make_records():
    proposed = read_json(HERE / "slate_agent" / "stock_only_slate.json")
    old = {r["ticker"]:r for r in proposed["records"]}
    yahoo_def = {r["ticker"]:r for r in read_json(HERE / "forensic_agent" / "defensive_quotes.json")}
    cboe_def = {r["ticker"]:r for r in read_json(HERE / "forensic_agent" / "defensive_cboe_quotes.json")}
    live_old = {r["ticker"]:r for r in read_json(HERE / "INTRADAY_OCT1_CBOE.json")["records"]}
    records = []
    for ticker, weight in WEIGHTS.items():
        if ticker in REPLACEMENTS:
            yd = yahoo_def[ticker]
            cb = cboe_def[ticker]
            day = next(b for b in yd["bars"] if b["date_et"] == "2026-09-30")
            price = round(day["close"],2)
            previous = cb["data"]["prev_day_close"]
            live = cb["data"]["current_price"]
            live_sha = cb["raw_sha256"]
            yahoo_sha = yd["raw_sha256"]
            second_sha = cb["raw_sha256"]
            sector = REPLACEMENTS[ticker]
        else:
            row = old[ticker]
            cb = live_old[ticker]
            price = row["reference_yahoo_close_usd"]
            previous = row["cboe_late_trade_usd"]
            live = cb["close"]
            live_sha = cb["raw_sha256"]
            yahoo_sha = row["yahoo_raw_sha256"]
            second_sha = row["cboe_raw_sha256"]
            sector = row["sector"]
            assert cb["session_match"] and cb["prev_day_close"] == price
        assert abs(previous - price)/price <= 0.001
        records.append({
            "ticker":ticker,"instrument":"individual_US_listed_stock","sector":sector,
            "weight_pct":weight,"target_usd_50000":50000*weight/100,"target_usd_100000":100000*weight/100,
            "reference_close_date_et":"2026-09-30","reference_close_usd":price,
            "second_source_sep30_usd":previous,"second_source_gap_pct":round(abs(previous-price)/price*100,5),
            "oct1_delayed_intraday_usd":live,"oct1_intraday_change_from_sep30_pct":round((live/price-1)*100,3),
            "quote_raw_sha256_primary":yahoo_sha,"quote_raw_sha256_second":second_sha,
            "oct1_quote_raw_sha256":live_sha,
            "diligence":"primary_filing_challenge_v013_or_current" if ticker in FRESH else "inherited_v011_dossier_plus_quote_event_check",
            "action":"BUY_TARGET_AFTER_LIVE_ACCOUNT_GATE","live_gate":GATES[ticker],
            "modeled_flat_multiple_3yr_irr_pct":THREE_YEAR_FLAT_IRR.get(ticker),
            "prior_v013_funded_weight_pct":0,
            "prior_limit_status":"historical_review_only" if ticker in {"MSFT","NVDA","ALLE"} else "none",
        })
    return records


def make_workbook(records, sectors):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    ws = wb.active
    ws.title = "Stock targets"
    ws.append(["Ticker","Sector","Weight %","$50,000 target","$100,000 target","30 Sep USD close","1 Oct delayed USD","Oct move %","Diligence","Live gate"])
    for r in records:
        ws.append([r["ticker"],r["sector"],r["weight_pct"],r["target_usd_50000"],r["target_usd_100000"],r["reference_close_usd"],r["oct1_delayed_intraday_usd"],r["oct1_intraday_change_from_sep30_pct"],r["diligence"],r["live_gate"]])
    ws.append(["TOTAL","",f"=SUM(C2:C{len(records)+1})",f"=SUM(D2:D{len(records)+1})",f"=SUM(E2:E{len(records)+1})"])
    risk = wb.create_sheet("Risk and evidence")
    risk.append(["Metric","Value","Interpretation"])
    for row in [
        ("Individual stocks",100,"No strategic non-stock exposure"),("Treasury / bonds",0,"No target"),("ETF / index",0,"No target"),("Strategic cash",0,"No target"),
        ("Largest issuer weight",max(WEIGHTS.values()),"MSFT"),("Largest sector weight",max(sectors.values()),"Industrials"),
        ("GFC worst path %",-44.08,"Current-survivor historical replay, not forecast floor"),
        ("COVID worst path %",-35.51,"Same method"),("2022 worst path %",-21.03,"Same method"),
        ("Recent sample vol %",12.99,"753 common days, not loss cap"),
        ("Parent releases",", ".join(PARENTS),"Immutable source work")]:risk.append(row)
    sector_ws=wb.create_sheet("Sector targets")
    sector_ws.append(["GICS sector","Weight %"])
    for name, weight in sorted(sectors.items()):sector_ws.append([name,weight])
    audit=wb.create_sheet("Source and limits")
    for row in [
        ("Completed price session","2026-09-30","20/20 dual source identities within 0.1%"),
        ("Open-session check","2026-10-01 17:44–17:48 UTC","Delayed, not official close/executable"),
        ("Fresh primary subset",len(FRESH),"Of 20 final names; others inherit older dossiers"),
        ("Actual holdings","Unknown","Reconcile before placing any order"),
        ("Return hurdle","Not uniformly met","PG/PEP/PEG below old 12% at flat P/E"),
        ("Drawdown tolerance","15–20% previously given","100% stocks breached in observed crisis replays"),
    ]:audit.append(row)
    for sheet in wb:
        sheet.freeze_panes="A2"
        sheet.auto_filter.ref=sheet.dimensions
        for c in sheet[1]:
            c.fill=PatternFill("solid",fgColor="152B48")
            c.font=Font(color="FFFFFF",bold=True)
            c.alignment=Alignment(wrap_text=True)
        for col in sheet.columns:
            letter=get_column_letter(col[0].column)
            width=min(65,max(12,max(len(str(cell.value or "")) for cell in col)+2))
            sheet.column_dimensions[letter].width=width
    wb.save(HERE/"STOCKS_ONLY_TARGET_WORKBOOK.xlsx")


def make_dashboard(records, sectors):
    lines=[]
    for r in records:
        lines.append(f'<tr><td>{html.escape(r["ticker"])}</td><td>{html.escape(r["sector"])}</td><td>{r["weight_pct"]}%</td><td>${r["target_usd_50000"]:,.0f}</td><td>${r["reference_close_usd"]:,.2f}</td><td>{html.escape(r["live_gate"])}</td></tr>')
    bars=[]
    for sector,weight in sorted(sectors.items(),key=lambda v:-v[1]):
        bars.append(f'<div class="bar"><span>{html.escape(sector)}</span><b style="width:{weight*3}%"></b><strong>{weight}%</strong></div>')
    doc=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stocks-only decision · 1 Oct 2026</title><style>body{{margin:0;background:#0b1422;color:#e7edf4;font:16px/1.55 system-ui}}main{{max-width:1200px;margin:auto;padding:36px 22px}}h1{{font-size:clamp(30px,4vw,50px);line-height:1.12}}.eyebrow{{color:#f1c77a;text-transform:uppercase;letter-spacing:.12em}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}.card{{background:#14253b;padding:18px;border:1px solid #324965;border-radius:9px}}.card strong{{display:block;font-size:30px}}table{{border-collapse:collapse;width:100%;background:#14253b}}th,td{{padding:10px;text-align:left;border-bottom:1px solid #31435a;vertical-align:top}}th{{background:#1a3551}}.wrap{{overflow-x:auto}}.bar{{display:flex;align-items:center;gap:10px;margin:12px 0}}.bar span{{width:190px}}.bar b{{display:inline-block;background:#50b5aa;height:16px;border-radius:4px;max-width:70%}}.bar strong{{margin-left:auto}}a{{color:#bddcff}}.warning{{border-left:4px solid #e6ad5a;padding:12px 18px;background:#332a21}}p.small{{color:#afbdd0;font-size:14px}}</style><main><p class="eyebrow">Codex · decision correction · completed Sep 30 prices</p><h1>100% individual stocks</h1><p>New-money target for $50,000–$100,000. Zero Treasury, bonds, ETFs, index allocation or strategic cash. This model replaces v013; older reports remain archived.</p><div class="grid"><div class="card"><span>Direct stocks</span><strong>100%</strong><small>20 companies</small></div><div class="card"><span>Largest position</span><strong>8%</strong><small>MSFT</small></div><div class="card"><span>Financials</span><strong>10%</strong><small>From 25% in the challenged draft</small></div><div class="card"><span>GFC replay worst path</span><strong>−44.08%</strong><small>Hindsight stress, not a forecast</small></div></div><p class="warning">Your earlier 15–20% temporary-loss tolerance cannot be assured by this fully invested stock basket. Historical crises show materially deeper losses. PG, PEP and PEG lower the tested crisis drawdown but each fails the prior 12% return hurdle at an unchanged exit multiple.</p><h2>Target holdings</h2><div class="wrap"><table><thead><tr><th>Stock</th><th>Sector</th><th>Weight</th><th>$50k budget</th><th>Sep 30 close</th><th>Next decision gate</th></tr></thead><tbody>{''.join(lines)}</tbody></table></div><h2>Sector weights</h2>{''.join(bars)}<h2>What changed</h2><p>Replaced AMP 6%, HIG 5% and USB 4% in the first stock-only draft with PEP 6%, PG 5% and PEG 4%. Replayed the same six past stress episodes, audited latest available owner cash and terminal-multiple sensitivity, and retained every original source as a dated parent. Delayed October 1 quotes are a session check, not an executable offer.</p><p class="small">Read the memo, model, forensic filing challenge and risk replay in this package. Actual holdings and tax/cost details remain unknown; no trade has been placed. Prepared from completed Sep 30 US prices and Oct 1 evidence checks.</p></main></html>'''
    (HERE/"STOCKS_ONLY_DASHBOARD.html").write_text(doc,encoding="utf-8")


def package():
    zip_path=HERE/"STOCKS_ONLY_RELEASE_2026-10-01.zip"
    members=[p for p in HERE.rglob("*") if p.is_file() and p!=zip_path and p.name!="PACKAGE_CONTENTS.json"]
    contents=[{"path":p.relative_to(HERE).as_posix(),"bytes":p.stat().st_size,"sha256":digest(p)} for p in sorted(members)]
    (HERE/"PACKAGE_CONTENTS.json").write_text(json.dumps({"generated_utc":datetime.now(timezone.utc).isoformat(),"files":contents},indent=2),encoding="utf-8")
    members.append(HERE/"PACKAGE_CONTENTS.json")
    with ZipFile(zip_path,"w",compression=ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(members):z.write(p,"GPT/2026-10-01/stocks_only_correction/"+p.relative_to(HERE).as_posix())
        for source,name in [
            (ROOT/"versions"/PARENTS[0]/"package.zip","parent_completed/v013_package.zip"),
            (ROOT/"versions"/PARENTS[1]/"RELEASE_NOTES.md","parent_completed/v012_RELEASE_NOTES.md"),
            (ROOT/"versions"/PARENTS[2]/"RELEASE_NOTES.md","parent_completed/v011_RELEASE_NOTES.md"),
        ]:
            z.write(source,name)
        for source,name in [
            (HERE/"STOCKS_ONLY_DECISION_MEMO.md","review/weekly/2026-10-01_STOCKS_ONLY_DECISION_MEMO.md"),
            (HERE/"STOCKS_ONLY_MODEL.json","review/weekly/2026-10-01_STOCKS_ONLY_MODEL.json"),
            (HERE/"STOCKS_ONLY_ACTION_TABLE.csv","review/weekly/2026-10-01_STOCKS_ONLY_ACTION_TABLE.csv"),
            (HERE/"STOCKS_ONLY_TARGET_WORKBOOK.xlsx","review/weekly/2026-10-01_STOCKS_ONLY_TARGET_WORKBOOK.xlsx"),
        ]:z.write(source,name)
    with ZipFile(zip_path) as z:
        assert z.testzip() is None
    return zip_path


def main():
    records=make_records()
    sectors=defaultdict(int)
    for r in records:sectors[r["sector"]]+=r["weight_pct"]
    assert len(records)==20 and len({r["ticker"] for r in records})==20
    assert sum(r["weight_pct"] for r in records)==100 and max(r["weight_pct"] for r in records)==8
    assert max(sectors.values())<=25
    assert sum(r["target_usd_50000"] for r in records)==50000
    assert sum(r["target_usd_100000"] for r in records)==100000
    assert all(r["instrument"]=="individual_US_listed_stock" for r in records)
    assert all(r["second_source_gap_pct"]<=0.1 for r in records)
    assert all(r["quote_raw_sha256_primary"] and r["quote_raw_sha256_second"] and r["oct1_quote_raw_sha256"] for r in records)
    model={"status":"completed_stock_only_target_not_broker_order","author":"Codex","parents":PARENTS,
        "completed_price_cutoff_et":"2026-09-30","oct1_delayed_check_utc":"2026-10-01 17:44–17:48 UTC",
        "capital_range_usd":[50000,100000],"individual_stocks_pct":100,"treasury_bonds_pct":0,"index_etf_pct":0,"strategic_cash_pct":0,
        "sector_weights_pct":dict(sectors),"records":records,
        "historical_stress":{"gfc_endpoint_pct":-41.81,"gfc_worst_path_pct":-44.08,"covid_worst_path_pct":-35.51,"year2022_worst_path_pct":-21.03,"recent_sample_vol_pct":12.99,"risk_method":"current-survivor quarterly-rebalanced adjusted Yahoo; hindsight diagnostic with missing early histories"},
        "limits":"No uniformly comparable expected-return estimate; 15–20% loss cap infeasible for 100% unhedged stock model; actual holdings and live execution unknown."}
    (HERE/"STOCKS_ONLY_MODEL.json").write_text(json.dumps(model,indent=2),encoding="utf-8")
    with (HERE/"STOCKS_ONLY_ACTION_TABLE.csv").open("w",newline="",encoding="utf-8-sig") as f:
        cols=["ticker","action","weight_pct","target_usd_50000","target_usd_100000","reference_close_date_et","reference_close_usd","oct1_delayed_intraday_usd","prior_v013_funded_weight_pct","prior_limit_status","diligence","live_gate","sector","modeled_flat_multiple_3yr_irr_pct"]
        w=csv.DictWriter(f,fieldnames=cols,extrasaction="ignore");w.writeheader();w.writerows(records)
        for t,reason in [("AMP","6% draft rejected; rerating dependence"),("HIG","5% draft rejected; price above prior review and NICO one-off"),("USB","4% draft rejected; financial concentration and TBV sensitivity"),("PAYX","cash/dividend bridge and flat-P/E sensitivity"),("WEC","capex-funded regulated cash and low compressed-multiple return"),("LVS","terminal P/E dependence and capital intensity"),("LH","H2 FCF bridge"),("PGR","malformed inherited estimate"),("HBAN","duplicate bank credit exposure")]:
            w.writerow({"ticker":t,"action":"WAIT_EXCLUDED_FROM_NEW_MONEY_TARGET","weight_pct":0,"prior_v013_funded_weight_pct":0,"live_gate":reason})
    make_workbook(records,sectors)
    make_dashboard(records,sectors)
    validation={"status":"pass_with_explicit_evidence_limits","checked_utc":datetime.now(timezone.utc).isoformat(),"unique_stocks":20,"weight_total_pct":100,
        "non_stock_target_pct":0,"largest_name_pct":8,"largest_sector_pct":max(sectors.values()),"dual_feed_completed_close":20,"dual_feed_max_gap_pct":max(r["second_source_gap_pct"] for r in records),
        "delayed_oct1_session_checks":20,"fresh_primary_challenge_name_count":len(FRESH),"inherited_dossier_name_count":20-len(FRESH),"fully_refreshed_503_name_universe":False,
        "stress_replay_raw_hashes_present":(HERE/"risk_agent"/"raw_yahoo").exists(),"replacement_filing_hashes_present":(HERE/"forensic_agent"/"peg_20260630_10q.html").exists(),
        "parent_package_sha256":digest(ROOT/"versions"/PARENTS[0]/"package.zip"),
        "no_trading_or_broker_access":True,"unknown_actual_holdings":True,
        "material_open_questions":["PEP and PEG partial-period cash after capex below dividends","PG low no-rerating modeled return","12 final names rely on inherited older dossiers","15–20% drawdown cannot be assured","PTC and MCK Oct1 >4% move event cause not cleared"]}
    (HERE/"VALIDATION.json").write_text(json.dumps(validation,indent=2),encoding="utf-8")
    z=package()
    print(json.dumps({"zip":str(z),"bytes":z.stat().st_size,"sha256":digest(z),"weights":sum(WEIGHTS.values()),"sector_weights":sectors},default=dict))


if __name__=="__main__":main()
