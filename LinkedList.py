class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
        
    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def prepend(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return node
    
    def __str__(self):
        res = ""
        cur = self.head 
        while cur != None:
            res += str(cur.val) + " --> "
            cur = cur.next
        return res[:-5]
    
    def __len__(self):
        return self.size
    

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)
print(len(ll))

# test = [1,2,3,4]
# test.insert(1,10)
# print(test)