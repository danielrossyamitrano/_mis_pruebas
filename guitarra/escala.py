class Escala:
    _notas = ['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si']
    notas = []
    def __init__(self, tonica):
        if tonica in self._notas:
            idx = self._notas.index(tonica)
            self.tonica = tonica

        elif type(tonica) is int:
            idx = tonica
            self.tonica = self._notas[tonica]

        else:
            raise TypeError('La nota indicada es inválida')
        
        self.notas = self._notas[idx:]+self._notas[:idx]+[self.tonica]

    def __getitem__(self, key):
        if type(key) is int:
            return self.notas[key]
        if type(key) is str:
            idx = self.notas.index(key)
            return idx

    def __repr__(self):
        return self.tonica

class Acorde:
    mayor = {1:0,2:2,3:4,4:5,5:7,6:9,7:11,8:12}
    menor = {1:0,2:2,3:3,4:5,5:7,6:8,7:10,8:12}
    tonos = {'Mayor':mayor,'Menor':menor,'M':mayor,'m':menor}
    
    def __init__(self, escala, modo='Mayor', septima=False):
        self.notas = []
        notas = [1,3,5]
        if septima: 
            notas.append(7)
            
        for n in notas:
            self.notas.append(escala[self.tonos[modo][n]])
    
    def __repr__(self):
        return ','.join(self.notas)

def descifrar(codigo):
    cifrado = {'A':'La','B':'Si','C':'Do','D':'Re','E':'Mi','F':'Fa','G':'Sol'}
    args = [cifrado[codigo[0]],'Mayor']
    if '#' in codigo:
        args[0] += '#'
    if 'm' in codigo:
        args[1] = 'Menor'
    if '7' in codigo:
        args.append(True)

    return args

def cifrar(nota,modo,septima):
    cifrado = {'La':'A','Si':'B','Do':'C','Re':'D','Mi':'E','Fa':'F','Sol':'G'}
    codigo = ''
    
    if '#' in nota:
        codigo = cifrado[nota[:-1]] + "#"
    else:
        codigo = cifrado[nota]
        
    if modo == 'Menor' or modo == 'm':
        codigo += 'm'
    if septima:
        codigo += '7'

    return codigo

