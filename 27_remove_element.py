class Solution:
def removeElement(self, nums: List[int], val: int) -> int:
    if not nums:return 0
    tail=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[tail]=nums[i]
            tail+=1
    return tail
