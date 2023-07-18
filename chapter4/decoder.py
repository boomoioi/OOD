class Queue():
    def __init__(self, items=[]):
        self.items_size = len(items)
        self.items = items
    
    @property
    def size(self):
        return self.items_size

    def deQueue(self):
        if self.items:
            self.items_size -= 1
            return self.items.pop(0)
        return "Empty"
    
    def enQueue(self, val):
        self.items.append(val)
        self.items_size += 1
    
    def isEmpty(self):
        return not self.items

    def __str__(self):
        return f"{self.items}"
    
def encodemsg(q1, q2):
    temp = Queue()
    i=0
    while not q1.isEmpty():
        adder = q2.deQueue()
        q2.enQueue(adder)
        i+=1
        i=i%q2.size
        ch = q1.deQueue()
        if ch.isupper():
            base = 65
        else:
            base = 97
        out_ascii = (ord(ch)-base+adder)%26 + base

        temp.enQueue(chr(out_ascii))
    while i!=0:
        i+=1
        i=i%q2.size
        q2.enQueue(q2.deQueue())
    while not temp.isEmpty():
        q1.enQueue(temp.deQueue())
    print(f"Encode message is :  {q1}")

def decodemsg(q1, q2):
    temp = Queue()
    while not q1.isEmpty():
        adder = q2.deQueue()
        q2.enQueue(adder)

        ch = q1.deQueue()
        if ch.isupper():
            base = 65
        else:
            base = 97
        out_ascii = (ord(ch)-base-adder)%26 + base

        temp.enQueue(chr(out_ascii))
    print(f"Decode message is :  {temp}")



st, nums = input("Enter String and Code : ").split(",")
string = [ch for ch in st if ch.isalpha()]
number = [int(num) for num in nums]

q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)