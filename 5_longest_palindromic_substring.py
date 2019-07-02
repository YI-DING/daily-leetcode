    def longestPalindrome(self, s):
        if not s:return ""
        length=len(s)
        if length==1:return s
        longest=[0,0,0]
        table=[[0 for i in range(length)]for j in range(length)]
        for i in range(length-1):
            table[i][i]=True
            table[i][i+1]=True if s[i]==s[i+1] else False
            if s[i]==s[i+1]:longest=[i,i+1,2]
        table[length-1][length-1]=True
        if length<3:return s[longest[0]:longest[1]+1]
        for level in range(3,length+1):
            for i in range(0,length+1-level):
                j=i+level-1
                table[i][j]=table[i+1][j-1] and s[i]==s[j]
                if j-i+1>longest[2] and table[i][j]:
                    longest=[i,j,j-i+1]
        return s[longest[0]:longest[1]+1]
#mid expand:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:return ""
        length=len(s)
        if length==1:return s
        def expand(midleft,midright):
            if s[midleft]!=s[midright]:return (0,0,0)
            while midleft>=0 and midright<length:
                if s[midleft]==s[midright]:midleft,midright=midleft-1,midright+1
                else:break
            return (midright-midleft-1,midleft+1,midright-1)
        longest=[1,0,0]
        for i in range(1,length):
            temp1=expand(i,i)
            temp2=expand(i-1,i)
            longest=temp1 if temp1[0]>max(temp2[0],longest[0]) else \
            temp2 if temp2[0]>max(temp1[0],longest[0]) else longest
        return s[longest[1]:longest[2]+1]
