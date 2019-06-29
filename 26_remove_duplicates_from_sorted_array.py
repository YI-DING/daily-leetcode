class Solution:
    def removeDuplicates(self, nums: List[int]):
        if not nums:return 0
        length=len(nums)
        if length==1:return 1
        last=nums[0]
        for number in nums[1:]:
            if number==last:
                nums.remove(number)
                length-=1
            else:
                last=number
        return length
#this seems really slow...
def removeDuplicates(self, nums: List[int]):
    if not nums:return 0
    if len(nums)==1:return 1
    tail=0
    for i in range(1,len(nums)):
        if nums[tail]!=nums[i]:
            tail+=1
            nums[tail]=nums[i]
    return tail+1
#this is faster because it only changes pointer while the previous method modifies the whole array.
