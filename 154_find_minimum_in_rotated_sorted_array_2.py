class Solution:
    def findMin(self, nums: List[int]):
        if not nums:
            return None
        start, end = 0, len(nums)-1
        if nums[start] < nums[end]:#rotated
            return nums[0]
        #rotated:
        while start+1 < end:
            while nums[start] == nums[start+1] and start+2 < end:
                start += 1
            while nums[end] == nums[end-1] and start+2 < end:
                end -= 1
            mid = (start+end)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid] > nums[end]:
                    start = mid
                else:
                    end = mid
        return nums[end]