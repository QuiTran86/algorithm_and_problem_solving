import pytest

from algorithm_and_problem_solving.sort_techniques import bubble_sort, selection_sort, \
    insertion_sort


@pytest.mark.parametrize('items,expected_items', [
    ([1, 6, 11, 9, 7, 3, 2, 5], [1, 2, 3, 5, 6, 7, 9, 11]),
    ([], None)
])
def test_bubble_sort_techniques(items, expected_items):
    assert bubble_sort(items) == expected_items


@pytest.mark.parametrize('items,expected_items', [
    ([1, 6, 11, 9, 7, 3, 2, 5], [1, 2, 3, 5, 6, 7, 9, 11]),
    ([], None)
])
def test_selection_sort(items, expected_items):
    assert selection_sort(items) == expected_items


@pytest.mark.parametrize('items,expected_items', [
    ([1, 6, 11, 9, 7, 3, 2, 5], [1, 2, 3, 5, 6, 7, 9, 11]),
    ([], None)
])
def test_insertion_sort(items, expected_items):
    assert insertion_sort(items) == expected_items
