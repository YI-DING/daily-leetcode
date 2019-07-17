def twoSum(self, nums, target):
	if not nums:
		return False
	left, right = 0, len(nums) - 1
	while 0<= left < right <= len(nums) -1:
		if nums[left] + nums[right] == target:
			return [left + 1, right + 1]
		elif nums[left] + nums[right] > target:
			right -= 1
		else:
			left += 1
	return False