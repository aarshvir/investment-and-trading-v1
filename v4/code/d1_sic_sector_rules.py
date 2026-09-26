"""d1_sic_sector_rules.py - explicit, documented SIC -> GICS-like 11-sector mapping.

Two layers:
 1. RANGE_RULES: a priori mapping of SIC ranges to the 11 GICS sectors (written from the SIC manual + GICS
    definitions, before looking at agreement).
 2. CODE_OVERRIDES: 4-digit exceptions (a priori, e.g. pharma 2834 inside chemicals) plus TUNED overrides that
    were added after measuring systematic mismatches vs current GICS (flagged tuned=True with the evidence).
Sector labels: Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials,
Information Technology, Communication Services, Utilities, Real Estate.
Known, irreducible limitation: SIC is an establishment/product code and several SIC codes contain companies in
different GICS sectors (7370/7372: internet media vs software; 5912: CVS (HC) vs Walgreens (Staples); 7374/7389:
payments (Financials) vs processing/HR services (Industrials/IT)). The mapping picks the majority.
"""
EN, MA, IN, CD, CS, HC, FN, IT, CM, UT, RE = ("Energy", "Materials", "Industrials", "Consumer Discretionary",
                                              "Consumer Staples", "Health Care", "Financials",
                                              "Information Technology", "Communication Services", "Utilities",
                                              "Real Estate")
SECTORS = [EN, MA, IN, CD, CS, HC, FN, IT, CM, UT, RE]

