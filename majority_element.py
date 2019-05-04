from statistics import median
class Solution:
    def majorityElement(self, nums: List[int]):
        n=len(nums)
        if n%2==1:
            return (int(median(nums)))
        else:
            return (int(median(nums[0:n])))           

'''test:
nums=[3,3,4,4,4]
print(majorityElement(nums))
'''