class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:return []
        dicc={}
        for index,num in enumerate(nums):
            if num not in dicc:
                dicc.update({target-num:index})
            else:
                return([dicc[num],index])