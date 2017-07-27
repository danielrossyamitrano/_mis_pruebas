from pygame import display as pantalla, init as pyinit, quit as pyquit, event, KEYDOWN, QUIT
from pygame import K_KP0, K_ESCAPE, font
from planet.graph import graph_loop
import os
import sys

pyinit()
os.environ['SDL_VIDEO_CENTERED'] = "{!s},{!s}".format(0, 0)
fondo_1 = pantalla.set_mode((640, 480))
fuente = font.SysFont('verdana', 16)

while True:
    for e in event.get():
        if e.type == QUIT:
            pyquit()
            sys.exit()
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pyquit()
                sys.exit()

            elif e.key == K_KP0:
                mass, radius = graph_loop()
                pantalla.set_mode((640, 480))
                render = fuente.render('mass:' + str(mass) + ',radius:' + str(radius), 1, (255, 255, 255), (0, 0, 0))
                pantalla.get_surface().blit(render, (0, 0))

    pantalla.flip()
