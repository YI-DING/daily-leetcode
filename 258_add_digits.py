class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            st=str(num)
            num=sum(int(i) for i in st)
        return num
            