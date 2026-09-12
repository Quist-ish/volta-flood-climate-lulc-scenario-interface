# Volta Basin Climate–LULC Scenario-Interface Flood Analysis

## Reproducibility materials

This repository contains the code, documentation, manifests, analysis-ready data, and reference outputs supporting the study:

**Scenario-interface uncertainty reshapes climate versus land-use contributions to future flood occurrence across the transboundary Volta Basin**

The repository is intended to support transparent inspection and reproduction of the analyses reported in the manuscript and Supplementary Information. A versioned Zenodo archive will provide the permanent citable record and the larger reproducibility artifacts that are unsuitable for routine GitHub storage.

## Study overview

The analysis evaluates how the representation of future climate and land-use/land-cover (LULC) scenarios affects modeled future flood-occurrence probability across the six-country transboundary Volta Basin.

A frozen Random Forest classifier is evaluated within a four-state climate × LULC counterfactual framework:

- `C0L0` — historical climate + historical LULC
- `C1L0` — future climate + historical LULC
- `C0L1` — historical climate + future LULC
- `C1L1` — future climate + future LULC

The four states are evaluated separately within each retained climate model before ensemble summarization.

The final Core-7 CMIP6 ensemble comprises:

- ACCESS-CM2
- ACCESS-ESM1-5
- CanESM5
- INM-CM5-0
- IPSL-CM6A-LR
- MIROC6
- TaiESM1

Future analyses cover:

- **SSP2-4.5**
- **SSP5-8.5**

for three projection periods:

- **2021–2040**
- **2041–2060**
- **2081–2100**

## Analyses supported by this archive

The deposited materials support reproduction or verification of the following components of the study:

1. grouped historical out-of-fold model evaluation;
2. corrected historical and future precipitation predictors, including the R10mm and R20mm count-index correction;
3. RAW, `CAP500`, and `EXCLUDE500` precipitation-tail sensitivity analyses;
4. model-level climate, LULC, interaction, and combined factorial effects;
5. threshold sensitivity across `p = 0.08–0.20`, including the archived `p = 0.14` projection slice;
6. future applicability-domain diagnostics;
7. MODIS–Hou harmonized versus Direct-Hou LULC representation sensitivity;
8. GFD observation-support sensitivity;
9. paired Tree SHAP scenario-response diagnostics when the frozen fitted model is available; and
10. Core-7 climate-model dependence weighting and associated sensitivity analyses.

## Authoritative analytical inputs

The authoritative corrected factorial input for the final future analysis is:

`data/analysis_ready/RAW_FACTORIAL_PREDICTIONS.csv.gz`

This file contains the corrected future predictor states used in the final factorial analysis, including the corrected R10mm and R20mm count indices.

The earlier Phase5E factorial feature table is retained only for provenance and audit purposes under:

`data/audit_only/`

It predates the corrected future R10mm/R20mm states and **must not be used for the final factorial interpretation or Tree SHAP analysis**.

Compressed analysis-ready files are used in the GitHub repository where appropriate to reduce unnecessary duplication and repository size.

## Repository structure

```text
.
├── code/
│   ├── reproduce/
│   └── exact/
├── data/
│   ├── analysis_ready/
│   ├── audit_only/
│   ├── boundary/
│   ├── exposure/
│   ├── observation_support/
│   ├── reference_outputs/
│   └── supplementary_tables/
├── docs/
├── manifests/
├── reproduced_outputs/
├── CITATION.cff
├── DATA_AVAILABILITY.md
├── DATA_LICENSE_NOTICE.md
├── PROVENANCE_LIMITATIONS.md
├── RELEASE_STATUS.md
├── RUN_ORDER.md
├── environment.yml
└── requirements.txt
```

The corresponding Zenodo archival release will contain the frozen fitted model and other larger artifacts that are unsuitable for routine GitHub storage.

## Reproduction

The reproducibility code is provided in the `code/` directory of this repository.

### Environment

Using Conda:

```bash
conda env create -f environment.yml
conda activate volta-objective3-repro
```

### Run the reproducibility workflow

```bash
python code/reproduce/reproduce_all.py
```

See `RUN_ORDER.md` for the recommended execution sequence and `RELEASE_STATUS.md` for the verification status of the released materials.

Some analyses, particularly Tree SHAP reproduction, require the frozen fitted model distributed with the complete Zenodo archival release.

