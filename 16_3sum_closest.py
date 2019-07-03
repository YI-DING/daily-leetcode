from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        if not nums:
            return 0
        nums.sort()
        last,closest=len(nums)-1,inf
    
        for i,number in enumerate(nums[:last-1]):
            target_2=target-number
            left,right=i+1,last
            
            while left < right :
                diff=nums[left]+nums[right]-target_2
                if diff**2 < (closest-target)**2:
                    closest=nums[left]+nums[right]+number
                
                if diff > 0:
                    right-=1
                elif diff < 0:
                    left+=1
                else:
                    return target
        
        return closest
#after style update:
class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        if not nums:
            return 0
        nums.sort()
        last,closest=len(nums)-1,sum(nums[:3])
    
        for i,number in enumerate(nums[:last-1]):
            left,right=i+1,last
            
            while left < right :
                summ=nums[left]+nums[right]+number
                if abs(summ-target) < abs(closest-target):
                    closest=summ
                
                if summ-target > 0:
                    right-=1
                elif summ-target < 0:
                    left+=1
                else:
                    return target
        
        return closest