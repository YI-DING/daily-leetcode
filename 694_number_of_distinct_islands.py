from collections import deque
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        def get_neighbors(i,j):
            result = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
            if i == 0: result.remove((i-1,j))
            if i == row_num-1: result.remove((i+1,j))
            if j == 0: result.remove((i,j-1))
            if j == col_num-1: result.remove((i,j+1))
            return result
            
        row_num,col_num = len(grid),len(grid[0])
        visited,island = set(),set()
        for i in range(row_num):#traverse lines
            for j in range(col_num):#for each line, traverse each node
                if (i,j) in visited or grid[i][j] == 0 :
                    continue
                visited.add((i,j))#if first time visit
                path = "00"
                queue=deque()
                queue.append((i,j))
                while queue:
                    (a,b)=queue.popleft()
                    for neighbor in get_neighbors(a,b):
                        if (grid[neighbor[0]][neighbor[1]] == 1 and 
                        neighbor not in visited):
                            visited.add(neighbor)
                            queue.append(neighbor)
                            path = path + str(neighbor[0]-i)+str(neighbor[1]-j)
                island.add(path)
        return len(island)