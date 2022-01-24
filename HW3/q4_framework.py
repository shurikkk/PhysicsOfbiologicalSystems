import numpy as np
import matplotlib.pyplot as plt


def simulate(lini, T, beta_start, beta_stop, beta_s, k, number_of_genes=1, n_0=0, split_rate=1/50):
    n_0_rate = n_0 * split_rate
    t = 0
    l = lini
    ts = []
    ls = []
    ts.append(t)
    ls.append(l)

    # We start the process from the first time the transition is on
    t = 0
    n = 0
    number_active = 0
    number_inactive = number_of_genes
    # Only one initial inactive gene is exists
    while t < T:
        beta = beta_s * number_active
        # beta = beta_s
        beta_deact = beta_stop * number_active
        beta_act = beta_start * number_inactive
        clearance_rate = k*l
        rate = beta + clearance_rate + beta_act + beta_deact + n_0_rate
        next_dt = np.random.exponential(1/rate)
        # next_dt = np.random.exponential(rate)
        t += next_dt

        p_copy = beta / rate
        p_erase = clearance_rate / rate
        p_act = beta_act / rate
        p_deact = beta_deact / rate
        p_split = n_0_rate / rate

        next_event = np.random.choice(['inc', 'dec', 'act', 'deact', 'spl'],
                                      p=[p_copy, p_erase, p_act, p_deact, p_split])
        if next_event == 'inc':
            l += 1
        elif next_event == 'dec':
            l -= 1
        elif next_event == 'act':
            # We switch gene active status
            number_active += 1
            number_inactive -= 1
            # l += 1
        elif next_event == 'deact':
            # We switch gene active status
            number_active -= 1
            number_inactive += 1
        elif next_event == 'spl':
            n += 1
            if n_0 != 0:
                if n - 1 < 0.3 * n_0 <= n:
                    # Duplicate the number of gene copies, all the new one are in a new state
                    number_inactive += number_active + number_inactive
                elif n - 1 < n_0 <= n:
                    # Number of gene copies are reset to original value
                    number_active = 0
                    number_inactive = number_of_genes
                    l = sum(np.random.randint(0, 2, l))
                    n = 0

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
