def binpad(x, n = 0):
    assert(0 <= x)
    return '0b' + f'{x:0b}'.rjust(n, '0')

def extract(w, m, n):
    up = 2**(m+n-1)                                         # MSB of the subword
    lo = 2**(m)                                             # LSB of the subword

    tmp = w % up                                            # remove all before subword
    tmp = tmp // lo                                         # remove all after subword

    return tmp, bin(tmp)

def to_signed(w, n):
    return w if w&2**(n) == 0 else w - 2**(n+1)

def of_signed(i, n):
    return i + 2**(n+1) if i < 0 else i


