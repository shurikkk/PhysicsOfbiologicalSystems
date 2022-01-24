import numpy as np
import matplotlib.pyplot as plt
from q3_1_1_YourTurn10C import simulate


panelA1 = np.load('panelA1.npy')
panelA2 = np.load('panelA2.npy')
panelA3 = np.load('panelA3.npy')
panelC = np.load('panelC.npy')
panelD1 = np.load('panelD1.npy')
panelD2 = np.load('panelD2.npy')
panelD3 = np.load('panelD3.npy')

# beta = 1.5
beta = 0.15
k = 0.014
# beta = 5
# k = 1
n = 150
# n = 600
l_init = 0
T = 600
n_t = int(T/beta)
t_s = np.linspace(0, T, n_t)
l_avg = np.zeros(n_t)
zero_copy_p = np.zeros(n_t)
raw_res = [simulate(l_init, T, beta, k) for _ in range(n)]
for i, t in enumerate(t_s):
    still_zero = np.zeros(n)
    tmp_l = np.zeros(n)
    for j, (t_simulation, l_simulation) in enumerate(raw_res):
        alpha = np.argmax(t_simulation > t)
        tmp_l[j] = l_simulation[alpha-1]
        if l_simulation[alpha-1] == 0:
            still_zero[j] = 1
    l_avg[i] = np.mean(tmp_l)
    zero_copy_p[i] = np.count_nonzero((tmp_l == 0) * (still_zero == 1)) / n

max_t_i = np.where(zero_copy_p <= np.exp(-3))[0][0]
log_zero_copy_p = np.log(zero_copy_p[:max_t_i])
log_zero_copy_p_th = -beta * t_s[:max_t_i]

plt.figure()
plt.plot(panelD1[:, 0], panelD1[:, 1], marker="^", linestyle="", label=r'Experimental')
plt.plot(panelD2[:, 0], panelD2[:, 1], marker="o", linestyle="", label=r'Experimental')
plt.plot(panelD3[:, 0], panelD3[:, 1], marker="*", linestyle="", label=r'Experimental')
plt.plot(t_s[:max_t_i], log_zero_copy_p, label='simulation')
plt.plot(t_s[:max_t_i], log_zero_copy_p_th, label='theory')
plt.xlabel('t')
plt.ylabel(r'$\ln\left(\mathcal{P}_{\ell\left(t\right)}\left(0\right)\right)$')
plt.legend()
plt.title('Log of probability of having zero copies over ' + '{n} '.format(n=n) + 'realizations')
plt.show()
