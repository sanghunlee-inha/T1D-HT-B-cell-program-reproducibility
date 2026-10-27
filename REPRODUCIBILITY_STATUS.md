# Reproducibility audit — IJMS third revision (2026-10-28)

## Recalculated from retained summary inputs

Figure 2: 24 existing cohort-level pathway-effect records (eight pathways × three cohorts) are inputs to DerSimonian–Laird random-effects pooling and Benjamini–Hochberg correction. `scripts/98_validate_summary_level.py` independently recalculates every row and compares against the archived result table. Eight of eight rows matched in a local test. **This does not verify extraction, expression preprocessing, participant visit selection, or original source effect estimates.**

## Not independently reproduced from this repository

1. Figure 3 RNA-first spatial topics and histopathology model comparisons: topic fitting, rank and model selection, feature matrices, cross-dataset mapping and held-out predictions are not completely included.
2. Figure 4A frozen 14-gene HT bulk: checked versioned weights, original normalization helper, sample expression/design matrix and null gene pool inputs are required to regenerate β = 2.653394 and permutation results.
3. Figure 4B: the five-slide spatial score matrix and matched-gene-null inputs are not bundled. Reported exact P = 0.10 and matched-gene P = 0.085 are not independent reproductions here.
4. Figure 4C–E: processed single-cell object, source-to-library crosswalk and complete HT pathway fit inputs are missing. The single-cell collection comprises 3 HT and 3 ICI thyroiditis libraries without healthy controls.
5. Figure 5A–B: model M0–M5 inputs, B-cell/plasma-cell proxy scoring, bootstrap design and outputs needed to verify ~90% attenuation are not fully supplied.
6. Figure 5C–D: random-weight simulation settings, model covariates, external signature gene coverage and reference-score computation are not fully supplied.
7. The historical 15-gene analysis has unresolved provenance and is not independent HT cohort validation.

## Reviewer action

**Either** release authorized inputs, methods, exact code/environment, fixed seeds, machine-readable outputs, figure scripts and clean-run evidence for each retained quantitative analysis **or** remove non-verifiable analyses and related statements throughout main text, figures and supplements. Merely labeling unsupported analyses 'exploratory' is insufficient.

No files in this update were presented as verified outputs of Figure 3–5 runs. Zenodo v1 DOI `10.5281/zenodo.23164148` is a separate historical software deposit, not proof of end-to-end validation.
