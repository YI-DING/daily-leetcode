from math import inf
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            maxx = -inf
            for _ in range(size):
                node = queue.popleft()
                maxx = max(maxx,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxx)
        return result 