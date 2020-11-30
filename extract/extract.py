from pygame import init, image, Surface, PixelArray
from os import getcwd
from os.path import join

ruta = join(getcwd(), 'fondo.png')
init()
surf = image.load(ruta)
w, h = surf.get_size()
pxarray = PixelArray(surf)

base = Surface((w, h))
r = PixelArray(base.copy())
g = PixelArray(base.copy())
b = PixelArray(base.copy())

for y in range(h):
    for x in range(w):
        color = surf.unmap_rgb(pxarray[x, y])

        if color[0]:
            r[x, y] = color[0], 0, 0, 255
        if color[1]:
            g[x, y] = 0, color[1], 0, 255
        if color[2]:
            b[x, y] = 0, 0, color[2], 255

r_img = r.make_surface()
b_img = b.make_surface()
g_img = g.make_surface()

ruta = getcwd()
image.save(r_img, join(ruta, 'canal rojo.png'))
image.save(b_img, join(ruta, 'canal azul.png'))
image.save(g_img, join(ruta, 'canal verde.png'))
