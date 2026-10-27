# Reproducibility Status and Open Dependencies — IJMS Third Revision

**Manuscript ID:** ijms-4640479  
**Audit date:** 2026-10-28  
**Status:** PARTIAL REPRODUCIBILITY — ADDITIONAL VERIFICATION REQUIRED

## 1. Overview

This document describes the computational reproducibility status of the analyses associated with the third-round revision of IJMS manuscript ijms-4640479.

The repository distinguishes numerical reconstruction from retained summary-level inputs from complete end-to-end reproducibility using original transcriptomic datasets.

The availability of scripts, reported outputs, or archived software does not independently establish the reproducibility of all manuscript analyses.

## 2. Summary-Level Analysis: Figure 2

The DerSimonian–Laird random-effects meta-analysis and Benjamini–Hochberg FDR correction use a retained 24-row pathway-effect table representing eight pathways across three T1D peripheral-blood cohorts.

The relevant files are:

- `data/derived/t1d_pathway_cohort_effects.tsv`
- `scripts/01_t1d_random_effects_meta.py`
- `scripts/98_validate_summary_level.py`
- `scripts/99_audit_summary.py`
- `results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv`

The independent standard-library implementation recalculates all eight pathway-level estimates and compares them with the retained results.

All eight pathway estimates agreed with the retained output table in the reported local validation.

The B-cell pathway yielded Hedges' g = 0.514716 (95% CI 0.177885–0.851547), BH-adjusted q = 0.021948, and I² = 0%.

**Status: SUMMARY-LEVEL VERIFIED.**

This verification does not independently reconstruct cohort-level effect estimates from raw expression matrices.

The original pathway-level visit estimator, platform-specific normalization, expression preprocessing, participant selection, and source-to-effect estimation remain incompletely documented.

## 3. Frozen 14-Gene Signature: Figure 4A

The manuscript reports a frozen 14-gene T1D-derived signature applied to HRA001684, comprising 16 HT and 50 non-HT thyroid specimens.

The reported HC3-adjusted HT coefficient was β = 2.653394 (95% CI 2.367850–2.938938), with empirical P values of approximately 2 × 10^-5.

Independent reconstruction requires verification of:

1. The complete signed 14-gene weights from Supplementary Table S1.
2. The original gene-standardization implementation, including the historical `common.py` dependency.
3. Platform-specific normalization and sample-level expression processing.
4. Analysis-ready HRA001684 expression and covariate matrices.
5. Complete matched-gene-null sampling inputs and configurations.
6. Reproducible permutation settings and numerical outputs.

**Status: REPORTED — NOT INDEPENDENTLY REPRODUCED HERE.**

## 4. Historical 15-Gene Analysis

The historical unweighted 15-gene program and the frozen 14-gene weighted signature are distinct analytical quantities.

The original 15-gene score and associated null-analysis provenance remain incompletely documented.

Both scoring approaches used the same HRA001684 thyroid cohort and therefore do not constitute independent patient-cohort validation.

Historical results with unresolved upstream provenance must not be presented as independently reproduced confirmatory evidence.

## 5. Spatial Transcriptomic Analyses: Figures 3 and 4B

### RNA-first topic analysis

Independent reproduction requires:

- Complete source expression and spatial matrices.
- The original 12-topic fitting configuration.
- Topic-rank and component-selection criteria.
- Topic-loading and score matrices.
- Cross-dataset correspondence and matching procedures.
- Refitting stability and model-selection evidence.

The APC/HLA-II-associated Topic 7 representation was inferred independently from the frozen T1D-derived signature.

External GSE230424 P3/P4 maps represent descriptive HT-only spatial context rather than independent validation of the frozen signature.

### Direct frozen-score spatial comparison

The reported GSE248205 five-slide comparison comprised three HT and two control sections.

The reported results were:

- Observed contrast Δ = 0.459.
- Exact slide-label permutation P = 0.10.
- Matched-gene-null P = 0.085.
- B/plasma-topic correspondence P = 0.90.

These results do not establish preferential spatial localization of the frozen T1D-derived signature.

Complete slide-level or spot-level scoring matrices and matched-gene-null inputs are not currently deposited in this GitHub repository.

**Status: REPORTED — NOT INDEPENDENTLY REPRODUCED HERE.**

## 6. Single-Cell Analysis: Figure 4C–D

GSE192580 contains three HT and three immune-checkpoint-inhibitor-associated thyroiditis libraries, representing 6,512 processed cells.

The dataset does not contain healthy thyroid controls.

The original source-to-processed library crosswalk, complete processed objects, and historical cell-state modeling dependencies require further verification.

Single-cell observations are interpreted descriptively and do not constitute independent confirmation of the frozen transferred signature.

**Status: DESCRIPTIVE — COMPLETE REPRODUCTION NOT ESTABLISHED.**

## 7. H&E-Associated Modeling: Figure 3G–H

