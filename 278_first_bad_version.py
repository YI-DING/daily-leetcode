class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return None
        if n == 1:
            return 1
        start, end = 1, n
        while start+1 < end:
            mid = (start+end)//2
            if isBadVersion(mid):#mid is bad
                end = mid 
            else:#mid is good
                start = mid+1
        return start if isBadVersion(start) else end