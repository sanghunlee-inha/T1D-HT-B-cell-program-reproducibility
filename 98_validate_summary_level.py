#!/usr/bin/env python3
"""Independently recalculate all eight *summary-level* rows from retained effects.

No source-expression matrices, frozen-signature scores or spatial analyses are tested.
This script uses only the Python standard library so it provides a cross-implementation
check of the derived summary table, not independent raw-data validation.
"""
from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/derived/t1d_pathway_cohort_effects.tsv"
REFERENCE = ROOT / "results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv"
EXPECTED = {"B_CELL", "CYTOKINE_INFLAMMATION", "HLA_I", "HLA_II_APC", "IFN_I", "IFN_II", "JAK_STAT", "T_CELL"}
CHECK_FIELDS = ("meta_hedges_g", "meta_ci_low", "meta_ci_high", "meta_p", "I2_percent", "tau2_DL", "meta_q_BH")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def recalc(values: list[dict[str, str]]) -> dict[str, float]:
    y = [float(x["hedges_g"]) for x in values]
    v = [float(x["var_g"]) for x in values]
    if len(y) != 3 or not all(math.isfinite(a) for a in y + v) or any(a <= 0 for a in v):
        raise ValueError("Each pathway needs three finite effects and positive variances")
    w = [1.0 / a for a in v]
    fixed = sum(a * b for a, b in zip(w, y)) / sum(w)
    q = sum(a * (b - fixed) ** 2 for a, b in zip(w, y))
    c = sum(w) - sum(a * a for a in w) / sum(w)
    tau2 = max(0.0, (q - (len(y) - 1)) / c) if c > 0 else 0.0
    wr = [1.0 / (a + tau2) for a in v]
    mu = sum(a * b for a, b in zip(wr, y)) / sum(wr)
    se = math.sqrt(1.0 / sum(wr))
    return {
        "meta_hedges_g": mu,
        "meta_ci_low": mu - 1.96 * se,
        "meta_ci_high": mu + 1.96 * se,
        "meta_p": math.erfc(abs(mu / se) / math.sqrt(2.0)),
        "I2_percent": max(0.0, (q - (len(y) - 1)) / q) * 100.0 if q > 0 else 0.0,
        "tau2_DL": tau2,
    }


def main() -> int:
    rows = read_tsv(SOURCE)
    refrows = read_tsv(REFERENCE)
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row["pathway"]].append(row)
    if len(rows) != 24 or set(groups) != EXPECTED or any(len(g) != 3 or len({x["cohort"] for x in g}) != 3 for g in groups.values()):
        raise SystemExit("FAIL: expected 24 rows comprising eight pathways x three unique cohorts")
    reference = {r["pathway"]: r for r in refrows}
    if len(refrows) != 8 or set(reference) != EXPECTED:
        raise SystemExit("FAIL: expected exactly eight pathway results in reference table")
    computed = {k: recalc(v) for k, v in groups.items()}
    ordered = sorted(EXPECTED, key=lambda x: computed[x]["meta_p"])
    running = 1.0
    for rank in range(len(ordered), 0, -1):
        pathway = ordered[rank - 1]
        running = min(running, computed[pathway]["meta_p"] * len(ordered) / rank)
        computed[pathway]["meta_q_BH"] = running
    mismatches = []
    for pathway in sorted(EXPECTED):
        for field in CHECK_FIELDS:
            actual = computed[pathway][field]
            expected = float(reference[pathway][field])
            if not math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9):
                mismatches.append(f"{pathway}.{field}: computed={actual:.12g} archived={expected:.12g}")
        print(f"CHECK {pathway}: derived summary recomputation completed")
    if mismatches:
        print("FAIL: " + "; ".join(mismatches))
        return 1
    print("PASS: all 8 summary-level pathways agree with the retained output table")
    print("LIMITATION: input effects were not reconstructed from raw patient-level expression data")
    print("NOT TESTED: 14-gene HT regression, spatial, single-cell, H&E, Figure 5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
