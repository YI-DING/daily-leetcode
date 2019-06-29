#genius solution:
'''for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)'''
#smart O(n) linear DP solution:
'''    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
'''
#Divide and Conque solution: Gosh this is ON CLRS chapter 4......and is very slow......
from math import inf
class Solution:
    def maxSubArray(self,nums):
        def middle_case(left,right,mid):
            left_sum=-inf
            summ=0
            for i in range(mid,left-1,-1):
                summ+=nums[i]
                if summ>left_sum:
                    left_sum=summ
                    max_left=i
            right_sum=-inf
            summ=0
            for j in range(mid+1,right+1):
                summ+=nums[j]
                if summ>right_sum:
                    right_sum=summ
                    max_right=j
            return (left_sum+right_sum,max_left,max_right)
            
        def  maxsub(left,right):#input left and right index, output maxvale, where it starts and ends
            if left==right:#base csae 
                return (nums[left],left,right)
            #when nums has at least two numbers
            mid=(left+right)//2
            lefthalf=maxsub(left,mid)
            righthalf=maxsub(mid+1,right)
            mid_case=middle_case(left,right,mid)
            #check
            if lefthalf[0]>=max(righthalf[0],mid_case[0]):
                return lefthalf
            elif righthalf[0]>=max(lefthalf[0],mid_case[0]):
                return righthalf
            else:return mid_case
        
        return maxsub(0,len(nums)-1)[0]
