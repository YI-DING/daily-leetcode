class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        i = 0
        dicc = {}
        maxx = 0

        def get_max(dicc):
            return 0 if not dicc else max([val for val in dicc.values()])
        
        for j, letter in enumerate(s):
            if letter not in dicc:
                dicc[letter] = 1
            else:
                dicc[letter] += 1
            while j - i + 1 - get_max(dicc) > k:
                    dicc[s[i]] -= 1
                    i += 1
            maxx = max(maxx, j - i + 1)
        return maxx
#in other words, find longest A[i]~A[j] such that no more than K other chars inside
#case 1:if there are <= K others inside, increment j
#case 2:if > K others inside, increment i
#use dictionary to tell which one is the major letter