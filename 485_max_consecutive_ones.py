class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fast, slow = 0, 0
        maxx = 0
        while fast <= len(nums) - 1:
            if fast == slow:
                if nums[fast] == 1:
                    maxx = max(maxx, 1)
                fast += 1
            elif nums[fast] == 1:
                if nums[slow] == 0:
                    slow = fast
                maxx = max(fast - slow + 1, maxx)
                fast += 1
            elif nums[fast] == 0:
                fast += 1
                slow = fast 
        return maxx
#cleaner:
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
        