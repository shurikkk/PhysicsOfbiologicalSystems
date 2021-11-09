import q6_framework as q6_framework
from multiprocessing import Pool
import json
from timeit import default_timer as timer


if __name__ == '__main__':
    number_of_mutations = [[0] * q6_framework.c for ii in range(q6_framework.m)]
    minimal_mutation_generation = [[0] * q6_framework.c for ii in range(q6_framework.m)]
    for ii in range(q6_framework.m):
        for i in range(q6_framework.c):
            start = timer()

            with Pool(8) as p:
                simulation_res = p.map(q6_framework.simulate_single_branch, [j for j in range(q6_framework.n0)])
                count = sum(x[0] for x in simulation_res)
                min_g = min(x[1] for x in simulation_res)
                number_of_mutations[ii][i] = count
                minimal_mutation_generation[ii][i] = min_g
            print(ii, i, (count, min_g))

            # count, min_g = q6_framework.simulate_single_branch()
            # number_of_mutations[ii][i] = count
            # minimal_mutation_generation[ii][i] = min_g
            # print(ii, i, (count, min_g))

            end = timer()
            print(end - start)

    # print(res)
    with open('res.dat', 'w') as fl:
        json.dump((number_of_mutations, minimal_mutation_generation), fl)
