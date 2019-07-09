from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int):
        queue = deque([root])
        x_lev,y_lev = None,None
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                if node.val == x:
                    x_lev = level
                elif node.val == y:
                    y_lev = level
                if x_lev and y_lev:
                    return x_lev == y_lev
                if node.left:
                    queue.append(node.left)
                    if node.right:
                        if (node.left.val,node.right.val) in [(x,y),(y,x)]:
                            return False 
                if node.right:
                    queue.append(node.right)