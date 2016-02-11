from globs import Globals as g, pop_menu
import os

class MenuBase:
    inFunction = False
    _exit = False
    nombre = ''
    
    def __init__(self,prompt,opciones,funcs):
        self.prompt = prompt #string
        self.opciones = opciones #lista de nombres de funciones
        self.funcs = funcs #lista de funciones
    
    @staticmethod
    def clear():
        os.system(['clear','cls'][os.name == 'nt'])
        
    def choose_opt(self):
        print('Elije una opción')
        self.funcs[subselector(self.prompt,self.opciones)]()
    
    def update(self):
        if not self.inFunction:
            self.choose_opt()
            
        if self._exit is True:
            self.clear()
            return False
        else:
            return True

def subselector (prompt,lista):
    for i in range(len(lista)):
        print(str(i)+': '+lista[i])
    
    item = ''
    while item == '':
        item = input ('\n'+prompt+': ').capitalize()
        if item.isnumeric():
            if int(item) not in range(len(lista)):
                print('La selección es incorrecta, intente nuevamente')
                item = ''
            else:
                return int(item)
        elif item not in lista:
            print('La selección es incorrecta, intente nuevamente')
            item = ''
        else:
            return lista.index(item)
