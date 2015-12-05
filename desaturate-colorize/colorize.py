from pygame import Surface, init as py_init, quit as py_quit
from pygame import display as pantalla, event as Event, KEYDOWN, QUIT
from pygame import PixelArray, image, font, Color
import sys, colorsys

def hsv2rgb(h,s,v):
    return list(int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def colorize(image,color):
    mock = image.copy()
    unmap = mock.unmap_rgb
    pxarray = PixelArray(mock)
    if type(color) is list:
        color = Color(*color)
    hi = color.hsva[0]/360
    
    w,h = mock.get_size()
    for y in range(h):
        for x in range(w):
            s,v,alpha = Color(*unmap(pxarray[x,y])).hsva[1:]
            
            r,g,b,a = hsv2rgb(hi,s/100,v/100)+[int(alpha)]

            pxarray[x,y] = Color(r,g,b,a)

    render = pxarray.surface
    del pxarray
    return render
    

py_init()
fondo = pantalla.set_mode((200,200))
fondorect= fondo.get_rect()
img = image.load('arbol.png').convert_alpha()
render = colorize(img,[0,0,255])
#fijate que estoy usando azul puro
rect = img.get_rect(center=fondorect.center)


while True:
    events = Event.get([KEYDOWN, QUIT])
    Event.clear()
    fondo.fill((0,0,0))
    for event in events:    
        py_quit()
        sys.exit()
    
    fondo.blit(render,rect)
    pantalla.flip()