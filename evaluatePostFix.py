class Solution:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()
    def top(self):
        if self.stack == []:
            return -1
        else:
            return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    
    def evalPost(self, exp):
        stack = []
        for c in exp:
            #Operands are added to stack
            if c.isalnum():
                self.push(c)
            #Pop 2 elements and evaluate 
            else:
                v1 = self.pop()
                v2 = self.pop()
                #print(v2,c,v1)
                v3 = str(eval(v2 + c + v1))
                #Add the new value to stack and repeat
                self.push(v3)
        return self.top()
    
S = Solution()
s1 = '123+*8-'
s2 = '231*+9-'
print(S.evalPost(s1))
print(S.evalPost(s2))
