class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        i=j=0
        while i-j<=m-1 and j<=n-1:
            if nums1[i]>nums2[j]:
                #all nums1 go back for one spot and leave nums1[i] for nums2[j]  
                for k in range(m+n-1,i,-1):
                    nums1[k]=nums1[k-1]
                nums1[i]=nums2[j]
                j+=1
            i+=1
        if i-j==m:#only j left
            for k in range(1,n-j+1):
                nums1[i+k-1]=nums2[j+k-1]
        #else only i left, which is already finished
'''test
A1=[1,2,3,0,0,0]
A2=[2,5,6]
m=3
n=3
print(merge(A1,3,A2,3))
'''