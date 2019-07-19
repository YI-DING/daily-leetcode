'''Given a binary array, find the maximum number of consecutive 1s in this 
array if you can flip at most one 0.
	Input:  nums = [1,0,1,1,0]
	Output:  4
	Input: nums = [1,0,1,0,1]
	Output:  3'''
class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
    	if not nums:
    		return 0
    	fast, slow, flip = 0, 0, None
    	maxx = 0
    	while fast <= len(nums) - 1:
    		if nums[fast] == 1:
    			fast += 1
    		elif nums[fast] == 0:
    			if flip is not None:
    				maxx = max(fast - slow -1, maxx)
    				slow, flip = flip, fast
    			else:
    				flip = fast 
    			fast += 1
    	maxx = max(fast - slow, maxx)
    	return maxx
#nice one by @jiuzhang.com
def findMaxConsecutiveOnes(self, nums):
    # write your code here
    can_still_flip, no_more_flips, max_ones = 0, 0, 0
    
    for num in nums:
        
        if num == 1:
            can_still_flip += 1 
            no_more_flips += 1
        else:
            can_still_flip += 1 
            no_more_flips, can_still_flip = can_still_flip, 0
            
        max_ones = max(max_ones, can_still_flip, no_more_flips)

    return max_ones