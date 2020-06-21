#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

def to_signed(w, n):
    return w if (w&2**(n-1) == 0) else w - 2**(n)

def of_signed(i, n):
    return i + 2**(n) if i < 0 else i

#list of valid instructions
valid = ['FORK', 'MOV', 'NOT', 'AND', 'OR', 'LS', 'AS', 'ADD', 'SUB', 'CMP', 'LT', 'POP', 'PUSH',
         'JMP', 'BZ', 'DIE']

#for the index corresponding to the instruction in the list 'valid', this one tells if the first and second operands are used
valid_operands = {
    'FORK': ([],[]),
    'MOV': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'NOT': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'AND': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'OR': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'LS': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'AS': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'ADD': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'SUB': (['$', '@', '#', 'r'],['@', '#', 'r']),
    'CMP': (['$', '@', '#', 'r'],['$', '@', '#', 'r']),
    'LT': (['$', '@', '#', 'r'],['$', '@', '#', 'r']),
    'POP': (['@', '#', 'r'],[]),
    'PUSH': (['$', '@', '#', 'r'],[]),
    'JMP': (['$', '@', '#', 'r'],[]),
    'BZ': (['$', '@', '#', 'r'],[]),
    'DIE': ([], [])
}

#$ (immediate), @ (relative), # (computed) or r (register)
mode_list = ['$', '@', '#', 'r']
        
def readlines(filename):
    with open(filename, 'r') as stream:
        for line in stream:
            yield line.rstrip('\r\n')
            
def strip_comment(line):
    '''
    -Remove its comment (i.e. the ; ... part)
    -Remove any leading or trailing space 
    -Return the obtained line if it is not empty – otherwise, the function returns None.
    '''
    if line == '':
        return None
    else:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == ';':
                return line[:i].strip()
        return line

def strip_comment(line): ### elouan ver
    '''
    -Remove its comment (i.e. the ; ... part)
    -Remove any leading or trailing space
    -Return the obtained line if it is not empty – otherwise, the function returns None.
    '''
    line = line.strip()
    for i in range(len(line)):
        if line[i] == ";":
            line = line[:i].strip()
            return line if line else None
    return line if line else None

def extract_label(line, lineno, labels):
    '''
    -Extract label(&...:) and returns new line 
    -In dictionnary labels, associate the extracted label(&...) to lineno. 
     Note that if &xxx is already defined, this is an error and your function should raise an exception
    '''
    #verifier si code le plus efficace
    #note
    res = line.split(':')
    if len(res) == 2:
        labels[res[0].strip()] = lineno
        return res[1].strip()
    else:
        return res[0].strip()

        
def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def parse_operand(oprd, index, labels):
    operand_mode = oprd[0]
    operand_value = oprd[1:]
    
    if is_integer(operand_value):#operand value is an integer
        operand_value = int(oprd[1:]) % (2**12)
    else: #operand value is a label
        operand_value = (labels[operand_value] - index)
        operand_value = (operand_value % (2**12)) if operand_value > 0 else of_signed(operand_value, 12)
    
    return (operand_mode, operand_value)
        

def parse_instruction(txt, index, labels):
    res = txt.split(' ')
    res = [x for x in res if x != '']
    instruction = res[0]
    
    if len(res) == 1:
        return (instruction, None, None)
    
    if len(res) == 2:
        operand1 = parse_operand(res[1], index, labels)
        return (instruction, operand1, None)
    
    if len(res) == 3:
        operand1 = parse_operand(res[1], index, labels)
        operand2 = parse_operand(res[2], index, labels)
        return (instruction, operand1, operand2)
            

def validate_instruction(parsed_instruction):
    '''Check if:
    -the instruction name is valid
    -the number of operands matches the expected one
    -the operands make sense for the instruction 
    (essentially, you should check wether an operand is writable when the instruction needs to write it).
    -Otherwise: raise Exception
    '''
    instruction = parsed_instruction[0]
    if instruction not in valid:
        raise Exception("This is not a valid instruction")
        
    else:
        # index = valid.index(instruction)
        
        for i in range(1,3): #check for the first and the second operand
            #if the instruction requires this operand but there isn't one in the input
            if parsed_instruction[i] and parsed_instruction[i][0] not in valid_operands[instruction][i-1]:
                raise Exception("Input operands of incorrect number or type")


def instruction_name_code(name):
    return valid.index(name)

def operand_mode_code(mode):
    return mode_list.index(mode)

def instruction_code(parse_instruction):
    instruction = 0
    instruction += instruction_name_code(parse_instruction[0])
    if parse_instruction[1]:
        instruction += operand_mode_code(parse_instruction[1][0]) * (2**4)
        instruction += (parse_instruction[1][1] | 0) * (2 ** 8)
    if parse_instruction[2]:
        instruction += operand_mode_code(parse_instruction[2][0]) * (2 ** 6)
        instruction += (parse_instruction[2][1] | 0) * (2**20)
    return instruction

def assembler(filename):
    labels, lineno, src, codes, aout = {}, 0, [], [], bytearray()
    with open(filename, 'r') as stream:
        for line in stream:
            line = strip_comment(line)
            if line is not None:
                src.append(extract_label(line, lineno, labels))
                lineno += 1
    for i, line in enumerate(src):
        instr = parse_instruction(line, i, labels)
        validate_instruction(instr)
        codes.append(instruction_code(instr))
    for i in codes:
        aout.extend(int.to_bytes(i, 4, 'little'))
    return bytes(aout)
    
               
if __name__ == "__main__":
    args = [str(i) for i in sys.argv[1:]]
    if len(args) == 0:
        print("syntax: python assembler.py <source> <executable>")
        sys.exit(-1)
    elif len(args) == 1:
        if not os.path.exists(args[0]):
            print('invalid source file')
            sys.exit(-1)
        with open(args[0].split('.')[0]+'.cor', 'wb') as stream:
            stream.write(assembler(args[0]))
    elif len(args) == 2:
        if not os.path.exists(args[0]):
            print('invalid source file')
            sys.exit(-1)
        with open(args[1], 'wb') as stream:
            stream.write(assembler(args[0]))
    else:
        print("too many options")
        sys.exit(-1)
