class Solution:
    def binaryGap(self, N: int):
        pos = 0
        fast, slow = None, None
        max_dist = 0
        while N >= 1 << pos:
            if N & (1 << pos) != 0:
                if slow is None:
                    slow = pos
                elif fast is None:
                    fast = pos
                    max_dist = max(max_dist, fast - slow)
                else:
                    slow, fast = fast, pos
                    max_dist = max(max_dist, fast - slow)
            pos += 1
        return max_dist