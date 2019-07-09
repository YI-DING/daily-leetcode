from collections import deque
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        #first convert it into a graph
        #BFS, with 5 as the start node
        def tree_to_adj_list(root):
            dicc,queue = {},deque([root])
            while queue:
                node = queue.popleft()
                if node not in dicc:
                    dicc[node] = set()
                if node.left:
                    dicc[node].add(node.left)
                    if node.left not in dicc:
                        dicc[node.left] = set([node])
                    else:
                        dicc[node.left].add(node)
                    queue.append(node.left)
                if node.right:
                    dicc[node].add(node.right)
                    if node.right not in dicc:
                        dicc[node.right] = set([node])
                    else:
                        dicc[node.right].add(node)
                    queue.append(node.right)
            return dicc
        
        graph = tree_to_adj_list(root)
        queue = deque([target])
        level,visited = 0,set()
        while queue:
            size,sub = len(queue),[]
            for _ in range(size):
                node = queue.popleft()
                sub.append(node.val)
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            if level == K:
                return sub
            level += 1
        return []