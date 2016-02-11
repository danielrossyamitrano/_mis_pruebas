from .base import MenuBase, subselector
from globs import dialogo

class MenuLineas(MenuBase):
    def __init__(self):
        prompt = 'Opción'
        opciones = ['Agregar lineas de diálogo',
                    'Ver lineas de diálogo',
                    'Eliminar lineas de diálogo',
                    'Volver']
        
        funcs = [self.add_diag_line,
                 self.view_diag_line,
                 self.del_diag_line,
                 self.exit]
        
        super().__init__(prompt,opciones,funcs)
        self.nombre = 'MenuPersonajes'
    
    def add_diag_line(self):
        self.clear()
        
        def add_linea(loc,linea):
            chunk = ' '.join(linea)
            dialogo.lineas.append({'loc':loc,'txt':chunk})
            
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
                        add_linea(pj,lineas)
                        lineas.clear()
                        pj = dialogo.personajes[int(_s)]
                        
                    elif _s in dialogo.personajes:
                        add_linea(pj,lineas)
                        lineas.clear()
                        pj = _s
                        
                    elif _s.lower() == 'end':
                        add_linea(pj,lineas)
                        lineas.clear()
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
        
    def view_diag_line(self):
        for i in dialogo.lineas:
            print(i)
        
        input('\n[Presione Enter para continuar]\n')
    def del_diag_line(self):
        pass
    def exit(self):
        pass