class CyclicStack:
    def __init__(self, size):
        self.size = size
        self.top = 0                                                        # the top  pointer of the stack
        self.stack = [0]*size                                               # initialize the stack array

    def __len__(self):
        return self.size

    def pop(self):
        self.top = (self.top - 1) % self.size                               # decrement top pointer
        return self.stack[self.top]                                         # return the value on top of the stack

    def push(self, n):
        self.stack[self.top] = n                                            # replace the next value with that of n
        self.top = (self.top + 1) % self.size