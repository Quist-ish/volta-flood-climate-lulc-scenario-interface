#!/usr/bin/env python3
"""Verify the archived CAP500 support present in the current GitHub repository."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"data/analysis_ready/CAP500_FACTORIAL_PREDICTIONS.csv.gz"
if not p.exists():
    raise SystemExit(f"Missing archived CAP500 file: {p}")
d=pd.read_csv(p,usecols=["cell_id","climate_model","scenario","period","state"])
assert len(d)==619*7*2*3*4,(len(d),103992)
assert d.cell_id.nunique()==619
assert d.climate_model.nunique()==7
assert set(d.scenario)=={"ssp245","ssp585"}
assert set(d.period)=={"near_2021_2040","mid_2041_2060","late_2081_2100"}
assert set(d.state)=={"C0L0","C1L0","C0L1","C1L1"}
assert d.groupby(["climate_model","scenario","period","cell_id"]).state.nunique().eq(4).all()
print("PASS: 103,992 CAP500 rows; 619 cells; 7 models; 2 SSPs; 3 direct periods; 4 states.")
print("NOTE: the fourth (2061–2080*) period is estimated, not part of native CAP500 data.")
