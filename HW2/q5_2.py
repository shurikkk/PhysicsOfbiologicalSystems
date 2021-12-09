import numpy as np
import matplotlib.pyplot as plt
from q5_framework import calculate_autocorrelation, calculate_power_spectrum, find_corner_f
# import seaborn as sns

L = 5
n = 10000
t_max = 5
D = n*np.power(L, 2)/(2*t_max)
T = 0.994*t_max
dt = t_max / n

x_hist = np.loadtxt('vanMameren.txt')
x_start = x_hist[0]
t = np.linspace(0, t_max, len(x_hist))

plt.figure()
plt.plot(t, x_hist-x_start)
plt.xlabel('t')
plt.ylabel('x')
plt.show()

s, ac = calculate_autocorrelation(t, x_hist-x_start, T, dt)
plt.figure()
plt.plot(s, ac)
plt.xlabel('s')
plt.ylabel('A')
plt.show()

T = 100/n*t_max
s, ac = calculate_autocorrelation(t, x_hist-x_start, T, dt)

f, ps = calculate_power_spectrum(s, ac)
# f_c = find_corner_f(f, ps)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(f, ps, '.')

plt.xlabel('f')
plt.ylabel('C')
plt.xlim([1e-1, 1e3])
plt.ylim([1e-1, 1e3])
plt.xscale('log')
plt.yscale('log')
# ax.axvline(x=f_c, alpha=0.8, ymax=0.8, linestyle=":")
# ax.text((f_c+3)/max(f), 0.85, "f_c", size=11, alpha=0.85)
plt.show()
print('bla')
