class Stack:

    def __init__(self, List=None):
        if List == None:
            self.items = []
        else:
            self.items = List

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]


inp = input('Enter Infix : ')

S = Stack()
sym = ["+", "-", "*", "/", "^"]
piority = [1, 1, 2, 2, 3]

print('Postfix : ', end='')

### Enter Your Code Here ###
for char in inp:
    if char.isalpha():
        print(char, end='')
        pass
    else:
        if char == ')':
            while not S.isEmpty() and S.peek() != '(':
                print(S.pop(), end='')
            S.pop()
        elif char == '(':
            S.push(char)
        else:
            while not S.isEmpty() and S.peek() != '(' and piority[sym.index(char)] <= piority[sym.index(S.peek())]:
                print(S.pop(), end='')
            S.push(char)

while not S.isEmpty():
    print(S.pop(), end='')

print()
