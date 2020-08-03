txt = open('text.txt', 'r', encoding='utf-8').read()
output = open('format.txt', 'wt', encoding='utf-8')

tag_in = '[COLOR=rgb(183, 28, 28)]'
tag_out = '[/COLOR]'
puntuacion = [',', '.', ';', ':', '{', '}', '[', ']', ')', '(', '¿', '?', '¡', '!', '+', '-', '=', '*', '/']

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
        punt = indexes[idx]  # ,
        b = idx
        string += tag_in + ''.join(char_line[a:b]) + tag_out + punt
        a = idx + 1
    output.write(string + '\n')

output.close()
