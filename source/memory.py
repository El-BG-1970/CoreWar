from source.instructions_management import *

class Memory:
    def __init__(self, size):
        self.memory = [0]*size
        self.pending = {}
        self.length = size

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return self.memory[idx % len(self)]

    def __setitem__(self, idx, value):
        idx = idx % len(self)
        if idx in self.pending:
            self.pending[idx].append(value)
        else:
            self.pending[idx] = [value]

    def writes(self):
        return self.pending

    def commit(self):
        for i in self.pending:
            self.memory[i] = resolve_writes(self.memory[i], self.pending[i])

        self.pending = {}

    def load(self, data, offset):
        idx = offset % len(self)
        for i in data:
            self.memory[idx] = i
            idx = (idx + 1) % len(self)