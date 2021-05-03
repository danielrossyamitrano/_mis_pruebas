from pygame import KEYDOWN, K_ESCAPE, SRCALPHA, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import display, event, QUIT, quit, draw, mouse, Color
from pygame.sprite import Sprite, LayeredUpdates
from math import sin, cos, pi, radians
from pygame import Surface, transform
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

    def __init__(self, parent, angle, x, y, color_idx):
        super().__init__(parent)
        self.angle = angle
        self.linked = []
        color = colors2[color_idx]

        self.img_uns = self.create(color, 6)
        self.img_sel = self.create('white', 8)
        self.color_name = color
        self.image = self.img_uns
        self.rect = self.image.get_rect(center=(x, y))
        self.link(parent)

    @staticmethod
    def create(color, size):
        image = Surface((size, size), SRCALPHA)
        image.fill(Color(color))
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
        delta = 0
        if self.pressed:
            if 0 <= self.angle <= 90:  # bottomright
                if dx < 0 or dy > 0:
                    delta = +1
                else:
                    delta = -1
            elif 90 <= self.angle <= 180:  # bottomleft
                if dx < 0 or dy < 0:
                    delta = +1
                else:
                    delta = -1
            elif 180 <= self.angle <= 270:  # topleft
                if dx > 0 or dy < 0:
                    delta = +1
                else:
                    delta = -1
            elif 270 <= self.angle <= 360:  # topright
                if dx > 0 or dy > 0:
                    delta = +1
                else:
                    delta = -1

            self.angle += delta
            if self.angle >= 360:
                self.angle = 0
            elif self.angle <= 0:
                self.angle = 360

            self.rect.center = self.set_xy()
            for widget in self.linked:
                widget.adjust(self.angle - delta, delta)

    def link(self, arc):
        self.linked.append(arc)

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

    def merge(self, other):
        """
        Al unirse dos Handlers, estos deben mezclarse porque el arco que había entre ellos desapareció.

        :type other: Handle
        """
        for arc in other.linked:
            if arc not in self.linked:
                self.link(arc)

        other.kill()

    def __repr__(self):
        return self.color_name + ' Handler'


class Arc(BaseWidget):
    layer = 1
    pressed = False
    points = None

    def __init__(self, val, color_idx, a, b, cx, cy, r):
        super().__init__()
        self.value = val
        self.arco = b - a
        self.radius = r
        self.points = []
        self.color = Color(colors[color_idx])
        self.color_name = colors[color_idx]
        self.a = a
        self.b = b
        self.image = self.create(a, b)
        self.rect = self.image.get_rect()

        x, y = self.point(b)
        angle = b if b < 360 else 360 - b
        self.handle = Handle(self, angle, x, y, color_idx)

        dx = cx - self.rect.centerx
        dy = cy - self.rect.centery
        self.displace(dx, dy)

    def point(self, n, rect=None):
        if rect is None:
            rect = self.rect
        x = rect.w // 2 + int(self.radius * cos(n * pi / 180))
        y = rect.h // 2 + int(self.radius * sin(n * pi / 180))
        return x, y

    def create(self, a, b):
        image = Surface((self.radius * 2, self.radius * 2), SRCALPHA)
        rect = image.get_rect()
        p = [(rect.centerx, rect.centery)]
        for n in range(a, b + 1):
            p.append(self.point(n, rect))
        try:
            draw.polygon(image, self.color, p)
            self.points = p

        except ValueError:
            # acá debería hacer merge()
            self.handle.kill()

        return image

    def displace(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self.handle.rect.move_ip(dx, dy)

    def adjust(self, angle, delta):
        a = self.a
        b = self.b
        c = 360 + angle
        d = 360 - angle

        if angle == a or a == c:
            print('caso 1', self, 'a:', a, 'b:', b, 'c:', c, 'd:', d, 'angle:', angle)
            self.a += delta
        elif angle == b or b == c:
            print('caso 2', self, 'a:', a, 'b:', b, 'c:', c, 'd:', d, 'angle:', angle)
            self.b += delta
        elif a == d:
            print('caso 3', self, 'a:', a, 'b:', b, 'c:', c, 'd:', d, 'angle:', angle)
            # self.b = self.a
            # self.a = delta
        else:
            print('caso -', self, 'a:', a, 'b:', b, 'c:', c, 'd:', d, 'angle:', angle)

        self.image = self.create(self.a, self.b)

    def __repr__(self):
        return 'Arc ' + self.color_name


values = [60, 36, 4]
colors = ['red', 'blue', 'green']
colors2 = ['black', 'magenta', 'yellow']

chart = LayeredUpdates()
arco = 0
angle = 0
u = 0
previous_handle = None
arc = None
handles = []
arcs = []
for i, value in enumerate(values):
    arco += round((value / 100) * 360)
    if arc is not None:
        previous_handle = arc.handle
    arc = Arc(value, i, u, arco, *screen_rect.center, 74)
    if previous_handle is not None:
        previous_handle.link(arc)
    chart.add(arc, arc.handle)
    handles.append(arc.handle)
    arcs.append(arc)
    u = arco
    angle += value
else:
    arc.handle.link(arcs[0])

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
