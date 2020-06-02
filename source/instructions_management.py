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

def resolve_writes(base, xs):
    chg = [i for i in combinations(xs+[base], 3)]
    ret = chg.pop()
    ret = ((ret[0] & ret[1]) & (ret[1] & ret[2])) | ((ret[0] & ret[1]) & (ret[0] & ret[2])) | ((ret[0] & ret[1]) & (ret[1] & ret[2]))
    for i in chg:
        ret = ret | ((i[0] & i[1]) & (i[1] & i[2])) | ((i[0] & i[1]) & (i[0] & i[2])) | ((i[0] & i[1]) & (i[1] & i[2]))
    print(bin(ret))
    return ret