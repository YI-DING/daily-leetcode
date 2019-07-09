from collections import deque
class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        queue,result = deque([root]),[]
        while queue:
            size,tmp = len(queue),[]
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            if tmp:
                result.append(tmp)
        return result