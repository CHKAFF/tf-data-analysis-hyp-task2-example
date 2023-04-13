import numpy as np
from scipy.stats import ks_2samp

chat_id = 303247798

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = ks_2samp(x, y)
    return p_value < 0.1
