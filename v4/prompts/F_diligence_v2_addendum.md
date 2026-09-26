# Addendum v2 to F_diligence_analyst.md (Loop-2 requirements — these OVERRIDE the base template where they differ)

Why: Loop-1 auditors found (a) 13/15 held names had no one-line thesis in the structured output, (b) three names' kill
criteria existed in the dossier but not in the summary JSON, (c) one dossier's narrative called the valuation "earned"
while the systematic valuation model (V1) said "demanding" with a negative base case, and nobody reconciled the two.

1. **Summary JSON format (exact):** write `v4\outputs\{AGENT_ID}_summary.json` as
   `{"agent": "{AGENT_ID}", "as_of": "2026-09-25", "tickers": {"<TICKER>": {...}}}` where each ticker object has:
   - `verdict`: one of `INCLUDE`, `INCLUDE-SMALL`, `WATCH`, `REJECT`
   - `thesis_one_line`: ≤ 25 words, plain English a non-finance reader understands, no jargon, no ticker-speak
     (e.g. "America's largest hotel REIT owner, buying back stock at a discount to asset value while group travel recovers.")
   - `kill_criteria`: list of 3–5 strings, each **measurable** (a number, a threshold, a count of quarters) and each
     copied verbatim from dossier section 9
   - `key_adverse_facts`, `data_conflicts`, `next_earnings_date` (YYYY-MM-DD), `horizon`, `confidence_in_thesis`
   - `valuation_view_vs_v1`: `{"v1_verdict": ..., "v1_base_3y": ..., "dossier_view": "cheap|fair|full|expensive",
     "consistent": true|false, "reconciliation": "one or two sentences"}`
2. **Read the systematic valuation first:** your company's row in `v4\outputs\v1_valuation_table.csv` and its detail
   in `v4\outputs\v1_valuation.json` (method, WACC, implied growth, own-history percentile, bear/base/bull 3-yr returns).
   Your dossier's valuation section (7) must state V1's verdict and base case and say explicitly whether you agree.
   If you disagree, explain which V1 input you think is wrong, with a primary-source number. Never leave a silent
   conflict between the narrative and V1.
3. **Verdict discipline:** INCLUDE = would hold at full weight; INCLUDE-SMALL = investable but with a specific,
   named reservation (state it); WATCH = not now, with the condition that would change it; REJECT = thesis broken or
   unacceptable risk. Base the verdict on the evidence, not on the quant rank.
4. **End every dossier with a "Data basis, recency and disclaimer" block:** most recent period incorporated (with
   filing date), events checked to 2026-09-25, GAAP vs adjusted labelling statement, and "Research, not personal
   investment advice."
5. **Time box ~60 minutes per company.** If you run short, the priority order is: verdict + thesis line, results table,
   balance sheet / capital, valuation reconciliation with V1, kill criteria, red-flag scan, then the rest.
6. Run `scripts\lint_report.py` from the stock-analysis skill folder on each finished dossier; fix error-level findings.
7. Do NOT spawn sub-agents. Do NOT edit any file other than your dossiers, your summary JSON and your cache folder
   `C:\Users\user\eqv4\cache\{AGENT_ID}\`.
