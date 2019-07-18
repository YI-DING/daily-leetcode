class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        self.result = []
        def partition(A):
            start = 0
            #print(A)
            if not A:
                return
            end = len(A) - 1
            while end > 0:
                if A[end] == A[0]:
                    break
                else:
                    end -= 1
            if end == 0:
                self.result.append(1)
                return partition(A[1:])
            while True:
                dicc = {num : 0 for num in set(A[start:end]) if num != A[start]}
                if not dicc:
                    break
                for num in dicc:
                    ed = len(A) - 1
                    while ed > 0:
                        if A[ed] == num:
                            break
                        else:
                            ed -= 1
                    dicc[num] = ed
                #print(dicc)
                lower = max([bound for bound in dicc.values()])
                start = end
                end = lower if lower > end else end
                flag = False
                for char in A[start:end]:
                    if char not in dicc:
                        flag = True
                if flag:
                    continue
                else:
                    break
            self.result.append(end + 1)
            return partition(A[end+1:])
        partition(S)
        return self.result
#result after realizing adding a 26-char mapping of right most index:
#note that this is still constant space
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans