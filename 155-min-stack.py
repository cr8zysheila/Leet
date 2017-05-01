class MinStack(object):
    def __init__(self):
        self.stack = []
        self.mins = []

    def pop(self):
        if not self.stack:
            raise Exception('empty stack!')

        x = self.stack.pop()
        if x == self.mins[-1]:
            self.mins.pop()

        return x

    def push(self, x):
        self.stack.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)

    def top(self):
        if not self.stack:
            raise Exception('empty stack!')

        return self.stack[-1]

    def getMin(self):
        if not self.mins:
            raise Exception('empty stack!')

        return self.mins[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print minStack.getMin()
print minStack.pop()
print minStack.top()
print minStack.getMin()