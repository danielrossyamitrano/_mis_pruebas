from collections import OrderedDict
from types import MethodType
from .composites import *
from .decorators import *
from .node import Leaf


class BehaviourTree:
    # this is a container.
    nodes = []
    tree_structure = None
    to_check = None

    def __init__(self, tree_data,scripts):
        self.tree_structure = OrderedDict()
        for key in [str(i) for i in range(len(tree_data))]:
            data = tree_data[key]
            idx = int(key)
            self.tree_structure[idx] = []

            if 'children' in data:  # composite
                self.tree_structure[idx].extend(data['children'])
                node = eval(data['type'] + "(self,idx,data['children'])")

            elif 'child' in data:  # decorator
                self.tree_structure[idx].append(int(data['child']))
                node = eval(data['script'] + "(self,idx,data['child'])")

            else:  # leaf
                node = Leaf(self, idx, data['context'])
                if data['script'] in globals():  # si la funcion ya existe,
                    # obtenemos la referencia de globals y le asignamos un nuevo self
                    node.process = MethodType(globals()[data['script']], node)

                else:  # si fuera un modulo
                    f = getattr(scripts, data['script'])  # obtenemos la referencia
                    # asignamos un nuevo self a la referencia
                    node.process = MethodType(f, node)

            self.nodes.append(node)

        self.set_parents()
        self.set_children()
        self.to_check = self.nodes[0]
        
    def __repr__(self):
        return 'BehaviourTree: current node #'+str(self.to_check.idx)
        
    def set_parents(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                node = self.nodes[idx]
                for idxn in self.tree_structure[idx]:
                    self.nodes[idxn].set_parent(node)
    
    def set_children(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                if hasattr(self.nodes[idx],'children'):
                    for idxn in self.nodes[idx].children:
                        node = self.nodes[idxn]
                        index = self.nodes[idx].children.index(idxn)
                        self.nodes[idx].children[index] = node
                
                elif hasattr(self.nodes[idx],'child'):
                    idxn = self.tree_structure[idx][0]
                    node = self.nodes[idxn]
                    self.nodes[idx].child = node
                    
    def set_to_check(self, node):
        self.to_check = node

    def reset_to_check(self):
        self.to_check = None

    def update(self):
        if self.to_check is not None:
            self.to_check.update()
        else:
            return True