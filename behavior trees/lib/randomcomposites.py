from random import choice, randint
from .composites import *
from .status import *


class RandomComposite(Composite):
    explored_children = []

    def __init___(self, tree, idx, children):
        super().__init__(tree, idx, children)
        self.current_id = randint(0, len(children))
        self.explored_children.append(self.children[self.current_id])


class RandomSecuence(Secuence):
    explored_children = []

    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Success:
            idx = choice(self.children)
            while idx in self.explored_children:
                idx = choice(self.children)

            self.explored_children.append(idx)
            self.current_id = idx

            if len(self.explored_children) == len(self.children):
                status = Success
            else:
                status = Running

        self.parent.get_child_status(status)


class RandomSelector(Selector):
    explored_children = []

    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Failure:
            idx = choice(self.children)
            while idx in self.explored_children:
                idx = choice(self.children)

            self.explored_children.append(idx)
            self.current_id = idx

            if len(self.explored_children) == len(self.children):
                status = Failure
            else:
                status = Running

        self.parent.get_child_status(status)
