class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast=slow=0
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if nums[fast]==nums[slow]:break
        #found the meeting point.
        fast=0
        while fast != slow:
            fast=nums[fast]
            slow=nums[slow]
        return fast
        #dup found
        