from source.cyclic_stack import CyclicStack

class Process:
    def __init__(self):
        self.registers = [0] * 16                # registers
        self.stack = CyclicStack(16)
        self.PC = 0
        self.Z = 0