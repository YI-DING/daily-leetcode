class Solution:
    def containsDuplicate(self, nums: List[int]):
        '''
        sett=set()
        for item in nums:
            if item in sett:return True
            else:
                sett.add(item)
        return False
        '''
        return len(set(nums)) < len(nums)