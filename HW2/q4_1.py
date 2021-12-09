import numpy as np
import matplotlib.pyplot as plt
from q4_framework import generate_free_energy
# import seaborn as sns

n = 50000
L = 10
x0 = 50 * L
x = np.linspace(0, 100*L, n)
y = generate_free_energy(x, x0, L)

plt.xlabel('x')
plt.ylabel('U/kT')
plt.plot(x, y, label="Free energy")
# plt.legend()
plt.show()
