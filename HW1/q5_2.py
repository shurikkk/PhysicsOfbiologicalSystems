import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


def wrapper(xi):
    sample = np.random.uniform(0, 1, size=100000)
    sample = np.log(1-sample)/np.log(1-xi)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.hist(sample, bins=1000)
    plt.xlabel('Bins')
    plt.ylabel('# of random numbers in bin')
    plt.title('Histogram of Exponential distribution for xi={xi}.'.format(xi=xi))
    plt.show()

    mapped_sampling = np.digitize(sample, np.linspace(0, 1000, 1001))

    m = np.average(mapped_sampling)
    std = np.std(mapped_sampling)
    print("mean: {m}, std: {std}".format(m=m, std=std))
    return m, std


# a = poissonSetup(1.4)
# print(a)

xi = 1/2
wrapper(xi)
