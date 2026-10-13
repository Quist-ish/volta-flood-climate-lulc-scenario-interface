# Volta Basin flood-occurrence scenario-interface reproducibility

**Associated study:** Future land-cover translation can reverse the modeled climate–landscape attribution of flood occurrence in the transboundary Volta Basin.

This is a **journal-neutral** research repository. Its code and outputs may be examined by editors and reviewers of any journal. No manuscript Word file is deposited here.

> **Verified compact workflow; incomplete full-source archive.** The published `main` branch has passed a GitHub Actions smoke test of archived CAP500 factorial predictions (run 38378290970). The separately assembled journal-neutral v1.1.0 ZIP contains additional scripts and outputs that are **not all deposited here**. Neither set should be described as complete source-level reconstruction. See [independent audit](REPRODUCIBILITY_AUDIT_2026-10-13.md).

## Study design and analytical support

- Volta basin: 623 intersecting 0.25° cells; 622 historical model cells; **619 complete future-support cells**.
- Historical support: **4,354** cell-years, **520** flood-positive labels; 15 model predictors.
- Seven retained CMIP6 models under SSP2-4.5 and SSP5-8.5.
- **Directly evaluated:** 2021–2040, 2041–2060, 2081–2100.
- **Estimated only:** 2061–2080* using the interpolation–emulation approach documented in Supplement Sect. S15.
- Primary MODIS–Hou **harmonized** future-LULC interface versus unharmonized **Direct-Hou** sensitivity.
- Four fitted-model states: C0L0, C1L0, C0L1, C1L1; contrasts decompose into climate, LULC and interaction. These are **statistical response-surface contrasts, not causal or physically conserved attribution fractions**.

The common-support input `data/analysis_ready/CAP500_FACTORIAL_PREDICTIONS.csv.gz` has **103,992** archived rows: 619 × 7 × 2 × 3 × 4. The *estimated* 2061–2080 period is not a native fourth period in this table.

## Available executable verification

From the repository root, install `requirements.txt` and run:

```bash
python code/00_verify_public_repository.py
python code/01_reproduce_cap500_direct_periods.py
```

The first script checks the archived CAP500 cell/model/scenario/period/state structure. The second recomputes cell-level factorial contrasts, their algebraic closure and area-weighted model-level summaries of the **three directly evaluated periods**. Both succeeded in a GitHub Actions run; this checks only the deposited subset of the analysis. It writes new files under `generated_outputs/` and does not overwrite submitted/reference results.

Do **not** interpret the outputs as a re-execution of the full model-training pipeline, Direct-Hou factorial predictions, or the original 2061–2080 emulation. For access to other compact v1.1.0 integration scripts and their generated files, consult the separately assembled research package and `RELEASE_STATUS.md`.

## Results interpretation and verification boundaries

The headline representation result is that climate-only contrasts are identical across the LULC interfaces, whereas the combined SSP5-8.5 response is positive under harmonization and negative under Direct-Hou for the directly evaluated three periods and the estimated 2061–2080* period. The climate share changes by 19.70–39.05 percentage points between interfaces (reported table values).

The 2023 UNOSAT six-cell comparison is **descriptive local evidence only**, not basin-wide discrimination, calibration, or hydraulic validation. The random forest is a statistical response model, not a process-based hydrological or hydraulic model. Historical covariate diagnostics cannot establish absence of future concept drift.

## Provenance and release transparency

- `STUDY_ALIGNMENT.md` — exact current study support and period semantics.
- `RUN_ORDER.md` — commands available **on this branch**.
- `RELEASE_STATUS.md` — what is present, what is not, and which results are reported versus independently recomputed.
- `DATA_AVAILABILITY.md` and `PROVENANCE_LIMITATIONS.md` — availability and interpretation boundaries.
- `reference_outputs/current_reported/` — transcribed, **not recalculated**, manuscript-reported data tables.

The associated manuscript cites Zenodo DOI **10.5281/zenodo.22713203**. This is **manuscript-reported but has not been independently resolved or its files verified**; do not claim that the permanent archive has been verified. The archive's existence and contents must be checked by the corresponding author.

Third-party datasets retain their provider terms. New code in this repository is under MIT where expressly licensed.

## Additional original-source recovery (13 October 2026)

The authors supplied 49 original source files after the earlier compact-package audit. All 49 matched their inventory SHA-256 values and file sizes in an independent check. The new local review package v1.2.0 includes the original frozen model (SHA-256 f08389f3b416f7f9cdd03ac62c0e41f2fcd0aac496f472122157229abd65dcd6), historical and outer-OOF tables (4,354 records, 622 cells, 520 flood positives), original RAW predictions (103,992 rows), V7 primary results, archived V9.2 Direct-Hou headline summaries, GFD observation-support files, the five-component basin shapefile and WorldPop reference/backup files.

The original RAW data reproduce six V7 primary factorial headline shares and component medians to numerical precision. The archived V9.2 comparison shows identical climate-only contrasts (maximum difference 0.0), a sign reversal of the SSP5-8.5 combined response in all three directly evaluated periods, and a 19.70–39.05 percentage-point change in climate share.

This original-source archive is held separately for author/editor review and HAS NOT been uploaded to public GitHub because provider-redistribution and binary model security checks remain outstanding. No original analysis .py or .ipynb files were found in the 49 recovered files; the exact estimated 2061–2080 and S19 spatial code and the original Direct-Hou cellwise predictions remain unavailable. The manuscript-cited Zenodo DOI has not been independently verified.

See ORIGINAL_SOURCE_RECOVERY_VERIFICATION_2026-10-13.md for an audit and release boundaries.

## Additional review files from the 13 October public upload

Review-only method reimplementations are available at `code/02_estimate_2061_harmonized.py` and `code/03_spatial_meta_learning.py`. The **estimated 2061–2080** analysis and S19 spatial meta-learning here are *reimplementations*, not recovered original executables. Their archived results are kept under `generated_outputs/` and must not be substituted for the original manuscript tables under `reference_outputs/current_reported/`.

These optional scripts use scikit-learn, which is not part of the minimal CI-only dependencies. To run them in a compatible local environment:

```bash
python -m pip install -r requirements-extended.txt
python code/00_verify_public_repository.py
python code/01_reproduce_cap500_direct_periods.py
python code/02_estimate_2061_harmonized.py
python code/03_spatial_meta_learning.py
```

The 03 script is slower and is **not** part of the short automated CAP500 GitHub workflow. No original RAW or Direct-Hou source data have been made public by this upload. Consult `ORIGINAL_SOURCE_RECOVERY_VERIFICATION_2026-10-13.md` before interpreting these derived outputs.
