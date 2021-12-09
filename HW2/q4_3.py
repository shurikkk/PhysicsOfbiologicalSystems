import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from q4_framework import generate_rate_table, create_intervals, generate_free_energy, simulate_steps
import seaborn as sns


L = 10
x0 = 50 * L
number_of_intervals = 100
intervals = create_intervals(L, number_of_intervals + 1)
table = generate_rate_table(x0, L, number_of_intervals + 1)
table_function = generate_free_energy(intervals, x0, L)
# sphere_radius = 0.1
sphere_radius = 0.0
point_function = table_function + sphere_radius

n = 7000
# n = 70
x_start = 10*L
i_start = np.searchsorted(intervals, x_start)

pos_hist, x_hist = simulate_steps(x0, L, x_start, number_of_intervals, n)
fig, ax = plt.subplots()
# sns.histplot(data=x_hist, stat='count')
# fig.savefig('q4_3.png')
#
# fig.clear()

# plt.xlabel('x')
# plt.ylabel('U/kT')
# plt.plot(intervals, table_function, label="Free energy")
# points, = ax.plot(intervals[i_start], point_function[i_start], 'o')


def animate_point(frame_i, *fargs):
    current_i = pos_hist[frame_i]
    # points.set_xdata(intervals[current_i])
    # points.set_ydata(point_function[current_i])
    ax.clear()
    plt.xlabel('x')
    plt.ylabel('U/kT')
    plt.plot(intervals, table_function, label="Free energy")
    ax.plot(intervals[current_i], point_function[current_i], 'o')
    return pos_hist,


ani = animation.FuncAnimation(fig, animate_point, frames=n, fargs=(), interval=1)
ani.save('q4_simulation.mp4', fps=30)
# ani.save('q4_simulation.gif', writer='imagemagick')
