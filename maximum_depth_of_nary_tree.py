"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node'):
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

I used if root is None :return 0. 
Could try:  if not root.         Instead of if not node.
'Cause when root is null   if not null is true.
If not root.children is also smart. 'Cause if no chilren it will also return False.

max ()  over a list comprehension is also pretty smart and neat. 
'''



#after looking at discussion:
class Solution:
    def maxDepth(self, root: 'Node'):
        if not root: return 0
        if not root.children: return 1
        return max(Solution.maxDepth(self,child) for child in root.children)+1


#took 16min to get first acception. Took 24 min to get polished acception, 99% faster.
