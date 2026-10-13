# Original source recovery and analytical evidence — 13 October 2026

## Verified

- The 49 original bytes are preserved in `original_sources/` without renaming, except Windows path separators converted to directory separators. Source SHA-256 and byte sizes independently match all 49 entries in both uploaded inventories.
- The two unmatched expected filenames (`GRDC_VOLTA_POLITICAL_TRANSBOUNDARY_BASIN.gpkg`, `.geojson`) are *alternative formats*, not missing geographic information. The original five-part shapefile is included. Do not claim a GeoPackage or GeoJSON was recovered.
- Original frozen model `PHASE5D_FINAL_FLOOD_MODEL.joblib` SHA-256 **f08389f3b416f7f9cdd03ac62c0e41f2fcd0aac496f472122157229abd65dcd6** matches prior project provenance. The verifier does not execute/unpickle the model. Loading it is a separate trusted-software, pinned-environment operation.
- Historical original feature/outer-OOF tables: 4,354 rows, 622 unique cells, 520 flood-positive labels, seven event years. No new out-of-event training is claimed.
- Original RAW factorial predictions: 103,992 records from 619 cells, 7 models, 2 SSPs, 3 directly evaluated periods and 4 states. The cellwise four-state maximum absolute numerical closure residual is 1.1102230246251565e-16.
- Model-by-model area-weighted RAW contrasts and the ensemble median-of-model summaries reproduce the six original V7 `HEADLINE_FACTORIAL_RESULTS.csv` rows and climate shares to numerical precision.
- The archived V9.2 adopted-vs-Direct-Hou comparison reports climate-only contrast invariance (maximum difference 0.0), SSP5-8.5 sign reversal for all 3 directly evaluated periods, and climate-share shifts from 19.70 to 39.05 percentage points.
- Fixed-2020 full-basin WorldPop has 619 cells, total approximately 28.855 million; a separate *single-tile backup* has approximately 3.042 million and must not be used for the study's final exposure.

## Editorial interpretation

Exact closure holds for **each model–cell counterfactual**. Medians are aggregated separately by component; `median(C)+median(L)+median(I)` need not equal `median(Combined)`. The table should not be described as failing factorial closure for this reason. Dataset-specific CAP500 percentages must not be compared with the primary RAW headlines as if they were the same treatment.

## Still unavailable or unverified

- **No original `.py` or `.ipynb` analysis scripts were captured** among the 49 files. The collector searched only script areas `11_OBJECTIVE3_ANALYSIS` and `12_CRITICAL_REANALYSIS_2026`, not later `13_ANALYSIS_2026_NOVELTY_ROBUSTNESS` or `25_MILLIE_REPRODUCIBILITY_AND_EDITOR_PACKAGE_2026`. A wider script-only collection is needed before claiming original source-code availability.
- The original full **Direct-Hou cellwise predicted probabilities** are not present; the archive provides its V9.2 six-row headline summary, raw Hou future fractions and reconstructed-Hou predictions, which are distinct things.
- The original reported 2061–2080 interpolation–emulation script and finalized spatial meta-learning script have not been recovered. The v1.1.1 scripts for these steps are documented *reimplementations*, not the original executed source.
- The manuscript-reported Zenodo DOI `10.5281/zenodo.22713203` remains independently unverified; no assertion of archived complete deposition is justified.
- Provider redistribution rights, particularly for GRDC-derived boundary, GFD-derived rows, and other third-party sources, must be checked before publishing the original-source folder openly.

## How to run

`python code/04_verify_recovered_originals.py`

The script checks original file bytes, historical support, RAW factorial closure, exact six V7 headlines, V9.2 Direct-Hou summary, and the final-vs-backup WorldPop distinction. It **does not unpickle or refit** the frozen model, and does not overwrite original source files.

**Status: VERIFIED ORIGINAL ARCHIVE AND DIRECT-PERIOD OUTPUT REPRODUCTION; INCOMPLETE ORIGINAL FULL-PIPELINE CODE.**
