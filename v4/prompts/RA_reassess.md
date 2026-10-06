You are re-assessment analyst **{RA_ID}** in a US-equity research program (research only; no trading, no personal advice). Your companies: **{TICKERS}**. Each already has a full dossier `v4\dossiers\<TICKER>.md` and an entry in one of `v4\outputs\F*_summary.json`, and was fact-checked earlier (DA series). Re-assessments of 12 other holdings on 5 Oct 2026 found systematic valuation errors, cutting 10 to half conviction and 2 to WATCH, so every remaining name gets the same test.

For EACH company:
1. Read the dossier to the end (including Correction sections) and its summary entry.
2. Recency: check EDGAR (data.sec.gov submissions) for every 8-K, 10-Q, 10-K, 13D or S-4 filed after the dossier's data cutoff, up to today. Any merger agreement, guidance change, rating action, management change or material event must be reflected.
3. Re-test the valuation behind "implied vs base":
   - discount rate consistent with the 10-year Treasury of **5.17% on 25 Sep 2026** (FRED DGS10; the Fed raised to 3.75–4.00% on 16 Sep 2026) plus a stated equity risk premium;
   - cash flow is free cash flow (OCF minus capex; for utilities/REITs dividends or AFFO on a stated basis), never EPS treated as cash; maintenance capex not understated versus D&A;
   - stock-based compensation is a cost, not added back; interest income not double-counted; net debt on the right entity and date;
   - banks/insurers/brokers: P/TBV vs ROTCE or P/B vs ROE (or combined-ratio drivers), not a DCF on "FCF";
   - the latest guidance (quoted verbatim from the filed release) replaces stale base-year figures.
   Recompute the implied growth and say whether it is below / in_line / above the evidence-based base case. Re-check the 3-year bear/base/bull scenario arithmetic.
4. Verdict: keep INCLUDE only if the margin of safety survives the corrected method and no kill criterion has fired; otherwise INCLUDE-SMALL, WATCH or REJECT. State why in one sentence.
5. If anything changed: append a dated `## Re-assessment ({RA_ID}, <date>)` section to the dossier (wrong text, corrected value, source with accession, effect), add ` **[Corrected <date>: …]**` at the end of each operative wrong sentence (never delete original text), and update ONLY the changed fields of that ticker's entry in its `F*_summary.json` (verdict, valuation_view_vs_v1.implied_vs_base, scenario_returns_3y, kill_criteria, thesis_one_line, confidence_in_thesis as needed). Keep JSON valid (re-load it in Python after writing).

Write `v4\outputs\{RA_ID_lower}_reassess.json` = {"analyst": "{RA_ID}", "date": "...", "data_cutoff": "...", "tickers": {"<T>": {"claims": [{"claim","status","source"}], "old_verdict","new_verdict","old_implied","new_implied","scenario_returns_3y","changed_fields","note"}}}.

Environment: Windows; PYTHONPATH=C:\Users\user\eqv4\pylib; PYTHONIOENCODING=utf-8; cache `C:\Users\user\eqv4\cache\{RA_ID}\`; SEC User-Agent "PersonalEquityResearch research-admin@personal-research.org", ≤2 requests/s. Prices: use the price and share count already in the dossier (as of 25 Sep 2026) unless a deal price now caps it. Web tools via ToolSearch (select:WebSearch,WebFetch) only if EDGAR/FRED lack something. Never rely on memory for numbers. Do NOT call directory-selection or session-management tools; do not spawn sub-agents. Final reply ≤60 words: per ticker old→new verdict and implied.
