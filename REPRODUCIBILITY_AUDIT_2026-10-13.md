# Independent reproducibility audit — 13 October 2026

**Study:** Future land-cover translation can reverse the modeled climate–landscape attribution of flood occurrence in the transboundary Volta Basin

**Repository:** https://github.com/Quist-ish/volta-flood-climate-lulc-scenario-interface

**Assessment:** **PARTIALLY REPRODUCIBLE**. This is a scope-limited audit, not a certification of end-to-end source-level reproduction or an editorial acceptance recommendation.

## Verified reproducible evidence

| Check | Evidence / conclusion |
| --- | --- |
| GitHub authentication and repository access | `Quist-ish` account had read/write access; changes merged to public `main` |
| GitHub Actions CAP500 CI | PR #2 merged; pull-request run **38378290970** completed **success**; job **cap500-reproducibility**; structural check, recomputation, generated-output checks and artifact upload passed |
| GitHub-generated artifact | `cap500-direct-period-recomputed` present on successful Actions run |
| Compact archive integrity | 58 manifest entries checked, 58 SHA-256 matches (local archive integrity execution) |
| Archived CAP500 support | 103,992 = 619 common-support cells × 7 climate models × 2 SSPs × 3 directly evaluated periods × 4 states |
| Four-state decomposition | Maximum absolute closure residual = **1.1102230246251565e-16** |
| Basin intersection-area summary | **410,991.544 km²**, rounded to 410,992 km² |
| Direct-period CAP500 model/basin outputs | Recalculated from archived predictions and written separately from reported manuscript tables |
| 2061–2080* | Supplement S15 **method reimplementation executed**, not an exact rerun of unavailable original revision source |
| Spatial meta-learning | Five-fold spatial-block evaluation and 500 block-bootstrap analyses executed from method reimplementation; results **not an exact match** to reported Supplement S19 |

## Numerical differences that remain open

1. The archived CAP500 direct-period climate shares differ from manuscript primary harmonized/RAW shares by up to **0.9004 percentage points**. These represent *different precipitation-tail treatments* and should not be conflated; the primary RAW row-level table is needed for a like-for-like check.
2. The 2061–2080 CAP500 reimplementation yielded climate shares **85.6079%** for SSP2-4.5 and **73.8244%** for SSP5-8.5. The Supplement lists CAP500 rounded values **85.6%** and **74.2%**, respectively. This supports approximate behavior, not numerical identity.
3. Reimplemented spatial meta-learning ROC-AUC compared with reported Table S19: active vs inactive **0.8965 vs 0.900**, landscape vs climate on active cells **0.7586 vs 0.771**, and sign of response **0.7274 vs 0.725**. Reimplemented sample sizes **4,952 / 3,481 / 2,918** compared with reported **4,952 / 3,479 / 2,917**. The original script and its full precision/seed decisions are required to resolve the last two sample-count discrepancies.

These values are **diagnostic evidence**, not corrected manuscript results. No numbers in the manuscript should be overwritten solely to make the reimplementation agree.

## Availability and provenance boundaries

- The full original RAW and Direct-Hou factorial prediction files, historical training / out-of-fold inputs, frozen fitted random-forest artifact, exact original 2061–2080 execution script, locked project basin vector and WorldPop cell-level table were **not present** in the compact source archives available for this audit.
- Consequently, the currently published GitHub CI validates **CAP500 direct-period archived predictions only**. It does not reconstruct the original full historical training, Direct-Hou scenario input, external-data verification or the supplementary estimated period.
- The corresponding manuscript reports Zenodo DOI **10.5281/zenodo.22713203**, but independent direct Zenodo/DOI/DataCite retrieval was unsuccessful on 13 October 2026. This cannot be called an independently verified public archival record.
- The random forest is a **statistical response model**, not a hydraulic model; the six-cell UNOSAT case is descriptive local evidence only; the 2061–2080 period is estimated rather than directly model-evaluated.

## Required before declaring the archive fully reproduced

1. Confirm the Zenodo record publicly resolves, and compare its deposited file inventory and checksums with the version cited in the manuscript.
2. Recover the original RAW and Direct-Hou row-level predictions and frozen fitted model plus historical input/output files; retain original author provenance and checksums.
3. Recover the exact revised 2061–2080 interpolation/emulation and S19 spatial meta-learning scripts, with fixed random seeds and thresholding rules.
4. Run like-for-like checks against all final main and supplementary tables. Retain differences transparently; do not backfit outputs to rounded tables.
5. Freeze the complete source archive in a versioned release with immutable checksums, an executable environment, and clear distinction between original and reconstructed code.

**Do not describe the present public GitHub repository or compact assembled ZIP as complete end-to-end reproducibility.**

This record is journal-neutral and does not modify manuscript figures, equations, tables or conclusions.
