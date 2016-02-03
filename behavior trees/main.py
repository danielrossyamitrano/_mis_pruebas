import json
from clases import BehaviourTree


def abrir_json(archivo):
    ex = open(archivo, 'r')
    data = json.load(ex)
    ex.close()
    return data


file = abrir_json('example_1.json')

b = BehaviourTree(file)

while True:
    if b.update():
        break

