class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_next(self, node):
        new_node = node
        self.head = node.val
        new_node.next = None
