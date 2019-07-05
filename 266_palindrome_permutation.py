def canPermutePalindrome(self, s):
    if not s or len(s) ==1: 
        return True
    dicc,odd_count={},0
    for char in s:
        if char not in dicc:
            dicc[char]=1
        else:
            dicc[char]+=1
    for value in dicc.values():
        if value%2 == 1:
            odd_count+=1
            if odd_count > 1:
                return False
    return True