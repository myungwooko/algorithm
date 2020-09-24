"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        self.min.append(min(self.min[-1],
                            x)) if self.min else self.min.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        return self.min[-1]
