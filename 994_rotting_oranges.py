from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        row = len(grid)
        col = len(grid[0])
        start = []
        queue = deque()
        visited = set()
        fresh_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    start.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if not start:
            if not fresh_count:
                return 0
            else:
                return -1
        for point in start:
            queue.append(point)
            visited.add(point)
        time = 0
        
        def get_neighbor(x,y):
            lst = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            if x <= 0:lst.remove((x-1,y))
            if y <= 0:lst.remove((x,y-1))
            if x >= row-1:lst.remove((x+1,y))
            if y >= col-1:lst.remove((x,y+1))
            return lst
        
        while queue:
            size = len(queue)
            time += 1
            for _ in range(size):
                org = queue.popleft()
                for nei in get_neighbor(org[0],org[1]):
                    if grid[nei[0]][nei[1]] in (0,2) or nei in visited:
                        continue 
                    visited.add(nei)
                    queue.append(nei)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1
        return time-1