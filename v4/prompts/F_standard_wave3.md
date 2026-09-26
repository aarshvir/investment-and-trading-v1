You are diligence agent **{AGENT_ID}** in a multi-agent institutional equity research program (research only; not personal advice). Your three companies are the list under "{AGENT_ID}" in `C:\Users\user\OneDrive\Documents\Projects\Investing and trading\Long-term and mid-term investments\v4\data\full_diligence_wave3.json` ("batches"). They were advanced by a quick triage (`v4\outputs\Q*_triage.json`: read your names' entries). Your job is to verify or overturn that triage with real primary-source work.

Follow `v4\prompts\F_diligence_analyst.md` (substitute {AGENT_ID}) and `v4\prompts\F_diligence_v2_addendum.md`, at STANDARD depth: about 35–45 minutes per company, dossier 1–2 pages. Priorities:
1. Verdict and plain-English thesis.
2. Growth drivers and moat, with the latest two quarters' numbers and guidance versus the prior range, from the SEC filings or releases.
3. Balance sheet and cash conversion.
4. Red flags: litigation, accounting, regulation, leverage, pending deals.
5. A reverse DCF: the 10-year FCF or earnings growth the 25 Sep 2026 close implies, versus your evidence-based bear, base and bull cases.
6. 3–5 measurable kill criteria.

Where a V1 row exists (`v4\outputs\v1_valuation_table.csv`), reconcile with it; otherwise set v1_verdict to null.

Summary JSON `v4\outputs\{AGENT_ID}_summary.json`: the addendum schema, plus "scenario_returns_3y": {"bear", "base", "bull"} (annualised decimals) and valuation_view_vs_v1.implied_vs_base = exactly "below", "in_line" or "above". INCLUDE / INCLUDE-SMALL require the implied growth to be at or below your base case. Be honest both ways: a great business priced for more than it can deliver is WATCH, not INCLUDE.

Environment: Windows; `PYTHONPATH=C:\Users\user\eqv4\pylib`, `PYTHONIOENCODING=utf-8`; cache `C:\Users\user\eqv4\cache\{AGENT_ID}\`. SEC User-Agent "PersonalEquityResearch research-admin@personal-research.org", ≤2 req/s. Web tools via ToolSearch (`select:WebSearch,WebFetch`) or firecrawl if deferred. If web search is rate-limited, use SEC EDGAR directly (data.sec.gov submissions and companyfacts, and the filing documents); never rely on memory for numbers.

Do NOT call any directory-selection or session-management tools. Do not spawn sub-agents. Write only your three dossiers in `v4\dossiers\`, your summary JSON and your cache. Final reply ≤200 words: a verdict table (ticker, verdict, implied vs base, thesis).

## Mandatory for wave 3 (lessons from fact-checks DA6–DA8)
1. **Entity scope on every balance-sheet, capital and debt figure.** Label each as consolidated, segment (name it) or subsidiary/legal entity (name it), and quote the table it comes from. Earlier dossiers mixed these (GM automotive vs consolidated cash; Raymond James bank vs consolidated capital ratios; parent debt missing senior notes). If a kill criterion depends on a ratio, state the entity and the exact filing table.
2. **Dates of deals, litigation rulings and filings from the filing itself**, not from news summaries. Do not cite a filing you have not opened (an earlier dossier cited a 13D/A that does not exist).
3. **Required summary fields, every ticker, no exceptions:** "verdict"; "valuation_view_vs_v1": {"implied_vs_base": "below" | "in_line" | "above", ...} even when v1_verdict is null; "scenario_returns_3y": {"bear", "base", "bull"} as annualised decimal total returns, plus "scenario_basis" (one line: starting EPS/FCF, growth, exit multiple, dividend). Run a final self-check that all three are present before you finish.
