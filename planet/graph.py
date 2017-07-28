from pygame import display as pantalla, quit as pyquit
from pygame import K_ESCAPE, draw, font, Rect, image, mouse, event
from pygame import KEYDOWN, K_LCTRL, K_LSHIFT, MOUSEBUTTONDOWN, KEYUP, K_RETURN, NOFRAME
from sys import exit
import bisect
import os

font.init()
graph = image.load('graph.png')
fuente = font.SysFont('verdana', 16)
mass_keys = [(i + 1) / 10 for i in range(1, 9)] + [i * 1000 for i in range(1, 9)] + [
    i for i in range(1, 10)] + [i * 10 for i in range(1, 10)] + [i * 100 for i in range(1, 10)]
mass_keys.sort()
radius_keys = [i / 10 for i in range(2, 10, 2)] + [i for i in range(1, 20)]
negro, gris, cian = (0, 0, 0), (125, 125, 125), (0, 125, 255)

x, a = 0, 0
exes = []
for j in range(5):
    for x in [33, 53, 68, 79, 88, 95, 102, 108, 114]:
        x += a
        if j == 1:
            x += 1
        elif j == 2:
            x += 2
        elif j == 3:
            x += 1
        elif j == 4:
            x += 2
        exes.append(x)
    a = x
exes.sort()
yes = [26, 48, 68, 85, 100, 200, 259, 300, 333, 359, 381, 400, 417, 433]


def graph_loop():
    w, h = 606, 606
    os.environ['SDL_VIDEO_CENTERED'] = "{!s},{!s}".format(0, 0)
    pantalla.set_mode((w, h), NOFRAME)
    rect = Rect(72, 3, w - 78, h - 74)
    move_x, move_y = True, True
    lockx, locky = False, False
    mass_value = 0
    radius_value = 0
    while True:
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pyquit()
                    exit()

                if e.key == K_LSHIFT:
                    move_x = False

                elif e.key == K_LCTRL:
                    move_y = False

                elif e.key == K_RETURN:
                    pantalla.quit()
                    return mass_value, radius_value

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

        mouse_x, mouse_y = mouse.get_pos()
        if move_x and not lockx:
            line_x = mouse_x
        if move_y and not locky:
            line_y = mouse_y

        dx = mouse_x - rect.left
        dy = abs(mouse_y - rect.bottom)

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

        pantalla.get_surface().fill(gris)
        area = pantalla.get_surface().blit(graph, (3, 3))
        if rect.collidepoint(line_x, line_y):
            draw.line(pantalla.get_surface(), cian, (line_x, rect.top + 1), (line_x, rect.bottom), 2)
            mass_text = 'Mass:' + str(round(mass_value, 3))
        else:
            mass_text = 'Mass:'

        if rect.collidepoint(rect.left, line_y):
            draw.line(pantalla.get_surface(), cian, (rect.left, line_y), (rect.right, line_y), 2)
            radius_text = 'Radius:' + str(round(radius_value, 3))
        else:
            radius_text = 'Radius:'

        pantalla.get_surface().blit(fuente.render(mass_text, 1, negro), (area.left, area.bottom - 22))
        pantalla.get_surface().blit(fuente.render(radius_text, 1, negro), (area.left + 153, area.bottom - 22))

        pantalla.flip()


if __name__ == '__main__':
    graph_loop()
