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
    nodes_is_infected = np.random.poisson(alpha_g, int(total_number_of_nodes))
    # The first node has no mutation
    nodes_is_infected[0] = 0
    # Now run over all the cells and check whether we have two mutated children cells.
    # In case there are, choose the first one to be mutated.
    nodes_is_infected = nodes_is_infected > 0
    left_child_i = 0
    right_child_i = 0
    while left_child_i < g:
        left_child_i = find_child_index(left_child_i)[0]
        right_child_i = find_child_index(right_child_i)[1]
        for i in range(left_child_i, right_child_i, 2):
            if nodes_is_infected[i] == True:
                nodes_is_infected[i+1] = False
    return nodes_is_infected


def simulate_single_branch(_):
    nodes_is_infected = prepare_random_infected_nodes()
    # infected_i = np.where(nodes_is_infected == True).tolist()
    min_i = np.argmax(nodes_is_infected)
    if min_i == 0:
        # The first node has no mutation, thus we for sure got no mutant cells at all!
        first_g = g + 1
    else:
        first_g = find_generation(min_i)

    infected_i = list(np.where(nodes_is_infected == True)[0])
    # infected_i2 = list(np.where(nodes_is_infected == True)[0])
    # valid_infected_i2 = list(np.where(nodes_is_infected == True)[0])

    # start = timer()
    # test_sum = 0
    # for node_i in infected_i2:
    #     if node_i not in valid_infected_i2:
    #         continue
    #     node_g = find_generation(node_i)
    #     test_sum += calculate_tree_size(tree_depth - node_g)
    #     subtree_ranges = find_subtree_ranges(node_i)
    #     valid_infected_i2 = [x for x in valid_infected_i2 if x not in itertools.chain(*subtree_ranges)]
    # end = timer()
    # print(end - start)  # Time in seconds, e.g. 5.38091952400282

    # start = timer()
    while len(infected_i) > 0:
        next_infected_i = []
        for node_i in infected_i:
            # We don't have to change all the tree, but to add the spanning sub_tree size
            children_i = find_child_index(node_i)
            for child_i in children_i:
                if child_i < total_number_of_nodes:
                    nodes_is_infected[child_i] = True
                    next_infected_i.append(child_i)
        infected_i = next_infected_i
    test_sum2 = sum(1 for x in nodes_is_infected if x)
    # end = timer()
    # print(end - start)  # Time in seconds, e.g. 5.38091952400282
    return test_sum2, first_g
