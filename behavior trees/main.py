import json
import data.scripts
from lib import BehaviourTree


def abrir_json(archivo):
    ex = open(archivo, 'r')
    data = json.load(ex)
    ex.close()
    return data


file = abrir_json('data/example_1.json')

b = BehaviourTree(file,data.scripts)

while True:
    if b.update():
        break
