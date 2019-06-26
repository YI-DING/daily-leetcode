class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k==1:return([] if n>9 else [n])
        if k==2:
            if n<3 or n>17:return ([])
            else: 
                result=[]
                for i in range(1,n//2+1):
                    if i!=n-i:result.append([i,n-i])
                return (result)
        result=[]
        for i in range(1,n//k+1):#get the first number out
            #print(f'i is {i}, cand is {Solution.combinationSum3(self,k-1,n-i):}')
            for j in Solution.combinationSum3(self,k-1,n-i):
                if i not in j and len(set(j))==len(j) and max(j)<10:
                    j.append(i)
                    j.sort()
                    if j not in result:result.append(j)
        return result

'''class Solution:
    def combinationSum3(self, k, n):
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k-1, n-last, last)]
        return combs(k, n, 10)'''
'''class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]):
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res


    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return
        
        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()'''
'''def combinationSum3(self, k, n):
    res = []
    self.dfs(xrange(1,10), k, n, 0, [], res)
    return res
    
def dfs(self, nums, k, n, index, path, res):
    if k < 0 or n < 0: # backtracking 
        return 
    if k == 0 and n == 0: 
        res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)'''