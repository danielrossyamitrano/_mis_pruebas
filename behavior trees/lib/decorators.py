from .node import Node
from .status import *

class Decorator(Node):
    type = 'Decorator'
    child = None

    def __init__(self, tree, idx, child):
        # these nodes can only point to one child
        super().__init__(tree, idx)
        self.child_idx = child
        
        
    def __repr__(self):
        return str(self.idx) + ' ' + self.type +' '+ self.name
    
    def update(self):
        self.child.update()

        
class Repeater(Decorator):
    name = 'Repeater'
    current_round = 0
    def __init__(self, tree, idx, child, times=0):
        super().__init__(tree, idx, child)
        
        
    def get_child_status(self, status):
        pass

        
class UntilFail(Decorator):
    name = 'UntilFail'
    def get_child_status(self, status):
        if status is Failure:
            self.parent.get_child_status(Success)
        
        else:
            self.tree.set_to_check(self.child)

        
class Succeeder(Decorator):
    name = 'Succeeder'
    
    def get_child_status(self, status):
    
        self.parent.get_child_status(Success)


class Inverter(Decorator):
    name = 'Inverter'
    
    def get_child_status(self, status):
        if status is Success:
            status = Failure
        
        elif status is Failure:
            status = Success
        
    
        self.parent.get_child_status(status)
