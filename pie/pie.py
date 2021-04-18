from pygame import display, draw, event, QUIT, quit
from pygame import KEYDOWN, K_LEFT, K_RIGHT, K_ESCAPE
# from random import randint
import math
from sys import exit

# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled

screen = display.set_mode((160, 160))
screen.fill((125, 125, 125))
screen_rect = screen.get_rect()

values = [
    [60, [255, 0, 0]],
    [36, [0, 255, 0]],
    [4, [0, 0, 255]]
]


def pie_chart():
    radius = (screen_rect.width//2)-3
    u = 0
    arc = 0
    for i in range(len(values)):
        p = [screen_rect.center]
        val, color = values[i]
        arc += round((val/100)*360)

        for n in range(u, arc+1):
            x = screen_rect.centerx + int(radius * math.cos(n * math.pi / 180))
            y = screen_rect.centery + int(radius * math.sin(n * math.pi / 180))
            p.append((x, y))
        u = arc
        draw.polygon(screen, color, p)


rotation = 0
pie_chart()
while True:
    events = event.get([KEYDOWN, QUIT])
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                rotation -= 1

            elif e.key == K_RIGHT:
                rotation += 1

    display.update()
