import numpy as np


def prob(n):
    r = np.random.uniform(0, 1, n)
    y = np.exp(r)
    return y
