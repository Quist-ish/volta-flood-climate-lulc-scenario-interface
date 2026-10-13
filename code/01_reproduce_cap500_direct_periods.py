#!/usr/bin/env python3
"""Recompute CAP500 direct-period factorial closure and area-weighted contrasts."""
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/"data/analysis_ready/CAP500_FACTORIAL_PREDICTIONS.csv.gz"
OUT=ROOT/"generated_outputs"
OUT.mkdir(exist_ok=True)
d=pd.read_csv(IN)
KEY=["climate_model","scenario","period","cell_id"]
p=d.pivot_table(index=KEY,columns="state",values="prob_cap500")
assert set(["C0L0","C1L0","C0L1","C1L1"]).issubset(p.columns)
p["dC"]=p.C1L0-p.C0L0
p["dL"]=p.C0L1-p.C0L0
p["dI"]=p.C1L1-p.C1L0-p.C0L1+p.C0L0
p["combined"]=p.C1L1-p.C0L0
res=(p.combined-(p.dC+p.dL+p.dI)).abs().max()
assert res<2e-15,res
area=d[d.state=="C0L0"].drop_duplicates("cell_id").set_index("cell_id").cell_area_km2
q=p.reset_index()
q["area"]=q.cell_id.map(area)
columns=["dC","dL","dI","combined"]
def summarize(x):
    return pd.Series({k:np.average(x[k],weights=x.area) for k in columns})
m=q.groupby(["climate_model","scenario","period"]).apply(summarize)
m.to_csv(OUT/"CAP500_model_level_direct_periods.csv")
h=m.groupby(["scenario","period"]).median()
total=h.dC.abs()+h.dL.abs()+h.dI.abs()
h["climate_share_pct"]=h.dC.abs()/total*100
h["lulc_share_pct"]=h.dL.abs()/total*100
h["interaction_share_pct"]=h.dI.abs()/total*100
h.to_csv(OUT/"CAP500_basin_headline_direct_periods.csv")
print("PASS: direct-period four-state maximum absolute closure residual =",format(res,".17g"))
print("Area (intersection km^2):",round(area.sum(),3))
print(h.round(6).to_string())
print("NOTE: Results are CAP500 archived-prediction summaries, not new model refits.")
