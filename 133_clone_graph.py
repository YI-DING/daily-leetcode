from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        queue,visited = deque([node]),set([node])
        mapping = {}
        #create nodes
        while queue:
            head = queue.popleft()
            new_node = Node(head.val,[])
            mapping.update({head:new_node})
            for neighbor in head.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        #add neiboring relationships
        queue = deque([node])
        visited = set([node])
        while queue:
            head = queue.popleft()
            for old_neighbor in head.neighbors:
                if old_neighbor not in visited: 
                    visited.add(old_neighbor)
                    queue.append(old_neighbor)
                mapping[head].neighbors.append(mapping[old_neighbor])
        return mapping[node]
#answer from jiuzhang:
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node
            
        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)
        
        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]
        
    def getNodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result