# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Min Stack.py
# Creation Time: 2017/7/30
###########################################
'''
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
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minstack) == 0 or self.minstack[-1][0] > x:
            self.minstack.append((x, 1))
        elif self.minstack[-1][0] == x:
            self.minstack[-1] = (x, self.minstack[-1][1] + 1)

    def pop(self):
        """
        :rtype: void
        """
        ans = self.stack[-1]
        self.stack = self.stack[0:len(self.stack) - 1]
        if ans == self.minstack[-1][0]:
            if self.minstack[-1][1] == 1:
                self.minstack.remove(self.minstack[-1])
            else:
                self.minstack[-1] = (ans, self.minstack[-1][1] - 1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1][0]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()