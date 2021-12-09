import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from q6_framework import log_likelihood_gaussian, minus_log_likelihood_gaussian
import seaborn as sns

y = np.load('djiweekly.npy')
start_mu_y = 0
start_sigma = 10

res = minimize(minus_log_likelihood_gaussian, np.array([start_mu_y, start_sigma]), args=(y,),
               bounds=np.array([(None, None), (1e-2, None)]),
               # gtol=1e-8,
               )
print(res)

mu_N = 200
sigma_N = 100
mu_y = np.linspace(2000, 4000, mu_N)
sigma = np.linspace(3000, 6000, sigma_N)
res = np.zeros((mu_N, sigma_N))
for i in range(mu_N):
    for j in range(sigma_N):
        res[i][j] = log_likelihood_gaussian((mu_y[i], sigma[j]), y)

fig, ax = plt.subplots()
im = ax.pcolormesh(mu_y, sigma, res.transpose(), shading='auto')
fig.colorbar(im, ax=ax)
plt.xlabel('mu_y')
plt.ylabel('sigma')
plt.show()
