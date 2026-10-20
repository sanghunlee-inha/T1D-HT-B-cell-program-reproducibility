"""Summary-level DerSimonian–Laird meta-analysis; not raw-expression processing."""
from __future__ import annotations
import numpy as np
from scipy.stats import norm
from statsmodels.stats.multitest import multipletests

def dersimonian_laird(y, v):
    y, v = np.asarray(y, float), np.asarray(v, float)
    if len(y) < 2 or y.shape != v.shape or not np.isfinite(y).all() or not np.isfinite(v).all() or (v <= 0).any():
        raise ValueError('Require at least two finite effect/positive variance pairs')
    k = len(y); w = 1/v; mu0 = np.sum(w*y)/np.sum(w)
    q = np.sum(w*(y-mu0)**2); c = np.sum(w)-np.sum(w*w)/np.sum(w)
    tau2 = max(0., (q-(k-1))/c) if c > 0 else 0.
    wr = 1/(v+tau2); mu = np.sum(wr*y)/np.sum(wr); se = np.sqrt(1/np.sum(wr))
    return {'k':k,'meta_hedges_g':float(mu),'meta_ci_low':float(mu-1.96*se),'meta_ci_high':float(mu+1.96*se),'meta_p':float(2*norm.sf(abs(mu/se))),'I2_percent':float(max(0,(q-(k-1))/q)*100 if q>0 else 0),'tau2_DL':float(tau2)}

def bh_adjust(p): return multipletests(p, method='fdr_bh')[1]
