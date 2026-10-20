#!/usr/bin/env python
"""Recalculate the historical summary-level meta-analysis from retained effect estimates."""
import sys
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from t1d_ht_bcell.stats import dersimonian_laird,bh_adjust

def main():
    table=pd.read_csv(ROOT/'data/derived/t1d_pathway_cohort_effects.tsv',sep='\t')
    assert table.shape==(24,6),f'Expected 24 pathway/cohort entries; found {table.shape}'
    assert all(g.cohort.nunique()==3 for _,g in table.groupby('pathway'))
    rows=[]
    for pathway,g in table.groupby('pathway'):
        row=dersimonian_laird(g.hedges_g,g.var_g)
        rows.append({'pathway':pathway,**row})
    out=pd.DataFrame(rows)
    out['meta_q_BH']=bh_adjust(out.meta_p)
    results=ROOT/'results';results.mkdir(exist_ok=True)
    out.to_csv(results/'SYSTEMIC_PATHWAY_RANDOM_EFFECTS_META.tsv',sep='\t',index=False)
    print(out.to_string(index=False));print('Saved summary-level results.')
if __name__=='__main__':main()
