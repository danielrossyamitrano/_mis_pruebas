from pygame import KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import display, event, QUIT, quit, mouse
from pie import PieChart

pantalla = display.set_mode((320, 240))
screen_rect = pantalla.get_rect()

d1 = {'iron': {'color': 'red', 'value': 60, 'handle': 'yellow'},
      'silicates': {'color': 'blue', 'value': 36, 'handle': 'magenta'},
      'water ice': {'color': 'green', 'value': 4, 'handle': 'grey'}}

PieChart.init(*screen_rect.center, d1)

while True:
    events = event.get([KEYDOWN, QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP])
    px, py = mouse.get_pos()
    for e in events:
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()

        if e.type == MOUSEBUTTONDOWN:
            widgets = PieChart.chart.get_sprites_at(e.pos)
            for widget in widgets:
                widget.on_mousebuttondown(e)

        elif e.type == MOUSEBUTTONUP:
            widgets = PieChart.chart.sprites()
            for widget in widgets:
                widget.on_mousebuttonup(e)

        elif e.type == MOUSEMOTION:
            for widget in PieChart.chart.sprites():  # this action is non-standard
                if widget.pressed:
                    widget.on_mousemotion(e)

    for sprite in PieChart.chart:
        if sprite.rect.collidepoint(px, py):
            sprite.on_mouseover()

    pantalla.fill((125, 125, 125, 255))
    PieChart.draw(pantalla)
    display.update()
