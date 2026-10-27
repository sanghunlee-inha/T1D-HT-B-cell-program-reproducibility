
#!/usr/bin/env python3
"""
IJMS R3 - Independent Summary-Level Meta-Analysis Validation

Manuscript: ijms-4640479

Purpose:
    Independently recalculate all eight T1D pathway meta-analysis
    results from the retained 24 cohort-level effect estimates.

Scope:
    - DerSimonian-Laird random-effects meta-analysis
    - 95% confidence intervals
    - Two-sided P values
    - Between-cohort heterogeneity (I2)
    - Benjamini-Hochberg FDR correction
    - Comparison with the archived summary-level results

Limitations:
    This script does NOT reconstruct the original cohort effects
    from raw expression matrices.

    It does NOT validate the frozen 14-gene HT regression,
    single-cell analyses, spatial analyses, H&E models,
    or Figure 5 sensitivity analyses.

Dependencies:
    Python standard library only.

Expected location:
    repository/scripts/98_validate_summary_level.py
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path


# ============================================================
# 1. Repository paths
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

SOURCE = (
    ROOT
    / "data"
    / "derived"
    / "t1d_pathway_cohort_effects.tsv"
)

REFERENCE = (
    ROOT
    / "results"
    / "SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv"
)


# ============================================================
# 2. Expected datasets
# ============================================================

EXPECTED_PATHWAYS = {
    "B_CELL",
    "CYTOKINE_INFLAMMATION",
    "HLA_I",
    "HLA_II_APC",
    "IFN_I",
    "IFN_II",
    "JAK_STAT",
    "T_CELL",
}

EXPECTED_COHORTS = {
    "GSE30210",
    "GSE9006",
    "GSE156035",
}

CHECK_FIELDS = (
    "meta_hedges_g",
    "meta_ci_low",
    "meta_ci_high",
    "meta_p",
    "I2_percent",
    "tau2_DL",
    "meta_q_BH",
)

REL_TOL = 1e-9
ABS_TOL = 1e-9


# ============================================================
# 3. Read TSV files
# ============================================================

def read_tsv(path: Path) -> list[dict[str, str]]:

    if not path.is_file():
        raise FileNotFoundError(
            f"Required file not found: {path}"
        )

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as fh:

        reader = csv.DictReader(
            fh,
            delimiter="\t",
        )

        return list(reader)


# ============================================================
# 4. DerSimonian-Laird meta-analysis
# ============================================================

def recalc(
    values: list[dict[str, str]],
) -> dict[str, float]:

    y = [
        float(x["hedges_g"])
        for x in values
    ]

    v = [
        float(x["var_g"])
        for x in values
    ]

    if len(y) != 3:
        raise ValueError(
            "Each pathway must contain three cohort effects."
        )

    if not all(
        math.isfinite(x)
        for x in y + v
    ):
        raise ValueError(
            "Non-finite effect or variance detected."
        )

    if any(x <= 0 for x in v):
        raise ValueError(
            "All sampling variances must be positive."
        )

    # Fixed-effect inverse-variance weights

    w = [
        1.0 / variance
        for variance in v
    ]

    fixed_mean = (
        sum(weight * effect for weight, effect in zip(w, y))
        / sum(w)
    )

    # Cochran's Q

    q = sum(
        weight * (effect - fixed_mean) ** 2
        for weight, effect in zip(w, y)
    )

    k = len(y)

    c = (
        sum(w)
        - sum(weight ** 2 for weight in w) / sum(w)
    )

    # DerSimonian-Laird tau squared

    if c > 0:
        tau2 = max(
            0.0,
            (q - (k - 1)) / c,
        )
    else:
        tau2 = 0.0

    # Random-effects weights

    wr = [
        1.0 / (variance + tau2)
        for variance in v
    ]

    pooled_effect = (
        sum(weight * effect for weight, effect in zip(wr, y))
        / sum(wr)
    )

    standard_error = math.sqrt(
        1.0 / sum(wr)
    )

    # Normal-approximation confidence interval

    ci_low = (
        pooled_effect - 1.96 * standard_error
    )

    ci_high = (
        pooled_effect + 1.96 * standard_error
    )

    z_value = pooled_effect / standard_error

    # Two-sided normal P value

    p_value = math.erfc(
        abs(z_value) / math.sqrt(2.0)
    )

    # I-squared heterogeneity

    if q > 0:
        i2 = max(
            0.0,
            (q - (k - 1)) / q,
        ) * 100.0
    else:
        i2 = 0.0

    return {
        "meta_hedges_g": pooled_effect,
        "meta_ci_low": ci_low,
        "meta_ci_high": ci_high,
        "meta_p": p_value,
        "I2_percent": i2,
        "tau2_DL": tau2,
    }


# ============================================================
# 5. Benjamini-Hochberg correction
# ============================================================

def apply_bh(
    computed: dict[str, dict[str, float]],
) -> None:

    ordered = sorted(
        EXPECTED_PATHWAYS,
        key=lambda x: computed[x]["meta_p"],
    )

    number_tests = len(ordered)

    running = 1.0

    for rank in range(
        number_tests,
        0,
        -1,
    ):

        pathway = ordered[rank - 1]

        raw_p = computed[pathway]["meta_p"]

        running = min(
            running,
            raw_p * number_tests / rank,
        )

        computed[pathway]["meta_q_BH"] = running


# ============================================================
# 6. Input validation
# ============================================================

def validate_inputs(
    rows: list[dict[str, str]],
) -> dict[str, list[dict[str, str]]]:

    groups = defaultdict(list)

    for row in rows:
        groups[row["pathway"]].append(row)

    if len(rows) != 24:
        raise ValueError(
            f"Expected 24 input rows; found {len(rows)}."
        )

    if set(groups) != EXPECTED_PATHWAYS:
        raise ValueError(
            "Unexpected or missing pathway names."
        )

    for pathway, values in groups.items():

        cohorts = {
            row["cohort"]
            for row in values
        }

        if len(values) != 3:
            raise ValueError(
                f"{pathway}: expected three cohort records."
            )

        if cohorts != EXPECTED_COHORTS:
            raise ValueError(
                f"{pathway}: unexpected cohort composition."
            )

    return dict(groups)


# ============================================================
# 7. Compare against archived results
# ============================================================

def compare_results(
    computed: dict[str, dict[str, float]],
    reference: dict[str, dict[str, str]],
) -> list[str]:

    mismatches = []

    for pathway in sorted(EXPECTED_PATHWAYS):

        print(f"\nCHECK PATHWAY: {pathway}")

        for field in CHECK_FIELDS:

            actual = computed[pathway][field]

            expected = float(
                reference[pathway][field]
            )

            passed = math.isclose(
                actual,
                expected,
                rel_tol=REL_TOL,
                abs_tol=ABS_TOL,
            )

            status = (
                "PASS" if passed else "FAIL"
            )

            print(
                f"  {field}: {status} "
                f"computed={actual:.12g} "
                f"reference={expected:.12g}"
            )

            if not passed:
                mismatches.append(
                    f"{pathway}.{field}: "
                    f"computed={actual:.12g}, "
                    f"reference={expected:.12g}"
                )

    return mismatches


# ============================================================
# 8. Main validation
# ============================================================

def main() -> int:

    print("=" * 65)
    print("IJMS R3 SUMMARY-LEVEL REPRODUCIBILITY VALIDATION")
    print("=" * 65)

    print(f"Repository: {ROOT}")
    print(f"Input: {SOURCE}")
    print(f"Reference: {REFERENCE}")

    # Load source inputs

    rows = read_tsv(SOURCE)

    groups = validate_inputs(rows)

    # Load archived reference results

    reference_rows = read_tsv(REFERENCE)

    reference = {
        row["pathway"]: row
        for row in reference_rows
    }

    if (
        len(reference_rows) != 8
        or set(reference) != EXPECTED_PATHWAYS
    ):
        raise ValueError(
            "Reference table must contain "
            "eight unique pathway results."
        )

    # Independently recompute pathway statistics

    computed = {}

    for pathway, values in groups.items():

        computed[pathway] = recalc(values)

    # Recalculate multiple-testing correction

    apply_bh(computed)

    # Compare all numeric results

    mismatches = compare_results(
        computed,
        reference,
    )

    print("\n" + "=" * 65)

    if mismatches:

        print("VALIDATION STATUS: FAIL")

        for item in mismatches:
            print(f"  {item}")

        return 1

    print("VALIDATION STATUS: PASS")
    print("All eight summary-level pathways agree.")
    print("")

    # Important scientific boundaries

    print("REPRODUCIBILITY LEVEL:")
    print("  SUMMARY-LEVEL DERIVED-DATA CONSISTENCY")
    print("")

    print("NOT VALIDATED:")
    print("  - Raw cohort expression preprocessing")
    print("  - Original cohort-effect estimation")
    print("  - Frozen 14-gene signature derivation")
    print("  - HT bulk regression")
    print("  - Spatial transcriptomics")
    print("  - Single-cell transcriptomics")
    print("  - H&E modeling")
    print("  - Figure 5 sensitivity analyses")

    print("=" * 65)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
