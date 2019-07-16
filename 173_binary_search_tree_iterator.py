class BSTIterator:

    def __init__(self, root: TreeNode):
        self.lst = []
        self.num = -1
        self.helper(root)
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.lst.append(root.val)
        self.helper(root.right)
        
    def next(self):
        """
        @return the next smallest number
        """
        self.num += 1
        return self.lst[self.num]
        
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.num < len(self.lst) -1 

#stack version by @jiuzhang.com
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """
    def next(self):
        node = self.stack.pop()
        next_node = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return next_node