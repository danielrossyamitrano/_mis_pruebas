from pygame import Surface, init as py_init, quit as py_quit
from pygame import display as pantalla, event as Event, KEYDOWN
from pygame import PixelArray, image, font
import sys


def desaturate(image,method=0):
    '''Method:
        0: Average
        1: Luminosity (from gimp)
        2: Lightness (from gimp)'''
    mock = image.copy()
    imap = mock.unmap_rgb
    pxarray = PixelArray(mock)
    
    w,h = mock.get_size()
    for y in range(h):
        for x in range(w):        
            r,g,b,a = imap(pxarray[x,y])
            if method == 0:
                p = (r+g+b)//3         
            elif method == 1:
                p = int(0.21 * r + 0.72 * g + 0.07 * b)
            elif method == 2:
                p = int(0.5 + (max([r,g,b]) + min([r,g,b])))
            
            pxarray[x,y] = p,p,p,a

    render = pxarray.surface
    del pxarray
    return render
    

py_init()
fondo = pantalla.set_mode((500,232))
fondorect= fondo.get_rect()
img = image.load('arbol.png').convert_alpha()

rendera = desaturate(img,0)
renderb = desaturate(img,1)
renderc = desaturate(img,2)

rect0 = img.get_rect(left=fondorect.left)
rect1 = img.get_rect(centerx=fondorect.centerx)
rect2 = img.get_rect(right=fondorect.right)

fuente = font.SysFont('verdana',16,bold=True)
txt1 = fuente.render('Average', 1, (0,0,0),(125,125,125))
txt2 = fuente.render('Luminosity', 1, (0,0,0),(125,125,125))
txt3 = fuente.render('Lightness', 1, (0,0,0),(125,125,125))

text_rect1 = txt1.get_rect(centerx=rect0.centerx)
text_rect2 = txt2.get_rect(centerx=rect1.centerx)
text_rect3 = txt3.get_rect(centerx=rect2.centerx)

text_rect1.bottom = fondorect.bottom
text_rect2.bottom = fondorect.bottom
text_rect3.bottom = fondorect.bottom

while True:
    events = Event.get(KEYDOWN)
    Event.clear()
    fondo.fill((0,0,0))
    for event in events:
        if event.type == KEYDOWN:            
            py_quit()
            sys.exit()
    
    fondo.blit(rendera,rect0)
    fondo.blit(renderb,rect1)
    fondo.blit(rendera,rect2)
    fondo.blit(txt1,text_rect1)
    fondo.blit(txt2,text_rect2)
    fondo.blit(txt3,text_rect3)
    pantalla.flip()

