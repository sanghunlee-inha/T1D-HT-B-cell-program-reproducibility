#!/usr/bin/env python
"""Check only the explicitly computable summary-level anchor."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
f=ROOT/'results/SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv'
if not f.exists(): raise SystemExit('HOLD: run scripts/01_t1d_random_effects_meta.py first')
df=pd.read_csv(f,sep='\t');x=df.set_index('pathway').loc['B_CELL']
ref={'meta_hedges_g':0.5147161197211815,'meta_ci_low':0.17788496253154312,'meta_ci_high':0.8515472769108199,'meta_p':0.0027435328887971456,'meta_q_BH':0.021948263110377165,'I2_percent':0.0}
for k,v in ref.items():
    ok=abs(float(x[k])-v)<1e-10
    print(f'{k}: {"PASS" if ok else "FAIL"}; observed={x[k]}; retained_reference={v}')
    if not ok: raise SystemExit(2)
print('PASS: retained SUMMARY-LEVEL T1D meta-analysis only; remaining analyses NOT evaluated')
