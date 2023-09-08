class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
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
    def getSmallest(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur
    
    def delete(self,root, data):
        if not root:
            print("Error! Not Found DATA")
            return root
                    
        if data<root.data: 
            root.left = self.delete(root.left, data)
            return root
        elif data > root.data:
            root.right = self.delete(root.right, data)
            return root
    
        if not root.left:
            temp = root.right
            del root
            return temp 
        elif not root.right:
            temp = root.left
            del root
            return temp 
        
        new = self.getSmallest(root.right)
        root.data = new.data
        root.right = self.delete(root.right, new.data)
        return root
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for da in data:
    mode = da.split()[0]
    val = int(da.split()[1])
    if mode == 'i':
        print("insert", val)
        tree.insert(val)
    else: 
        print("delete", val)
        tree.root = tree.delete(tree.root, val)
    printTree90(tree.root)