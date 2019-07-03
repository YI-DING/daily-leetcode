class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        visited,start,maxx={},0,0
        for i,letter in enumerate(s):
            if letter in visited and start<=visited[letter]:
                start=visited[letter]+1
            else:
                maxx=max(maxx,i-start+1)
            visited[letter]=i
        return maxx