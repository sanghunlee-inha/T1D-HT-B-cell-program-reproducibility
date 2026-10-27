
# Reproducibility Audit — IJMS Third Revision

**Manuscript ID:** ijms-4640479  
**Audit date:** 2026-10-28

**Manuscript title:** Cross-Tissue Concordance of a T1D Blood-Derived B-Cell Signature with Hashimoto Thyroiditis Tissue: Exploratory Spatial Immune-Topic Analysis

## 1. Purpose and Scope

This document provides a figure-by-figure assessment of the computational reproducibility of the analyses reported in the revised manuscript.

The audit distinguishes analyses that can be recalculated from publicly deposited summary-level inputs from those for which complete source-to-result reconstruction remains unavailable.

The presence of analytical scripts, reported numerical results, or previously deposited software does not, by itself, establish independent end-to-end reproducibility.

Three evidence categories are used:

- **SUMMARY-LEVEL VERIFIED:** The reported numerical results can be recalculated from the retained summary-level inputs and compared against archived outputs.
- **REPORTED BUT NOT INDEPENDENTLY REPRODUCED:** Numerical findings are reported in the manuscript, but the currently available repository does not contain all verified inputs and dependencies necessary for independent reconstruction.
- **DESCRIPTIVE ONLY:** Analyses provide biological or methodological context without establishing independent validation of the transferred signature.

These categories describe the evidence currently available in this GitHub repository. They do not establish whether historical analyses were correctly or incorrectly performed.

## 2. Summary-Level Meta-Analysis: Figure 2

The retained input table contains 24 cohort-level pathway-effect records, representing eight immune pathways across three T1D peripheral-blood cohorts:

- GSE30210
- GSE9006
- GSE156035

The analysis uses DerSimonian–Laird random-effects meta-analysis followed by Benjamini–Hochberg false-discovery-rate correction.

### Available files

- `data/derived/t1d_pathway_cohort_effects.tsv`
- `scripts/01_t1d_random_effects_meta.py`
- `scripts/99_audit_summary.py`
- `scripts/98_validate_summary_level.py`
- `results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv`

The independent standard-library implementation recalculates pooled effect sizes, confidence intervals, P values, heterogeneity statistics, and FDR-adjusted q values.

In the reported local validation, all eight recalculated pathway results agreed with the retained summary-level output table.

### Verified numerical anchor

**B-cell-associated pathway**

- Pooled Hedges' g = 0.514716
- 95% CI = 0.177885–0.851547
- BH-adjusted q = 0.021948
- I² = 0%

**Reproducibility status: SUMMARY-LEVEL VERIFIED**

This verification establishes numerical agreement using retained cohort-level effect estimates.

It does not independently verify:

- Original expression-data preprocessing
- Platform-specific normalization
- Participant and visit selection
- Original cohort-level effect estimation
- Pathway-score construction from raw expression matrices

Accordingly, Figure 2 should be described as reproducible from retained summary-level analytical inputs, not as a fully reconstructed raw-data analysis.

## 3. Figure-by-Figure Reproducibility Assessment

| Figure | Analysis | Current status | Principal limitation |
|---|---|---|---|
| Figure 1 | Study design and dataset relationships | DESCRIPTIVE ONLY | Conceptual figure; does not represent independent biological validation |
| Figure 2A–B | T1D blood pathway meta-analysis | SUMMARY-LEVEL VERIFIED | Original cohort effects are not reconstructed from expression matrices |
| Figure 3A–C | RNA-first thyroid topic inference and annotation | NOT INDEPENDENTLY REPRODUCED | Complete topic fitting and selection dependencies are unavailable |
| Figure 3D–F | Spatial topic mapping and external descriptive sections | NOT INDEPENDENTLY REPRODUCED | Topic mapping and source-to-score provenance remain incomplete |
| Figure 3G–H | H&E-associated model comparisons | NOT INDEPENDENTLY REPRODUCED | Model selection, held-out predictions, and complete computational records are unavailable |
| Figure 4A | Frozen 14-gene HT bulk association | NOT INDEPENDENTLY REPRODUCED | Verified weights, normalization implementation, expression inputs, and null-model dependencies are incomplete |
| Figure 4B | Five-slide frozen-signature spatial analysis | NOT INDEPENDENTLY REPRODUCED | Complete spatial score matrices and null-sampling inputs are unavailable |
| Figure 4C–D | Thyroiditis single-cell characterization | DESCRIPTIVE; NOT REPRODUCED HERE | Processed single-cell objects and complete library-level provenance are unavailable |
| Figure 4E | HT bulk immune-pathway associations | NOT INDEPENDENTLY REPRODUCED | Complete sample-level model inputs and reconstruction workflow are unavailable |
| Figure 5A–B | B-cell/plasma-cell marker adjustment | NOT INDEPENDENTLY REPRODUCED | Analysis-ready covariates, proxy scores, and bootstrap evidence are incomplete |
| Figure 5C–D | Signature-weight and external-reference benchmarking | NOT INDEPENDENTLY REPRODUCED | Random-weight settings, model specifications, and reference-score provenance are incomplete |

