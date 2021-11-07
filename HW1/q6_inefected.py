import numpy as np

m = 1
c = 500
n0 = 200
alpha_g = 2e-9
# multiply_rate = 3
g = 21
number_of_children = 2


class Cell(object):

    def __init__(self, father=None, is_infected=False, generation=1):
        self.father = father
        self.children = []
        self.is_infected = is_infected
        self.generation = generation

    def reproduce(self, is_infected):
        for child_is_infected in is_infected:
            is_infected = self.is_infected or child_is_infected
            new_child = Cell(self, is_infected, self.generation+1)
            self.children.append(new_child)


def run_simulation(node, depth, max_depth):
    if depth > max_depth:
        return 0, max_depth + 1
    elif depth == max_depth:
        return (1, depth) if node.is_infected else (0, depth+1)
    if node.is_infected:
        return 2 ** (max_depth - depth), depth
    node.reproduce()
    count = 0
    min_child_depth = max_depth + 1
    for child in node.children:
        child_count, child_depth = run_simulation(child, depth+1, max_depth)
        count += child_count
        if min_child_depth < child_depth:
            min_child_depth = child_depth
    return count, min_child_depth


res = [{} for ii in range(m)]

for ii in range(m):
    count = 0
    first_infected_generation = 0
    for i in range(c):
        current_nodes = [Cell() for _ in range(n0)]
        next_nodes = []
        count = 0
        generation = 1
        while generation < g:
            children_is_infected = np.random.uniform(0, 1, number_of_children * len(current_nodes))
            children_is_infected = children_is_infected < alpha_g
            children_is_infected = np.reshape(children_is_infected, (len(current_nodes), number_of_children))
            for node, child_is_infected in zip(current_nodes, children_is_infected):
                node.reproduce(child_is_infected)
                next_nodes.extend(node.children)
                count += len([1 for x in node.children if x.is_infected])
                if first_infected_generation == 0 and count > 0:
                    # This is the first time an infected node was discovered
                    first_infected_generation = generation + 1
            current_nodes = next_nodes
            next_nodes = []
            generation += 1

        if count not in res[ii]:
            res[ii][count] = 1
        else:
            res[ii][count] += 1


print(res)
