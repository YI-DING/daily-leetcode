def firstUniqChar(self, str):
    if not str:return ''
    dicc={}
    for i,char in enumerate(str):
        if char not in dicc:
            dicc[char]=[1,i]#times,position
        else:
            dicc[char][0]+=1
    first=len(str)
    for pair in dicc.values():
        if pair[0]==1:
            if pair[1]<first:
                first=pair[1]
    return str[first]