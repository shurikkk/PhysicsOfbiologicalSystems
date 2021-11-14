import json
import matplotlib.pyplot as plt
import numpy as np
import q6_framework


with open('res.dat', 'r') as fl:
    number_of_mutations, minimal_mutation_generation = json.load(fl)

for i, (raw_number_of_mutations, raw_minimal_mutation_generation) in enumerate(zip(number_of_mutations,
                                                                                   minimal_mutation_generation)):
    number_of_bins = 50
    sample = [x if x < number_of_bins else number_of_bins for x in raw_number_of_mutations]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.plot(raw_minimal_mutation_generation, raw_number_of_mutations, '*')
    plt.xlabel('i*')
    plt.ylabel('m')
    plt.title('Plot of {i}-th simulation of number of mutations vs first generation the mutation appeared.'
              ''.format(i=i+1))
    plt.show()

    unique_minimal_mutation_generation = sorted(list(set(raw_minimal_mutation_generation)))
    average_number_of_resistant_mutants = [np.mean([z for y, z in zip(raw_minimal_mutation_generation,
                                                                      raw_number_of_mutations) if y == x])
                                           for x in unique_minimal_mutation_generation]

    fit = np.polyfit(unique_minimal_mutation_generation[:-1], np.log(average_number_of_resistant_mutants[:-1]), 1)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.semilogy(unique_minimal_mutation_generation, average_number_of_resistant_mutants, '*',
                label='Simulation average')
    plt.xlabel('i*')
    plt.ylabel('m')
    plt.title('Semi-log plot of {i}-th simulation of first generation of mutation appearance vs average '
              'number of mutations'
              ''.format(i=i+1))
    fit_N = 1000
    fit_x = np.linspace(min(unique_minimal_mutation_generation), max(unique_minimal_mutation_generation), fit_N)
    fit_y = np.exp(fit[1]) * np.exp(fit[0] * fit_x)
    fit_str = 'log[y(i)]={:2.2f} + {:2.2g}*i'.format(fit[1], fit[0])
    ax.plot(fit_x, fit_y, label=fit_str)
    plt.legend()
    plt.show()

    m = np.average(raw_number_of_mutations)
    std = np.std(raw_number_of_mutations)
    print("Fit {i}: {f}".format(i=i, f=fit_str))
