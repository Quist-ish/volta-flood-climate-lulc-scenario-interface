# Assembly validation report

This report records checks actually executed while assembling the journal-neutral package.

## Passed checks

- `code/00_verify_package.py`: all packaged files matched the SHA-256 manifest at validation time and the CAP500 factorial structure was 103,992 rows = 619 cells × 7 models × 2 SSPs × 3 directly evaluated periods × 4 states.
- `code/01_reproduce_cap500_direct_periods.py`: four-state closure reproduced with maximum absolute residual `1.1102230246251565e-16`.
- The supplied CAP500 cell-intersection areas summed to `410,991.544 km²`, consistent with the study’s rounded `410,992 km²` domain.
- Direct-period spatial-attribution rows reproduced the locked current Table S18 to its reported rounding.
- `code/02_estimate_2061_harmonized.py` ran successfully and generated a transparent S15 method reimplementation plus an eight-experiment cell table.

## 2061–2080 reimplementation check

The current Supplement explicitly treats 2061–2080 as an interpolation–emulation estimate rather than a directly evaluated window. The exact original revision execution file was not among the supplied source archives, so the package retains the submitted Table S18/S20 values as locked references and keeps the independent reimplementation separate.

For CAP500, the reimplemented basin climate shares were `85.608%` (SSP2-4.5) and `73.824%` (SSP5-8.5). The current Supplement reports the corresponding CAP500 basin-scale climate shares rounded as `85.6%` and `74.2%`; the deviations are approximately `+0.008` and `−0.376` percentage points. These are well inside the Supplement’s stated “few percentage points” uncertainty for the estimated window.

For the S18-style cell diagnostics, the largest absolute deviation from a current reported rounded value among the two 2061–2080 rows was about `1.1 percentage points`; all three directly evaluated periods reproduce to the reported rounding. This is why the package labels the 2061 script a **method reimplementation**, not an exact recovery of an unavailable original execution file.

## Slow analysis not run in the default smoke test

`code/03_spatial_meta_learning.py` implements the current eight-experiment spatial-block cross-validation, permutation-importance and 500-block-bootstrap workflow. It is intentionally excluded from the default `reproduce_all.py` smoke test because it is substantially slower. The authoritative submitted values are preserved in `reference_outputs/current_reported/Supplement_Table_S19_spatial_meta_learning.csv`.

## Submission-system hygiene

The archive contains no manuscript DOCX and no journal-specific package naming. It should be uploaded as code/data/reproducibility material rather than as the primary manuscript, avoiding a second Word-manuscript upload that could interfere with automatic metadata extraction.

## Recovered-author originals — v1.2.0 additional executed verification

- 49/49 recovered original files had matching independent SHA-256 hashes and byte counts.
- Historical features and OOF tables: 4,354 rows and 520 positives; fitted model SHA-256 exactly matches the prior frozen hash. No unsafe pickle deserialization was performed.
- Original RAW 103,992 factorial records: exact cellwise four-state closure (1.1102230246251565e-16); area-weighted model values aggregated to six **exact V7 RAW headline shares and effects**.
- Archived V9.2 Direct-Hou six-row summary: climate-only effect invariant to machine precision (stored difference 0), SSP5-8.5 combined sign reversal for all three directly evaluated periods; share changes 19.70–39.05 percentage points.
- Full WorldPop 619-cell input recognized separately from superseded single-tile backup.
- **No original analysis source scripts** in the recovered archive; 2061 estimate and spatial reimplementation remain not exact. The Zenodo DOI remains unverified.

For exact evidence and limitations see `ORIGINALS_RECOVERY_REPORT.md`.
