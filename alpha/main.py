from pygame import image, init as py_init, quit as py_quit
from pygame import display as pantalla
from pygame import PixelArray, mask, Surface
from pygame import event, QUIT, KEYDOWN, SRCALPHA
import sys

def extract_mask(img):
    mock = img.copy()
    umap = mock.unmap_rgb
    pxarray = PixelArray(mock)

    w,h = mock.get_size()
    alpha = mask.Mask((w, h))
    for y in range(h):
        for x in range(w):
            r,g,b,a = umap(pxarray[x,y])
            if a == 255:
                alpha.set_at([x,y],1)
            elif a != 0:
                pxarray[x,y] = r,g,b,255

    render = pxarray.make_surface()
    return render,alpha

py_init()
fondo = pantalla.set_mode((75,50))
img =  image.load('crate.png').convert_alpha()
render,mascara = extract_mask(img)

w,h = mascara.get_size()
layer = Surface((w,h),SRCALPHA)
for y in range(h):
    for x in range(w):
        if mascara.get_at((x,y)):
            layer.fill((255,0,255,125),(x,y,1,1))

while True:
    fondo.fill((0,255,125))
    for e in event.get():
        if e.type == QUIT or e.type == KEYDOWN:
            py_quit()
            sys.exit()
    fondo.blit(render,(5,10))
    fondo.blit(img,(30,10))
    fondo.blit(render, (55,10))
    fondo.blit(layer,(55,10))
    pantalla.flip()