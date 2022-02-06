import Lurie_Delbruck_framework as q6_framework
from multiprocessing import Pool
import json
from timeit import default_timer as timer
import numpy as np


def mutation_rate_func_1(alpha_g, wt_number, mutation_number):
    """
    Identity function (the rate is independent on the number wild type cells, nor on number of mutated cells).
    :param alpha_g: original probability of a cell turn to be mutant
    :param wt_number: number of wild type cells.
    :param mutation_number: number of mutated cells.
    :return:
    """
    return alpha_g


def mutation_rate_func_2(alpha_g, wt_number, mutation_number):
    """
    original rate multiplied by a fraction of mutated cell function.
    :param alpha_g: original probability of a cell turn to be mutant
    :param wt_number: number of wild type cells.
    :param mutation_number: number of mutated cells.
    :return:
    """
    return alpha_g * (1 + mutation_number / (mutation_number + wt_number))


if __name__ == '__main__':
    function_i = 1
    functions = [mutation_rate_func_1, mutation_rate_func_2]
    rate_func = functions[function_i]

    number_of_mutations = np.zeros(q6_framework.c)
    minimal_mutation_generation = np.zeros(q6_framework.c)
    for i in range(q6_framework.c):
        start = timer()

        with Pool(8) as p:
            simulation_res = p.map(q6_framework.simulate_single_branch,
                                   [rate_func for j in range(q6_framework.n0)])
            count = sum(x[0] for x in simulation_res)
            min_g = min(x[1] for x in simulation_res)
            number_of_mutations[i] = count
            minimal_mutation_generation[i] = min_g
        print(i, (count, min_g))

        # count, min_g = q6_framework.simulate_single_branch()
        # number_of_mutations[ii][i] = count
        # minimal_mutation_generation[ii][i] = min_g
        # print(ii, i, (count, min_g))

        end = timer()
        print(end - start)

    # print(res)
    np.save('mutations_{i}'.format(i=function_i), number_of_mutations)
    np.save('minimal_generation_{i}'.format(i=function_i), minimal_mutation_generation)
