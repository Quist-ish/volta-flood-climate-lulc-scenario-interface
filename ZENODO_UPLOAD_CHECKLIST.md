# Zenodo deposit checklist

## What to upload

Upload this single, complete package (the same contents you are reading
right now) as one Zenodo record. It already contains everything the
manuscript's Data and Code Availability statements commit to providing:
the versioned analysis pipeline, environment/version manifests, the
fitted-model and corrected-factorial checksums, the predictor-correlation
matrix, the harmonized/Direct-Hou applicability table, and the exact
locked analysis geometry.

There is no separate historical-archive tier to assemble. An earlier
draft of this checklist assumed several additional local `.rar`/`.zip`
archives and a Windows-only collection script would supply original
development-stage files; that assumption did not match the author's
actual local file organization and has been removed. Nothing is lost by
this: the manuscript never promises those files, only the versioned
pipeline and diagnostic tables that are already here and verified (see
`RELEASE_STATUS.md`).

## Before publishing

- [ ] Confirm the one open item in `RELEASE_STATUS.md` (the WorldPop
      file discrepancy) is resolved on the author's side.
- [ ] Confirm third-party data licenses before redistributing any raw
      provider files (see `DATA_LICENSE_NOTICE.md`). Do not apply the
      repository's MIT license to third-party data.
- [ ] Reserve or obtain the Zenodo DOI, then replace `DOI_PENDING` in
      `CITATION.cff`, `.zenodo.json`, and `README.md`.
- [ ] Add the Zenodo DOI to the manuscript's Data Availability statement
      (see `DATA_AVAILABILITY_STATEMENT_FOR_MANUSCRIPT.txt`), replacing
      "available from the corresponding author" with the public DOI.

## Recommended Zenodo metadata

**Title:** Volta Basin Objective 3: climate-land-use flood-occurrence reproducibility archive

**Resource type:** Software (or Dataset, if the analysis-ready data should
be the primary object — linked software and dataset records are also an
option if Zenodo's interface makes that convenient).

**Creator:** Ishmeal Quist

**Description:** Code, analysis-ready data, the fitted model, and
reproducibility diagnostics supporting a four-state climate x land-use
counterfactual analysis of future flood-occurrence probability across
the transboundary Volta Basin, evaluated under two competing scenario
interfaces (MODIS-Hou harmonized and Direct-Hou).

**Keywords:** Volta Basin; flood occurrence; CMIP6; land-use change;
machine learning; counterfactual decomposition; scenario-interface
uncertainty; reproducibility.

## GitHub linkage

Unzip this package into a clean GitHub repository at
`github.com/Quist-ish/volta-flood-climate-lulc-scenario-interface` (or
your preferred name), push it as the initial commit, tag a release
(e.g., `v1.0.0`), then connect the repository to Zenodo's GitHub
integration to mint the DOI from that tagged release.
