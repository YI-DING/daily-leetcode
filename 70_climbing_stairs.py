class Solution:
    def climbStairs(self, n: int):
        if n<4:return n
        n_2=2
        n_1=3
        for i in range(n-3):
            n_2,n_1=n_1,n_2+n_1
        return n_1