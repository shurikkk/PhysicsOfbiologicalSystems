import matplotlib.pyplot as plt
import numpy as np

a = np.genfromtxt('HIVseries.csv', delimiter=',')

# Fit
n_v0 = 1.061e5
X = 1.674e5
k_v = 1.292
k_1 = 0.43


def my_fit(_x):
    return (n_v0-X)*np.exp(-k_v*_x) + X*np.exp(-k_1*_x)


fit_y = [my_fit(_x) for _x in a[:, 0]]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogy(a[:, 0], a[:, 1], 'bo')
ax.semilogy(a[:, 0], fit_y)
# ax.plot(t, n, 'bo')
plt.xlabel('t')
plt.ylabel('N')
plt.title('Number of virions as a function of time')
plt.show()
