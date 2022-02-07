import matplotlib.pyplot as plt
import numpy as np
import Lurie_Delbruck_framework as q6_framework


number_of_mutations = np.load('mutations_1.npy')

number_of_bins = 50
max_threshold = 300
sample = [x if x < max_threshold else max_threshold for x in number_of_mutations]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# print(x)
bins = list(range(0, max_threshold+1, max_threshold // number_of_bins))
ax.hist(sample, bins=bins)
plt.xlabel('Bins')
plt.ylabel('# of random numbers in bin')
plt.title('Histogram of Luria-Delbrück experiment with C={c} and n_0={n0}.'
          ''.format(c=q6_framework.c, n0=q6_framework.n0))
plt.show()

m = np.average(number_of_mutations)
std = np.std(number_of_mutations)
print("mean: {m}, std: {std}".format(m=m, std=std))