The historical H&E-associated models compared tissue-morphology-informed and non-image approaches for predicting RNA-first topic scores.

Independent reproduction requires:

- Original image-feature extraction procedures.
- Model architectures and software environments.
- Training and validation splits.
- Hyperparameter and model-selection history.
- Held-out predictions and corresponding target values.
- Complete quantitative model-comparison outputs.

Reported performance differences must not be interpreted as independently validated improvements or evidence of frozen-signature localization.

**Status: REPORTED — NOT INDEPENDENTLY REPRODUCED HERE.**

## 8. Marker-Proxy Adjustment: Figure 5A–B

The manuscript reports approximately 90% attenuation of the HT coefficient after joint B-cell and plasma-cell marker-proxy adjustment.

The fully adjusted confidence interval included zero.

The following evidence remains necessary for independent reproduction:

1. Complete HRA001684 analysis-ready model inputs.
2. Exact B-cell and plasma-cell proxy-scoring procedures.
3. Model specifications and covariate design matrices for M0–M5.
4. Regression coefficients and robust confidence intervals.
5. Bootstrap resampling configuration, seeds, and outputs.

Marker-proxy adjustment does not directly measure immune-cell abundance and cannot establish causal mediation.

**Status: REPORTED — NOT INDEPENDENTLY REPRODUCED HERE.**

## 9. Signature-Weight Sensitivity: Figure 5C–D

The manuscript reports the following residual partial R² values:

| Signature | Reported residual partial R² |
|---|---:|
| Original frozen 14-gene signature | 0.0187 |
| Equal-weight 14-gene signature | 0.0111 |
| Travaglini lung B-cell reference | 0.037 |
| Aizarani liver B-cell reference | 0.003 |

Independent reproduction requires complete random-weight sampling specifications, random seeds, reference-signature gene coverage, covariate definitions, residualization procedures, and associated output records.

The observed numerical differences do not establish statistically significant superiority of the T1D-derived weights.

These comparisons are not independent clinical predictive-performance evaluations.

**Status: REPORTED — NOT INDEPENDENTLY REPRODUCED HERE.**

## 10. Scientific Interpretation Boundaries

The current findings must not be interpreted as demonstrating:

- A shared circulating B-cell state in T1D and HT.
- Systemic activation of the frozen signature in HT peripheral blood.
- Independent patient-cohort replication from the two HRA001684 scoring methods.
- Preferential spatial localization of the frozen signature.
- A shared disease-specific, cell-intrinsic B-cell program.
- Causal mediation by B-cell abundance.
- Statistically demonstrated superiority of the T1D-derived weights.
- Established clinical diagnostic or therapeutic utility.

The biological replication units differ across analyses: participants for blood-derived cohort effects, thyroid specimens for bulk associations, libraries for descriptive single-cell analyses, and tissue sections for spatial disease comparisons.

## 11. Code and Data Availability

**GitHub:**

https://github.com/sanghunlee-inha/T1D-HT-B-cell-program-reproducibility

**Historical Zenodo software deposit:**

https://doi.org/10.5281/zenodo.23164148

The historical Zenodo v1 deposit includes additional downstream analytical scripts but does not establish complete end-to-end reproduction.

A new Zenodo v2 record is being prepared for the third-round reproducibility documentation update. Its DOI must not be described as published until final registration is completed.

The roles of source datasets, derived analytical inputs, software availability, and independent result verification must remain distinct.

## 12. Requirements Before Full Reproducibility Can Be Claimed

For each retained quantitative analysis, the authors should provide or verify:

1. Source datasets and applicable access permissions.
2. Preprocessing and normalization procedures.
3. Original analytical inputs and versioned signature weights.
4. Complete code, dependencies, and environment specifications.
5. Random seeds and computational configurations.
6. Intermediate analytical objects and final results.
7. Figure-generation procedures.
8. Numerical consistency checks.
9. Clean-environment execution logs.
10. File provenance and checksums.

Analyses that cannot be adequately documented and independently reconstructed must either be supported by additional verifiable evidence or removed, together with their associated inferential claims, from the manuscript and supplementary materials.

Simply labeling an unsupported analysis as exploratory is insufficient to resolve the reproducibility concern.

## 13. Final Audit Assessment

The public repository supports numerical reconstruction of the retained T1D pathway meta-analysis using 24 cohort-level effect estimates.

Complete end-to-end reconstruction of the frozen 14-gene HT association, RNA-first spatial topics, histopathology-associated models, single-cell analyses, and marker-adjustment and weighting benchmarks has not been established from the currently deposited GitHub materials.

**Figure 2 summary-level validation: VERIFIED.**

**Figures 3–5 end-to-end reproducibility: NOT YET VERIFIED.**

**Overall reproducibility status: PARTIAL — ADDITIONAL ANALYTICAL EVIDENCE REQUIRED.**

This document is an audit of available evidence and outstanding dependencies, not a certification of complete manuscript reproducibility.
