from pygame import display as pantalla, init as pyinit, quit as pyquit
from pygame import K_ESCAPE, draw, font, Rect, image, mouse, event
from pygame import KEYDOWN, QUIT, K_LCTRL, K_LSHIFT, MOUSEBUTTONDOWN, KEYUP
from sys import exit
import bisect
import os

pyinit()
os.environ['SDL_VIDEO_CENTERED'] = "{!s},{!s}".format(0, 0)
fondo = pantalla.set_mode((601, 597))
graph = image.load('graph.png')
fondo.blit(graph, (0, 0))
fuente = font.SysFont('verdana', 16)
rect = Rect(67, 1, 601 - 72, 597 - 67)

mass_keys = [(i + 1) / 10 for i in range(1, 9)] + [i * 1000 for i in range(1, 9)] + [
    i for i in range(1, 10)] + [i * 10 for i in range(1, 10)] + [i * 100 for i in range(1, 10)]
mass_keys.sort()

radius_keys = [i / 10 for i in range(2, 10, 2)] + [i for i in range(1, 20)]

x, a = 0, 0
exes = []
for j in range(5):
    for x in [35, 55, 70, 81, 90, 98, 105, 110, 115]:
        x += a
        if j == 1:
            x += j
        elif j == 2:
            x += 1
        exes.append(x)
    a = x
exes.sort()
yes = [26, 48, 68, 85, 100, 200, 259, 300, 333, 359, 381, 400, 417, 433]

move_x, move_y = True, True
lockx, locky = False, False
mass_value = 0
radius_value = 0
while True:
    for e in event.get():

        if e.type == QUIT:
            pyquit()
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pyquit()
                exit()

            elif e.key == K_LSHIFT:
                move_x = False

            elif e.key == K_LCTRL:
                move_y = False

        elif e.type == KEYUP:
            if e.key == K_LSHIFT:
                if not lockx:
                    move_x = True

            elif e.key == K_LCTRL:
                if not locky:
                    move_y = True

        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if (not lockx) or (not locky):
                    if (not lockx) and (not move_x):
                        lockx = True
                    if (not locky) and (not move_y):
                        locky = True
                else:
                    lockx, locky = False, False
                    move_x, move_y = True, True

    x, y = mouse.get_pos()
    if move_x and not lockx:
        line_x = x
    if move_y and not locky:
        line_y = y

    dx = x - rect.left
    dy = abs(y - rect.bottom)

    if move_x:
        if dx in exes:
            idx = exes.index(dx)
        else:
            idx = bisect.bisect(exes, dx)
        mass_value = dx * mass_keys[idx] / exes[idx]

    if move_y:
        if dy in yes:
            idy = yes.index(dy)
        else:
            idy = bisect.bisect(yes, dy) - 1
        radius_value = dy * radius_keys[idy] / yes[idy]

    mass_text = 'Mass:' + str(round(mass_value, 3))
    radius_text = 'Radius:' + str(round(radius_value, 3))
    render1 = fuente.render(mass_text, 1, (0, 0, 0), (255, 255, 255))
    render2 = fuente.render(radius_text, 1, (0, 0, 0), (255, 255, 255))

    fondo.blit(graph, (0, 0))

    draw.line(fondo, (0, 125, 255), (line_x, rect.top), (line_x, rect.bottom), 2)
    draw.line(fondo, (0, 125, 255), (rect.left, line_y), (rect.right, line_y), 2)

    fondo.blit(render1, (0, 579 - 10))
    fondo.blit(render2, (150, 579 - 10))
    pantalla.flip()
