class Stack:
    def __init__(self):
        self.stack = []
    #Check if Stack is empty
    def isEmpty(self):
        return self.stack == []
    #Adding an element to the top Stack    
    def push(self, data):
        self.stack.append(data)
        return
    #Deleting the top element from the Stack
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    #To check the last element of the Stack    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

def paranthesisCheck(e):
    #If expression is empty, it is considered balanced
    if e == '':
        return True
    
    S = Stack()
    for c in e:
        #Add opening paranthesis to Stack
        if c == '(' or c == '{' or c == '[':
            S.push(c)
            continue
        #If  a closing paranthesis is encountered, but Stack is empty
        #then it is unbalanced
        if S.isEmpty() is True:
            return False
        #If a closing paranthesis is encountered, pop and check if 
        #it is a closing paranthesis, if not, then expression is unbalanced
        if c == ')':
            t = S.pop()
            if t != '(':
                return False   
        if c == '}':
            t = S.pop()
            if t != '{':
                return False    
        if c == ']':
            t = S.pop()
            if t != '[':
                return False
    #If the expression is checked and stack is empty, it is balanced        
    if S.isEmpty() is True:
        return True
exp = input()
#exp = '[{()}]'
for tst in exp:
    if paranthesisCheck(tst) is True:
        print('YES')
    else:
        print('NO')
