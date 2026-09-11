# Volta Basin Objective 3 reproducibility archive

**Study:** Scenario-interface uncertainty reshapes climate versus land-use contributions to future flood occurrence across the transboundary Volta Basin

**Repository:** https://github.com/Quist-ish/volta-flood-climate-lulc-scenario-interface (create this repository under your GitHub account and push this package's contents as its initial commit)

This repository/archive is the reproducibility package for the final Objective 3 analysis. It is designed for a **GitHub code repository linked to a Zenodo DOI**. The package separates (i) executable code and small analysis-ready data that are suitable for GitHub, from (ii) bulky audit archives and third-party source products that are more appropriate for Zenodo or should be re-downloaded from their authoritative providers.

## What this release reproduces

The final analysis uses a frozen Random Forest classifier and a four-state counterfactual design (`C0L0`, `C1L0`, `C0L1`, `C1L1`) on the six-country transboundary Volta analytical domain. The final projection ensemble contains seven CMIP6 models: ACCESS-CM2, ACCESS-ESM1-5, CanESM5, INM-CM5-0, IPSL-CM6A-LR, MIROC6 and TaiESM1. Scenarios are SSP2-4.5 and SSP5-8.5; projection windows are 2021–2040, 2041–2060 and 2081–2100.

The deposited analysis-ready files reproduce:

1. grouped historical out-of-fold evaluation;
2. corrected future climate predictors, including the R10mm/R20mm count-unit correction;
3. source-native / CAP500 / EXCLUDE500 precipitation-tail sensitivity (audit archive); 
4. model-first factorial climate, LULC and interaction components;
5. threshold sensitivity (`p=0.08`–`0.20`) and the archived `p=0.14` operating point;
6. future applicability-domain diagnostics;
7. MODIS–Hou harmonized versus Direct-Hou LULC representation sensitivity;
8. GFD observation-support sensitivity;
9. paired Tree SHAP scenario-response diagnostics when the frozen model is present;
10. Core-7 dependence-aware weighting.

## Critical authority rule

`data/analysis_ready/RAW_FACTORIAL_PREDICTIONS.csv.gz` is the authoritative corrected factorial input for the final future analysis. The older Phase5E table is retained only in `data/audit_only/` because it predates the corrected future R10mm/R20mm states and **must not be used for final SHAP interpretation**.

## Quick start

```bash
conda env create -f environment.yml
conda activate volta-objective3-repro
python code/reproduce/reproduce_all.py
```

The reproduction scripts use only the analysis-ready tables and the frozen model already included in this release, and do not require redownloading any third-party data. See `RUN_ORDER.md`, `DATA_AVAILABILITY.md`, `PROVENANCE_LIMITATIONS.md`, the CSV manifests in `manifests/`, and the exact published-table source files in `data/supplementary_tables/` (predictor correlation matrix and interface applicability-domain comparison). The frozen model (`models/`), the exact GRDC boundary shapefile (`data/boundary/`), the seven raw GFD observation-support exports (`data/observation_support/`), and the WorldPop cell population table (`data/exposure/`) are now included and independently verified — see `RELEASE_STATUS.md` for the verification details and one flagged discrepancy requiring author attention.

## Zenodo/GitHub release strategy

Use the GitHub ZIP generated with this package for code, manifests and compact analysis-ready data. Upload the larger Zenodo audit ZIP separately and cite its DOI from the GitHub README. A GitHub release can then be archived through Zenodo's GitHub integration.

## Reproducibility boundaries

- The complete intermediate GIS edit history that transformed the upstream GRDC Major River Basins source package into the local `GRDC_VOLTA_POLITICAL_TRANSBOUNDARY_BASIN` derivative was not recoverable. The exact locked geometry is therefore the reproducible analysis geometry.
- `p=0.14` is an archived analytical operating point, not a demonstrated calibrated/CV-selected threshold.
- Independent event-matched Sentinel-1 validation, dynamic reservoir operations and dynamic future population were **not completed** and are not represented as completed analyses.
- WorldPop is fixed-2020 exposure; it is not a future demographic projection.
- OpenStreetMap counts were removed from headline inference because basin-wide completeness was not established.

## Citation

After the Zenodo record is published, replace `DOI_PENDING` in this README and `CITATION.cff` with the issued DOI. Do not invent a DOI before Zenodo issues or reserves one.
