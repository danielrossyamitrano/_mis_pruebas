from pygame import PixelArray, mask, Surface, init, quit, display, event as events, QUIT, image
from sys import exit
import re


def get_hex_palette(surface):
    _tmpSurf = surface.copy()
    pxarray = PixelArray(_tmpSurf)
    width, height = pxarray.shape
    colores = []
    for x in range(width):
        for y in range(height):
            rgba = _tmpSurf.unmap_rgb(pxarray[x, y])
            hex_color = '{0:0=2X}{1:0=2X}{2:0=2X}{3:0=2X}'.format(*rgba)
            if hex_color not in colores:
                colores.append(hex_color)

    return colores


def serialize(surface):
    mascara = mask.from_threshold(surface, (255, 0, 255), (1, 1, 1, 255))
    width, height = mascara.get_size()
    serial_code = ''
    for y in range(height):
        for x in range(width):
            serial_code += str(mascara.get_at([x, y]))

    return serial_code


def encode(input_string):
    count = 1
    prev = ''
    code = ''
    string = input_string.replace('0', 'A').replace('1', 'B')
    for character in string:
        if character != prev:
            if prev != '':
                entry = prev + str(count)
                code += entry
            count = 1
            prev = character
        else:
            count += 1
    code += prev + str(count)

    return code


def decode(code):
    q = ""
    num = ''
    char = ''
    for character in code:
        if character.isalpha():
            if num != '':
                q += char * int(num)
                num = ''
            if character == 'A':
                char = '0'
            elif character == 'B':
                char = '1'

        elif character.isnumeric():
            num += character
    q += char * int(num)
    return q


def deserialize(serial_code, w, h):
    _surf = Surface((w, h))
    img = PixelArray(_surf)
    idx = -1
    for y in range(h):
        for x in range(w):
            idx += 1
            if 0 <= idx < len(serial_code):
                if serial_code[idx] == '1':
                    img[x, y] = 255, 0, 255

            else:
                img[x, y] = 0, 0, 0

    return img.make_surface()


def comprimir(code):
    s = 'B'
    e = code
    while e.replace(s, 'J').count('JJ') == 0:
        s += e[e.find(s[-1], e.find(s)) + 1]

    comp = e.replace(s, 'J')
    jotas = comp.count('J')
    split = comp.split('J' * jotas)

    comp = ('J' + str(jotas)).join(split) + ':' + s
    return comp


def descomprimir(comp):
    assert analize_code(comp), f'Code "{comp}" is invalid'
    key, val = comp.split(':')
    j = key.find('J')
    if not j == -1:
        n = int(key[key.find('J') + 1])
        missing = val * int(n)
        return missing.join(key.split('J' + str(n)))
    else:
        return key


def analize_code(serial_code: str):
    code = re.compile(r'[A-B]\d+[J]\d+[A-B]\d+[A-B]\d+:[A-B]\d+[A-B]\d+')

    valid = re.fullmatch(code, serial_code) is not None
    valid = serial_code.count('AA') <= 1 and valid
    valid = serial_code.count('BB') <= 1 and valid
    valid = serial_code.count('JJ') <= 1 and valid
    return valid


init()

surf = Surface((53, 71))
surf.fill((255, 0, 255), (22, 61, 10, 16))

serial = serialize(surf)
encoded = encode(serial)
compressed = comprimir(encoded)
decompressed = descomprimir(compressed)
decoded = decode(decompressed)
imagen = deserialize(decoded, 53, 71)  # hay que suministrar las medidas de la imagen original

get_hex_palette(image.load('arbol_escalado.png'))

fondo = display.set_mode((200, 200))
while True:
    fondo.fill((255, 255, 255))

    fondo.blit(imagen, (10, 10))
    fondo.blit(surf, (90, 10))
    display.update()
    for event in events.get():
        if event.type == QUIT:
            quit()
            exit()
