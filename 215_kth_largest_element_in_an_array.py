class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None 
        def quicksort(A, start, end, k):
            if start == end:
                return A[start]
            left, right = start, end
            pivot = A[(start + end) // 2]
            while left <= right:
                while left <= right and A[left] > pivot:
                    left += 1
                while left <= right and A[right] < pivot:
                    right -= 1
                if left <= right:
                    A[left], A[right] = A[right], A[left]
                    left += 1
                    right -= 1
            if start + k - 1 <= right:
                return quicksort(A, start, right, k)
            elif start + k - 1 >= left:
                return quicksort(A, left, end, k - (left - start))
            else:
                return A[right + 1]
        return quicksort(nums, 0, len(nums) - 1, k)