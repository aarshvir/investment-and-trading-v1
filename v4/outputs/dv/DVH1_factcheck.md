# DVH1 verification, 6 Oct 2026

Scope: WTW, V, SNA, ACGL, WFC, TEL, ALLE, BRK-B, ACN, INTU. Research only; not personal advice. Full table: `DVH1_factcheck.json` (69 facts: 41 PASS, 18 FAIL, 9 MINOR, 1 UNVERIFIABLE).

Valuation re-tests used the programme parameters: 10-year Treasury 5.17% (25 Sep 2026), equity risk premium 4.14%, Blume-adjusted beta (Yahoo raw beta from the d4 snapshot), ten years of constant growth then 3.0% terminal, free cash flow after stock-based compensation; banks on P/TBV-ROTCE, Berkshire on P/B-ROE plus an operating-earnings test.

| Ticker | Result | Corrections written |
|---|---|---|
| WTW | Q4'25 revenue/FY25 margin mis-derived (Q4 $2,936M, not ~2,45x); Q1'26 organic 3% not 4%; +30bps belongs to HWC (R&B +100bps); EPS-based reverse DCF. Restated on FCF: implied 0.7%/yr vs 8-10% base: still below | Dossier + F49. Verdict unchanged |
| V | Facts pass. Reverse DCF used rf 4.2% and added back $0.9bn SBC; restated 11.1% vs 13% base (was 8.9%): still below, margin halved. "Five quarters" of litigation is seven; $563M severance omitted | Dossier + F58. Verdict unchanged |
| SNA | All load-bearing facts pass (Q2 sales/EPS, verbatim capex/tax outlook, consolidated net cash, FCF). Mixed sales bases in the quarterly table; WACC not tied to 5.17% (implied about 2% vs 5-7% base) | None (MINOR) |
| ACGL | All pass; DV01's correction is accurate (P/B 1.39x implies ROE 11.4%, or 9.0% at the programme CAPM rate) | None |
| WFC | Table and capital figures pass. EPS-based DCF (rf 4.2%, best quarter annualised) is the wrong method for a bank; P/TBV 1.80x implies ROTCE 13.9% vs 16.1% delivered: still below, thinner | Dossier + F49. Verdict unchanged |
| TEL | Quarterly table, FCF and debt mostly pass. FY26 "guidance raised, ~15% sales / 20%+ EPS" is not in the release (those are FQ2 actuals; TE guides one quarter); short-term debt $102M and $1.4bn Astrodyne deal omitted. Restated implied 6.9-7.6% vs 7% base: in line | Dossier + F106. **INCLUDE -> INCLUDE-SMALL** |
| ALLE | Quarterly figures and guidance pass; capex gap closed ($98.1M, ACF $685.7M); EPS guide raised once, not twice. Gordon model on a Yahoo FCF yield replaced; implied 5.4-6.6% vs 6% base: in line | Dossier + F100. **INCLUDE -> INCLUDE-SMALL** |
| BRK-B | Results, cash ($365.5bn / $397.4bn), buybacks and equity purchases pass. 68% of Q2 operating-earnings growth is an FX swing (underwriting -13%); no valuation method existed; P/B 1.45x. Tests mixed: in line | Dossier + F79. **INCLUDE -> INCLUDE-SMALL** |
| ACN | All pass; DV01's net cash $2.73bn, -2.4% reverse DCF and Q4 FY26 update independently confirmed | None |
| INTU | Q4 EPS reported $1.34/$1.35 (not derived $1.30/$1.28); capex $221M; FY27 non-GAAP guide includes a $5.81 SBC cost (SBC no longer excluded from 1 Aug 2026), not an add-back; single-stage DCF restated: about -2.2%/yr vs ~15% base | Dossier + F45. Verdict unchanged |

Verdict changes: TEL, ALLE and BRK-B INCLUDE -> INCLUDE-SMALL (implied vs base restated from below/unstated to in line). Implied-vs-base restated without verdict change: none (V, WTW, WFC, INTU stay below).

Limits: Visa's verbal guidance and the "14 consecutive quarters" of Berkshire net selling could not be verified on EDGAR (secondary sources); TE's "$3B AI target pulled forward" is not in the release. Beta is the d4 snapshot's Yahoo value, Blume-adjusted, not a recomputed 5-year weekly regression. Scenario returns were not re-derived for tickers whose method (exit multiples) is unaffected; WFC's scenario EPS base ($8.00) and INTU's non-GAAP base ($24.27, SBC excluded) are flagged as on the old basis. Summary JSON files were reserialised with a scenario_returns_3y one-line format for all tickers in the touched files (content unchanged).
