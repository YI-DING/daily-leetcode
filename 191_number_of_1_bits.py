class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(32):
            if (n & (1<<i)) != 0:
                count+=1
        return count