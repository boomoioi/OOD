class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, root, data):
        if not root: 
            return Node(data)
        if data > root.data:
            root.right = self._insert(root.right, data)
        else: 
            root.left = self._insert(root.left, data)
        return root
    
    def rank(self, data):
        print("--------------------------------------------------")
        print(f"Rank of {data} : {self._rank(self.root, data)[0]}")
        
    
    def _rank(self, root, data):
        if not root:
            return 0, 0 
        res = 0
        left = self._rank(root.left,data)
        res += left[0]
        if left[1]:
            return res, 1
        if root.data > data:
            return res, 1
        res += 1
        if root.data == data:
            return res, 1 
        right = self._rank(root.right,data)
        res += right[0]
        if right[1]: 
            return res, 1
        return res, 0 
        
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp, num = input('Enter Input : ').split("/")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.rank(int(num))