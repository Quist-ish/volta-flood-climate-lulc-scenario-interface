# Reproduction run order

This is the complete, tested reproduction pipeline. It is the "versioned
analysis scripts" referred to in the manuscript's Code Availability
statement. There is no separate "Level B" historical-source workflow:
the exploratory development stages referenced only internally during
analysis were not preserved as separately named scripts, and are not
part of what the manuscript commits to providing.

## Run order

1. `python code/reproduce/00_verify_release.py` — structural checks (row
   counts, expected columns, expected factorial states) before running
   anything else.
2. `python code/reproduce/01_reproduce_historical_validation.py` — Table 2 /
   Table S5 grouped-fold validation metrics.
3. `python code/reproduce/02_reproduce_factorial_headlines.py` — Table 3
   harmonized factorial headline.
4. `python code/reproduce/03_reproduce_lulc_interface.py` — harmonized vs.
   reconstructed vs. Direct-Hou interface comparison (Table 3, Table S11).
5. `python code/reproduce/04_reproduce_applicability_domain.py` —
   applicability-domain diagnostics (Table S11).
6. `python code/reproduce/05_reproduce_core7_dependence.py` — Core-7
   dependence weights and effective-rank diagnostics (Table S3).
7. `python code/reproduce/06_reproduce_observation_support.py` — GFD
   observation-support sensitivity (Table S4/S5). Uses the seven raw
   `data/observation_support/V10_1C_GFD_SUPPORT_FINAL_*.csv` exports,
   which are included in this release.
8. `python code/reproduce/07_reproduce_paired_shap.py` — paired Tree SHAP
   diagnostics. Requires `models/PHASE5D_FINAL_FLOOD_MODEL.joblib`
   (included) and is computationally the most expensive step.
9. `python code/reproduce/08_reproduce_tail_sensitivity.py` — RAW/CAP500/
   EXCLUDE500 precipitation-tail sensitivity.
10. `python code/reproduce/09_reproduce_threshold_sensitivity.py` —
    threshold sensitivity p=0.08-0.20 across all three LULC interfaces.

`python code/reproduce/reproduce_all.py` runs all of the above in order.

## What "reproduction" means here

Steps 1-6 and 8-10 use only the analysis-ready tables already in
`data/analysis_ready/`, `data/observation_support/`, and
`data/supplementary_tables/`, and reproduce the reported values to
machine precision (see `RELEASE_STATUS.md` for the exact verified
tolerances). Step 7 additionally requires the frozen model file, which
is included. No step in this pipeline requires access to raw
third-party provider data (CHIRPS, ERA5-Land, NEX-GDDP-CMIP6, etc.);
those are cited by version and source in
`manifests/external_data_sources.csv` for anyone wanting to rebuild the
analysis-ready tables from scratch, but rebuilding them is not required
to verify the paper's reported results.
