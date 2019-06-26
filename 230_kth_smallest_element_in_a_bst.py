# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def build(node):
            if not node:return([])
            ordered=[node.val]
            ordered.extend(build(node.right))
            lefty=build(node.left)
            lefty.extend(ordered)
            return lefty
        return build(root)[k-1]