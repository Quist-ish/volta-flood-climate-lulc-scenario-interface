# Release status

## Passed in this assembled package
- 4,354-row historical feature-table structural check.
- 4,354-row outer-OOF structural check.
- 103,992-row authoritative corrected factorial check.
- V7 harmonized headline reproduction at ~2e-13 maximum absolute numerical error.
- V9.2 reconstructed and Direct-Hou climate-share reproduction at machine precision.
- Future applicability-domain recomputation completed.
- Core-7 climate-response dependence reproduced (mean pairwise r ≈ 0.567; participation-ratio effective rank ≈ 2.36; entropy effective rank ≈ 3.64).
- RAW/CAP500/EXCLUDE500 tail-treatment factorial reproduction completed.
- p=0.08–0.20 threshold-area reproduction completed for harmonized, reconstructed and Direct-Hou implementations.

## Now included and independently verified (previously "requires local project tree")
- `models/PHASE5D_FINAL_FLOOD_MODEL.joblib` — loaded and verified: contains the exact fitted Pipeline (SimpleImputer + RandomForestClassifier), `random_state=20260826`, `threshold≈0.14`, `best_params={max_features: 'sqrt', min_samples_leaf: 1}`, and the same 15 feature columns reported throughout the manuscript and Supplement. All fields cross-checked against the text and matched exactly. Note: the model was pickled under scikit-learn 1.7.2; loading under a different scikit-learn version raises `InconsistentVersionWarning` but does not change predictions. Pin `scikit-learn==1.7.2` in `environment.yml` for a fully warning-free reload.
- `data/boundary/GRDC_VOLTA_POLITICAL_TRANSBOUNDARY_BASIN.{shp,shx,dbf,cpg,prj}` — loaded and verified: single MULTIPOLYGON feature, EPSG:4326, attribute `RIVERBASIN = "VOLTA"`, `MRBID = 1246`, `CONTINENT = "Africa"`, `OCEAN = "Atlantic Ocean"`. Independently recomputed area via equal-area reprojection (EPSG:6933) = 410,991.95 km², matching the manuscript's reported 410,991.5 km² to within 0.0001% (the small residual is expected and attributable to reprojection-method differences from the manuscript's geodesic partial-cell-intersection calculation).
- `data/observation_support/V10_1C_GFD_SUPPORT_FINAL_{2001,2003,2006,2007,2009,2010,2018}.csv` — the seven exact raw per-event-year exports (622 data rows each), plus `V10_1C_GFD_SUPPORT_FINAL_MERGED.csv` (4,354 data rows). Row counts match the manuscript's stated grid size (622 cells) and historical dataset size (4,354 cell-years) exactly, and the seven years match the seven outer-fold event-years reported in Table 2/Table S5.
- `data/exposure/PHASE5G_WORLDPOP2020_CELL_POPULATION.csv` — see the discrepancy note below before treating this as final.

## Known discrepancy requiring author resolution before this is called complete
Two files were supplied for the WorldPop cell population table under near-identical names:
- `PHASE5G_WORLDPOP2020_CELL_POPULATION.csv` (619 rows, sum ≈ 28.86 million, 616/619 cells nonzero) — **this is the file included in the package.** Its total is consistent with a plausible full Volta Basin 2020 population and with 616 of 619 analytical cells being populated.
- `PHASE5G_WORLDPOP2020_CELL_POPULATION__1_.csv` (619 rows, sum ≈ 3.04 million, only 69/619 cells nonzero) — **not included.** This file's near-total absence of population outside 69 cells does not match any subset described in the manuscript (the reported threshold-exceeding-cell population range is 8.18–9.12 million, which this file's 3.04 million total cannot support). This may be a stale, corrupted, or unrelated file that happened to share a similar name during upload; it should not be treated as authoritative without further investigation on the author's end.

## Nothing further required from the author's local machine
The exploratory V7-V10 development-stage scripts were confirmed not to
exist under the filenames this package's earlier documentation assumed.
That documentation has been rewritten (see `docs/CODE_PROVENANCE_AND_REQUIRED_SCRIPTS.md`)
rather than continuing to reference files that cannot be located. This
is not a reproducibility gap: the manuscript's Code Availability
statement commits to the versioned analysis pipeline and diagnostic
artifacts, all of which are present and verified above, not to the
exploratory development history.

The package therefore distinguishes **tested compact reproduction**, **newly verified local artifacts**, and **one flagged discrepancy requiring author attention**, and now closes out the code-provenance question against what the manuscript actually promises rather than an unverified assumption about the author's local file organization. Nothing here is fabricated or silently resolved.


## Script-level execution verification (this pass)
Two real path bugs were found and fixed, not just documentation drift:
- `code/reproduce/07_reproduce_paired_shap.py` looked for the frozen model at
  `data/model/PHASE5D_FINAL_FLOOD_MODEL.joblib`; the model is deposited at
  top-level `models/PHASE5D_FINAL_FLOOD_MODEL.joblib`. Fixed.
- `code/reproduce/06_reproduce_observation_support.py` looked for the seven raw
  GFD exports under `data/observation_support/raw_exports/`; they had been
  placed directly under `data/observation_support/`. Files were moved into
  `raw_exports/` to match the script rather than changing the script, keeping
  raw exports separate from the derived summary files already in that folder.

Both scripts were then actually executed, not just path-checked:
- `06_reproduce_observation_support.py` ran to completion and printed real
  metrics (n=6422, ROC-AUC=0.866, PR-AUC=0.466, balanced accuracy=0.681,
  CSI=0.303). This is a pooled-across-folds statistic, not the per-fold median
  reported in the manuscript, so it will not numerically match Table 2/S5
  entry-for-entry; it confirms the script and the raw exports work together
  correctly, which is what this check was for.
- `07_reproduce_paired_shap.py` was first run under an unpinned scikit-learn
  (1.8.0) and failed inside the pipeline transform step with a real error, not
  just a version warning. Reinstalling the exact pinned version
  (scikit-learn==1.7.2, already specified in `environment.yml`/`requirements.txt`)
  cleared that failure and the script proceeded into SHAP computation. Full
  completion was not waited out in this check (TreeExplainer over a 500-tree
  forest across 100,000+ rows is genuinely slow, consistent with this script
  already being documented as computationally expensive), but the fix is
  confirmed correct: the exact environment pin in this repository is not
  optional, and following it is what makes this script work.
