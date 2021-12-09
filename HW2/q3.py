import numpy as np

n = 50000
beta = 6
# Check whether we converge into the right formula
mu = np.random.exponential(1/beta, size=n)
print(np.average(mu))
k = [np.random.poisson(lam) for lam in mu]
sample_avg = np.average(k)
theory_avg = 1/beta
print("Sample of {n}: theory average {a_th}, sample average: {a_s}".format(n=n, a_th=theory_avg, a_s=sample_avg))
