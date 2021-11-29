import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


r = np.genfromtxt('flowCytometry.txt')
r = r[r >= 0]
log10r = np.log10(r)
med = np.median(log10r)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
sns.histplot(data=log10r, stat='density')
plt.xlabel('Log of fluorescence levels')
plt.ylabel('Histogram of log of fluorescence levels')
ax.axvline(med, alpha=0.8, ymax=0.7, linestyle=":")
ax.text(med-0.4, 0.49, "median", size=11, alpha=0.85)
plt.show()
print('Median: {m}'.format(m=med))
