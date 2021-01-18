from pygame import event as events, quit, KEYDOWN, QUIT, K_ESCAPE, init, display
from sys import exit
from mode7 import draw_bg

init()
fondo = display.set_mode((640, 480))
fondo.fill((0, 125, 155))

bg = draw_bg()
while True:
    for e in events.get([KEYDOWN, QUIT]):
        if (e.type == KEYDOWN and e.key == K_ESCAPE) or (e.type == QUIT):
            quit()
            exit()

    fondo.blit(bg, (0, 240))
    display.update()
