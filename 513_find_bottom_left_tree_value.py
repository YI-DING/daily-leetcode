from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        while queue:
            size = len(queue)
            bottom = []
            for _ in range(size):
                node = queue.popleft()
                bottom.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottom[0]