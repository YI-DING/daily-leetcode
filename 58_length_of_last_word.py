class Solution:
    def lengthOfLastWord(self, s: str) :
        return len(s.strip().split(" ").pop())
        #return len(s.strip().split(" ")[-1])