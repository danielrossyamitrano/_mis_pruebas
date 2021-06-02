from pickle import dump, load
from pygame import Surface, PixelArray


def unpickle_surf(filename):
    with open(filename, 'r+b') as file:
        d = load(file)

    img = Surface([d['w'], d['h']])
    px_array = PixelArray(img)
    i = -1
    for x in range(d['w']):
        for y in range(d['h']):
            i += 1
            px_array[x, y] = d['pixels'][i]

    return px_array.make_surface()


def pickle_surf(surface, ruta):
    pxarray = PixelArray(surface)
    pixels = []
    w, h = surface.get_size()
    d = {'w': w, 'h': h}
    for x in range(w):
        for y in range(h):
            pixels.append(pxarray[x, y])
    d['pixels'] = pixels

    with open(ruta, 'w+b') as file:
        dump(d, file)
