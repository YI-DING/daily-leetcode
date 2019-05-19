# iterative solution: 
'''     
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root: #stack is a sequece of left nodes 
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def iT(rt):
            if rt:
                if rt.left:
                    iT(rt.left)
                result.append(rt.val)
                if rt.right:
                    iT(rt.right)
        iT(root)
        return result