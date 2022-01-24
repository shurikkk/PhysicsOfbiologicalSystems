import numpy as np
import matplotlib.pyplot as plt
from q3_1_1_YourTurn10C import simulate


# beta = 1.5
beta = 0.15
k = 0.014
# beta = 5
# k = 1
# n = 150
n = 150
l_init = 0
T = 600
n_t = int(T/beta)
t_s = np.linspace(0, T, n_t)
l_avg = np.zeros(n_t)
raw_res = [simulate(l_init, T, beta, k) for _ in range(n)]
for i, t in enumerate(t_s):
    tmp_l = []
    for t_simulation, l_simulation in raw_res:
        alpha = np.argmax(t_simulation > t)
        tmp_l.append(l_simulation[alpha-1])
    l_avg[i] = np.mean(tmp_l)

ss = np.ones(n_t) * beta/k
l_th = (1-np.exp(-k*t_s)) * beta/k

plt.figure()
plt.plot(t_s, l_avg, label=r'${<\ell>}$')
plt.plot(t_s, ss, label=r'${\ell_{ss}}$')
plt.plot(t_s, l_th, label=r'${\ell_{th}}$')
plt.xlabel('t')
plt.ylabel('${<\\ell>}$')
plt.legend()
plt.title('Average ${\\ell}$ over ' + '{n} '.format(n=n) + 'realizations')
plt.show()
