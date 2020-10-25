# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.prev = self

    def is_sentinel(self):
        return self.value == None

    def is_empty(self):
        return self.next == self and self.prev == self

    def is_last(self):
        return self.next.is_sentinel()

    def last(self):
        return self.prev

    def append(self, node):
        self.prev.next = node
        node.prev = self.prev
        self.prev = node
        node.next = self

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


    def insert(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def at(self, index):
        node = self
        for _ in range(index):
            node = node.next
        return node


    def search(self, value):
        node = self
        for _ in range(index):
            node = node.next
            if node.value == value:
                return node
        return None
