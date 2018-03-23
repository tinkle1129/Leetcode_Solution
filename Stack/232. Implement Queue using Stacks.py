# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Implement Queue using Stacks.py
# Creation Time: 2018/3/8
###########################################
'''
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2):
            return self.stack2.pop()
        while (self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if len(self.stack2):
            return self.stack2[-1]
        while (self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return self.stack1 == [] and self.stack2 == []