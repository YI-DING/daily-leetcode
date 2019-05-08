class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first make a dictionary of elements and its frequency:
        dic=dict()
        for number in nums:
            if number not in dic:
                dic.update({number:1})
            else:dic[number]+=1
        A=[]
        result=[]
        for key in dic:#store it in A 
            A.append([dic[key],key])
        n=len(A)
    
        def max_heapify(i):
            nonlocal A
            #print(f'we are heapifying the {i} th element. current A is {A}')
            n=len(A)
            if i<n//2:
                if 2*i+2>n-1:
                    if A[i][0]<A[2*i+1][0]:
                        temp=A[i]
                        A[i]=A[2*i+1]
                        A[2*i+1]=temp
                else:
                    maxi=max(A[i][0],A[2*i+1][0],A[2*i+2][0])
                    mini=min(A[i][0],A[2*i+1][0],A[2*i+2][0])
                    if not maxi==A[i][0]:
                        if maxi==A[2*i+1][0]:
                            temp=A[i]
                            A[i]=A[2*i+1]
                            A[2*i+1]=temp
                        else:
                            temp=A[i]
                            A[i]=A[2*i+2]
                            A[2*i+2]=temp
                        max_heapify(2*i+1)
                        max_heapify(2*i+2)
                                 
        def extract_max():
            nonlocal A
            #    print(f'We are extracting curent A as {A}')
            A[0]=A[len(A)-1]
            A=A[:len(A)-1]
            max_heapify(0)
            
        for i in range(n//2-1,-1,-1):
            max_heapify(i)
        for i in range(k):
            result.append(A[0][1])
            extract_max()
        return result