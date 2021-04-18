from pygame import KEYDOWN, K_ESCAPE, SRCALPHA, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import display, event, QUIT, quit, draw
from pygame.sprite import Sprite, LayeredUpdates
from pygame import Surface, transform
from math import sin, cos, pi
from sys import exit

# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled

pantalla = display.set_mode((320, 240))
screen_rect = pantalla.get_rect()


class BaseWidget(Sprite):
    parent = None

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if hasattr(parent, 'layer'):
            self.layer = self.parent.layer + 1

    def on_mousebuttondown(self, event):
        pass

    def on_mousebuttonup(self, event):
        pass

    def on_mousemotion(self, event):
        pass


class Handle(BaseWidget):
    pressed = False

    def __init__(self, parent, x, y):
        super().__init__(parent)
        image = Surface((8, 8), SRCALPHA)
        image.fill((0, 0, 0))
        self.image = transform.rotate(image, 45.0)
        self.rect = self.image.get_rect(center=(x, y))

    def on_mousebuttondown(self, event):
        if event.button == 1:
            self.pressed = True

    def on_mousebuttonup(self, event):
        if event.button == 1:
            self.pressed = False

    def on_mousemotion(self, event):
        dx, dy = event.rel
        self.rect.move_ip(dx, dy)
        self.parent.adjust()

    def update(self, *args, **kwargs) -> None:
        pass

    def __repr__(self):
        return 'Handler'


class Arc(BaseWidget):
    layer = 1
    pressed = False

    def __init__(self, clr, a, b, cx, cy, r):
        super().__init__()
        self.image = Surface((r * 2, r * 2), SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = clr
        p = [(self.rect.centerx, self.rect.centery)]
        for n in range(a, b+1):
            x = self.rect.centerx + int(r * cos(n * pi / 180))
            y = self.rect.centery + int(r * sin(n * pi / 180))
            p.append((x, y))

        draw.polygon(self.image, clr, p)

        self.handle_left = Handle(self, p[1][0], p[1][1])
        self.handle_right = Handle(self, p[-1][0], p[-1][1])

        dx = cx-self.rect.centerx
        dy = cy-self.rect.centery
        self.displace(dx, dy)

    def displace(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self.handle_right.rect.move_ip(dx, dy)
        self.handle_left.rect.move_ip(dx, dy)

    def adjust(self):
        pass

    def update(self, *args, **kwargs) -> None:
        pass

    def __repr__(self):
        return 'Arc'+str(self.color)


values = [
    [60, [255, 0, 0, 255]],
    [36, [0, 255, 0, 255]],
    [4, [0, 0, 255, 255]]
]

chart = LayeredUpdates()
arco = 0
u = 0
for value, color in values:
    arco += round((value / 100) * 360)
    arc = Arc(color, u, arco, *screen_rect.center, 74)
    chart.add(arc, arc.handle_left, arc.handle_right)
    u = arco

while True:
    events = event.get([KEYDOWN, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()

        if e.type == MOUSEBUTTONDOWN:
            widgets = chart.get_sprites_at(e.pos)
            for widget in widgets:
                widget.on_mousebuttondown(e)

        elif e.type == MOUSEBUTTONUP:
            widgets = chart.get_sprites_at(e.pos)
            for widget in widgets:
                widget.on_mousebuttonup(e)

        elif e.type == MOUSEMOTION:
            for widget in chart.sprites():
                if widget.pressed:
                    widget.on_mousemotion(e)

    pantalla.fill((125, 125, 125, 255))
    chart.update()
    chart.draw(pantalla)
    display.update()
