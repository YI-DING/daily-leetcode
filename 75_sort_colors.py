class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quicksort(A, color, start):
            end = len(A) - 1
            while start <= end:
                while start <= end and A[start] == color:
                    start += 1
                while start <= end and A[end] != color:
                    end -= 1
                if start <= end:
                    A[start], A[end] = A[end], A[start]
                    start += 1
                    end -= 1
            return start 
        
        if not nums:
            return None 
        start = quicksort(nums, 0, 0)
        quicksort(nums, 1, start)