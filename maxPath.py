def maxPath(self, root):
    if not root:
        return []

    left = maxPath(root.left)
    right = maxPath(root.right)
    max_list = []
    if sum(left) > sum(right): 
        max_list = left
    else:
        max_list = right    
        
    return [root] + max_list

def maxPathh(root):
    if not root:
        return 0, []

    left = maxPath(root.left)
    right = maxPath(root.right)
    if left[0] > right[0]: 
        max_list = left[1]
        val = left[0]
    else:
        max_list = right[1] 
        val = right[0]
    return val+root.data, [root] + max_list