class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return "items is empty."
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


def postFixeval(st):

    s = Stack()
    sym = ['+', '-', '*', '/']
    for ch in st:
        if ch in sym:
            second = str(s.pop())
            first = str(s.pop())
            s.push(eval(first+ch+second))
        else:
            s.push(int(ch))
    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))