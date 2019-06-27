class Solution:
    def combinationSum(self, candidates: List[int], target: int) :
        #print(f'now calculate Comb({candidates},{target})')
        if not candidates: return candidates
        if len(candidates)==1:
            if target==candidates[0]:return [candidates]
            if target%candidates[0]==0:return [[candidates[0] for i in range(target//candidates[0])]]
            return []
        #multiple candidates:
        result=[]
        for index,item in enumerate(candidates):
            #print(f'    result is {result},item is {item}')
            #if target%item==0:return [[item for i in range(target//item)]]
            for i in range(1,target//item+1):
                #print(f'        {i} {item}s to put,now calculate res.')
                if target==i*item:res=[[item for k in range(i)]]
                else:
                    res=self.combinationSum(candidates[index+1:],target-i*item)
                    #print(f'            res is {res}')
                    for ans in res:
                        for j in range(i):ans.insert(0,item)
                    #print(f'        res is {res} before appending to result')
                result.extend(res)
        return result

def combinationSum(self,candidates,target):
	res=[]
	candidates.sort()
	def dfs(target,index,path):
		if target<0:
			return 
		if target==0:
			res.append(path)
			return 
		for i in range(index,len(candidates)):
			dfs(target-candidates[i],i,path+[candidates[i]])
	dfs(target,0,[])
	return res