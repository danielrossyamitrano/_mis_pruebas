from pygame import init as py_init, quit as py_quit
from pygame import event, KEYDOWN, QUIT, display, time
from pygame import K_LEFT, K_RIGHT, K_ESCAPE, K_x, K_z, K_RETURN, K_c, K_d
from circular.renderer import Renderer
from circular.circular_menu import CircularMenu, Element as E
from sys import exit


def salir():
    py_quit()
    exit()


py_init()
fps = time.Clock()
fondo = Renderer.init((640, 480))

cascadas = {'inicial': [E('a'), E('b'), E('c'), E('d')],
            'b': [E('b1'), E('b2'), E('b3'), E('b4')],
            'c': [E('c1'), E('c2'), E('c3'), E('c4')],
            'd': [E('d1'), E('d2'), E('d3'), E('d4')]
            }

otra_cascada = {
    'e': [E('e1'), E('e2'), E('e3')],
    'e1': [E('f'), E('g')]
}

menu = CircularMenu(cascadas)

while True:
    fps.tick(60)
    fondo.fill((0, 0, 0))
    events = event.get([KEYDOWN, QUIT])
    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            salir()

        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                menu.turn(-1)

            elif e.key == K_RIGHT:
                menu.turn(+1)

            elif e.key == K_x:
                menu.foward()

            elif e.key == K_z:
                menu.backward()

            elif e.key == K_d:
                menu.del_tree_recursively('e')

            elif e.key == K_RETURN:
                menu.add_item_to_cascade(E('e'), 'inicial')
                menu.add_cascades(otra_cascada)

            elif e.key == K_c:
                pass

    menu.update()
    cambios = menu.draw(fondo)
    display.update(cambios)
