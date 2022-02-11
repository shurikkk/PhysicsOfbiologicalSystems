import Lurie_Delbruck_framework as ld_framework
from multiprocessing import Pool
import numpy as np


def mutation_rate_func(alpha_g, wt_number, mutation_number, beta):
    """
    original rate multiplied by a fraction of mutated cell function.
    :param alpha_g: original probability of a cell turn to be mutant
    :param wt_number: number of wild type cells.
    :param mutation_number: number of mutated cells.
    :return:
    """
    # mutation_ratio = mutation_number / (mutation_number + wt_number)
    # beta = 10
    return alpha_g * (1 + beta * mutation_number)


if __name__ == '__main__':
    number_of_betas = 100
    c = 5000
    number_of_mutations = np.zeros((number_of_betas, c))
    minimal_mutation_generation = np.zeros((number_of_betas, c))
    betas = np.linspace(0, 1, number_of_betas)
    for i, beta in enumerate(betas):
        print(i)

        with Pool(8) as p:
            simulation_res = p.starmap(ld_framework.simulate_single_branch,
                                       [(mutation_rate_func, (beta, )) for j in range(c)])

            for j in range(c):
                number_of_mutations[i][j] = simulation_res[j][0]
                minimal_mutation_generation[i][j] = simulation_res[j][1]

        # print(res)
    np.save('mutations', number_of_mutations)
    np.save('minimal_generations', minimal_mutation_generation)
    np.save('betas', betas)