The current evidence does not support a claim that Figures 3–5 have been independently reproduced end to end.

## 4. Frozen 14-Gene Signature and Historical 15-Gene Analysis

The frozen signature consists of 14 genes retained from a 17-gene candidate panel based on gene availability across the three T1D discovery cohorts.

The manuscript describes inverse-variance pooling of gene-level effect estimates and L1 normalization of the resulting signed weights.

The frozen signature was subsequently evaluated in HRA001684, comprising:

- 16 HT thyroid samples
- 50 non-HT thyroid samples

The reported HC3-adjusted coefficient was:

- β = 2.653394
- 95% CI = 2.367850–2.938938
- Reported empirical P values approximately 2 × 10^-5

These results are manuscript-reported numerical anchors and are not independently regenerated by this repository.

The following dependencies require verification:

1. Complete, versioned 14-gene signed weights.
2. Original robust-standardization implementation.
3. Analysis-ready HRA001684 expression and covariate inputs.
4. Exact regression and permutation configurations.
5. Complete matched-gene null-generation inputs.
6. Machine-readable outputs and clean-run verification records.

The historical unweighted 15-gene score and the frozen 14-gene signature are distinct analytical quantities.

Both were evaluated using the same HRA001684 cohort.

They therefore do not constitute independent patient-cohort replications.

The historical 15-gene analysis retains unresolved upstream analytical provenance and should not be presented as independently verified evidence.

## 5. Spatial and Single-Cell Analyses

### 5.1 Direct spatial assessment

The reported GSE248205 frozen-signature comparison included:

- Three HT sections
- Two control sections
- Observed contrast Δ = 0.459
- Exact slide-label permutation P = 0.10
- Matched-gene null P = 0.085

The previously reported B/plasma-topic correspondence test yielded P = 0.90.

These findings do not establish preferential spatial localization of the frozen T1D-derived signature.

The direct spatial analysis has only ten possible HT/control label assignments.

The corresponding numerical results remain reported rather than independently reproduced from the deposited files.

### 5.2 RNA-first spatial topics

The RNA-first thyroid immune topics were inferred independently from the frozen 14-gene signature.

Topic 7 was annotated with APC/HLA-II-associated transcriptional features.

External GSE230424 sections P3 and P4 were selected for descriptive illustration because they represent HT-only tissue without concurrent carcinoma.

These sections do not constitute independent disease-effect validation of frozen-signature localization.

Complete topic-fitting configurations, source-to-topic matrices, matching procedures, and model-selection evidence remain necessary for independent reconstruction.

### 5.3 Single-cell characterization

GSE192580 includes 6,512 processed cells from:

- Three HT libraries
- Three immune-checkpoint-inhibitor-associated thyroiditis libraries

The dataset does not include healthy thyroid controls.

Single-cell marker expression is interpreted descriptively and does not independently establish a transferred B-cell signature or an HT-versus-healthy-control effect.

## 6. B-Cell Marker Adjustment and Weighting Sensitivity

### 6.1 Marker-proxy adjustment

The manuscript reports that joint adjustment for B-cell and plasma-cell expression-derived marker proxies attenuated the HT-associated signature coefficient by approximately 90%.

The confidence interval for the fully adjusted coefficient included zero.

This result is consistent with substantial dependence of the observed association on B-lineage-associated transcriptional variation.

However, marker-proxy adjustment cannot independently distinguish:

- B-cell abundance
- B-cell activation or differentiation state
- Correlated tissue transcriptional variation

The reported attenuation must not be interpreted as a measured change in B-cell fractions or as a causal mediation effect.

The complete model M0–M5 inputs, bootstrap settings, and independently verified outputs are not currently provided in this GitHub repository.

