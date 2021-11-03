import scipy.stats as sp


def poissonSetup(mu):
    bins = max(int(10*mu), 10) + 1
    dist = sp.poisson.pmf(mu)
    res = []
    return


a = poissonSetup(1)
print(a)
