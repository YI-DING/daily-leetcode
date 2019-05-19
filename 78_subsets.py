class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for n in nums:
            new=[]
            for item in result:
                new.append(item+[n])
            result=result+new
        return result
            