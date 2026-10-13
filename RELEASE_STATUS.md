# Reproducibility status — current public repository (13 October 2026)

**PASS — compact CAP500 CI.** PR #2 merged to main. GitHub Actions run [38378290970](https://github.com/Quist-ish/volta-flood-climate-lulc-scenario-interface/actions/runs/38378290970) succeeded with archived-input, recomputation, structure and artifact-upload checks.

**PASS — local archive integrity.** 58/58 checksums matched. CAP500 = 103,992 rows from 619 × 7 × 2 × 3 × 4; maximum absolute four-state closure residual 1.1102230246251565e-16; basin area 410,991.544 km².

**RAN, NOT EXACT MATCH — analytical reimplementations.** Estimated 2061–2080* and eight-experiment spatial meta-learning were executed against archived CAP500 inputs. They did not reproduce all reported rounded statistics exactly. See [REPRODUCIBILITY_AUDIT_2026-10-13.md](REPRODUCIBILITY_AUDIT_2026-10-13.md).

**NOT YET VERIFIED — public Zenodo archive.** Manuscript-reported DOI 10.5281/zenodo.22713203 could not be independently resolved through attempted Zenodo, DOI or DataCite retrieval; this does not prove absence but blocks a verified-record claim.

**MISSING — complete original analysis.** Full original RAW/Direct-Hou row predictions; historical model training and out-of-fold files; exact frozen classifier/model artifact; original 2061 analysis code; some GIS, exposure and source validation materials.

**Interpretation:** verified *partial* reproducibility from already archived factorial predictions; not full re-execution of the original experiment or direct verification of the permanent archive.

All missing-file claims have been limited to items actually absent from the supplied compact archives. No scientific result was altered.
