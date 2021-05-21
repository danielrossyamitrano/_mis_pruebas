from pygame import Surface, draw, image

blanco = 255, 255, 255
amarillo = 255, 255, 0
negro = 0, 0, 0
ruta = 'D:/Python/p/axial/'

fondo = Surface((1200, 600))
rect = fondo.get_rect()
fondo.fill(blanco)

draw.line(fondo,negro,[100,rect.centery],[rect.w-50, rect.centery],width=2)

draw.circle(fondo, amarillo, [200, rect.centery], 50)
planet = draw.circle(fondo, negro, [800, rect.centery], 200, width=2)
draw.line(fondo, negro, [planet.centerx,0],[planet.centerx,rect.h])

image.save(fondo, ruta + 'tilted.png')
