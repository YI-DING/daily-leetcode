class Solution:
    def search(self, nums: List[int], target: int):
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        #firstly find pivot position
        pivot = None
        if nums[start] < nums[end]:#unrotated
            pivot = 0
        else:
            while start+1 < end:
                mid = (start+end)//2
                if nums[mid] > nums[mid+1]:
                    pivot = mid+1
                    break
                else:
                    if nums[mid] >= nums[end]:
                        start = mid 
                    else:
                        end = mid 
            if pivot is None:
                pivot = end
        #pivot found. 
        if pivot == 0:
            start, end = 0, len(nums)-1
        else:
            if nums[pivot] <= target <= nums[len(nums)-1]:
                start, end = pivot, len(nums)-1
            else:
                start, end = 0, pivot-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1