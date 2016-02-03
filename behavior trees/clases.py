from collections import OrderedDict

class Status:
    def __init__(self,value):
        self.value = value
        
    def __repr__(self):
        if self.value is None:
            return 'Running'
        elif self.value is False:
            return 'Failure'
        elif self.value is True:
            return 'Success'

Success = Status(True)
Running = Status(None)
Failure = Status(False)

class BehaviourTree:
    #this is a container.
    nodes = []
    tree_structure = None
    to_check = None
    def __init__(self,tree_data):
        self.tree_structure = OrderedDict()
        for key in [str(i) for i in range(len(tree_data))]:
            data = tree_data[key]
            idx = int(key)
            self.tree_structure[idx] = []
            
            
            if 'children' in data:  # composite
                self.tree_structure[idx].extend(data['children'])
                node = eval(data['type']+"(self,idx,data['children'])")
            
            elif 'child' in data:  # decorator
                self.tree_structure[idx].append(int(data['child']))                
                node = eval(data['script']+"(self,idx,data['child'])")
            
            else: # leaf
                node = Leaf(self,idx,data['context'])
                if data['script'] in globals():
                    method = eval(data['script'])
                node.process = method
            
            self.nodes.append(node)
        
        self.set_parents()
        self.to_check = self.nodes[0]
        
    def set_parents(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                for idxn in self.tree_structure[idx]:
                    self.nodes[idxn].set_parent(idx)
    
    def get_node(self,idx):
        if 0 <= idx <= len(self.nodes)-1:
            return self.nodes[idx]
    
    def place_to_check(self,idx):
        self.to_check = self.nodes[idx]
            
    def update(self):
        if self.to_check is not None:
            debug = self.to_check
            
            status = self.to_check.update()
            if (status is Success) or (status is Failure):
                self.to_check = None


class Node:
    idx = None
    parent = None
    
    def __init__(self,tree,idx):
        self.idx = idx
        self.tree = tree
    
    def set_parent(self,parent):
        self.parent = parent
    
    def __repr__(self):
        st = str(self.idx) +' '+ self.type
        if hasattr(self,'name'):
            st += ' '+self.name
        elif hasattr(self,'children'):
            st += '('+','.join(self.children)+')'
        return st
    
    
    def update(self):
        pass
    
#######################
class Composite(Node):
    type = 'Composite'
    children = None
    current_id = None
    chld = None
    def __init__ (self,tree,idx,children):
        #these are NOT containers, they just point to their children
        self.children = []  # to prevent overriding
        super().__init__(tree,idx)
        for child in children:
            self.children.append(child)
        self.current_id = 0
    
    def update(self):
        super().update()
        return self.tree.get_node(self.children[self.current_id])


class Decorator(Node):
    type = 'Decorator'
    child = None
    def __init__(self,tree,idx, child):
        #these nodes can only point to one child
        super().__init__(tree,idx)
        self.child = child


class Leaf(Node):
    type = 'Leaf'
    process = None
    
    def __init__(self,tree, idx, data):
        # leaves are incapable of having any children
        super().__init__(tree, idx)
        self.data = data
    
    def update(self):
        status = self.process(*self.data)
        if status is None:
            return Running
        return status


#######################
class Secuence(Composite):
    name = 'Secuence'
    
    def update(self):
        child = super().update()
        status = child.update()
        if status is Running:
            self.tree.place_to_check(self.children[self.current_id])

        elif status is Success:
            self.current_id += 1
            if self.current_id >= len(self.children):
                return Success
            
        elif status is Failure:
            return Failure
        
        return Running


class Selector(Composite):
    name = 'Selector'
    def update(self):
        child = super().update()
        status = child.update()
        if status is Running:
            self.tree.place_to_check(self.children[self.current_id])
        
        elif status is Failure:
            self.current_id += 1
            if self.current_id >= len(self.children):
                return Failure

        elif status is Success:
            return Success

        return Running

#######################
class Repeater(Decorator):
    name = 'Repeater'


class UntilFail(Decorator):
    name = 'UntilFail'


class Succeeder(Decorator):
    name = 'Succeeder'


class Inverter(Decorator):
    name = 'Inverter'
#######################

#Cambiar los returns de Success a Failure para explorar opciones
def _walk(target):
    if target == 'door':
        return Success
    elif target == 'window':
        return Failure

def _close(openable):
    return Success

def _open(openable):
    return Failure

def _smash(openable):
    return Success

def _unlock(openable):
    return Failure
