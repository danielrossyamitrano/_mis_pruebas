from collections import OrderedDict
from types import MethodType


class Status:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value is None:
            return 'Running'
        elif self.value is False:
            return 'Failure'
        elif self.value is True:
            return 'Success'

    def __str__(self):
        if self.value is None:
            return '(running)'
        elif self.value is False:
            return '(failure)'
        elif self.value is True:
            return '(success)'


Success = Status(True)
Running = Status(None)
Failure = Status(False)


class BehaviourTree:
    # this is a container.
    nodes = []
    tree_structure = None
    to_check = None

    def __init__(self, tree_data):
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

                    # else:  # si fuera un modulo
                    #     f = getattr(Modulo, data['script'])  # obtenemos la referencia
                    #     # asignamos un nuevo self a la referencia
                    #     node.process = MethodType(f, n)

            self.nodes.append(node)

        self.set_parents()
        self.to_check = self.nodes[0]

    def set_parents(self):
        for idx in self.tree_structure.keys():
            if len(self.tree_structure[idx]):
                for idxn in self.tree_structure[idx]:
                    self.nodes[idxn].set_parent(idx)

    def get_node(self, idx):
        if 0 <= idx <= len(self.nodes) - 1:
            return self.nodes[idx]

    def set_to_check(self, idx):
        self.to_check = self.nodes[idx]

    def reset_to_check(self):
        self.to_check = None

    def update(self):
        if self.to_check is not None:
            self.to_check.update()
        else:
            return True


class Node:
    idx = None
    parent = None
    type = ''

    def __init__(self, tree, idx):
        self.idx = idx
        self.tree = tree

    def set_parent(self, parent):
        self.parent = self.tree.get_node(parent)


#######################
class Composite(Node):
    type = 'Composite'
    children = None
    current_id = None
    chld = None

    def __init__(self, tree, idx, children):
        # these are NOT containers, they just point to their children
        self.children = []  # to prevent overriding
        super().__init__(tree, idx)
        for child in children:
            self.children.append(child)
        self.current_id = 0

    def get_current_child(self):
        return self.tree.get_node(self.children[self.current_id])


class Decorator(Node):
    type = 'Decorator'
    child = None

    def __init__(self, tree, idx, child):
        # these nodes can only point to one child
        super().__init__(tree, idx)
        self.child = child


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


#######################
class Secuence(Composite):
    name = 'Secuence'

    def __repr__(self):
        return str(self.idx) + ' ' + self.type + ' ' + self.name + '(' + ','.join(self.children) + ')'

    def update(self):
        child = self.get_current_child()
        child.update()

    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Success:
            self.current_id += 1
            if self.current_id >= len(self.children):
                status = Success
            else:
                status = Running

        self.parent.get_child_status(status)


class Selector(Composite):
    name = 'Selector'

    def __repr__(self):
        return str(self.idx) + ' ' + self.type + ' ' + self.name + '(' + ','.join(self.children) + ')'

    def update(self):
        child = self.get_current_child()
        child.update()

    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Failure:
            self.current_id += 1
            if self.current_id >= len(self.children):
                status = Failure
            else:
                status = Running

        if self.parent is not None:
            self.parent.get_child_status(status)

        elif status is Success:
            self.tree.reset_to_check()


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

# Cambiar los returns de Success a Failure para explorar opciones
def _walk(self, target):
        if target == 'door':
            print('reached', target, Success)
            return Success

        elif target == 'window':
            print('reached', target, Success)
            return Success


def _close(self, openable):
    print('closing', openable, Success)
    return Success


def _open(self, openable):
    print('opening', openable, Success)
    return Success


def _smash(self, openable):
    print('smashing', openable, Success)
    return Success


def _unlock(self, openable):
    print('unlocking', openable, Success)
    return Success
