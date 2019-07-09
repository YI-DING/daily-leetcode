from collections import deque
class Solution:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level