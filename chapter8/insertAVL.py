class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, root, data):
        if not root:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        
        #check balance
        balance = self.height(root.left) - self.height(root.right)
        if balance > 1 and data < root.left.data: 
            root = self.rotateRight(root)
        elif balance > 1 and data >= root.left.data:
            root.left = self.rotateLeft(root.left)
            root = self.rotateRight(root)
        elif balance < -1 and data >= root.right.data: 
            root = self.rotateLeft(root)
        elif balance < -1 and data < root.right.data: 
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
        
        return root
    
    def rotateRight(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
    
    def rotateLeft(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root
    
    def height(self, root):
        if not root:
            return 0 
        return 1 + max(self.height(root.left), self.height(root.right))


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

# 50 40 35 30 20 10 5
inp = [int(num) for num in input("Enter Input : ").split()]
T = AVL()
for num in inp:
    T.insert(num)
    print(f"Insert : ( {num} )")
    T.printTree(T.root)
    print("--------------------------------------------------")