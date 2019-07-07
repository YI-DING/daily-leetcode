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

# BFS:    
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        
        def children(node):
            result=[]
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return result
        
        queue,visited,result = deque(),set(),[[root.val]]
        queue.append(root)
        visited.add(root)
        while len(queue):
            size,tmp = len(queue),[]
            for _ in range(size):
                head = queue.popleft()
                for child in children(head):
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
                        tmp.append(child.val)
            if tmp:
                result.append(tmp)
        return result