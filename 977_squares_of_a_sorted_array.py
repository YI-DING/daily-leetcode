class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return None
        pos = -1
        neg = len(A) - 1
        for i,num in enumerate(A):
            if num >= 0:
                pos = i
                neg = i - 1
                break
        result = []
        for _ in range(len(A)):
            if neg < 0:
                result.append(A[pos]**2)
                pos += 1
            elif pos > len(A) - 1:
                result.append(A[neg]**2)
                neg -= 1
            elif A[neg]**2 >= A[pos]**2:
                result.append(A[pos]**2)
                pos += 1
            else:
                result.append(A[neg]**2)
                neg -= 1
        return result
            