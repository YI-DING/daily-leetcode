# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            if not p and not q: return True 
            else: return False 
        if p.val!=q.val:return False 
        if not self.isSameTree(p.left,q.left):return False
        if not self.isSameTree(p.right,q.right):return False
        return True

        
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q