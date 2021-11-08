import numpy as np
import json

m = 1
c = 500
n0 = 200
alpha_g = 2e-9
# multiply_rate = 3
g = 21
number_of_children = 2


def find_child_index(father_i):
    father_i = father_i + 1
    father_g = np.floor(np.log2(father_i)) + 1
    # child_g = father_g + 1
    # We have whole population up to father generation + relative indices in the child layer
    father_i_in_layer = father_i - (1-number_of_children**(father_g-1))/(1-number_of_children)
    first_child_i = int((1-number_of_children**father_g)/(1-number_of_children) +
                        (father_i_in_layer-1) * number_of_children)
    return list(range(first_child_i, first_child_i + number_of_children))


res = [{} for ii in range(m)]

for ii in range(m):
    for i in range(c):
        count = 0
        for j in range(n0):
            total_number_of_nodes = (1-number_of_children**g)/(1-number_of_children)
            nodes_is_infected = np.random.uniform(0, 1, int(total_number_of_nodes))
            nodes_is_infected = nodes_is_infected < alpha_g
            for node_i, prob in enumerate(nodes_is_infected):
                if prob is True:
                    children_i = find_child_index(node_i)
                    for child_i in children_i:
                        nodes_is_infected[child_i] = True
            count += sum(1 for x in nodes_is_infected if x)
            print(i, j, count)
        if count not in res[ii]:
            res[ii][count] = 1
        else:
            res[ii][count] += 1


print(res)
with open('res.dat', 'w') as fl:
    json.dump(res, fl)
