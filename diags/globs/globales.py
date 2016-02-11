class Globals:
    menu_actual = None
    menu_previo = ''

def pop_menu(menu_name):
    from menus import MenuInicial,MenuPersonajes
    g = Globals
    
    if g.menu_previo == '' and g.menu_previo != menu_name:
        g.menu_previo = menu_name

    try:
        menu = eval(menu_name + '()')
        g.menu_actual = menu
    except Exception as Description:
        print('No se pudo abrir el menu porque:', Description)