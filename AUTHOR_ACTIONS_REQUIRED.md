# Author material required for complete reproduction

The automated CAP500 test **passed**. No further manual execution of that test is needed.

The following materials are **not in the supplied compact source archives** and cannot be recreated without changing the evidence:

- Original RAW and Direct-Hou full four-state, per-cell/per-model/per-SSP/per-period prediction outputs (with state definitions and upstream feature tables).
- Original historical model training features, event-year folds and out-of-fold predictions; fitted random-forest model with its exact environment.
- Final original 2061–2080 interpolation/emulation script (including random seeds, clips, postprocessing, and output precision).
- Final original spatial meta-learning / S19 generation script (including threshold tie-breaks and exact split assignment).
- Exact basin boundary GIS files, observation support exports and WorldPop 2020 cell table as required by the reported analysis.
- A publicly accessible Zenodo record page or record export for the manuscript-cited DOI `10.5281/zenodo.22713203`, plus the frozen deposited files/checksums.

Provide the above originals (or an accessible immutable versioned archive) to complete an exact end-to-end reconciliation. Avoid putting undocumented replacement values into the main submission.

**Version control:** retain these author-supplied originals alongside the current verified CAP500 archive, with hashes; label any revised or reconstructed scripts separately. See [audit](REPRODUCIBILITY_AUDIT_2026-10-13.md).
