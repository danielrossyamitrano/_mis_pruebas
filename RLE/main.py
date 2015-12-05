from pygame import PixelArray

def get_hex_palette(surface):
    _tmpSurf = surface.copy()
    pxarray = PixelArray(_tmpSurf)
    w,h = pxarray.shape
    colores = []
    for x in range(w):
        for y in range(h):
            rgba = _tmpSurf.unmap_rgb(pxarray[x,y])
            hexColor = '{0:0=2X}{1:0=2X}{2:0=2X}{3:0=2X}'.format(*rgba)
            if hexColor not in colores:
                colores.append(hexColor)

    return colores
    
def serialize(surf):
    mask = pygame.mask.from_threshold(surf, (255,0,255), (1,1,1,255))
    w,h = mask.get_size()
    serial = ''
    for y in range(h):
        for x in range(w):
            serial += str(mask.get_at([x,y]))
        
    return serial

def encode(input_string):
    count = 1
    prev = ''
    code = ''
    string = input_string.replace('0','A').replace('1','B')
    for character in string:
        if character != prev:
            if prev != '':
                entry = prev+str(count)
                code += entry
            count = 1
            prev = character
        else:
            count += 1
    code += prev+str(count)
    
    return code
 
def decode(code):
    q = ""
    num = ''
    for character in code:
        if character.isalpha():
            if num != '':
                q += char * int(num)
                num = ''
            if character == 'A': char = '0'
            elif character == 'B': char = '1'
            
        elif character.isnumeric():
            num += character
    q += char * int(num)
    return q

def deserialize(serial,w,h):
    _surf = pygame.Surface((w,h))
    img = pygame.PixelArray(_surf)
    idx = -1
    for y in range(h):
        for x in range(w):
            idx += 1
            if serial[idx]=='1':
                img[x,y] = 255,0,255
                
            else:
                img[x,y] = 0,0,0
                
    return img.make_surface()

def comprimir (encoded):
    s = 'B'
    e = encoded
    while e.replace(s,'J').count('JJ') == 0:
        s+=e[e.find(s[-1],e.find(s))+1]

    comp = e.replace(s,'J')
    Js = comp.count('J')
    split = comp.split('J'*Js)

    comp = ('J'+str(Js)).join(split)+':'+s
    return comp

def descomprimir(comp):
    key,val = comp.split(':')
    n = int(key[key.find('J')+1])
    missing = val*int(n)
    return missing.join(key.split('J'+str(n)))

import pygame, sys
pygame.init()

surf = pygame.Surface((53,71))
surf.fill((255,0,255),(22,61,10,16))

serial = serialize(surf)
encoded = encode(serial)
compressed = comprimir(encoded)
decompressed = descomprimir("B333AAAA:")
decoded = decode(decompressed)
image = deserialize(decoded,53,71) #hay que suministrar las medidas de la imagen original

fondo = pygame.display.set_mode((200,200))
while True:
    fondo.fill((255,255,255))

    fondo.blit(image,(10,10))
    fondo.blit(surf,(90,10))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

