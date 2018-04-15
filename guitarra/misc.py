import json


def abrir_json(ruta, encoding='utf-8'):
    with open(ruta, 'r', encoding=encoding) as file:
        return json.load(file)


def guardar_json(ruta, datos, encoding='utf-8'):
    with open(ruta, 'w', encoding=encoding) as file:
        json.dump(file, datos)
