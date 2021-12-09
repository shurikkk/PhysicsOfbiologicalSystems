import numpy as np
import matplotlib.pyplot as plt
from q4_framework import generate_rate_table, create_intervals, simulate_steps
# import seaborn as sns


L = 10
D = 10000
x0 = 50 * L
number_of_intervals = 100
intervals = create_intervals(L, number_of_intervals + 1)
table = generate_rate_table(x0, L, number_of_intervals + 1)
n = 7000
x_start = 10*L
i_start = np.searchsorted(intervals, x_start)

pos_hist, x_hist = simulate_steps(x0, L, x_start, number_of_intervals, n)

t = np.linspace(0, n*np.power(L, 2)/(2*D), n)
fig, ax = plt.subplots()
plt.plot(x_hist, t)
plt.xlabel('x')
plt.ylabel('t')
# sns.histplot(data=x_hist, stat='count')
# ax.set_xlim(0, 100 * L)
plt.show()
