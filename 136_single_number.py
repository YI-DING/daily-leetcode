'''
        a = 0
        for i in nums:
            a ^= i
        return a
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sett=set()
        while nums:
            if nums[0] not in sett:
                sett.add(nums.pop(0))
                continue 
            sett.remove(nums.pop(0)) 
        return list(sett)[0]