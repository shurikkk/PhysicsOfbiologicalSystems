import matplotlib.pyplot as plt
import numpy as np
from q5_framework import solve_SIR

R0 = 2.5
gamma = 1/20
N_tot = 3162
n_t = 1000
T = 13
t_span = (0, T)
t_eval = np.linspace(0, T, n_t)
i0 = np.array((0.99, 0.01))
res = solve_SIR(R0, i0, t_span, t_eval)

cases_rate = N_tot * gamma * R0 * res.y[0, :] * res.y[1, :]

plt.figure()
plt.plot(res.t/gamma, cases_rate, label=r'cases rate')
plt.xlabel('$t [days]$')
plt.ylabel('Cases rate')
plt.title('Dynamics of the cases rate for R0={r0}'.format(r0=R0))
plt.show()
