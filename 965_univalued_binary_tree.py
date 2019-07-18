class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        val = root.val
        def traverse(node):
            if node.val != val:
                return False
            if node.left:
                if not traverse(node.left):
                    return False
            if node.right:
                if not traverse(node.right):
                    return False
            return True
        return traverse(root)