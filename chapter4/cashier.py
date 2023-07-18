class Queue():
    def __init__(self, max_size=1000):
        self.items_size = 0 
        self.items = []
        self.max_size = max_size
    
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

    def isFull(self):
        return self.items_size == self.max_size
    
    def isEmpty(self):
        return not self.items

    def __str__(self):
        return f"{self.items}"
    

word, minu = input("Enter people and time : ").split()
minu = int(minu)
all = Queue()
for ch in word:
    all.enQueue(ch)
cashier_1 = Queue(5)
cashier_2 = Queue(5)
first_en, sec_en = None, None

for i in range(1,minu+1):
    
    if first_en and i-first_en == 3:
        cashier_1.deQueue()
        first_en = i
    if sec_en and i-sec_en == 2:
        cashier_2.deQueue()
        sec_en = i

    if not all.isEmpty():
        ch = all.deQueue()
        if not cashier_1.isFull():
            cashier_1.enQueue(ch)
            if not first_en:
                first_en = i
        else:
            cashier_2.enQueue(ch)
            if not sec_en:
                sec_en = i
            
    print(i, all, cashier_1, cashier_2)