class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        if not matrix or not matrix[0]:
            return False
        start, end = 0, len(matrix)-1
        while start+1 < end:
            mid = (start+end)//2
            if matrix[mid][0] > target:
                end = mid
            else:
                start = mid
        if matrix[end][0] > target:
            row, start, end = start, 0, len(matrix[0])-1
        else:
            row, start, end = end, 0, len(matrix[0])-1
        while start+1 < end:
            mid = (start+end)//2
            if matrix[row][mid] > target:
                end = mid
            else:
                start = mid
        if matrix[row][start] == target:
            return True
        elif matrix[row][end] == target:
            return True
        return False
#this method uses BFS twice, first among rows then among cols
#however you could see it as len(m*n) and do binary search for only once