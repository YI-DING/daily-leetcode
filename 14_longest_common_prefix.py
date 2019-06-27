class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs:return ""
        #if len(strs)==1:return strs[0]
        #result=""
        #sht=len(strs[0])
        #which=0
        #for i,string in enumerate(strs[1:]):
        #    if len(string)<sht:
        #        sht=len(string)
        #        which=i+1    
        shortest=min(strs,key=len) 
        strs.remove(shortest)
        #for index,character in enumerate(strs.pop(which)):
        for index,character in enumerate(shortest):
            for string in strs:
                #if string[index]!=character:return result
                if string[index]!=character:return shortest[:index]
            #result+=character
        return shortest