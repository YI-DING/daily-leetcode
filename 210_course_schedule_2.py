from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        def create_neighbors(prereq):#prereq ---> node->its neighbours i.e.  course, upcoming courses
            dicc = {i:set() for i in range(n)}
            for pair in prerequisites:
                dicc[pair[1]].add(pair[0])
            return dicc
        def count_degrees(neighbour_dicc):#neighbors_dicc -----> node->how many prereq it has
            dicc = {i:0 for i in range(n)}
            for course in neighbour_dicc:
                for upcom in neighbour_dicc[course]:
                    dicc[upcom]+=1
            return dicc
        
        neighbors = create_neighbors(prerequisites)
        degrees = count_degrees(neighbors)
        start = [course for course in degrees if degrees[course] == 0]
        queue = deque(start)
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for upcoms in neighbors[course]:
                degrees[upcoms]-=1
                if degrees[upcoms] == 0:
                    queue.append(upcoms)
        return order if len(order) == n else []