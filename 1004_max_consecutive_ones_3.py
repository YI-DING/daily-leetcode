from collections import deque
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        slow, flips, maxx = 0, deque(), 0
        for fast,num in enumerate(A):
            if num == 0:
                if len(flips) < K:
                    flips.append(fast)
                elif K > 0:
                    slow = flips.popleft() + 1
                    flips.append(fast)
                elif K == 0:
                    slow = fast + 1
            maxx = max(maxx, fast - slow + 1)
        return maxx 
#genius Solution&explanation by lee215@leetcode
'''Intuition
Translation:
Find the longest subarray with at most K zeros.

Explanation
For each A[j], try to find the longest subarray.
If A[i] ~ A[j] has zeros <= K, we continue to increment j.
If A[i] ~ A[j] has zeros > K, we increment i.'''
    def longestOnes(self, A, K):
        i = 0
        for j in xrange(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
