import numpy as np
# import itertools
# from timeit import default_timer as timer


def calculate_tree_size(_g):
    return (1 - number_of_children ** _g) / (1 - number_of_children)


m = 3
c = 500
n0 = 200
alpha_g = 2e-9
# alpha_g = 1/1000
# multiply_rate = 3
g = 21
tree_depth = g+1
number_of_children = 2
total_number_of_nodes = calculate_tree_size(tree_depth)


def find_generation(node_i):
    return int(np.floor(np.log2(node_i+1)))


def find_child_index(father_i):
    father_g = find_generation(father_i)
    # child_g = father_g + 1
    # We have whole population up to father generation + relative indices in the child layer
    father_i_in_layer = father_i - calculate_tree_size(father_g-1)
    first_child_i = int(calculate_tree_size(father_g) +
                        father_i_in_layer * number_of_children)
    return list(range(first_child_i, first_child_i + number_of_children)) \
        if first_child_i < total_number_of_nodes else []


def find_subtree_ranges(node_i):
    node_g = find_generation(node_i)
    res = [range(node_i, node_i+1)]
    first_child_i = node_i
    last_child_i = node_i
    while node_g < g:
        first_child_i = find_child_index(first_child_i)[0]
        last_child_i = find_child_index(last_child_i)[-1]
        res.append(range(first_child_i, last_child_i + 1))
        node_g += 1
    return res


def prepare_random_infected_nodes():
    nodes_is_infected = np.random.uniform(0, 1, int(total_number_of_nodes))
    # The first node has no mutation
    nodes_is_infected[0] = 1
    # Now run over all the cells and check whether we have two mutated children cells.
    # In case there are, choose the first one to be mutated.
    nodes_is_infected = nodes_is_infected < alpha_g
    left_child_i = 0
    right_child_i = 0
    while left_child_i < g:
        left_child_i = find_child_index(left_child_i)[0]
        right_child_i = find_child_index(right_child_i)[1]
        for i in range(left_child_i, right_child_i, 2):
            if nodes_is_infected[i] == True:
                nodes_is_infected[i+1] = False
    return nodes_is_infected


def simulate_single_branch(n_s_i=1):
    n_s = [0] * (g+1)
    n_r = [0] * (g+1)
    # n_s[0] = n_s_i
    n_s[0] = 1
    # n_s[0] = 1
    first_g = g+1
    for i in range(1, g+1):
        # print(i)
        potential_mutant_cells = number_of_children*n_s[i-1]
        mutations = np.random.poisson(alpha_g, potential_mutant_cells)
        n_mutations = np.count_nonzero(mutations)
        if first_g == g+1 and n_mutations > 0:
            first_g = i
        n_s[i] = number_of_children*n_s[i-1] - n_mutations
        n_r[i] = number_of_children*n_r[i-1] + n_mutations

    return sum(n_r), first_g
