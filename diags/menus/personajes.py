from .base import MenuBase, subselector
from globs import dialogo, Globals as g, pop_menu

class MenuPersonajes(MenuBase):
    def __init__(self):
        prompt = 'Opción'
        opciones = ['Agregar personajes',
                    'Ver personajes',
                    'Eliminar personajes',
                    'Editar personajes',
                    'Volver']
        
        funcs = [self.add_pj,
                 self.view_pjs,
                 self.del_pjs,
                 self.edit_pjs,
                 self.exit]
        
        super().__init__(prompt,opciones,funcs)
        self.nombre = 'MenuPersonajes'
        
    def add_pj(self):
        self.clear()
        print('Ingrese personajes')
        while True:
            p = input("> ")
            if p != '':
                dialogo.personajes.append(p)
            else:
                self.inFunction = False
                break
    
    def view_pjs(self):
        self.clear()
        l = len(dialogo.personajes)
        if l != 0:
            print('Hay '+str(l)+' personajes agregados:')
            for pj in dialogo.personajes:
                print(pj)
        else:
            print('No hay personajes agregados')
            
        input('\n[Presione Enter para continuar]\n')
    
    def del_pjs(self):
        self.clear()
        l = len(dialogo.personajes)
        if l != 0:
            print('Hay '+str(l)+' personajes agregados:')
            idx = subselector('Personaje',dialogo.personajes)
            
            del dialogo.personajes[idx]
    
    def edit_pjs(self):
        self.clear()
        l = len(dialogo.personajes)
        if l != 0:
            print('Hay '+str(l)+' personajes agregados:')
            idx = subselector('Personaje',dialogo.personajes)
        new = ''
        while new == '':
            new = input("Nuevo nombre para '"+dialogo.personajes[idx]+"': ")
        
        dialogo.personajes[idx] = new
    
    def exit(self):
        pop_menu(g.menu_previo)