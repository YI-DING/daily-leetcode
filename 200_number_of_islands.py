from collections import deque
def numIslands(self, grid: List[List[str]]):
    if not grid:
        return 0
    row_num,col_num = len(grid),len(grid[0])
    visited,island_count = set(),0
    
    def get_neighbors(i,j):
        result = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
        if i == 0: result.remove((i-1,j))
        if i == row_num-1: result.remove((i+1,j))
        if j == 0: result.remove((i,j-1))
        if j == col_num-1: result.remove((i,j+1))
        return result
        
    for i in range(row_num):#traverse lines
        for j in range(col_num):#for each line, traverse each node
            if (i,j) in visited or grid[i][j] == '0' :
                continue
            visited.add((i,j))#if first time visit
            island_count+=1
            queue=deque()
            queue.append((i,j))
            while len(queue):
                (a,b)=queue.popleft()
                for neighbor in get_neighbors(a,b):
                    if grid[neighbor[0]][neighbor[1]] == '1' and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return island_count

#this guy is smart: BFS in place 
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))