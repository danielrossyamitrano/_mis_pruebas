from pygame import draw
from itertools import cycle

colors = cycle([(125, 125, 125), (255, 255, 255)])
color = next(colors)


def draw_bg(surface, dy=1):
    global color

    for i, y in enumerate(range(240, 480)):
        if i == dy:
            color = next(colors)
            dy *= 2
        draw.line(surface, color, (0, y), (640, y))
