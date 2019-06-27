class Solution(object):
    def isHappy(self, n):
        def nexx(n):
            return(sum([int(x)**2 for x in str(n)]))
        if n==1:return True
        fast=slow=n
        while fast is not 1 and slow is not 1:
            fast=nexx(fast)
            if fast is 1:return True
            if fast is slow:return False 
            slow=nexx(slow)
            fast=nexx(fast)
        return True
        """
        :type n: int
        :rtype: bool
'''
def isHappy(self, n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True
'''
#dont need to use cycle detection. Can just storage past paths