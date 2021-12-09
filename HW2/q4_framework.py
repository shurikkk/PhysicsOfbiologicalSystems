import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


def generate_free_energy(x, x0, L, zeta=1, D=1):
    y = 12 * (1 / 4 * np.power(((x - x0) / (40 * L)), 4) - 1 / 2 * np.power(((x - x0) / (40 * L)), 2))*zeta*D
    return y


def generate_step_probability(x, x0, L):
    # if x <= 0:
    #     return 1
    # if x >= 100 * L:
    #     return 0
    du = 3/10*(np.power(((x-x0)/(40*L)), 3) - np.power(((x-x0)/(40*L)), 1))
    p_plus = 1/2*(1-du/2)
    p_plus[np.where(x <= 0)] = 1
    p_plus[np.where(x >= 100 * L)] = 0
    return p_plus


def create_intervals(L, n):
    return np.linspace(0, 100 * L, n)


def generate_rate_table(x0, L, n):
    x = create_intervals(L, n)
    table = generate_step_probability(x, x0, L)
    return table


def simulate_steps(x0, L, x_start, n_intervals, n_steps):
    intervals = create_intervals(L, n_intervals + 1)
    table = generate_rate_table(x0, L, n_intervals + 1)
    i_start = np.searchsorted(intervals, x_start)

    pos_hist = np.zeros(n_steps, dtype=np.int)
    steps_prob = np.random.uniform(0, 1, n_steps)

    current_i = i_start
    for i, prob in enumerate(steps_prob):
        pos_hist[i] = current_i
        if prob < table[current_i]:
            # current_i = min(100, current_i+i)
            current_i += 1
        else:
            # current_i = max(0, current_i-1)
            current_i -= 1

    return pos_hist, intervals[pos_hist]
