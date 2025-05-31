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


ll = LinkedList(1)
items = [2, 3, 4]
ll.from_values(items)
ll.from_values([])
ll.print_list()
