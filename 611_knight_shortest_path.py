"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    #first create a function to calculate neighbor((i,j)->set(neighbors))
    #topological sort. by level. 
    def shortestPath(self, grid, source, destination):
        def get_neighbors(node: tuple, grid_row:int, grid_col:int) -> set:
            x,y = node[0],node[1]
            neighbors = [(x + 1, y + 2),(x + 1, y - 2),
                         (x - 1, y + 2),(x - 1, y - 2),
                         (x + 2, y + 1),(x + 2, y - 1),
                         (x - 2, y + 1),(x - 2, y - 1)]
            result = []
            for point in neighbors:
                if (point[0] < 0 or point[0] > grid_row or
                point[1] < 0 or point[1] > grid_col):  
                    continue
                else:
                    result.append(point)
            return result
    
        grid_row = len(grid)-1
        grid_col = len(grid[0])-1
        queue,level = deque([tuple([source.x,source.y])]),0
        visited,destination = set(),(destination.x,destination.y)
        while queue:
            size = len(queue)
            if not size:
                break
            else:
                level += 1
            for _ in range(size):
                point = queue.popleft()
                visited.add(point)
                for upcom in get_neighbors(point,grid_row,grid_col):
                    if upcom not in visited:
                        if grid[upcom[0]][upcom[1]] == 1:
                            continue
                        if upcom == destination:
                            return level
                        visited.add(upcom)
                        queue.append(upcom)
        return -1