# Data availability and redistribution

The repository contains compact analysis-ready/derived tables needed to reproduce the paper's final numerical conclusions. Very large third-party source datasets are not duplicated in the GitHub release. They must be obtained from the authoritative providers listed in `manifests/external_data_sources.csv`, using the exact product/version stated there and the original local inventory in `manifests/original_local_file_inventory.csv`.

The Zenodo audit archive may contain the author's analysis archives and derived products. Third-party source products should only be redistributed when their provider licence permits it. In particular, preserve each provider's citation and licence requirements; do not apply the repository's code licence to third-party data.

For the strictest source-to-result reproduction, run the Windows release builder on the original `D:\PROGRESS_PAPERS\3nd_Objective` tree. It creates a manifest and SHA-256 digest for every collected file and reports any expected script/data artifact it cannot find.
