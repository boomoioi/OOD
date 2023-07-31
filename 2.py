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
        newnode = Node(item) # Create new Node
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.previous = self.tail
            self.tail.next = newnode
            self.tail = newnode
        
    def addHead(self, item):
        newnode = Node(item)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.previous = newnode
            self.head = newnode

    # always insert newnode to in front of node
    # 1 2 3 4
    # insert T at 1 :1 T 2 3 4
    # insert T at -2 : 1 2 T 3 4
    def insert(self, pos, item):
        newnode = Node(item)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            if pos == 0:
                self.addHead(item)
            else:
                if pos > 0:
                    cnt = 0
                    currnode = self.head
                    while currnode.next != None and cnt != pos:
                        currnode = currnode.next
                        cnt += 1
                    
                    if cnt < pos :
                        self.append(item)
                    else:
                        newnode.next = currnode
                        newnode.previous = currnode.previous
                        currnode.previous = newnode
                        if newnode.previous != None:
                            newnode.previous.next = newnode
                        else:
                            self.append(item)
                else:
                    cnt = -1
                    currnode = self.tail
                    while currnode.previous != None and cnt != pos:
                        currnode = currnode.previous
                        cnt -= 1

                    if cnt > pos:
                        self.addHead(item)
                    else:
                        newnode.next = currnode
                        newnode.previous = currnode.previous
                        currnode.previous = newnode
                        if newnode.previous != None:
                            newnode.previous.next = newnode
                        else:
                            self.addHead(item)

    def search(self, item):
        if self.head == None:
            return "Not Found"
        
        if self.head.next == None:
            if self.head.value == item:
                return "Found"
            else:
                return "Not Found"


        currnode = self.head
        while currnode.next != None:
            if currnode.value == item:   
                return "Found"
            currnode = currnode.next

        return "Not Found"

    def index(self, item):
        if self.head == None:
            return -1
        
        cnt = 0
        currnode = self.head
        if currnode.value == item:
            return 0
        
        while currnode.next != None:
            if currnode.value == item:
                return cnt
            currnode = currnode.next
            cnt += 1
        return -1

    def size(self):
        if self.head == None:
            return 0
        
        cnt = 1
        currnode = self.head
        while currnode.next != None:
            cnt += 1
            currnode = currnode.next
        return cnt

    def pop(self, pos):
        if self.head == None:
            return "Out of Range"

        if self.size() == 1 and pos == 0:
            delnode = self.head
            self.head = None
            self.tail = None
            del delnode
            return "Success"
        
        if pos == 0:
            delnode = self.head
            self.head = self.head.next
            del delnode
            return "Success"

        if pos == self.size() - 1:
            delnode = self.tail
            self.tail = self.tail.previous
            del delnode
            return "Success"

        cnt = 0
        currnode = self.head
        while currnode.next != None:
            if cnt == pos:
                delNode = currnode
                prevnode = currnode.previous
                nextnode = currnode.next
                if prevnode != None:
                    prevnode.next = nextnode
                if nextnode != None:
                    nextnode.previous = prevnode
                del delNode
                return "Success"
            currnode = currnode.next
            cnt += 1
        return "Out of Range"

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