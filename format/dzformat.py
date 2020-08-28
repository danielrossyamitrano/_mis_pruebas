import subprocess
import sys
from tkinter import Tk

r = Tk()
txt = r.clipboard_get()
output_string = ''
r.clipboard_clear()

tag_in = '[COLOR=rgb(183, 28, 28)]'
tag_out = '[/COLOR]'
puntuacion = [',', '.', ';', ':', '{', '}', '[', ']', ')', '(', '¿', '?', '¡', '!', '+', '-', '=', '*', '/', '"', "'"]


def copy(s):
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(s)
    else:
        raise Exception('Platform not supported')


for line in txt.splitlines():
    char_line = [i for i in line]
    string = ''
    indexes = {}
    all_idx = [0]
    for i, char in enumerate(line):
        for p in puntuacion:
            if char == p:
                indexes[i] = p
                all_idx.append(i)

    a, b = 0, 0
    for idx in indexes:
        punt = indexes[idx]
        b = idx
        string += tag_in + ''.join(char_line[a:b]) + tag_out + punt
        a = idx + 1
    output_string += string + '\n'

copy(bytes(output_string, encoding='utf-8'))
