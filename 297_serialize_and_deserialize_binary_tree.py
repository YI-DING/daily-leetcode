from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        queue,lst = deque([root]),[]
        while queue:
            node = queue.popleft()
            lst.append(str(node.val) if node else "$")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(lst)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None 
        nodes = [TreeNode(int(val)) if val != "$" else None 
                for val in data.split()]
        root = nodes[0]
        pool = [root]
        parent,children = 0,1
        while parent < len(pool):
            node = pool[parent]
            parent += 1
            node.left = nodes[children]
            node.right = nodes[children+1]
            children += 2
            if node.left:
                pool.append(node.left)
            if node.right:
                pool.append(node.right)
        return root