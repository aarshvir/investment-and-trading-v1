# Independent challenge of industrials/payments valuations

Reviewed 26 September 2026 by the technology underwriting agent, independently of the root analyst who built these three models. Scope: `industrials_payments.json` and its arithmetic, against the complete cached Corpay/NetApp releases and the AMETEK issuer release and closing announcement. This is a second analytical pass, not an independent auditor opinion.

**Disposition: no decision-changing arithmetic or source-mapping defect found. Publish the three conditional decisions with the qualifications below.**

| Name | Recomputed base hurdle ceiling | Proposed limit | Arithmetic/source check |
|---|---:|---:|---|
| CPAY | $355.5744 | $350 | PASS: $27.35 − ($150m + $110.106m) × 74% / 66m = $24.43366 normalized starting EPS |
| NTAP | $154.3857 | $150 | PASS: $7.50 GAAP FY2027 guide midpoint, $2.19 SBC adjustment and $0.52 quarterly dividend match issuer release |
| AME | $187.1064 | $185 reconsideration | PASS: $8.20–$8.30 pre-close adjusted guide and $0.34 quarterly dividend match issuer; $0.05 acquisition accretion is distinctly analyst-assumed |

All three limits are below the present value of the specified base dividends and terminal earnings at their chosen hurdles. No scenario multiplies a price target into its own justification. All forecast growth rates and multiples remain judgment calls. CPAY's 26% normalizing tax is within the issuer's 25–27% adjusted outlook. The SBC and integration deductions are pretax amounts and are correctly tax-effected. The adjusted starting EPS still excludes intangible amortization; call it a normalized cash-earnings proxy, not GAAP or distributable FCF. This residual optimism is consistent with a lower terminal multiple and a deferred entry, but warrants a separate acquisition-return check before increasing weight.

NTAP's model correctly retains SBC, rather than capitalizing adjusted EPS $9.88 without accounting for employee compensation. Its FY2030 endpoint is a forward fiscal-year P/E at a September 2029 exit, not a trailing-year multiple. Inventory-turn and cash-conversion conditions are economically relevant. A $150 price alone would not cure a new inventory impairment or cash-collection failure.

AME remains **AVOID AT CURRENT PRICE**. Its $185 is a reconsideration price, not an unconditional cleared purchase, because post-close financing and acquired-profit evidence remain incomplete. This is a complete present decision. The adjusted baseline excludes integration/financing charges as well as acquired intangible amortization; the report must state this and must not describe it as clean GAAP recurring earnings. Recurring acquisition spending cannot permanently be treated as costless. The model's forward growth and premium 24x multiple are material sensitivities, not externally validated facts.

Implementation suggestions: remove the generic AME funding sentence from CPAY/NTAP's individual `conditional_entry` display; it only applies to AME. State explicitly that sell/hold decisions for existing positions depend on portfolio exposure and tax position. Do not market the three-point scenario spread as a confidence interval or claim these limits cap losses.

Primary checks: [Corpay release/reconciliation](https://www.sec.gov/Archives/edgar/data/1175454/000117545426000045/ex991q2_2026.htm), [NetApp Q1 FY2027 release](https://investors.netapp.com/news/news-details/2026/NetApp-Reports-First-Quarter-of-Fiscal-Year-2027-Results/default.aspx), [AMETEK Q2 release](https://investors.ametek.com/news-releases/news-release-details/ametek-announces-record-second-quarter-2026-results-and-raises), [AMETEK closing announcement](https://investors.ametek.com/news-releases/news-release-details/ametek-completes-acquisition-indicor-instrumentation).
