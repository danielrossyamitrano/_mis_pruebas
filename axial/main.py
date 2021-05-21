from pygame import Surface, draw, image, font
from math import cos, pi


def axial_precession(year):
    a1 = 19.87  # minimum axial tilt value
    a2 = 34.05  # maximum axial tilt value
    m = 20000  # period of the precession

    # from: https://www.youtube.com/watch?v=a5aAIbTs_Gw
    b = (a1 + a2) / 2
    a = a2 - b
    y = a * cos((2 * pi / m) * year - pi) + b
    return y


def interpolate(x, h):
    p = [[0, h // 2], [90, h]]

    x1 = p[0][0]
    x2 = p[1][0]

    y1 = p[0][1]
    y2 = p[1][1]

    diff_x = x2 - x1
    a = (y2 - y1) / diff_x
    b = y1 - a * x1

    y = round(a * x + b)
    return y


blanco = 255, 255, 255
negro = 0, 0, 0
rojo = 255, 0, 0
azul = 0, 0, 255
verde = 0, 255, 0
magenta = 255, 0, 255

s = Surface((1200, 601))
s.fill(blanco)

font.init()
f = font.SysFont('Verdana', 16)

ruta = 'D:/Python/p/axial/lines/'

for year in range(0, 20001, 250):
    name = str(year).rjust(5, '0')
    tilt = axial_precession(year)

    frame = s.copy()
    rect = frame.get_rect()

    equator = rect.centery
    draw.line(frame, verde, [0, equator], [rect.w, equator])

    south_tropic = interpolate(tilt, rect.h)
    draw.line(frame, rojo, [0, south_tropic], [rect.w, south_tropic])

    north_tropic = rect.h - south_tropic
    draw.line(frame, rojo, [0, north_tropic], [rect.w, north_tropic])

    south_polar = interpolate(90 - tilt, rect.h)
    draw.line(frame, azul, [0, south_polar], [rect.w, south_polar])

    north_polar = rect.h - south_polar
    draw.line(frame, azul, [0, north_polar], [rect.w, north_polar])

    render = f.render('año ' + str(year), True, negro, blanco)
    frame.blit(render, (0, 0))

    render_tilt = f.render('tilt: '+str(round(tilt, 2)), True, negro, blanco)
    tilt_rect = render_tilt.get_rect(right=rect.w)
    frame.blit(render_tilt, tilt_rect)

    image.save(frame, ruta + name + '.png')
