class Solution:
    def removeDuplicates(self, nums: List[int]):
        if not nums:
            return 0
        slow, fast, last, last_val, length = 0, 0, 0, nums[0], 0
        while fast <= len(nums) - 1:
            if nums[fast] == last_val and fast > last + 1:
                fast += 1
                continue
            if nums[fast] != last_val:
                last, last_val = fast, nums[fast]
            nums[slow] = nums[fast]
            length += 1
            slow += 1
            fast += 1
        return length
#beautiful solution by StefanPochmann@leetcode:
def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i