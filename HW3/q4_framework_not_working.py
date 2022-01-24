import numpy as np
import matplotlib.pyplot as plt


def simulate(lini, T, beta_start, beta_stop, beta_s, k):
    t = 0
    l = lini
    ts = []
    ls = []
    ts.append(t)
    ls.append(l)
    is_active = True
    # active_sequence = [(0, is_active)]
    active_sequence = []
    t = 0
    dt_active = []
    dt_inactive = []
    while t < T:
        if is_active is False:
            # next_t = np.random.exponential(1/beta_start)
            next_t = np.random.exponential(1/beta_stop)
            is_active = True
            dt_active.append(next_t)
        else:
            # next_t = np.random.exponential(1/beta_stop)
            next_t = np.random.exponential(1/beta_start)
            is_active = False
            dt_inactive.append(next_t)
        t += next_t
        active_sequence.append((t, is_active))

    # We start the process from the first time the transition is on
    t = 0
    active_i = 0
    while t < T:
        copy_t = t
        next_t_gene_indicator, is_active = active_sequence[active_i]
        while copy_t >= next_t_gene_indicator:
            if active_i < len(active_sequence):
                active_i += 1
                next_t_gene_indicator, is_active = active_sequence[active_i]
            else:
                is_active = not is_active
                break
        beta = beta_s if is_active else 0
        # beta = beta_s
        rate = beta + k*l
        # rate = beta_s + k*l
        if rate == 0:
            # We have both l == 0 and is_active is false, thus we propagate time to the next event when the system is
            # reproducing
            t = next_t_gene_indicator
            continue
        next_dt = np.random.exponential(1/rate)
        # next_dt = np.random.exponential(rate)
        t += next_dt

        if t >= next_t_gene_indicator:
            active_i += 1

        xi = beta / rate
        next_event = np.random.choice([1, -1], p=[xi, 1-xi])
        l += next_event
        if l < 0:
            l = 0
        ts.append(t)
        ls.append(l)

    return np.array(ts), np.array(ls)


if __name__ == '__main__':
    # beta = 15
    # beta = 1.5
    # beta = 0.15
    # k = 0.014
    m = 5
    beta_start = 1/37
    beta_stop = 1/6
    beta_s = m*beta_start
    # beta_s = m*beta_stop
    k = np.log(2)/50
    l_ini = 0
    # T_s = 1600
    T_s = 300
    for i in range(3):
        ts, ls = simulate(l_ini, T_s, beta_start, beta_stop, beta_s, k)
        l_th = (1 - np.exp(-k * ts)) * beta_start*m / k
        plt.figure()
        plt.plot(ts, ls, label=r'${<\ell>}$')
        plt.plot(ts, l_th, label=r'${\ell_{th}}$')
        plt.xlabel('t')
        plt.ylabel('${\\ell}$')
        plt.legend()
        plt.show()
