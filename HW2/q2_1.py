import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
from q2_framework import prob

n = 10000
filename = 'q2_{n}.npy'.format(n=n)
if os.path.isfile(filename):
    y = np.load(filename)
else:
    y = prob(50000)
    np.save(filename, y)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
sns.histplot(data=y, stat='density')
plt.xlabel('y')
plt.ylabel('P(y)')

x = np.linspace(1, np.exp(1), 1000)
f_x = 1/x
plt.plot(x, f_x, label="g(x)=1/x")
plt.legend()
plt.show()
