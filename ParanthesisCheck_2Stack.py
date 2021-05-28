class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self, data):
        self.stack.append(data)
        return
    def pop(self):
        if self.isEmpty() is True:
            return -1
        else:
            return self.stack.pop()
    def peek(self):
        if self.isEmpty() is True:
            return -1
        else:
        return self.stack[-1]

def paranthesisCheck(self, exp):
    return -1

x = input()
x = '[{()}]'
res = paranthesisCheck(x)
