import matplotlib.pyplot as plt
import numpy as np
# import Lurie_Delbruck_framework as ld_framework


number_of_all_mutations = np.load('mutations.npy')
betas = np.load('betas.npy')
n, c = np.shape(number_of_all_mutations)

means = np.mean(number_of_all_mutations, 1)
stds = np.std(number_of_all_mutations, 1)

cv = stds/means

plt.plot(betas, cv)
plt.xlabel(r'$\beta$')
plt.ylabel('$CV$')
# plt.title(r'Coefficient of variance vs $\beta$')
plt.show()
