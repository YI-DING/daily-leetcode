from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList=set(wordList)
        queue = deque([beginWord])
        visited = set([beginWord])
        length = 1
        
        def change(word,lst):
            result = []
            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == word[i]:
                        continue
                    #print(word[:i]+letter+word[i+1:])
                    if (word[:i]+letter+word[i+1:]) in lst:
                        result.append(word[:i]+letter+word[i+1:])
            return result
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                visited.add(current)
                if current == endWord:
                    return length
                for word in change(current,wordList):
                    if word not in visited:
                        queue.append(word)
                        visited.add(word)
            length += 1
        return 0