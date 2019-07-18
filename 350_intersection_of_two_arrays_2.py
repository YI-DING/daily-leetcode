class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        pointer1, pointer2 = 0, 0
        result = []
        len1, len2 = len(nums1) - 1, len(nums2) -1
        while pointer1 <= len1 and pointer2 <= len2:
            if nums1[pointer1] == nums2[pointer2]:
                result.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                res = nums2[pointer2]
                while pointer2 <= len2 and res == nums2[pointer2]:
                    pointer2 += 1
            else:
                res = nums1[pointer1]
                while pointer1 <= len1 and res == nums1[pointer1]:
                    pointer1 += 1
        return result
#this is nlogn+mlogm in time and no extra space
#hash: O(m+n) time and space