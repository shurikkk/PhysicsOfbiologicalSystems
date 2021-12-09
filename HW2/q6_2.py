import numpy as np
import matplotlib.pyplot as plt
from q6_framework import log_likelihood_cauchy
import seaborn as sns

y = np.load('djiweekly.npy')
mu_N = 200
eta_N = 100
mu_y = np.linspace(0, 2*np.mean(y), mu_N)
eta = np.linspace(0.015, 0.035, eta_N)
# mu_y = np.linspace(2000, 6000, mu_N)
# eta = np.linspace(1000, 6000, eta_N)

res = np.zeros((mu_N, eta_N))
for i in range(mu_N):
    for j in range(eta_N):
        res[i][j] = log_likelihood_cauchy((mu_y[i], eta[j]), y)

fig, ax = plt.subplots()
im = ax.pcolormesh(mu_y, eta, res.transpose(), shading='auto')
fig.colorbar(im, ax=ax)
plt.xlabel('mu_y')
plt.ylabel('eta')
plt.show()
