class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        if self.head == None: 
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            
    def addHead(self, item):
        node = Node(item)
        if self.head == None: 
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def insert(self, pos, item):
        if pos == 0 or self.head == None:
            self.addHead(item)
        else:
            node = Node(item)
            cur = self.head
            i = 0
            while cur.next != None:
                if pos-1 == i:
                    node.next = cur.next
                    cur.next.previous = node
                    node.previous = cur
                    cur.next = node
                    return
                i+=1
                cur = cur.next
            self.append(item)

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        i=0
        while cur != None:
            if cur.value == item:
                return i
            i+=1
            cur = cur.next
        return -1

    def size(self):
        cur = self.head
        i=0
        while cur != None:
            i+=1
            cur = cur.next
        return i

    def pop(self, pos):
        if pos<0 or self.head==None or pos>=self.size():
            return "Out of Range"
        if pos == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head.next.previous = None
                self.head = self.head.next
        else:
            cur = self.head
            i = 0 
            while cur.next != self.tail:
                if pos-1 == i:
                    cur.next.next.previous = cur 
                    cur.next = cur.next.next
                i += 1
                cur = cur.next 
            if pos-1 == i: 
                cur.next = None
                self.tail = cur
        return "Success"
            
        

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())