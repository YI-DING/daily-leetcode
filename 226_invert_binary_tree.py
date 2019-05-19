# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode):
        if not root: return root
        lft=Solution.invertTree(self,root.left)
        rgt=Solution.invertTree(self,root.right)
        root.right=lft
        root.left=rgt
        return root
#damn only take two minutes.......