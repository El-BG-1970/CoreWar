from itertools import combinations
from source.word_management import *
from source.bit_management import *

def idecode(w):
    opcode = extract(w, 0, 4)
    modeA = extract(w, 4, 2)
    modeB = extract(w, 6, 2)
    operandA = extract(w, 8,12)
    operandB = extract(w, 20, 12)
    return (opcode, (modeA, operandA), (modeB, operandB))

# def resolve_writes(base, xs):
#     # chg = [i for i in combinations(xs, 3)] if (len(xs) % 2 == 1) else [i for i in combinations(xs+[base], 3)]
#     chg = [i for i in combinations(xs+[base], 3)]
#     ret = chg[0]
#     ret = ((ret[0] & ret[1]) | (ret[1] & ret[2])) | \
#           ((ret[1] & ret[2]) | (ret[0] & ret[2])) | \
#           ((ret[0] & ret[1]) | (ret[0] & ret[2]))
#     ret = sum([2**i for i in range(32)])
#     ret = 0
#     for i in chg:
#         ret = ret | (((i[0] | i[1]) & (i[1] | i[2])) & \
#                     ((i[1] | i[2]) & (i[0] | i[2])) & \
#                     ((i[0] | i[1]) & (i[0] | i[2])))
#     # here ret is the majority of all the elements of xs
#     return ret

def resolve_writes(base, xs):
    for i in range(32):
        ct = [0, 0]
        for j in xs:
            ct[extract(j, i, 1)] += 1
        if ct[1] > ct[0]:
            base = bit_set(base, i)
        if ct[0] > ct[1]:
            base = bit_clear(base, i)
    return base

