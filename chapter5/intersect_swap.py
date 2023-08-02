class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
      
    def append(self, node):
        if self.head == None:
            self.head = node
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        return node

    def prepend(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return node
    
    def unconnect(self, node):
        cur = self.head
        seen = set()
        while cur != None and cur not in seen:
            if cur.next == node:
                cur.next = None
                break
            seen.add(cur)
            cur = cur.next

    def nodeAt(self, count):
        cur = self.head
        seen = set()
        i =  0
        while cur != None and cur not in seen:
            if i==count:
                return cur.val
            i+=1
            seen.add(cur)
            cur = cur.next
        return None
    
    def __contains__(self, node):
        cur = self.head
        seen = set()
        while cur != None and cur not in seen:
            if cur == node:
                return True
            seen.add(cur)
            cur = cur.next
        return False
    
    def __str__(self):
        res = ""
        cur = self.head
        seen = set()
        while cur != None and cur not in seen:
            res += str(cur.val) + " --> "
            seen.add(cur)
            cur = cur.next
        return res[:-5]

    def __len__(self):
        cur = self.head
        seen = set()
        count = 0
        while cur != None and cur not in seen:
            seen.add(cur)
            count+=1
            cur = cur.next
        return count
  
class NodeContainer:
    def __init__(self):
        self.nodes = []
   
    def getNode(self, val):
        for node in self.nodes:
            if node.val == val:
                return node
        return None
   
    def append(self, node):
        self.nodes.append(node)
   
    def __iter__(self):
        for node in self.nodes:
            yield node
    
    def __len__(self):
        return len(self.nodes)
   
    def __contains__(self, val):
        for node in self.nodes:
            if node.val == val:
                return True
        return False
    
    def __str__(self):
        res = ""
        for node in self.nodes:
            res += str(node.val) + " "
        return res
    
def sorter(ll_list):
    nums = []
    res = []
    for ll in ll_list:
        nums.append(ll.head.val)
    nums.sort()
    for num in nums:
        for ll in ll_list:
            if ll.head.val == num:
                res.append(ll)
    return res
   
def deleteIntersect(intersect, ll_list):   
    for ll_in in intersect:
        in_node = ll_in.head
        new_head = in_node.next
        for index, ll in enumerate(ll_list):
            if ll.head in ll_in:
                del ll_list[index]
                break
        if new_head:
            ll_list.append(LinkedList(new_head))
        for ll in ll_list:
            ll.unconnect(in_node)
    return ll_list
    
def showMerge(ll_list):
    ll_list = sorter(ll_list)
    print("Delete intersection then swap merge:")
    count = 0 
    res = ""
    while(True):
        check = 1
        for ll in ll_list:
            if ll.nodeAt(count) != None:
                res += str(ll.nodeAt(count)) + " -> "
                check = 0 
        if check:
            break
        count += 1
    print(res[:-4])
 
def deleteUnrelevant(intersect, ll_list):
    temp = []
    for ll in ll_list:
        check = 0
        for ll_in in intersect:
            if ll_in.head in ll:
                check = 1 
        if check:
            temp.append(ll)
    return temp
 
def solve(commands):
    node_list = NodeContainer()
    intersect = []
    ll_list = []
    be_pointed = set()
    
    #create all linked list
    for command in commands:
        #initialize node
        first = int(command.split(">")[0])
        second = int(command.split(">")[1])
        if first not in node_list:
            node = Node(first)
            ll_list.append(LinkedList())
            ll_list[-1].append(node)
            node_list.append(node)
        if second not in node_list:
            node_list.append(Node(second))
            
        #get node    
        first_node = node_list.getNode(first)
        second_node = node_list.getNode(second)
        
        #merge head
        for index, ll in enumerate(ll_list):
            if ll.head == second_node and first_node not in ll:
                del ll_list[index]
                break
        
        #check intersect
        if second not in be_pointed:
            be_pointed.add(second)
        else: 
            intersect.append(LinkedList(second_node))
            
        first_node.next = second_node

    #print node size
    intersect = sorter(intersect)
    if intersect:
        for ll in intersect:
            print(f"Node({ll.head.val}, size={len(ll)})")
    else:
        print("No intersection")
        return 
    
    ll_list = deleteUnrelevant(intersect, ll_list)
    ll_list = deleteIntersect(intersect, ll_list)
    showMerge(ll_list)
                


#driver
inp = input("Enter edges: ").split(",")
solve(inp)