def validPalindrome(s):
    if len(s)==1:return True 
    left,right,count=0,len(s)-1,0
    while left<right:
        if s[left]!=s[right]:
            count+=1
            if count==2:return False
            if s[left]==s[right-1]:
                left-=1
            else:right+=1
        left+=1
        right-=1
    return True
#this code is wrong! 
#e.g. ececcec
class Solution:
    def validPalindrome(self, s: str) :
        if len(s)<3:return True 
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                first,second=s[left:right],s[left+1:right+1]
                return first==first[::-1] or second==second[::-1]
            left,right=left+1,right-1
        return True
