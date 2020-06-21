from collections import deque
from source.memory import Memory
from source.process import Process
from source.instructions_management import *
from source.instructions import *
from source.operands import *

class Machine:
    instruction = AbstractInstruction(None, None)
    operand = AbstractOperand(None)

    def __init__(self, program1, program2, max = 0):
        self.max = max
        self.memory = Memory(4095)
        if len(program1) >= 2048 or len(program2) >= 2048:
            raise ValueError
        self.memory.load(program1, 0)
        self.memory.load(program2, 2048)

        self.player1 = deque()
        self.player2 = deque()
        self.player1.appendleft(Process())
        tmp = Process()
        tmp.PC = 2048
        self.player2.appendleft(tmp)

    def status(self):
        if len(self.player1) == 0 and len(self.player2) > 0:
            return 2
        if len(self.player2) == 0 and len(self.player1) > 0:
            return 1
        if len(self.player2) == 0 and len(self.player1) == 0:
            return 0

    def step(self):
        p1 = self.player1.pop()
        p2 = self.player2.pop()
        i1 = idecode(self.memory[p1.PC])
        i2 = idecode(self.memory[p2.PC])
        p1 = self.instruction.create(i1[0],
                                self.operand.create(i1[1][0], i1[1][1]),
                                self.operand.create(i1[2][0], i1[2][1])).exec(self.memory, p1)
        p2 = self.instruction.create(i2[0],
                                self.operand.create(i2[1][0], i2[1][1]),
                                self.operand.create(i2[2][0], i2[2][1])).exec(self.memory, p2)
        self.memory.commit()
        for i in p1:
            self.player1.appendleft(i)
        for i in p2:
            self.player2.appendleft(i)

    def run(self):
        a = self.status()
        if self.max > 0:
            ct = 0
            while not a and ct < self.max:
                self.step()
                a = self.status()
                ct += 1
            return a
        while not a:
            self.step()
            a = self.status()
        return a
