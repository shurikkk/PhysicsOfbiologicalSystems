import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
from q4_framework import generate_rate_table, create_intervals, generate_free_energy, simulate_steps
import seaborn as sns


L = 10
x0 = 50 * L
number_of_intervals = 100

n_steps = 7000
x_start = 10*L

n_simulations = 10000
last_x_hist = np.zeros(n_simulations)

for i in range(n_simulations):
    pos_hist, x_hist = simulate_steps(x0, L, x_start, number_of_intervals, n_steps)
    last_x_hist[i] = x_hist[-1]

fig, ax = plt.subplots()
sns.histplot(data=last_x_hist, stat='count')
fig.savefig('q4_4.png')

fig.clear()
# plt.xlabel('x')
# plt.ylabel('U/kT')
# plt.plot(intervals, table_function, label="Free energy")
# points, = ax.plot(intervals[i_start], point_function[i_start], 'o')
