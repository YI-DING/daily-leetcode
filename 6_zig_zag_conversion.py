class Solution:
    def convert(self, s: str, numRows: int):
        if not s:
            return ""
        leng=len(s)
        if numRows >= leng or numRows == 1:
            return s
        result=""
        for row in range(1,numRows+1):
            index=row-1
            iterr=[2*numRows-2,2*numRows-2] if row in (1,numRows) else [2*(numRows-row),2*row-2]
            while index<leng:
                result+=s[index]
                index+=iterr[0]
                iterr.reverse()
        return result