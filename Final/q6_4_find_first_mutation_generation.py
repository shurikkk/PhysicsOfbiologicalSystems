import matplotlib.pyplot as plt
import numpy as np


number_of_mutations = np.load('500/mutations_0.npy')
minimal_mutation_generation = np.load('500/minimal_generation_0.npy')

number_of_bins = 50
sample = [x if x < number_of_bins else number_of_bins for x in number_of_mutations]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# print(x)
ax.plot(minimal_mutation_generation, number_of_mutations, '*')
plt.xlabel('i*')
plt.ylabel('m')
plt.title('Plot of number of mutations vs first generation the mutation appeared.')
plt.show()

unique_minimal_mutation_generation = sorted(list(set(minimal_mutation_generation)))
average_number_of_resistant_mutants = [np.mean([z for y, z in zip(minimal_mutation_generation,
                                                                  number_of_mutations) if y == x])
                                       for x in unique_minimal_mutation_generation]

fit = np.polyfit(unique_minimal_mutation_generation[:-1], np.log(average_number_of_resistant_mutants[:-1]), 1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# print(x)
ax.semilogy(unique_minimal_mutation_generation, average_number_of_resistant_mutants, '*',
            label='Simulation average')
plt.xlabel('i*')
plt.ylabel('m')
plt.title('Semi-log plot of first generation of mutation appearance vs average '
          'number of mutations')
fit_N = 1000
fit_x = np.linspace(min(unique_minimal_mutation_generation), max(unique_minimal_mutation_generation), fit_N)
fit_y = np.exp(fit[1]) * np.exp(fit[0] * fit_x)
fit_str = 'log[y(i)]={:2.2f} + {:2.2g}*i'.format(fit[1], fit[0])
ax.plot(fit_x, fit_y, label=fit_str)
plt.legend()
plt.show()

m = np.average(number_of_mutations)
std = np.std(number_of_mutations)
print("Fit: {f}".format(f=fit_str))
