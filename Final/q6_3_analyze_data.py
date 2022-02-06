import matplotlib.pyplot as plt
import numpy as np
import Lurie_Delbruck_framework as q6_framework


number_of_mutations = np.load('500/mutations_0.npy')

number_of_bins = 50
sample = [x if x < number_of_bins else number_of_bins for x in number_of_mutations]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# print(x)
bins = list(range(0, number_of_bins+1))
ax.hist(sample, bins=bins)
plt.xlabel('Bins')
plt.ylabel('# of random numbers in bin')
plt.title('Histogram of Luria-Delbrück experiment with C={c} and n_0={n0}.'
          ''.format(c=q6_framework.c, n0=q6_framework.n0))
plt.show()

m = np.average(number_of_mutations)
std = np.std(number_of_mutations)
print("mean: {m}, std: {std}".format(m=m, std=std))
