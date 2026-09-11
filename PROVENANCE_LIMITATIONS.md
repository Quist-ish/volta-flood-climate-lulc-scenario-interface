# Provenance and interpretation limitations

1. **Boundary:** the locked analytical geometry is the project-local `GRDC_VOLTA_POLITICAL_TRANSBOUNDARY_BASIN` derivative associated with the GRDC Major River Basins 2020 source package. The full sequence of historical intermediate GIS edits was not recoverable. The release therefore deposits/copies the exact locked geometry rather than claiming an undocumented transformation history.
2. **Threshold:** the archived `p=0.14` operating point is not described as calibrated or cross-validation selected. Authentic outer-fold thresholds and pooled-OOF diagnostics are retained separately.
3. **Phase5E supersession:** the original Phase5E factorial feature table is audit-only; final future SHAP and scenario-response interpretation use V7 `RAW_FACTORIAL_PREDICTIONS.csv.gz`, which contains corrected R10mm/R20mm future states.
4. **LULC interface:** the harmonized MODIS–Hou implementation and Direct-Hou implementation are both scientifically informative structural representations. Direct-Hou is a sensitivity analysis, not an error condition.
5. **Observation support:** GFD observation-support sensitivity is a same-source label-support sensitivity, not independent sensor validation.
6. **Uncompleted extensions:** no clean event-matched Sentinel-1 independent-validation experiment, dynamic reservoir-operation experiment or dynamic SSP population experiment is claimed.
