class Solution:
    def backspaceCompare(self, S: str, T: str):
        ends, endt = len(S) - 1, len(T) - 1
        sskip, tskip = 0, 0
        while ends >= 0 or endt >= 0:
            while ends >= 0:
                if S[ends] == "#":
                    ends -= 1
                    sskip += 1
                elif sskip > 0:
                    ends -= 1
                    sskip -= 1
                else:
                    break
            while endt >= 0:
                if T[endt] == "#":
                    endt -= 1
                    tskip += 1
                elif tskip > 0:
                    endt -= 1
                    tskip -= 1
                else:
                    break
            #either both of them are char or at least one of them is empty
            if ends < 0:
                if endt < 0:
                    return True
                return False
            if endt < 0:
                return False 
            if S[ends] == T[endt]:
                endt -= 1
                ends -= 1
            else:
                return False
        return True