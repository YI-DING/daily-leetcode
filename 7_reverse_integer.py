class Solution:
    def reverse(self, x: int) -> int:
        if 0<=x<10:return x
        x=str(x)
        head=""
        if x[0]=="-":
            head="-"
            x=x[1:]
        x=x[::-1]
        if x[0]=="0":return int(head+x[1:]) if -2**31<=int(head+x[1:])<=2**31-1 else 0
        else:return int(head+x) if -2**31<=int(head+x)<=2**31-1 else 0