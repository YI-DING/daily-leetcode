from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        queue,result = deque([root]),[]
        while queue:
            size,level = len(queue),[]
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                result.append(level)
        return result[::-1]