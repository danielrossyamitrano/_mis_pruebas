from .basewidget import BaseWidget
from math import sin, cos, radians, sqrt
from pygame import Surface, transform, SRCALPHA, Color

colors2 = ['magenta', 'yellow', 'black']


class Handle(BaseWidget):
    pressed = False
    selected = False

    def __init__(self, angle, pos, color_idx):
        super().__init__()
        self.layer = 5
        self.angle = angle
        self.linked = []
        color = colors2[color_idx]

        self.img_uns = self.create(color, 6)
        self.img_sel = self.create('white', 8)
        self.color_name = color
        self.image = self.img_uns
        self.rect = self.image.get_rect(center=pos)

    @staticmethod
    def create(color, size):
        image = Surface((size, size), SRCALPHA)
        image.fill(Color(color))
        return transform.rotate(image, 45.0)

    def on_mousemotion(self, event):
        dx, dy = event.rel
        # distance = self.euclidean_distance_to_point(*event.pos)
        # print(distance)
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

            if self.angle + delta >= 360:
                self.angle = 0
            elif self.angle + delta <= 0:
                self.angle = 360
            else:
                self.angle += delta

            self.rect.center = self.set_xy()
            for widget in self.linked:
                # print('esto')
                widget.adjust(self)

    def link(self, arc):
        if arc not in self.linked:
            self.linked.append(arc)

    def set_xy(self):
        x = round(160 + 74 * cos(radians(self.angle)))
        y = round(120 + 74 * sin(radians(self.angle)))
        return x, y

    def euclidean_distance(self, other):
        x1, y1 = self.rect.center
        x2, y2 = other.rect.center
        d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return d

    def euclidean_distance_to_point(self, px, py):
        x1, y1 = self.rect.center
        return round(sqrt((px - x1) ** 2 + ((py - y1) ** 2)))

    def update(self, *args, **kwargs) -> None:
        if self.selected:
            self.image = self.img_sel
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image = self.img_uns
            self.rect = self.image.get_rect(center=self.rect.center)

        self.selected = False

    def merge(self):
        """
        Al unirse dos Handlers, estos deben mezclarse porque el arco que había entre ellos desapareció.
        """

        for arc in self.linked:
            if self is not arc.handle_a and self.euclidean_distance(arc.handle_a) < 3:
                arc.handle_a.kill()
                self.linked.remove(arc)
                linked = [a for a in arc.handle_a.linked if a is not arc][0]
                self.linked.append(linked)
                linked.handle_b = self

            elif self is not arc.handle_b and self.euclidean_distance(arc.handle_b) < 3:
                arc.handle_b.kill()
                self.linked.remove(arc)
                linked = [a for a in arc.handle_b.linked if a is not arc][0]
                self.linked.append(linked)
                linked.handle_a = self

    def __repr__(self):
        return self.color_name + ' Handler'
