# 2D - Link List ( pri_node ไม่มีวันที่ pri_node ซ้ำกัน )

# ADN  : add pri_node
# ADSN : add sec_node

class Node:
    def __init__(self,data):
        self.val = data 
        self.next = None
        self.child = None

class Snode:
    def __init__(self,data):
        self.val = data 
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None

    def next_node(self,data):
        if self.search(data) != None:
            return
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:  
            self.tail.next = node
            self.tail = node

    def next_secondary_node(self,n,data):
        node = Snode(data)
        pri_node = self.search(n)
        if pri_node.child == None:
            pri_node.child = node
            return
        cur = pri_node.child
        while cur.next != None:
            cur=cur.next
        cur.next = node

        
    def search(self,data):
        pri = self.head
        while pri != None:
            if pri.val == data:
                return pri
            pri = pri.next
        return None

    def show_all(self):
        pri = self.head
        res = ""
        while pri != None:
            res += pri.val + " : "
            cur = pri.child
            while cur != None:
                res += cur.val + ","
                cur = cur.next
            res += "\n"
            pri = pri.next
        return res
lll = Link()
inp = input("input : ")
for com in inp.split(","):
    if com.split()[0] == "ADN":
        lll.next_node(com.split()[1])
    elif com.split()[0] == "ADSN":
        pri = com.split()[1].split("-")[0]
        data = com.split()[1].split("-")[1]
        lll.next_secondary_node(pri, data)
print(lll.show_all())