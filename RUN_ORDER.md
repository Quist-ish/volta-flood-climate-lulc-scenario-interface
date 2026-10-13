# Available reproduction commands

Use Python from the **repository root**, not from inside `code/`.

```bash
python -m pip install -r requirements.txt
python code/00_verify_public_repository.py
python code/01_reproduce_cap500_direct_periods.py
```

The verification script checks 103,992 archived CAP500 state rows with 619 unique cells, seven CMIP6 models, two scenarios, three *directly evaluated* periods, and all four counterfactual states.

The second command recomputes the CAP500 C0L0/C1L0/C0L1/C1L1 decomposition and saves model-level and basin-median summaries to `generated_outputs/`.

### Not part of the present branch smoke test

- **2061–2080***: supplementary S15 interpolation–emulation *estimate*, not a native archived fourth period.
- Direct-Hou: the complete original row-level counterfactual predictions are not available in the compact GitHub data currently present.
- Historical refitting, external observations, reservoir/UNOSAT context and Tree SHAP: their complete original artifacts were not supplied to this public branch.
- Spatial meta-learning: the reported eight-experiment output depends in part on the 2061–2080 estimated cells; the full slow reproduction implementation belongs to the separately assembled package.

For manuscript-reported values consult `reference_outputs/current_reported/`. Do **not** treat copied reported values as regenerated calculations.
