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
