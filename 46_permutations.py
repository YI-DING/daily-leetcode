class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev_perm=[[]]
        for n in nums:
            new=[]
            for item in prev_perm:
                for i in range(len(item)+1):
                    new.append(item[:i]+[n]+item[i:])
            prev_perm=new
        return prev_perm
    
