# T1D–HT B-cell program reproducibility

**Manuscript:** Cross-Tissue Concordance of a T1D Blood-Derived B-Cell Signature in Hashimoto Thyroiditis: Exploratory Spatial Characterization of Thyroid Immune Niches (IJMS, manuscript ijms-4640479).

**Authors:** Eun Young Joo and Sang Hun Lee.

This repository separates independently executable summary-level analyses from analyses requiring source data, unpublished intermediate objects, or historical software dependencies. It is **not** a claim that all analyses or figures can be reconstructed end to end.

## Data and evidence levels

| Component | Dataset | Status in this release |
|---|---|---|
| T1D pathway random-effects meta-analysis | GSE30210, GSE9006, GSE156035 | Executable from the included *retained cohort-level effect estimates* (not raw expression reconstruction) |
| Frozen 14-gene weighted signature | Three T1D datasets → HRA001684 | Reported in manuscript, signed weights must be supplied from verified Supplementary Table S1; not reconstructed here |
| Historical unweighted 15-gene HT analysis | HRA001684 | Historical reported result; upstream lineage unresolved |
| Spatial frozen-score contrast | GSE248205 | Five-slide result reported, but no raw spatial scoring matrices included; not replicated here |
| Descriptive single-cell immune markers | GSE192580 | Source-verified manuscript description; counts/metadata are not redistributed in this release |
| Exploratory spatial RNA-first topics and H&E modelling | GSE248205 / GSE230424 | Historical fitting and model selection dependencies incomplete |

### Biological units and interpretation

- HRA001684 comprises 16 HT and 50 non-HT bulk thyroid samples. Two distinct scoring procedures applied to the *same* cohort do not provide independent patient-cohort replication.
- GSE192580 contains three HT and three ICI-associated thyroiditis libraries (6,512 cells), **not healthy thyroid controls**. These data are used descriptively.
- The slide-level GSE248205 contrast involved three HT and two control sections (exact permutation P = 0.10). Matched-gene-null P = 0.085 and B/plasma-topic correspondence P = 0.90 do **not** establish preferential localization of the frozen score.
- HT peripheral blood and T1D pancreatic islets were **not** directly tested with the frozen signature.

## Quick start (summary-level meta-analysis only)

```bash
python -m pip install -r requirements.txt
python scripts/01_t1d_random_effects_meta.py
python scripts/99_audit_summary.py
```

The meta-analysis reads `data/derived/t1d_pathway_cohort_effects.tsv` and writes summary results under `results/`. It does not claim to independently reproduce the underlying effect estimates from expression matrices.

## Reported primary numerical anchors

- T1D summary-level B-cell pooled Hedges' g: **0.514716** (95% CI **0.177885–0.851547**); BH-adjusted q **0.021948**; I² **0%**.
- HRA001684 frozen 14-gene score: HC3-adjusted β **2.653394**, 95% CI **2.367850–2.938938**; both 50,000-draw empirical P values approximately **2 × 10⁻⁵** (reported results, **not recomputed** by this package).
- Historical 15-gene unweighted HT association: β **2.70** (95% CI **2.41–2.99**) (reported result, **not recomputed** here).

## Data and code provenance

See [docs/REPRODUCIBILITY_STATUS.md](docs/REPRODUCIBILITY_STATUS.md) and [docs/DATA_ACCESS.md](docs/DATA_ACCESS.md). The versioned signed weights, original robust normalization helper, raw-to-result source manifests, and any trained models must be validated and added before calling the corresponding workflows independently reproducible. No patient-level records or restricted files should be uploaded without authorization.

## Citation

Article manuscript ID: `ijms-4640479`. Zenodo DOI: **pending publication**. Please cite the published paper and the archive DOI once issued.
