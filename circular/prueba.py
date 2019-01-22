from pygame import init as py_init, quit as py_quit
from pygame import event, KEYDOWN, QUIT, K_ESCAPE, K_x
from pygame import display
from math import sin, cos, radians
from sys import exit

py_init()
fondo = display.set_mode((640, 480))


def get_xy(angle, radius):
    x = round(320 + radius * cos(radians(angle)))
    y = round(240 + radius * sin(radians(angle)))
    return x, y


n_angles = 6
radio = 40

points = [get_xy(i, radio) for i in range(-90, 360-90, 360//n_angles)]

for point in points:
    fondo.fill((255, 0, 0), (point, (32, 32)))

while True:
    events = event.get([KEYDOWN, QUIT])
    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            py_quit()
            exit()
        elif e.type == KEYDOWN and e.key == K_x:
            pass

    display.update()
