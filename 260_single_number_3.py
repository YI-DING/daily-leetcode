class Solution:
    def singleNumber(self, nums: List[int]):
        set1=set()
        for item in nums:
            if item in set1:
                set1.remove(item)
            else:
                set1.add(item)
        return list(set1)

#not quite sure how to do it in constant space.....