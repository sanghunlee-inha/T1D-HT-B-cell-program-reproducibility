# IJMS Third Revision — Reviewer Comments and Manuscript–GitHub Alignment

**Manuscript ID:** ijms-4640479  
**Revision:** Third-round revision (R3)  
**Audit date:** 2026-10-28

**Title:** Cross-Tissue Concordance of a T1D Blood-Derived B-Cell Signature with Hashimoto Thyroiditis Tissue: Exploratory Spatial Immune-Topic Analysis

## 1. Purpose

This document aligns the third-round reviewer comments with the revised manuscript, GitHub repository, available analytical materials, and outstanding reproducibility requirements.

The objective is to distinguish independently recalculated results from manuscript-reported analyses that cannot yet be reconstructed from the deposited materials.

This document does not certify complete reproducibility of the manuscript.

## 2. Reviewer Comment 1 — Reproducibility

**Reviewer concern:** Several analyses previously acknowledged as incompletely reproducible remain in the manuscript. The authors must either remove the analyses and associated claims or provide sufficient methodological documentation and verifiable analytical workflows.

### Evidence currently supported

The GitHub repository provides the retained 24-row cohort-level pathway-effect table and scripts for reproducing the summary-level T1D meta-analysis.

The available analytical files are:

- `data/derived/t1d_pathway_cohort_effects.tsv`
- `scripts/01_t1d_random_effects_meta.py`
- `scripts/99_audit_summary.py`
- `scripts/98_validate_summary_level.py`
- `results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv`

The independent summary-level recalculation checks eight immune pathways using DerSimonian–Laird random-effects pooling and Benjamini–Hochberg correction.

All eight pathway results agreed with the retained summary-level output table in the reported local validation.

**Reproducibility status: SUMMARY-LEVEL VERIFIED.**

This validation does not independently reconstruct the original cohort-level effects from raw transcriptomic data.

### Analyses requiring additional verification

**Figure 3 — RNA-first spatial topic analysis**

Complete topic-fitting configurations, model-selection criteria, source-to-topic matrices, external mapping procedures, and H&E model outputs are not fully available.

The existing documentation does not establish independent reproduction of these analyses.

**Figure 4A — Frozen 14-gene signature**

The reported HT association is β = 2.653394 (95% CI 2.367850–2.938938), with reported empirical P values of approximately 2 × 10^-5.

The complete verified signed weights, original standardization implementation, analysis-ready expression and covariate data, and null-sampling dependencies are not all available in the GitHub repository.

These values remain manuscript-reported results rather than independently reproduced outputs of this repository.

**Figure 4B — Spatial signature assessment**

The reported five-slide comparison yielded Δ = 0.459, exact permutation P = 0.10, and matched-gene P = 0.085.

The complete spatial scoring matrices and matched-gene null inputs are not available for independent reconstruction.

These results do not demonstrate preferential spatial localization.

**Figure 4C–E — Single-cell and HT pathway analyses**

Complete processed analytical objects and source-to-library provenance are not provided.

The GSE192580 dataset contains three HT and three ICI-associated thyroiditis libraries, without healthy thyroid controls.

The available evidence supports descriptive interpretation rather than independent confirmation of the transferred signature.

**Figure 5A–D — Marker adjustment and weighting sensitivity**

The manuscript reports substantial attenuation following B-cell/plasma-cell marker adjustment and exploratory comparisons of alternative weighting strategies.

Complete regression inputs, bootstrap settings, random-weight specifications, reference-gene coverage, and independently verified outputs are not currently included in this repository.

### Historical 15-gene analysis

The historical unweighted 15-gene score is distinct from the frozen 14-gene signature.

Both scores were evaluated in the same HRA001684 cohort and therefore do not constitute independent patient-cohort validation.

Historical 15-gene results with
