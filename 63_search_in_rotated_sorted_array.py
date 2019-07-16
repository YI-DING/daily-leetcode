#alright, since there are duplicates, you can't use binary search.
#If you still want to use it, it is expeced to be O(n).
#Which means, linear search would be good.......
class Solution:
    def search(self, A: List[int], target: int):
        if not A or target is None:
            return False
        start, end = 0, len(A)-1
        #first, find the pivot
        pivot = None
        if A[start] >= A[end]:#rotated
            while start+1 < end:
                while A[start] == A[start+1] and start+2 < end:
                    start += 1
                while A[end] == A[end-1] and start+2 < end:
                    end -= 1
                mid = (start+end)//2
                if A[mid] > A[mid+1]:#pivout found!
                    pivot = mid+1
                    break
                else:#pivot not found
                    if A[mid] > A[end]:
                        start = mid
                    else:
                        end = mid
            pivot = end if not pivot else pivot
            if A[0] <= target <= A[pivot-1]:
                start, end = 0, pivot-1
            else:
                start, end = pivot, len(A)-1
        #binary serch
        while start+1<end:
            while A[start] == A[start+1] and start+2 < end:
                start += 1
            while A[end] == A[end-1] and start+2 < end:
                end -= 1
            mid = (start+end)//2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            return True
        elif A[end] == target:
            return True
        else:
            return False 