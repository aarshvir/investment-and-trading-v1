"""r3_curated_sources.py - Agent R3: machine-readable, source-cited tables transcribed from primary documents.

Writes (v4/data): r3_spiva.csv, r3_published_base_rates.csv, r3_literature.csv (+ .meta.json each).
Every row carries source URL, publication date, and verification status:
  VERIFIED-R3      = number checked by R3 in the primary document (PDF text / official page) on 2026-09-26
  VERIFIED-SUB     = checked by an R3 research sub-agent in the primary document (not re-checked by R3)
  SECONDARY        = only available from a secondary/mirror source
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from r3_french_lib import DATA, write_meta  # noqa: E402

YE25 = ("SPIVA U.S. Year-End 2025", "2026-03-03", "https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2025.pdf", "2025-12-31")
MY26 = ("SPIVA U.S. Mid-Year 2026", "2026-09-17", "https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-mid-year-2026.pdf", "2026-06-30")
YE24 = ("SPIVA U.S. Year-End 2024", "2025-03-04", "https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2024.pdf", "2024-12-31")
H = ["1y", "3y", "5y", "10y", "15y", "20y"]
spiva_rows = []


def add(rep, category, benchmark, measure, vals, status, horizons=H):
    for h, v in zip(horizons, vals):
        spiva_rows.append({"report": rep[0], "published": rep[1], "data_as_of": rep[3], "category": category, "benchmark": benchmark,
                           "measure": measure, "horizon": h, "value_pct": v, "source_url": rep[2], "verification": status})


add(YE25, "All Large-Cap Funds", "S&P 500", "% underperforming (absolute, count-based, Report 1a)", [78.78, 66.84, 88.96, 85.59, 89.93, 92.89], "VERIFIED-R3")
add(YE25, "All Domestic Funds", "S&P Composite 1500", "% underperforming (absolute, Report 1a)", [79.83, 80.40, 91.47, 90.43, 93.15, 95.01], "VERIFIED-R3")
add(YE25, "All Large-Cap Funds", "S&P 500", "% underperforming (risk-adjusted, Report 1b)", [82.76, 91.14, 95.73, 98.61, 97.76], "VERIFIED-R3", H[1:])
add(MY26, "All Large-Cap Funds", "S&P 500", "% underperforming (absolute, count-based, Report 1a)", [78.69, 76.63, 89.32, 83.33, 90.49, 92.61], "VERIFIED-R3")
add(MY26, "All Large-Cap Funds", "S&P 500", "% underperforming (absolute, Report 1a)", [67.18], "VERIFIED-R3", ["YTD (H1 2026)"])
add(MY26, "All Domestic Funds", "S&P Composite 1500", "% underperforming (absolute, Report 1a)", [60.82, 79.31, 91.40, 88.19, 93.25, 94.89], "VERIFIED-SUB")
add(YE24, "All Large-Cap Funds", "S&P 500", "% underperforming (absolute, Report 1a)", [65.24, 84.96, 76.26, 84.34, 89.50, 91.99], "VERIFIED-SUB")
add(YE25, "All Large-Cap Funds", "-", "fund survival rate (Report 2)", [67.02, 34.61], "VERIFIED-SUB", ["10y", "20y"])
add(MY26, "All Large-Cap Funds", "-", "fund survival rate (Report 2)", [68.75, 36.52], "VERIFIED-R3", ["10y", "20y"])
# annual large-cap underperformance rates 2001-2025 (YE2025 exhibit; 25 values)
annual = [65, 68, 75, 69, 49, 68, 45, 56, 48, 66, 82, 63, 55, 87, 65, 66, 63, 65, 71, 60, 85, 51, 60, 65, 79]
for yr, v in zip(range(2001, 2026), annual):
    spiva_rows.append({"report": YE25[0], "published": YE25[1], "data_as_of": YE25[3], "category": "All Large-Cap Funds", "benchmark": "S&P 500",
                       "measure": "% underperforming in calendar year (annual series exhibit)", "horizon": str(yr), "value_pct": v,
                       "source_url": YE25[2], "verification": "VERIFIED-R3"})
PERS = ("SPIVA U.S. Persistence Scorecard Year-End 2025", "2026-05-07", "https://www.spglobal.com/spdji/en/documents/spiva/persistence-scorecard-year-end-2025.pdf", "2025-12-31")
for cat, meas, h, v in [
    ("Large-cap", "top quartile in CY2023 staying top quartile through 2025 (3 consecutive yrs)", "3 consecutive years", 28.90),
    ("All Domestic", "top quartile in CY2023 staying top quartile through 2025", "3 consecutive years", 33.01),
    ("Large-cap", "top half staying top half 3 consecutive yrs (random expectation 25%)", "3 consecutive years", 49.41),
    ("Large-cap", "top quartile in CY2021 staying top quartile 5 consecutive yrs", "5 consecutive years", 0.00),
    ("All Domestic", "top quartile in CY2021 staying top quartile 5 consecutive yrs", "5 consecutive years", 0.00),
    ("Large-cap", "top half staying top half 5 consecutive yrs (random expectation 6.25%)", "5 consecutive years", 4.49),
    ("Large-cap", "top-quartile over 2015-20 still top quartile over 2020-25 (random 25%)", "5y->next 5y", 13.84),
    ("All Domestic", "top-quartile over 2015-20 still top quartile over 2020-25 (random 25%)", "5y->next 5y", 11.79),
    ("Large-cap", "top-half over 2015-20 still top half over 2020-25 (random 50%)", "5y->next 5y", 39.62),
]:
    spiva_rows.append({"report": PERS[0], "published": PERS[1], "data_as_of": PERS[3], "category": cat, "benchmark": "peer ranking",
                       "measure": meas, "horizon": h, "value_pct": v, "source_url": PERS[2], "verification": "VERIFIED-SUB"})
spiva = pd.DataFrame(spiva_rows)
p = DATA / "r3_spiva.csv"
spiva.to_csv(p, index=False)
write_meta(p, {"description": "S&P Dow Jones Indices SPIVA U.S. scorecards: share of active funds underperforming; persistence",
               "rows": len(spiva), "columns": list(spiva.columns),
               "retrieval": "spglobal.com blocks plain HTTP fetch; PDFs retrieved via Firecrawl scrape on 2026-09-25/26 UTC; "
                            "R3 cached MY2026 and YE2025 scrapes in C:/Users/user/eqv4/cache/r3/spiva_*_firecrawl.json",
               "caveats": ["Count-based (equal-weighted) unless stated; survivorship-adjusted by S&P DJI (merged/liquidated funds count as underperformers)",
                           "Persistence random-chance benchmarks as stated by S&P DJI (25% for 3-yr top-half, 6.25% for 5-yr top-half)."]})

# ------------------------------------------------------------------ published single-stock / market base rates
BR = [
    # source, metric, value, sample, url, date, status
    ("Bessembinder (2018) JFE 129(3):440-457", "share of CRSP common stocks with lifetime buy-and-hold return > 1-month T-bills", "42.6%", "US CRSP 1926-2016, 25,967 stocks",
     "https://doi.org/10.1016/j.jfineco.2018.06.004 (accepted MS text checked)", "2018", "VERIFIED-R3"),
    ("Bessembinder (2018)", "share of stocks beating the value-weighted market: annual / decade / lifetime", "44.4% / 37.3% / 30.8%", "US CRSP 1926-2016 (Table 2A)",
     "https://doi.org/10.1016/j.jfineco.2018.06.004", "2018", "VERIFIED-R3"),
    ("Bessembinder (2018)", "share beating 1-month T-bills: annual / decade / lifetime", "51.6% / 49.5% / 42.6%", "US CRSP 1926-2016 (Table 2A)",
     "https://doi.org/10.1016/j.jfineco.2018.06.004", "2018", "VERIFIED-R3"),
    ("Bessembinder (2018)", "share of monthly stock returns > T-bill", "47.8%", "US CRSP 1926-2016", "https://doi.org/10.1016/j.jfineco.2018.06.004", "2018", "VERIFIED-R3"),
    ("Bessembinder (2018)", "firms accounting for all net wealth creation", "1,092 firms = 4.31% of 25,332 firms", "US 1926-2016",
     "https://doi.org/10.1016/j.jfineco.2018.06.004", "2018", "VERIFIED-R3"),
    ("Bessembinder (2018)", "share with positive lifetime return; median lifetime return", "49.5%; median -2.29%", "US CRSP 1926-2016",
     "https://doi.org/10.1016/j.jfineco.2018.06.004", "2018", "VERIFIED-R3 (sign inferred: <50% positive)"),
    ("Bessembinder, Chen, Choi & Wei (2023) FAJ 79(3):33-63", "share of stocks underperforming 1-month T-bills over life", "US 55.2%; non-US 57.4%",
     "64,000+ global stocks 1990-2020", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3710251", "2023", "VERIFIED-SUB"),
    ("Bessembinder (2026) 'One Hundred Years in the U.S. Stock Markets' (SSRN)", "median buy-and-hold return; share reducing wealth", "median -6.9%; ~60% reduced wealth",
     "29,754 US stocks 1926-2025", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6438198", "2026-03-18", "VERIFIED-SUB"),
    ("J.P. Morgan Eye on the Market, 'Agony & Ecstasy' (Cembalest, 2021)", "catastrophic loss (-70% from peak, not recovered) / negative absolute return / underperformed Russell 3000 / megawinners",
     "44% / 42% / 66% / 10%", "Russell 3000 constituents 1980-2020",
     "https://assets.jpmprivatebank.com/content/dam/jpm-pb-aem/global/en/documents/eotm/agony-ecstasy-2021.pdf", "2021-03-15", "VERIFIED-R3"),
    ("J.P. Morgan 'Agony & Ecstasy' (2014, v2.0)", "catastrophic loss / negative absolute / underperformed Russell 3000 (median excess -54%)", "40% / 40% / 64%",
     "~13,000 Russell 3000 stocks 1980-2014", "https://www.researchgate.net/publication/303696398 (mirror)", "2014", "SECONDARY (mirror; VERIFIED-SUB)"),
    ("Dimensional, 'Singled Out' (Crill)", "share of US stocks that survived AND beat the market over 5 / 10 / 20 yrs", "34.7% / 28.8% / 21.4%",
     "US stocks, rolling, 1927-2020", "https://www.dimensional.com/ie-en/insights/singled-out-historical-performance-of-individual-stocks", "2022-05-11", "VERIFIED-R3"),
    ("Dimensional, 'Singled Out'", "past 20-yr winners vs losers surviving & beating market next 10 yrs", "30.2% vs 30.3% (all stocks 24.3%)",
     "US 1947-2020", "https://www.dimensional.com/ie-en/insights/singled-out-historical-performance-of-individual-stocks", "2022-05-11", "VERIFIED-R3"),
    ("S&P DJI SPIVA YE2025, Exhibit 7", "share of S&P 500 stocks beating the index in 2025 (Q1/Q2/Q3/Q4)", "30% (62/29/38/40%)", "S&P 500 constituents 2025",
     YE25[2], "2026-03-03", "VERIFIED-R3"),
    ("S&P DJI Indexology blog 'Skewing Success'", "share of S&P 500 constituents beating the index: 2023 / 2024", "26% / 28%", "S&P 500",
     "https://www.indexologyblog.com/2025/09/30/skewing-success/", "2025-09-30", "VERIFIED-SUB"),
    ("S&P DJI 'Shooting the Messenger'", "stocks in the S&P 500 at some point 2002-2021 beating the average", "26% (253 of 975); 20-yr median return 88% vs mean 358%",
     "S&P 500 2002-2021", "https://www.spglobal.com/spdji/en/documents/research/research-shooting-the-messenger.pdf", "2022-11-22", "VERIFIED-SUB"),
    ("'The Capitalism Distribution' (Blackstar/Longboard, c.2008)", "Russell 3000-eligible stocks: negative lifetime return / underperformed index / lost >=75%",
     "39% / 64% / 18.5%", "8,054 stocks 1983-2007",
     "https://web.archive.org/web/20160309100319id_/http://theivyportfolio.com/wp-content/uploads/2008/12/thecapitalismdistribution.pdf", "c.2008", "VERIFIED-SUB"),
    ("Anarkulova, Cederburg & O'Doherty (2022) JFE 143(1):409-433", "probability a diversified investor loses to inflation over 30 years", "12%",
     "39 developed markets 1841-2019 (bootstrap)", "https://doi.org/10.1016/j.jfineco.2021.06.040", "2022", "VERIFIED-R3 (abstract via RePEc)"),
    ("Dimensional, 'The Uncommon Average'", "S&P 500 positive over rolling 1 / 5 / 10 years", "75.2% / 87.7% / 94.7%", "1926-2018 overlapping",
     "https://www.dimensional.com/us-en/insights/the-uncommon-average", "2019-05-02", "VERIFIED-SUB"),
    ("MSCI Barra, Gleiser & McKenna 'Converting Scores into Alphas'", "practitioner IC benchmarks", "'good' IC 0.05; 'very good' 0.10",
     "practitioner note", "https://www.msci.com/documents/10199/1645561/PI_Converting_Scores_Into_Alphas.pdf", "2010-05", "VERIFIED-R3"),
]
br = pd.DataFrame(BR, columns=["source", "metric", "value", "sample", "url", "published", "verification"])
p2 = DATA / "r3_published_base_rates.csv"
br.to_csv(p2, index=False)
write_meta(p2, {"description": "Published single-stock and market base rates (transcribed, cited)", "rows": len(br), "columns": list(br.columns)})

# ------------------------------------------------------------------ literature (filled from verified records; see r3_literature_records.py)
try:
    from r3_literature_records import LIT  # noqa: E402
    lit = pd.DataFrame(LIT)
    p3 = DATA / "r3_literature.csv"
    lit.to_csv(p3, index=False)
    write_meta(p3, {"description": "Factor/anomaly literature table (paper, authors, journal, year, sample, key finding, decay/caveats, DOI/URL)",
                    "rows": len(lit), "columns": list(lit.columns)})
    print("literature rows:", len(lit))
except ImportError:
    print("literature records not yet available")
print("spiva rows:", len(spiva), "| base-rate rows:", len(br))
