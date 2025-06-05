import pytest

from algorithm_and_problem_solving.single_linkedlist.interview import LinkedList, Node


@pytest.mark.parametrize('values, expected_output', [
    ([1, 2, 3, 4, 5], Node(3)),
    ([1, 2, 3, 4, 5, 6], Node(4)),
    ([1], Node(1))
])
def test_find_middle_node(values, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        assert ll.find_middle_node().value == expected_output.value


@pytest.mark.parametrize('values, tail_to_head, expected_output', [
    ([1, 2, 3, 4, 5], False, False),
    ([1, 2, 3, 4, 5, 6], True, True),
    (None, True, False),
    (None, False, False),
])
def test_has_loop(values, tail_to_head, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        if tail_to_head:
            ll.tail.next = ll.head
        assert ll.has_loop() == expected_output


@pytest.mark.parametrize('values, k, exepected_output', [
    ([1, 2, 3, 4, 5, 6], 2, Node(5)),
    ([1, 2, 3, 4, 5], 4, Node(2)),
    ([1, 2, 3], 4, None),
    ([1, 2, 3], -1, None)
])
def test_find_kth_node_from_end(values, k, exepected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        result = ll.find_kth_node_from_end(k)
        if not result:
            assert result == exepected_output
        if result:
            assert result.value == exepected_output.value


@pytest.mark.parametrize('values, expected_length, expected_values', [
    ([1, 2, 3, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 3, 3, 2], 3, [1, 2, 3]),
    ([1], 1, [1])
])
def test_remove_duplicates_with_set(values, expected_length, expected_values):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values)
        ll.remove_duplicates_with_set()
        assert ll.length == expected_length
        for value in ll.values:
            assert value in expected_values


@pytest.mark.parametrize('values, expected_length, expected_values', [
    ([1, 2, 3, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 3, 3, 2], 3, [1, 2, 3]),
    ([1], 1, [1])
])
def test_remove_duplicates_in_place(values, expected_length, expected_values):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values)
        ll.remove_duplicates_in_place()
        assert ll.length == expected_length
        for value in ll.values:
            assert value in expected_values


@pytest.mark.parametrize('values, expected_output', [
    ([1, 0, 1], 5),
    ([1, 0, 0, 1], 9),
    ([1, 0, 1, 1, 0, 1], 45)
])
def test_binary_to_decimal(values, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        assert ll.binary_to_decimal() == expected_output


@pytest.mark.parametrize('values, target, expected_output', [
    ([1, 2, 8, 3, 5, 10], 5, [1, 2, 3, 8, 5, 10]),
    ([9, 1, 3, 6, 7, 12, 11, 8, 4], 6, [1, 3, 4, 9, 6, 7, 12, 11, 8])
])
def test_partition_list(values, target, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        ll.partition_list(target)
        assert ll.values == expected_output


@pytest.mark.parametrize('values, start, end, expected_output', [
    ([1, 2, 3, 4, 5, 6], 2, 4, [1, 2, 5, 4, 3, 6]),
    ([1, 2, 3, 4], 0, 2, [3, 2, 1, 4])
])
def test_reverse_between(values, start, end, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        ll.reverse_between(start, end)
        assert ll.values == expected_output


@pytest.mark.parametrize('values, expected_output', [
    ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], None),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [2, 1, 3])
])
def test_swap_pair(values, expected_output):
    if values:
        ll = LinkedList(values[0])
        ll.from_values(values[1:])
        ll.swap_pair()
        assert ll.values == expected_output