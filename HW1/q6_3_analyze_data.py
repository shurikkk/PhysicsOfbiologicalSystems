import json
import matplotlib.pyplot as plt
import numpy as np
import q6_framework


with open('res.dat', 'r') as fl:
    number_of_mutations, _ = json.load(fl)

for i, raw_number_of_mutations in enumerate(number_of_mutations):
    number_of_bins = 50
    sample = [x if x < number_of_bins else number_of_bins for x in raw_number_of_mutations]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    bins = list(range(0, number_of_bins+1))
    ax.hist(sample, bins=bins)
    plt.xlabel('Bins')
    plt.ylabel('# of random numbers in bin')
    plt.title('Histogram of {i}-th simulation of Luria-Delbrück experiment with C={c} and n_0={n0}.'
              ''.format(i=i+1, c=q6_framework.c, n0=q6_framework.n0))
    plt.show()

    m = np.average(raw_number_of_mutations)
    std = np.std(raw_number_of_mutations)
    print("sample {i}: mean: {m}, std: {std}".format(i=i, m=m, std=std))
