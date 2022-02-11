import matplotlib.pyplot as plt
import numpy as np
# import Lurie_Delbruck_framework as ld_framework


number_of_all_mutations = np.load('mutations.npy')
betas = np.load('betas.npy')
n, c = np.shape(number_of_all_mutations)

choose_indices = [0, 33, 66, 99]

for i in choose_indices:
    number_of_mutations = number_of_all_mutations[i]
    number_of_bins = 50
    max_threshold = 100
    sample = [x if x < max_threshold else max_threshold for x in number_of_mutations]

    bins = list(range(0, max_threshold+1, max_threshold // number_of_bins))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.hist(sample, bins=bins)
    plt.xlabel('Bins')
    plt.ylabel('# of random numbers in bin')
    plt.title(r'Histogram of Luria-Delbrück experiment for $\beta$={beta:4.2} parameter'.format(beta=betas[i]))
    fig.canvas.draw()
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[-2] = '<' + labels[-2]
    ax.set_xticklabels(labels)
    # plt.show()

    m = np.average(number_of_mutations)
    std = np.std(number_of_mutations)
    print("mean: {m}, std: {std}".format(m=m, std=std))
