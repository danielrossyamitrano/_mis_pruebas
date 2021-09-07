from .basewidget import BaseWidget
from math import sin, cos, radians, sqrt
from pygame import Surface, transform, SRCALPHA, Color


class Handle(BaseWidget):
    pressed = False
    selected = False

    def __init__(self, angle, pos, color1, color2='white'):
        super().__init__()
        self.angle = angle
        self.linked = []
        self.img_uns = self.create(6, color1)
        self.img_sel = self.create(8, color2)
        self.image = self.img_uns
        self.rect = self.image.get_rect(center=pos)

    @staticmethod
    def create(size, fg, bg='gold'):
        image = Surface((size + 2, size + 2), SRCALPHA)
        image.fill(bg)
        image.fill(Color(fg), rect=[1, 1, size, size])
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

            if self.angle + delta >= 360:
                self.angle = 0
            elif self.angle + delta <= 0:
                self.angle = 360
            else:
                self.angle += delta

            self.rect.center = self.set_xy()
            for widget in self.linked:
                widget.adjust(self)

    def link(self, arc):
        if arc not in self.linked:
            self.linked.append(arc)

    def unlink(self, arc):
        if arc in self.linked:
            self.linked.remove(arc)

    def set_xy(self):
        x = round(160 + 74 * cos(radians(self.angle)))
        y = round(120 + 74 * sin(radians(self.angle)))
        return x, y

    def euclidean_distance(self, other) -> float:
        """Devuelve la distancia de Euclides que hay entre dos handles."""
        x1, y1 = self.rect.center
        x2, y2 = other.rect.center
        d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return d

    def update(self, *args, **kwargs) -> None:
        """Controla la imagen del handle según si está seleccionado o no."""

        if self.selected:
            self.image = self.img_sel
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            self.image = self.img_uns
            self.rect = self.image.get_rect(center=self.rect.center)

        self.selected = False

    def merge(self):
        """
        Al unirse dos Handles, estos se mezclan porque el arco que había entre ellos desapareció.
        """

        for arc in self.linked:
            if self is not arc.handle_a and self.euclidean_distance(arc.handle_a) < 3:
                arc.handle_a.kill()
                self.unlink(arc)
                linked = [a for a in arc.handle_a.linked if a is not arc][0]
                self.link(linked)
                linked.handle_b = self

            elif self is not arc.handle_b and self.euclidean_distance(arc.handle_b) < 3:
                arc.handle_b.kill()
                self.unlink(arc)
                linked = [a for a in arc.handle_b.linked if a is not arc][0]
                self.link(linked)
                linked.handle_a = self
