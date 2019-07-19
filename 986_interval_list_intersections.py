class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        a, b = 0, 0
        lenA, lenB = len(A) - 1, len(B) - 1
        result = []
        while a <= lenA and b <= lenB:
            if A[a][0] <= B[b][0] < A[a][1] <= B[b][1]:
                result.append( [ B[b][0], A[a][1] ] )
                a += 1
            elif B[b][0] <= A[a][0] < B[b][1] <= A[a][1]:
                result.append( [ A[a][0], B[b][1] ] )
                b += 1
            elif A[a][0] <= B[b][0] < B[b][1] <= A[a][1]:
                result.append( [ B[b][0], B[b][1] ] )
                b += 1
            elif B[b][0] <= A[a][0] < A[a][1] <= B[b][1]:
                result.append( [ A[a][0], A[a][1] ] )
                a += 1
            elif B[b][1] <= A[a][0]:
                if B[b][1] == A[a][0]:
                    result.append( [ B[b][1], A[a][0] ] )
                b += 1
            elif A[a][1] <= B[b][0]:
                if A[a][1] == B[b][0]:
                    result.append( [ A[a][1], B[b][0] ] )
                a += 1
                
        return result
#smarter move:
class Solution(object):
    def intervalIntersection(self, A, B):
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))

            # Remove the interval with the smallest endpoint
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return ans