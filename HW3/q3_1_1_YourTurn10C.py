import numpy as np
import matplotlib.pyplot as plt


def simulate(lini, T, beta, k):
    t = 0
    l = lini
    ts = []
    ls = []
    ts.append(t)
    ls.append(l)
    while t < T:
        rate = beta + k*l
        next_dt = np.random.exponential(1/rate)
        t += next_dt
        xi = beta / rate
        next_event = np.random.choice([1, -1], p=[xi, 1-xi])
        l += next_event
        ts.append(t)
        ls.append(l)

    return np.array(ts), np.array(ls)


if __name__ == '__main__':
    # beta = 15
    # beta = 1.5
    # beta = 0.15
    # k = 0.014
    beta = 5
    k = 1
    l_ini = 0
    # T_s = 1600
    T_s = 300
    for i in range(3):
        ts, ls = simulate(l_ini, T_s, beta, k)
        l_th = (1 - np.exp(-k * ts)) * beta / k
        ss = np.ones(len(ts)) * beta / k
        plt.figure()
        plt.plot(ts, ls, label=r'${<\ell>}$')
        plt.plot(ts, ss, label=r'${\ell_{ss}}$')
        plt.plot(ts, l_th, label=r'${\ell_{th}}$')
        plt.xlabel('t')
        plt.ylabel('${\\ell}$')
        plt.legend()
        plt.show()
