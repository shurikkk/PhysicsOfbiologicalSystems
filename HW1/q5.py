import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


def geometricSetup(xi):
    bins = max(10*int(1/xi), 10)
    widths = [sp.geom.cdf(i, xi) for i in range(bins)]
    res = [0] + widths
    return res


def wrapper(xi):
    sample = np.random.uniform(0, 1, size=10000)

    widths = geometricSetup(xi)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # print(x)
    ax.hist(sample, bins=widths)
    plt.xlabel('Bins')
    plt.ylabel('# of random numbers in bin')
    plt.title('Histogram of Exponential distribution for xi={xi} and {b} bins.'.format(xi=xi,
                                                                                       b=len(widths)-1))
    plt.show()

    mapped_sampling = np.digitize(sample, np.linspace(0, np.ceil(np.max(sample)), 1)) - 1

    m = np.average(mapped_sampling)
    std = np.std(mapped_sampling)
    print("mean: {m}, std: {std}".format(m=m, std=std))
    return m, std


# a = poissonSetup(1.4)
# print(a)

xi = 1/20
wrapper(xi)
