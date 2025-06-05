"""
This file is all about operations with single linkedlist.
1. find_middle_node
2. has_loop
3. find_kth_node_from_end
4. remove_duplicates
5. binary_to_decimal
6. partition_list
7. reverse_between
8. swap_pair
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value})'


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next

    @property
    def values(self):
        if not self.head:
            return []

        temp = self.head
        results = []
        while temp:
            results.append(temp.value)
            temp = temp.next
        return results

    def from_values(self, values):
        if not values:
            return

        for _ in values:
            self.append(_)

    def make_empty(self):
        self.head = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def find_middle_node(self):
        """
        Time Complexity: O(n), Space Complexity: O(1)
        :return:
        """
        if not self.head:
            return

        slow, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self):
        """
        The Time complexity: O(n), Space Complexity: O(1)
        :return:
        """
        if not self.head:
            return False

        slow, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def find_kth_node_from_end(self, k):
        """
        The Time complexity: O(n), Space Complexity: O(1)
        :return:
        """
        if not self.head:
            return

        if k < 0 or k > self.length:
            return

        slow, fast = self.head, self.head
        for _ in range(k - 1):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        return slow

    def remove_duplicates_with_set(self):
        """
        The time complexity: O(n), space complexity: O(n)
        :return:
        """
        if not self.head:
            return

        seen_nodes = []
        prev, current = self.head, self.head
        while current:
            if current.value in seen_nodes:
                prev.next = current.next
                prev = prev.next
                self.length -= 1
            else:
                seen_nodes.append(current.value)
            current = current.next

    def remove_duplicates_in_place(self):
        """
        The time complexity: O(n^2). Space complexity: O(1)
        :return:
        """
        if not self.head:
            return

        current, runner = self.head, self.head
        while current:
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
            runner = current

    def binary_to_decimal(self):
        """
        The time complexity: O(n), Space complexity: O(1)
        :return:
        """
        if not self.head:
            return

        current = self.head
        result = 0
        while current:
            result = result * 2 + current.value
            current = current.next
        return result

    def partition_list(self, value):
        """
        The time complexity: O(n), Space complexity: O(1)
        :param value:
        :return:
        """
        if not self.head:
            return

        dummy1 = Node(0)
        dummy2 = Node(0)
        cur1 = dummy1
        cur2 = dummy2
        current = self.head
        while current:
            if current.value < value:
                cur1.next = current
                cur1 = current
            else:
                cur2.next = current
                cur2 = current
            current = current.next
        cur1.next = dummy2.next
        cur2.next = None
        self.head = dummy1.next

    def reverse_between(self, start, end):
        """
        The time complexity: O(N). Space complexity: O(1)
        :param start:
        :param end:
        :return:
        """
        if start < 0 or end > self.length:
            return

        if not self.head:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for i in range(start):
            prev = prev.next

        current = prev.next
        for i in range(end - start):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = prev.next
            prev.next = node_to_move

        self.head = dummy.next

    def swap_pair(self):
        """
        The time complexity: O(n), Space complexity: O(1)
        :return:
        """
        if not self.head:
            return

        dummy = Node(0)
        prev = dummy
        first = self.head
        if not first.next:
            dummy.next = first

        while first.next:
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            first = first.next
            if not first:
                break
        self.head = dummy.next


ll = LinkedList(1)
print(ll.values)
ll.swap_pair()
print(ll.values)
