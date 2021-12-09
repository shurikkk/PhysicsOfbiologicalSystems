import numpy as np
import matplotlib.pyplot as plt
from q5_framework import generate_rate_table, create_intervals, simulate_steps
import seaborn as sns

L = 1
D = 1000
number_of_intervals = 1000
intervals = create_intervals(L, number_of_intervals + 1)
table = generate_rate_table(L, number_of_intervals + 1)
n = 70000
x_start = 50*L
# x_start = 0
i_start = np.searchsorted(intervals, x_start)
t_max = n*np.power(L, 2)/(2*D)

pos_hist, x_hist = simulate_steps(L, x_start, number_of_intervals, n)
t = np.linspace(0, t_max, n)
plt.plot(x_hist, t)
plt.xlabel('x')
plt.ylabel('t')
# sns.histplot(data=x_hist, stat='count')
# ax.set_xlim(0, 100 * L)
plt.show()
