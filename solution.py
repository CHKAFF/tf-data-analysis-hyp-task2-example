import numpy as np
from scipy.stats import kruskal, wilcoxon, mannwhitneyu, ks_2samp

chat_id = 303247798

def solution(x: np.array, y: np.array) -> bool:
    _, pval_K = kruskal(x, y)
    _, pval_W = wilcoxon(x, y)
    _, pval_M = mannwhitneyu(x, y)
    _, pval_L = ks_2samp(x, y)
    return pval_K < 0.1 or pval_W < 0.1 or pval_M < 0.1 or pval_L < 0.1
