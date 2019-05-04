class Solution:
    def mySqrt(self, x: int) -> int:
        n=len(str(x))
        start=0
        end=x//(10**((n-1)//2))
        while (start<=end):
            mid=(start+end)//2
            print(mid)
            if mid**2<=x:
                if (mid+1)**2>x:return(mid)
                start=mid+1
                continue
            else:
                if (mid-1)**2<=x:return(mid-1)
                end=mid-1
                continue
