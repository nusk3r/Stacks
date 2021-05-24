class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
        return
    
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

s = Stack()
s.push(30)
print(s.peek())
s.push(20)
s.push(10)
print(s.peek())
s.pop()
print(s.peek())
s.pop()
s.pop()
s.pop()
print(s.peek())
print(s.pop())
