def to_binary(decimal, size=8):
    seq = []
    while decimal > 0:
        seq.append(str(decimal % 2))
        decimal //= 2

    # add leading 0s to fit size
    seq += ['0'] * (size - len(seq))

    # reverse, join and return
    return ''.join(reversed(seq))


def to_decimal(b):
    n = 0
    for i, s in enumerate(reversed(b)):
        n += ((2 ** i) * int(s))
    return n


def alphatobin(char):
    letters = 'abcdefghijklmnñopqrstuvwxyz '
    i = letters.index(char)
    d = to_binary(i)
    return d


def bintoalpha(code):
    letters = 'abcdefghijklmnñopqrstuvwxyz '
    dec = to_decimal(code)
    i = letters[dec]
    return i
