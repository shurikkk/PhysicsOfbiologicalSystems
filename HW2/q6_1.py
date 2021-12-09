import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from q6_framework import minus_log_likelihood_cauchy
import seaborn as sns

y = np.load('djiweekly.npy')
# start_mu_y = 0
# start_eta = 0.2
# print(-minus_log_likelihood_cauchy((start_mu_y, start_eta), y))
start_mu_y = 0.0001
start_eta = 0.035

res = minimize(minus_log_likelihood_cauchy, np.array([start_mu_y, start_eta]), args=(y,),
               bounds=np.array([(None, None), (1e-9, None)]),
               # gtol=1e-8,
               )
print(res)
