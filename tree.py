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
    
    def peek(self):
        return self.items[-1]

def put_back(temp, stack):
    while not temp.isEmpty():
        stack.push(temp.pop())

def count(stack):
    counter = Stack()
    max = 0
    count = 0
    while not stack.isEmpty():
        popper = stack.pop()
        if popper > max:
            max = popper
            count+=1
        counter.push(popper)
    put_back(counter, stack)
    print(count)

def edit(stack):
    temp = Stack()
    while not stack.isEmpty():
        popper = stack.pop()
        if popper%2 == 0:
            popper -= 1
            if popper < 1:
                popper = 1
        else:
            popper += 2
        temp.push(popper)
    put_back(temp, stack)


def player(inp):
    stack = Stack()
    for opers in inp:
        oper = opers.split(" ")[0]
        if oper == 'A':
            num = opers.split(" ")[1]
            stack.push(int(num))
        elif oper == 'B':
            count(stack)
        elif oper == 'S':
            edit(stack)


inp = input("Enter text : ").split(",")
player(inp)