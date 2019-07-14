def closestValue(self, root, target):
    # write your code here
    def find(node):
        if not node:
            return None
        if node.val > target:#search for its left but not right tree
            if node.left:
                lft = find(node.left)
                return (node.val if 
                abs(lft-target) > abs(node.val-target)
                else lft)
        elif node.val < target:
            if node.right:
                rt = find(node.right)
                return (node.val if 
                abs(rt-target) > abs(node.val-target)
                else rt)
        return node.val
    return find(root)
#iterative solution by @jiuzhang.com:
def closestValue(self, root, target):
    upper = root
    lower = root
    while root:
        if target > root.val:
            lower = root
            root = root.right
        elif target < root.val:
            upper = root
            root = root.left
        else:
            return root.val
    if abs(upper.val - target) <= abs(lower.val - target):
        return upper.val
    return lower.val