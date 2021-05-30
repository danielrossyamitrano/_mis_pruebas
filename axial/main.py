from pygame import KEYDOWN, K_UP, K_DOWN, QUIT, K_ESCAPE, K_SPACE, K_RETURN, KEYUP, SCALED
from pygame import draw, image, font, display, event, quit, init, Surface, time
from fuciones import lines, set_xy
from os import path, getcwd, remove
from constantes import *
from sys import exit

init()
fps = time.Clock()
display.set_caption('Worldbuilding')
ruta_b = path.join(getcwd(), 'latitudes.png')
if path.exists(ruta_b):
    remove(ruta_b)


def axial_loop():
    screen = display.set_mode((600, 300), SCALED)
    frame = Surface((600, 300))
    frame.fill(blanco)

    rect = screen.get_rect()

    screen.fill(blanco)
    f = font.SysFont('Verdana', 16)

    tilt = 0
    done = False
    lats = None
    delta = 0
    data = {'axial tilt': 0}
    while not done:
        fps.tick(60)
        events = event.get([KEYDOWN, QUIT, KEYUP])
        event.clear()

        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                quit()
                exit()

            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    delta = +1
                elif e.key == K_DOWN:
                    delta = -1
                elif e.key == K_RETURN or e.key == K_SPACE and lats is not None:
                    done = True
                    image.save(lats, ruta_b)
                    data['axial tilt'] = tilt

            elif e.type == KEYUP:
                delta = 0

        if tilt + delta < 0:
            tilt = 180
        elif tilt + delta > 180:
            tilt = 0

        tilt += delta

        frame.fill(blanco)
        draw.line(frame, negro, [100, rect.centery], [rect.w - 50, rect.centery], width=2)  # orbital plane
        draw.circle(frame, amarillo, [100, rect.centery], 50)  # "here's a star"
        planet = draw.circle(frame, negro, [400, rect.centery], 100, width=2)  # "and a planet"

        draw.line(frame, negro, [planet.centerx, 0], [planet.centerx, rect.h])  # perpendicular line
        x1, y1 = set_xy(planet.inflate(75, 75), tilt - 90)
        x2, y2 = set_xy(planet.inflate(75, 75), tilt + 90)
        draw.line(frame, negro, [x1, y1], [x2, y2], width=1)  # axial tilt line

        render_tilt = f.render('tilt: ' + str(round(tilt, 2)), True, negro)
        tilt_rect = render_tilt.get_rect(right=rect.w)
        frame.blit(render_tilt, tilt_rect)

        lats = lines(tilt)
        screen.fill(blanco)
        screen.blit(frame, (0, 0))
        display.update()

    return data


__all__ = [
    'axial_loop'
]

if __name__ == '__main__':
    print(axial_loop())
