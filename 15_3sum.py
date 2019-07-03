class Solution:
    def threeSum(self, nums: List[int]):
        nums.sort()
        last, result , previous=len(nums)-1 , [] , None
        for i,number in enumerate(nums):
            if number == previous:
                continue
            else:
                previous=number
            if number > 0:
                break
            target=-number
            left,right,sub = i+1,last,[]
            while left < right:
                if nums[left]+nums[right] == target:
                    if [number,nums[left],nums[right]] not in sub: 
                        sub.append([number,nums[left],nums[right]])
                    right,left=right-1,left+1
                elif nums[left]+nums[right] > target:
                    right-=1
                else:
                    left+=1
            if sub:
                result.extend(sub)
        return result 