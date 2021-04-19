from pygame import KEYDOWN, K_ESCAPE, SRCALPHA, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import display, event, QUIT, quit, draw, mouse
from pygame.sprite import Sprite, LayeredUpdates
from math import sin, cos, pi, radians
from pygame import Surface, transform
from random import randint
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

    def on_mouseover(self):
        pass


class Handle(BaseWidget):
    pressed = False
    selected = False

    def __init__(self, parent, angle, x, y):
        super().__init__(parent)
        self.angle = angle
        self.linked = []
        self.img_uns = self.create((0, 0, 0), 6)
        self.img_sel = self.create((255, 255, 255), 8)
        self.image = self.img_uns
        self.rect = self.image.get_rect(center=(x, y))

    @staticmethod
    def create(color, size):
        image = Surface((size, size), SRCALPHA)
        image.fill(color)
        return transform.rotate(image, 45.0)

    def on_mouseover(self):
        self.selected = True

    def on_mousebuttondown(self, event):
        if event.button == 1:
            self.pressed = True

    def on_mousebuttonup(self, event):
        if event.button == 1:
            self.pressed = False

    def on_mousemotion(self, event):
        dx, dy = event.rel
        if self.pressed:
            if 0 <= self.angle <= 90:  # bottomright
                if dx < 0 or dy > 0:
                    self.angle += 1
                else:
                    self.angle -= 1
            elif 90 <= self.angle <= 180:  # bottomleft
                if dx < 0 or dy < 0:
                    self.angle += 1
                else:
                    self.angle -= 1
            elif 180 <= self.angle <= 270:  # topleft
                if dx > 0 or dy < 0:
                    self.angle += 1
                else:
                    self.angle -= 1
            elif 270 <= self.angle <= 360:  # topright
                if dx > 0 or dy > 0:
                    self.angle += 1
                else:
                    self.angle -= 1

            if self.angle > 360:
                self.angle = 0
            if self.angle < 0:
                self.angle = 360

            self.rect.center = self.set_xy()
            for widget in self.linked:
                widget.adjust()

    def set_xy(self):
        x = round(self.parent.rect.centerx + self.parent.radius * cos(radians(self.angle)))
        y = round(self.parent.rect.centery + self.parent.radius * sin(radians(self.angle)))
        return x, y

    def update(self, *args, **kwargs) -> None:
        if self.selected:
            self.image = self.img_sel
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image = self.img_uns
            self.rect = self.image.get_rect(center=self.rect.center)

        self.selected = False

    def __repr__(self):
        return 'Handler'


class Arc(BaseWidget):
    layer = 1
    pressed = False

    def __init__(self, val, a, b, cx, cy, r):
        super().__init__()
        self.value = val
        self.radius = r
        self.image = Surface((r * 2, r * 2), SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.create(a, b)

        x, y = self.point(a)
        self.handle_left = Handle(self, a, x, y)

        dx = cx - self.rect.centerx
        dy = cy - self.rect.centery
        self.displace(dx, dy)

    def point(self, n):
        x = self.rect.w//2 + int(self.radius * cos(n * pi / 180))
        y = self.rect.h//2 + int(self.radius * sin(n * pi / 180))
        return x, y

    def create(self, a, b):
        p = [(self.rect.centerx, self.rect.centery)]
        for n in range(a, b + 1):
            p.append(self.point(n))

        draw.polygon(self.image, self.color, p)

    def displace(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self.handle_left.rect.move_ip(dx, dy)

    def adjust(self):
        print(self)

    def update(self, *args, **kwargs) -> None:
        pass

    def __repr__(self):
        return 'Arc ' + str(self.value)


values = [60, 36, 4]

chart = LayeredUpdates()
arco = 0
u = 0
for value in values:
    arco += round((value / 100) * 360)
    arc = Arc(value, u, arco, *screen_rect.center, 74)
    chart.add(arc, arc.handle_left)
    u = arco

while True:
    events = event.get([KEYDOWN, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
    px, py = mouse.get_pos()
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()

        if e.type == MOUSEBUTTONDOWN:
            widgets = chart.get_sprites_at(e.pos)
            for widget in widgets:
                widget.on_mousebuttondown(e)

        elif e.type == MOUSEBUTTONUP:
            widgets = chart.sprites()
            for widget in widgets:
                widget.on_mousebuttonup(e)

        elif e.type == MOUSEMOTION:
            for widget in chart.sprites():  # this action is non-standard
                if widget.pressed:
                    widget.on_mousemotion(e)

    for sprite in chart:
        if sprite.rect.collidepoint(px, py):
            sprite.on_mouseover()

    pantalla.fill((125, 125, 125, 255))
    chart.update()
    chart.draw(pantalla)
    display.update()
