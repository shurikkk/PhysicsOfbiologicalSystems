import numpy as np
# import itertools
# from timeit import default_timer as timer


def calculate_tree_size(_g):
    return (1 - number_of_children ** _g) / (1 - number_of_children)


m = 1
n0 = 200
alpha_g = 2e-9
# alpha_g = 1/1000
# multiply_rate = 3
g = 21
tree_depth = g+1
number_of_children = 2
total_number_of_nodes = calculate_tree_size(tree_depth)


def simulate_single_branch(mutation_rate_func, params):
    n_wt = np.zeros(g+1)
    n_mut = np.zeros(g+1)
    n_wt[0] = n0
    # n_s[0] = 1
    first_g = g+1
    for i in range(1, g+1):
        # print(i)
        potential_wt_cells = number_of_children*n_wt[i-1]
        potential_mutated_cells = number_of_children*n_mut[i-1]
        # mutations = np.random.poisson(alpha_g, potential_mutant_cells)
        # n_mutations = np.count_nonzero(mutations)

        prob = mutation_rate_func(alpha_g, potential_wt_cells, potential_mutated_cells, *params)
        n_mutations = np.random.poisson(prob*potential_wt_cells)
        if first_g == g+1 and n_mutations > 0:
            first_g = i
        n_wt[i] = potential_wt_cells - n_mutations
        n_mut[i] = potential_mutated_cells + n_mutations

    return n_mut[-1], first_g
