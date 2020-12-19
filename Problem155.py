# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Methods pop, top and getMin operations will always be called on non-empty stacks.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        min_value = min(x, self.min_values[0]) if len(self.min_values) else x
        self.min_values.insert(0, min_value)

    def pop(self) -> None:
        self.stack.pop(0)
        self.min_values.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_values[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
