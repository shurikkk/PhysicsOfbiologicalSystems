import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

alpha = 4


def cauchy_fit(mu_y, eta, y):
    # Valid for alpha = 4
    return np.sqrt(2)/(np.pi*eta)/(1+np.power(((y-mu_y)/eta), alpha))


def gaussian_fit(mu_y, sigma, y):
    # Valid for alpha = 4
    return 1/np.sqrt(2*np.pi*np.power(sigma, 2))*np.exp(-np.power((y-mu_y), 2)/(2*np.power(sigma, 2)))


def likelihood_cauchy(params, y):
    mu_y = params[0]
    eta = params[1]
    L = np.prod(cauchy_fit(mu_y, eta, y))
    return L


def likelihood_gaussian(params, y):
    mu_y = params[0]
    sigma = params[1]
    L = np.prod(gaussian_fit(mu_y, sigma, y))
    return L


def log_likelihood_cauchy(params, y):
    mu_y = params[0]
    eta = params[1]
    L = np.sum(np.log(cauchy_fit(mu_y, eta, y)))
    return L


def log_likelihood_gaussian(params, y):
    mu_y = params[0]
    sigma = params[1]
    fit_vec = gaussian_fit(mu_y, sigma, y)
    fit_vec = fit_vec[np.where(fit_vec > 0)]
    L = np.sum(np.log(fit_vec))
    return L


def minus_log_likelihood_cauchy(params, y):
    return -log_likelihood_cauchy(params, y)


def minus_log_likelihood_gaussian(params, y):
    return -log_likelihood_gaussian(params, y)


def dll_deta(params, y):
    mu_y = params[0]
    eta = params[1]
    return -len(y)/eta + alpha*np.inner(1/(1+np.power(((y-mu_y)/eta), alpha)),
                                        np.power((y-mu_y), alpha)/np.power(eta, alpha+1))


def dll_dmu_y(params, y):
    mu_y = params[0]
    eta = params[1]
    return alpha*np.inner(1/(1+np.power(((y-mu_y)/eta), alpha)),
                          np.power((y-mu_y), alpha-1)/np.power(eta, alpha))


def grad_ll(params, y):
    return np.array([dll_dmu_y(params, y), dll_deta(params, y)])
