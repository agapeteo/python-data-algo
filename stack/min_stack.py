class MinStack():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, in_value):
        if len(self.stack) == 0 or in_value <= self.min_stack[-1]:
            self.min_stack.append(in_value)
        self.stack.append(in_value)

    def pop(self):
        result = self.stack.pop()
        if result == self.min_stack[-1]:
            self.min_stack.pop()
        return result

    def min(self):
        return self.min_stack[-1]


min_stack = MinStack()
min_stack.push(1)
min_stack.push(2)
min_stack.push(0)
min_stack.push(0)
min_stack.push(-1)
min_stack.push(3)

assert min_stack.min() == -1
min_stack.pop()
min_stack.pop()
assert min_stack.min() == 0
min_stack.pop()
assert min_stack.min() == 0
min_stack.pop()
assert min_stack.min() == 1
