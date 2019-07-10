class Solution:
    def searchRange(self, nums: List[int], target: int):
        if not nums or target is None:
            return [-1,-1]
        first, last = None, None
        #last
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid -1
            else:
                start = mid
        if nums[end] == target:
            last = end
        elif nums[start] == target:
            last = start
        else:
            last = -1
        #first
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid -1
            elif nums[mid] == target:
                end = mid
            else:# mid < target 
                start = mid+1
        if nums[start] == target:
            first = start
        elif nums[end] == target:
            first = end
        else:
            first = -1
        return [first,last]
#could have written a function to avoid duplicate code since it is essentially
#running binary search with minor difference twice