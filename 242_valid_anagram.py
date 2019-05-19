class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        sDic={}
        tDic={}
        for n in s:
            if n in sDic:
                sDic[n]+=1
            else:sDic.update({n:1})
            #print(f'sDic is {sDic}')
        for n in t:
            if n in tDic:
                tDic[n]+=1
            else:tDic.update({n:1})
            #print(f'tDic is {tDic}')
        if tDic==sDic: return True
        else:return False