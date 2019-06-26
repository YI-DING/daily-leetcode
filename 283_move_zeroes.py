#elegant solution. Save the position of first zero. change whenever there is a good candidate.
'''def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1'''
class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i==len(nums)-1:break
            if nums[i]==0:
                k=i+1
                while k<len(nums):
                    if nums[k]!=0:break
                    else: k+=1
                if k==len(nums):break
                temp=nums[k]
                nums[k]=nums[i]
                nums[i]=temp
        