#elegant solution. Save the position of first zero. change whenever there is a good candidate.
'''def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1'''
#sol
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums:
            return 
        head = 0
        for number in nums:
            if number != 0:
                nums[head] = number
                head += 1
        for i in range(head,len(nums)):
            if nums[i] != 0:
                nums[i] = 0