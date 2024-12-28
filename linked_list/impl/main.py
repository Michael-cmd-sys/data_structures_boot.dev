class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        if self.val:
            self.next = node.val
            node.next = None

    def __repr__(self):
        return self.val
