"""
This file will implement Queue and Stack for a list
"""


class Stack:

    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    @property
    def is_empty(self):
        return len(self.stack_list) == 0

    @property
    def peek(self):
        if self.is_empty:
            return

        return self.stack_list[-1]

    @property
    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.size == 0:
            return
        return self.stack_list.pop()


def is_balanced_parentheses(text):
    s = Stack()
    for t in text:
        if t == '(':
            s.push(t)
        elif t == ')':
            if s.is_empty or s.pop() != '(':
                return False
    return s.is_empty


def reverse_string(string):
    s = Stack()
    for _ in string:
        s.push(_)

    output = ''
    while not s.is_empty:
        output += s.pop()
    return output


def sort_stack(original_stack):
    s = Stack()
    while not original_stack.is_empty:
        temp = original_stack.pop()
        while not s.is_empty and temp < s.peek:
            original_stack.push(s.pop())
        s.push(temp)

    if original_stack.is_empty:
        while not s.is_empty:
            original_stack.push(s.pop())

    return original_stack


class Queues:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0

    def peek(self):
        return self.stack1[-1]

    def enqueue(self, value):
        if self.is_empty():
            self.stack1.append(value)
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            self.stack1.append(value)

        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return

        return self.stack1.pop()
