# Reviewer comments ↔ GitHub evidence — IJMS ijms-4640479 R3

## 1. Reproducibility

Supported: summary-level Figure 2 effects computed from a retained 24-row file, and cross-checked independently by `scripts/98_validate_summary_level.py`. Unsupported by this GitHub package: original expression-to-effect calculations and quantitative analyses in Figures 3–5. Retained unsupported inferential results need a verifiable workflow or deletion across Results, captions, Discussion, Abstract and Supplementary Materials. Historical 15-gene numbers must not be treated as independent 14-gene validation.

## 2. Code/data availability

The README reports exactly what the default branch includes. `https://doi.org/10.5281/zenodo.23164148` refers to a **separate v1 software deposit**. The distinct DOI `10.5281/zenodo.23502426` must be verified before asserting that it is accessible. Existing GitHub tag `v0.1.1` does not include these proposed R3 changes unless a new release is published. Any manuscript Code Availability and Data Availability statements must be synchronized to published and verified contents.

## 3. Interpretation

Marker-proxy adjustment reportedly attenuated the HT coefficient ~90% with the fully adjusted 95% CI including zero, consistent with B-lineage-associated expression variation but not identifying abundance, cellular state or a mediation effect. Original versus equal-weight residual partial R² of 0.0187 versus 0.0111 does not show statistically established superiority. These are **reported results not rerun here**. If removed to meet Comment 1, revise corresponding interpretations in every section consistently.

**This documentation update is not a substitute for resolving Comment 1.**
