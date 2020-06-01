class CyclicStack:
    def __init__(self, size):
        self.size = size
        self.top = 0                                                        # the top  pointer of the stack
        self.stack = [None]*size                                            # initialize the stack array

    def __len__(self):
        return self.size

    def pop(self):
        tmp = None
        tmp, self.stack[self.top] = self.stack[self.top], tmp               # replace the last value with None
        self.top = (self.top - 1) % 16                                      # decrement top pointer
        return tmp                                                          # return the popped value

    def push(self, n):
        self.top = (self.top + 1) % 16
        self.stack[self.top] = n                                            # replace the next value with that of n