## Key documentation

The repository includes the following supporting documentation:

- `RUN_ORDER.md` — recommended analysis execution sequence
- `DATA_AVAILABILITY.md` — data access and redistribution information
- `DATA_LICENSE_NOTICE.md` — licensing and redistribution notes
- `PROVENANCE_LIMITATIONS.md` — provenance boundaries and methodological limitations
- `RELEASE_STATUS.md` — release verification information
- `CITATION.cff` — machine-readable citation metadata
- `docs/DOWNLOAD_EXTERNAL_SOURCES.md` — authoritative third-party source locations
- `docs/CODE_PROVENANCE_AND_REQUIRED_SCRIPTS.md` — code provenance and script requirements

The `manifests/` directory provides file inventories, traceability information, data dictionaries, and checksums linking analytical inputs and outputs to the reported study.

## Integrity verification

Release integrity can be checked using the supplied SHA-256 records:

`manifests/checksums.sha256`

and

`manifests/checksum_manifest.csv`

These records are provided to verify that released analytical inputs and supporting artifacts correspond to the frozen reproducibility package.

## Reproducibility and interpretation boundaries

### Analytical domain

The exact project-local Volta Basin geometry distributed with the reproducibility materials is the analytical boundary used in the study.

The complete intermediate GIS editing history connecting the upstream GRDC Major River Basins source package to the locked project derivative was not preserved. The distributed locked geometry therefore defines the reproducible analytical domain.

### Historical validation

Historical validation consists of grouped event-year evaluation and GFD observation-support sensitivity.

No independent event-matched flood-sensor or hydrometric dataset formed part of the validation design. The resulting model probabilities are therefore interpreted comparatively rather than as calibrated absolute event probabilities.

### Threshold interpretation

The archived `p = 0.14` value is retained as a secondary projection-continuity slice within the broader `p = 0.08–0.20` threshold sensitivity analysis.

It is not interpreted as a calibrated, cross-validation-selected, or universally optimal deployment threshold.

### Reservoir representation

The model does not dynamically simulate future reservoir operating rules. Historical regulation may be represented indirectly through fitted historical spatial associations, but future changes in Lake Volta–Akosombo reservoir operations are outside the modeled system.

### Population exposure

Population exposure uses WorldPop 2020 held fixed through time.

These results therefore represent **fixed-current population exposure** rather than future demographic projections or dynamic future flood risk.

### Infrastructure

OpenStreetMap infrastructure counts are not used in headline inference because basin-wide completeness was not established.

### Future LULC representation

Future LULC uncertainty is evaluated using the Hou et al. scenario product through both:

- a primary MODIS–Hou harmonized interface; and
- a Direct-Hou structural sensitivity.

The Direct-Hou analysis is a scenario-interface sensitivity test rather than an alternative estimate of causal truth.

## Data availability and third-party sources

This repository redistributes study-generated and analysis-ready products where appropriate.

Large or externally licensed third-party source datasets are not necessarily redistributed. Where source products are omitted, the repository provides provider information, provenance records, manifests, and processing documentation needed to identify their role in the analysis.

See `DATA_AVAILABILITY.md` and `docs/DOWNLOAD_EXTERNAL_SOURCES.md` for details.

## GitHub and Zenodo archive strategy

GitHub provides the version-controlled repository for code, documentation, manifests, compact analysis-ready data, and reproducibility outputs.

Zenodo will provide the permanent archival release and DOI. The Zenodo record will contain the complete frozen reproducibility package, including larger artifacts that are not appropriate for routine GitHub storage.

For reproduction of the published study, users should use the versioned GitHub release and corresponding Zenodo archive associated with the manuscript rather than later development versions of the repository.

**Zenodo DOI:** 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22713203.svg)](https://doi.org/10.5281/zenodo.22713203).

### Recommended citation

QUIST, I., Bi, S., Yeboah, E., Sarfo, I., Mensah, A. O. K. N., Evi, M., Oduro, C., & Benjamin Nana yaw Quist. (2026). Reproducibility materials for scenario-interface uncertainty in future flood occurrence across the transboundary Volta Basin (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22713203.

## License

See `LICENSE` and `DATA_LICENSE_NOTICE.md` for the licensing conditions applicable to the repository code, study-generated outputs, and third-party-derived materials.
