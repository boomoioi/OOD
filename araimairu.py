class Stack():
    def __init__(self,list=None):
        if list == None:self.items = []
        else:self.items = list
    def push(self,value):
        return self.items.append(value)
    def pop(self):
        return self.items.pop()    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')
for i in range(len(inp)):
    if inp[i] == " ":
        S.push(inp[i])
        S.pop()
    elif inp[i] not in "+-*()/^":
        print(inp[i],end="")
        if i==len(inp)-1:
            while S.items:
                print(S.pop(),end="")
    elif i==len(inp)-1 and inp[i]==")":
        while True:
            if S.peek() == "(":
                S.pop()
            elif S.size()>0:
                print(S.pop(),end="")
            else:break
    elif inp[i] == ")":  
        while True:
            if S.peek() == "(":
                S.pop()
                break
            else:
                print(S.pop(),end="")  
    elif inp[i] in "+-" and S.peek() in "*/^" :
        while S.items:
            print(S.pop(),end="")
            if S.peek() == "(":
                break
        S.push(inp[i])
    elif inp[i] in "*/" and S.peek() in "*/":
        print(S.pop(),end="")
        S.push(inp[i])
    elif inp[i] in "+-" and S.peek() in "+-":
        print(S.pop(),end="")
        S.push(inp[i])
    elif inp[i] in "+-(/^*":
        S.push(inp[i])