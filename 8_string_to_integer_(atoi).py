class Solution:
    def myAtoi(self, str: str):
        if not str:
            return 0
        numb,space_flag,sign="",False,False
        
        for letter in str:
            if letter == " ":
                if space_flag or numb or sign:
                    break
                else:
                    continue
            if letter in ("+","-"):
                if not sign and not numb:
                    sign=letter
                    continue
                else:
                    break
            if letter.isnumeric():
                numb+=letter
                continue
            break
            
        if not numb:
            return 0
        sign=1 if not sign or sign=="+" else -1 
        numb=int(numb)*sign
        
        if numb > 2**31-1:
            return 2**31-1
        elif numb< -2**31:
            return -2**31
        else:
            return numb
        