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

Historical 15-gene results with unresolved analytical provenance must not be presented as independently reproduced confirmatory findings.

### Required manuscript action

For every retained quantitative analysis without sufficient reproducibility evidence, the authors must either provide the complete documented and verifiable analytical workflow or remove the affected analyses and corresponding claims.

This requirement applies consistently to the Abstract, Results, Figures, Figure Legends, Discussion, Conclusions, Methods, and Supplementary Materials.

Describing an unsupported analysis as exploratory does not by itself resolve the reproducibility concern.

**Current status: PARTIALLY ADDRESSED — FURTHER EVIDENCE OR MANUSCRIPT REMOVAL REQUIRED.**

## 3. Reviewer Comment 2 — Code and Data Availability

**Reviewer concern:** Conflicting statements regarding GitHub, Zenodo, supporting analytical materials, and reproducibility must be reconciled.

### GitHub repository

https://github.com/sanghunlee-inha/T1D-HT-B-cell-program-reproducibility

The repository contains retained cohort-level pathway-effect estimates, executable summary-level meta-analysis scripts, validation tools, and documentation of computational limitations.

The repository does not establish complete end-to-end reproducibility of all manuscript figures.

### Zenodo archive

The separate historical software deposit is available at:

https://doi.org/10.5281/zenodo.23164148

This version 1 software record provides additional downstream analysis scripts.

The availability of these scripts does not establish that every analysis has been successfully reconstructed from its original input data.

The previously referenced DOI `10.5281/zenodo.23502426` requires confirmation of public accessibility, archived contents, and correspondence with the GitHub release before it can be cited as a verified reproducibility snapshot.

The historical GitHub release `v0.1.1` is not automatically equivalent to subsequent changes made to the default branch.

### Manuscript alignment

Section 4.12, Code Availability, and the Data Availability Statement must describe the same verified analytical resources.

Any statement that all analytical results or figures are independently reproducible must be avoided unless supported by successful execution records.

A public repository, code availability, and independent end-to-end reproduction are distinct levels of evidence.

**Current status: DOCUMENTATION CLARIFIED — ARCHIVE AND MANUSCRIPT CONSISTENCY REQUIRE FINAL VERIFICATION.**

## 4. Reviewer Comment 3 — Interpretation and Reporting

**Reviewer concern:** The main findings must adequately reflect substantial attenuation following B-cell marker adjustment and the absence of demonstrated superiority of T1D-derived weights.

### Marker-adjusted HT association

The manuscript reports that simultaneous adjustment for B-cell and plasma-cell marker proxies attenuated the HT-associated coefficient by approximately 90%.

The confidence interval for the fully adjusted coefficient included zero.

This finding indicates that the original association is substantially related to B-lineage-associated transcriptional variation.

However, expression-derived marker proxies cannot distinguish differences in cellular abundance from differences in cell-intrinsic transcriptional state.

The adjustment does not establish causal mediation.

### Signature-weight sensitivity

The reported residual partial R² values include:

| Signature | Residual partial R² |
|---|---:|
| Original frozen 14-gene signature | 0.0187 |
| Equal-weight 14-gene signature | 0.0111 |
| Travaglini lung B-cell reference | 0.037 |
| Aizarani liver B-cell reference | 0.003 |

These exploratory numerical comparisons do not establish statistically significant superiority of the T1D-derived weights.

The external reference comparisons also do not establish clinical prediction accuracy or disease specificity.

### Required scientific interpretation

The principal findings should be interpreted as an observed cross-tissue B-lineage-associated transcriptional relationship, subject to the limitations of bulk-tissue composition and incomplete independent analytical validation.

The evidence does not establish:

- A shared disease-specific, cell-intrinsic B-cell program.
- Systemic activation of the transferred signature in HT peripheral blood.
- Preferential spatial localization of the frozen signature.
- Statistically demonstrated superiority of T1D-derived signature weights.
- Clinical diagnostic or therapeutic utility.

These limitations must be stated consistently wherever the corresponding findings are retained.

**Current status: INTERPRETATION REVISED — NUMERICAL REPRODUCIBILITY STILL REQUIRES VERIFICATION.**

## 5. Manuscript-to-GitHub Evidence Matrix

| Manuscript component | Supporting GitHub resource | Evidence level |
|---|---|---|
| Figure 1 | README and dataset documentation | Descriptive |
| Figure 2A–B | Retained pathway-effect table and meta-analysis validation scripts | Summary-level verified |
| Figure 3A–H | Figure-level reproducibility audit | Not independently reproduced |
| Figure 4A | Reported 14-gene bulk-association details | Not independently reproduced |
| Figure 4B | Reported spatial statistics and limitations | Not independently reproduced |
| Figure 4C–E | Dataset descriptions and limitations | Descriptive; not reproduced here |
| Figure 5A–B | Reported marker-adjustment results | Not independently reproduced |
| Figure 5C–D | Reported signature-weight benchmarks | Not independently reproduced |
| Code Availability | README and reproducibility documentation | Partially verified |
| Data Availability | Dataset accession documentation | Source identifiers documented |

The corresponding detailed figure audit is provided in:

`docs/FIGURE_REPRODUCIBILITY_MATRIX.md`

Additional open dependencies are documented in:

`docs/REPRODUCIBILITY_STATUS.md`

## 6. Required Final Verification Before Submission

Before resubmission, the authors should complete the following checks:

1. Confirm that all manuscript statements correspond to the actual deposited resources.
2. Verify the signed 14-gene weights and analytical preprocessing procedures.
3. Supply sufficient source-to-result evidence for every retained quantitative analysis or remove unsupported results.
4. Reconcile figure legends, Methods, Supplementary Methods, Results, Discussion, and Conclusions after any analysis removal.
5. Confirm the public accessibility and exact contents of all cited Zenodo records.
6. Verify that the final GitHub commit, release, and archived snapshot correspond to the version cited in the manuscript.
7. Record the completed verification process without treating missing evidence as a successful reproducibility test.

## 7. Final Assessment

The public GitHub repository supports reproducibility of the T1D pathway meta-analysis from retained summary-level inputs.

Complete end-to-end reconstruction of the remaining analyses has not been established from the files currently available in this repository.

The reported attenuation following marker-proxy adjustment and the absence of demonstrated superiority of the transferred signature weights appropriately constrain the scientific interpretation, but their computational reproducibility remains a separate outstanding issue.

**Overall R3 status: PARTIALLY ADDRESSED.**

**Figure 2 summary-level validation: VERIFIED.**

**Figures 3–5 end-to-end reproducibility: NOT YET VERIFIED.**

**Final manuscript and archive reconciliation: REQUIRED BEFORE RESUBMISSION.**

This document provides an explicit evidence map for the third-round revision. It must not be interpreted as proof that all outstanding reviewer concerns have been resolved.
