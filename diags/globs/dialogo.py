#este es el objeto de trabajo
import json

class dialogo:
    personajes = []
    lineas = []
        
    
    def add_new(cls,txt,loc,leads):
        d = {'txt':txt,'loc':loc,'leads':leads}
        cls.nodos.append(d)
        
    def convert(cls):
        pass
           
    def export(cls):
        '''converts the data to a json file'''
        pass