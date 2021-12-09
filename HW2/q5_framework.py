import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


def generate_free_energy(x, L, zeta=1, D=1):
    y = 0.0025*zeta*D*np.power((x/L-50), 2)
    return y


def generate_step_probability(x, L):
    # if x <= 0:
    #     return 1
    # if x >= 100 * L:
    #     return 0
    du = 0.005/L*(x/L-50)
    p_plus = 1/2*(1-du/2)
    p_plus[np.where(x <= 0)] = 1
    p_plus[np.where(x >= 100 * L)] = 0
    return p_plus


def create_intervals(L, n):
    return np.linspace(0, 100 * L, n)


def generate_rate_table(L, n):
    x = create_intervals(L, n)
    table = generate_step_probability(x, L)
    return table


def simulate_steps(L, x_start, n_intervals, n_steps):
    intervals = create_intervals(L, n_intervals + 1)
    table = generate_rate_table(L, n_intervals + 1)
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


def calculate_autocorrelation(t, simulation_res, T, dt):
    start_i = np.where(t >= T)[0][0]
    dt = t[1] - t[0]
    # start_t = t[end_i]
    s_len = len(simulation_res) - start_i
    s = np.zeros(s_len)
    a = np.zeros(s_len)
    for i in range(-int(s_len/2), int(s_len/2)):
        new_i = int(s_len/2) + i
        s[new_i] = dt*i
        corr = dt/T * np.inner(simulation_res[int(s_len/2):len(simulation_res)-int(s_len/2)],
                               simulation_res[int(s_len/2)-i:len(simulation_res)-int(s_len/2)-i])
        a[new_i] = corr
    return s, a


def calculate_power_spectrum(s, a):
    ds = s[1] - s[0]
    S = s[-1] - s[0]
    ps = np.fft.fft(a)
    f = np.fft.fftfreq(len(a), d=ds)
    ps = 2*ds/S*ps[np.where(f >= 0)]
    ps[0] = ps[0] / 2
    f = f[np.where(f >= 0)]
    # def manual_fft(f):
    #     return 2*ds/S * np.sum(s*np.exp(1j*2*np.pi*s*f))
    # res2 = manual_fft(0)
    # res3 = manual_fft(1)
    return f, np.abs(ps)


def find_corner_f(f, ps):
    f_c = f[np.where(ps <= 0.5*max(ps))][0]
    return f_c

