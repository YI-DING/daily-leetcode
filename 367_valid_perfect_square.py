class Solution:
    def isPerfectSquare(self, num: int) :
        start, end = 0, num
        while start+1 < end:
            mid = (start+end)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                end = mid-1
            else:
                start = mid+1
        if start**2 == num:
            return True
        elif end**2 == num:
            return True
        else:
            return False