"""Causal research primitives for a future, separately published investment engine.

This module deliberately reads or changes no parent research file. It repairs two
isolated methods and specifies deterministic analyst-verdict selection. A complete
factor backtest, quote refresh, and investment recommendation are outside scope.

Dependencies: pandas and numpy. For this workspace's archived Python 3.11 data,
set PYTHONPATH=C:\\Users\\user\\eqv4\\pylib.
"""
from __future__ import annotations

from datetime import datetime
import math
import re
from typing import Any, Iterable

import numpy as np
import pandas as pd


class InvalidResearchRecord(ValueError):
    """A research input lacks an auditable identity, timestamp, or lineage."""


class AmbiguousVerdictError(InvalidResearchRecord):
    """More than one approved analyst verdict remains effective."""


def causal_share_basis_repair(
    panel: pd.DataFrame,
    splits: pd.DataFrame,
    *,
    reject_future_share_dates: bool = True,
    reference_window: int = 13,
) -> pd.DataFrame:
    """Choose a share-count split basis using observations available by each row's date.

    The historical code used a *centered* 13-row median and backward filling to
    choose between an as-reported share count and a count multiplied by corporate
    splits between the filing's share date and the formation date. Here the
    reference is a trailing 13-row median plus forward fill within entity. A
    dated share count later than the formation date is invalidated by default.

    `split_factor_after` converts all row counts into the archived common basis.
    It is a retrospective unit conversion, not a return signal. A full historical
    rebuild must also verify that truncating future raw corporate-action records
    leaves earlier *investment decisions* unchanged.

    Returns one row per input row, in original order, with explicit reasons.
    Missing causal references do not silently trigger a split adjustment.
    """
    required = {"month_end", "entity", "series", "shares_out", "shares_out_date", "split_factor_after"}
    split_required = {"date", "ticker", "split_ratio"}
    if required - set(panel.columns):
        raise InvalidResearchRecord(f"missing panel columns: {sorted(required - set(panel.columns))}")
    if split_required - set(splits.columns):
        raise InvalidResearchRecord(f"missing split columns: {sorted(split_required - set(splits.columns))}")
    if reference_window < 1:
        raise InvalidResearchRecord("reference_window must be positive")
    p = panel.copy().reset_index(drop=False).rename(columns={"index": "_source_index"})
    p["month_end"] = pd.to_datetime(p["month_end"])
    p["shares_out_date"] = pd.to_datetime(p["shares_out_date"])
    p = p.sort_values(["entity", "month_end"], kind="stable").reset_index(drop=True)
    if p.duplicated(["entity", "month_end"]).any():
        raise InvalidResearchRecord("duplicate entity/month_end records")
    s = splits.copy()
    s["date"] = pd.to_datetime(s["date"])
    if (s["split_ratio"].dropna() <= 0).any():
        raise InvalidResearchRecord("split ratios must be positive")
    split_groups = {ticker: g.sort_values("date") for ticker, g in s.groupby("ticker")}

    future_share_date = p.shares_out.notna() & (p.shares_out_date > p.month_end)
    usable_shares = p.shares_out.where(~future_share_date) if reject_future_share_dates else p.shares_out.copy()
    n = len(p)
    between_ratio = np.ones(n, dtype=float)
    ambiguous = np.zeros(n, dtype=bool)
    for row, (ticker, share_date, asof, shares) in enumerate(
        zip(p.series, p.shares_out_date, p.month_end, usable_shares)
    ):
        if pd.isna(ticker) or pd.isna(share_date) or pd.isna(shares) or ticker not in split_groups:
            continue
        g = split_groups[ticker]
        matches = g[(g.date > share_date) & (g.date <= asof)]
        if not matches.empty:
            ambiguous[row] = True
            between_ratio[row] = float(matches.split_ratio.prod())

    as_reported = usable_shares * p.split_factor_after
    rescaled = usable_shares * between_ratio * p.split_factor_after
    clean_reference = as_reported.where(~ambiguous)
    # A trailing window and within-entity forward fill only: no centered
    # window, bfill, or post-formation observation enters the reference.
    reference = clean_reference.groupby(p.entity).transform(
        lambda x: x.rolling(reference_window, min_periods=1).median()
    )
    reference = reference.groupby(p.entity).ffill()
    choose_split = ambiguous & reference.notna() & (
        np.log(rescaled / reference).abs() < np.log(as_reported / reference).abs()
    )
    chosen = usable_shares * np.where(choose_split, between_ratio, 1.0)
    reason = np.select(
        [future_share_date & reject_future_share_dates,
         ambiguous & reference.isna(), choose_split, ambiguous],
        ["future_share_date_rejected", "missing_causal_reference_no_adjustment",
         "split_basis_rescaled", "split_basis_as_reported"],
        default="no_between_date_split",
    )
    out = pd.DataFrame({
        "source_index": p._source_index,
        "month_end": p.month_end,
        "entity": p.entity,
        "series": p.series,
        "future_share_date": future_share_date,
        "split_ambiguous": ambiguous,
        "between_date_split_ratio": between_ratio,
        "causal_reference": reference,
        "split_adjustment_applied": choose_split,
        "chosen_share_count": chosen,
        "reason": reason,
    })
    return out.sort_values("source_index", kind="stable").reset_index(drop=True)


