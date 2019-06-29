class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack==needle:return 0
        needle_length=len(needle)
        if len(haystack)<needle_length:return -1
        for i in range(len(haystack)-1):
            if haystack[i:i+needle_length]==needle:return i
        return -1