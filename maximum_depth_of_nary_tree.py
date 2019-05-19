"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:return 0
        cdmaxdepth=0
        for child in root.children:
            childmaxdepth=Solution.maxDepth(self,child)
            if childmaxdepth>=cdmaxdepth:
                cdmaxdepth=childmaxdepth
        return cdmaxdepth+1


'''
n-nary tree means that a tree has at most n children 

so..recursively solve it?  take max of max depth of children and plus 1??
'''