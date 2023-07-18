class Stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        return self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


inp = input('Enter Input : ').split(',')
w_list = Stack()
f_list = Stack()

for i in inp:
    weight = int(i.split()[0])
    sound = int(i.split()[1])
    if w_list.isEmpty():
        w_list.push(weight)
        f_list.push(sound)
    else:
        while not w_list.isEmpty() and w_list.peek() < weight:
            print(f_list.pop())
            w_list.pop()
        w_list.push(weight)
        f_list.push(sound)
