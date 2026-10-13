# Reproducibility release status — review branch

## Verified from the archived CAP500 data in the assembled v1.1.0 package

- 103,992 factorial records = 619 future cells × 7 models × 2 SSPs × 3 directly evaluated windows × 4 states.
- C0L0/C1L0/C0L1/C1L1 contrasts close with a recorded maximum absolute residual of 1.1102230246251565e-16.
- The 2061–2080* period is estimated, not a fourth native period in CAP500 data.
- The assembled v1.1.0 compact package contains additional integration/reimplementation files and integrity manifests; it is a **separate package**, not automatically equivalent to the contents of this review branch.

## Files added in this GitHub review update

- Corrected journal-neutral README, study alignment, run order, release-status, data-availability and citation metadata.
- Executable directly evaluated CAP500 structural/closure scripts.
- Current reported Table 2 transcribed to `reference_outputs/current_reported/`; this is evidence to inspect, **not an independently reproduced table**.
- Current study parameter/period record.

## Important limits not concealed

The original RAW and Direct-Hou row-level tables, historical training and outer-fold prediction artifacts, exact model pickle, boundary GIS vector, WorldPop cell-level table, and some legacy source scripts were **not present** in the supplied compact repository ZIP used to assemble v1.1.0. GitHub should not claim they exist merely because older manifests mention them.

The original 2061–2080 emulation execution file was also not provided in the input material; a separately prepared integration script reimplemented Supplement S15, but it is not identical to an independently recovered original analysis script.

The Zenodo DOI cited in the manuscript is 10.5281/zenodo.22713203. DOI metadata may be recorded for consistency, but the existence and exact contents of its public deposit must be checked independently.

Do not mark this branch as a fully deposited archival release until the missing materials are addressed or the final archive scope is explicitly limited.
