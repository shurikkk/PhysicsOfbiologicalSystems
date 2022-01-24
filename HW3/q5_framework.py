import scipy.integrate
import numpy as np


def solve_SIR(R0, i0, t_span, t_eval):
    def SIR(t, sir):
        ds_dt = -R0 * sir[0] * sir[1]
        di_dt = (R0 * sir[0] - 1) * sir[1]
        return np.array((ds_dt, di_dt))

    res = scipy.integrate.solve_ivp(SIR, t_span, i0, t_eval=t_eval)
    return res

