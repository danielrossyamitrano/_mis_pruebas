from pygame import Surface, font
from pygame.sprite import Sprite, LayeredUpdates
from math import sin, cos, radians


class Element(Sprite):
    parent = None
    command = None
    angle = 0
    delta = 0

    def __init__(self, dato):
        super().__init__()
        self.nombre = dato
        self.image = Surface((32, 32))
        self.image.fill((255, 255, 255))
        fuente = font.SysFont('verdana', 16)
        render = fuente.render(dato, 1, (0, 0, 0), (255, 255, 255))
        self.image.blit(render, (0, 0))
        self.rect = self.image.get_rect()
        self.__hash__ = Sprite.__hash__

    def circular(self, delta: int) -> None:
        self.angle += delta
        if self.angle > 359:
            self.angle = 0
        if self.angle < 0:
            self.angle += 360

    def check_placement(self) -> bool:
        return self.angle == 0

    def do_action(self):
        if self.command is None:
            self.parent.foward()

    def update(self):
        self.circular(self.delta)
        self.rect.center = self.parent.set_xy(self.angle)
        if self.check_placement():
            self.parent.actual = self
            self.parent.stop_everything(self)

    def __eq__(self, other) -> bool:
        return self.nombre == other.nombre and self.angle == other.angle

    def __hash__(self):
        return hash((self.nombre, self.angle))

    def __repr__(self):
        return 'Elemento ' + self.nombre


class CircularMenu:
    center = 320, 240
    base_radius = 8
    stopped = True
    actual = None
    cascadaActual = None
    acceso_cascadas = None

    def __init__(self, cascadas: dict):
        self.cuadros = LayeredUpdates()
        self.cascadas = {}
        self.acceso_cascadas = ['inicial']
        self.cascadaActual = 'inicial'

        self.add_cascades(cascadas)
        self.radius = self.base_radius * (len(self.cascadas['inicial']) + 1)
        self.cuadros.add(*self.cascadas['inicial'])

    def add_cascades(self, cascades: dict):
        for key in cascades:
            group = cascades[key]
            if key not in self.cascadas:
                self.cascadas[key] = []
            else:
                # por alguna razón no funciona con list comprehension
                for item in self.cascadas[key]:
                    if item in group:
                        group.remove(item)
                if not len(group):
                    return
                group += self.cascadas[key]
                self.cascadas[key].clear()

            separation = 360 // len(group)
            angle = 0
            for e in group:
                e.angle = angle
                e.parent = self
                self.cascadas[key].append(e)
                angle += separation

    def del_cascade(self, cascade: str):
        if cascade in self.cascadas:
            del self.cascadas[cascade]

    def del_tree_recursively(self, csc: str):
        for cascade in reversed(self.acceso_cascadas[self.acceso_cascadas.index(csc):]):
            self.backward()
            self.del_cascade(cascade)
            self.del_item_from_cascade(cascade, self.acceso_cascadas[-1])  # me preocupa ese [-1]
        self.stop_everything(self.actual)

    def add_item_to_cascade(self, item: Element, cascade: str):
        new = {cascade: [item]}
        self.add_cascades(new)
        self.radius = self.base_radius * (len(self.cascadas[cascade]) + 1)
        self._change_cube_list()

    def del_item_from_cascade(self, item_name: str, cascade: str):
        for item in self.cascadas[cascade]:
            if item_name == item.nombre:
                self.cascadas[cascade].remove(item)
                self._change_cube_list()
                break

    def set_xy(self, angle: int):
        x = round(self.center[0] + self.radius * cos(radians(angle - 90)))
        y = round(self.center[1] + self.radius * sin(radians(angle - 90)))
        return x, y

    def foward(self):
        if self.actual.nombre in self.cascadas:
            self.cascadaActual = self.actual.nombre
            self.acceso_cascadas.append(self.cascadaActual)
            self._change_cube_list()

    def backward(self):
        if len(self.acceso_cascadas) > 1:
            del self.acceso_cascadas[-1]
            self.cascadaActual = self.acceso_cascadas[-1]
            self._change_cube_list()
        else:
            pass

    def turn(self, delta: int):
        for cuadro in self.cuadros:
            cuadro.delta = delta * 3

    def stop_everything(self, on_spot: Element):
        cuadros = self.cuadros.sprites()
        angle = 360 // len(cuadros)  # base

        for i, cuadro in enumerate(sorted(cuadros, key=lambda c: c.angle)):
            if cuadro is not on_spot:
                cuadro.angle = angle * i
            cuadro.delta = 0
        self.stopped = True

    def _change_cube_list(self):
        self.cuadros.empty()
        self.cuadros.add(*self.cascadas[self.cascadaActual])

    def update(self):
        self.cuadros.update()

    def draw(self, fondo):
        return self.cuadros.draw(fondo)
