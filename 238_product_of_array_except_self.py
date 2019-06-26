class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        ans=[1]*length
        ans[0]=1
        for i,num in enumerate(nums[1:]):
            ans[i+1]=ans[i]*nums[i]
        r=1
        print(ans)
        for i in range(length-2,-1,-1):
            r*=nums[i+1]
            ans[i]*=r
            print(ans[i])
        return(ans)
#constant space, no division, O(n) runtime