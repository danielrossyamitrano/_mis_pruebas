import json
from clases import *

def abrir_json (archivo):
    ex = open(archivo,'r')
    data = json.load(ex)
    ex.close()
    return data

file = abrir_json('example_2.json')


b = BehaviourTree(file)