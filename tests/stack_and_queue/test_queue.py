import pytest

from algorithm_and_problem_solving.stack_and_queue import Queue


@pytest.mark.parametrize('values,expected_values,expected_length', [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),
    ([6, 7, 8], [6, 7, 8], 3),
    ([], [], 0)
])
def test_build_queue_from_values(values, expected_values, expected_length):
    queue = Queue.from_values(values)
    assert queue.values == expected_values
    assert queue.length == expected_length


@pytest.mark.parametrize('init_value,values,expected_values,expected_length', [
    (1, [6, 7, 8, 9], [1, 6, 7, 8, 9], 5),
    (2, [3], [2, 3], 2)
])
def test_enqueue(init_value, values, expected_values, expected_length):
    queue = Queue(init_value)
    for val in values:
        queue.enqueue(val)
    assert queue.values == expected_values
    assert queue.length == expected_length


@pytest.mark.parametrize('values,expected_values,expected_length', [
    ([1, 7, 8, 9, 10], [7, 8, 9, 10], 4),
    ([1, 2, 3], [2, 3], 2)
])
def test_dequeue(values, expected_values, expected_length):
    queue = Queue.from_values(values)
    queue.dequeue()
    assert queue.values == expected_values
    assert queue.length == expected_length
