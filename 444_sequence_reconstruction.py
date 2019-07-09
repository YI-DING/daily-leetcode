from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        #1.transform seqs to graph structure i.e. number and its next number
        #2. get degrees from the graph
        #3. Do topological sort. if queue length>=2, false
        #4. if order unique, chekc if it is org
        if not seqs:
            return False
        def create_graph(seqs):#num : upcoming num
            graph = {}
            for seq in seqs:
                if len(seq) == 1:
                    continue
                for i in range(1,len(seq)):
                    if seq[i-1] not in graph:
                        graph[seq[i-1]] = set([seq[i]])
                    else:
                        graph[seq[i-1]].add(seq[i])
            return graph
        
        def get_degree(graph):#node: indegree
            deg = {}
            for nd in graph:
                if nd not in deg:
                    deg[nd] = 0
                for upcom in graph[nd]:
                    if upcom not in deg:
                        deg[upcom] = 1
                    else:
                        deg[upcom] += 1
            return deg
        
        graph = create_graph(seqs)
        degrees = get_degree(graph)
        single_nodes = [seq[0] for seq in seqs if len(seq) == 1]
        start = [nd for nd in degrees if degrees[nd] ==0]
        start += single_nodes
        queue,order = deque(start),[]
        while queue:
            if len(queue) > 1:
                return False
            num = queue.popleft()
            order.append(num)
            if num not in graph:
                break
            for upcom in graph[num]:
                degrees[upcom] -= 1
                if degrees[upcom] == 0:
                    queue.append(upcom)
        return order == org