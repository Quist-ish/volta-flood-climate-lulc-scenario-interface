#!/usr/bin/env python3
"""Run only checks whose required input files are present on this review branch."""
from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parent
for name in ["00_verify_public_repository.py","01_reproduce_cap500_direct_periods.py"]:
    subprocess.run([sys.executable,str(r/name)],check=True)
print("Direct-period compact checks complete; see RELEASE_STATUS.md for un-reproduced analysis stages.")
