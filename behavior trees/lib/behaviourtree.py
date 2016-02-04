from collections import OrderedDict
from .composites import *
from .decorators import *
from .node import Leaf


class BehaviourTree:
    # this is a container.
    nodes = []
    tree_structure = None
    to_check = None

    def __init__(self, tree_data, scripts):
        self.tree_structure = OrderedDict()
        for key in [str(i) for i in range(len(tree_data))]:
            node = None
            data = tree_data[key]
            idx = int(key)
            self.tree_structure[idx] = []

            if 'children' in data:  # composite
                self.tree_structure[idx].extend(data['children'])
                if data['type'] == 'Selector':
                    node = Selector(self, idx, data['children'])
                elif data['type'] == 'Secuence':
                    node = Secuence(self, idx, data['children'])

            elif 'child' in data:  # decorator
                self.tree_structure[idx].append(int(data['child']))
                if data['script'] == 'Repeater':
                    node = Repeater(self, idx, data['child'])
                elif data['script'] == 'UntilFail':
                    node = UntilFail(self, idx, data['child'])
                elif data['script'] == 'Succeeder':
                    node = Succeeder(self, idx, data['child'])
                elif data['script'] == 'Inverter':
                    node = Inverter(self, idx, data['child'])

            else:  # leaf
                node = Leaf(self, idx, data['context'],data['script'])
                process = None
                if data['script'] in globals():
                    process = globals()[data['script']]
                elif hasattr(scripts, data['script']):
                    process = getattr(scripts, data['script'])

                node.set_process(process)

            self.nodes.append(node)

        self.set_parents()
        self.set_children()
        self.to_check = self.nodes[0]

    def __repr__(self):
        return 'BehaviourTree: current node #' + str(self.to_check.idx)

    def set_parents(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                node = self.nodes[idx]
                for idxn in self.tree_structure[idx]:
                    self.nodes[idxn].set_parent(node)

    def set_children(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                if hasattr(self.nodes[idx], 'children'):
                    for idxn in self.nodes[idx].children:
                        node = self.nodes[idxn]
                        index = self.nodes[idx].children.index(idxn)
                        self.nodes[idx].children[index] = node

                elif hasattr(self.nodes[idx], 'child'):
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
