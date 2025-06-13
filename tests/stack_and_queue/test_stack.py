import pytest

from algorithm_and_problem_solving.stack_and_queue import Stack


@pytest.mark.parametrize('values,expected_values,expected_height', [
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 5),
    ([], [], 0),
    ([1, 2], [2, 1], 2)
])
def test_build_stack_from_values(values, expected_values, expected_height):
    s = Stack.from_values(values)
    assert s.values == expected_values
    assert s.height == expected_height


@pytest.mark.parametrize('init_value,values,expected_values,expected_height', [
    (1, [2, 3], [3, 2, 1], 3),
    (5, [7, 8, 9], [9, 8, 7, 5], 4)
])
def test_push_in_stack(init_value, values, expected_values, expected_height):
    s = Stack(init_value)
    for val in values:
        s.push(val)

    assert s.values
    assert s.height == expected_height


@pytest.mark.parametrize('values,expected_values, expected_height', [
    ([1, 2, 3, 4, 5], [4, 3, 2, 1], 4),
    ([5, 9, 8, 7], [8, 9, 5], 3)
])
def test_pop_in_stack(values, expected_values, expected_height):
    s = Stack.from_values(values)
    s.pop()
    assert s.values == expected_values
    assert s.height == expected_height
