def bit_set(w, i):
    return w | (0b1 << i)

def bit_clear(w, i):
    return w & (~ (0b1 << i))

def bit_toggle(w, i):
    return w ^ (0b1 << i)