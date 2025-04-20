class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value})'


class LinkedList:

    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def append(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            self.head, self.tail = None, None
            return

        pre, temp = self.head, self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head, self.tail = None, None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return

        temp = self.head.next
        self.head = temp
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return

        if index == 0:
            return self.head

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        target_node = self.get(index)
        if target_node:
            target_node.value = value
        return target_node

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        if self.length == 0:
            return new_node

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 and index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        node = pre.next
        pre.next = node.next
        node.next = None
        self.length -= 1
        return node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node_with_length(self):
        if self.length == 0:
            return

        if self.length == 1:
            return self.head

        if self.length % 2 == 0:
            middle_pointer = int(self.length / 2) + 1
        else:
            middle_pointer = int(self.length / 2)

        temp = self.head
        for _ in range(middle_pointer):
            temp = temp.next
        return temp

    def find_middle_node_without_length(self):
        temp = self.head
        if not temp:
            return

        if not temp.next:
            return temp

        slow_node, fast_node = temp, temp
        while fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if not fast_node:
                break
        return slow_node

    def has_loop(self):
        temp = self.head
        if not temp:
            return

        if not temp.next:
            return temp

        slow_node, fast_node = temp, temp
        while fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if not fast_node:
                break
            if fast_node == slow_node:
                return True
        return False

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())