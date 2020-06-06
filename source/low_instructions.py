from source.word_management import *
from source.bit_management import *

def eval_ADD(w1, w2):
    return (w1 + w2) % (2**32)

def eval_SUB(w1, w2):
    return (w1 - w2) % (2**32)

def eval_NOT(w):
    for i in range(32):
        w = bit_toggle(w, i)
    return w

def eval_AND(w1, w2):
    return w1 & w2

def eval_OR(w1, w2):
    return w1 | w2

def eval_LS(a, w):
    i = to_signed(a, 32)
    return w >> i if i >= 0 else (w << -i) % (2**32)

def eval_AS(a, w):
    i = to_signed(a, 32)
    if i < 0:
        return (w << -i) % (2**32)
    # if i > 32:
    #     print(binpad(w, 31))
    #     return extract(w, 31, 1) * sum([2**j for j in range(32)])
    for j in range(i):
        w = (w >> 1) + (extract(w, 31, 1) * 2**31)
    return w

def eval_CMP(w1, w2):
    return w1 == w2

def eval_LT(w1, w2):
    w1 = to_signed(w1, 32)
    w2 = to_signed(w2, 32)
    return w1 < w2
