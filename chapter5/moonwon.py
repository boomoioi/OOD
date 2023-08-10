class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        if self.head.val.isnumeric():
            cur, s = self.head, str(self.head.val) + " <-> "
            while cur.next != None:
                s += str(cur.next.val) + " <-> "
                cur = cur.next
            return s[:-5]
        else:
            cur, s = self.head, str(self.head.val) + " > "
            while cur.next != None:
                s += str(cur.next.val) + " > "
                cur = cur.next
            return s[:-3]

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
            
    def reverseByK(self, k):
        cur = self.head
        temp = None
        check =  0
        while cur != None:           
            first = cur 
            for i in range(k):
                t = cur.next
                cur.next = cur.previous
                cur.previous = t
                last = cur
                cur = cur.previous
                if cur == None:
                    break
            #left
            if not temp:
                self.head = last
            else:
                temp.next = last
            last.prev = temp
            first.next = cur
            temp = first
            
ll = LinkedList()
inp = input("Enter the elements of Linked list/group's size: ")
for data in inp.split("/")[0].split():
    ll.append(data)
k = int(inp.split("/")[1])
if ll.head == None:
    print("No elements in Linked List ? OK!")
    print("Group' size should be greater than 0")
    exit()
if k<=0:
    print("Group' size should be greater than 0")
    exit()
print()

print("Original Linked list:" ,ll)
ll.reverseByK(k)
print("Modified Linked list:", ll)
