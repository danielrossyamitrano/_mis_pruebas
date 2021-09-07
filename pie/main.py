from pygame import KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import display, event, QUIT, quit, mouse
from pygame.sprite import LayeredUpdates
from pie import Arc, Handle

pantalla = display.set_mode((320, 240))
screen_rect = pantalla.get_rect()

values = [60, 36, 4]

chart = LayeredUpdates()
arco = 0
angle = 0
u = 0

arc = None
handles = []
arcs = []
w, h = screen_rect.size
for i, value in enumerate(values):
    arco += round((value / 100) * 360)
    arc = Arc(value, i, u, arco, 74)
    pos = arc.handle_pos
    handle = Handle(arco, pos, i)

    chart.add(arc, handle)
    arcs.append(arc)
    handles.append(handle)
    u = arco

arcs[0].links(handles[2], handles[0])
arcs[1].links(handles[0], handles[1])
arcs[2].links(handles[1], handles[2])

arcs[0].displace(*screen_rect.center)
arcs[1].displace(*screen_rect.center)
arcs[2].displace(*screen_rect.center)

while True:
    events = event.get([KEYDOWN, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
    px, py = mouse.get_pos()
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()

        if e.type == MOUSEBUTTONDOWN:
            widgets = chart.get_sprites_at(e.pos)
            for widget in widgets:
                widget.on_mousebuttondown(e)

        elif e.type == MOUSEBUTTONUP:
            widgets = chart.sprites()
            for widget in widgets:
                widget.on_mousebuttonup(e)

        elif e.type == MOUSEMOTION:
            for widget in chart.sprites():  # this action is non-standard
                if widget.pressed:
                    widget.on_mousemotion(e)

    for sprite in chart:
        if sprite.rect.collidepoint(px, py):
            sprite.on_mouseover()

    pantalla.fill((125, 125, 125, 255))
    chart.update()
    chart.draw(pantalla)
    display.update()
