import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
import seaborn as sns


n = 10000
mu = 1
beta = 1/mu
alpha = 1

# Uses the same method described on page 113 but in way efficient way...
t_w = np.random.exponential(beta, (alpha, n))
t_alpha = np.sum(t_w, axis=0)
fig = plt.figure()
x = np.arange(0, int(np.ceil(max(t_alpha)/beta)))
lamb = beta*alpha
fit = beta * np.exp(-beta*x)
x = x * beta
sns.histplot(t_alpha, bins=40, stat='density')
plt.xlabel('${t_\\alpha}$ [s]')
plt.ylabel('# of appearances')
plt.title('Histogram of ${\\alpha=' + '{a}'.format(a=alpha) + '}$ blips')
plt.plot(x, fit, 'r')
plt.show()

print('bla')
