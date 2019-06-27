class Solution:
    def isValid(self, s: str) -> bool:
            string=s
            while True:
                if not string:return True
                if len(string)==1:return False
                length=len(string)
                for i in range(1,length):
                    if string[i-1]+string[i] in {"()","{}","[]"}:
                        string=string[:i-1]+string[i+1:]
                        break
                if len(string)==length:return False 
#same idea but implememnted with stacks:
'''
    def isValid(self, s: str) -> bool:
        if not s:return True 
        stack=[]
        for item in s:
            if not stack or stack[len(stack)-1]+item not in {"()","{}","[]"}:stack.append(item)
            else:stack.pop()
        return True if not stack else False '''
