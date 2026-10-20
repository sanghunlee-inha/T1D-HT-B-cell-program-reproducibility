# Reproducibility status and open dependencies

## Executable now

The summary-level DerSimonian–Laird random-effects meta-analysis and Benjamini–Hochberg FDR correction use the retained 24-row pathway effect table. They are not a new derivation of cohort effects from participant-level expression data.

## Requires verified inputs before reproducible claim

1. The fixed signed 14-gene weights from Supplementary Table S1 and gene-standardization implementation (`common.py` historical dependency).
2. Auditable cohort-level expression processing, platform-specific normalization, GSE30210 participant/visit selection, and the original pathway-effect generation method.
3. HRA001684 processed sample-level gene expression and covariates, plus full null gene-matching inputs to regenerate β = 2.653394 and 50,000-draw P values.
4. Historical 15-gene unweighted score and null lineage; these are **not** interchangeable with the 14-gene frozen weighted result.
5. GSE192580 original source-to-processed library crosswalk and scVI state identities; no healthy control comparator exists.
6. Original spatial Stage13 topic fitting configuration, topic selection, cross-dataset matching, and complete H&E hyperparameter/model selection history.

## Scientific limits to retain

- Cross-tissue association is not evidence of the same circulating B-cell state in HT.
- GSE248205 spatial slide-level tests were nonsignificant, and independently inferred RNA-first thyroid topics are not mapped frozen signatures.
- Biological replication units are participants for blood effects, thyroid samples for bulk associations, libraries for descriptive single-cell summaries, and slides for spatial comparisons.

## Release criteria

Before Zenodo archiving: independently rerun the scripts, verify inputs and expected outputs, record software package versions and checksums, label any blocked components, and release a Git tag. Do not mark blocked components as passed based on manuscript values alone.
