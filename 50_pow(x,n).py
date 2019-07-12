class Solution:
    def myPow(self, x: float, n: int):
        ans, base, positive = 1, x, True if n > 0 else False
        n = abs(n)
        while n > 0:
            if n%2 == 1:
                ans *= base
            base *= base
            n = n//2
        return ans if positive else 1/ans