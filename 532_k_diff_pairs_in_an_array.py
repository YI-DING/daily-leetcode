class Solution:
    def findPairs(self, nums: List[int], k: int):
        if not nums or len(nums) == 1:
            return 0
        fast, slow = 1, 0
        lenn = len(nums) - 1
        count = 0
        nums.sort()
        while slow < fast <= lenn:
            if abs(nums[fast] - nums[slow]) == k:
                count += 1
                print(fast, slow)
                fst = nums[fast]
                slo = nums[slow]
                
                while nums[fast] == fst:
                    if fast < lenn:
                        fast += 1
                    else:
                        break
                slow += 1
                while nums[slow] == slo:
                    if slow < fast - 1:
                        slow += 1
                    else:
                        break
                if nums[fast] == nums[slow] or nums[fast] == fst:
                    break
            elif abs(nums[fast] - nums[slow]) > k:
                if slow == fast - 1:
                    fast += 1
                else:
                    slow += 1
            else:
                if fast == lenn:
                    slow += 1
                else:
                    fast += 1
        return count