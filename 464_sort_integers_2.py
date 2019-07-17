def sortIntegers2(self, A):
	if not A:
		return 

	def quicksort(A, start, end):
    	if start >= end:
    		return 
    	left, right = start, end
    	pivot = A[(start + end) // 2]
    	while left <= right:
    		while left <= right and A[left] < pivot :
    			left += 1
    		while left <= right and A[right] > pivot:
    			right -= 1
    		if left <= right:
    			A[left], A[right] = A[right], A[left]
    			left += 1
    			right -= 1
    	quicksort(A, start, right)
    	quicksort(A, left, end)
    	
	quicksort(A, 0 , len(A) - 1)