# (from, to, sector, note) - inclusive ranges, evaluated first-match in order of specificity (narrowest first)
RANGE_RULES = [
    (100, 999, CS, "Agriculture, forestry, fishing"),
    (800, 899, MA, "Forestry"),
    (1000, 1099, MA, "Metal mining"),
    (1200, 1299, EN, "Coal mining"),
    (1300, 1399, EN, "Oil & gas extraction and services"),
    (1400, 1499, MA, "Nonmetallic minerals mining"),
    (1500, 1599, CD, "Building construction (homebuilders = GICS Consumer Discretionary)"),
    (1600, 1799, IN, "Heavy & specialty construction contractors"),
    (2000, 2099, CS, "Food & kindred products"),
    (2100, 2199, CS, "Tobacco"),
    (2200, 2399, CD, "Textiles & apparel"),
    (2400, 2499, MA, "Lumber & wood products"),
    (2500, 2599, CD, "Furniture & fixtures"),
    (2600, 2699, MA, "Paper & allied products"),
    (2700, 2749, CM, "Publishing (newspapers, periodicals, books)"),
    (2750, 2799, IN, "Commercial printing & services"),
    (2800, 2829, MA, "Chemicals & plastics materials"),
    (2830, 2839, HC, "Drugs / pharmaceuticals / biologicals"),
    (2840, 2849, CS, "Soaps, detergents, cosmetics (household & personal products)"),
    (2850, 2899, MA, "Paints, agricultural & other chemicals"),
    (2900, 2999, EN, "Petroleum refining"),
    (3000, 3099, MA, "Rubber & plastics products"),
    (3100, 3199, CD, "Leather & footwear"),
    (3200, 3299, MA, "Stone, clay, glass, concrete"),
    (3300, 3399, MA, "Primary metals"),
    (3400, 3499, IN, "Fabricated metal products"),
    (3500, 3569, IN, "Industrial machinery"),
    (3570, 3579, IT, "Computer & office equipment"),
    (3580, 3599, IN, "Refrigeration/service/misc machinery"),
    (3600, 3629, IN, "Electrical equipment"),
    (3630, 3639, CD, "Household appliances"),
    (3640, 3649, IN, "Lighting & wiring equipment"),
    (3650, 3659, CD, "Household audio & video"),
    (3660, 3669, IT, "Communications equipment"),
    (3670, 3679, IT, "Electronic components & semiconductors"),
    (3680, 3699, IN, "Misc electrical machinery"),
    (3700, 3712, CD, "Motor vehicles"),
    (3713, 3716, IN, "Truck bodies, trailers, motor homes"),
    (3714, 3714, CD, "Motor vehicle parts"),
    (3720, 3729, IN, "Aircraft & parts"),
    (3730, 3749, IN, "Ships, railroad equipment"),
    (3750, 3759, CD, "Motorcycles & bicycles"),
    (3760, 3769, IN, "Guided missiles & space vehicles"),
    (3790, 3799, CD, "Misc transportation equipment"),
    (3800, 3839, IT, "Measuring, analysing & controlling instruments"),
    (3812, 3812, IN, "Search, detection, navigation (defense electronics)"),
    (3840, 3859, HC, "Medical, surgical, dental & ophthalmic instruments"),
    (3860, 3869, IT, "Photographic equipment"),
    (3870, 3879, CD, "Watches & clocks"),
    (3900, 3999, CD, "Misc manufacturing (jewelry, toys, sporting goods)"),
    (4000, 4099, IN, "Railroads"),
    (4100, 4299, IN, "Transit, trucking, warehousing"),
    (4400, 4499, IN, "Water transportation"),
    (4500, 4599, IN, "Air transportation"),
    (4600, 4699, EN, "Pipelines (ex natural gas)"),
    (4700, 4799, IN, "Transportation services"),
    (4800, 4899, CM, "Communications (telecom, broadcasting, cable)"),
    (4900, 4949, UT, "Electric, gas, water utilities"),
    (4922, 4923, EN, "Natural gas transmission (midstream = GICS Energy)"),
    (4950, 4959, IN, "Sanitary services (waste management)"),
    (4960, 4999, UT, "Steam, cogeneration & other utilities"),
    (5000, 5099, IN, "Wholesale - durable goods (trading companies & distributors)"),
    (5045, 5045, IT, "Wholesale - computers & software"),
    (5047, 5047, HC, "Wholesale - medical, dental & hospital equipment"),
    (5065, 5065, IT, "Wholesale - electronic parts"),
    (5100, 5199, CS, "Wholesale - nondurable goods (groceries etc.)"),
    (5122, 5122, HC, "Wholesale - drugs (drug distributors = GICS Health Care)"),
    (5170, 5179, EN, "Wholesale - petroleum products"),
    (5200, 5299, CD, "Building materials & garden retail"),
    (5300, 5399, CD, "General merchandise stores"),
    (5400, 5499, CS, "Food stores"),
    (5500, 5599, CD, "Auto dealers & gas stations"),
    (5600, 5699, CD, "Apparel & accessory stores"),
    (5700, 5799, CD, "Home furniture & electronics stores"),
    (5800, 5899, CD, "Eating & drinking places"),
    (5900, 5999, CD, "Misc retail"),
    (5912, 5912, CS, "Drug stores"),
    (6000, 6199, FN, "Banks & credit institutions"),
    (6200, 6299, FN, "Securities brokers, exchanges, asset managers"),
    (6300, 6499, FN, "Insurance"),
    (6500, 6599, RE, "Real estate operators, developers, agents"),
    (6700, 6799, FN, "Holding & other investment offices"),
    (6792, 6792, EN, "Oil royalty traders"),
    (6798, 6798, RE, "Real estate investment trusts"),
    (7000, 7099, CD, "Hotels & lodging"),
    (7200, 7299, CD, "Personal services"),
    (7300, 7319, CM, "Advertising"),
    (7320, 7369, IN, "Business services (credit reporting, building services, rental, staffing)"),
    (7370, 7379, IT, "Computer programming, software, data processing"),
    (7380, 7399, IN, "Misc business services"),
    (7500, 7599, IN, "Auto rental & repair services"),
    (7800, 7899, CM, "Motion pictures & video"),
    (7900, 7999, CD, "Amusement & recreation (casinos, parks)"),
    (8000, 8099, HC, "Health services"),
    (8100, 8199, IN, "Legal services"),
    (8200, 8299, CD, "Educational services"),
    (8300, 8399, HC, "Social services"),
    (8700, 8799, IN, "Engineering, accounting, research, management services"),
    (8731, 8731, HC, "Commercial physical & biological research (CROs)"),
    (8900, 8999, IN, "Services NEC"),
    (9995, 9995, FN, "Non-operating establishments (SPAC-like)"),
]

# 4-digit overrides. tuned=False: a priori; tuned=True: added after the agreement test on current members.
CODE_OVERRIDES = {
    # code: (sector, tuned, rationale)
}


def _rule_sector(sic: int):
    """narrowest matching range wins"""
    best = None
    for lo, hi, sec, note in RANGE_RULES:
        if lo <= sic <= hi:
            width = hi - lo
            if best is None or width < best[0]:
                best = (width, sec, f"range {lo}-{hi}: {note}")
    return (best[1], best[2]) if best else (None, "no rule")


def sic_to_sector(sic, overrides=None):
    """returns (sector, basis)"""
    if sic is None:
        return None, "missing SIC"
    try:
        s = int(sic)
    except (TypeError, ValueError):
        return None, "missing SIC"
    ov = CODE_OVERRIDES if overrides is None else overrides
    if s in ov:
        sec, tuned, why = ov[s]
        return sec, ("tuned override: " if tuned else "a-priori override: ") + why
    return _rule_sector(s)
