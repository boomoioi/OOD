def nameValue(st):
    sum = 0
    for ch in st:
        sum += ord(ch)
    return sum


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.data + f" ({nameValue(self.data)})"


class AVL_Tree(object):
    def insert(self, root, data):
        if not root:
            return Node(data)
        if nameValue(data) < nameValue(root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        #check balance
        balance = self.getBalance(root)
        if balance > 1 and nameValue(data) < nameValue(root.left.data): 
            root = self.rotateRight(root)
        elif balance > 1 and nameValue(data) >= nameValue(root.left.data):
            root.left = self.rotateLeft(root.left)
            root = self.rotateRight(root)
        elif balance < -1 and nameValue(data) >= nameValue(root.right.data): 
            root = self.rotateLeft(root)
        elif balance < -1 and nameValue(data) < nameValue(root.right.data): 
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
        
        return root

    def delete(self, root, data):
        if not root:
            return root
        if nameValue(data) < nameValue(root.data):
            root.left = self.delete(root.left, data)
        elif nameValue(data) > nameValue(root.data):
            root.right = self.delete (root.right, data)
        
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        
        if root is None:
            return root
        
        #check balance
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
 
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

    def getBalance(self, root):
        return self.height(root.left) - self.height(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
    
    def printTree(self, node, level=0):
        if node != None:
            print('    ' * level , node, sep="")
            if node.left or node.right:
                if node.left:
                    self.printTree(node.left, level + 1)
                else: 
                    print('    ' * (level+1), "*", sep="")
                if node.right:
                    self.printTree(node.right, level + 1)
                else:
                    print('    ' * (level+1), "*", sep="")
                  

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split()
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")