class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, st):
        self.root = self._creatTree(st)


    def _creatTree(self, st):
        stack = []
        for ch in st:
            if ch in "+-*/":
                sec = stack.pop()
                first = stack.pop() 
                node = Node(ch)
                node.left = first
                node.right = sec
                stack.append(node)
            else:
                stack.append(Node(ch))
        return stack.pop()
    
    def printTree(self):
        self._printTree(self.root)
    
    def preOrder(self):
        print(self._preOrder(self.root))
    
    def _preOrder(self, root): 
        if not root:
            return ""
        res = ""
        res += root.data
        res += self._preOrder(root.left)
        res += self._preOrder(root.right)
        return res
    
    def inOrder(self):
        print(self._inOrder(self.root))
        
    def _inOrder(self, root):
        if not root.left and not root.right:
            return root.data
        res = "("
        res += self._inOrder(root.left)
        res += root.data
        res += self._inOrder(root.right)
        res += ")"
        return res
    
    def _printTree(self, node, level = 0):
        if node != None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node)
            self._printTree(node.left, level + 1)

T = BST(input("Enter Postfix : "))
print("Tree :")
T.printTree()
print("--------------------------------------------------\nInfix : ",end="")
T.inOrder()
print("Prefix : ", end="")
T.preOrder()
