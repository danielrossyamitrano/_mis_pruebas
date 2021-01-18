from pygame import draw, Surface
from itertools import cycle

yes = [1, 2, 4, 8, 16, 32, 64, 128]
y_cycler = cycle(yes)

mapa = [
    (255, 255, 255),
    (125, 125, 125),
    (255, 255, 255),
    (125, 125, 125),
    (255, 255, 255),
    (125, 125, 125),
    (255, 255, 255),
    (125, 125, 125),
]


def draw_bg():
    new = Surface((640, 240))
    dy = next(y_cycler)
    i = -1
    for y in range(new.get_height()):
        if y == dy:
            i += 1
            dy = next(y_cycler)
        draw.line(new, mapa[i], (0, y), (640, y))

    return new
