# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int: 
            if root is None:return 0
            return max(Solution.maxDepth(self,root.left),Solution.maxDepth(self,root.right))+1