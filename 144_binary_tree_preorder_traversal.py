# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return([])
        result=[]
        result.append(root.val)
        result.extend(Solution.preorderTraversal(self,root.left))
        result.extend(Solution.preorderTraversal(self,root.right))
        return(result)
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack,result=[root],[]
        while stack:
            node=stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return(result)