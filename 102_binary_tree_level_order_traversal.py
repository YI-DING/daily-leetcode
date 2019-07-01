# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:return []
        stack=[]
        result=[]
        stack.append((root,1))
        while stack:
            (node,level)=stack.pop(0)
            if len(result)<level:
                result.append([node.val])
            else:
                result[level-1].append(node.val)
            if node.left:stack.append((node.left,level+1))
            if node.right:stack.append((node.right,level+1))
        return result
'''
def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans'''