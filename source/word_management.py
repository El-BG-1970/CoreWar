def binpad(x, n = 0):
    assert(0 <= x)
    return '0b' + f'{x:0b}'.rjust(n, '0')