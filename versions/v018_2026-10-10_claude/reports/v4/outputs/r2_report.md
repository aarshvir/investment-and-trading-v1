# R2 report (output-contract pointer)

**Status:** Complete (2026-09-26). The full deliverable is **`r2_implementation_facts.md`**. It is general factual information with citations, not personalised advice.

## Summary

- **US estate tax (NRA):**
  - The USD 13k credit (§2102(b)(1)) shelters about USD 60k of US-situs assets. Rates run 18–40% (§2001(c)).
  - Form 706-NA is required above USD 60k.
  - There is no US–UAE estate or income tax treaty.
  - Illustrative tax: USD 80k gives USD 5,200; USD 100k gives USD 10,800.
- **US dividends:**
  - A UAE resident suffers 30% withholding. W-8BEN does not reduce it.
  - Capital gains are generally not US-taxed (<183 days, no US trade or business).
- **UAE:**
  - No personal income tax.
  - Cabinet Decision 49/2023 excludes Personal Investment income from Corporate Tax.
- **Irish UCITS S&P 500 ETFs:**
  - Not US-situs.
  - US withholding is 15% at fund level for physical funds (CSPX, VUAA, SPY5) and about 0% for the swap-based SPXS, which carries counterparty and regulatory risk.
  - All-in annual drag at a 1.11% yield: VOO 0.36%, CSPX/VUAA 0.24%, SPY5 0.20%, SPXS 0.12%.
- **Brokers:**
  - IBKR (Pro): US stocks USD 0.005/share with a USD 1 minimum; LSE 0.05% of trade value; FX 0.2 bp with a USD 2 minimum.
  - Vested (VF Securities, cleared by DriveWealth): 0.25% commission (max USD 35); US stocks and ETFs only; the US stocks and ETFs held there are US-situs.

## Validation

9 checks passed, 0 failed. They are listed in §8 of the facts file.

## Files

| File | Size | Contents |
|---|---|---|
| `r2_implementation_facts.md` | — | Main report |
| `r2_estate_tax_scenarios.csv` (+ `.meta.json`) | 18 rows | Estate-tax scenario grid |
| `r2_tax_drag.csv` (+ `.meta.json`) | 15 rows | Tax-drag table |
| `../code/r2_implementation_calcs.py` | — | Calculation script |

Raw downloads are cached in `C:\Users\user\eqv4\cache\r2\`.

## Open items

See §9 of the facts file, which lists 12 unverified items. The main ones:
- whether UCITS ETFs can be bought as fractional shares at IBKR;
- which IBKR entity carries the account;
- the estate situs of cash held at US brokers;
- Irish inheritance tax (CAT) on US-listed Irish plcs;
- how long the §871(m) exception that SPXS relies on will last.
