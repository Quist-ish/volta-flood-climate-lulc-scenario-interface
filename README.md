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
