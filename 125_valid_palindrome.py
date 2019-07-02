class Solution:
    def isPalindrome(self, s: str):
        if not s:return True
        sett=set([chr(order) for order in range(97,123)]+[str(i) for i in range(10)])
        new=""
        for letter in s.lower():
            if letter in sett:
                new+=letter
        return True if new==new[::-1] else False
def isPalindrome(self, s: str):
	s=''.join(letter for letter in s if letter.isalnum()).lower()
	return s==[s::-1]

