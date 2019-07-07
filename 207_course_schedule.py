from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        #topoligical sort 
        if numCourses in (0,1) or not prerequisites:
            return True
            
        def prereq_to_upcoming_courses(List):
            dicc={i:set() for i in range(numCourses)}
            for pair in List:
                dicc[pair[1]].add(pair[0])
            return dicc

        def get_degrees_from_prereq(neighbors):
            dicc={i:0 for i in range(numCourses)}
            for keys in neighbors:
                for node in neighbors[keys]:
                    dicc[node]+=1
            return dicc

        neighbors = prereq_to_upcoming_courses(prerequisites)
        degrees = get_degrees_from_prereq(neighbors)
        order = []
        #start nodes
        starts = [node for node in degrees if degrees[node] == 0]
        queue = deque(starts)
        if not queue:
            return False 

        while queue:
            course = queue.popleft()
            order.append(course)
            for upcoming in neighbors[course]:
                degrees[upcoming] -=1 
                if degrees[upcoming] == 0:
                    queue.append(upcoming)

        return len(order) == numCourses