def b(n):
    b = ''
    if n == 0:
        f = '0'
    else:
        while n > 0:
            r = n%2
            n = n//2
            b += str(r)
        l = list(b)
        l.reverse()
        f = ''.join(l)
    return f

def alphatobin(char):
    L = 'abcdefghijklmnñopqrstuvwxyz '
    i = L.index(char)
    d = b(i)
    return d

def bintoalpha(code):
    L = 'abcdefghijklmnñopqrstuvwxyz '
    dec = d(code)
    i = L[dec]
    return i

def d(b):
    if type(b) is int:
        b = str(b)
    n = 0
    l = len(b)-1
    for i in range(len(b)):
        d = int(b[i])
        p = l-i
        n += d*(2**p)
    return n
