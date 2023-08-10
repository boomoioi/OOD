class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None 

    def countStation(self, direction, val): 
        cur = self
        i=0
        if direction == "F":
            while cur.val != val:
                i += 1
                cur = cur.next 
        else:
            while cur.val != val:
                i += 1
                cur = cur.prev
        return i 
    
    def append(self, node):
        self.next = node
        node.prev = self
        
    def printForward(self, des):
        cur = self
        seen = set()
        res = ""
        while cur!=None and cur not in seen:
            seen.add(cur)
            res += cur.val + "->"
            if cur.val == des:
                break
            cur = cur.next
        return res[:-2]
    def printBackward(self, des):
        cur = self
        seen = set()
        res = ""
        while cur!=None and cur not in seen:
            seen.add(cur)
            res += cur.val + "->"
            if cur.val == des:
                break
            cur = cur.prev
        return res[:-2]

inp = input("***Railway on route***\nInput Station name/Source, Destination, Direction(optional): ")
stations = inp.split("/")[0].split(",")
S = inp.split("/")[1].split(",")[0]
G = inp.split("/")[1].split(",")[1]
D = None
if len(inp.split("/")[1].split(",")) > 2:
    D = inp.split("/")[1].split(",")[2]
nodes = [Node(station) for station in stations]
nodes_dict = {}
for i in range(len(nodes)):
    nodes[i].append(nodes[(i+1)%len(nodes)])
    nodes_dict.update({nodes[i].val : nodes[i]})
    
if not D:
    if nodes_dict[S].countStation("F", G) < nodes_dict[S].countStation("B", G):
        print("Forward Route: " + nodes_dict[S].printForward(G) ,end=",")
        print(nodes_dict[S].countStation("F", G))
    elif nodes_dict[S].countStation("F", G) > nodes_dict[S].countStation("B", G):
        print("Backward Route: " + nodes_dict[S].printBackward(G) ,end=",")
        print(nodes_dict[S].countStation("B", G))
    else:
        print("Forward Route: " + nodes_dict[S].printForward(G) ,end=",")
        print(nodes_dict[S].countStation("F", G))
        print("Backward Route: " + nodes_dict[S].printBackward(G) ,end=",")
        print(nodes_dict[S].countStation("B", G))
else:
    if D == "F":
        print("Forward Route: " + nodes_dict[S].printForward(G) ,end=",")
    else:
        print("Backward Route: " + nodes_dict[S].printBackward(G) ,end=",")
    print(nodes_dict[S].countStation(D, G))