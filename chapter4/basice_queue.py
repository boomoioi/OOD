class Queue():
    def __init__(self):
        self.items_size = 0 
        self.items = []
    
    @property
    def size(self):
        return self.items_size

    def deQueue(self):
        if self.items:
            self.items_size -= 1
            print(f"Pop {self.items.pop(0)} size in queue is {self.items_size}")
        else:
            print("-1")
    
    def enQueue(self, val):
        self.items.append(val)
        print(f"Add {val} index is {self.items_size}")
        self.items_size += 1

    def itemLeft(self):
        if self.items:
            print(f"Number in Queue is :  {self.items}")
        else:
            print("Empty")

inp = input("Enter Input : ").split(",")
q = Queue()
for cmd in inp:
    com = cmd.split()[0]
    if com == "E":
        q.enQueue(cmd.split()[1])
    elif com == "D":
        q.deQueue()
q.itemLeft()