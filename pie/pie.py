from pygame import display, event, QUIT, quit, draw
from pygame.sprite import Sprite, LayeredUpdates
from pygame import KEYDOWN, K_ESCAPE, SRCALPHA
from pygame import Surface
from math import sin, cos, pi
from sys import exit

# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled

pantalla = display.set_mode((320, 240))
screen_rect = pantalla.get_rect()
values = [
    [60, [255, 0, 0, 255]],
    [36, [0, 255, 0, 255]],
    [4, [0, 0, 255, 255]]
]


class Arc(Sprite):
    def __init__(self, clr, a, b, cx, cy, r):
        super().__init__()
        self.image = Surface((r*2, r*2), SRCALPHA)
        self.rect = self.image.get_rect()
        p = [[self.rect.centerx, self.rect.centery]]
        for n in range(a, b):
            x = self.rect.centerx + int(r * cos(n * pi / 180))
            y = self.rect.centery + int(r * sin(n * pi / 180))
            p.append((x, y))

        draw.polygon(self.image, clr, p)
        self.rect.center = (cx, cy)


chart = LayeredUpdates()
arco = 0
u = 0
for value, color in values:
    arco += round((value / 100) * 360)
    arc = Arc(color, u, arco, *screen_rect.center, 74)
    chart.add(arc)
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
