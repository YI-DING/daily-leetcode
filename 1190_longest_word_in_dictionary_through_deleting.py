class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        #you can check all words or sort them and check til you found max        
        def deletion_works(word, string):
            if word == string:
                return True
            if len(word) > len(string) or not string:
                return False
            pt_word, pt_string = 0, 0
            while pt_string <= len(string) - 1:
                if pt_word == len(word):
                    return True
                if word[pt_word] == string[pt_string]:
                    pt_word += 1
                pt_string += 1
            return True if pt_word == len(word) else False
        
        d.sort(key = lambda word:(-len(word),word))
        for word in d:
            if deletion_works(word, s):
                return word
        return ""
#way better solution from @jiuzhang.com......:
    def findLongestWord(self, s, d):
        # write your code  here
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''