from .globales import Globals as g
from menus import *

def pop_menu(menu_name):
    if g.menu_previo == '' and g.menu_previo != menu_name:
        g.menu_previo = menu_name

    menu = eval(menu_name + '()')
    g.menu_actual = menu