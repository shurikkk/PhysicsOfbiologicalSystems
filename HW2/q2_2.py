import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 50000
filename = 'q2_{n}.npy'.format(n=n)
y = np.load(filename)
g = sns.histplot(data=y, stat='density')
g.set_yscale("log")
g.set_xscale("log")
plt.xlabel('y')
plt.ylabel('P(y)')
x = np.linspace(1, np.exp(1), 1000)
f_x = 1/x
plt.plot(x, f_x, label="g(x)=1/x", scalex=True, scaley=True)
plt.legend()
plt.show()
