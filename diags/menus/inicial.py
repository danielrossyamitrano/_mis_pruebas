from .base import MenuBase, subselector
from globs import dialogo, pop_menu

class MenuInicial(MenuBase):
    _exit = False
    def __init__(self):
        prompt = 'Opción'
        opciones = ['Editar personajes',
                    'Agregar lineas de diálogo',
                    'Editar conexiones',
                    'Salir']
        
        funcs = [lambda:pop_menu('MenuPersonajes'),
                 self.add_diag_line,
                 self.edit_conx,
                 self.exit]
        
        super().__init__(prompt,opciones,funcs)
        self.diag = dialogo()
        self.nombre = 'MenuInicial'
    
    def add_diag_line(self): 
        self.clear()
        if len(dialogo.personajes) != 0:
            print('Elige un locutor')
            idx = subselector('Locutor',dialogo.personajes)
            pj = dialogo.personajes[idx]
            
            _pj = ''
            lineas = []
            while True:
                if pj != _pj:
                    self.clear()
                    print('locutores: '+' | '.join([str(i)+': '+dialogo.personajes[i] for i in range(len(dialogo.personajes))]),'\n')
                    print('Ingresa el diálogo de este locutor','\n"'+pj+'"')
                    _pj = pj
                
                s = input('> ')
                if s.startswith('#'):
                    _s = s.strip('#')
                    if _s == "?":
                        print('\nInstrucciones')
                        print('Ingresa # y el número, o el nombre de un',
                        'locutor para cambiar a este. O ingresa #? para',
                        'ver estas instrucciones nuevamente.\n')
                        
                    if _s.isnumeric():
                        chunk = '. '.join(lineas)+'.'
                        lineas.clear()
                        dialogo.lineas.append({'loc':pj,'txt':chunk})
                        pj = dialogo.personajes[int(_s)]
                    elif _s in dialogo.personajes:
                        chunk = '.'.join(lineas)+'.'
                        lineas.clear()
                        dialogo.lineas.append({'loc':pj,'txt':chunk})
                        pj = _s
                        
                    elif _s.lower() == 'end':
                        break
                    
                    else:
                        print('Comando inválido')
                
                elif s == '':
                    lineas.append('\n')
                else:
                    lineas.append(s.capitalize())
                    
        else:
            print('No hay personajes agregados')
           
        input('\n[Presione Enter para continuar]\n')
        
    def edit_conx(self):
        print('edit_conx')
    
    def exit(self):
        self._exit = True