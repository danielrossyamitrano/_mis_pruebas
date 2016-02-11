from globs import Globals as g, pop_menu
import os

pop_menu('MenuInicial')

running = True
while running:
    os.system(['clear','cls'][os.name == 'nt'])
    
    running = g.menu_actual.update()