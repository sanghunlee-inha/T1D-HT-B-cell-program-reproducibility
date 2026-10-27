# T1D–HT B-cell program reproducibility — IJMS R3

Manuscript: **Cross-Tissue Concordance of a T1D Blood-Derived B-Cell Signature with Hashimoto Thyroiditis Tissue: Exploratory Spatial Immune-Topic Analysis** (ijms-4640479).

**Scope:** This repository recalculates Figure 2's **summary-level** meta-analysis from 24 retained cohort/pathway effects. It does not independently derive effects from source expression matrices or reproduce Figures 3–5 end to end. Code availability must not be confused with reproduction of an analysis.

## Quick start

```bash
python -m pip install -r requirements.txt
python scripts/01_t1d_random_effects_meta.py
python scripts/99_audit_summary.py
python scripts/98_validate_summary_level.py
```

The new independent implementation `scripts/98_validate_summary_level.py` (standard-library only) checks all eight pathway meta-analysis rows against `results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv` using `data/derived/t1d_pathway_cohort_effects.tsv`. It **passed all eight rows on 2026-10-28** using the currently published retained inputs. This verifies derived-input consistency, **not original raw-cohort effect generation**.

## Figure-by-figure evidence

| Manuscript | Status in this repository |
|---|---|
| Figure 1, workflow | Conceptual; not analytical validation |
| Figure 2A–B | Summary-level independently recalculated from 24 retained effects; no raw-expression workflow |
| Figure 3A–H, spatial RNA-first topics and H&E | **Not reproduced here**: topic fitting/model selection and model input-output lineage incomplete |
| Figure 4A, frozen 14-gene HT bulk | **Not reproduced here**: complete signed weights, standardized expression/covariates and null inputs not provided here |
| Figure 4B, spatial frozen score | **Not reproduced here**: processed spot/slide matrices and gene-null assets unavailable |
| Figure 4C–E, single-cell/context | **Not reproduced here**: processed cell/library and HT pathway analysis objects unavailable |
| Figure 5A–D, marker-proxy and weights | **Not reproduced here**: design matrices, bootstrap settings, random weights and reference gene coverage unverified |

See [R3 reproducibility status](docs/REPRODUCIBILITY_STATUS.md) and [manuscript alignment](docs/R3_MANUSCRIPT_ALIGNMENT.md).

## Interpretation

The historical 15-gene and frozen 14-gene HT scores used the **same 66 HRA001684 specimens** and do not provide independent patient-cohort replication. The direct spatial five-slide tests were nonsignificant (reported exact P = 0.10; matched-gene P = 0.085), and Topic 7 spatial maps do not localize the frozen signature. Marker-proxy adjustment reportedly attenuated the HT coefficient approximately 90% (fully adjusted interval includes zero). This cannot distinguish B-cell infiltration from B-cell state or establish causal mediation. The reported residual partial R² difference (original 0.0187 vs equal-weight 0.0111) does not demonstrate statistically significant superiority of T1D-derived weights. These analyses **were not rerun by the current GitHub package**.

## Release / archival status

- Historical [GitHub v0.1.1](https://github.com/sanghunlee-inha/T1D-HT-B-cell-program-reproducibility/releases/tag/v0.1.1) predates this R3 update; it is not evidence that these changes were archived.
- Separate [Zenodo software v1 DOI: 10.5281/zenodo.23164148](https://doi.org/10.5281/zenodo.23164148) contains historical downstream scripts, but a complete clean rerun of all manuscript figures has not been verified.
- The previously cited DOI `10.5281/zenodo.23502426` requires separate verification before any claim of accessible archival publication. This update **does not claim a new Zenodo DOI**.

If an analysis cannot be independently substantiated with auditable inputs and rerunnable code, remove its inferential claims rather than describing it as independently reproduced. Do not distribute restricted or personally identifiable data.
