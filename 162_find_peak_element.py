class Solution:
    def findPeakElement(self, nums: List[int]):
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid 
        return start if nums[start] > nums[end] else end