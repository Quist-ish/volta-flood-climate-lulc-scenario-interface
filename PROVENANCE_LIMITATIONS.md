# Scope and provenance limitations

1. **Archive boundaries:** The public GitHub repository and the separately assembled compact v1.1.0 ZIP do not automatically contain the full historical project directory. Older checklists naming absent model files, raw observation exports, or GIS inputs are not evidence those bytes were uploaded.
2. **Direct versus estimated periods:** Three IPCC-assessment periods were directly evaluated; the 2061–2080* period was constructed by interpolation–emulation. The estimated period must not be mixed into a 103,992-row direct-period table as though it were an archived fourth climate simulation.
3. **Interfaces:** Harmonized and Direct-Hou share climate forcing but use different future-LULC translation. Direct-Hou is an unharmonized sensitivity/stress test, not a physically validated alternative.
4. **Validation scope:** The UNOSAT 2023 check has only six supported cells; it is descriptive local spatial ranking, not basin-wide or hydraulic validation.
5. **Statistical nature:** The fitted random forest predicts satellite-derived flood occurrence conditional on sampled event years; the factorial attribution partitions a statistical response surface, not hydrological mass balance or causal fractions.
6. **Concept drift:** Extrapolation and covariate-shift checks cannot non-circularly establish the future flood-response relation without future observed flood labels.
7. **Reuse:** Third-party source data and derived products may have licensing/distribution constraints. Code licenses do not override those terms.
