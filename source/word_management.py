def binpad(x, n = 0):
    assert(0 <= x)
    return '0b' + f'{x:0b}'.rjust(n, '0')

def extract(w, m, n):
    w = w >> m
    tmp = w %(2**(n))
    return tmp

def to_signed(w, n):
    return w if (w&2**(n-1) == 0) else w - 2**(n)

def of_signed(i, n):
    return i + 2**(n) if i < 0 else i


