class Solution:
    def romanToInt(self, s: str):
        dicc1={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        dicc2={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        def cutt(s,numm):
            if not s:return numm
            if len(s)==1:return (numm+dicc2[s])
            if s[0:2] in dicc1:return cutt(s[2:],numm+dicc1[s[0:2]])
            return cutt(s[1:],numm+dicc2[s[0]])
        return cutt(s,0)