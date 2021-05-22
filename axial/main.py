from pygame import draw, image, font, display, event, quit, init, Surface
from pygame import KEYDOWN, K_UP, K_DOWN, QUIT, K_ESCAPE, K_SPACE, K_RETURN
from fuciones import lines, set_xy
from os import path, getcwd, remove
from constantes import *
from sys import exit

init()
ruta_a = path.join(getcwd(), 'tilted.png')
ruta_b = path.join(getcwd(), 'latitudes.png')
if path.exists(ruta_a):
    remove(ruta_a)
if path.exists(ruta_b):
    remove(ruta_b)
fondo = display.set_mode((1200, 600))
frame = Surface(fondo.get_size())
frame.fill(blanco)

rect = fondo.get_rect()

fondo.fill(blanco)
f = font.SysFont('Verdana', 16)

tilt = 0
done = False
lats = None
while not done:
    events = event.get([KEYDOWN, QUIT])
    event.clear()
    delta = 0

    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True

        elif e.type == KEYDOWN:
            if e.key == K_UP:
                delta = +1
            elif e.key == K_DOWN:
                delta = -1
            elif e.key == K_RETURN or e.key == K_SPACE and lats is not None:
                image.save(frame, ruta_a)
                image.save(lats, ruta_b)

    if tilt + delta < 0:
        tilt = 180
    elif tilt + delta > 180:
        tilt = 0

    tilt += delta

    frame.fill(blanco)
    draw.line(frame, negro, [100, rect.centery], [rect.w - 50, rect.centery], width=2)
    draw.circle(frame, amarillo, [200, rect.centery], 50)
    planet = draw.circle(frame, negro, [800, rect.centery], 200, width=2)

    draw.line(frame, negro, [planet.centerx, 0], [planet.centerx, rect.h - 50])
    x1, y1 = set_xy(planet.inflate(150, 150), tilt - 90)
    x2, y2 = set_xy(planet.inflate(150, 150), tilt + 90)
    draw.line(frame, negro, [x1, y1], [x2, y2], width=1)

    render_tilt = f.render('tilt: ' + str(round(tilt, 2)), True, negro)
    tilt_rect = render_tilt.get_rect(right=rect.w)
    frame.blit(render_tilt, tilt_rect)

    lats = lines(tilt)
    if done:
        quit()
        exit()
    else:
        fondo.fill(blanco)
        fondo.blit(frame, (0, 0))
        display.update()
