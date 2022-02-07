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
    return alpha_g * (1 + 1 * mutation_number / (mutation_number + wt_number))


def mutation_rate_func_3(alpha_g, wt_number, mutation_number):
    """
    original rate multiplied by a fraction of mutated cell function.
    :param alpha_g: original probability of a cell turn to be mutant
    :param wt_number: number of wild type cells.
    :param mutation_number: number of mutated cells.
    :return:
    """
    return alpha_g * (1 + 4 * mutation_number / (mutation_number + wt_number))


def mutation_rate_func_4(alpha_g, wt_number, mutation_number):
    """
    original rate multiplied by a fraction of mutated cell function.
    :param alpha_g: original probability of a cell turn to be mutant
    :param wt_number: number of wild type cells.
    :param mutation_number: number of mutated cells.
    :return:
    """
    return alpha_g * (1 + 6 * mutation_number / (mutation_number + wt_number))


if __name__ == '__main__':
    functions = [mutation_rate_func_1, mutation_rate_func_2, mutation_rate_func_3, mutation_rate_func_4]
    for function_i, rate_func in enumerate(functions):

        number_of_mutations = np.zeros(q6_framework.c)
        minimal_mutation_generation = np.zeros(q6_framework.c)
        with Pool(8) as p:
            simulation_res = p.map(q6_framework.simulate_single_branch,
                                   [rate_func for j in range(q6_framework.c)])

            for i in range(q6_framework.c):
                number_of_mutations[i] = simulation_res[i][0]
                minimal_mutation_generation[i] = simulation_res[i][1]
                print(i, (number_of_mutations[i], minimal_mutation_generation[i]))

        # print(res)
        np.save('mutations_{i}'.format(i=function_i), number_of_mutations)
        np.save('minimal_generation_{i}'.format(i=function_i), minimal_mutation_generation)
