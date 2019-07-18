from math import inf
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1
        self.minn = root.val
        self.minn_2 = inf
        def traverse(root):
            if not root:
                return 
            if self.minn < root.val < self.minn_2:
                self.minn_2 = root.val
            if not root.left:
                return 
            if self.minn_2 is not inf and root.left.val > self.minn_2:
                traverse(root.right)
            elif self.minn_2 is not inf and root.right.val > self.minn_2:
                traverse(root.left)
            else:
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return -1 if self.minn_2 is inf else self.minn_2