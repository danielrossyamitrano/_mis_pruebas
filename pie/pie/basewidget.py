from pygame.sprite import Sprite


class BaseWidget(Sprite):
    parent = None
    selected = False
    pressed = False

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if hasattr(parent, 'layer'):
            self.layer = self.parent.layer + 1

    def on_mousemotion(self, event):
        pass

    def on_mouseover(self):
        self.selected = True

    def on_mousebuttondown(self, event):
        if event.button == 1:
            self.pressed = True

    def on_mousebuttonup(self, event):
        if event.button == 1:
            self.pressed = False
