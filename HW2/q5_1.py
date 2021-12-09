import numpy as np
import matplotlib.pyplot as plt
from q5_framework import generate_rate_table, create_intervals, simulate_steps, calculate_autocorrelation, \
    calculate_power_spectrum
import seaborn as sns

L = 5
n = 10000
t_max = 5
D = n*np.power(L, 2)/(2*t_max)
number_of_intervals = 100
intervals = create_intervals(L, number_of_intervals + 1)
table = generate_rate_table(L, number_of_intervals + 1)
x_start = 50*L
# x_start = 0
i_start = np.searchsorted(intervals, x_start)
T = 0.94*t_max
dt = t_max / n

t = np.linspace(0, t_max, n)
pos_hist, x_hist = simulate_steps(L, x_start, number_of_intervals, n)
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
plt.figure()
plt.plot(f, ps, '.')
plt.xlabel('f')
plt.ylabel('C')
plt.xscale('log')
plt.yscale('log')
plt.show()
