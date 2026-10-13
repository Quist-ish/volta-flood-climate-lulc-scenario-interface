# Current manuscript and Supplement alignment

- **Study title:** Future land-cover translation can reverse the modeled climate–landscape attribution of flood occurrence in the transboundary Volta Basin.
- **Basin support:** 623 intersecting grid cells; 622 historical model cells; 619 future common-support cells.
- **Historical labels:** 4,354 cell-years; 520 flood positives; seven event years; 15 predictors.
- **Scenarios:** SSP2-4.5 and SSP5-8.5; seven retained climate models.
- **Windows evaluated directly:** 2021–2040, 2041–2060, 2081–2100.
- **Window estimated in the manuscript:** 2061–2080*, interpolated/emulated from bracketing periods; it is **not** a direct climate-model/frozen-random-forest evaluation.
- **Future representation:** MODIS–Hou harmonized interface (primary) and Direct-Hou substitution (stress test).
- **Four-state decomposition:** C0L0, C1L0, C0L1, C1L1, with exact algebraic closure; reported maximum residual about 1.11 × 10⁻¹⁶.
- **Spatial analysis:** eight scenario-period experiments = 619 × 2 × 4 = 4,952 cell–experiment records.
- **UNOSAT:** six-cell local descriptive case, not independent basin-wide calibration/validation.
- **Current reported main tables:** Table 2 (factorial decomposition) and Table 3 (representation mechanism); supplementary spatial/emulation diagnostics S18–S20.

**Status**: this review branch aligns the study documentation, current Table 2, and the executable *direct-period* CAP500 verification. It does not itself deposit every artifact cited in the manuscript.
