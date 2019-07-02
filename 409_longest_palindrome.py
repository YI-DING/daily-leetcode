class Solution:
    def longestPalindrome(self, s: str) :
        if not s:return 0
        dic={}
        for letter in s:
            if letter not in dic:
                dic[letter]=1
            else:
                dic[letter]+=1 
        odd_count=0
        for counts in dic.values():
            if counts%2==1:
                odd_count+=1
        return len(s)-(odd_count-1) if odd_count>0 else len(s)