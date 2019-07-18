class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                res = nums1[i]
                while i <= len(nums1) - 1 and nums1[i] == res:
                    i += 1
                while j <= len(nums2) - 1 and nums2[j] == res:
                    j += 1
            elif nums1[i] > nums2[j]:
                res = nums2[j]
                while j <= len(nums2) - 1 and nums2[j] == res:
                    j += 1
            else:
                res = nums1[i]
                while i <= len(nums1) - 1 and nums1[i] == res:
                    i += 1
        return result
#this is nlogn+mlogm in time and no extra space
#hash: O(m+n) time and space
 