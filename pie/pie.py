from pygame import display, event, QUIT, quit, draw
from pygame.sprite import Sprite, LayeredUpdates
from pygame import KEYDOWN, K_ESCAPE, SRCALPHA
from pygame import Surface, transform
from math import sin, cos, pi
from sys import exit

# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled

pantalla = display.set_mode((320, 240))
screen_rect = pantalla.get_rect()
values = [
    # [60, [255, 0, 0, 255]],
    [36, [0, 255, 0, 255]],
    # [4, [0, 0, 255, 255]]
]


class Handle(Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = Surface((8, 8), SRCALPHA)
        image.fill((0, 0, 0))
        # self.image = transform.rotate(image, 45.0)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))


class Arc(Sprite):
    def __init__(self, clr, a, b, cx, cy, r):
        super().__init__()
        self.image = Surface((r * 2, r * 2), SRCALPHA)
        self.rect = self.image.get_rect()
        p = [(self.rect.centerx, self.rect.centery)]
        for n in range(a, b+1):
            x = self.rect.centerx + int(r * cos(n * pi / 180))
            y = self.rect.centery + int(r * sin(n * pi / 180))
            p.append((x, y))

        draw.polygon(self.image, clr, p)

        self.handle_left = Handle(p[1][0]-self.rect.width, p[1][1])
        # self.handle_right = Handle(p[-1][0]+self.rect.centerx, p[-1][1]+self.rect.centery, 'right')

        self.rect.center = (cx, cy)


chart = LayeredUpdates()
arco = 0
u = 0
for value, color in values:
    arco += round((value / 100) * 360)
    arc = Arc(color, u, arco, 50, 50, 74)
    chart.add(arc, arc.handle_left)
    u = arco

while True:
    events = event.get([KEYDOWN, QUIT])
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()

    pantalla.fill((125, 125, 125, 255))
    chart.draw(pantalla)
    display.update()
