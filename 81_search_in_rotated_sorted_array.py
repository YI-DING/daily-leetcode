#alright, since there are duplicates, you can't use binary search.
#If you still want to use it, it is expeced to be O(n).
#Which means, linear search would be good.......
class Solution:
    def search(self, nums: List[int], target: int):
        if not nums or target is None:
            return False
        start, end = 0, len(nums)-1
        #first, find the pivot
        pivot = None
        if nums[start] >= nums[end]:#rotated
            while start+1 < end:
                while nums[start] == nums[start+1] and start+2 < end:
                    start += 1
                while nums[end] == nums[end-1] and start+2 < end:
                    end -= 1
                mid = (start+end)//2
                if nums[mid] > nums[mid+1]:#pivout found!
                    pivot = mid+1
                    break
                else:#pivot not found
                    if nums[mid] > nums[end]:
                        start = mid
                    else:
                        end = mid
            pivot = end if not pivot else pivot
            if nums[0] <= target <= nums[pivot-1]:
                start, end = 0, pivot-1
            else:
                start, end = pivot, len(nums)-1
        #binary serch
        while start+1<end:
            while nums[start] == nums[start+1] and start+2 < end:
                start += 1
            while nums[end] == nums[end-1] and start+2 < end:
                end -= 1
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return True
        elif nums[end] == target:
            return True
        else:
            return False 