from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while (start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if start==end:
                return -1
            if nums[mid]<target:
                start=mid+1
                continue 
            else:
                end=mid-1
                continue
        return -1

'''test:
nums=[-1,0,3,5,9,12]
target=0
print(search(nums,target))
'''