from data import scripts
from lib import BehaviourTree
import json


def abrir_json(archivo):
    ex = open(archivo, 'r')
    data = json.load(ex)
    ex.close()
    return data


file = abrir_json('data/example_2.json')

b = BehaviourTree(file, scripts)

while True:
    if b.update():
        break
