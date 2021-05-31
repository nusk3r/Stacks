class Solution:
    def __init__(self):
        self.stack = []
    
    def push(self, n):
        self.stack.append(n)
        
    def isEmpty(self):
        return self.stack == []
        
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
            
    def InfixtoPostfix(self, exp):
        opPrec = {'(':0, '+':1, '-':1,'*':2,'/':2,'^':3}

        result = ''
        
        for c in exp:
            #Operand is added to result
            if c.isalnum():
                result += c
            #Opening brace added to stack    
            elif c == '(':
                self.push(c)
            #If closing brace, pop until you find it opening pair
            elif c == ')':
                x = self.pop()
                while x != '(':
                    result += x
                    x = self.pop()
            #Operator, check its precedency in the dictionary
            else:
                #Pop from the stack until the top's precedency is higher
                while(self.isEmpty() is not True and opPrec[c] <= opPrec[self.top()]):
                    result += self.top()
                    self.pop()
                self.push(c)
        #Lastly, print any operators if present in stack
        while(self.isEmpty() is not True):
            result += self.top()
            self.pop()
                
        return result
            
ss = Solution()

s3 = '(a+b+c)/d'
s2 = '(2*3+4*(5-6))'
s1 = 'A*(B+C)/D'

print('Postfix: ', ss.InfixtoPostfix(s1))

print('Postfix: ', ss.InfixtoPostfix(s2))

print('Postfix: ', ss.InfixtoPostfix(s3))
