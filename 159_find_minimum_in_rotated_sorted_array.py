def findMin(self, nums: List[int]):
    if not nums:
        return None
    if nums[0] < nums[len(nums)-1]:
        return nums[0]
    #rotated.
    start, end =0, len(nums)-1
    while start+1 < end:
        mid = (start+end)//2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[end]:
            end = mid
        else:
            start = mid
    return nums[end]