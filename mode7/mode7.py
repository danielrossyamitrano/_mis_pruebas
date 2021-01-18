from pygame import draw, Surface
from itertools import cycle

colors = [(255, 255, 255), (125, 125, 125)]
cycler = cycle(colors)
yes = [1, 2, 4, 8, 16, 32, 64, 128]
y_cycler = cycle(yes)


def draw_bg():
    new = Surface((640, 240))
    color = next(cycler)
    dy = next(y_cycler)
    for y in range(new.get_height()):
        if y == dy:
            dy = next(y_cycler)
            color = next(cycler)

        draw.line(new, color, (0, y), (640, y))

    return new
