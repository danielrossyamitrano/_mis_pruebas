class BehaviourTree:
    #this is a container.
    nodes = []
    tree_structure = {}  # provisionalmente; luego ordered_dict
    to_tick = []  # list of nodes to be ticked in the next frame
    def __init__(self,tree_data):
        for key in [str(i) for i in range(len(tree_data))]:
            data = tree_data[key]
            idx = int(key)
            parent = data['parent']
            self.tree_structure[idx] = []
            
            if 'children' in data:  # composite
                self.tree_structure[idx].extend(data['children'])
                node = eval(data['type']+"(idx,parent,data['children'])")
            
            elif 'child' in data:  # decorator
                self.tree_structure[idx].append(int(data['child']))                
                node = eval(data['script']+"(idx,parent,data['child'])")
                
            elif data['script'] in globals(): # leaf
                node = eval(data['script']+"(idx,parent,data['context'])")
            
            else: # fallback
                node = Leaf(idx,parent,data['context'])
            
            self.nodes.append(node)
    
    def add_to_check_list(self):
        for node in self.nodes:
            if node.is_active():
                self.to_check_list.append(node)
                
        
    def update(self):
        if len(self.to_check_list) == 0:  #list is empty
            pass

class Node:
    idx = None
    _active = False
    parent = None
    
    def __init__(self,idx,parent):
        self.idx = idx
        self.parent = parent
    
    def __repr__(self):
        st = str(self.idx) +' '+ self.type + ' '
        if hasattr(self,'name'):
            st += self.name
        return st
    
    def is_active(self):
        return self._active
    

#######################
class Composite(Node):
    type = 'Composite'
    children = []
    def __init__ (self,idx, parent, children):
        #these are NOT containers, they just point to their children
        self.children.clear()  # to prevent overriding
        super().__init__(idx, parent)
        for child in children:
            self.children.append(child)


class Decorator(Node):
    type = 'Decorator'
    child = None
    def __init__(self,idx, parent, child):
        #these nodes can only point to one child
        super().__init__(idx, parent)
        self.child = child
        

class Leaf(Node):
    type = 'Leaf'
    
    def __init__(self,idx, parent, data):
        # leaves are incapable of having any children
        super().__init__(idx, parent)
    
    def process(self):
        pass

#######################
class Secuence(Composite):
    name = 'Secuence'

    
class Selector(Composite):
    name = 'Selector'

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
