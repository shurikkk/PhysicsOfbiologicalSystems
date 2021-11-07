import numpy as np

m = 1
c = 500
n0 = 200
alpha_g = 2e-9
# multiply_rate = 3
g = 21


class Cell(object):
    number_of_children = 2

    def __init__(self, father=None, is_infected=False):
        self.father = father
        self.children = []
        self.is_infected = is_infected

    def reproduce(self):
        for _ in range(self.number_of_children):
            sample = np.random.uniform(0, 1)
            is_infected = self.is_infected or sample < alpha_g
            new_child = Cell(self, is_infected)
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
    for i in range(c):
        current_nodes = [Cell() for _ in range(n0)]
        count = 0
        for node in current_nodes:
            simulation_count, simulation_first_generation = run_simulation(node, 0, g)
            count += run_simulation(node, 0, g)
    if count not in res[ii]:
        res[ii][count] = 1
    else:
        res[ii][count] += 1


print(res)
