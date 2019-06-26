#    return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))
class Solution:
    def titleToNumber(self, s: str) -> int:
        result=0
        leng=len(s)
        for i in range(leng-1,-1,-1):
            result+=(26**i)*(ord(s[leng-1-i])-64)
        return(result)