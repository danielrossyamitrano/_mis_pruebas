from pygame import event as events, quit, KEYDOWN, QUIT, K_ESCAPE, init, display
from pygame import KEYUP, K_UP, K_DOWN
from sys import exit
from mode7 import draw_bg

init()
fondo = display.set_mode((640, 480))
fondo.fill((0, 125, 155))
dy = 1
while True:
    for e in events.get([KEYDOWN, QUIT]):
        if (e.type == KEYDOWN and e.key == K_ESCAPE) or (e.type == QUIT):
            quit()
            exit()

        elif e.type == KEYDOWN:
            if e.key == K_UP:
                dy += 1
            elif e.key == K_DOWN:
                dy -= 1

        elif e.type == KEYUP:
            dy = 1

    draw_bg(fondo, dy)
    display.update()
