# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None: return None
        if L<=root.val<=R:
            root.left=Solution.trimBST(self,root.left,L,R)
            root.right=Solution.trimBST(self,root.right,L,R)
            return root
        if root.val<L:return Solution.trimBST(self,root.right,L,R)
        if root.val>R:return Solution.trimBST(self,root.left,L,R)
        