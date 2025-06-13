"""
This file will implement stack and queue for linkedlist
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value})'


class Stack:

    def __init__(self, value=None):
        self.top = Node(value) if value is not None else None
        self.height = 1 if value is not None else 0

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp)
            temp = temp.next

    @classmethod
    def from_values(cls, values):
        new_stack = cls()
        if not values:
            return new_stack

        new_stack.push(value=values[0])

        for _ in values[1:]:
            new_stack.push(_)
        return new_stack

    def push(self, value):
        node = Node(value)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if not self.top:
            return

        self.top = self.top.next
        self.height -= 1

    @property
    def values(self):
        res = []
        temp = self.top
        while temp:
            res.append(temp.value)
            temp = temp.next
        return res


class Queue:

    def __init__(self, value=None):
        node = Node(value) if value is not None else None
        self.first = node
        self.last = node
        self.length = 1 if value is value is not None else 0

    @classmethod
    def from_values(cls, values):
        queue = cls()
        if not values:
            return queue

        queue.enqueue(value=values[0])
        for val in values[1:]:
            queue.enqueue(val)

        return queue

    def enqueue(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return

        self.first = self.first.next
        self.length -= 1

    @property
    def values(self):
        res = []
        temp = self.first
        while temp:
            res.append(temp.value)
            temp = temp.next
        return res
