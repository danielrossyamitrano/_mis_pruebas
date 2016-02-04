from .status import Running

class Node:
    idx = None
    parent = None
    type = ''

    def __init__(self, tree, idx):
        self.idx = idx
        self.tree = tree

    def set_parent(self, parent):
        self.parent = parent

        
class Leaf(Node):
    type = 'Leaf'
    process = None
    tick = 0

    def __init__(self, tree, idx, data):
        # leaves are incapable of having any children
        super().__init__(tree, idx)
        self.data = data

    def __repr__(self):
        return str(self.idx) + ' ' + self.type + ' '

    def update(self):
        self.tick += 1
        status = self.process(*self.data)
        if status is None:
            status = Running

        self.parent.get_child_status(status)
