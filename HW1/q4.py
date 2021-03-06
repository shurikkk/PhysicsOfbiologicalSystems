import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


def poissonSetup(mu):
    bins = max(int(10*mu), 10)
    widths = [sp.poisson.cdf(i, mu) for i in range(bins)]
    res = [0] + widths
    return res


def wrapper(mu):
    sample = np.random.uniform(0, 1, size=10000)

    widths = poissonSetup(mu)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.hist(sample, bins=widths)
    plt.xlabel('Bins')
    plt.ylabel('# of random numbers in bin')
    plt.title('Histogram of Poisson distribution for mu={mu} and {b} bins.'.format(mu=mu,
                                                                                   b=len(widths)-1))
    plt.show()

    mapped_sampling = np.digitize(sample, widths) - 1

    m = np.average(mapped_sampling)
    std = np.std(mapped_sampling)
    print("mean: {m}, std: {std}".format(m=m, std=std))
    return m, std


# a = poissonSetup(1.4)
# print(a)

mu = 20
wrapper(mu)
