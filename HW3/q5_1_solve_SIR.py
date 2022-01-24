import matplotlib.pyplot as plt
import numpy as np
from q5_framework import solve_SIR

R0 = 2.5
gamma = 1/20


n_t = 1000
T = 13
t_span = (0, T)
t_eval = np.linspace(0, T, n_t)
i0 = np.array((0.99, 0.01))
res = solve_SIR(R0, i0, t_span, t_eval)

plt.figure()
plt.plot(res.t, res.y[0, :], label=r'S')
plt.plot(res.t, res.y[1, :], label=r'I')
plt.xlabel('$\gamma t$')
plt.ylabel('SIR fraction')
plt.legend()
plt.title('Dynamics of the infection for R0={r0}'.format(r0=R0))
plt.show()

plt.figure()
plt.plot(res.t/gamma, res.y[0, :], label=r'S')
plt.plot(res.t/gamma, res.y[1, :], label=r'I')
plt.xlabel('$t [days]$')
plt.ylabel('SIR fraction')
plt.legend()
plt.title('Dynamics of the infection for R0={r0}'.format(r0=R0))
plt.show()
