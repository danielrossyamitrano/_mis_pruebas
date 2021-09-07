from pygame import draw, Color, Surface, SRCALPHA, transform
from .basewidget import BaseWidget
from math import sin, cos, pi

# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled
colors = ['red', 'blue', 'green']


class Arc(BaseWidget):
    layer = 1
    pressed = False
    points = None
    handle_a = None
    handle_b = None
    handle_pos = None

    def __init__(self, val, color_idx, a, b, r):
        super().__init__()
        self.value = val
        self.arco = b - a
        self.radius = r
        self.color = Color(colors[color_idx])
        self.color_name = colors[color_idx]
        self.a = a
        self.b = b
        self.image = self.create(a, b)
        self.rect = self.image.get_rect()

    def point(self, n, rect=None):
        if rect is None:
            rect = self.rect
        x = rect.w // 2 + int(self.radius * cos(n * pi / 180))
        y = rect.h // 2 + int(self.radius * sin(n * pi / 180))
        return x, y

    def create(self, a, b):
        image = Surface((self.radius * 2, self.radius * 2), SRCALPHA)
        rect = image.get_rect()
        point_sequence = [(rect.centerx, rect.centery)]
        x, y = a, b
        rotation = False
        if a < 0:
            x = 0
            y = b + abs(a)
            rotation = abs(a)

        elif 360 >= a > b:
            y = 361-a+b
            x = 0
            rotation = abs(360-a)

        for n in range(x, y + 1):
            point_sequence.append(self.point(n, rect))

        if self.handle_pos is None:
            self.handle_pos = point_sequence[-2]
        try:
            draw.polygon(image, self.color, point_sequence)

        except ValueError:
            self.kill()
            if self.handle_a.pressed:
                self.handle_a.merge()
            elif self.handle_b.pressed:
                self.handle_b.merge()

        if rotation:
            image = transform.rotate(image, rotation)

        return image

    def displace(self, cx, cy):
        dx = cx - self.rect.centerx
        dy = cy - self.rect.centery
        self.rect.move_ip(dx, dy)
        self.handle_a.rect.move_ip(dx // 2, dy // 2)
        self.handle_b.rect.move_ip(dx // 2, dy // 2)

    def adjust(self, handle):
        if handle is self.handle_a:
            self.a = handle.angle
        if handle is self.handle_b:
            self.b = handle.angle

        pos = self.rect.center
        self.image = self.create(self.a, self.b)
        self.rect = self.image.get_rect(center=pos)

    def __repr__(self):
        return 'Arc ' + self.color_name

    def links(self, handle_a, handle_b):
        self.handle_a = handle_a
        self.handle_b = handle_b

        self.handle_a.link(self)
        self.handle_b.link(self)

    def is_handle(self, handle):
        a = handle == self.handle_a
        b = handle == self.handle_b
        return a or b
