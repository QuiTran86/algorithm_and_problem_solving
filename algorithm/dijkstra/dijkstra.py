from math import inf


def find_lowest_cost_node(cost, processed_nodes=[]):
    lowest_cost = inf
    lowest_node = None
    for _ in cost:
        if cost[_] < lowest_cost and _ not in processed_nodes:
            lowest_cost = cost[_]
            lowest_node = _
    return lowest_node


def find_optimized_cost_node(graph, cost, processed_nodes=[]):
    while node := find_lowest_cost_node(cost, processed_nodes):
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost[node] + neighbors[n]
            cost[n] = min(new_cost, cost[n])
        processed_nodes.append(node)

    return cost['Fin']
