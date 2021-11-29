import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


r = np.genfromtxt('flowCytometry.txt')
# r = r[r >= 0]
med = np.median(r)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# sns.histplot(data=r, bins=100, stat='probability')
sns.histplot(data=r, stat='probability')
plt.xlabel('fluorescence levels')
plt.ylabel('Histogram of fluorescence levels')
ax.axvline(med, alpha=0.8, ymax=0.5, linestyle=":")
ax.text(med-3, 0.105, "median", size=11, alpha=0.85)
plt.show()
print('Median: {m}'.format(m=med))
