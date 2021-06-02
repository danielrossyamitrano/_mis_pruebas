from pygame import init, image, Surface, PixelArray
from os import getcwd, mkdir
from os.path import join, exists

ruta = join(getcwd(), 'experimento.png')
init()
surf = image.load(ruta)
w, h = surf.get_size()
pxarray = PixelArray(surf)

base = Surface((w, h))
r = PixelArray(base.copy())  # reds
g = PixelArray(base.copy())  # greens
b = PixelArray(base.copy())  # blues
a = PixelArray(base.copy())  # alphas

c = PixelArray(base.copy())  # cyans
m = PixelArray(base.copy())  # magentas
y = PixelArray(base.copy())  # yellows

rag = PixelArray(base.copy())  # red, alpha, 0, 255
rab = PixelArray(base.copy())  # red, 0, alpha, 255

gar = PixelArray(base.copy())  # alpha, green, 0, 255
gab = PixelArray(base.copy())  # 0, green, alpha, 255

bar = PixelArray(base.copy())  # alpha, 0, blue, 255
bag = PixelArray(base.copy())  # 0, alpha, blue, 255

for dy in range(h):
    for dx in range(w):
        red, green, blue, alpha = surf.unmap_rgb(pxarray[dx, dy])

        if red:
            r[dx, dy] = red, 0, 0, 255
        if green:
            g[dx, dy] = 0, green, 0, 255
        if blue:
            b[dx, dy] = 0, 0, blue, 255
        if red or green or blue:
            a[dx, dy] = alpha, alpha, alpha, 255

        if red and blue:
            m[dx, dy] = red, 0, blue, 255
        if red and green:
            y[dx, dy] = red, green, 0, 255
        if blue and green:
            c[dx, dy] = 0, green, blue, 255

        if red and alpha:
            rag[dx, dy] = red, alpha, 0, 255
            rab[dx, dy] = red, 0, alpha, 255
        if green and alpha:
            gar[dx, dy] = alpha, green, 0, 255
            gab[dx, dy] = 0, green, alpha, 255
        if blue and alpha:
            bar[dx, dy] = alpha, 0, blue, 255
            bag[dx, dy] = 0, alpha, blue, 255

r_img = r.make_surface()
b_img = b.make_surface()
g_img = g.make_surface()

a_img = a.make_surface()
c_img = c.make_surface()
m_img = m.make_surface()
y_img = y.make_surface()

rag_img = rag.make_surface()
rab_img = rab.make_surface()
bar_img = bar.make_surface()
bag_img = bag.make_surface()
gar_img = gar.make_surface()
gab_img = gab.make_surface()

ruta = join(getcwd(), 'results')
if not exists(ruta):
    mkdir(ruta)
image.save(r_img, join(ruta, 'canal rojo.png'))
image.save(b_img, join(ruta, 'canal azul.png'))
image.save(g_img, join(ruta, 'canal verde.png'))
image.save(a_img, join(ruta, 'canal alpha.png'))
image.save(c_img, join(ruta, 'canal cian.png'))
image.save(m_img, join(ruta, 'canal magenta.png'))
image.save(y_img, join(ruta, 'canal amarillo.png'))

image.save(rag_img, join(ruta, 'canal red alpha as green.png'))
image.save(rab_img, join(ruta, 'canal red alpha as blue.png'))
image.save(bar_img, join(ruta, 'canal blue alpha as red.png'))
image.save(bag_img, join(ruta, 'canal blue alpha as green.png'))
image.save(gar_img, join(ruta, 'canal green alpha as red.png'))
image.save(gab_img, join(ruta, 'canal green alpha as blue.png'))
