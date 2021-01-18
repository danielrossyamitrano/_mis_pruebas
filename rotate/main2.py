from pygame import display as pantalla, init as pyinit
from pygame import font, Surface, transform, event, quit as pyquit, Rect
from pygame import KEYDOWN, K_RIGHT, K_LEFT, K_ESCAPE
import sys

pyinit()
blanco = 255, 255, 255
negro = 0, 0, 0

top = 0
left = 0
right = 0
bottom = 0
cw = ['north', 'east', 'south', 'west']
idx = 0

fondo = pantalla.set_mode((250, 250))
frect = Rect(0, 0, 200, 200)
fuente = font.SysFont('verdana', 30)

img = Surface((200, 200))
img.fill(blanco)
rect = img.get_rect(center=frect.center)

render = fuente.render('0', 1, negro, blanco)
ra = render.get_rect()
img.blit(render, (0, 0))

render = fuente.render('1', 1, negro, blanco)
rb = render.get_rect()
img.blit(render, (rect.w - ra.w, 0))

render = fuente.render('2', 1, negro, blanco)
rc = render.get_rect()
img.blit(render, (0, rect.h - rb.h))

render = fuente.render('3', 1, negro, blanco)
rd = render.get_rect()
img.blit(render, (rect.w - rc.w, rect.h - rc.h))
x, y = 0, 0

d = 90
while True:
    angle = 0
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pyquit()
                sys.exit()
            elif e.key == K_RIGHT:
                angle = d
            elif e.key == K_LEFT:
                angle = -d

            if angle:
                img = transform.rotate(img, angle)

    fondo.blit(img, (25, 25))
    pantalla.flip()
