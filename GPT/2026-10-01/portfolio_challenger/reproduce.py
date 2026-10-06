"""Reproduce bounded portfolio diagnostics from immutable v011/v012 sources.

This deliberately does not estimate forward return probabilities or optimize weights.
"""

from __future__ import annotations

import json
import math
import hashlib
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "versions/v011_2026-09-27_claude/package.zip"
OUTPUT = Path(__file__).with_name("diagnostics.json")


def main() -> None:
    with zipfile.ZipFile(PACKAGE) as archive:
        member_paths = [
            "v4/outputs/lead_portfolio_build.json",
            "v4/outputs/lead_j_sensitivity.json",
            "v4/outputs/lead_risk_results.json",
            "v4/outputs/v1_valuation.json",
        ]
        raw = {path: archive.read(path) for path in member_paths}
        member_hashes = {path: hashlib.sha256(content).hexdigest() for path, content in raw.items()}
        build = json.loads(raw[member_paths[0]])
        sensitivity = json.loads(raw[member_paths[1]])
        risk = json.loads(raw[member_paths[2]])
        valuations = json.loads(raw[member_paths[3]])["companies"]

    archive_hasher = hashlib.sha256()
    with PACKAGE.open("rb") as package_stream:
        for chunk in iter(lambda: package_stream.read(1024 * 1024), b""):
            archive_hasher.update(chunk)

    eligible = [row for row in build["candidates"] if row.get("eligible") is True]
    finite_base = [row for row in eligible if isinstance(row.get("base"), (int, float)) and math.isfinite(row["base"])]
    orderings = {
        title: {
            "overlap_with_actual": item["overlap_with_actual"],
            "weighted_base_return_unvalidated": item["weighted_base_return"],
            "same_set_as_actual": set(item["names"]) == set(build["selected"]),
        }
        for title, item in sensitivity["orderings"].items()
    }

    flat_multiple = {}
    for ticker in ("CMCSA", "BKNG", "LVS"):
        item = valuations[ticker]
        base = item["scenarios"]["base"]
        price = item["inputs"]["price_2026_09_25"]
        current_multiple = item["multiples"]["value_now"]
        exit_multiple = base["exit_multiple"]
        eps_year3 = base["eps_or_ffops_yr3"]
        cumulative_dividends = base["cum_dividends"]
        flat_return = ((current_multiple * eps_year3 + cumulative_dividends) / price) ** (1 / 3) - 1
        flat_multiple[ticker] = {
            "price_sep25": price,
            "current_ntm_pe": current_multiple,
            "v1_base_exit_pe": exit_multiple,
            "v1_base_eps_year3": eps_year3,
            "v1_cumulative_dividends": cumulative_dividends,
            "v1_base_annualized_return": base["annualised_return_3y"],
            "flat_multiple_annualized_endpoint_return": flat_return,
            "method": "V1 EPS year 3 and total dividends held fixed; substitute current NTM P/E for V1 exit P/E; compound total endpoint value over three years. No tax, costs, dividend timing or estimate repair.",
        }

    # WEC has no V1 record. Use its archived dossier's September price and FY2026
    # EPS guidance midpoint, but replace the dossier's stale dividend estimate
    # with the issuer's $0.9525 quarterly 2026 declaration.
    wec_price, wec_eps0, wec_eps_growth, wec_dividend = 101.45, 5.56, 0.075, 3.81
    wec_eps3 = wec_eps0 * (1 + wec_eps_growth) ** 3

    def wec_cashflow_irr(exit_pe: float) -> float:
        terminal = wec_eps3 * exit_pe
        lo, hi = -0.99, 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            present_value = sum(wec_dividend / (1 + mid) ** year for year in (1, 2, 3))
            present_value += terminal / (1 + mid) ** 3
            if present_value > wec_price:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    replay = {}
    for row in risk["stress"]:
        replay[row["episode"]] = {
            "v011_stock_sleeve": row["sleeve"],
            "spy": row["spy"],
            "v011_defensive_15_index_10_direct_75_reserve": row["Defensive (15/10/75)"],
            "v011_defensive_worst_point": row["Defensive (15/10/75) | worst point"],
            "v011_moderate_55_index_15_direct_30_reserve": row["Moderate (55/15/30)"],
            "sleeve_real_data_share": row["sleeve_real_data_share"],
        }

    weights = build["weights"]
    direct_10 = {ticker: 0.10 * weight for ticker, weight in weights.items()}
    sector_weights = build["sectors"]
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source_release": "v011_2026-09-27_claude",
        "comparison_release": "v012_2026-09-27_codex",
        "source_archive": str(PACKAGE.relative_to(ROOT)).replace("\\", "/"),
        "source_archive_sha256": archive_hasher.hexdigest(),
        "source_members_sha256": member_hashes,
        "coverage": {
            "eligible_candidates": len(eligible),
            "eligible_with_numeric_finite_base_scenario": len(finite_base),
            "v011_holdings": len(weights),
            "selected_with_v1_valuation": sum(t in valuations for t in weights),
        },
        "ordering_sensitivity": orderings,
        "in_every_ordering": sensitivity["in_every_ordering"],
        "flat_multiple_diagnostic": flat_multiple,
        "wec_diagnostic": {
            "price_sep25": wec_price,
            "fy2026_guided_eps_midpoint": wec_eps0,
            "assumed_three_year_eps_growth": wec_eps_growth,
            "issuer_2026_quarterly_dividend": wec_dividend / 4,
            "assumed_flat_annual_dividend": wec_dividend,
            "gross_cashflow_irr_flat_fy2026_pe": wec_cashflow_irr(wec_price / wec_eps0),
            "gross_cashflow_irr_exit_15x": wec_cashflow_irr(15),
            "gross_cashflow_irr_exit_13x": wec_cashflow_irr(13),
            "issuer_dividend_source": "https://investor.wecenergygroup.com/investors/news-releases/press-release-details/2026/WEC-Energy-Group-declares-quarterly-dividend-7ab72a82c/default.aspx",
            "issuer_guidance_source": "https://investor.wecenergygroup.com/investors/news-releases/press-release-details/2026/WEC-Energy-Group-posts-2025-results/default.aspx",
        },
        "historical_replays": replay,
        "shadow_15_index_10_v011_direct_75_reserve": {
            "direct_weights_total_portfolio": direct_10,
            "largest_direct_name_total_portfolio": max(direct_10.values()),
            "direct_sector_weights_total_portfolio": {k: 0.10 * v for k, v in sector_weights.items()},
            "largest_direct_sector_total_portfolio": 0.10 * max(sector_weights.values()),
            "status": "historical replay/feasibility diagnostic only, not an endorsed replacement or trade plan",
        },
        "limitations": [
            "Current holdings applied to old crises create look-ahead/survivorship risk.",
            "The 2007-09 replay has no GDDY or VEEV prices for 6.2% of sleeve; mix substitutes SPY.",
            "Reserve replay assumes constant 4% annual return.",
            "V1 scenario returns mix models and vintages; analyst-route scenarios are not calibrated expected returns.",
            "No current executable quotes, tax status or actual holdings are represented by this file.",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
