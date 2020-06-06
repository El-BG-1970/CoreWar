from source.low_instructions import *

class AbstractInstruction:
    def __init__(self, operandA, operandB):
        self.operandA = operandA
        self.operandB = operandB

    def exec(self, memory, process):
        raise NotImplementedError

    @staticmethod
    def create(opcode, operandA, operandB):
        return {
            0b0000: FORK,
            0b0001: MOV,
            0b0010: NOT,
            0b0011: AND,
            0b0100: OR,
            0b0101: LS,
            0b0110: AS,
            0b0111: ADD,
            0b1000: SUB,
            0b1001: CMP,
            0b1010: LT,
            0b1011: POP,
            0b1100: PUSH,
            0b1101: JMP,
            0b1110: BZ,
            0b1111: DIE}[opcode](operandA, operandB)


class FORK(AbstractInstruction):
    def exec(self, memory, process):
        process.Z = 0
        process.PC = (process.PC + 1) % len(memory)


class MOV(AbstractInstruction):
    def exec(self, memory, process):
        self.operandB.write(memory, process, self.operandA.read(memory, process))
        process.PC = (process.PC + 1) % len(memory)


class NOT(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_NOT(self.operandA.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class AND(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_AND(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class OR(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_OR(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class LS(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_LS(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class AS(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_AS(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class ADD(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_ADD(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class SUB(AbstractInstruction):
    def exec(self, memory, process):
        tmp = eval_SUB(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.Z = tmp == 0
        self.operandB.write(memory, process, tmp)
        process.PC = (process.PC + 1) % len(memory)


class CMP(AbstractInstruction):
    def exec(self, memory, process):
        process.Z = eval_CMP(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.PC = (process.PC + 1) % len(memory)


class LT(AbstractInstruction):
    def exec(self, memory, process):
        process.Z = eval_LT(self.operandA.read(memory, process), self.operandB.read(memory, process))
        process.PC = (process.PC + 1) % len(memory)


class POP(AbstractInstruction):
    def exec(self, memory, process):
        self.operandA.write(memory, process, process.stack.pop())
        process.PC = (process.PC + 1) % len(memory)


class PUSH(AbstractInstruction):
    def exec(self, memory, process):
        process.stack.push(self.operandA.read(memory, process))
        process.PC = (process.PC + 1) % len(memory)


class JMP(AbstractInstruction):
    def exec(self, memory, process):
        process.PC = (process.PC + self.operandA.read(memory, process)) % len(memory)


class BZ(AbstractInstruction):
    def exec(self, memory, process):
        process.PC = (process.PC + (self.operandA.read(memory, process) if process.Z else 1)) % len(memory)


class DIE(AbstractInstruction):
    def exec(self, memory, process):
        pass

