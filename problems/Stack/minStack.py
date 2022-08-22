# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
class MinStack(object):
    def __init__(self):
        self.stacks = []
        self.minStacks = []
        

    def push(self, val):
        self.stacks.append(val)
        if not self.minStacks or self.minStacks[-1] >= val:
            self.minStacks.append(val)
        

    def pop(self):
        if self.stacks[-1] == self.minStacks[-1]:
            self.minStacks.pop()
        return self.stacks.pop()
        

    def top(self):
        return self.stacks[-1]
        

    def getMin(self):
        return self.minStacks[-1]
