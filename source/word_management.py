def binpad(x, n = 0):
    assert(0 <= x)
    return '0b' + f'{x:0b}'.rjust(n, '0')

def extract(w, m, n):
    up = 2**(m+n-1)
    lo = 2**(m)

    tmp = w % up
    tmp = tmp // lo

    return tmp, bin(tmp)