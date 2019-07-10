class Solution:
    def peakIndexInMountainArray(self, A: List[int]):
        start, end = 0 ,len(A)-1
        while start+1 < end:
            mid = (start+end)//2
            if A[mid] >= A[mid+1]:
                end = mid
            else:
                start = mid+1
        return (start if A[start] >= A[end]
        else end)