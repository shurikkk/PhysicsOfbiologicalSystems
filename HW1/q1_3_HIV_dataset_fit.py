import matplotlib.pyplot as plt
import numpy as np

a = np.genfromtxt('HIVseries.csv', delimiter=',')

cut_off_i = 9
fit_func = np.poly1d(np.polyfit(a[cut_off_i:, 0], np.log(a[cut_off_i:, 1]), 1,
                                rcond=None, full=False, w=None, cov=False))
fit_y = [fit_func(_x) for _x in a[:, 0]]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(a[:, 0], np.log(a[:, 1]), 'bo')
ax.plot(a[cut_off_i:, 0], fit_y[cut_off_i:])
# ax.plot(t, n, 'bo')
plt.xlabel('t')
plt.ylabel('Log[N]')
plt.title('Number of virions as a function of time')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(a[:, 0], a[:, 1], 'bo')
ax.plot(a[cut_off_i:, 0], np.exp(fit_y[cut_off_i:]))
# ax.plot(t, n, 'bo')
plt.xlabel('t')
plt.ylabel('N')
plt.title('Number of virions as a function of time')
plt.show()

print("X, k_v are: ", np.exp(fit_func[0]), -fit_func[1])