def scaled_identity_shrinkage_v2(returns: np.ndarray) -> tuple[np.ndarray, float]:
    """Correct the archived scaled-identity covariance-shrinkage scaling.

    Uses mean(||x_t x_t' - S||_F^2) / T as the estimated variance of sample
    covariance S, rather than the archived per-observation value without /T.
    This is a bounded linear shrinkage diagnostic; it is not by itself an
    independent certification against a reference Ledoit-Wolf implementation.
    """
    x = np.asarray(returns, dtype=float)
    if x.ndim != 2 or x.shape[0] < 2 or x.shape[1] < 1 or not np.isfinite(x).all():
        raise InvalidResearchRecord("returns must be finite T x N with T>=2 and N>=1")
    x = x - x.mean(axis=0, keepdims=True)
    t, n = x.shape
    sample = (x.T @ x) / t
    mu = float(np.trace(sample) / n)
    target = mu * np.eye(n)
    distance_sq = float(np.sum((sample - target) ** 2))
    if distance_sq <= 0:
        intensity = 0.0
    else:
        fourth = float(np.mean(np.sum(x * x, axis=1) ** 2))
        per_observation_error = max(0.0, fourth - float(np.sum(sample * sample)))
        intensity = float(np.clip(per_observation_error / t / distance_sq, 0, 1))
    covariance = intensity * target + (1 - intensity) * sample
    covariance = (covariance + covariance.T) / 2
    return covariance, intensity


def _utc_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise InvalidResearchRecord(f"{field} must be ISO timestamp with timezone")
    try:
        out = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidResearchRecord(f"{field} invalid ISO timestamp") from exc
    if out.tzinfo is None or out.utcoffset() is None:
        raise InvalidResearchRecord(f"{field} must include timezone")
    return out


def effective_verdict(
    records: Iterable[dict[str, Any]], ticker: str, asof_utc: str
) -> dict[str, Any]:
    """Select one approved verdict through explicit supersession, never file mtime.

    Required fields per same-ticker record: analysis_id, ticker, revision (int),
    verdict, status, approved_at_utc, market_cutoff_utc, filing_cutoff_utc,
    source_sha256, supersedes_id (string or null). All approved records that are
    effective by `asof_utc` must form one chain. Parallel approved branches fail.
    Drafts never override an earlier approved view.
    """
    cutoff = _utc_time(asof_utc, "asof_utc")
    required = {"analysis_id", "ticker", "revision", "verdict", "status", "approved_at_utc",
                "market_cutoff_utc", "filing_cutoff_utc", "source_sha256", "supersedes_id"}
    relevant = [dict(r) for r in records if str(r.get("ticker", "")).upper() == ticker.upper()]
    if not relevant:
        raise InvalidResearchRecord(f"no records for {ticker}")
    all_by_id = {}
    for r in relevant:
        if required - set(r):
            raise InvalidResearchRecord(f"missing verdict metadata: {sorted(required - set(r))}")
        rid = r["analysis_id"]
        if not isinstance(rid, str) or not rid or rid in all_by_id:
            raise InvalidResearchRecord("analysis_id must be unique nonempty string")
        all_by_id[rid] = r
        if not isinstance(r["revision"], int) or isinstance(r["revision"], bool) or r["revision"] < 1:
            raise InvalidResearchRecord(f"{rid}: revision must be positive integer")
        if not isinstance(r["source_sha256"], str) or not re.fullmatch(r"[0-9a-fA-F]{64}", r["source_sha256"]):
            raise InvalidResearchRecord(f"{rid}: source_sha256 must be SHA-256 hex")
        approved = _utc_time(r["approved_at_utc"], "approved_at_utc")
        market = _utc_time(r["market_cutoff_utc"], "market_cutoff_utc")
        filing = _utc_time(r["filing_cutoff_utc"], "filing_cutoff_utc")
        if market > approved or filing > approved:
            raise InvalidResearchRecord(f"{rid}: input cutoff after approval")
        if r["status"] not in {"APPROVED", "DRAFT", "REJECTED"}:
            raise InvalidResearchRecord(f"{rid}: unknown status")
    for rid, r in all_by_id.items():
        parent_id = r["supersedes_id"]
        if parent_id is not None:
            parent = all_by_id.get(parent_id)
            if parent is None or parent["revision"] >= r["revision"]:
                raise InvalidResearchRecord(f"{rid}: missing/invalid superseded record")
            if _utc_time(parent["approved_at_utc"], "approved_at_utc") > _utc_time(r["approved_at_utc"], "approved_at_utc"):
                raise InvalidResearchRecord(f"{rid}: approval predates superseded record")
    active = {rid: r for rid, r in all_by_id.items()
              if r["status"] == "APPROVED" and _utc_time(r["approved_at_utc"], "approved_at_utc") <= cutoff}
    if not active:
        raise InvalidResearchRecord(f"no approved verdict for {ticker} at cutoff")
    superseded = {r["supersedes_id"] for r in active.values() if r["supersedes_id"] in active}
    terminal = [r for rid, r in active.items() if rid not in superseded]
    if len(terminal) != 1:
        raise AmbiguousVerdictError(f"{ticker}: {len(terminal)} approved terminal verdicts")
    selected = terminal[0]
    # An approved successor may not skip an unapproved intermediate record.
    ancestor = selected
    seen = set()
    while ancestor["supersedes_id"] is not None:
        if ancestor["analysis_id"] in seen:
            raise InvalidResearchRecord("supersession cycle")
        seen.add(ancestor["analysis_id"])
        parent_id = ancestor["supersedes_id"]
        if parent_id not in active:
            raise InvalidResearchRecord(f"{selected['analysis_id']}: chain includes unapproved/future parent")
        ancestor = active[parent_id]
    if len(seen) + 1 != len(active):
        raise AmbiguousVerdictError(f"{ticker}: approved records form multiple chains")
    return selected
