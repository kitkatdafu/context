import numpy as np
import math
from itertools import combinations, product


def find_legalConfigs(n_images_per_question : int) -> list:
    # generate all legal configurations
    legal_configs = []
    for possible_config in list(product([0, 1], repeat=math.comb(n_images_per_question, 2))):
        # create an empty graph
        g = np.zeros((n_images_per_question, n_images_per_question), dtype=int)
        # fill the graph with the possible configs
        for idx, (i, j) in enumerate(combinations(range(n_images_per_question), 2)):
            g[i, j] = possible_config[idx]
            g[j, i] = possible_config[idx]
        np.fill_diagonal(g, 1)

        # check if each component in the graph is fully connected
        # if this is true, the the configuration is legal
        explored = set()
        is_legal = True
        for node in range(n_images_per_question):
            if node in explored:
                continue
            explored.add(node)

            # get node's neighbors
            neighbors = set(list(np.where(g[node] == 1)[0]))

            # for each node
            # check if each of its neighbors' neighbor is equal to its neighbor
            for neighbor in neighbors:
                if neighbor in explored:
                    continue
                explored.add(neighbor)

                # get neighbor's neighbors
                neighbor_neighbors = set(list(np.where(g[neighbor] == 1)[0]))

                # early break
                if neighbor_neighbors != neighbors:
                    is_legal = False
                    break

            # early break
            if not is_legal:
                break
        if is_legal:
            legal_configs.append(possible_config)
    return legal_configs