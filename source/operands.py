from source.word_management import *

class InvalidOperation(Exception):
    pass

class AbstractOperand:
    def __init__(self, value):
        self.value = value

    def read(self, memory, process):
        raise InvalidOperation

    def write(self, memory, process, value):
        raise InvalidOperation

    @staticmethod
    def create(opmode, opvalue):
        child = {
            0: ImmediateOperand,
            1: RelativeOperand,
            2: ComputedOperand,
            3: RegisterOperand
        }
        return child[opmode](opvalue)


class ImmediateOperand(AbstractOperand):
    def read(self, memory, process):
        return of_signed(to_signed(self.value, 12), 32)


class RegisterOperand(AbstractOperand):
    def read(self, memory, process):
        return process.registers[self.value % 16]

    def write(self, memory, process, value):
        process.registers[self.value % 16] = value


class RelativeOperand(AbstractOperand):
    def read(self, memory, process):
        return memory[process.PC + to_signed(self.value, 12)]

    def write(self, memory, process, value):
        memory[process.pc + to_signed(self.value, 12)] = value


class ComputedOperand(AbstractOperand):
    def read(self, memory, process):
        l = to_signed(memory[process.PC + to_signed(self.value, 12)] % (2**12), 12)
        return memory[process.PC + l]

    def write(self, memory, process, value):
        l = to_signed(memory[process.PC + to_signed(self.value, 12)], 12)
        memory[process.PC + l] = value