### 6.2 Signature-weight benchmarking

Reported residual partial R² values include:

| Signature | Reported residual partial R² |
|---|---:|
| Original frozen 14-gene signature | 0.0187 |
| Equal-weight 14-gene signature | 0.0111 |
| Travaglini lung B-cell reference | 0.037 |
| Aizarani liver B-cell reference | 0.003 |

These comparisons are exploratory.

The observed numerical differences do not establish statistically significant superiority of the T1D-derived weights.

The reference-signature comparisons do not constitute independent clinical predictive-performance validation.

Complete random-weight simulation settings, covariate specifications, gene coverage, and reference-score calculations remain necessary for independent reproduction.

## 7. GitHub and Zenodo Availability

**Manuscript-specific GitHub repository:**

https://github.com/sanghunlee-inha/T1D-HT-B-cell-program-reproducibility

The repository contains retained cohort-level effect estimates, summary-level analysis code, numerical auditing tools, and documentation of reproducibility limitations.

**Related Zenodo software deposit:**

https://doi.org/10.5281/zenodo.23164148

The separate Zenodo v1 software deposit provides additional historical downstream scripts.

The existence of these scripts does not establish that all source-to-result analytical workflows have been independently reproduced.

The previously referenced DOI 10.5281/zenodo.23502426 requires separate confirmation of its public accessibility and archived contents before being cited as a verified reproducibility snapshot.

A public code repository and an archived software package should not be treated as evidence of complete reproducibility without documented input verification and successful execution.

## 8. Outstanding Requirements for Full Reproducibility

For every retained quantitative analysis, the following should be documented or supplied where legally and technically permissible:

1. Exact source dataset identifiers and access conditions.
2. Verified preprocessing and normalization procedures.
3. Fixed gene definitions and signed weights.
4. Analysis-ready inputs or reproducible input-construction procedures.
5. Complete analysis scripts and software dependencies.
6. Prespecified or documented random seeds and model settings.
7. Machine-readable intermediate and final outputs.
8. Scripts linking analytical results to the manuscript figures.
9. Independent execution logs and numerical validation records.
10. Documentation of unresolved dependencies or excluded analyses.

Analyses that cannot be adequately reconstructed must not be described as independently reproduced.

Where methodological documentation and verifiable workflows remain insufficient, the affected analyses and their associated claims should be removed from the revised manuscript and corresponding supplementary materials.

Simply identifying an analysis as exploratory does not, by itself, resolve an outstanding reproducibility concern.

## 9. Alignment with Third-Round Reviewer Comments

### Comment 1 — Reproducibility

This audit identifies which analyses are supported by executable summary-level workflows and which retain unresolved computational dependencies.

Figure 2 summary-level reproducibility is distinguished explicitly from the unavailable raw-expression reconstruction.

The remaining quantitative analyses require complete analytical evidence or removal of unsupported inferential claims.

### Comment 2 — Code and Data Availability

The roles of the GitHub repository and related Zenodo software deposit are distinguished.

Public availability of scripts is not equated with successful end-to-end reproducibility.

The manuscript, supplementary materials, reviewer responses, and repository documentation must describe the same verified scope.

### Comment 3 — Interpretation and Reporting

The manuscript interpretation should emphasize the approximately 90% attenuation following B-cell/plasma-cell marker adjustment and the inclusion of zero in the fully adjusted confidence interval, provided the corresponding reported analysis is retained and adequately supported.

The available weighting comparisons do not demonstrate superiority of the T1D-derived signature weights.

The results should not be interpreted as evidence of a shared disease-specific, cell-intrinsic B-cell program or validated spatial localization.

## 10. Final Audit Conclusion

The currently available repository supports numerical reconstruction of the retained T1D pathway meta-analysis from 24 cohort-level effect estimates.

It does not establish independent end-to-end reproducibility of the frozen-signature HT association, spatial topic analyses, single-cell analyses, histopathology models, or marker-adjustment and weighting benchmarks.

The principal supported conclusion is therefore limited to summary-level computational consistency and carefully qualified reported cross-tissue associations.

**Overall reproducibility status: PARTIAL — ADDITIONAL EVIDENCE REQUIRED.**

**Publication-level reproducibility: NOT YET FULLY VERIFIED.**

This document is an audit of available evidence and outstanding dependencies. It is not a certification that all manuscript analyses have been independently reproduced.
