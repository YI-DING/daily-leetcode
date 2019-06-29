class Solution:
    def searchInsert(self, nums: List[int], target: int) :
        if not nums:return 0
        for i,number in enumerate(nums):
            if number>=target:return i
        return len(nums)
#could use Binary Search:
def searchInsert(self, nums: List[int], target: int) :
        if not nums:return 0
        if len(nums)==1:return 0 if target<=nums[0] else 1
        mid=len(nums)//2
        if nums[mid]==target:return mid
        if nums[mid]>target:return self.searchInsert(nums[:mid],target)
        else:return mid+1+self.searchInsert(nums[mid+1:],target)