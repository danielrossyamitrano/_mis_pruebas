class BehaviourTree:
    #this is a container.
    nodes = []
    tree_structure = {}  # provisionalmente; luego ordered_dict
    to_tick = []  # list of nodes to be ticked in the next frame
    def __init__(self,tree_data):
        for key in [str(i) for i in range(len(tree_data))]:
            data = tree_data[key]
            idx = int(key)
            self.tree_structure [idx] = []
            
            if 'children' in data:  # composite
                self.tree_structure[idx].extend(data['children'])
                node = eval(data['type']+"(idx,data['children'])")
            
            elif 'child' in data:  # decorator
                self.tree_structure[idx].append(int(data['child']))
                node = eval(data['script']+"(idx,data['child'])")
                
            elif data['script'] in globals(): # leaf
                node = eval(data['script']+"(idx,data['context'])")
            
            else: # fallback
                node = Leaf(idx,data['context'])
            
            self.nodes.append(node)
    
    def check_ticked(self):
        pass
        
    def run(self):
        if len(self.to_check_list) == 0:  #list is empty
            pass

class Node:
    data = None
    idx = None
    _active = False
    
    def __init__(self,idx, data):
        self.idx = idx
        self.data = data
    
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
    #these are NOT containers, they just point to their children
    
    

class Decorator(Node):
    type = 'Decorator'


class Leaf(Node):
    type = 'Leaf'
    
    def __init__(self,idx,data):
        super().__init__(idx,data)
    
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
