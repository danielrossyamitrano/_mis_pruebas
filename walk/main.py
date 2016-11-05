import os


def _generar_arbol(_path):
    walk = []
    dx = _path.count('\\')
    for dirname, hijos, _ in os.walk(_path):
        _split = os.path.split(dirname)
        nombre = _split[1]
        for exclude in ['.git', '.idea', '__pycache__']:
            if exclude in hijos:
                hijos.remove(exclude)
        for subdirname in hijos:
            if subdirname.startswith('_'):
                hijos.remove(subdirname)

        if hijos:
            empty = False
        else:
            empty = True

        x = dirname.count('\\') - dx
        walk.append({'x': x, 'obj': nombre, 'empty': empty, 'path': dirname, 'hijos': hijos})

    return walk


path = 'D:\Python\ls'
ret = _generar_arbol(path)
for obj in ret:
    # noinspection PyTypeChecker
    print(obj['x'], obj['path'])
