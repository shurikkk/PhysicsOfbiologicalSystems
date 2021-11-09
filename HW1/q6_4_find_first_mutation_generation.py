import json
import matplotlib.pyplot as plt
import numpy as np


with open('res.dat', 'r') as fl:
    number_of_mutations, minimal_mutation_generation = json.load(fl)

for i, raw_number_of_mutations, raw_minimal_mutation_generation in enumerate(zip(number_of_mutations, minimal_mutation_generation)):
    number_of_bins = 50
    sample = [x if x < number_of_bins else number_of_bins for x in raw_number_of_mutations]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.plot(raw_number_of_mutations, raw_minimal_mutation_generation)
    plt.xlabel('m')
    plt.ylabel('i*')
    plt.title('Plot of {i}-th simulation of number of mutations vs first generation the mutation appeared.'
              ''.format(i=i+1))
    plt.show()

    m = np.average(raw_number_of_mutations)
    std = np.std(raw_number_of_mutations)
    print("sample {i}: mean: {m}, std: {std}".format(i=i, m=m, std=std))
