import pytest
from math import inf

from dijkstra import find_optimized_cost_node


@pytest.mark.parametrize('graph, cost, expected_value', [
    (
            {'start': {'A': 6, 'B': 2}, 'B': {'A': 3, 'Fin': 5}, 'A': {'Fin': 1}, 'Fin': {}},
            {'A': 6, 'B': 2, 'Fin': inf},
            6
    ),
    (
            {'start': {'A': 5, 'B': 2}, 'A': {'C': 2, 'D': 4}, 'B': {'A': 8, 'C': 7}, 'C': {'Fin': 1},
             'D': {'C': 6, 'Fin': 3}, 'Fin': {}},
            {'A': 5, 'B': 2, 'C': inf, 'D': inf, 'Fin': inf},
            8
    ),
    (
            {'start': {'A': 10}, 'A': {'B': 20}, 'B': {'C': 1, 'Fin': 30}, 'C': {'A': 1}, 'Fin': {}},
            {'A': 10, 'B': inf, 'C': inf, 'Fin': inf},
            60
    )
])
def test_find_optimized_cost_node(graph, cost, expected_value):
    assert find_optimized_cost_node(graph, cost, processed_nodes=[]) == expected_value
